from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

from loguru import logger
from mcp.server.fastmcp import FastMCP
from newspaper import Article
import requests

# Compile regex patterns at module level
URL_PATTERN = re.compile(r"^https?://.+")

# HTTP headers
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0.0.0 Safari/537.36"
)

@dataclass(slots=True)
class ArticleData:
    """Structured article data."""

    title: str
    text: str
    author: str | None
    date: str | None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary format."""
        return {
            "title": self.title,
            "text": self.text,
            "author": self.author,
            "date": self.date,
        }


# Create the MCP server instance
app = FastMCP("news-scraper")


def validate_url(url: str) -> bool:
    """Validate if the provided string is a valid URL.
    
    Args:
        url: The URL string to validate.
        
    Returns:
        True if valid URL, False otherwise.
    """
    if not url or not isinstance(url, str):
        return False
    
    if not URL_PATTERN.match(url):
        return False
    
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


@app.tool()
def fetch_article(url: str) -> dict[str, Any]:
    """Fetch a news article by URL and return structured data.

    Args:
        url: The URL of the news article.

    Returns:
        A dict with keys: title, text, author, date.
        
    Raises:
        ValueError: If URL is invalid or article cannot be parsed.
        requests.RequestException: If HTTP request fails.
    """
    logger.info(f"Fetching article: {url}")
    
    # Validate URL
    if not validate_url(url):
        raise ValueError(f"Invalid URL provided: {url}")

    # Fetch page HTML using requests with custom User-Agent
    try:
        response = requests.get(url, timeout=15, headers={"User-Agent": USER_AGENT})
        response.raise_for_status()
        logger.debug(
            f"fetched status={response.status_code} content_length={len(response.content)}"
        )
    except requests.RequestException as exc:
        logger.error(f"Failed to fetch URL: {exc}")
        raise
    except Exception as exc:
        logger.error(f"Unexpected error fetching URL: {exc}")
        raise ValueError(f"Failed to fetch URL: {exc}")

    try:
        article = Article(url)
        article.set_html(response.text)
        article.parse()
    except Exception as exc:
        logger.error(f"Failed to parse article: {exc}")
        raise ValueError(f"Failed to parse article: {exc}")

    title: str = article.title or ""
    text: str = article.text or ""

    # newspaper3k can return a list of authors and a datetime
    author: str | None = None
    if article.authors:
        author = ", ".join(article.authors)

    date: str | None = None
    if article.publish_date:
        date = article.publish_date.isoformat()

    # Validate extracted content
    if not title.strip() and not text.strip():
        logger.warning("No content extracted from article")
        raise ValueError("No content could be extracted from the article")

    logger.debug(
        f"extracted title_length={len(title)} text_length={len(text)} author={author} date={date}"
    )

    article_data = ArticleData(
        title=title.strip(),
        text=text.strip(),
        author=author,
        date=date,
    )
    
    return article_data.to_dict()


if __name__ == "__main__":
    # Running as a CLI MCP server
    app.run()

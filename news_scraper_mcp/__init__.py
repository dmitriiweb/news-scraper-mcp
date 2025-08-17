"""News Scraper MCP server package."""

from .server import app, fetch_article, ArticleData

__version__ = "0.1.0"
__all__ = ["__version__", "app", "fetch_article", "ArticleData"]

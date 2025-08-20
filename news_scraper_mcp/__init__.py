"""News Scraper MCP server package."""

from .server import app, fetch_article, ArticleData

__version__ = "1.0.0"
__all__ = ("__version__", "app", "fetch_article", "ArticleData")

#!/usr/bin/env python3
"""Main entry point for the news scraper MCP server."""

from news_scraper_mcp.server import app


def main():
    """Run the MCP server."""
    app.run()


if __name__ == "__main__":
    main()

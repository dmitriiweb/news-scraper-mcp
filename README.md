# Article Scraper MCP

A Model Context Protocol (MCP) server that fetches article data from URLs using newspaper3k.

## Features

- Extract article title, text, author, and publication date
- Robust error handling and URL validation
- Structured data output
- Built with FastMCP for easy integration

## Installation

Install directly from PyPI:

```bash
uvx article-scraper-mcp
```

## Usage

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "article-scraper": {
      "command": "uvx",
      "args": ["article-scraper-mcp"]
    }
  }
}
```

## API

### `fetch_article(url: str) -> dict[str, Any]`

Fetches and parses a news article from the given URL.

**Parameters:**
- `url`: The URL of the news article to fetch

**Returns:**
A dictionary containing:
- `title`: Article title
- `text`: Article content text
- `author`: Author name(s) (may be None)
- `date`: Publication date in ISO format (may be None)

**Raises:**
- `ValueError`: If URL is invalid or article cannot be parsed
- `requests.RequestException`: If HTTP request fails

## Requirements

- Python 3.11+
- newspaper3k
- requests
- loguru
- mcp[cli]

## License

MIT

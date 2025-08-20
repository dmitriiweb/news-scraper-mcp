# Article Scraper MCP

A Model Context Protocol (MCP) server that fetches article data from URLs using newspaper3k.

## Features

- Extract article title, text, author, and publication date
- Robust error handling and URL validation
- Structured data output
- Built with FastMCP for easy integration

## Installation

This project uses `uv` for package management and is designed to be run locally from source:

```bash
# Clone the repository
git clone https://github.com/dmitriiweb/article-scraper-mcp.git
cd article-scraper-mcp

# Install dependencies
uv sync

# Install the package in development mode
uv pip install -e .
```

## Usage

### As an MCP Server

The article scraper can be used as an MCP server in various MCP clients:

#### Claude Desktop

1. Install the server locally:
```bash
# From the cloned repository directory
uv run mcp install .
```

2. The server will be available as "article-scraper" in Claude Desktop

#### Other MCP Clients

Run the server directly from the cloned repository:
```bash
# Using stdio transport (default)
uv run article-scraper-mcp

# Or directly with Python
uv run python main.py

# Or using the MCP development command
uv run mcp dev server.py
```

### Server Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "article-scraper": {
      "command": "uv",
      "args": ["run", "python", "main.py"],
      "cwd": "/path/to/your/cloned/article-scraper-mcp"
    }
  }
}
```

Or for development:
```json
{
  "mcpServers": {
    "article-scraper": {
      "command": "uv",
      "args": ["run", "mcp", "dev", "server.py"],
      "cwd": "/path/to/your/cloned/article-scraper-mcp"
    }
  }
}
```

## Development

```bash
# Install development dependencies
uv sync --dev

# Run tests (if available)
uv run pytest

# Format code
uv run black .
uv run isort .

# Lint code
uv run flake8 .

# Run in development mode with MCP
uv run mcp dev server.py
```

## Requirements

- Python 3.11+
- newspaper3k
- requests
- loguru
- mcp[cli]

## License

MIT

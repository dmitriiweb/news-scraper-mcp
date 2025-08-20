# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-01-17

### Added
- Initial release of article-scraper-mcp
- MCP server implementation using FastMCP
- Article extraction tool with newspaper3k
- Support for extracting title, text, author, and publication date
- URL validation and error handling
- Structured data output using ArticleData dataclass
- Comprehensive logging with loguru
- CLI entry point for running as MCP server

### Features
- `fetch_article` tool for extracting article data from URLs
- Robust error handling for network and parsing failures
- Content validation to ensure articles are properly extracted
- Support for international content (tested with Russian Habr articles)
- MCP server integration ready for Claude Desktop and other clients

### Technical
- Python 3.11+ compatibility
- Type hints throughout the codebase
- PEP 8 compliant code style
- Comprehensive documentation
- MIT license

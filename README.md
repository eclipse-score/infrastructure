# S-CORE Infrastructure Documentation

This repository contains the sources for the S-CORE infrastructure documentation.

The published documentation is available at:

- https://eclipse-score.github.io/infrastructure/

## How The Site Is Structured

The README intentionally stays short to avoid duplicating the actual documentation. Use the published site for content and this repository for source files, local preview, and contribution work.

## Contributing

Contribution guidance, documentation style, and detailed instructions for AI agents live in [CONTRIBUTING.md](CONTRIBUTING.md).

## Run MkDocs Locally

This repository uses `uv` for local toolchain management.

Install dependencies and start a live preview:

```bash
uv sync
uv run mkdocs serve
```

Build the site with strict checks:

```bash
uv run mkdocs build --strict
```

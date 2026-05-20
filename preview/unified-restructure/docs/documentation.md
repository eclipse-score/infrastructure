# Documentation

How documentation is written, built, and published in S-CORE repositories.

## Toolchain

S-CORE documentation sites use:

- **MkDocs** with the **readthedocs** theme
- **mermaid2** plugin for diagrams
- **uv** for Python dependency management

## Local Preview

Set up and preview documentation locally:

```bash
uv sync
uv run mkdocs serve
```

This starts a local development server with live reload.

## Strict Build

Before submitting changes, verify the build passes in strict mode:

```bash
uv run mkdocs build --strict
```

This catches broken links, missing references, and other issues that would fail in CI.

## Pre-commit

Install pre-commit hooks for automatic formatting and validation:

```bash
pre-commit install
```

## Style Guide

Follow the contribution guidelines in [CONTRIBUTING.md](https://github.com/eclipse-score/infrastructure/blob/dev/CONTRIBUTING.md) for documentation style and structure.

## Publishing

CI deploys documentation to GitHub Pages on merge to the main branch. No manual deployment steps are needed.

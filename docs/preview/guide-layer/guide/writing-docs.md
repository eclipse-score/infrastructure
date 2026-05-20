# Writing Documentation

## Toolchain

S-CORE documentation sites use:

- **MkDocs** with the ReadTheDocs theme
- **mermaid2** plugin for diagrams
- **uv** for Python dependency management

## Local Preview

```bash
uv sync
uv run mkdocs serve
```

This opens a live-reloading preview at `http://127.0.0.1:8000/`.

## Strict Build

```bash
uv run mkdocs build --strict
```

Catches broken links and invalid markup. This must pass before merging.

## Pre-commit

If the repository has pre-commit configured:

```bash
pre-commit install
```

Hooks may include checks like mindmap generation from chapter headings or other documentation-specific validations.

## Style Guide

See [CONTRIBUTING.md](https://github.com/eclipse-score/infrastructure/blob/dev/CONTRIBUTING.md) for documentation style conventions, cross-chapter formatting rules, and contribution guidelines.

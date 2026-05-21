# How to Write Documentation

## Toolchain

S-CORE documentation sites use:

- **MkDocs** with the ReadTheDocs theme
- **mermaid2** plugin for diagrams
- **uv** for Python dependency management

## Start a local preview

```bash
uv sync
uv run mkdocs serve
```

This opens a live-reloading preview at `http://127.0.0.1:8000/`.

## Run a strict build

```bash
uv run mkdocs build --strict
```

Catches broken links and invalid markup. This must pass before merging.

## Set up pre-commit

If the repository has pre-commit configured:

```bash
pre-commit install
```

Hooks may include checks like mindmap generation from chapter headings or other documentation-specific validations.

## Follow style conventions

See [CONTRIBUTING.md](https://github.com/eclipse-score/infrastructure/blob/dev/CONTRIBUTING.md) for documentation style conventions, cross-chapter formatting rules, and contribution guidelines.

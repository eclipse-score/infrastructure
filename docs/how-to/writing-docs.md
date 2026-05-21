# How to Write Documentation

## Toolchain

This site is built with the S-CORE [docs-as-code](https://github.com/eclipse-score/docs-as-code) toolchain:

- **Bazel** as the build system
- **Sphinx** with the **MyST** parser for Markdown support
- **pydata-sphinx-theme** with S-CORE branding via `score_layout`
- **Mermaid** and **PlantUML** for diagrams

## Start a local preview

```bash
bazel run //:live_preview
```

This opens a live-reloading preview in your browser.

## Run a validation build

```bash
bazel run //:docs_check
```

Catches broken links, orphaned pages, and invalid markup. This must pass before merging.

## Set up IDE support

```bash
bazel run //:ide_support
```

Creates a `.venv_docs` virtual environment that IDEs can use for autocompletion and linting of reStructuredText/MyST content.

## Set up pre-commit

```bash
pre-commit install
```

Hooks auto-update generated content such as the chapter mindmap and maturity status rollups.

## MyST Markdown syntax

Content is written in Markdown using [MyST](https://myst-parser.readthedocs.io/) extensions.

Admonitions use the colon-fence syntax:

````markdown
:::{tip} Optional title
Body text here.
:::
````

Mermaid diagrams use the directive syntax:

````markdown
```{mermaid}
graph LR
    A --> B
```
````

## Follow style conventions

See [CONTRIBUTING.md](https://github.com/eclipse-score/infrastructure/blob/dev/CONTRIBUTING.md) for documentation style conventions, cross-chapter formatting rules, and contribution guidelines.

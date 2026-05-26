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

## Add a new page

1. Create the file in the right quadrant directory (`docs/tutorials/`, `docs/how-to/`, `docs/reference/`, or `docs/explanation/`).

2. Add it to the section's toctree. For example, to add a how-to guide:

   ```markdown
   :::{toctree}
   :maxdepth: 1

   existing-guide
   your-new-guide
   :::
   ```

3. Add a link to it from the landing page (`docs/index.md`) in the matching section.

4. Run `bazel run //:docs_check` — pages without a toctree entry produce a build warning.

For explanation chapters, the filename follows the pattern `NN-topic-name.md` where `NN` is the chapter number. New chapters also need an entry in the mindmap section of `docs/explanation/index.md`, but that is regenerated automatically (see below).

## Update generated content

Two scripts auto-regenerate parts of the documentation. Both are also run by pre-commit hooks, so if you have pre-commit installed they run on every commit automatically.

### Chapter mindmap

`docs/explanation/index.md` contains a mindmap built from the chapter heading structure. Regenerate it after changing chapter headings or adding a chapter:

```bash
python3 scripts/generate_mindmap.py
```

### Status rollups

Section and chapter headings show an aggregate maturity status. These are rolled up from the leaf `###` headings by `aggregate_status.py`:

```bash
python3 scripts/aggregate_status.py
```

Run this after changing any leaf-level status marker. The script rewrites only the files where the rolled-up status changed.

## Update status markers

Status markers indicate maturity at the leaf section level (`###` headings). The aggregate markers on `##` and `#` headings are generated — do not edit them by hand.

| Marker | Meaning |
|---|---|
| 🟢 | Implemented and effective |
| 🟡 | Partially implemented or needs improvement |
| 🟠 | Exists but has significant problems |
| 🔴 | Not yet started or clearly missing |
| ⚪ | Not assessed |

Add or update a marker at the end of a `###` heading:

```markdown
### 4.1.1 C++ Test Frameworks 🟡
```

Then run `python3 scripts/aggregate_status.py` to propagate the change to parent headings. Verify the result in the chapter and in the mindmap.

## Follow style conventions

See [CONTRIBUTING.md](https://github.com/eclipse-score/infrastructure/blob/dev/CONTRIBUTING.md) for documentation style conventions, cross-chapter formatting rules, and contribution guidelines.

@CONTRIBUTING.md

# Repository

S-CORE infrastructure documentation site. Published at <https://eclipse-score.github.io/infrastructure/>.

This is a documentation-only repository — no application code, no tests beyond the docs build.

# Documentation Structure

The site uses the [Divio documentation system](https://docs.divio.com/documentation-system/) with four quadrants:

| Directory | Quadrant | Content type |
|---|---|---|
| `docs/tutorials/` | Tutorials | Step-by-step learning guides for newcomers |
| `docs/how-to/` | How-to Guides | Task-oriented recipes for practitioners |
| `docs/reference/` | Reference | Factual lookup material (repos, config, versions) |
| `docs/explanation/` | Explanation | Architecture, design rationale, maturity assessment |

The explanation quadrant contains the numbered landscape chapters (`01-source-code-infrastructure.md` through `10-infrastructure-operations.md`) plus an index page with an interactive mindmap.

`docs/index.md` is the landing page with a Divio grid, quadrant link lists, and team quick links.

## When editing documentation

Know which quadrant a change belongs in before making it:

- **Tutorials** teach through doing. They are sequential, follow a specific path, and end with a concrete result. Do not add reference material or architectural discussion here.
- **How-to guides** solve a specific problem. They assume the reader already has a working environment. Include concrete commands and config snippets. Do not explain why things work.
- **Reference** is lookup material. Tables, lists, exact values. No narrative.
- **Explanation** is the place for architecture, design decisions, tradeoffs, and maturity assessment. Prose-heavy, not step-oriented.

When a topic spans quadrants, write each piece for its quadrant's purpose and cross-link. Do not put a tutorial inside a how-to or reference material inside an explanation.

## Cross-chapter rules in the explanation quadrant

The explanation chapters have specific ownership rules for cross-cutting topics. Before editing a chapter, check CONTRIBUTING.md for which chapter canonically owns which topic. Write the main narrative in the canonical chapter and use brief perspective-specific summaries with links elsewhere.

# Build & Validation

```bash
bazel run //:docs           # build documentation
bazel run //:live_preview   # local preview with live reload
bazel run //:docs_check     # validation — must pass cleanly
bazel run //:ide_support    # create .venv_docs for IDE integration
```

A change is not complete until `bazel run //:docs_check` passes cleanly.

# Pre-commit Hooks

Two hooks auto-update generated content in the explanation quadrant:

- `aggregate-status` — rolls up subsection maturity markers (🟢🟡🟠🔴⚪) to section and chapter headings
- `generate-mindmap` — regenerates the chapter map in `docs/explanation/index.md` from chapter headings

If not using pre-commit, run manually:

```bash
python3 scripts/aggregate_status.py
python3 scripts/generate_mindmap.py
```

# Navigation

Navigation is defined by `toctree` directives in the section index files (`docs/tutorials/index.md`, `docs/how-to/index.md`, `docs/reference/index.md`, `docs/explanation/index.md`). The top-level `docs/index.md` includes a hidden toctree pointing to these four section indices.

When adding a new page, add it to the appropriate section's toctree. Pages without a toctree entry will cause build warnings.

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

Before writing anything, answer: **What is the reader trying to do right now?**

| Reader intent | Quadrant |
|---|---|
| "I am learning — walk me through it" | Tutorial |
| "I know what I want — tell me how" | How-to |
| "I need to look up a value or option" | Reference |
| "I want to understand why this works the way it does" | Explanation |

If the reader intent does not match the quadrant you are editing, move the content — do not add it anyway.

### Hard rules per quadrant

**Tutorials** (`docs/tutorials/`)
- Sequential steps from zero to a working result. Never assume prior knowledge beyond the stated prerequisites.
- ❌ No lookup tables — move to Reference
- ❌ No architecture explanations — move to Explanation
- ❌ No "assumes you already have X set up" — that is a How-to

**How-to guides** (`docs/how-to/`)
- One goal, concrete steps, done. Assumes a working environment.
- ❌ No concept introductions or "why this works" paragraphs — move to Explanation or link to Tutorial
- ❌ No lookup tables (option lists, feature matrices, version tables) — move to Reference
- ❌ No content that duplicates a Tutorial — replace with a one-sentence description and a link

**Reference** (`docs/reference/`)
- Dry, factual, lookup-only. Tables, exact values, flag lists.
- ❌ No narrative prose explaining motivation — move to Explanation
- ❌ No procedural steps — move to How-to

**Explanation** (`docs/explanation/`)
- Architecture, design decisions, tradeoffs, maturity assessment. Prose-heavy.
- ❌ No step-by-step instructions — move to How-to
- ❌ No exact configuration values as the primary content — those belong in Reference

### When a topic spans quadrants

Each quadrant develops its own treatment fully — do not stub out a quadrant just because another quadrant covers the same topic from a different angle. A topic can have a complete tutorial, a complete how-to, and complete reference material at the same time.

What to avoid is writing the *same content type* in two places: if a how-to and a tutorial both contain the same step-by-step instructions, one of them is wrong. Remove the duplicate, not the quadrant.

## Cross-chapter rules in the explanation quadrant

The explanation chapters have specific ownership rules for cross-cutting topics. Before editing a chapter, check CONTRIBUTING.md for which chapter canonically owns which topic. Write the main narrative in the canonical chapter and use brief perspective-specific summaries with links elsewhere.

# Build & Validation

```bash
bazel run //:docs           # build documentation
bazel run //:live_preview   # local preview with live reload
bazel run //:docs_check     # quick check during development
bazel run //:docs           # full build — required before commit
bazel run //:ide_support    # create .venv_docs for IDE integration
```

A change is not complete until `bazel run //:docs` passes cleanly.

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

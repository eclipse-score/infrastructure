# Contributing

This repository contains the source for the S-CORE infrastructure documentation. Contributions should improve clarity, keep the information architecture coherent, and make the documentation easier to use for both humans and tools.

## Working On The Documentation

Use the published site for content consumption and this repository for source edits, review, and validation.

For local work:

```bash
uv sync
uv run mkdocs serve
uv run mkdocs build --strict
```

A contribution is not complete until the documentation still builds cleanly with strict checks.

## Documentation Style

Prefer short prose over long bullet lists. Bullets are useful for genuinely list-shaped content such as commands, checklists, or grouped links, but explanatory sections should read like normal English.

When a topic spans multiple chapters, choose one canonical home for the end-to-end explanation. Other chapters should describe only their local perspective and link back to the canonical section instead of repeating the same narrative. This keeps the reader experience coherent and prevents drift between chapters.

Explain the mental model first, then the practical steps. Readers should understand what a thing is for before being asked to configure or operate it. When configuration is important, include a minimal concrete snippet rather than describing it abstractly.

Link to authoritative upstream documentation when it owns the procedure. Do not copy long release checklists or external workflows into this repository when a maintained upstream README or manual already exists. Instead, explain how that external source fits into the S-CORE infrastructure story.

Preserve the existing chapter structure unless there is a strong reason to change it. Adding a new top-level page or chapter is a last resort, not the default fix for a documentation problem.

## Cross-Chapter Topics

Cross-cutting topics are expected in this repository, but they should still feel unified to the reader.

- Put the main narrative in the chapter that best matches the topic's primary purpose.
- Let build-oriented chapters explain consumption and configuration.
- Let release and distribution chapters explain publication, discoverability, and user-facing flow.
- Let operations chapters explain service ownership, monitoring, and recovery.
- Use short cross-references instead of parallel explanations when a chapter only needs the topic from one angle.

The current reference example for this pattern is the Bazel registry writeup:

- [docs/08-artifact-distribution.md](docs/08-artifact-distribution.md) is the canonical end-to-end explanation.
- [docs/03-build-infrastructure.md](docs/03-build-infrastructure.md) keeps only the build-consumer perspective.
- [docs/10-infrastructure-operations.md](docs/10-infrastructure-operations.md) keeps only the operations perspective.

## Review Checklist

Before opening or merging a change, check the following:

- The main explanation lives in one place.
- Neighboring chapters do not repeat the same prose unnecessarily.
- Explanatory sections read as prose, not as bullet dumps.
- Configuration details are concrete and minimal.
- External procedures are linked, not copied.
- Links and navigation still work.
- `mkdocs build --strict` passes.

## Detailed Instructions For AI Agents

AI agents contributing to this repository should follow the same rules as human contributors, with extra care for structure and readability.

When editing documentation:

- Inspect neighboring chapters before rewriting a section so you understand where the topic should canonically live.
- Prefer rewriting bullet-heavy content into short prose paragraphs when the section is explanatory.
- For cross-cutting topics, write one complete explanation and convert the other locations into brief perspective-specific summaries with links.
- Do not create a new top-level page just to avoid making a chapter more readable.
- Include concrete snippets only when they directly help a contributor act, such as a `bazelrc` or command example.
- Prefer linking upstream source-of-truth documents over copying long procedures into this repository.
- Keep README content short; repo workflow belongs in `README.md`, while contribution and style guidance belongs here.
- Validate changes with `uv run mkdocs build --strict` when possible, and say so if verification could not be completed.

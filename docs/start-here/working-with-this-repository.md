# Working With This Repository

This repository is maintained as docs-as-code with Markdown and MkDocs.

## Local Workflow

1. Install the documentation toolchain:

```bash
uv sync
```

2. Start local preview:

```bash
uv run mkdocs serve
```

3. Validate before submitting changes:

```bash
uv run mkdocs build --strict
```

## Contribution Expectations

- keep content practical and neutral
- do not add unverified S-CORE claims
- keep pages linked to related guides, work packages, and platform areas
- update existing pages when possible instead of creating duplicates

## Documentation Patterns

- use [Platform Areas](../source/overview.md) for stable area context
- use [Guides](../guides/overview.md) for task-oriented instructions
- use [Work Ahead](../work-ahead/work-breakdown-structure.md) for roadmap and contribution visibility

## Useful Entry Points

- [Where to start](../overview/where-to-start.md)
- [Guides Overview](../guides/overview.md)
- [Current focus areas](../work-ahead/current-focus-areas.md)
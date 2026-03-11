# S-CORE Infrastructure Documentation

This repository contains the MkDocs-based documentation for the technical infrastructure that supports the S-CORE project.

The focus is not only end-user documentation. This site is also used as:

- an infrastructure overview for technical and non-technical stakeholders
- a development map for current state and remaining work
- a contribution map for infrastructure contributors
- a reference for architecture and cross-cutting infrastructure concerns

The infrastructure is still evolving. Some areas have strong foundations, while others are partially established or still being defined.

## What This Repository Documents

The documentation is organized around eight infrastructure areas:

- Source Code Infrastructure
- Build Infrastructure
- Integration Infrastructure
- Artifact Infrastructure
- Testing Infrastructure
- Security & Compliance Infrastructure
- Documentation Infrastructure
- Infrastructure Operations

## How The Site Is Structured

Top-level navigation is intentionally compact:

- Overview
- Infrastructure Development Map
- Infrastructure Areas
- Guides
- Architecture

The primary backbone is Infrastructure Areas. Development status, work packages, guides, and architecture pages are aligned to these areas.

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

## Where To Start Reading

- Start at `docs/index.md` for audience-specific entry points.
- Use `docs/infrastructure-development-map.md` for progress and work package overview.
- Open `docs/areas/<area>/index.md` when you work by infrastructure area.
- Use `docs/guides/index.md` for practical task-oriented instructions.

# S-CORE Infrastructure Documentation

This repository contains the infrastructure documentation for S-CORE.

It is a docs-as-code site built with Markdown and MkDocs. The goal is to provide practical guidance for engineers, contributors, managers, and compliance-oriented stakeholders.

## Documentation Structure

The documentation is organized around five navigation sections:

- `Start Here`: onboarding path and capability map
- `Work Ahead`: work breakdown structure, contribution map, and current focus areas
- `Platform Areas`: stable capability model used across the documentation
- `Guides`: task-oriented pages for common infrastructure work
- `Architecture`: platform model, tool landscape, and cross-cutting concerns

The platform areas are:

- Source Platform
- Build Platform
- CI/CD Platform
- Artifact Platform
- Testing Platform
- Security & Compliance Platform
- Documentation Platform
- Platform Operations

## Run MkDocs Locally

This repository uses `uv` to manage the MkDocs toolchain.

Install dependencies and start a local preview:

```bash
uv sync
uv run mkdocs serve
```

The local site will usually be available at `http://127.0.0.1:8000`.

To build the static site:

```bash
uv run mkdocs build --strict
```

## How To Contribute

- Keep changes practical and directly useful.
- Prefer task-oriented wording over abstract conceptual text.
- Add or update cross-links between platform areas, guides, and work packages.
- Mark evolving or incomplete details clearly; do not guess.
- Keep the capability model stable while allowing implementation details to evolve.

## Publishing

The site is published with GitHub Pages in workflow mode using the repository CI/CD setup.

## Reading Entry Points

- [Documentation Home](docs/index.md)
- [Start Here](docs/start-here/platform-overview.md)
- [Work Ahead](docs/work-ahead/work-breakdown-structure.md)
- [Guides Overview](docs/guides/overview.md)

If you work by area, start in the relevant overview page under `docs/<area>/overview.md`.

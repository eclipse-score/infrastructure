# S-CORE Infrastructure Documentation

This repository documents the technical infrastructure of the S-CORE project.

It is a docs-as-code repository built with Markdown and MkDocs. The goal is to provide a practical, maintainable reference for people who use, operate, and improve the infrastructure around source control, builds, CI/CD, testing, artifacts, security, compliance, and platform operations.

## What This Repository Covers

The documentation is organized as a platform capability map. Each major capability area has an overview page and supporting guides:

- Source Platform
- Build Platform
- CI/CD Platform
- Artifact Platform
- Testing Platform
- Security & Compliance Platform
- Documentation Platform
- Platform Operations

This structure is intended to help three audiences:

- Developers who need to understand how to work with the infrastructure
- Contributors who want to improve automation, tooling, and standards
- Managers and stakeholders who need an understandable overview of the platform landscape

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

## Publishing

The site is intended to be published with GitHub Pages in workflow mode.

The repository contains a GitHub Actions workflow that:

- builds the site with MkDocs
- uploads the generated `site/` directory as the GitHub Pages artifact
- deploys the site from the `main` branch

## How To Contribute

- Keep changes focused and practical.
- Prefer short, readable Markdown over formal document language.
- Update existing pages when improving a capability area instead of creating parallel documentation.
- Mark uncertain or evolving topics clearly instead of guessing.
- Treat the documentation as a living operational resource, not a one-time deliverable.

When contributing:

1. Make the smallest documentation change that improves clarity.
2. Add or update links so related pages stay connected.
3. Use neutral wording when a process or tool is still evolving.
4. Keep examples realistic and directly useful for onboarding or operational work.

## Where To Start Reading

Start with the main landing page and the platform model:

- [Documentation Home](docs/index.md)
- [Capability Map](docs/platform/capability-map.md)
- [Contribution Areas](docs/platform/contribution-areas.md)
- [Working Model](docs/platform/working-model.md)

If you are looking for a specific area, use the overview page for that capability first and then continue into the related guide pages.

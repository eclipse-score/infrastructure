# Documentation Tooling

Documentation tooling covers the formats, generators, and supporting conventions used to maintain infrastructure documentation.

## Scope

This includes:

- Markdown authoring
- MkDocs configuration for this repository
- local preview workflows
- conventions that keep documentation readable and maintainable

## Relevant Tools

- Markdown
- MkDocs
- uv for dependency and command management in this repository
- GitHub review workflows for docs-as-code changes

## Current Context

This repository is intentionally simple: Markdown content, a maintainable MkDocs configuration, a `uv`-managed Python toolchain, and normal repository review practices. The wider S-CORE project may also use other documentation tooling where needed, but this repository should stay focused on practical infrastructure documentation rather than tool sprawl.

## Typical Work Items

- improve navigation and page structure
- keep wording concise and technically useful
- add missing pages when a platform area lacks onboarding guidance
- remove duplication when the same explanation appears in multiple places

## Practical Principle

Documentation tooling should lower the cost of keeping content current. If the tooling makes small updates difficult, the documentation will drift.
# Source Code Infrastructure

## Short summary

Source Code Infrastructure covers how S-CORE repositories are structured, governed, and maintained in a multi-repository setup.

## Why this area matters in S-CORE

GitHub is the central collaboration platform for S-CORE. Consistent repository setup and governance are needed so contributors can work predictably across repositories and automation can be reused.

## Scope

- repository structure and baseline conventions
- contribution and review governance baseline
- repository metadata and ownership conventions
- organization and repository automation, including Otterdog usage

## Boundaries / what is not covered here

- application-specific source code architecture
- build graph design and dependency modeling
- CI workflow orchestration details

## Main tools and technologies

- GitHub organization and repository features
- Otterdog for organization and repository automation
- CODEOWNERS and repository-level policy settings

## Current state

Foundations are in place. Baseline standards are documented and partially automated, but consistency is still uneven across repositories.

## Key work packages

- standardize repository baseline files and metadata
- expand policy automation coverage and exception documentation
- improve repository lifecycle guidance from onboarding to archival
- make ownership and review paths more explicit

## How contributors can help

- improve reusable repository setup patterns
- document current repository practices where implicit
- improve policy exception transparency
- reduce manual repository setup steps

## Related guides

- [Repository onboarding](../../guides/repository-onboarding.md)
- [Repository policies](../../guides/repository-policies.md)

## Related architecture pages

- [Infrastructure model](../../architecture/infrastructure-model.md)
- [Tool landscape](../../architecture/tool-landscape.md)
- [Cross-cutting concerns](../../architecture/cross-cutting-concerns.md)

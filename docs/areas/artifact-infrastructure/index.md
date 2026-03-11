# Artifact Infrastructure

## Short summary

Artifact Infrastructure defines how reusable outputs are versioned, stored, promoted, and distributed in S-CORE.

## Why this area matters in S-CORE

Reusable outputs are needed across repositories and workflows. Clear artifact handling supports reliable reuse, traceability, and safer downstream decisions.

## Scope

- artifact storage and retention expectations
- artifact lifecycle and promotion stages
- artifact versioning and metadata baseline
- distribution channels, including Bazel registry usage

## Boundaries / what is not covered here

- build target design and dependency modeling
- full release management governance
- security triage process ownership

## Main tools and technologies

- Bazel registry
- GitHub Actions-based publishing workflows
- repository release features where applicable

## Current state

Artifact handling is fragmented and evolving. Publication exists in parts, but lifecycle and retention rules are not yet systematically defined.

## Key work packages

- define shared artifact lifecycle stages
- define storage and retention baselines
- clarify versioning and metadata expectations
- improve distribution documentation for consumers

## How contributors can help

- help define artifact lifecycle rules
- improve publication workflow documentation
- improve compatibility notes for artifact consumers
- reduce manual publication steps

## Related guides

- [Artifact publishing](../../guides/artifact-publishing.md)
- [Bazel and dependencies](../../guides/bazel-and-dependencies.md)

## Related architecture pages

- [Infrastructure model](../../architecture/infrastructure-model.md)
- [Tool landscape](../../architecture/tool-landscape.md)
- [Cross-cutting concerns](../../architecture/cross-cutting-concerns.md)

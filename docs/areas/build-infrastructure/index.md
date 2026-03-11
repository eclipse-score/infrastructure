# Build Infrastructure

## Short summary

Build Infrastructure defines how S-CORE builds are executed and how dependencies are managed with reproducibility in mind.

## Why this area matters in S-CORE

Bazel is a central build technology in S-CORE. Build consistency affects integration stability, artifact quality, and compliance-related traceability.

## Scope

- Bazel build baseline and shared conventions
- dependency management with Bzlmod
- Bazel registry integration for reusable components
- build diagnostics and reproducibility improvements

## Boundaries / what is not covered here

- repository-specific functional design of build targets
- CI pipeline ownership and workflow orchestration
- artifact retention policy decisions

## Main tools and technologies

- Bazel
- Bzlmod
- Bazel registry

## Current state

Build foundations are in place and actively used. Dependency governance and cross-repository consistency are still under active development.

## Key work packages

- align Bazel baseline conventions across repositories
- improve Bzlmod module onboarding and governance
- strengthen build diagnostics and performance visibility
- reduce drift between local and CI build behavior

## How contributors can help

- improve Bazel module onboarding documentation
- add practical examples for common dependency scenarios
- improve reproducibility checks in workflows
- document known build constraints and trade-offs

## Related guides

- [Bazel and dependencies](../../guides/bazel-and-dependencies.md)
- [Artifact publishing](../../guides/artifact-publishing.md)

## Related architecture pages

- [Infrastructure model](../../architecture/infrastructure-model.md)
- [Tool landscape](../../architecture/tool-landscape.md)
- [Cross-cutting concerns](../../architecture/cross-cutting-concerns.md)

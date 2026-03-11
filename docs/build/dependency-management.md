# Dependency Management

Dependency management covers how build-time and module-level dependencies are declared, resolved, updated, and reviewed.

## Scope

This includes:

- Bazel module declarations
- Bzlmod usage patterns
- registry-based dependency resolution
- consistency of dependency versions across repositories
- review and update processes for dependency changes

## Relevant Tools

- Bzlmod
- Bazel registry infrastructure
- repository-level module configuration

## Current Context

The S-CORE infrastructure landscape includes a Bazel registry and Bzlmod-related workflows. Public repositories also indicate that module and toolchain management are important parts of the wider setup. The exact publication and update flow should be documented based on verified implementation details as that process matures.

## Typical Work Items

- explain how repositories consume shared Bazel modules
- document when dependencies come from a registry versus local overrides
- make dependency update paths understandable for contributors
- reduce inconsistent dependency handling between repositories
- connect dependency choices to reproducibility and auditability goals

## Typical Questions

- Which dependencies are centrally curated?
- How are new modules added to the registry?
- How are breaking dependency changes introduced safely?
- What information should accompany a dependency update for review?

## Practical Guidance

Dependency management documentation should make it easy to answer two questions: where a dependency comes from, and how confidently it can be updated. Those answers matter for developer productivity, but also for traceability and compliance-related activities such as license review and vulnerability response.
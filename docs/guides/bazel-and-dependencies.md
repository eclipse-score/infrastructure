# Bazel And Dependencies

Use this guide when working on build behavior, Bzlmod, or dependency-related workflows.

## Goal

Keep Bazel-based builds reproducible and dependencies understandable across repositories.

## Steps

1. Identify whether your change affects local build behavior, integration behavior, or both.
2. Update Bazel and Bzlmod configuration with clear intent.
3. Check dependency source and versioning expectations.
4. Validate in local build and integration workflows.
5. Document cross-repository impact and follow-up work.

## Practical Checks

- dependency source is explicit
- module version decisions are documented
- build behavior remains consistent between local and automated execution
- changes are reflected in related area and planning pages

## Related Infrastructure Areas

- [Build Infrastructure](../areas/build-infrastructure/index.md)
- [Artifact Infrastructure](../areas/artifact-infrastructure/index.md)

## Related Planning Pages

- [Infrastructure Development Map](../infrastructure-development-map.md)
- [Work Breakdown Structure](../work-breakdown-structure.md)

## Background Detail

- [Build system](../build/build-system.md)
- [Dependency management](../build/dependency-management.md)
- [Build performance](../build/build-performance.md)

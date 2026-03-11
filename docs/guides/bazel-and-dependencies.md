# Bazel And Dependencies

Use this guide when working on build behavior, Bzlmod, or dependency-related workflows.

## Goal

Keep Bazel-based builds reproducible and dependencies understandable across repositories.

## Steps

1. Identify whether your change affects local build behavior, CI behavior, or both.
2. Update Bazel and Bzlmod configuration with clear intent.
3. Check dependency source and versioning expectations.
4. Validate in local build and CI.
5. Document cross-repository impact and follow-up work.

## Practical Checks

- dependency source is explicit
- module version decisions are documented
- build behavior remains consistent between local and CI execution
- changes are reflected in relevant guide and area pages

## Related Pages

- [Build Platform](../build/overview.md)
- [Artifact publishing](artifact-publishing.md)
- [Build Platform work packages](../work-ahead/work-breakdown-structure.md#wbs-build)
- Background detail: [Build system](../build/build-system.md), [Dependency management](../build/dependency-management.md), and [Build performance](../build/build-performance.md)
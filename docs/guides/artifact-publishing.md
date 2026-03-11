# Artifact Publishing

Use this guide when defining how outputs are published for downstream consumption.

## Goal

Make artifact storage, versioning, and distribution clear and traceable.

## Steps

1. Classify outputs as temporary CI artifacts or reusable published artifacts.
2. Define versioning and metadata expectations.
3. Select supported distribution channel.
4. Document retention and deprecation expectations.
5. Link publication flow to build and CI workflows.

## Practical Checks

- publication channel is explicit
- consumer usage is documented
- versioning expectations are visible
- lifecycle behavior is clear

## Related Pages

- [Artifact Platform](../artifacts/overview.md)
- [Bazel and dependencies](bazel-and-dependencies.md)
- [Artifact Platform work packages](../work-ahead/work-breakdown-structure.md#wbs-artifacts)
- Background detail: [Artifact storage](../artifacts/artifact-storage.md), [Artifact lifecycle](../artifacts/artifact-lifecycle.md), and [Artifact distribution](../artifacts/artifact-distribution.md)
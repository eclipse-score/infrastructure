# Build Performance

Build performance is about keeping local and CI builds fast enough to support normal development without undermining correctness or reproducibility.

## Scope

This topic includes:

- reducing avoidable rebuilds
- improving cache effectiveness
- identifying expensive targets or dependencies
- understanding where CI build time is spent
- deciding which optimizations are worth standardizing

## Relevant Tools

- Bazel profiling and build analysis tools
- CI timing data from GitHub Actions
- cache and dependency analysis techniques

## Current Context

Because Bazel is a central build technology, performance issues are often structural rather than local. Build graph design, dependency shape, cache behavior, and test placement can all affect developer feedback time.

Some optimization approaches, such as more advanced cache or execution strategies, may evolve over time. They should be documented when they become part of the supported platform rather than treated as assumptions.

## Typical Work Items

- document the largest known build-time drivers
- identify duplicated or unnecessary CI build steps
- improve cache use in reusable workflows
- set expectations for what should be optimized centrally versus locally

## Why It Matters

Slow builds reduce iteration speed and make shared infrastructure harder to trust. At the same time, performance work should not compromise the qualities that matter elsewhere in the platform, especially reproducibility, transparency, and reliable automation.
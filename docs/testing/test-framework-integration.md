# Test Framework Integration

Test framework integration describes how test tools are connected to the wider build and CI platform.

## Scope

This topic includes:

- integration of `pytest` and other frameworks with Bazel-based workflows
- shared conventions for defining and invoking tests
- repository-specific adapters that still need to fit the platform model

## Relevant Tools

- Bazel test targets
- pytest
- CI workflow definitions that execute or aggregate test stages

## Current Context

The testing landscape in S-CORE includes both Bazel-native execution and framework-level tooling such as `pytest`. The infrastructure task is not to force every repository into the same internal test design, but to ensure that different frameworks still fit into a coherent execution and reporting model.

## Typical Work Items

- document how framework-specific tests are exposed to Bazel or CI
- reduce special-case integration logic that is hard to maintain
- make test entry points understandable for new contributors
- align test integration with reproducibility and consistent automation

## Why It Matters

Poor framework integration creates fragile CI, duplicate setup logic, and inconsistent local developer experience. Good integration makes it easier to add new tests without redesigning the delivery pipeline.
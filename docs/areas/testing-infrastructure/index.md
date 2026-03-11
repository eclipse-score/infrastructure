# Testing Infrastructure

## Short summary

Testing Infrastructure describes how tests are executed, integrated, and reported across local and automated S-CORE workflows.

## Why this area matters in S-CORE

Reliable test feedback is required for safe and efficient integration in a multi-repository environment.

## Scope

- baseline expectations for local and CI test execution
- test framework integration with build and integration workflows
- test reporting quality and diagnostics
- handling strategies for expensive or unstable tests

## Boundaries / what is not covered here

- feature-level test design decisions inside application repositories
- integration workflow ownership and runner operations
- security/compliance policy ownership

## Main tools and technologies

- Bazel test
- framework-specific tooling such as pytest where used
- GitHub Actions workflows for automated execution and reporting

## Current state

Baseline execution is available, but integration patterns and reporting quality are still uneven. This area is under active development.

## Key work packages

- align local and CI test expectations
- improve test framework integration patterns
- improve reporting clarity and diagnostic usefulness
- define handling baseline for unstable or long-running tests

## How contributors can help

- strengthen test reporting outputs
- document current test execution practices
- improve reusable testing workflow steps
- reduce unclear failure modes in CI feedback

## Related guides

- [Testing and reporting](../../guides/testing-and-reporting.md)
- [CI workflows](../../guides/cicd-workflows.md)

## Related architecture pages

- [Infrastructure model](../../architecture/infrastructure-model.md)
- [Tool landscape](../../architecture/tool-landscape.md)
- [Cross-cutting concerns](../../architecture/cross-cutting-concerns.md)

# Testing Platform

## Purpose

Provide reliable test execution and reporting across local and CI workflows.

## Why It Matters In S-CORE

Testing integrates Bazel-based workflows, framework-specific test execution, and CI feedback loops. Predictable testing is necessary for safe integration and delivery in a multi-repository environment.

## Main Tools

- Bazel test
- pytest and related framework tooling
- GitHub Actions test execution workflows

## Scope

- local and CI test execution expectations
- framework integration into shared workflows
- reporting quality and failure diagnostics
- handling of expensive or unstable tests

## Boundaries

- does not define application-specific test case design
- does not replace CI/CD workflow architecture ownership
- does not replace security/compliance verification requirements

## Common Work Topics

- aligning local and CI validation expectations
- improving framework integration consistency
- making test failures actionable
- improving reporting coverage and quality

## Related Guides

- [Testing and reporting](../guides/testing-and-reporting.md)
- [CI/CD workflows](../guides/cicd-workflows.md)

## Related Work Packages

- [Testing Platform work packages](../work-ahead/work-breakdown-structure.md#wbs-testing)

## Related Platform Areas

- [Build Platform](../build/overview.md)
- [CI/CD Platform](../cicd/overview.md)
- [Platform Operations](../operations/overview.md)
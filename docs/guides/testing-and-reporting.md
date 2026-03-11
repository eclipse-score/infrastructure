# Testing And Reporting

Use this guide when changing test execution, framework integration, or reporting behavior.

## Goal

Keep test feedback reliable and actionable in local and CI workflows.

## Steps

1. Define which tests are expected locally and in CI.
2. Align framework integration with build and workflow conventions.
3. Ensure failures are clear and diagnosable.
4. Capture reporting outputs needed by contributors and maintainers.
5. Document scope and known limitations.

## Practical Checks

- test entry points are clear
- CI and local expectations are aligned
- reporting makes failures actionable
- expensive or unstable tests have explicit handling

## Related Pages

- [Testing Platform](../testing/overview.md)
- [CI/CD workflows](cicd-workflows.md)
- [Testing Platform work packages](../work-ahead/work-breakdown-structure.md#wbs-testing)
- Background detail: [Test execution](../testing/test-execution.md), [Test framework integration](../testing/test-framework-integration.md), and [Test reporting](../testing/test-reporting.md)
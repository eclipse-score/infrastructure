# CI/CD Workflows

Use this guide when adding or changing CI/CD workflows.

## Goal

Use reusable workflows and runner choices consistently so validation is predictable across repositories.

## Steps

1. Start from existing reusable workflow patterns.
2. Define required validation stages for your repository context.
3. Select runner type based on workload and execution constraints.
4. Keep workflow outputs clear for developers and maintainers.
5. Document the change and link related work packages.

## Practical Checks

- reusable workflow usage is preferred over duplicated YAML
- runner choice is explicit and justified
- failure output is actionable
- pipeline behavior is documented for contributors

## Related Pages

- [CI/CD Platform](../cicd/overview.md)
- [Testing and reporting](testing-and-reporting.md)
- [CI/CD Platform work packages](../work-ahead/work-breakdown-structure.md#wbs-cicd)
- Background detail: [Pipeline architecture](../cicd/pipeline-architecture.md), [Execution infrastructure](../cicd/execution-infrastructure.md), and [Pipeline optimization](../cicd/pipeline-optimization.md)
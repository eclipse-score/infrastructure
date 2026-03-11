# CI Workflows

Use this guide when adding or changing integration workflows.

## Goal

Use reusable workflows and runner choices consistently so pull request validation is predictable across repositories.

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

## Related Infrastructure Areas

- [Integration Infrastructure](../areas/integration-infrastructure/index.md)
- [Testing Infrastructure](../areas/testing-infrastructure/index.md)

## Related Planning Pages

- [Infrastructure Development Map](../infrastructure-development-map.md)
- [Work Breakdown Structure](../work-breakdown-structure.md)

## Background Detail

- [Pipeline architecture](../cicd/pipeline-architecture.md)
- [Execution infrastructure](../cicd/execution-infrastructure.md)
- [Pipeline optimization](../cicd/pipeline-optimization.md)

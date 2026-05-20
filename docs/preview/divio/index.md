# S-CORE Infrastructure Documentation

This site organizes S-CORE infrastructure documentation using four distinct content types, each serving a different reader need.

## Documentation Map

| | **Learning** | **Working** |
|---|---|---|
| **Practical** | [Tutorials](tutorials/getting-started.md) | [How-to Guides](how-to/building.md) |
| **Theoretical** | [Explanation](explanation/01-source-code-infrastructure.md) | [Reference](reference/quick-reference.md) |

## Tutorials

Step-by-step lessons for newcomers. Follow along to build understanding.

- [Getting Started](tutorials/getting-started.md) — Set up your environment and run your first build
- [Your First Pull Request](tutorials/first-pull-request.md) — From fork to merged PR, end to end
- [Creating a New Module](tutorials/creating-a-module.md) — Start a new Bazel module from the template

## How-to Guides

Practical recipes for specific tasks. Assumes you already have a working environment.

- [Building with Bazel](how-to/building.md) — Registry, dependencies, toolchains, lock files
- [Testing](how-to/testing.md) — Test frameworks, coverage, sanitizers
- [Code Quality](how-to/code-quality.md) — Pre-commit, lint policies, copyright headers
- [Publishing Modules](how-to/publishing.md) — Release, registry import, consumer access
- [Writing Documentation](how-to/writing-docs.md) — MkDocs setup, local preview, strict builds

## Reference

Factual lookup material. No narrative, just the data you need.

- [Quick Reference](reference/quick-reference.md) — Repositories, commands, links
- [Configuration Reference](reference/configuration.md) — .bazelrc, pre-commit, devcontainer settings
- [CI & Workflow Reference](reference/ci-workflows.md) — Reusable workflow inputs, outputs, and secrets
- [Tool Versions](reference/tool-versions.md) — Version matrix for shared toolchains and images

## Explanation

Architecture, design rationale, and maturity assessment of each infrastructure area.

- [1. Source Code Infrastructure](explanation/01-source-code-infrastructure.md)
- [2. Developer Environment](explanation/02-developer-environment.md)
- [3. Build & Dependencies](explanation/03-build-infrastructure.md)
- [4. Testing](explanation/04-testing-infrastructure.md)
- [5. Code Analysis Infrastructure](explanation/05-static-analysis-infrastructure.md)
- [6. Compliance & Dependency Analysis](explanation/06-compliance-infrastructure.md)
- [7. Automation & CI](explanation/07-automation-integration.md)
- [8. Release & Distribution](explanation/08-artifact-distribution.md)
- [9. Documentation & Traceability](explanation/09-documentation-infrastructure.md)
- [10. Infrastructure Operations](explanation/10-infrastructure-operations.md)

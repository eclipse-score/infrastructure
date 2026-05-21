# CI & Workflow Reference

## Platform

S-CORE uses **GitHub Actions** for all CI/CD automation.

## Reusable Workflows

Shared workflows are maintained in [eclipse-score/tooling](https://github.com/eclipse-score/tooling). Module repositories call these workflows to avoid duplicating CI logic.

| Workflow | Purpose |
|---|---|
| Build & Test | Bazel build and test for all targets |
| Pre-commit | Run pre-commit checks |
| Documentation | Build and validate MkDocs sites |
| Registry Publish | Import released module into Bazel registry |

## Runner Infrastructure

| Runner type | Environment | Use case |
|---|---|---|
| GitHub-hosted | Ubuntu (latest) | Standard builds, tests, pre-commit |
| Self-hosted (Linux) | Custom image | Builds requiring specific toolchains or large resources |
| Self-hosted (QNX) | QNX target | Hardware-in-the-loop and target-specific tests |

## PR Checks

Every pull request triggers:

1. **Pre-commit hooks** — formatting, headers, lock files
2. **Bazel build** — full build of all targets
3. **Bazel test** — full test suite execution
4. **Documentation build** — strict MkDocs build (if docs are present)

All checks must pass before merge.

## Secrets

CI secrets are managed at the GitHub organization level. Repository-level secrets are avoided where possible. See [Explanation: Automation & CI](../explanation/07-automation-integration.md) for the security model.

## Cross-Repository Integration

The [reference_integration](https://github.com/eclipse-score/reference_integration) repository tests cross-module compatibility by building and testing a combined workspace of multiple S-CORE modules.

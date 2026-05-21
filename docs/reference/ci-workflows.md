# CI & Workflow Reference

## Platform

S-CORE uses **GitHub Actions** for all CI/CD automation.

## Reusable Workflows

Shared reusable workflows are maintained in [eclipse-score/cicd-workflows](https://github.com/eclipse-score/cicd-workflows). Module repositories call these workflows to avoid duplicating CI logic. The available workflows cover building, testing, formatting, copyright, lock file checks, documentation, static analysis, CodeQL, license scanning, coverage, QNX cross-compilation, and template synchronization. Two meta-workflows — `on-pr.yml` and `daily.yml` — compose these checks into standard pipeline shapes for pull requests and scheduled maintenance respectively.

Shared composite actions are maintained in [eclipse-score/cicd-actions](https://github.com/eclipse-score/cicd-actions) for cross-repository token provisioning and QNX SDP setup.

## Runner Infrastructure

| Runner type | Environment | Use case |
|---|---|---|
| GitHub-hosted | Ubuntu (latest) | Standard builds, tests, pre-commit |
| Self-hosted (Linux) | Custom image | Builds requiring specific toolchains or large resources |
| Self-hosted (QNX) | QNX target | Hardware-in-the-loop and target-specific tests |

## PR Checks

The `on-pr.yml` meta-workflow triggers checks on every pull request. A typical PR runs:

1. **Formatting** — code style enforcement
2. **Copyright** — header presence
3. **Lock file check** — `MODULE.bazel.lock` freshness
4. **Build and test** — full Bazel build and test suite
5. **Documentation** — Bazel docs-as-code build (if docs are present)
6. **Static analysis** — linters and analyzers

All checks must pass before merge. Required status checks are configured centrally via [otterdog](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet).

## Secrets

CI secrets are managed at the GitHub organization level. Repository-level secrets are avoided where possible. See [Explanation: Automation & CI](../explanation/07-automation-integration.md) for the security model.

## Test Execution in CI

ITF tests run as ordinary `bazel test` targets. Docker-based ITF tests work on standard GitHub-hosted runners. QEMU-based ITF tests and QNX unit tests require runners with QEMU installed and KVM access (typically self-hosted).

| Test type | Runner requirement | Notes |
|---|---|---|
| Unit tests (C++, Rust, Python) | GitHub-hosted | Standard `bazel test` |
| ITF Docker tests | GitHub-hosted | Requires Docker |
| ITF QEMU tests | Self-hosted (QEMU + KVM) | Needs QEMU images in `data` |
| QNX unit tests | Self-hosted (QEMU + KVM) | Needs QNX SDP credentials |

## Cross-Repository Integration

The [reference_integration](https://github.com/eclipse-score/reference_integration) repository tests cross-module compatibility by building and testing a combined workspace of multiple S-CORE modules.

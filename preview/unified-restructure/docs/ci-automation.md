# CI & Automation

How continuous integration works across S-CORE repositories.

## Platform

All S-CORE repositories use **GitHub Actions** for CI. Workflow definitions live in `.github/workflows/` within each repository.

## Runners

CI runs on GitHub-hosted cloud runners with multiple architectures:

- **x86** -- standard Linux runners
- **ARM** -- ARM-based Linux runners
- **QEMU with KVM** -- for emulated target testing

## Devcontainer in CI

CI workflows use the same [devcontainer](https://github.com/eclipse-score/devcontainer) image (`ghcr.io/eclipse-score/devcontainer`) as local development. This ensures that the tool versions, compilers, and formatters in CI match exactly what developers use locally.

## Reusable Workflows

Central reusable workflows exist for common CI patterns (build, test, lint). Individual repositories call these workflows rather than duplicating pipeline logic.

## Required Checks

Required status checks are configured centrally via [Otterdog](https://otterdog.readthedocs.io/) in the [S-CORE configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet). This ensures consistent merge requirements across all repositories.

## Dependency Updates

Automated dependency management keeps repositories up to date:

- **Dependabot** -- opens pull requests to bump dependency versions and SHA hashes
- **Renovate** -- provides additional version update automation

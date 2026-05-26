# How-to Guides

Practical recipes for specific tasks. Assumes you already have a working environment.

## Module development

- [Building with Bazel](building.md) — Registry, dependencies, toolchains, lock files
- [Testing](testing.md) — Test frameworks, coverage, sanitizers, QNX
- [Code Quality](code-quality.md) — Pre-commit, lint policies, copyright headers
- [Publishing Modules](publishing.md) — Release, registry import, consumer access
- [Writing Documentation](writing-docs.md) — Bazel + Sphinx/MyST setup, local preview, validation

## Infrastructure development

- [Update the Devcontainer](update-devcontainer.md) — Build, publish, and roll out a new shared image
- [Manage CI Secrets](manage-ci-secrets.md) — Create, rotate, and replace secrets with OIDC
- [Update a Shared Toolchain](update-toolchain.md) — Bump compiler or policy versions across repositories

:::{toctree}
:maxdepth: 1
:hidden:

building
testing
code-quality
publishing
writing-docs
update-devcontainer
manage-ci-secrets
update-toolchain
:::

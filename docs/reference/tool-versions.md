# Tool Versions

## Devcontainer Image

Image: `ghcr.io/eclipse-score/devcontainer`

The devcontainer image is the canonical source for tool versions. Check the image's Dockerfile and release tags in [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) for the current version matrix.

## Toolchain Repositories

| Component | Repository | What it provides |
|---|---|---|
| C++ toolchain | [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) | GCC/Clang for Linux, QNX cross-compiler |
| GCC toolchain | [toolchains_gcc](https://github.com/eclipse-score/toolchains_gcc) | Bazel toolchains for GNU GCC |
| QNX toolchain | [toolchains_qnx](https://github.com/eclipse-score/toolchains_qnx) | Bazel toolchains for QNX |
| Rust toolchain | [toolchains_rust](https://github.com/eclipse-score/toolchains_rust) | Rust stable, Ferrocene (safety-qualified) |
| Ferrocene builder | [ferrocene_toolchain_builder](https://github.com/eclipse-score/ferrocene_toolchain_builder) | Builder for Ferrocene artifacts |
| C++ policies | [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) | Warning levels, sanitizers, constraint targets |
| Rust policies | [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) | Clippy rules, rustfmt configuration |
| Integration Test Framework | [itf](https://github.com/eclipse-score/itf) | pytest-based target testing (Docker, QEMU, hardware) |
| QNX unit test runner | [qnx_unit_tests](https://github.com/eclipse-score/qnx_unit_tests) | QEMU microvm test execution for QNX 8 |

## CI/CD Components

| Component | Repository | What it provides |
|---|---|---|
| Reusable workflows | [cicd-workflows](https://github.com/eclipse-score/cicd-workflows) | Shared GitHub Actions workflows (on-pr, daily, tests, coverage, etc.) |
| Reusable actions | [cicd-actions](https://github.com/eclipse-score/cicd-actions) | Composite actions (inter-repo-access, setup-qnx-sdp) |
| Docs-as-code | [docs-as-code](https://github.com/eclipse-score/docs-as-code) | Documentation build tooling (Sphinx extensions, traceability) |

## Build System

| Tool | Source |
|---|---|
| Bazel | Version pinned via `.bazelversion` in each repository |
| Bzlmod | Module system used for all dependency management |

## Documentation Tooling

| Tool | Role |
|---|---|
| docs-as-code | Shared Bazel module for documentation builds |
| Sphinx + MyST | Documentation engine with Markdown support |
| pydata-sphinx-theme | HTML theme with S-CORE branding via `score_layout` |
| Mermaid / PlantUML | Diagram rendering |
| sphinx-needs | Traceability and requirement management |

Version is pinned via `bazel_dep` in each repository's `MODULE.bazel`.

## Pre-commit Hooks

Hook versions are pinned in each repository's `.pre-commit-config.yaml`. The hook definitions themselves come from [eclipse-score/tooling](https://github.com/eclipse-score/tooling).

## How to check current versions

Inside a devcontainer:

```bash
bazel version                    # Bazel version
cat .bazelversion                # Pinned Bazel version
python3 --version                # Python version
pre-commit --version             # Pre-commit version
rustc --version                  # Rust compiler version
```

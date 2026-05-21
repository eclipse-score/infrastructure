# Tool Versions

## Devcontainer Image

Image: `ghcr.io/eclipse-score/devcontainer`

The devcontainer image is the canonical source for tool versions. Check the image's Dockerfile and release tags in [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) for the current version matrix.

## Toolchain Repositories

| Component | Repository | What it provides |
|---|---|---|
| C++ toolchain | [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) | GCC/Clang for Linux, QNX cross-compiler |
| Rust toolchain | [toolchains_rust](https://github.com/eclipse-score/toolchains_rust) | Rust stable, Ferrocene (safety-qualified) |
| C++ policies | [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) | Warning levels, sanitizers, constraint targets |
| Rust policies | [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) | Clippy rules, rustfmt configuration |

## Build System

| Tool | Source |
|---|---|
| Bazel | Version pinned via `.bazelversion` in each repository |
| Bzlmod | Module system used for all dependency management |

## Documentation Tooling

| Tool | Role |
|---|---|
| MkDocs | Static site generator |
| mermaid2 | Diagram rendering plugin |
| uv | Python package manager |

Version pins are in `pyproject.toml` and `uv.lock` per repository.

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

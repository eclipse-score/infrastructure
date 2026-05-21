# Configuration Reference

## .bazelrc

Standard S-CORE registry configuration:

```bazelrc
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

Registry resolution order: S-CORE registry first, then Bazel Central Registry.

## MODULE.bazel

Module metadata and dependency declarations:

```python
module(
    name = "my_module",
    version = "0.1.0",
)

bazel_dep(name = "score_cpp_policies", version = "...")
bazel_dep(name = "bazel_cpp_toolchains", version = "...")
```

Lock file: `MODULE.bazel.lock` — commit to the repository, refresh via `pre-commit run --all-files`.

## Devcontainer

Standard devcontainer configuration in `.devcontainer/devcontainer.json`:

```json
{
  "image": "ghcr.io/eclipse-score/devcontainer"
}
```

The image includes: Bazel, Python, pre-commit, C++ and Rust toolchains, documentation tooling.

Source: [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer)

## Pre-commit

S-CORE repositories use [pre-commit](https://pre-commit.com/) hooks from two sources: a project-specific hook from `eclipse-score/tooling` and standard ecosystem hooks.

### S-CORE hook

Source: [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml)

```yaml
repos:
  - repo: https://github.com/eclipse-score/tooling
    rev: <version>
    hooks:
      - id: copyright
```

| Hook | What it checks |
|---|---|
| `copyright` | SPDX license identifier and copyright header presence (via `cr_checker`) |

### Ecosystem hooks

Formatting, YAML validation, lock file freshness, and other hygiene checks come from standard pre-commit hooks (e.g. `pre-commit-hooks`, `mirrors-clang-format`). Each repository pins these in its own `.pre-commit-config.yaml`.

The reusable CI workflows in [cicd-workflows](https://github.com/eclipse-score/cicd-workflows) include `format.yml` and `copyright.yml` that enforce these checks in CI independently of local hook configuration.

## ITF Test Targets

Minimal `BUILD` configuration for an ITF integration test:

```starlark
load("@score_itf//:defs.bzl", "py_itf_test")

py_itf_test(
    name = "test_example",
    srcs = ["test_example.py"],
    args = ["--docker-image=ubuntu:24.04"],
    plugins = ["@score_itf//score/itf/plugins:docker_plugin"],
)
```

Available plugins:

| Plugin label | Purpose |
|---|---|
| `@score_itf//score/itf/plugins:docker_plugin` | Docker container targets |
| `@score_itf//score/itf/plugins:qemu_plugin` | QEMU virtual machine targets |
| `@score_itf//score/itf/plugins:dlt_plugin` | DLT log capture |
| `@score_itf//score/itf/plugins:attribute_plugin` | Requirement traceability metadata |

Source: [eclipse-score/itf](https://github.com/eclipse-score/itf)

## QEMU Configuration (ITF)

QEMU plugin configuration file (`qemu_config.json`):

```json
{
    "networks": [
        {
            "name": "tap0",
            "ip_address": "169.254.158.190",
            "gateway": "169.254.21.88"
        }
    ],
    "ssh_port": 22,
    "qemu_num_cores": 2,
    "qemu_ram_size": "1G"
}
```

Referenced from `BUILD` via `--qemu-config=$(location qemu_config.json)`.

## QNX Unit Tests

`.bazelrc` platform configs for QNX cross-compilation:

```bazelrc
build:qnx-x86_64   # Cross-compile for QNX x86_64
build:qnx-aarch64  # Cross-compile for QNX aarch64
```

Required flag for proper test extraction (prevents Bazel configuration conflicts):

```bazelrc
build --experimental_retain_test_configuration_across_testonly
```

Source: [eclipse-score/qnx_unit_tests](https://github.com/eclipse-score/qnx_unit_tests)

## MkDocs

Documentation site configuration in `mkdocs.yml`:

```yaml
theme:
  name: readthedocs

plugins:
  - search
  - mermaid2

markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - tables
  - toc:
      permalink: true
```

Python dependencies managed via `pyproject.toml` + `uv.lock`.

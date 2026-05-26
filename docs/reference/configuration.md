# Configuration Reference

## .bazelrc

Standard S-CORE registry configuration:

```text
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

For the full `py_itf_test` attribute reference and `py_itf_plugin` rule, see the [upstream Bazel macros reference](https://eclipse-score.github.io/itf/main/reference/bazel_macros.html).

For per-plugin CLI args and capabilities, see the [upstream plugin reference](https://eclipse-score.github.io/itf/main/reference/plugins.html).

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

```text
build:qnx-x86_64   # Cross-compile for QNX x86_64
build:qnx-aarch64  # Cross-compile for QNX aarch64
```

Required flag for proper test extraction (prevents Bazel configuration conflicts):

```text
build --experimental_retain_test_configuration_across_testonly
```

Source: [eclipse-score/qnx_unit_tests](https://github.com/eclipse-score/qnx_unit_tests)

## Sanitizers

[score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) provides the following sanitizer features as Bazel `cc_feature` definitions:

| Sanitizer | Purpose |
|---|---|
| ASan | Address errors (buffer overflow, use-after-free) |
| UBSan | Undefined behavior |
| LSan | Memory leaks |
| TSan | Data races |

Constraint targets: `no_tsan`, `any_sanitizer` (for conditional compilation via `select()`).

## Documentation (docs-as-code)

Documentation is built with Bazel using the `score_docs_as_code` module. Configuration lives in `docs/conf.py`:

```python
project = "S-CORE Infrastructure"
project_url = "https://eclipse-score.github.io/infrastructure"
version = "0.1"

extensions = [
    "score_sphinx_bundle",
]
```

The `score_sphinx_bundle` extension bundles MyST parser, Mermaid, PlantUML, sphinx-needs, and the S-CORE theme. The Bazel dependency is declared in `MODULE.bazel`.

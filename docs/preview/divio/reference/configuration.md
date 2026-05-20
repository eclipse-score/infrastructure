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

Hook source: [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml)

Standard `.pre-commit-config.yaml` entry:

```yaml
repos:
  - repo: https://github.com/eclipse-score/tooling
    rev: <version>
    hooks:
      - id: <hook-id>
```

Checks provided by the tooling repository:

| Hook | What it checks |
|---|---|
| Formatting | Code style (clang-format, rustfmt, black) |
| YAML validation | Syntax and schema |
| Copyright headers | SPDX identifier and copyright notice presence |
| Lock file freshness | `MODULE.bazel.lock`, `uv.lock` |

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

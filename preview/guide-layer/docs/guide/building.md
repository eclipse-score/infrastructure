# Building with Bazel

## Registry Configuration

Every S-CORE module repository configures two Bazel registries in `.bazelrc`:

```bazelrc
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

The first line resolves S-CORE internal modules. The second line falls back to the public [Bazel Central Registry](https://registry.bazel.build/) for everything else.

## Adding a Dependency

Declare dependencies in `MODULE.bazel`:

```python
bazel_dep(name = "my_dependency", version = "1.2.3")
```

Use the [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/) to discover available modules and their versions.

## Finding Modules

The [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/) lists all modules published to the S-CORE registry. Each registry entry corresponds to a GitHub Release in the module's repository.

## Toolchains

Build-side toolchains and policy modules are separate concerns:

| Repository | Role |
|---|---|
| [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) | **How to compile** C++ (Linux, QNX) |
| [toolchains_rust](https://github.com/eclipse-score/toolchains_rust) | **How to compile** Rust (incl. Ferrocene) |
| [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) | **Which rules to enforce** for C++ |
| [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) | **Which rules to enforce** for Rust |

Toolchains define compilers and linkers. Policies define warning baselines, lint rules, and sanitizer selections. They evolve independently.

## Remote Cache

A remote cache is available in CI pipelines. It reduces rebuild time across runs by sharing build artifacts between jobs.

## Lock Files

`MODULE.bazel.lock` and `uv.lock` should be committed to the repository. When dependency declarations change, refresh lock files via pre-commit:

```bash
pre-commit run --all-files
```

## Starting a New Module

Use [module_template](https://github.com/eclipse-score/module_template) as a starting point for new Bazel module repositories. It provides the standard directory layout, `.bazelrc`, devcontainer configuration, and CI workflows.

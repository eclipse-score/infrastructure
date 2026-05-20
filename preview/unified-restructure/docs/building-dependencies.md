# Building & Dependencies

How S-CORE repositories are built with Bazel, how dependencies are managed through the shared registry, and how toolchains and policies fit together.

## Bazel as Build System

Bazel is the standard build system for S-CORE middleware repositories. It provides hermetic, reproducible builds and a unified approach to building C++, Rust, and Python targets within the same repository.

## Registry Configuration

Each repository's `.bazelrc` configures two registries:

```bazelrc
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

The first line points to the S-CORE module registry. The second is the public Bazel Central Registry (BCR) for third-party dependencies.

## Adding a Dependency

Declare dependencies in your `MODULE.bazel` file:

```starlark
bazel_dep(name = "score_cpp_policies", version = "0.2.0")
```

The version must match an entry published in the [S-CORE registry](https://github.com/eclipse-score/bazel_registry) or the BCR.

## Finding Modules

Browse available modules and their versions at the [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/). Each registry entry corresponds to a GitHub Release in the source module repository.

## Toolchains

Toolchains define *how* to compile code:

- [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) -- C++ compilation for Linux and QNX targets
- [toolchains_rust](https://github.com/eclipse-score/toolchains_rust) -- Rust compilation including Ferrocene support

Toolchains are separate from policy modules. Toolchains control the compiler and linker configuration. Policies control which quality rules to enforce. They version independently so that updating a compiler does not force a policy change, and vice versa.

## Policy Modules

Policy modules define *which rules* to enforce:

- [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) -- warning baselines, sanitizer features, constraint targets
- [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) -- Clippy lint sets and rustfmt configuration

## Remote Cache

A remote build cache is available in CI. It stores build outputs so that unchanged targets do not need to be rebuilt, reducing CI build times.

## Lock Files

`MODULE.bazel.lock` and `uv.lock` should be committed to the repository. Pre-commit hooks automatically refresh these lock files when the corresponding declarations change.

## New Module

To create a new Bazel module repository, start from the [module_template](https://github.com/eclipse-score/module_template). It provides the standard repository layout, CI workflows, devcontainer configuration, and registry integration out of the box.

## Background

Bazel was chosen as the build system because S-CORE requires hermetic, reproducible builds across multiple languages (C++, Rust, Python) with strong cross-compilation support. The registry model couples directly to GitHub Releases: when a module repository creates a tagged release, that version can be imported into the shared registry and immediately becomes available to all consumers via `MODULE.bazel`. This avoids the need for a separate artifact server.

The toolchain/policy split exists because compilation infrastructure (which compiler, which target platform) and code quality rules (which warnings are errors, which lints are enforced) change at different rates and for different reasons. Keeping them in separate modules lets teams update one without being forced to update the other.

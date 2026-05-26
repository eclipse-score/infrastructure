# Glossary

Key terms used across the S-CORE infrastructure documentation.

## B

(bazel_registry)=
**bazel_registry** ([eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry))
: The S-CORE Bazel module registry. Module repositories publish versioned entries here; consuming repositories resolve first-party modules through it alongside the public [Bazel Central Registry](#bcr).

(bcr)=
**BCR** (Bazel Central Registry)
: The public registry at [registry.bazel.build](https://registry.bazel.build/) for third-party Bazel modules. S-CORE repositories fall back to BCR after the [S-CORE registry](#bazel_registry).

## C

**cicd-actions** ([eclipse-score/cicd-actions](https://github.com/eclipse-score/cicd-actions))
: Shared GitHub Actions composite actions for S-CORE workflows — for example, cross-repository token provisioning and QNX SDP setup.

**cicd-workflows** ([eclipse-score/cicd-workflows](https://github.com/eclipse-score/cicd-workflows))
: Shared reusable GitHub Actions workflows consumed by S-CORE module repositories. Covers build, test, formatting, copyright, lock file verification, documentation, static analysis, and release.

## D

**devcontainer** ([eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer))
: The shared development container image (`ghcr.io/eclipse-score/devcontainer`) used by S-CORE contributors. Contains Bazel, Python, pre-commit, C++/Rust toolchains, and documentation tooling. Also used as the CI execution environment.

**docs-as-code** ([eclipse-score/docs-as-code](https://github.com/eclipse-score/docs-as-code))
: The Sphinx + MyST + sphinx-needs toolchain used to build, validate, and publish S-CORE documentation. Provides the `score_sphinx_bundle` Bazel module.

## I

**ITF** (Integration Test Framework, [eclipse-score/itf](https://github.com/eclipse-score/itf))
: A pytest-based framework for target-oriented integration testing. Tests run against Docker containers, QEMU virtual machines, or real hardware through a unified `Target` interface. Integrated into Bazel via `py_itf_test`.

## K

(known_good)=
**known_good**
: An explicit manifest that names the set of component revisions (module + commit) that belong together in one validated S-CORE integration stack. Acts as the higher-level control file above individual Bazel lock files. See [reference_integration](#reference_integration).

## M

**module_template** ([eclipse-score/module_template](https://github.com/eclipse-score/module_template))
: GitHub template repository for new S-CORE Bazel modules. Provides standard directory layout, `.bazelrc`, devcontainer configuration, and CI workflows.

## O

**otterdog** ([otterdog docs](https://otterdog.readthedocs.io/en/latest/userguide/))
: Infrastructure-as-code tool for managing GitHub organization settings (branch protection, required checks, allowed Actions) as versioned configuration in [eclipse-score/.eclipsefdn](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet).

## R

(reference_integration)=
**reference_integration** ([eclipse-score/reference_integration](https://github.com/eclipse-score/reference_integration))
: Cross-repository integration environment. Assembles multiple S-CORE modules into one integrated stack and validates them together. The source of truth for [known_good](#known_good) records.

## S

**score_cpp_policies** ([eclipse-score/score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies))
: Shared C++ lint, warning, and sanitizer policy module. Provides selectable `cc_feature` definitions for ASan, UBSan, LSan, TSan, and warning baselines. Consumed independently from the C++ toolchain.

**score_rust_policies** ([eclipse-score/score_rust_policies](https://github.com/eclipse-score/score_rust_policies))
: Shared Rust Clippy and rustfmt policy module. Consumed independently from the Rust toolchain.

## T

**tooling** ([eclipse-score/tooling](https://github.com/eclipse-score/tooling))
: Shared Bazel rules, macros, and pre-commit hooks for S-CORE. Provides the `copyright` pre-commit hook among others.

**toolchains_rust** ([eclipse-score/toolchains_rust](https://github.com/eclipse-score/toolchains_rust))
: Rust toolchain Bazel module for S-CORE, including prebuilt Ferrocene toolchains.

**bazel_cpp_toolchains** ([eclipse-score/bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains))
: C++ toolchain Bazel module for S-CORE. Provides compiler configuration for Linux and QNX builds.

# Code Quality & Compliance

Pre-commit hooks, language-specific policies, licensing requirements, and organization-level settings for S-CORE repositories.

## Pre-commit Hooks

Install hooks to run checks automatically on each commit:

```bash
pre-commit install
```

Run all checks manually:

```bash
pre-commit run --all-files
```

The shared hooks are defined in [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml). They cover:

- Code formatting (language-specific formatters)
- YAML validation
- Copyright and license headers
- Lock file refresh (`MODULE.bazel.lock`, `uv.lock`)

## Copyright & License Headers

Every source file needs either:

- An **SPDX header** at the top of the file, or
- A `.license` **sidecar file** next to the source file

The [tooling](https://github.com/eclipse-score/tooling) repository provides pre-commit hooks and CI checks that verify headers are present and correctly formatted.

## C++ Policies

The [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) module provides shared quality standards for C++ code:

- Warning baselines (which compiler warnings are treated as errors)
- Sanitizer features (ASan, UBSan, LSan, TSan as selectable Bazel features)
- Constraint targets for platform-specific configuration

Add it as a dependency:

```starlark
bazel_dep(name = "score_cpp_policies", version = "0.2.0")
```

## Rust Policies

The [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) module provides shared Rust quality defaults:

- Clippy lint configuration
- rustfmt formatting rules

Add it as a dependency:

```starlark
bazel_dep(name = "score_rust_policies", version = "0.1.0")
```

## Where Checks Run

Quality checks run at multiple levels:

1. **Local** -- pre-commit hooks in the devcontainer catch issues before commit
2. **Bazel build** -- policy modules enforce warnings and lints during compilation
3. **CI gates** -- GitHub Actions workflows run the same checks as required status checks before merge

## Organization Settings

GitHub organization settings (branch protection rules, required status checks, app configurations) are managed as code via [Otterdog](https://otterdog.readthedocs.io/) in the [.eclipsefdn](https://github.com/eclipse-score/.eclipsefdn) repository. Changes go through pull request review.

## Background

S-CORE follows the [REUSE specification](https://reuse.software/) for licensing, which requires machine-readable license and copyright information in every file. The SPDX header approach (or `.license` sidecar) ensures that licensing data is always collocated with the source code rather than relying on a single top-level LICENSE file.

The toolchain/policy split keeps compilation configuration separate from quality rules. This means a team can update their compiler toolchain without changing which warnings are enforced, and vice versa. Both types of modules are versioned in the shared registry and consumed via `MODULE.bazel`.

# How to Update a Shared Toolchain

This guide covers how to update the shared C++ or Rust toolchain baseline in S-CORE and roll it out to consuming repositories.

S-CORE keeps toolchain concerns and policy concerns in separate repositories. An update to a compiler version belongs to the toolchain module; a change to lint rules or sanitizer defaults belongs to the policy module. They can evolve independently.

| Repository | What it owns | When to update it |
|---|---|---|
| [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) | C++ compiler, sysroots, toolchain registration | Compiler version bump, new target platform |
| [toolchains_rust](https://github.com/eclipse-score/toolchains_rust) | Rust toolchains incl. Ferrocene, registration | Rust stable or Ferrocene version bump |
| [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) | C++ warning baseline, sanitizer features, constraints | Warning rule changes, new sanitizer support |
| [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) | Clippy rules, rustfmt defaults | Lint rule updates, formatting changes |

## Update a toolchain module

### 1. Make the change

Clone the toolchain repository and create a branch. For a compiler version bump:

- Update the version pin in the relevant build file or download declaration
- Update any corresponding hash or checksum values
- Run `bazel build //...` and `bazel test //...` in the toolchain repository to verify the change compiles and tests pass

For cross-compilation targets (QNX, ARM), test those configurations explicitly if you have access:

```bash
bazel build //... --config=qnx-x86_64
bazel build //... --config=qnx-aarch64
```

### 2. Open a PR and get it reviewed

Toolchain changes affect every consumer. Reviewers should check:

- Do existing tests still pass?
- Are new compiler warnings triggered that would break consuming repositories?
- For Ferrocene toolchains: does the change affect safety certification claims?

### 3. Release a new version

After merge, create a GitHub Release with a semantic version tag (e.g. `v1.5.0`). Then follow the [registry import process](publishing.md) to publish the new version to the S-CORE Bazel registry.

## Roll out to consuming repositories

Once the new toolchain version is in the registry, consuming repositories need their `MODULE.bazel` updated:

```python
bazel_dep(name = "bazel_cpp_toolchains", version = "1.5.0")
# or
bazel_dep(name = "toolchains_rust", version = "2.3.0")
```

**Automated updates via `renovate-bot`**: the S-CORE registry is tracked by `renovate-bot`, which opens automated dependency-update PRs in consuming repositories. Review these PRs and merge once CI passes.

**Manual update**: if automated updates are not running for a repository, open a PR directly.

### Staged rollout

Roll out toolchain updates to a small set of repositories first, verify that builds and tests pass, then proceed to the rest. A breaking compiler update can fail builds in ways that are hard to diagnose in bulk.

If a toolchain update introduces new warnings that break builds in consuming repositories, two options:
1. Fix the warnings in the consuming repositories as part of the rollout
2. Adjust the shared policy module to allow the warning temporarily, with a tracked follow-up

## Update a policy module

Policy changes (lint rules, sanitizer flags) follow the same process as toolchain changes. Because policy modules evolve independently, a policy tightening that breaks existing code should be rolled out with a migration period:

1. Publish the new policy version
2. Identify repositories that fail under the new policy
3. Either fix the violations in those repositories or provide a suppression mechanism
4. Remove the suppression once the violations are resolved

## Governance note

Toolchain and policy modules need visible ownership. If no one is explicitly responsible for a shared toolchain, it drifts and eventually breaks. Each toolchain or policy module should have at least one named maintainer who monitors for upstream releases and security advisories.

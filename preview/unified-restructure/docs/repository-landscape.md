# Repository Landscape

An overview of the repositories in the [eclipse-score](https://github.com/eclipse-score) GitHub organization, how they relate, and essential quick-reference information.

## Repository Directory

| Repository | Purpose |
|---|---|
| [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) | Shared development container images |
| [eclipse-score/tooling](https://github.com/eclipse-score/tooling) | Shared Bazel rules and pre-commit hooks |
| [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry) | Shared Bazel module registry |
| [eclipse-score/bazel_registry_ui](https://github.com/eclipse-score/bazel_registry_ui) | Browsable registry UI |
| [eclipse-score/bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) | C++ Bazel toolchain (Linux, QNX) |
| [eclipse-score/toolchains_rust](https://github.com/eclipse-score/toolchains_rust) | Rust toolchains incl. Ferrocene |
| [eclipse-score/score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) | Shared C++ lint, warning, and sanitizer policies |
| [eclipse-score/score_rust_policies](https://github.com/eclipse-score/score_rust_policies) | Shared Rust Clippy and rustfmt policies |
| [eclipse-score/module_template](https://github.com/eclipse-score/module_template) | Template for new Bazel module repositories |
| [eclipse-score/sbom-tool](https://github.com/eclipse-score/sbom-tool) | SBOM generation Bazel rules |
| [eclipse-score/reference_integration](https://github.com/eclipse-score/reference_integration) | Cross-repository integration environment |
| [eclipse-score/.github](https://github.com/eclipse-score/.github) | Organization profile and cross-repo metrics |
| [eclipse-score/.eclipsefdn](https://github.com/eclipse-score/.eclipsefdn) | Otterdog configuration (org settings as code) |
| [eclipse-score/score](https://github.com/eclipse-score/score) | Main project repository and handbook |

## How Repositories Relate

Bazel module repositories produce versioned modules that are published via GitHub Releases. These releases are imported into the shared [bazel_registry](https://github.com/eclipse-score/bazel_registry), where they become available for other repositories to consume through `MODULE.bazel` dependency declarations. The [devcontainer](https://github.com/eclipse-score/devcontainer) provides the shared development environment used across all repositories. The [tooling](https://github.com/eclipse-score/tooling) repository supplies shared Bazel rules and pre-commit hooks, while the policy repositories ([score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies), [score_rust_policies](https://github.com/eclipse-score/score_rust_policies)) define language-specific quality standards that modules depend on.

## Quick Reference

### Devcontainer Image

```
ghcr.io/eclipse-score/devcontainer
```

### Registry Configuration

Add to your `.bazelrc`:

```bazelrc
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

The first line resolves S-CORE modules from the project registry. The second line falls back to the public Bazel Central Registry for everything else.

### Common Commands

```bash
# Build
bazel build //...

# Test
bazel test //...

# Coverage
bazel coverage //...

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

### Key Links

- [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/) -- browse available modules and versions
- [S-CORE Handbook](https://eclipse-score.github.io/score/main/handbook) -- processes, tooling, and contribution model
- [Slack: #score-infrastructure](https://sdvworkinggroup.slack.com/archives/C0894QGRZDM) -- main infrastructure discussion channel
- [Meeting Minutes](https://github.com/orgs/eclipse-score/discussions/236) -- infrastructure team meeting notes

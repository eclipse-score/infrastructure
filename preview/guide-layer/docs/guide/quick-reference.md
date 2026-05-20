# Quick Reference

## Key Repositories

| Repository | Purpose |
|---|---|
| [eclipse-score/score](https://github.com/eclipse-score/score) | Main project repository and handbook |
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

## Devcontainer Image

```
ghcr.io/eclipse-score/devcontainer
```

## Bazel Registry Configuration

Add to `.bazelrc`:

```bazelrc
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

## Common Commands

| Command | Purpose |
|---|---|
| `bazel build //...` | Build everything |
| `bazel test //...` | Run all tests |
| `bazel coverage //... --combined_report` | Collect coverage (LCOV) |
| `pre-commit install` | Set up git hooks |
| `pre-commit run --all-files` | Run all checks |

## Key Links

- [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/) — Browse available Bazel modules
- [S-CORE Handbook](https://eclipse-score.github.io/score/main/handbook) — Project-wide processes and contribution model
- [Slack: #score-infrastructure](https://sdvworkinggroup.slack.com/archives/C0894QGRZDM) — Infrastructure team discussion
- [Meeting Minutes](https://github.com/orgs/eclipse-score/discussions/236) — Infrastructure team meeting notes

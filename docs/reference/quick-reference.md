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
| [eclipse-score/itf](https://github.com/eclipse-score/itf) | Integration Test Framework (pytest, Docker/QEMU/hardware) |
| [eclipse-score/qnx_unit_tests](https://github.com/eclipse-score/qnx_unit_tests) | QNX microvm unit test runner (C++, Rust) |
| [eclipse-score/reference_integration](https://github.com/eclipse-score/reference_integration) | Cross-repository integration environment |
| [eclipse-score/.github](https://github.com/eclipse-score/.github) | Organization profile and cross-repo metrics |
| [eclipse-score/.eclipsefdn](https://github.com/eclipse-score/.eclipsefdn) | Otterdog configuration (org settings as code) |

## Devcontainer Image

```
ghcr.io/eclipse-score/devcontainer
```

## Common Commands

| Command | Purpose |
|---|---|
| `bazel build //...` | Build everything |
| `bazel test //...` | Run all tests |
| `bazel test //path/to:target` | Run a specific test |
| `bazel test //... --nocache_test_results` | Force re-run (skip cache) |
| `bazel coverage //... --combined_report` | Collect coverage (LCOV) |
| `pre-commit install` | Set up git hooks |
| `pre-commit run --all-files` | Run all pre-commit checks |
| `uv sync` | Install Python dependencies |
| `uv run mkdocs serve` | Start local docs preview |
| `uv run mkdocs build --strict` | Build docs with strict validation |

## Key Links

- [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/) — Browse available Bazel modules
- [S-CORE Handbook](https://eclipse-score.github.io/score/main/handbook) — Project-wide processes and contribution model
- [Repository Overview](https://eclipse-score.github.io/.github/) — Cross-repo metrics and status
- [Slack: #score-infrastructure](https://sdvworkinggroup.slack.com/archives/C0894QGRZDM) — Infrastructure team discussion
- [Slack: #score-infrastructure-review-requests](https://sdvworkinggroup.slack.com/archives/C08RDRKH5FE) — PR review requests
- [Meeting Minutes](https://github.com/orgs/eclipse-score/discussions/236) — Infrastructure team meeting notes

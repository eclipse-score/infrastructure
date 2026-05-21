# Quick Reference

## Key Repositories

The most-used infrastructure repositories. For the full list of all 60+ repositories with status and metrics, see the [Repository Overview](https://eclipse-score.github.io/.github/).

| Repository | Purpose |
|---|---|
| [score](https://github.com/eclipse-score/score) | Main project repository and handbook |
| [devcontainer](https://github.com/eclipse-score/devcontainer) | Shared development container images |
| [tooling](https://github.com/eclipse-score/tooling) | Shared Bazel rules and pre-commit hooks |
| [bazel_registry](https://github.com/eclipse-score/bazel_registry) | Shared Bazel module registry |
| [cicd-workflows](https://github.com/eclipse-score/cicd-workflows) | Reusable GitHub Actions workflows |
| [cicd-actions](https://github.com/eclipse-score/cicd-actions) | Reusable GitHub Actions (composite actions) |
| [docs-as-code](https://github.com/eclipse-score/docs-as-code) | Docs-as-code tooling (Sphinx, traceability) |
| [module_template](https://github.com/eclipse-score/module_template) | Template for new Bazel module repositories |
| [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) | C++ Bazel toolchain configuration (Linux, QNX) |
| [toolchains_rust](https://github.com/eclipse-score/toolchains_rust) | Rust toolchains incl. Ferrocene |
| [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) | Shared C++ lint, warning, and sanitizer policies |
| [score_rust_policies](https://github.com/eclipse-score/score_rust_policies) | Shared Rust Clippy and rustfmt policies |
| [itf](https://github.com/eclipse-score/itf) | Integration Test Framework (pytest, Docker/QEMU/hardware) |
| [reference_integration](https://github.com/eclipse-score/reference_integration) | Cross-repository integration environment |
| [.eclipsefdn](https://github.com/eclipse-score/.eclipsefdn) | Otterdog configuration (org settings as code) |

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
| `bazel run //:docs` | Build documentation |
| `bazel run //:live_preview` | Start local docs preview with live reload |
| `bazel run //:docs_check` | Validate docs (must pass before merge) |

## Key Links

- [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/) — Browse available Bazel modules
- [S-CORE Handbook](https://eclipse-score.github.io/score/main/handbook) — Project-wide processes and contribution model
- [Repository Overview](https://eclipse-score.github.io/.github/) — Cross-repo metrics and status
- [Slack: #score-infrastructure](https://sdvworkinggroup.slack.com/archives/C0894QGRZDM) — Infrastructure team discussion
- [Slack: #score-infrastructure-review-requests](https://sdvworkinggroup.slack.com/archives/C08RDRKH5FE) — PR review requests
- [Meeting Minutes](https://github.com/orgs/eclipse-score/discussions/236) — Infrastructure team meeting notes

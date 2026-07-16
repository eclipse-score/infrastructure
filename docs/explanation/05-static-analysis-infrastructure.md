# 5 Code Analysis Infrastructure 🔴

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure for inspecting S-CORE source code and repository configuration without executing the software, to enforce quality, consistency, and security expectations across repositories.*

:::{warning} Draft
This chapter has not been fully reviewed. Content may be incomplete or inaccurate.
:::

- Static analysis complements testing by finding issues through code and configuration inspection instead of runtime verification.
- This chapter defines the shared code-analysis capability: analyzer scope, baseline expectations, rule governance, and ownership boundaries across repositories.
- Local execution and CI gating consume this capability in their own chapters rather than defining separate analyzer baselines.
- In other words, [chapter 2](02-developer-environment.md) explains how contributors run checks locally, while this chapter explains which analyzers and rules those commands should carry.
- Runtime-driven techniques such as coverage, sanitizers, fuzzing, and profiling belong in [chapter 4](04-testing-infrastructure.md), not here.
- Dependency alerts, supply-chain analysis of dependency sets, and continuous SBOM monitoring belong in [chapter 6](06-compliance-infrastructure.md), not here.
- **Biggest gap**: code analysis is not yet defined and governed as one cross-repository capability with shared tooling, rule baselines, and ownership expectations.

## 5.1 Tooling Baseline 🔴

*Defining which static analysis tools are approved, recommended, or required for different S-CORE repository types and languages.*

- Code analysis in S-CORE includes linters, type/interface analyzers, style and import checks, and security-oriented analyzers where appropriate.
- Tool choice is currently influenced by language ecosystems, repository classes, and existing engineering practice.
- **Biggest gap**: no explicit cross-repository baseline defines which analyzers are expected by default for C++, Rust, Python, and workflow or documentation assets.

### 5.1.1 C++ 🔴

*Static analysis tooling for C++ repositories.*

C++ has the most developed policy infrastructure in S-CORE today. The `score_cpp_policies` module provides a reusable Bazel-integrated rule baseline covering compiler warnings, clang-tidy checks, and formatting expectations. Because policy is decoupled from the toolchain, repositories can adopt updated rule baselines independently of compiler version upgrades. The security-oriented analysis layer for C++ is covered by CodeQL, described in [section 5.4.1](#sast).

**Biggest gap**: the `score_cpp_policies` baseline and its expected adoption scope are not yet documented in a shared, accessible form. Deviation from the baseline is not governed.

### 5.1.2 Rust 🔴

*Static analysis tooling for Rust repositories.*

Rust has native linting via Clippy and formatting via rustfmt, both of which integrate naturally with `rules_rust` in a Bazel build. The `score_rust_policies` module packages shared Clippy and rustfmt configuration as a reusable Bazel module, following the same separation of policy from toolchain used by the C++ path. In practice, Clippy is already used in several Rust repositories but the shared policy baseline is not uniformly adopted.

**Biggest gap**: Clippy and rustfmt configuration exists in individual repositories, but the shared `score_rust_policies` baseline and its required adoption scope are not yet clearly defined or enforced.

### 5.1.3 Python 🟠

*Static analysis tooling for Python repositories.*

Python analysis in S-CORE is less standardized than C++ or Rust. Ruff covers linting and formatting in a single fast tool, while mypy or pyright can provide type checking where type annotations are present. Pre-commit integration already runs some checks in development environments, but CI-enforced shared baselines for Python are not in place.

**Biggest gap**: no shared Bazel-integrated or CI-enforced Python analyzer baseline exists across S-CORE repositories.

### 5.1.4 Workflow and Configuration Assets 🟠

*Applying analysis to GitHub Actions workflows and YAML configuration.*

GitHub Actions workflow files, YAML configuration, and Bazel `BUILD` files benefit from automated inspection independently of product code. Tools such as actionlint (for workflow files) and yamllint cover the most impactful targets here. Pre-commit runs some of these locally, but CI enforcement for workflow and configuration analysis is not yet a defined part of the S-CORE baseline.

**Biggest gap**: no shared CI-enforced baseline for workflow and configuration asset analysis exists across S-CORE repositories.

### 5.1.5 Documentation Assets 🔴

*Applying analysis to documentation sources such as reStructuredText, Markdown, and prose.*

Documentation repositories and repositories with significant prose content benefit from automated checks for broken links, spelling, and markup validity. Tools such as sphinx-lint, vale, or codespell can be integrated into pre-commit and CI. Currently there is no shared baseline for documentation analysis across S-CORE.

**Biggest gap**: documentation asset analysis is not defined or enforced as part of the shared S-CORE static analysis standard.


---

## 5.2 Shared Rule Configuration 🔴

*Managing analyzer rules, severities, suppressions, and versioning as shared infrastructure instead of ad-hoc repository detail.*

- Shared rule configurations are an important part of repository standards and should be versioned like other infrastructure policy artifacts.
- Repository overrides should be explicit, limited, and explainable rather than silent drift from the shared baseline.

In the current S-CORE repository landscape, these shared rules are increasingly packaged as separate policy modules rather than being folded into toolchain repositories. That is why repositories such as `score_rust_policies` and `score_cpp_policies` belong to this chapter's perspective, while `toolchains_rust` and `bazel_cpp_toolchains` belong to [chapter 3](03-build-infrastructure.md#toolchain-management). The important architectural rule is that consumers should be able to adopt shared lint, warning, and formatting baselines without having to change compiler versions or Bazel toolchain registration at the same time. When such a policy also exposes selectable runtime-oriented features such as sanitizers, [chapter 4](04-testing-infrastructure.md#sanitizers-runtime-checks) still owns why and when those checks are executed; this chapter owns only the reusable rule baseline.

### 5.2.1 Baseline Rulesets 🔴

*Defining centrally maintained defaults for analyzer configuration.*

- Central baselines should define default enabled checks, severity handling, and common exclusions.
- Baselines should be reusable in templates, synchronized configuration, or shared workflow inputs.
- **Biggest gap**: there is no visible authoritative baseline for static-analysis rules across S-CORE repositories.

### 5.2.2 Overrides and Suppressions 🔴

*Allowing repository-specific exceptions without losing visibility or governance.*

- Overrides and suppressions are sometimes necessary for migration, generated code, third-party constraints, or language-specific false positives.
- Exceptions should be narrow, reviewable, and traceable so that debt can be reduced over time.
- **Biggest gap**: suppressions and local overrides are not yet governed by a shared policy for justification, expiry, or review.

---

## 5.3 Incremental Adoption 🔴

*Rolling out stronger analyzer baselines without blocking repository progress all at once.*

- A shared analysis strategy should support migration from weak or inconsistent baselines toward stronger common enforcement.
- **Biggest gap**: there is no documented rollout model for moving repositories from optional analysis toward required shared baselines.

---

## 5.4 Security Scanning 🟠

*Clarifying how code analysis relates to security-oriented scanning of source and repository configuration.*

- Code analysis includes both general code-quality checks and security-relevant inspection of source and repository configuration.
- This chapter is the canonical home for shared tooling, rule configuration, and execution boundaries that are common across analyzer types.
- **Biggest gap**: the boundary between quality-oriented analyzers and security scanning is not yet described clearly enough to avoid duplication and ownership gaps.

### 5.4.1 SAST 🔴

*Static application security testing for S-CORE code and configuration.*

SAST tools analyze source code for security vulnerabilities without executing it. For S-CORE, CodeQL is the primary SAST tool because it integrates natively with GitHub through code scanning alerts, supports C/C++ and Python analysis relevant to the S-CORE language landscape, and can run as a standard GitHub Actions workflow. The infrastructure question is not whether CodeQL works — it does — but how it is configured consistently: which query suites are enabled, what severity thresholds gate a merge, and how results are surfaced to maintainers.

A useful SAST configuration has three layers. The query suite defines which vulnerability patterns to look for — the default security suite covers the most impactful findings, while extended suites add code-quality checks at the cost of more noise. The CI gate defines which findings block merges — typically only high and critical severity — while lower findings appear as alerts for maintainers to triage. The cross-repository alignment defines whether all S-CORE repositories use the same query suite and gate policy or whether repositories can override the baseline.

**Biggest gap**: SAST-specific configuration and required security-gate policies are not yet standardized across repositories. CodeQL query suite selection and severity thresholds vary between repositories.

### 5.4.2 Secret Scanning 🟡

*Detecting secrets inadvertently committed to S-CORE repositories.*

GitHub secret scanning detects common credential patterns in repository history and ongoing changes.

# 5 Code Analysis Infrastructure ⚪

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

## 5.1 Tooling Baseline ⚪

*Defining which static analysis tools are approved, recommended, or required for different S-CORE repository types and languages.*

- Code analysis in S-CORE includes linters, type/interface analyzers, style and import checks, and security-oriented analyzers where appropriate.
- Tool choice is currently influenced by language ecosystems, repository classes, and existing engineering practice.
- **Biggest gap**: no explicit cross-repository baseline defines which analyzers are expected by default for C++, Rust, Python, and workflow or documentation assets.

### 5.1.1 C++ ⚪

*Static analysis tooling for C++ repositories.*

C++ has the most developed policy infrastructure in S-CORE today. The `score_cpp_policies` module provides a reusable Bazel-integrated rule baseline covering compiler warnings, clang-tidy checks, and formatting expectations. Because policy is decoupled from the toolchain, repositories can adopt updated rule baselines independently of compiler version upgrades. The security-oriented analysis layer for C++ is covered by CodeQL, described in [section 5.4.1](#sast).

**Biggest gap**: the `score_cpp_policies` baseline and its expected adoption scope are not yet documented in a shared, accessible form. Deviation from the baseline is not governed.

### 5.1.2 Rust ⚪

*Static analysis tooling for Rust repositories.*

Rust has native linting via Clippy and formatting via rustfmt, both of which integrate naturally with `rules_rust` in a Bazel build. The `score_rust_policies` module packages shared Clippy and rustfmt configuration as a reusable Bazel module, following the same separation of policy from toolchain used by the C++ path. In practice, Clippy is already used in several Rust repositories but the shared policy baseline is not uniformly adopted.

**Biggest gap**: Clippy and rustfmt configuration exists in individual repositories, but the shared `score_rust_policies` baseline and its required adoption scope are not yet clearly defined or enforced.

### 5.1.3 Python ⚪

*Static analysis tooling for Python repositories.*

Python analysis in S-CORE is less standardized than C++ or Rust. Ruff covers linting and formatting in a single fast tool, while mypy or pyright can provide type checking where type annotations are present. Pre-commit integration already runs some checks in development environments, but CI-enforced shared baselines for Python are not in place.

**Biggest gap**: no shared Bazel-integrated or CI-enforced Python analyzer baseline exists across S-CORE repositories.

### 5.1.4 Workflow and Configuration Assets ⚪

*Applying analysis to GitHub Actions workflows and YAML configuration.*

GitHub Actions workflow files, YAML configuration, and Bazel `BUILD` files benefit from automated inspection independently of product code. Tools such as actionlint (for workflow files) and yamllint cover the most impactful targets here. Pre-commit runs some of these locally, but CI enforcement for workflow and configuration analysis is not yet a defined part of the S-CORE baseline.

**Biggest gap**: no shared CI-enforced baseline for workflow and configuration asset analysis exists across S-CORE repositories.

### 5.1.5 Documentation Assets ⚪

*Applying analysis to documentation sources such as reStructuredText, Markdown, and prose.*

Documentation repositories and repositories with significant prose content benefit from automated checks for broken links, spelling, and markup validity. Tools such as sphinx-lint, vale, or codespell can be integrated into pre-commit and CI. Currently there is no shared baseline for documentation analysis across S-CORE.

**Biggest gap**: documentation asset analysis is not defined or enforced as part of the shared S-CORE static analysis standard.


---

## 5.2 Shared Rule Configuration ⚪

*Managing analyzer rules, severities, suppressions, and versioning as shared infrastructure instead of ad-hoc repository detail.*

- Shared rule configurations are an important part of repository standards and should be versioned like other infrastructure policy artifacts.
- Repository overrides should be explicit, limited, and explainable rather than silent drift from the shared baseline.

In the current S-CORE repository landscape, these shared rules are increasingly packaged as separate policy modules rather than being folded into toolchain repositories. That is why repositories such as `score_rust_policies` and `score_cpp_policies` belong to this chapter's perspective, while `toolchains_rust` and `bazel_cpp_toolchains` belong to [chapter 3](03-build-infrastructure.md#toolchain-management). The important architectural rule is that consumers should be able to adopt shared lint, warning, and formatting baselines without having to change compiler versions or Bazel toolchain registration at the same time. When such a policy also exposes selectable runtime-oriented features such as sanitizers, [chapter 4](04-testing-infrastructure.md#sanitizers-runtime-checks) still owns why and when those checks are executed; this chapter owns only the reusable rule baseline.

### 5.2.1 Baseline Rulesets

*Defining centrally maintained defaults for analyzer configuration.*

- Central baselines should define default enabled checks, severity handling, and common exclusions.
- Baselines should be reusable in templates, synchronized configuration, or shared workflow inputs.
- **Biggest gap**: there is no visible authoritative baseline for static-analysis rules across S-CORE repositories.

### 5.2.2 Overrides and Suppressions

*Allowing repository-specific exceptions without losing visibility or governance.*

- Overrides and suppressions are sometimes necessary for migration, generated code, third-party constraints, or language-specific false positives.
- Exceptions should be narrow, reviewable, and traceable so that debt can be reduced over time.
- **Biggest gap**: suppressions and local overrides are not yet governed by a shared policy for justification, expiry, or review.

---

## 5.3 Execution Model ⚪

*Defining where and how the shared static-analysis capability should be executed across the engineering flow.*

- Static analysis should be executable in multiple contexts, especially local development and CI, without redefining analyzer baselines per context.
- Different execution contexts can use different subsets or frequencies, but they should all derive from the same shared rules and ownership model.
- **Biggest gap**: there is no documented execution model that cleanly separates shared analyzer policy from local and CI-specific delivery.

### 5.3.1 Local Execution Expectations

*Defining what static analysis should provide before code reaches CI.*

- Contributors should be able to run the shared analyzer baseline early enough to catch common issues before opening or updating a pull request.
- Local execution should favor fast feedback and alignment with the centrally defined ruleset, while the delivery details for shared environments, editor usage, and pre-commit belong in [chapter 2](02-developer-environment.md).
- **Biggest gap**: local execution expectations are not yet defined independently of specific tools such as devcontainers, IDEs, or pre-commit hooks.

### 5.3.2 CI Execution Expectations

*Defining what CI should enforce from the shared static-analysis capability.*

- CI should execute the agreed shared analyzer baseline in a consistent, review-visible way and use its outcomes for merge decisions where appropriate.
- The workflow, reporting, and branch-protection mechanics belong in [chapter 7](07-automation-integration.md), not in the code-analysis capability definition itself.
- **Biggest gap**: CI enforcement expectations are not yet clearly separated from workflow implementation details.

### 5.3.3 Incremental Adoption

*Rolling out stronger analyzer baselines without blocking repository progress all at once.*

- A shared analysis strategy should support migration from weak or inconsistent baselines toward stronger common enforcement.
- **Biggest gap**: there is no documented rollout model for moving repositories from optional analysis toward required shared baselines.

---

## 5.4 Security Scanning 🟠

*Clarifying how code analysis relates to security-oriented scanning of source and repository configuration.*

- Code analysis includes both general code-quality checks and security-relevant inspection of source and repository configuration.
- This chapter is the canonical home for shared tooling, rule configuration, and execution boundaries that are common across analyzer types.
- **Biggest gap**: the boundary between quality-oriented analyzers and security scanning is not yet described clearly enough to avoid duplication and ownership gaps.

### 5.4.1 SAST 🟠

*Static application security testing for S-CORE code and configuration.*

SAST tools analyze source code for security vulnerabilities without executing it. For S-CORE, CodeQL is the primary SAST tool because it integrates natively with GitHub through code scanning alerts, supports C/C++ and Python analysis relevant to the S-CORE language landscape, and can run as a standard GitHub Actions workflow. The infrastructure question is not whether CodeQL works — it does — but how it is configured consistently: which query suites are enabled, what severity thresholds gate a merge, and how results are surfaced to maintainers.

A useful SAST configuration has three layers. The query suite defines which vulnerability patterns to look for — the default security suite covers the most impactful findings, while extended suites add code-quality checks at the cost of more noise. The CI gate defines which findings block merges — typically only high and critical severity — while lower findings appear as alerts for maintainers to triage. The cross-repository alignment defines whether all S-CORE repositories use the same query suite and gate policy or whether repositories can override the baseline.

**Biggest gap**: SAST-specific configuration and required security-gate policies are not yet standardized across repositories. CodeQL query suite selection and severity thresholds vary between repositories.

### 5.4.2 Secret Scanning 🟠

*Detecting secrets inadvertently committed to S-CORE repositories.*

- GitHub secret scanning detects common credential patterns in repository history and ongoing changes.
- **Biggest gap**: custom secret patterns and push-protection configuration are not uniformly enabled.

### 5.4.3 Repository Configuration Security

*Inspecting workflows and repository configuration for risky patterns before they become incidents.*

- Infrastructure repositories depend heavily on workflow configuration, permissions, and automation wiring, so configuration-level analysis is a meaningful part of code-analysis security scanning.
- **Biggest gap**: configuration-oriented security analysis is not yet described as part of a shared S-CORE baseline.

---

## 5.5 Results and Governance ⚪

*Managing findings, conformance visibility, and analyzer evolution across repositories.*

- Code-analysis infrastructure should provide visibility into adoption, drift, and findings without forcing every repository to invent its own process.
- Governance includes rule changes, false-positive handling, technical-debt baselines, and measurement of conformance to shared expectations.
- **Biggest gap**: no cross-repository reporting and governance loop currently shows which repositories run which analyzers, with what deviations and outcomes.

### 5.5.1 False Positives and Baselines

*Handling existing findings and noisy rules in a controlled way.*

- Migration to stronger analyzers often needs temporary baselines or approved suppressions so repositories can improve incrementally.
- **Biggest gap**: there is no shared approach for introducing analyzers into repositories with existing finding backlogs.

### 5.5.2 Cross-Repository Visibility

*Measuring adoption and conformance of static-analysis standards across S-CORE.*

- Cross-repository reporting should show baseline adoption, exceptions, and required-check coverage, not just individual CI job output.
- **Biggest gap**: no common dashboard or conformance report currently summarizes static-analysis coverage across S-CORE.
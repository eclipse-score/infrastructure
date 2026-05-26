# 5 Code Analysis Infrastructure ⚪

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure for inspecting S-CORE source code and repository configuration without executing the software, to enforce quality, consistency, and security expectations across repositories.*

:::{warning} Draft
This chapter has not been fully reviewed. Content may be incomplete or inaccurate.
:::

**S-CORE**

- Static analysis complements testing by finding issues through code and configuration inspection instead of runtime verification.
- This chapter defines the shared code-analysis capability: analyzer scope, baseline expectations, rule governance, and ownership boundaries across repositories.
- Local execution and CI gating consume this capability in their own chapters rather than defining separate analyzer baselines.
- In other words, [chapter 2](02-developer-environment.md) explains how contributors run checks locally, while this chapter explains which analyzers and rules those commands should carry.
- Runtime-driven techniques such as coverage, sanitizers, fuzzing, and profiling belong in [chapter 4](04-testing-infrastructure.md), not here.
- Dependency alerts, supply-chain analysis of dependency sets, and continuous SBOM monitoring belong in [chapter 6](06-compliance-infrastructure.md), not here.
- **Biggest gap**: code analysis is not yet defined and governed as one cross-repository capability with shared tooling, rule baselines, and ownership expectations.

## 5.1 Tooling Baseline ⚪

*Defining which static analysis tools are approved, recommended, or required for different S-CORE repository types and languages.*

**S-CORE**

- Code analysis in S-CORE includes linters, type/interface analyzers, style and import checks, and security-oriented analyzers where appropriate.
- Tool choice is currently influenced by language ecosystems, repository classes, and existing engineering practice.
- **Biggest gap**: no explicit cross-repository baseline defines which analyzers are expected by default for C++, Rust, Python, and workflow or documentation assets.

### 5.1.1 Tool Selection Criteria

*Choosing analyzers that fit S-CORE repository needs and can be maintained at scale.*

**S-CORE**

- Tooling decisions should favor analyzers that can be shared across repositories, versioned centrally, and consumed consistently by local and automated execution environments.
- Shared tools should produce machine-readable results where possible so reporting and policy gates can consume them consistently.
- **Biggest gap**: selection criteria are implicit and repository-specific instead of centrally documented and reviewable.

### 5.1.2 Repository and Language Baselines

*Establishing default analyzer sets for major repository classes and implementation languages.*

**S-CORE**

- Different repository types need different analyzer sets, but the expected baseline should still be centrally defined.
- Repository-specific additions are valid when justified by language, framework, or safety needs.
- **Biggest gap**: baseline analyzer bundles and ownership of deviations are not yet described in one shared place.

### 5.1.3 Non-Code Asset Analysis

*Applying analyzers to workflows, documentation, configuration, and other repository assets beyond source code.*

**S-CORE**

- Repository quality and security depend on more than product code; workflow files, configuration, and documentation assets also need automated inspection.
- **Biggest gap**: the analyzer baseline for non-code repository assets is even less defined than the baseline for implementation languages.

---

## 5.2 Shared Rule Configuration ⚪

*Managing analyzer rules, severities, suppressions, and versioning as shared infrastructure instead of ad-hoc repository detail.*

**S-CORE**

- Shared rule configurations are an important part of repository standards and should be versioned like other infrastructure policy artifacts.
- Repository overrides should be explicit, limited, and explainable rather than silent drift from the shared baseline.

In the current S-CORE repository landscape, these shared rules are increasingly packaged as separate policy modules rather than being folded into toolchain repositories. That is why repositories such as `score_rust_policies` and `score_cpp_policies` belong to this chapter's perspective, while `toolchains_rust` and `bazel_cpp_toolchains` belong to [chapter 3](03-build-infrastructure.md#toolchain-management). The important architectural rule is that consumers should be able to adopt shared lint, warning, and formatting baselines without having to change compiler versions or Bazel toolchain registration at the same time. When such a policy also exposes selectable runtime-oriented features such as sanitizers, [chapter 4](04-testing-infrastructure.md#sanitizers-runtime-checks) still owns why and when those checks are executed; this chapter owns only the reusable rule baseline.

### 5.2.1 Baseline Rulesets

*Defining centrally maintained defaults for analyzer configuration.*

**S-CORE**

- Central baselines should define default enabled checks, severity handling, and common exclusions.
- Baselines should be reusable in templates, synchronized configuration, or shared workflow inputs.
- **Biggest gap**: there is no visible authoritative baseline for static-analysis rules across S-CORE repositories.

### 5.2.2 Overrides and Suppressions

*Allowing repository-specific exceptions without losing visibility or governance.*

**S-CORE**

- Overrides and suppressions are sometimes necessary for migration, generated code, third-party constraints, or language-specific false positives.
- Exceptions should be narrow, reviewable, and traceable so that debt can be reduced over time.
- **Biggest gap**: suppressions and local overrides are not yet governed by a shared policy for justification, expiry, or review.

---

## 5.3 Execution Model ⚪

*Defining where and how the shared static-analysis capability should be executed across the engineering flow.*

**S-CORE**

- Static analysis should be executable in multiple contexts, especially local development and CI, without redefining analyzer baselines per context.
- Different execution contexts can use different subsets or frequencies, but they should all derive from the same shared rules and ownership model.
- **Biggest gap**: there is no documented execution model that cleanly separates shared analyzer policy from local and CI-specific delivery.

### 5.3.1 Local Execution Expectations

*Defining what static analysis should provide before code reaches CI.*

**S-CORE**

- Contributors should be able to run the shared analyzer baseline early enough to catch common issues before opening or updating a pull request.
- Local execution should favor fast feedback and alignment with the centrally defined ruleset, while the delivery details for shared environments, editor usage, and pre-commit belong in [chapter 2](02-developer-environment.md).
- **Biggest gap**: local execution expectations are not yet defined independently of specific tools such as devcontainers, IDEs, or pre-commit hooks.

### 5.3.2 CI Execution Expectations

*Defining what CI should enforce from the shared static-analysis capability.*

**S-CORE**

- CI should execute the agreed shared analyzer baseline in a consistent, review-visible way and use its outcomes for merge decisions where appropriate.
- The workflow, reporting, and branch-protection mechanics belong in [chapter 7](07-automation-integration.md), not in the code-analysis capability definition itself.
- **Biggest gap**: CI enforcement expectations are not yet clearly separated from workflow implementation details.

### 5.3.3 Incremental Adoption

*Rolling out stronger analyzer baselines without blocking repository progress all at once.*

**S-CORE**

- A shared analysis strategy should support migration from weak or inconsistent baselines toward stronger common enforcement.
- **Biggest gap**: there is no documented rollout model for moving repositories from optional analysis toward required shared baselines.

---

## 5.4 Security Scanning 🟠

*Clarifying how code analysis relates to security-oriented scanning of source and repository configuration.*

**S-CORE**

- Code analysis includes both general code-quality checks and security-relevant inspection of source and repository configuration.
- This chapter is the canonical home for shared tooling, rule configuration, and execution boundaries that are common across analyzer types.
- **Biggest gap**: the boundary between quality-oriented analyzers and security scanning is not yet described clearly enough to avoid duplication and ownership gaps.

### 5.4.1 SAST 🟠

*Static application security testing for S-CORE code and configuration.*

**S-CORE**

SAST tools analyze source code for security vulnerabilities without executing it. For S-CORE, CodeQL is the primary SAST tool because it integrates natively with GitHub through code scanning alerts, supports C/C++ and Python analysis relevant to the S-CORE language landscape, and can run as a standard GitHub Actions workflow. The infrastructure question is not whether CodeQL works — it does — but how it is configured consistently: which query suites are enabled, what severity thresholds gate a merge, and how results are surfaced to maintainers.

A useful SAST configuration has three layers. The query suite defines which vulnerability patterns to look for — the default security suite covers the most impactful findings, while extended suites add code-quality checks at the cost of more noise. The CI gate defines which findings block merges — typically only high and critical severity — while lower findings appear as alerts for maintainers to triage. The cross-repository alignment defines whether all S-CORE repositories use the same query suite and gate policy or whether repositories can override the baseline.

**Biggest gap**: SAST-specific configuration and required security-gate policies are not yet standardized across repositories. CodeQL query suite selection and severity thresholds vary between repositories.

### 5.4.2 Secret Scanning 🟠

*Detecting secrets inadvertently committed to S-CORE repositories.*

**S-CORE**

- GitHub secret scanning detects common credential patterns in repository history and ongoing changes.
- **Biggest gap**: custom secret patterns and push-protection configuration are not uniformly enabled.

### 5.4.3 Repository Configuration Security

*Inspecting workflows and repository configuration for risky patterns before they become incidents.*

**S-CORE**

- Infrastructure repositories depend heavily on workflow configuration, permissions, and automation wiring, so configuration-level analysis is a meaningful part of code-analysis security scanning.
- **Biggest gap**: configuration-oriented security analysis is not yet described as part of a shared S-CORE baseline.

---

## 5.5 Results and Governance ⚪

*Managing findings, conformance visibility, and analyzer evolution across repositories.*

**S-CORE**

- Code-analysis infrastructure should provide visibility into adoption, drift, and findings without forcing every repository to invent its own process.
- Governance includes rule changes, false-positive handling, technical-debt baselines, and measurement of conformance to shared expectations.
- **Biggest gap**: no cross-repository reporting and governance loop currently shows which repositories run which analyzers, with what deviations and outcomes.

### 5.5.1 False Positives and Baselines

*Handling existing findings and noisy rules in a controlled way.*

**S-CORE**

- Migration to stronger analyzers often needs temporary baselines or approved suppressions so repositories can improve incrementally.
- **Biggest gap**: there is no shared approach for introducing analyzers into repositories with existing finding backlogs.

### 5.5.2 Cross-Repository Visibility

*Measuring adoption and conformance of static-analysis standards across S-CORE.*

**S-CORE**

- Cross-repository reporting should show baseline adoption, exceptions, and required-check coverage, not just individual CI job output.
- **Biggest gap**: no common dashboard or conformance report currently summarizes static-analysis coverage across S-CORE.
# 4 Static Analysis Infrastructure ⚪

*Infrastructure for inspecting S-CORE source code and configuration without executing the software, to enforce quality, consistency, and security expectations across repositories.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Static analysis complements testing by finding issues through code and configuration inspection instead of runtime verification.
- This chapter defines the shared capability: analyzer scope, baseline expectations, rule governance, and ownership boundaries across repositories.
- Local execution and CI gating consume this capability in their own chapters rather than defining separate analyzer baselines.
- **Biggest gap**: static analysis is not yet defined and governed as one cross-repository capability with shared tooling, rule baselines, and ownership expectations.

## 4.1 Tooling Baseline ⚪

*Defining which static analysis tools are approved, recommended, or required for different S-CORE repository types and languages.*

**S-CORE**

- Static analysis in S-CORE includes linters, type/interface analyzers, style and import checks, and security-oriented analyzers where appropriate.
- Tool choice is currently influenced by language ecosystems, repository classes, and existing engineering practice.
- **Biggest gap**: no explicit cross-repository baseline defines which analyzers are expected by default for C++, Rust, Python, and workflow or documentation assets.

### 4.1.1 Tool Selection Criteria

*Choosing analyzers that fit S-CORE repository needs and can be maintained at scale.*

**S-CORE**

- Tooling decisions should favor analyzers that can be shared across repositories, versioned centrally, and consumed consistently by local and automated execution environments.
- Shared tools should produce machine-readable results where possible so reporting and policy gates can consume them consistently.
- **Biggest gap**: selection criteria are implicit and repository-specific instead of centrally documented and reviewable.

### 4.1.2 Repository and Language Baselines

*Establishing default analyzer sets for major repository classes and implementation languages.*

**S-CORE**

- Different repository types need different analyzer sets, but the expected baseline should still be centrally defined.
- Repository-specific additions are valid when justified by language, framework, or safety needs.
- **Biggest gap**: baseline analyzer bundles and ownership of deviations are not yet described in one shared place.

---

## 4.2 Shared Rule Configuration 🟠

*Managing analyzer rules, severities, suppressions, and versioning as shared infrastructure instead of ad-hoc repository detail.*

**S-CORE**

- Shared rule configurations are an important part of repository standards and should be versioned like other infrastructure policy artifacts.
- Repository overrides should be explicit, limited, and explainable rather than silent drift from the shared baseline.
- **Biggest gap**: no documented baseline-versus-override model exists for static-analysis rules across repository classes.

### 4.2.1 Baseline Rulesets

*Defining centrally maintained defaults for analyzer configuration.*

**S-CORE**

- Central baselines should define default enabled checks, severity handling, and common exclusions.
- Baselines should be reusable in templates, synchronized configuration, or shared workflow inputs.
- **Biggest gap**: there is no visible authoritative baseline for static-analysis rules across S-CORE repositories.

### 4.2.2 Overrides and Suppressions

*Allowing repository-specific exceptions without losing visibility or governance.*

**S-CORE**

- Overrides and suppressions are sometimes necessary for migration, generated code, third-party constraints, or language-specific false positives.
- Exceptions should be narrow, reviewable, and traceable so that debt can be reduced over time.
- **Biggest gap**: suppressions and local overrides are not yet governed by a shared policy for justification, expiry, or review.

---

## 4.3 Execution Model 🟠

*Defining where and how the shared static-analysis capability should be executed across the engineering flow.*

**S-CORE**

- Static analysis should be executable in multiple contexts, especially local development and CI, without redefining analyzer baselines per context.
- Different execution contexts can use different subsets or frequencies, but they should all derive from the same shared rules and ownership model.
- **Biggest gap**: there is no documented execution model that cleanly separates shared analyzer policy from local and CI-specific delivery.

### 4.3.1 Local Execution Expectations

*Defining what static analysis should provide before code reaches CI.*

**S-CORE**

- Contributors should be able to run the shared analyzer baseline early enough to catch common issues before opening or updating a pull request.
- Local execution should favor fast feedback and alignment with the centrally defined ruleset, while the delivery details belong in [chapter 10](developer-environment.md).
- **Biggest gap**: local execution expectations are not yet defined independently of specific tools such as devcontainers, IDEs, or pre-commit hooks.

### 4.3.2 CI Execution Expectations

*Defining what CI should enforce from the shared static-analysis capability.*

**S-CORE**

- CI should execute the agreed shared analyzer baseline in a consistent, review-visible way and use its outcomes for merge decisions where appropriate.
- The workflow, reporting, and branch-protection mechanics belong in [chapter 5](automation-integration.md), not in the static-analysis capability definition itself.
- **Biggest gap**: CI enforcement expectations are not yet clearly separated from workflow implementation details.

---

## 4.4 Boundary to Security Static Analysis ⚪

*Clarifying how general static analysis relates to security scanning and SAST.*

**S-CORE**

- Static analysis includes both general code-quality checks and security-relevant inspection, but the security program and its policies remain part of [chapter 11](security-infrastructure.md).
- This chapter is the canonical home for shared tooling, rule configuration, and ownership boundaries that are common across analyzer types.
- **Biggest gap**: the boundary between quality-oriented analyzers and security scanning is not yet described clearly enough to avoid duplication and ownership gaps.

### 4.4.1 Shared Foundations

*Capabilities shared by quality and security analyzers.*

**S-CORE**

- Tool distribution, execution semantics, baseline configuration, and suppression governance are shared infrastructure concerns across analyzer types.
- These shared foundations should be managed once and referenced by both engineering-quality and security documentation.
- **Biggest gap**: SAST is discussed mainly as a security feature, while its shared infrastructure dependencies are not documented holistically.

### 4.4.2 Security-Specific Ownership

*Keeping security policy and risk handling in the security chapter.*

**S-CORE**

- Security-specific topics such as vulnerability triage, security ownership, risk acceptance, and required security gates belong in [chapter 11](security-infrastructure.md).
- This separation keeps the static-analysis chapter focused on shared engineering infrastructure rather than security governance detail.
- **Biggest gap**: ownership boundaries for SAST configuration versus broader static-analysis infrastructure are not yet explicit.

---

## 4.5 Results and Governance ⚪

*Managing findings, conformance visibility, and analyzer evolution across repositories.*

**S-CORE**

- Static-analysis infrastructure should provide visibility into adoption, drift, and findings without forcing every repository to invent its own process.
- Governance includes rule changes, false-positive handling, technical-debt baselines, and measurement of conformance to shared expectations.
- **Biggest gap**: no cross-repository reporting and governance loop currently shows which repositories run which analyzers, with what deviations and outcomes.

### 4.5.1 False Positives and Baselines

*Handling existing findings and noisy rules in a controlled way.*

**S-CORE**

- Migration to stronger analyzers often needs temporary baselines or approved suppressions so repositories can improve incrementally.
- These mechanisms should reduce noise without hiding ownership or turning exceptions into permanent blind spots.
- **Biggest gap**: there is no shared approach for introducing analyzers into repositories with existing finding backlogs.

### 4.5.2 Cross-Repository Visibility

*Measuring adoption and conformance of static-analysis standards across S-CORE.*

**S-CORE**

- Cross-repository reporting should show baseline adoption, exceptions, and required-check coverage, not just individual CI job output.
- This visibility is needed to prioritize migrations and understand where enforcement is still missing.
- **Biggest gap**: no common dashboard or conformance report currently summarizes static-analysis coverage across S-CORE.

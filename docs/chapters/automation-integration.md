# 5 Automation Infrastructure & Continuous Integration (CI/CD) ⚪

*Infrastructure integrating code changes safely across S-CORE repositories through automated workflows and quality gates.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- GitHub Actions is the CI/CD platform for S-CORE; workflows are triggered on pull requests and merges.
- Reusable workflows shared across repositories reduce duplication and enforce consistent pipeline structure.
- Pipeline execution relies on both GitHub-hosted cloud runners and hardware test runners.
- **Biggest gap**: reusable workflow coverage and quality gate consistency across S-CORE repositories are incomplete.

## 5.1 Runners 🟠

*Execution infrastructure used by S-CORE CI pipelines.*

**S-CORE**

- Pipeline execution relies on GitHub-hosted cloud runners and dedicated hardware test runners.
- **Biggest gap**: hardware runner availability and reliability remain a bottleneck for integration pipelines.

### 5.1.1 SW Test Runners 🟡

*GitHub-hosted runners providing execution environments for CI pipelines.*

**S-CORE**

- Cloud runners cover ARM, x86, and QEMU (with KVM) architectures with autoscaling to match pipeline demand.
- **Biggest gap**: runner capacity constraints under peak load are not yet fully mitigated.

### 5.1.2 Hardware Test Runners 🔴

*Execution environments for hardware-based testing in S-CORE CI pipelines.*

**S-CORE**

- **Biggest gap**: availability and reliability of hardware runners are not yet at a level that enables consistent automated hardware testing across S-CORE.

---

## 5.2 Reusable Workflows ⚪

*Shared GitHub Actions workflows reused across S-CORE repositories.*

**S-CORE**

- Workflows are defined in `.github/workflows/` per repository; reusable workflows are hosted centrally for cross-repository use.
- Reusable workflows are intended to standardize build, test, and compliance steps across repositories.
- Required status checks are configured centrally via [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet).
- **Biggest gap**: reusable workflow coverage is partial and quality gate definitions are not yet consistently enforced via shared workflows.

### 5.2.1 Workflow Library Coverage

*Completeness of centrally maintained reusable workflows for common CI patterns.*

**S-CORE**

- A shared reusable workflow library exists but does not yet cover all standard S-CORE pipeline scenarios.
- **Biggest gap**: a complete baseline library for standard build, test, and compliance patterns is not yet fully defined.

### 5.2.2 Build Validation

*Ensuring builds succeed before code is merged, using standardized workflow building blocks.*

**S-CORE**

- Build success is a required check for merges in S-CORE repositories via branch protection configuration.
- **Biggest gap**: build validation implementation details still vary by repository maturity.

### 5.2.3 Test Validation

*Ensuring tests pass before code is merged, with reusable test workflow patterns.*

**S-CORE**

- Test results gate merges in repositories where test pipelines are set up.
- **Biggest gap**: test gate coverage remains incomplete across S-CORE repositories.

### 5.2.4 Static Analysis Enforcement

*Executing shared static-analysis checks as reusable CI workflow steps and merge gates.*

**S-CORE**

- CI consumes the shared static-analysis capability described in [chapter 4](static-analysis-infrastructure.md) and turns it into workflow runs, status checks, and review-visible results.
- Reusable workflows should encapsulate execution and reporting so repositories do not reimplement the same enforcement mechanics.
- **Biggest gap**: reusable workflow coverage and required-check policy for static-analysis gates are not yet consistently applied across repositories.

---

## 5.3 Cross-Repository Integration ⚪

*Validating integration scenarios across S-CORE components in CI beyond single-repository scope.*

**S-CORE**

- Cross-repository integration validation is a target capability; most repositories currently validate in isolation.
- **Biggest gap**: no shared integration validation pipeline spans multiple S-CORE middleware components.

### 5.3.1 Integration Validation Scope

*Defining which component combinations and dependency chains are validated together.*

**S-CORE**

- Integration coverage is currently limited and often project-specific instead of platform-wide.
- **Biggest gap**: no agreed minimum integration matrix is defined for S-CORE.

### 5.3.2 Integration Pipeline Orchestration

*Coordinating multi-repository builds and tests as one automated CI flow.*

**S-CORE**

- Multi-repository orchestration is a target capability and not yet standardized.
- **Biggest gap**: trigger, artifact handover, and result aggregation patterns are not yet unified.

---

## 5.4 Secrets Management ⚪

*Protecting credentials and establishing least-privilege access for CI workflows and runners.*

**S-CORE**

- CI workflows rely on repository, organization, and environment secrets for accessing external systems.
- OIDC-based short-lived credentials are the preferred pattern where supported, reducing long-lived static secrets.
- **Biggest gap**: centralized secret inventory, rotation policy enforcement, and usage audits are not yet consistently implemented.

### 5.4.1 Secret Scope and Rotation

*Managing where secrets are stored and how frequently they are rotated.*

**S-CORE**

- Secret scoping follows GitHub constructs (repository, organization, environment), but conventions differ between repositories.
- **Biggest gap**: no uniform rotation cadence and ownership model is enforced across all CI secrets.

### 5.4.2 Federated Identity (OIDC)

*Replacing static credentials with short-lived identity federation for CI jobs.*

**S-CORE**

- OIDC adoption is progressing for cloud access use cases where providers support federated trust.
- **Biggest gap**: OIDC usage is not yet standardized across all repositories and target environments.

---

## 5.5 CI Observability ⚪

*Monitoring CI health, performance, and reliability to improve developer feedback loops.*

**S-CORE**

- CI observability relies on GitHub Actions logs, job outcomes, and repository status checks.
- Key indicators include queue times, job durations, failure rate, and flaky test behavior.
- **Biggest gap**: no shared observability baseline or dashboard is used consistently across S-CORE repositories.

### 5.5.1 Pipeline Health Metrics

*Tracking execution and quality signals to detect bottlenecks and reliability issues early.*

**S-CORE**

- Pipeline metrics exist in native tooling but are not yet normalized into common S-CORE KPIs.
- **Biggest gap**: threshold definitions and trend tracking are not centrally aligned.

### 5.5.2 Alerting and Incident Response

*Reacting quickly to CI outages, widespread failures, or degraded feedback latency.*

**S-CORE**

- Notification and incident handling practices exist but differ between repositories and teams.
- **Biggest gap**: no standard CI incident playbook with shared escalation paths is applied platform-wide.

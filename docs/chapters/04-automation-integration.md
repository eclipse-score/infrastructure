# 4 Automation Infrastructure & Continuous Integration (CI/CD) ⚪

*Infrastructure integrating code changes safely across S-CORE repositories through automated workflows and quality gates.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- GitHub Actions is the CI/CD platform for S-CORE; workflows are triggered on pull requests and merges.
- Reusable workflows shared across repositories reduce duplication and enforce consistent pipeline structure.
- Pipeline execution relies on both GitHub-hosted cloud runners and hardware test runners.
- **Biggest gap**: reusable workflow coverage and quality gate consistency across S-CORE repositories are incomplete.

## 4.1 CI Workflow Architecture ⚪

*Structure and reuse patterns for CI workflows across S-CORE.*

**S-CORE**

- Workflows are defined in `.github/workflows/` per repository; reusable workflows are hosted centrally for cross-repository use.
- **Biggest gap**: a shared reusable workflow library covering standard pipeline patterns is not yet fully defined.

### 4.1.1 Reusable Workflows

*Shared GitHub Actions workflows reused across S-CORE repositories.*

**S-CORE**

- Reusable workflows are provided to standardize build, test, and compliance steps across repositories.
- **Biggest gap**: reusable workflow coverage is partial; many repositories still inline their own pipeline logic.

---

## 4.2 Pipeline Execution 🟠

*Infrastructure providing the execution environments for CI pipelines.*

**S-CORE**

- Pipelines run on GitHub-hosted runners (ARM, x86, QEMU/KVM) managed by the ETAS INFRA team.
- Hardware test runners for firmware and board-level tests are operated by the ETAS INT team.
- **Biggest gap**: hardware runner availability and stability remain a bottleneck for integration pipelines.

### 4.2.1 Cloud Runners 🟡

*GitHub-hosted runners providing execution environments for CI pipelines.*

**S-CORE**

- Cloud runners cover ARM, x86, and QEMU (with KVM) architectures with autoscaling to match pipeline demand.
- Managed by ETAS INFRA team.
- **Biggest gap**: runner capacity constraints under peak load are not yet fully mitigated.

### 4.2.2 Hardware Test Runners 🔴

*Execution environments for hardware-based testing in S-CORE CI pipelines.*

**S-CORE**

- Hardware test runners are operated by the ETAS INT team for firmware and board-level CI tests.
- **Biggest gap**: availability and reliability of hardware runners are not yet at a level that enables consistent automated hardware testing across S-CORE.

---

## 4.3 Quality Gates ⚪

*Automated validation checks that must pass before code is merged into S-CORE repositories.*

**S-CORE**

- Required status checks are configured centrally via [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet).
- **Biggest gap**: quality gate definitions vary across repositories; a standard minimum gate set is not enforced.

### 4.3.1 Build Validation

*Ensuring builds succeed before code is merged.*

**S-CORE**

- Build success is a required check for merges in S-CORE repositories via branch protection configuration.
- **Biggest gap**: build validation coverage varies by repository maturity.

### 4.3.2 Test Validation

*Ensuring tests pass before code is merged.*

**S-CORE**

- Test results gate merges in repositories where test pipelines are set up.
- **Biggest gap**: test gate coverage is incomplete across S-CORE repositories.

### 4.3.3 Static Analysis

*Automated linting and static analysis as part of the CI pipeline.*

**S-CORE**

- Static analysis tools are integrated into CI pipelines in some repositories; standardization is incomplete.
- **Biggest gap**: no shared static analysis tool set or required quality gate is uniformly enforced.

### 4.3.4 Integration

*Validating integration scenarios across S-CORE components in CI.*

**S-CORE**

- Cross-repository integration validation is a target capability; most repositories only validate in isolation.
- **Biggest gap**: no shared integration validation pipeline spans multiple S-CORE middleware components.

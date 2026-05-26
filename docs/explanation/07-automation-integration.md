# 7 Automation Infrastructure & Continuous Integration (CI) ⚪

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure integrating code changes safely across S-CORE repositories through automated workflows and quality gates.*

:::{warning} Draft
This chapter has not been fully reviewed. Content may be incomplete or inaccurate.
:::

**S-CORE**

GitHub Actions is the CI/CD platform for S-CORE. Workflows are triggered on pull requests, merges, schedules, and releases. Reusable workflows shared across repositories reduce duplication and enforce consistent pipeline structure. Pipeline execution relies on both GitHub-hosted cloud runners and hardware-oriented execution environments. This chapter owns workflow orchestration and gate delivery, including cases where CI reuses the shared contributor environment from [chapter 2](02-developer-environment.md), not the technical baselines defined in [chapter 3](03-build-infrastructure.md), [chapter 4](04-testing-infrastructure.md), [chapter 5](05-static-analysis-infrastructure.md), and [chapter 6](06-compliance-infrastructure.md).

Because GitHub Actions is a managed platform, its constraints shape what workflows can and cannot do. The most consequential constraints include: workflow storage quotas that limit how much artifact data a repository can retain across runs, concurrency limits that determine how many jobs can run in parallel per organization, runner disk space that constrains large Bazel builds and Docker-in-Docker workloads, the split between `GITHUB_TOKEN` and fine-grained PAT permissions that affects cross-repository access, and the inability to share mutable state between jobs except through artifacts or caches. For self-hosted runners, additional constraints include node pool sizing, network access to internal resources, and the security implications of running untrusted pull-request code on persistent infrastructure. Established patterns that work well in S-CORE include using composite actions for Bazel setup and teardown, restricting `workflow_dispatch` and `pull_request_target` triggers to workflows that explicitly need elevated permissions, and using reusable workflows rather than copying common steps between repositories.

**Biggest gap**: reusable workflow coverage and quality gate consistency across S-CORE repositories are incomplete. GitHub Actions platform constraints and S-CORE-specific best practices are not documented in one place.

```{mermaid}
graph TD
    pr["Pull request / push"]
    schedule["Schedule / release trigger"]

    subgraph shared["Shared workflow libraries"]
        cwf["`cicd-workflows
on-pr.yml · daily.yml`"]
        cac["`cicd-actions
(composite actions)`"]
    end

    subgraph runners["Runners"]
        cloud["`GitHub-hosted
(cloud: x86, ARM, KVM)`"]
        hw["`Self-hosted
(hardware: RPi, automotive SoC)`"]
    end

    pr --> cwf
    schedule --> cwf
    cwf --> cac
    cac --> cloud
    cac --> hw
    cloud --> results["`Status checks
Artifacts / evidence`"]
    hw --> results
    results -->|"required checks via otterdog"| pr
```

## 7.1 Runners 🟠

*Execution infrastructure used by S-CORE CI pipelines.*

**S-CORE**

- Pipeline execution relies on GitHub-hosted cloud runners and dedicated hardware test runners.
- **Biggest gap**: hardware runner availability and reliability remain a bottleneck for integration pipelines.

### 7.1.1 SW Test Runners 🟡

*GitHub-hosted runners providing execution environments for CI pipelines.*

**S-CORE**

- Cloud runners cover ARM, x86, and QEMU (with KVM) architectures with autoscaling to match pipeline demand.
- **Biggest gap**: runner capacity constraints under peak load are not yet fully mitigated.

### 7.1.2 Hardware Test Runners 🔴

*Execution environments for hardware-based testing in S-CORE CI pipelines.*

**S-CORE**

Hardware test runners differ from cloud runners in almost every dimension. A cloud runner is an ephemeral VM that executes a job and disappears; a hardware runner is a persistent physical device — an embedded board, an automotive-grade SoC, or a development kit — that must be provisioned, maintained, and shared across pipelines. The infrastructure challenge is not just making hardware available, but making it usable as a CI execution target with the same trigger-run-report model that cloud runners already provide.

The practical need in S-CORE comes from two directions. Cross-compiled test execution ([section 4.3](04-testing-infrastructure.md#test-execution-dynamic-analysis)) needs a way to run `cc_test` and `rust_test` binaries built for non-host platforms such as QNX on an actual target or a representative emulator. Performance and benchmark testing ([section 4.3.4](04-testing-infrastructure.md#performance-benchmark-testing)) needs to measure timing, throughput, and resource consumption on real hardware where host-based emulation cannot reproduce the actual behavior. Both depend on the same underlying provisioning model.

The target hardware landscape currently includes single-board computers such as Raspberry Pi for lightweight integration and smoke testing, and automotive-grade SoCs such as the Qualcomm SA8650P for representative performance measurement and platform-level validation. Each class brings different constraints: single-board computers are cheap and easy to provision but limited in compute; automotive SoCs are representative but expensive, scarce, and often require vendor-specific BSPs and boot infrastructure. A viable hardware runner model must account for both ends of that spectrum.

The infrastructure layers that need to exist are: physical device management and health monitoring, a deployment mechanism that flashes or transfers test binaries and their dependencies to the target, a remote execution model that triggers test runs and collects results back into the CI pipeline, and an isolation strategy that prevents concurrent jobs from interfering with each other on shared devices. For GitHub Actions integration, this typically means self-hosted runners attached to specific device classes, with job routing based on labels that encode the target platform and availability.

**Biggest gap**: S-CORE has no documented hardware runner provisioning model, no deployment and result collection pipeline for embedded targets, and no device management or scheduling infrastructure. Hardware test execution is currently ad hoc rather than a reproducible CI capability.

### 7.1.3 Execution Isolation & Trust Boundaries

*Separating jobs and credentials appropriately across runner classes and workflow contexts.*

**S-CORE**

- CI execution environments should make trust boundaries explicit, especially when different jobs handle external contributions, internal credentials, or hardware access.
- **Biggest gap**: there is no clearly documented execution trust model across the different runner types used in S-CORE workflows.

## 7.2 Reusable Workflows ⚪

*Shared GitHub Actions workflows reused across S-CORE repositories.*

**S-CORE**

Reusable workflows are maintained in [eclipse-score/cicd-workflows](https://github.com/eclipse-score/cicd-workflows) and reusable composite actions in [eclipse-score/cicd-actions](https://github.com/eclipse-score/cicd-actions). Module repositories call these shared workflows to standardize build, test, analysis, documentation, and release steps. Two meta-workflows compose the individual checks into standard pipeline shapes: `on-pr.yml` for pull-request checks and `daily.yml` for scheduled maintenance. Required status checks are configured centrally via [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet).

When workflow consistency benefits from reusing the shared local environment described in [chapter 2](02-developer-environment.md), the workflow layer is still responsible for how that environment is invoked and gated.

**Biggest gap**: reusable workflow coverage is partial and quality gate definitions are not yet consistently enforced via shared workflows.

### 7.2.1 Workflow Library Coverage

*Completeness of centrally maintained reusable workflows for common CI patterns.*

**S-CORE**

The [cicd-workflows](https://github.com/eclipse-score/cicd-workflows) library already covers a broad set of pipeline patterns: build and test, formatting, copyright enforcement, lock file verification, documentation build and verification, static analysis, CodeQL security scanning, dependency license checking, C++ and Rust coverage, QNX cross-compilation, and template synchronization. The [cicd-actions](https://github.com/eclipse-score/cicd-actions) repository complements this with composite actions for cross-repository token provisioning and QNX SDP setup.

**Biggest gap**: the workflow library is substantial, but adoption is not yet universal. Some repositories still use local workflow copies instead of the shared library, and the full set of quality gates is not uniformly applied across all repository classes.

### 7.2.2 Build Validation

*Ensuring builds succeed before code is merged, using standardized workflow building blocks.*

**S-CORE**

- Build success is a required check for merges in S-CORE repositories via branch protection configuration.
- **Biggest gap**: build validation implementation details still vary by repository maturity.

Where repositories use dependency lock files, the CI perspective should be enforcement rather than regeneration: workflows should verify that committed files such as `MODULE.bazel.lock` and `uv.lock` are already up to date instead of silently rewriting them during the run.

### 7.2.3 Test Validation

*Ensuring tests pass before code is merged, with reusable test workflow patterns.*

**S-CORE**

- Test results gate merges in repositories where test pipelines are set up.
- **Biggest gap**: test gate coverage remains incomplete across S-CORE repositories.

### 7.2.4 Analysis Enforcement

*Executing shared code-analysis and dependency-analysis checks as reusable CI workflow steps and merge gates.*

**S-CORE**

- CI consumes the shared analysis capabilities described in [chapter 5](05-static-analysis-infrastructure.md) and [chapter 6](06-compliance-infrastructure.md) and turns them into workflow runs, status checks, and review-visible results.
- Reusable workflows should encapsulate execution and reporting so repositories do not reimplement the same enforcement mechanics.
- **Biggest gap**: reusable workflow coverage and required-check policy for analysis gates are not yet consistently applied across repositories.

### 7.2.5 Documentation & Release Workflows

*Supporting documentation publishing and release automation through shared pipeline building blocks.*

**S-CORE**

- Shared workflow infrastructure should cover more than compile-and-test paths.
- **Biggest gap**: non-build workflow patterns are not yet captured in one clearly reusable automation baseline.

---

## 7.3 Cross-Repository Integration ⚪

*Validating integration scenarios across S-CORE components in CI beyond single-repository scope.*

**S-CORE**

- Cross-repository integration validation is a target capability; most repositories currently validate in isolation.
- The integration environment itself belongs primarily to [chapter 4](04-testing-infrastructure.md); this chapter covers how CI orchestrates and gates it.
- **Biggest gap**: no shared integration validation pipeline spans multiple S-CORE middleware components.

### 7.3.1 Integration Validation Scope

*Defining which component combinations and dependency chains are validated together.*

**S-CORE**

- Integration coverage is currently limited and often project-specific instead of project-wide.
- **Biggest gap**: no agreed minimum integration matrix is defined for S-CORE.

### 7.3.2 Integration Pipeline Orchestration

*Coordinating multi-repository builds and tests as one automated CI flow.*

**S-CORE**

- Multi-repository orchestration is a target capability and not yet standardized.
- CI should be able to trigger shared environments such as `reference_integration`, pass the relevant module versions or revisions into them, and collect the resulting evidence.
- **Biggest gap**: trigger, artifact handover, and result aggregation patterns are not yet unified.

### 7.3.3 Artifact & Evidence Handover

*Passing build outputs, metadata, and test evidence safely between stages or repositories in one CI flow.*

**S-CORE**

- Cross-repository automation needs more than triggers; it also needs a repeatable way to hand off artifacts, SBOMs, and verification evidence between jobs or repositories.
- That handover may include the `known_good` manifest or identifier, module references resolved through `bazel_registry`, release assets, and the test outputs produced by `reference_integration`.
- **Biggest gap**: no shared artifact handover model exists for multi-repository automation scenarios.

### 7.3.4 Known-Good Promotion

*Using `reference_integration` to validate and promote integrated module sets in CI.*

**S-CORE**

`known_good` gives CI a stable unit of promotion. Module repositories can continue to publish releases, registry entries, or candidate revisions independently, but cross-repository automation needs one place where those inputs are assembled into a candidate stack, executed together, and either promoted or rejected with clear feedback. The important nuance is that CI does not treat `known_good` as a byproduct of Bazel resolution. It treats it as the higher-level control file that selects the candidate stack and can also carry automation metadata such as which branch should be followed for automatic updates.

Assuming the still-undecided Option 2 direction currently under discussion, `reference_integration` would own that promotion gate. For a pull request in one repository, CI would build a candidate manifest from the changed repository ref together with the last known-good refs for the other participating repositories, generate the Bazel-facing inputs needed for the integrated workspace from that manifest, and run the fast integration subset for early feedback. After merges, or on a schedule, `reference_integration` would build a fuller manifest from the latest eligible branches, run the deeper suite, and only on success update the stored `known_good` record. If the final scope of `reference_integration` is narrowed later, the same promotion pattern still makes sense, but the meaning of `known_good` must be reduced to the checks that are actually re-executed centrally.

That also gives the handover model a natural key: artifacts, SBOMs, reports, and logs should be traceable to the `known_good` identifier or manifest hash they were produced for rather than only to an individual repository run. **Biggest gap**: S-CORE has no standardized candidate-manifest construction, `known_good` promotion workflow, ownership model, or result schema for cross-repository CI.

The workflow shape described here follows the distributed-monolith integration model in [DR-002-Infra](https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html), while the stronger central ownership assumed in some sentences still depends on the unresolved Option 2 versus lighter-scope discussion in [DR-008-Int](https://github.com/qorix-group/score/blob/da4ea900f1eece5c8e795697d71e277446dca84e/docs/design_decisions/DR-008-int.rst?plain=1).

## 7.4 Secrets Management ⚪

*Protecting credentials and establishing least-privilege access for CI workflows and runners.*

**S-CORE**

- CI workflows rely on repository, organization, and environment secrets for accessing external systems.
- OIDC-based short-lived credentials are the preferred pattern where supported, reducing long-lived static secrets.
- **Biggest gap**: centralized secret inventory, rotation policy enforcement, and usage audits are not yet consistently implemented.

### 7.4.1 Secret Scope and Rotation

*Managing where secrets are stored and how frequently they are rotated.*

**S-CORE**

- Secret scoping follows GitHub constructs (repository, organization, environment), but conventions differ between repositories.
- **Biggest gap**: no uniform rotation cadence and ownership model is enforced across all CI secrets.

### 7.4.2 Federated Identity (OIDC)

*Replacing static credentials with short-lived identity federation for CI jobs.*

**S-CORE**

- OIDC adoption is progressing for cloud access use cases where providers support federated trust.
- **Biggest gap**: OIDC usage is not yet standardized across all repositories and target environments.

### 7.4.3 Workflow Permissions

*Defining the minimum permissions automation jobs need in order to operate safely.*

**S-CORE**

- GitHub workflow permissions, token scopes, and environment protections are part of automation infrastructure, not just repository-level policy trivia.
- **Biggest gap**: no shared least-privilege baseline governs permissions across S-CORE workflows.

## 7.5 CI Observability ⚪

*Monitoring CI health, performance, and reliability to improve developer feedback loops.*

**S-CORE**

- CI observability relies on GitHub Actions logs, job outcomes, and repository status checks.
- Key indicators include queue times, job durations, failure rate, and flaky test behavior.
- **Biggest gap**: no shared observability baseline or dashboard is used consistently across S-CORE repositories.

### 7.5.1 Pipeline Health Metrics

*Tracking execution and quality signals to detect bottlenecks and reliability issues early.*

**S-CORE**

- Pipeline metrics exist in native tooling but are not yet normalized into common S-CORE KPIs.
- **Biggest gap**: threshold definitions and trend tracking are not centrally aligned.

### 7.5.2 Alerting and Incident Response

*Reacting quickly to CI outages, widespread failures, or degraded feedback latency.*

**S-CORE**

- Notification and incident handling practices exist but differ between repositories and teams.
- **Biggest gap**: no standard CI incident playbook with shared escalation paths is applied project-wide.

### 7.5.3 Flakiness & Feedback Quality

*Improving trust in CI by detecting unstable jobs and reducing noisy feedback.*

**S-CORE**

- Developers lose trust in automation when failures are noisy, nondeterministic, or slow to diagnose.
- **Biggest gap**: no shared mechanism identifies unstable CI checks and turns them into actionable infrastructure work.
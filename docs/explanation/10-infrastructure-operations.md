# 10 Infrastructure Operations ⚪

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure for operating and maintaining the S-CORE engineering infrastructure.*

:::{warning} Draft
This chapter has not been fully reviewed. Content may be incomplete or inaccurate.
:::

**S-CORE**

- Infrastructure operations covers runner operations, monitoring, dependency maintenance, governance, and upkeep of shared services such as the Bazel registry and its UI.
- Some of the shared services used by S-CORE are operated by external providers or teams, especially in the runner space.
- Dependabot automates dependency updates for infrastructure tooling across repositories.
- **Biggest gap**: systematic monitoring, incident handling, and proactive maintenance processes are not yet consistently defined across S-CORE infrastructure.

## 10.1 CI Runner Operations ⚪

*Operating CI execution environments for S-CORE pipelines.*

**S-CORE**

- Self-hosted runner infrastructure may be operated outside the public S-CORE project, while public S-CORE CI also relies on GitHub-hosted runners.
- **Biggest gap**: dependency on external runner operations creates a gap in public contributor autonomy and visibility.

### 10.1.1 GitHub Public Runners

*GitHub-hosted runners used by S-CORE CI pipelines.*

**S-CORE**

- GitHub-hosted runners are the default execution environment for public S-CORE CI.
- **Biggest gap**: GitHub-hosted runner capacity and feature availability are outside S-CORE control.

### 10.1.2 Runner Configuration

*Managing runner environment configuration.*

**S-CORE**

- Runner configuration is managed through workflow YAML files and, for self-hosted runners, by external operating teams.
- **Biggest gap**: runner environment consistency and configuration documentation are not maintained in a central, public location.

### 10.1.3 Ownership & Boundaries

*Clarifying which parts of runner operations are owned inside S-CORE and which are external dependencies.*

**S-CORE**

- Contributors need a clearer model for which infrastructure concerns they can change directly and which depend on GitHub or external operators.
- **Biggest gap**: the operational boundary between project-owned configuration and externally operated execution services is not yet documented clearly enough.

---

## 10.2 Infrastructure Monitoring ⚪

*Monitoring CI usage, failures, and infrastructure health across S-CORE.*

**S-CORE**

- CI pipeline failures are visible via GitHub Actions; no proactive monitoring or alerting spans S-CORE repositories.
- Shared service monitoring should eventually include the Bazel registry publication path and the registry UI, not only CI pipelines.
- **Biggest gap**: no cross-repository infrastructure health dashboard or alert channel exists for S-CORE.

### 10.2.1 CI Usage Monitoring

*Monitoring CI usage patterns and capacity across S-CORE pipelines.*

**S-CORE**

- GitHub Actions provides per-repository usage metrics; no aggregated cross-repository view exists.
- **Biggest gap**: S-CORE-wide CI usage visibility and capacity planning are not operationalized.

### 10.2.2 Failure Monitoring

*Monitoring failures across S-CORE infrastructure systems.*

**S-CORE**

- Pipeline failures are surfaced per repository via GitHub; no S-CORE-wide failure tracking dashboard exists.
- Failures affecting the shared Bazel registry, its validation workflows, or the registry UI would block module publication or discovery across repositories.
- **Biggest gap**: recurring failure patterns across S-CORE pipelines and shared distribution services are not systematically detected.

### 10.2.3 Incident Coordination

*Coordinating response when infrastructure failures affect multiple repositories or teams.*

**S-CORE**

- Cross-repository incidents need lightweight coordination so contributors do not diagnose the same infrastructure problem independently.
- **Biggest gap**: there is no shared incident coordination and communication pattern for project-wide infrastructure problems.

---

## 10.3 Infrastructure Maintenance ⚪

*Keeping S-CORE infrastructure tooling and dependencies up to date.*

**S-CORE**

- Dependabot automates version and SHA updates for infrastructure dependencies across S-CORE repositories.
- **Biggest gap**: proactive maintenance beyond Dependabot (e.g. major tool upgrades, deprecation handling) is not yet structured.

### 10.3.1 Tool Updates

*Updating shared infrastructure tools across S-CORE repositories.*

**S-CORE**

- Tool upgrades (e.g. Bazel, docs-as-code, runner images) are performed reactively on a per-repository basis.
- **Biggest gap**: no coordinated tool update process or shared upgrade playbook exists across S-CORE.

### 10.3.2 Dependency Updates

*Updating infrastructure dependencies across S-CORE repositories.*

**S-CORE**

- [Dependabot](https://github.com/dependabot) automatically opens pull requests to bump dependency versions and SHA hashes.
- **Biggest gap**: Dependabot coverage is limited to supported dependency file types; non-standard lockfiles are not auto-updated.

### 10.3.3 Deprecation & Lifecycle Management

*Retiring outdated infrastructure components before they become operational risk.*

**S-CORE**

- Operational maintenance includes responding to upstream deprecations before they create outages.
- **Biggest gap**: there is no shared deprecation tracking and migration planning process for infrastructure components.

### 10.3.4 Shared Registry Services

*Maintaining the shared Bazel module registry and its consumer UI as part of S-CORE infrastructure.*

**S-CORE**

The shared Bazel registry at [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/) and the registry UI at [eclipse-score.github.io/bazel_registry_ui](https://eclipse-score.github.io/bazel_registry_ui/) are part of the live infrastructure surface for cross-repository dependency management. The full publication and consumption flow is described in [chapter 8](08-artifact-distribution.md#registry-based-distribution); this section is only about operating that service reliably.

Infrastructure maintainers therefore need to keep the registry repository, the automation that validates and publishes registry updates, the raw GitHub-hosted content that Bazel reads, and the GitHub Pages deployment of the companion [eclipse-score/bazel_registry_ui](https://github.com/eclipse-score/bazel_registry_ui) project working together. If the registry data is wrong, if validation breaks, or if the UI deployment is stale, module publication and discovery degrade across the project.

The [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md) should remain the canonical contributor guide for adding or updating module versions. Operations documentation should complement it with service ownership, monitoring, incident handling, and recovery guidance rather than copying the contributor workflow.

---

## 10.4 Infrastructure Governance ⚪

*Guiding and recording the evolution of S-CORE infrastructure.*

**S-CORE**

- Infrastructure decisions and policies are expected to be documented and version-controlled.
- **Biggest gap**: a structured decision record process and central policy repository are not yet operational across S-CORE.

### 10.4.1 Infrastructure Policies

*Defining policies governing S-CORE infrastructure usage.*

**S-CORE**

- Infrastructure usage policies (runner selection, dependency constraints, tooling standards) are not yet formally documented.
- **Biggest gap**: no central, versioned policy document set governs S-CORE infrastructure choices.

### 10.4.2 Infrastructure Decision Records

*Documenting major S-CORE infrastructure decisions.*

**S-CORE**

- Architecture Decision Records (ADRs) are a target practice for documenting significant infrastructure decisions.
- **Biggest gap**: no ADR process or repository is established for S-CORE infrastructure decisions.

### 10.4.3 Change Rollout & Communication

*Explaining how infrastructure changes are communicated across repositories.*

**S-CORE**

- Some cross-repository changes need more than a merged pull request; they also need timing and migration communication.
- **Biggest gap**: there is no documented rollout-and-communication model for changes that affect multiple S-CORE repositories.
# 9 Infrastructure Operations ⚪

*Infrastructure for operating and maintaining the S-CORE engineering infrastructure.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Infrastructure operations covers runner operations, monitoring, dependency maintenance, and governance.
- Dependabot automates dependency updates for infrastructure tooling across repositories.
- **Biggest gap**: systematic monitoring, incident handling, and proactive maintenance processes are not yet consistently defined across S-CORE infrastructure.

## 9.1 CI Runner Operations ⚪

*Operating CI execution environments for S-CORE pipelines — out of scope for public S-CORE.*

**S-CORE**

- Self-hosted runner infrastructure is operated by ETAS and is not part of the public S-CORE project.
- Public S-CORE CI relies on GitHub-hosted runners; no runner operations work is expected from S-CORE contributors.
- **Biggest gap**: dependency on external runner operations creates a gap in public contributor autonomy.

### 9.1.1 GitHub Public Runners

*GitHub-hosted runners used by S-CORE CI pipelines.*

**S-CORE**

- GitHub-hosted runners are the default execution environment for public S-CORE CI.
- **Biggest gap**: GitHub-hosted runner capacity and feature availability are outside S-CORE control.

### 9.1.2 Runner Configuration

*Managing runner environment configuration.*

**S-CORE**

- Runner configuration is managed through workflow YAML files and, for self-hosted runners, by the ETAS INFRA team.
- **Biggest gap**: runner environment consistency and configuration documentation are not maintained in a central, public location.

---

## 9.2 Infrastructure Monitoring ⚪

*Monitoring CI usage, failures, and infrastructure health across S-CORE.*

**S-CORE**

- CI pipeline failures are visible via GitHub Actions; no proactive monitoring or alerting spans S-CORE repositories.
- **Biggest gap**: no cross-repository infrastructure health dashboard or alert channel exists for S-CORE.

### 9.2.1 CI Usage Monitoring

*Monitoring CI usage patterns and capacity across S-CORE pipelines.*

**S-CORE**

- GitHub Actions provides per-repository usage metrics; no aggregated cross-repository view exists.
- **Biggest gap**: S-CORE-wide CI usage visibility and capacity planning are not operationalized.

### 9.2.2 Failure Monitoring

*Monitoring failures across S-CORE infrastructure systems.*

**S-CORE**

- Pipeline failures are surfaced per repository via GitHub; no S-CORE-wide failure tracking dashboard exists.
- **Biggest gap**: recurring failure patterns across S-CORE pipelines are not systematically detected.

---

## 9.3 Infrastructure Maintenance ⚪

*Keeping S-CORE infrastructure tooling and dependencies up to date.*

**S-CORE**

- Dependabot automates version and SHA updates for infrastructure dependencies across S-CORE repositories.
- **Biggest gap**: proactive maintenance beyond Dependabot (e.g., major tool upgrades, deprecation handling) is not yet structured.

### 9.3.1 Tool Updates

*Updating shared infrastructure tools across S-CORE repositories.*

**S-CORE**

- Tool upgrades (e.g., MkDocs, Bazel, runner images) are performed reactively on a per-repository basis.
- **Biggest gap**: no coordinated tool update process or shared upgrade playbook exists across S-CORE.

### 9.3.2 Dependency Updates

*Updating infrastructure dependencies across S-CORE repositories.*

**S-CORE**

- [Dependabot](https://github.com/dependabot) automatically opens pull requests to bump dependency versions and SHA hashes.
- **Biggest gap**: Dependabot coverage is limited to supported dependency file types; non-standard lockfiles are not auto-updated.

---

## 9.4 Infrastructure Governance ⚪

*Guiding and recording the evolution of S-CORE infrastructure.*

**S-CORE**

- Infrastructure decisions and policies are expected to be documented and version-controlled.
- **Biggest gap**: a structured decision record process and central policy repository are not yet operational across S-CORE.

### 9.4.1 Infrastructure Policies

*Defining policies governing S-CORE infrastructure usage.*

**S-CORE**

- Infrastructure usage policies (runner selection, dependency constraints, tooling standards) are not yet formally documented.
- **Biggest gap**: no central, versioned policy document set governs S-CORE infrastructure choices.

### 9.4.2 Infrastructure Decision Records

*Documenting major S-CORE infrastructure decisions.*

**S-CORE**

- Architecture Decision Records (ADRs) are a target practice for documenting significant infrastructure decisions.
- **Biggest gap**: no ADR process or repository is established for S-CORE infrastructure decisions.

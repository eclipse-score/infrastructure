# 1 Source Code Infrastructure 🟠

**Chapter Goal**

Define how S-CORE repositories are hosted, governed, and kept consistent over time across a large multi-repository landscape.

**S-CORE Model and State**

- Model: GitHub is the canonical source-code hosting platform for S-CORE repositories.
- Model: Lifecycle and policy management are intended to be centrally defined and automation-driven.
- Model: Standards should be versioned, measurable, and continuously synchronized across repositories.
- Current state: Hosting is established and operational.
- Current state: Lifecycle management is partially automated.
- Current state: Standards and synchronization capabilities are still evolving.

**Ownership and Interfaces**

- S-CORE infrastructure ownership defines the repository governance model and automation behavior.
- Repository maintainers consume the service by proposing and validating repository-specific intent.
- Policy and standards changes are expected to flow through reviewed configuration updates.

**References**

- S-CORE organization: https://github.com/eclipse-score
- Otterdog: https://github.com/eclipse-score/otterdog
- S-CORE org configuration example: https://github.com/eclipse-score/.eclipsefdn/blob/main/eclipse-score.jsonnet

## 1.0 Hosting 🟢

*Provide a stable, discoverable, and scalable hosting foundation for all S-CORE repositories.*

**S-CORE**

- Repositories are hosted in GitHub aligned with Eclipse governance on https://github.com/eclipse-score


## 1.1 Repository Lifecycle Management 🟠

*Infrastructure for repositories and repository configuration.*

### 1.1.1 Repository Provisioning & Lifecycle 🟡

*Infrastructure for creating, initializing, updating, and archiving repositories and executing lifecycle operations.*

**S-CORE**

- Desired repository state is defined centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet)
- Lifecycle transitions are configuration changes instead of manual one-off actions.
- **Biggest gap**: approval of changes is rather random and undefined.

### 1.1.2 Repository Policy Management 🔴

*Infrastructure for managing and synchronizing repository policies such as branch protection, and application thereof at scale.*

**S-CORE**

- Policy intent (for example branch protection and required checks) is expressed centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet)
- Exceptions are explicit, reviewed, and documented.
- **Biggest gap**: policies are not yet uniformly applied to all repositories.

---

## 1.2 Repository Standards ⚪

*Infrastructure defining standard elements expected across repositories and reducing unnecessary variation.*

**S-CORE**

- Standards are centrally defined and versioned.
- Repositories adopt standards directly or through synchronized templates/configuration.
- **Biggest gap**: consistency of adoption and conformance visibility remains limited.

### 1.2.1 Repository Metadata

*Infrastructure for maintaining standard project metadata such as LICENSE, README, and governance files.*

**S-CORE**

- Metadata expectations exist, but rollout and conformance visibility are not yet complete.
- Automated cross-repository conformance reporting is not yet in place.
- **Biggest gap**: no continuous cross-repository visibility of metadata conformance.

### 1.2.2 Tooling Configuration Standards

*Infrastructure for maintaining shared configuration for linters and development tools.*

**S-CORE**

- Shared conventions are emerging, but not yet uniformly synchronized.
- Baseline/override handling is not yet consistently defined across repository types.
- **Biggest gap**: no clearly enforced baseline/override model across repository classes.

---

## 1.3 Synchronization of Standards 🔴

*Infrastructure for keeping repositories aligned with evolving standards through shared templates and configuration synchronization.*

**S-CORE**

- Automation applies and reconciles standards from central definitions.
- Adoption and drift are tracked to prioritize migration work.
- Cross-repository synchronization is a target capability and remains incomplete.
- **Biggest gap**: drift metrics/reporting and migration playbooks are not yet consistently operationalized.

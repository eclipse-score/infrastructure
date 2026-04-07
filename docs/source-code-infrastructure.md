# 1 Source Code Infrastructure 🟡

*Infrastructure for hosting and governing repositories consistently across the S-CORE project.*

**S-CORE**

- GitHub is the canonical source-code hosting service for S-CORE repositories.
- This chapter answers questions such as "How are repositories provisioned and governed?" and "How do shared repository standards stay aligned over time?"
- Lifecycle and policy management are intended to be centrally defined and automation-driven.
- Standards should be versioned, measurable, and continuously synchronized across repositories.
- Build, test, and workflow behavior are owned in later chapters; this chapter owns the repository substrate they depend on.
- Hosting is established and operational; lifecycle and standards synchronization are only partially mature.
- **Biggest gap**: cross-repository consistency of policy and standards is not yet reliably enforced and measured.

## 1.1 Hosting & Organization ⚪

*Provide a stable, discoverable, and scalable hosting foundation for all S-CORE repositories.*

**S-CORE**

- Repositories are hosted in GitHub aligned with Eclipse governance on https://github.com/eclipse-score

### 1.1.1 Organization Structure

*Structuring repositories under a shared organizational home with clear ownership boundaries.*

**S-CORE**

- A common organization location makes repositories easier to discover, relate, and govern consistently.
- Shared hosting also enables organization-level settings, applications, and automation to be managed centrally.
- **Biggest gap**: repository ownership and organizational structure are visible operationally, but not yet described as a deliberate infrastructure model.

### 1.1.2 Repository Discovery

*Helping contributors and stakeholders find the right repositories and understand their role.*

**S-CORE**

- Discoverability depends not only on hosting location but also on repository naming, metadata, topics, and consistent descriptions.
- Good discovery infrastructure reduces onboarding friction and helps contributors navigate a growing repository landscape.
- **Biggest gap**: there is no shared discoverability standard for how S-CORE repositories should present themselves in GitHub.


## 1.2 Repository Lifecycle & Policies 🟠

*Defining how repositories are created, changed, and governed over time.*

**S-CORE**

- Repository lifecycle infrastructure includes provisioning, archival, branch protection, required checks, and other durable settings that shape repository behavior.
- The point is to make repository state intentional and reviewable instead of a collection of manual one-off admin actions.
- **Biggest gap**: lifecycle and policy intent are visible in tooling, but not yet applied and governed consistently enough across all repositories.

### 1.2.1 Repository Provisioning & Lifecycle 🟡

*Infrastructure for creating, initializing, updating, and archiving repositories and executing lifecycle operations.*

**S-CORE**

- Desired repository state is defined centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet)
- Lifecycle transitions are configuration changes instead of manual one-off actions.
- **Biggest gap**: approval of changes is rather random and undefined.

### 1.2.2 Repository Policy Management 🔴

*Infrastructure for managing and synchronizing repository policies such as branch protection, and application thereof at scale.*

**S-CORE**

- Policy intent (for example branch protection and required checks) is expressed centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet)
- Exceptions are explicit, reviewed, and documented.
- **Biggest gap**: policies are not yet uniformly applied to all repositories.

---

## 1.3 Repository Standards 🟡

*Define standard elements expected across repositories to reduce unnecessary variation.*

**S-CORE**

- Standards are centrally defined and versioned.
- Repositories adopt standards directly or through synchronized templates/configuration.
- These standards make repositories easier to discover, review, and automate across the broader S-CORE landscape.
- **Biggest gap**: consistency of adoption and conformance visibility remains limited.

### 1.3.1 Repository Metadata 🟡

*Define standard project metadata such as LICENSE, README, and governance files.*

**S-CORE**

- Metadata expectations exist, but rollout and conformance visibility are not yet complete.
- Automated cross-repository conformance reporting is not yet in place.
- **Biggest gap**: no continuous cross-repository visibility of metadata conformance.

### 1.3.2 Tooling Configuration Standards 🟠

*Define shared configuration for linters and development tools.*

**S-CORE**

- Shared conventions are emerging, but not yet uniformly synchronized; [chapter 5](static-analysis-infrastructure.md) is the canonical home for code-analysis tooling and rule-baseline details.
- Baseline/override handling is not yet consistently defined across repository types.
- **Biggest gap**: no clearly enforced baseline/override model across repository classes.

---

## 1.4 Synchronization & Conformance ⚪

*Keep repositories aligned with evolving standards through shared templates and configuration synchronization.*

**S-CORE**

- Automation applies and reconciles standards from central definitions.
- Adoption and drift are tracked to prioritize migration work.
- Cross-repository synchronization is a target capability and remains incomplete.
- **Biggest gap**: drift metrics/reporting and migration playbooks are not yet consistently operationalized.

### 1.4.1 Synchronization Mechanisms

*Applying shared standards into repositories through repeatable technical mechanisms.*

**S-CORE**

- Synchronization can be driven by central configuration, reusable templates, or generated repository settings rather than manual copying.
- The important infrastructure concern is not the exact mechanism, but that changes can be propagated predictably and reviewed.
- **Biggest gap**: the set of supported synchronization mechanisms is not yet documented as one coherent strategy.

### 1.4.2 Conformance Reporting

*Showing which repositories follow the shared baseline and where drift remains.*

**S-CORE**

- Conformance visibility is necessary if synchronization is meant to be measurable rather than aspirational.
- Cross-repository reporting should make deviations visible early enough to support planned migration rather than reactive cleanup.
- **Biggest gap**: no shared conformance dashboard or report currently shows adoption and drift across the repository landscape.

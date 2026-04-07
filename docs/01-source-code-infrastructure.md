# 1 Source Code Infrastructure 🟠

*Infrastructure for hosting and governing repositories consistently across the S-CORE project.*

## 1.1 Hosting & Organization ⚪

*Provide a stable, discoverable, and scalable hosting foundation for all S-CORE repositories.*

**S-CORE**

- GitHub is the canonical source-code hosting service for S-CORE repositories.
- Repositories are hosted in GitHub aligned with Eclipse governance on https://github.com/eclipse-score
- A common organization location makes repositories easier to discover, relate, and govern consistently.
- Shared hosting also enables organization-level settings, applications, and automation to be managed centrally.
- Discoverability depends not only on hosting location but also on repository naming, metadata, topics, and consistent descriptions.
- Good discovery infrastructure reduces onboarding friction and helps contributors navigate a growing repository landscape.
- **Biggest gap**: there is no shared discoverability standard for how S-CORE repositories should present themselves in GitHub.


## 1.2 Repository Provisioning & Lifecycle 🟡

*Infrastructure for creating, initializing, updating, and archiving repositories and executing lifecycle operations.*

**S-CORE**

- Lifecycle and policy management are intended to be centrally defined and automation-driven.
- Repository lifecycle infrastructure includes provisioning, archival, branch protection, required checks, and other durable settings that shape repository behavior.
- The point is to make repository state intentional and reviewable instead of a collection of manual one-off admin actions.
- Desired repository state is defined centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet)
- Lifecycle transitions are configuration changes instead of manual one-off actions.
- **Biggest gap**: approval of changes is rather random and undefined.

---

## 1.3 Repository Policy Management 🔴

*Infrastructure for managing and synchronizing repository policies such as branch protection, and application thereof at scale.*

**S-CORE**

- Policy intent (for example branch protection and required checks) is expressed centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet)
- Exceptions are explicit, reviewed, and documented.
- **Biggest gap**: there is no common policy definition or enforcement strategy, and the current state of policy across repositories is not well documented or visible.
---

## 1.4 Repository Standards 🟠

*Define, propagate, and measure standard repository elements to reduce unnecessary variation.*

**S-CORE**

- Standards should be versioned, measurable, and continuously synchronized across repositories.
- Standards are centrally defined and versioned.
- Repositories adopt standards directly or through synchronized templates, generated configuration, or managed settings.
- The standards story is only complete if adoption and drift can also be made visible across repositories.
- These standards make repositories easier to discover, review, and automate across the broader S-CORE landscape.
- **Biggest gap**: standards, synchronization, and conformance visibility are not yet operationalized as one coherent system.

### 1.4.1 Repository Metadata 🟡

*Define standard project metadata such as LICENSE, README, and governance files.*

**S-CORE**

- Metadata expectations exist, but rollout is not yet complete across repositories.
- Discoverability and governance depend on consistent metadata being present and kept current.
- **Biggest gap**: metadata standards exist only partially in enforceable, continuously synchronized form.

### 1.4.2 Tooling Configuration Standards 🟠

*Define shared configuration for linters and development tools.*

**S-CORE**

- Shared conventions are emerging, but not yet uniformly synchronized; [chapter 5](05-static-analysis-infrastructure.md) is the canonical home for code-analysis tooling and rule-baseline details.
- Baseline/override handling is not yet consistently defined across repository types.
- **Biggest gap**: no clearly enforced baseline/override model across repository classes.

### 1.4.3 Synchronization Mechanisms 🔴

*Applying shared standards into repositories through repeatable technical mechanisms.*

**S-CORE**

- Synchronization can be driven by central configuration, reusable templates, generated repository settings, or other automation rather than manual copying.
- The infrastructure concern is not a single mandated mechanism, but that changes can be propagated predictably, reviewed, and rolled out at scale.
- Migration support matters alongside synchronization, because existing repositories will not all converge at the same speed.
- **Biggest gap**: the supported synchronization and migration mechanisms are not yet documented as one coherent strategy.

### 1.4.4 Conformance Reporting 🔴

*Showing which repositories follow the shared baseline and where drift remains.*

**S-CORE**

- Conformance visibility is necessary if synchronization is meant to be measurable rather than aspirational.
- Adoption and drift should be tracked so migration work can be prioritized instead of discovered reactively.
- Cross-repository reporting should make deviations visible early enough to support planned migration rather than reactive cleanup.
- Cross-repository consistency of standards and related policy expectations is not yet reliably measured.
- **Biggest gap**: no shared conformance dashboard or report currently shows adoption and drift across the repository landscape.

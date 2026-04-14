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
- The organization start page, served through [eclipse-score/.github](https://github.com/eclipse-score/.github), is also part of that discoverability surface because it can link readers to shared repository inventories, standards, and other cross-project guidance.
- Good discovery infrastructure reduces onboarding friction and helps contributors navigate a growing repository landscape.
- **Biggest gap**: there is no shared discoverability standard for how S-CORE repositories should present themselves in GitHub.


## 1.2 Repository Provisioning & Lifecycle 🟡

*Infrastructure for creating, initializing, updating, and archiving repositories and executing lifecycle operations.*

**S-CORE**

Repository provisioning in S-CORE starts with creating the repository itself and attaching it to the shared organizational governance model. The infrastructure concern here is the durable repository state around creation, ownership, protection, archival, and other lifecycle transitions, not the detailed engineering baseline inside the repository.

Organization-level repository state is still managed centrally. Desired settings such as applications, branch protection, and required checks are defined through the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet), and lifecycle transitions are configuration changes instead of one-off admin actions.

**Biggest gap**: ownership and approval of repository lifecycle changes are still not clearly defined end to end.

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

Metadata expectations exist, but rollout is not yet complete across repositories. Discoverability and governance depend on consistent metadata being present and kept current.

For Bazel modules, [eclipse-score/module_template](https://github.com/eclipse-score/module_template) partially addresses this by giving new repositories a common starting set of metadata and governance files instead of requiring each maintainer to assemble them from scratch. That is useful as a bootstrap baseline, but it only covers repositories that fit the template and it does not by itself keep existing repositories aligned over time.

**Biggest gap**: metadata standards exist only partially in enforceable form, and the current bootstrap support is limited to Bazel-module-style repositories.

### 1.4.2 Tooling Configuration Standards 🟠

*Define shared configuration for linters and development tools.*

**S-CORE**

Shared conventions are starting to emerge, but not yet synchronized.

The same template also gives Bazel modules a partial starter baseline for repository-local tooling configuration, such as the initial Bazel wiring, editor settings, and starter workflow files. That helps new Bazel-based repositories begin from a more consistent shape, but it is still only a bootstrap aid for one repository class rather than a cross-project standardization mechanism.

Repository-local tooling configuration is only one part of the broader repository-standard surface. Cross-repository collection and publication of repository facts, adoption, and drift belong with [conformance reporting](#144-conformance-reporting), not as a tooling-only concern.

**Biggest gap**: no clearly enforced baseline/override model exists across repository classes, and the current template-based help is limited to Bazel modules.

### 1.4.3 Synchronization Mechanisms 🔴

*Applying shared standards into repositories through repeatable technical mechanisms.*

**S-CORE**

Synchronization can be driven by central configuration, reusable templates, generated repository settings, or other automation rather than manual copying. The infrastructure concern is not a single mandated mechanism, but that shared standards can be propagated predictably, reviewed, and rolled out at scale.

Migration support matters alongside synchronization, because existing repositories will not all converge at the same speed. New-repository templates can help with bootstrap, but they are not the same thing as synchronization once repositories already exist and start to drift.

**Biggest gap**: no alignment on a synchronization mechanism.

### 1.4.4 Conformance Reporting 🔴

*Showing which repositories follow the shared baseline and where drift remains.*

**S-CORE**

- Conformance visibility is necessary if synchronization is meant to be measurable rather than aspirational.
- Adoption and drift should be tracked so migration work can be prioritized instead of discovered reactively.
- Cross-repository reporting should make deviations visible early enough to support planned migration rather than reactive cleanup.
- Cross-repository consistency of standards and related policy expectations is not yet reliably measured.
- A practical reporting tool should be able to collect structured repository facts such as the Bazel version or module baseline in use, whether central reusable workflows such as `cicd-workflows/daily.yml` are consumed, whether `pre-commit` is configured, and where repositories intentionally diverge from the shared baseline.
- One suitable delivery model is generated Markdown stored in [eclipse-score/.github](https://github.com/eclipse-score/.github) and linked from the organization start page at [github.com/eclipse-score](https://github.com/eclipse-score/), so the conformance view becomes part of the normal project discovery surface rather than a hidden internal report.
- **Biggest gap**: no shared conformance dashboard or report currently shows adoption and drift across the repository landscape.

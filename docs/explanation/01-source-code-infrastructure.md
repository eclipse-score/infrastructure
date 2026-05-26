# 1 Source Code Infrastructure 🟠

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure for hosting and governing repositories consistently across the S-CORE project.*

```{mermaid}
graph TD
    eclipsefdn["`.eclipsefdn`\notterdog config"]
    otterdog["otterdog"]
    github_org["eclipse-score\nGitHub organization"]
    repos["Module repositories"]
    template["`eclipse-score/module_template`"]
    github_profile["`.github`\norg profile & conformance"]

    eclipsefdn -->|defines org policy| otterdog
    otterdog -->|applies: branch protection,\nrequired checks, Actions allowlist| github_org
    github_org -->|hosts| repos
    template -->|bootstraps new| repos
    github_profile -.->|discovery surface| github_org
```

## 1.1 Hosting & Organization ⚪

*Provide a stable, discoverable, and scalable hosting foundation for all S-CORE repositories.*

All S-CORE repositories are hosted on GitHub at [github.com/eclipse-score](https://github.com/eclipse-score), aligned with Eclipse Foundation governance. A shared organization enables organization-level settings, applications, and automation to be managed centrally. The organization profile page ([eclipse-score/.github](https://github.com/eclipse-score/.github)) serves as a discovery surface that links to shared repository inventories, standards, and cross-project guidance.

Discoverability depends not only on hosting location but on repository naming, metadata, topics, and consistent descriptions. Without a shared standard, repositories drift in how they present themselves, which increases onboarding friction as the repository landscape grows.

**Biggest gap**: there is no shared discoverability standard for how S-CORE repositories should present themselves in GitHub.


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

Repository policy covers the organization-level settings that govern how repositories behave: branch protection rules, required status checks, merge strategies, and which GitHub Actions are allowed to run. The infrastructure concern is not each individual rule but the system that makes policy intent explicit, reviewable, and enforceable at scale rather than hidden in per-repository admin pages.

In S-CORE, policy intent is expressed centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet). That makes policy changes reviewable as pull requests and exceptions explicit rather than silent. The same mechanism can restrict which GitHub Actions are allowed to run in the organization — an important supply-chain concern because third-party actions execute with the permissions of the workflow that calls them. An allowlist strategy classifies actions as approved, under review, or blocked, and the enforcement mechanism should prevent unapproved actions from running rather than merely warning about them.

**Biggest gap**: there is no common policy definition or enforcement strategy, and the current state of policy across repositories is not well documented or visible. GitHub Actions allowlisting is not yet implemented or documented as a security baseline.
---

## 1.4 Repository Standards 🟠

*Define, propagate, and measure standard repository elements to reduce unnecessary variation.*

Standards reduce unnecessary variation across the S-CORE repository landscape. To be effective, they need to be centrally defined, technically synchronized into repositories, and measurably adopted. These three concerns — definition, propagation, and conformance visibility — form a complete system only when they are all in place together.

S-CORE has the beginnings of central standards but has not yet closed the loop to synchronized enforcement and visible conformance. The [module_template](https://github.com/eclipse-score/module_template) provides a bootstrap baseline for new Bazel-module repositories, and shared tooling and policy modules define some common expectations. However, these elements do not yet add up to a coherent cross-repository standardization system with automated rollout and drift detection.

**Biggest gap**: standards, synchronization, and conformance visibility are not yet operationalized as one coherent system.

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

Repository-local tooling configuration is only one part of the broader repository-standard surface. Cross-repository collection and publication of repository facts, adoption, and drift belong with [conformance reporting](#conformance-reporting), not as a tooling-only concern.

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
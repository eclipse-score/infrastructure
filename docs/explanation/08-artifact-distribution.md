# 8 Release & Distribution ⚪

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure managing released deliverables, versioning, publication, and consumer access across S-CORE.*

:::{warning} Draft
This chapter has not been fully reviewed. Content may be incomplete or inaccurate.
:::

**S-CORE**

- GitHub Releases is the primary mechanism for publishing archive-style S-CORE deliverables, while Bazel modules are published through the shared registry at [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/).
- S-CORE delivery can include source releases, prebuilt artifacts, container images, and associated release metadata.
- The registry UI at [eclipse-score.github.io/bazel_registry_ui](https://eclipse-score.github.io/bazel_registry_ui/) is the intended discovery surface for published Bazel modules.
- Artifact versioning follows semantic versioning aligned with Git tagging.
- SBOM and provenance data should be generated during builds and accompany released deliverables.
- This chapter covers publishing that evidence with releases, while [chapter 6](06-compliance-infrastructure.md) is the canonical home for how SBOMs are scoped, interpreted, and monitored once they exist.

```{mermaid}
graph LR
    code["Module repository\n(source + tests)"]
    tag["Git tag\n(v1.2.3)"]
    release["GitHub Release\n(source archive + assets)"]
    registry["`eclipse-score/bazel_registry\n(registry entry)`"]
    ui["`Registry UI\nbazel_registry_ui`"]
    consumer["Consumer MODULE.bazel\nbazel_dep(name, version)"]

    code -->|"git tag + push"| tag
    tag -->|"GitHub Release workflow"| release
    release -->|"PR to add registry entry"| registry
    registry --> ui
    registry -->|"resolved via .bazelrc"| consumer
```

## 8.1 Deliverable Types ⚪

*Infrastructure defining which kinds of release deliverables S-CORE can publish and support.*

**S-CORE**

- S-CORE repositories may need to publish different deliverable types depending on consumer needs, including source archives, prebuilt packages, and container images.
- The infrastructure should support describing, versioning, and publishing these deliverables consistently across repositories.
- **Biggest gap**: no shared capability model defines which deliverable types exist in S-CORE, how they differ, or what infrastructure each type requires.

### 8.1.1 Source Deliverables

*Delivery of source-based release artifacts intended for downstream build or inspection.*

**S-CORE**

- Source delivery can include tagged source archives and related release metadata published from version control.
- GitHub Releases can act as a distribution point for source-based deliverables.
- **Biggest gap**: no shared definition exists for which source deliverables are expected, how complete they must be, or which metadata must always accompany them.

### 8.1.2 Prebuilt Deliverables

*Delivery of compiled or otherwise pre-generated artifacts for direct downstream consumption.*

**S-CORE**

- Prebuilt deliverables can include binaries, archives, packages, generated SDK assets, or other installable outputs attached to a release.
- GitHub Releases currently provides the most obvious publication mechanism for such assets.
- **Biggest gap**: no common publication pattern defines which prebuilt deliverables should be release-grade, how they are structured, or how consumers discover them.

### 8.1.3 Image Deliverables

*Delivery of container or VM-style images intended for execution or integration environments.*

**S-CORE**

- Some S-CORE use cases may require deliverables in image form, such as container images for tooling, CI, or runtime integration.
- Image-based delivery differs from archive-style release assets and usually requires registry-oriented publication and lifecycle handling.
- **Biggest gap**: no image delivery channel, registry strategy, or publication standard is currently defined for S-CORE.

## 8.2 Distribution Channels ⚪

*Infrastructure publishing release deliverables to downstream consumers through appropriate channels.*

**S-CORE**

- GitHub Releases is currently the primary public distribution channel for archive-style S-CORE deliverables.
- The shared Bazel registry is the public distribution channel for S-CORE Bazel modules.
- Different deliverable types may require different channels, such as release assets, registries, or mirrored repositories.
- **Biggest gap**: no shared distribution model maps deliverable types to supported publication channels and consumer access patterns.

### 8.2.1 Release Publishing

*Publishing release deliverables through release-oriented channels such as GitHub Releases.*

**S-CORE**

- Release pipelines can publish deliverables as GitHub Releases and attach binaries, source bundles, checksums, SBOMs, and related files.
- This channel is suitable for archive-style release deliverables and public release notes.
- **Biggest gap**: release publication is not yet standardized across repositories, and release composition is not consistently defined.

### 8.2.2 Registry-Based Distribution

*Publishing deliverables through registries such as package repositories or OCI registries.*

**S-CORE**

This subsection is the main description of how S-CORE publishes and consumes Bazel modules. Other chapters reference it from their own perspective, but the end-to-end registry flow belongs here.

For S-CORE Bazel modules, the custom registry is the release channel that matters. GitHub Releases are still useful for archives, binaries, checksums, and release notes, but Bazel itself consumes module metadata from the shared registry at [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/). In other words, if a module version should be usable as a dependency by another S-CORE repository, it needs to be present in the registry.

In S-CORE, the registry and GitHub Releases are deliberately coupled. The useful mental model is that the registry is Bazel's view of a released module version. A maintainer creates a GitHub release in the module repository, the registry imports that release as described in the [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md), and downstream repositories then resolve that version through Bazel. That coupling is why the split between "release" and "dependency resolution" can feel artificial: conceptually it is one publication pipeline, even though different infrastructure chapters look at it from different angles.

This also means module maintainers publish their modules by making a proper repository release and then adding the corresponding version to the registry, rather than inventing a repository-specific distribution pattern. The exact mechanics belong in the [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md), which should remain the maintained source of truth. This infrastructure guide explains the role of the registry and the end-to-end flow, but it deliberately avoids copying the details so that the workflow stays defined in one place.

For module users, the easiest entry point is the registry UI at [eclipse-score.github.io/bazel_registry_ui](https://eclipse-score.github.io/bazel_registry_ui/). It provides a browseable view of the modules and versions published in the registry and is backed by the data in [eclipse-score/bazel_registry_ui](https://github.com/eclipse-score/bazel_registry_ui). If there is ever any doubt, the registry repository itself remains authoritative because it is the actual input to Bazel.

The end-to-end flow is therefore simple. A module maintainer cuts a GitHub release in the module repository. The registry records that released version and the metadata Bazel needs to fetch it. Module users discover the version through the registry UI or the registry repository itself. Consumer repositories then resolve that version through `MODULE.bazel` and the registry configuration described in [chapter 3](03-build-infrastructure.md). Infrastructure maintainers, finally, operate the registry, its validation, and the UI as described in [chapter 10](10-infrastructure-operations.md).

This chapter is the best place to understand that overall publication flow. [Chapter 3](03-build-infrastructure.md) covers how consumers point Bazel at the registry, while [chapter 10](10-infrastructure-operations.md) covers how the registry and UI are run as shared services.

Helpful links:

- [S-CORE Bazel registry](https://github.com/eclipse-score/bazel_registry/)
- [Registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md)
- [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/)
- [Registry UI repository](https://github.com/eclipse-score/bazel_registry_ui)

---
### 8.2.3 Mirrors & Replication

*Replicating important deliverables into secondary channels for resilience, reach, or governance reasons.*


## 8.3 Release Metadata ⚪

*Infrastructure attaching the metadata required to identify, verify, and consume released deliverables.*

**S-CORE**

- Released deliverables should be accompanied by metadata such as version identifiers, checksums, SBOMs, provenance, and release notes.
- Metadata is part of the delivery capability because downstream consumers need it to verify, integrate, and audit releases.
- **Biggest gap**: no common release metadata baseline defines what every S-CORE release must publish.

### 8.3.1 Versioning & Tagging

*Identifying deliverables consistently across repositories and releases.*

**S-CORE**

- Semantic versioning aligned with Git tags is the expected standard across S-CORE repositories.
- Versioning and tagging identify release deliverables and connect them back to source history.
- **Biggest gap**: versioning conventions are not uniformly enforced or validated across repositories.

### 8.3.2 Compliance & Traceability Metadata

*Publishing supporting metadata needed for compliance, verification, and supply-chain traceability.*

**S-CORE**

SBOMs, provenance data, signatures, checksums, and release notes should accompany released deliverables where applicable. From the release perspective, the key question is simple: which evidence travels with the published artifact so downstream users can verify and understand it? The harder compliance questions, such as how a repository arrived at that SBOM, how license data was enriched, or whether a dependency belongs in development scope or product scope, belong in [chapter 6](06-compliance-infrastructure.md) and should not be duplicated here.

This metadata still matters here because publication is what makes the evidence durable and consumer-visible. A release artifact without its supporting evidence is harder to audit, trust, and respond to later when issues are disclosed. **Biggest gap**: no standardized process ensures that compliance and traceability metadata is generated and published with each release.

---

## 8.4 Consumer Access ⚪

*Infrastructure making released deliverables discoverable, retrievable, and usable by downstream consumers.*

**S-CORE**

- Consumers need a clear path to discover available deliverables, understand their intended use, and retrieve the correct format.
- For Bazel modules, consumer access is centered on the shared registry metadata and the registry UI.
- Consumer access includes naming, discoverability, documentation, and availability of public download or pull mechanisms.
- **Biggest gap**: no shared consumer-facing model explains where deliverables live, which consumers each format serves, or how access should work across S-CORE.

### 8.4.1 Discoverability

*Making available deliverables and their purpose visible to downstream users.*

**S-CORE**

GitHub Releases provide basic discoverability for release assets and release notes, but they are not the right starting point for Bazel modules. For modules, users should begin with the [registry UI](https://eclipse-score.github.io/bazel_registry_ui/), which presents the published contents of the shared registry in a way that is easier to browse than the raw repository. The underlying source of truth is still the registry data in [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/).

Good discoverability also requires light explanation. Users need to know that the registry answers the question "which module versions exist?" while the owning repository answers "how do I use this module once I depend on it?" Those two layers complement each other and should stay linked.

**Biggest gap**: no consistent discoverability pattern yet spans both GitHub release assets and registry-published modules in one coherent consumer story.

### 8.4.2 Retention, Availability & Rollback

*Keeping released deliverables accessible over time and enabling reliable rollback to previous baselines.*

**S-CORE**

Retention and rollback are two sides of the same coin. Retention asks which artifacts stay available and for how long; rollback asks how a consumer or the project itself reverts to a previously baselined release when a newer version turns out to be broken.

For S-CORE, the retention picture depends on the publication channel. GitHub Releases retain release assets indefinitely by default, which means source archives, binaries, and attached metadata remain accessible as long as the repository exists. The Bazel registry retains module entries permanently because they are committed files in a Git repository. GitHub Actions artifacts, by contrast, are ephemeral and disappear after a configurable retention window, which makes them unsuitable as the only home for anything that needs to survive beyond a single CI run.

Rollback requires more than artifact availability. A consumer who needs to revert to a previous module version can do so through the registry by pinning `bazel_dep` to the older version, which is straightforward as long as the older version is still present in the registry and the release assets it references are still available. For integrated baselines that span multiple modules, rollback means returning to a previous `known_good` manifest rather than individually downgrading components, because the combination of module versions matters as much as any single version. The `known_good` model described in [section 7.3.4](07-automation-integration.md#known-good-promotion) provides the identifier, but the ability to rebuild and redeploy from that identifier depends on all referenced artifacts, toolchain versions, and environment images still being retrievable.

A practical rollback strategy therefore needs three properties: durable artifact storage so that nothing disappears before it is no longer needed, manifest-level version identity so that "go back to the previous known-good" is an unambiguous operation, and a tested procedure so that rollback is a routine operation rather than an emergency improvisation.

**Biggest gap**: no explicit retention policy, rollback procedure, or availability guarantee is defined for S-CORE deliverables. The ability to roll back to a previous integrated baseline is assumed but not documented or tested.

### 8.4.3 Consumer Guidance

*Helping downstream users choose the right deliverable and understand how it should be consumed.*

**S-CORE**

For Bazel modules, the normal consumer workflow is straightforward. First, browse the [registry UI](https://eclipse-score.github.io/bazel_registry_ui/) to find the module and version you need. Next, configure your repository to use the S-CORE registry as described in [section 3.2.2](03-build-infrastructure.md#internal-module-dependencies). Finally, declare the dependency in `MODULE.bazel` and use the module according to the documentation in its owning repository.

Because registry entries are coupled to GitHub Releases, users can usually think of a registry version as the Bazel-consumable form of a repository release. The registry tells you which versions exist and how Bazel should fetch them. The owning repository tells you what the release contains and how to use the module once you depend on it.

To make this concrete, consumer repositories need the registry configuration in `.bazelrc`:

```text
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

With that in place, `MODULE.bazel` can declare dependencies with Bazel's normal module mechanism such as `bazel_dep(...)`. The S-CORE registry is then used for first-party modules, while the Bazel Central Registry remains available for public dependencies. The official [Bazel modules documentation](https://bazel.build/external/module) is the best reference for the `MODULE.bazel` syntax itself.

That split is important for keeping the documentation maintainable. This infrastructure guide explains where modules are published, how consumers discover them, and how Bazel is pointed at the registry. The mechanics for adding or updating module versions stay in the [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md), while module-specific API and usage details stay with the module's own source repository.

**Biggest gap**: there is no short, shared pattern for explaining how to consume registry-published S-CORE modules across repositories.

## 8.5 Post-Release Communication & Response ⚪

*Infrastructure for communicating and managing consumer-facing response once issues in distributed artifacts have been identified.*

**S-CORE**

- Dependency analysis, license interpretation, and continuous SBOM monitoring belong in [chapter 6](06-compliance-infrastructure.md).
- This chapter focuses on what happens on the consumer-facing release side once those issues are known.
- **Biggest gap**: no shared advisory and remediation communication model is defined for S-CORE deliverables.

### 8.5.1 Consumer Advisories

*Communicating post-release issues to downstream consumers in a clear and durable way.*

**S-CORE**

- Consumers need a clear advisory path once a relevant issue has been confirmed.
- **Biggest gap**: there is no shared advisory model for communicating issues affecting S-CORE releases.

### 8.5.2 Affected & Remediated Versions

*Explaining which released versions are affected and which versions contain remediation.*

**S-CORE**

- Consumer communication should eventually link affected versions, remediated versions, and the relevant release metadata.
- **Biggest gap**: version-level remediation guidance is not yet standardized across S-CORE releases.

### 8.5.3 Supporting Evidence

*Linking advisories back to the evidence that supports them.*

**S-CORE**

- Advisories are stronger when they can reference release notes, SBOMs, provenance, and other supporting material already produced elsewhere in the infrastructure flow, including the scoped compliance evidence described in [chapter 6](06-compliance-infrastructure.md).
- **Biggest gap**: there is no shared pattern for linking consumer advisories back to the supporting release evidence.
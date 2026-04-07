# 8 Release & Distribution ⚪

*Infrastructure managing released deliverables, versioning, publication, and consumer access across S-CORE.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- GitHub Releases is the primary mechanism for publishing S-CORE deliverables.
- S-CORE delivery can include source releases, prebuilt artifacts, container images, and associated release metadata.
- Artifact versioning follows semantic versioning aligned with Git tagging.
- SBOM and provenance data should be generated during builds and accompany released deliverables.
- Continuous security monitoring of distributed artifact SBOMs belongs in [chapter 6](06-compliance-infrastructure.md) once those artifacts exist.

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

- GitHub Releases is currently the primary public distribution channel for S-CORE deliverables.
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

- Registry-based distribution would be the natural channel for package-oriented or image-oriented deliverables.
- No shared package repository or OCI registry strategy is currently documented for S-CORE.
- **Biggest gap**: there is no common registry-backed distribution capability for deliverables that are not well served by GitHub Releases alone.

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

- SBOMs, provenance data, signatures, checksums, and release notes should accompany released deliverables where applicable.
- This metadata supports compliance, traceability, and trust in downstream usage.
- **Biggest gap**: no standardized process ensures that compliance and traceability metadata is generated and published with each release.

---

## 8.4 Consumer Access ⚪

*Infrastructure making released deliverables discoverable, retrievable, and usable by downstream consumers.*

**S-CORE**

- Consumers need a clear path to discover available deliverables, understand their intended use, and retrieve the correct format.
- Consumer access includes naming, discoverability, documentation, and availability of public download or pull mechanisms.
- **Biggest gap**: no shared consumer-facing model explains where deliverables live, which consumers each format serves, or how access should work across S-CORE.

### 8.4.1 Discoverability

*Making available deliverables and their purpose visible to downstream users.*

**S-CORE**

- GitHub Releases offers basic discoverability for release assets and notes.
- Deliverable discoverability should also include documentation that explains what is published and how it is meant to be consumed.
- **Biggest gap**: no consistent discoverability pattern helps consumers understand which release assets exist and which are relevant for their use case.

### 8.4.2 Retention & Availability

*Keeping released deliverables accessible over time according to a defined lifecycle.*

**S-CORE**

- GitHub retains release artifacts indefinitely, while GitHub Actions artifacts are ephemeral and CI-scoped only.
- Long-term consumer access depends on persistent publication channels rather than temporary pipeline storage.
- **Biggest gap**: no explicit retention, mirroring, or availability policy is defined for S-CORE deliverables.

### 8.4.3 Consumer Guidance

*Helping downstream users choose the right deliverable and understand how it should be consumed.*

**S-CORE**

- Good delivery infrastructure includes documentation that explains intended audiences, supported use, and expected integration paths for each deliverable.
- **Biggest gap**: there is no shared pattern for communicating deliverable purpose and consumption guidance to downstream users.

## 8.5 Post-Release Communication & Response ⚪

*Infrastructure for communicating and managing consumer-facing response once issues in distributed artifacts have been identified.*

**S-CORE**

- Dependency analysis and continuous SBOM monitoring belong in [chapter 6](06-compliance-infrastructure.md).
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

- Advisories are stronger when they can reference release notes, SBOMs, provenance, and other supporting material already produced elsewhere in the infrastructure flow.
- **Biggest gap**: there is no shared pattern for linking consumer advisories back to the supporting release evidence.

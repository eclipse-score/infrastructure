# 6 Artifact & Distribution Infrastructure ⚪

*Infrastructure managing build outputs, versioning, and distribution of S-CORE releases.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- GitHub Releases is the primary mechanism for publishing S-CORE artifacts.
- Artifact versioning follows semantic versioning aligned with git tagging.
- SBOM and provenance data should accompany released artifacts for compliance.
- **Biggest gap**: artifact distribution infrastructure is largely unstructured; no unified artifact storage, retention, or mirroring strategy exists across S-CORE.

## 6.1 Artifact Storage ⚪

*Infrastructure storing build artifacts produced by S-CORE repositories.*

**S-CORE**

- Build artifacts are stored as GitHub Actions artifacts during CI runs; long-term storage relies on GitHub Releases.
- **Biggest gap**: no shared artifact repository (e.g., OCI registry, package index) is operated for S-CORE.

### 6.1.1 Artifact Repositories

*Storage locations for generated build artifacts across S-CORE.*

**S-CORE**

- GitHub Releases hosts published artifacts; GitHub Actions artifact storage is ephemeral (CI-scope only).
- **Biggest gap**: no persistent, queryable artifact repository with metadata and dependency resolution exists.

### 6.1.2 Artifact Retention

*Policies controlling how long artifacts are stored.*

**S-CORE**

- GitHub retains release artifacts indefinitely; Actions artifacts expire after a configurable period.
- **Biggest gap**: no explicit retention policy or lifecycle management is defined for S-CORE artifacts.

---

## 6.2 Artifact Versioning ⚪

*Defining and enforcing consistent version numbering for S-CORE releases.*

**S-CORE**

- Semantic versioning aligned with git tags is the expected standard across S-CORE repositories.
- **Biggest gap**: versioning conventions are not uniformly enforced or validated across repositories.

### 6.2.1 Versioning Strategy

*Rules for artifact version numbering across S-CORE.*

**S-CORE**

- Semantic versioning (semver) is the expected convention; automation of version increments is not yet standardized.
- **Biggest gap**: no shared tooling or policy enforces consistent versioning across S-CORE repositories.

### 6.2.2 Release Tagging

*Tagging of releases in version control to mark published artifacts.*

**S-CORE**

- Git tags trigger release pipelines; tag naming conventions exist but are not centrally enforced.
- **Biggest gap**: no automated tag validation or cross-repository release coordination mechanism exists.

---

## 6.3 Artifact Distribution ⚪

*Infrastructure publishing S-CORE artifacts to downstream consumers.*

**S-CORE**

- Artifacts are primarily distributed via GitHub Releases as downloadable binaries and archives.
- **Biggest gap**: no mirroring, CDN distribution, or consumer-facing artifact registry is in place.

### 6.3.1 Release Publishing

*Publishing artifacts as GitHub Releases.*

**S-CORE**

- Release publishing pipelines create GitHub Releases and attach artifacts, SBOMs, and checksums.
- **Biggest gap**: release pipeline standardization across S-CORE repositories is incomplete.

### 6.3.2 Artifact Mirroring

*Replicating artifacts into downstream or partner environments.*

**S-CORE**

- No artifact mirroring infrastructure currently exists for S-CORE.
- **Biggest gap**: artifacts are only accessible via GitHub; no mirroring or secondary distribution channel is in place.

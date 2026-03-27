# 7 Compliance Infrastructure ⚪

*Infrastructure supporting legal and regulatory compliance for S-CORE software.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- SBOM generation, license compliance, and vulnerability tracking are core compliance requirements for S-CORE releases.
- License scanning and policy enforcement are partially operational; SBOM publication is a target capability.
- **Biggest gap**: compliance coverage is uneven across the dependency graph; automation from build through to published release artifacts is incomplete.

## 7.1 SBOM Infrastructure ⚪

*Infrastructure generating and managing software bill of materials for S-CORE repositories.*

**S-CORE**

- SBOMs document the full dependency graph of released S-CORE artifacts for supply chain transparency.
- **Biggest gap**: SBOM generation coverage across all repositories and publication alongside releases is incomplete.

### 7.1.1 SBOM Generation for Product 🟠

*Generating SBOMs during the build process for released product artifacts.*

**S-CORE**

- SBOM generation from Bazel build graphs is operational in some S-CORE repositories.
- **Biggest gap**: SBOM generation is not yet uniformly integrated into release pipelines across all repositories.

### 7.1.2 SBOM Generation for Development Environment

*Generating SBOMs for the build toolchain and development environment dependencies.*

**S-CORE**

- Development environment SBOMs (toolchain, devcontainer) are not yet generated.
- **Biggest gap**: toolchain and devcontainer dependency inventories are undocumented from a compliance perspective.

### 7.1.3 SBOM Publication

*Publishing SBOMs alongside released artifacts.*

**S-CORE**

- SBOM publication as a release artifact is a target capability.
- **Biggest gap**: no automated SBOM publication step is integrated into current S-CORE release pipelines.

---

## 7.2 License Compliance 🟠

*Infrastructure ensuring open source license obligations for S-CORE dependencies are fulfilled.*

**S-CORE**

- License scanning is in place in some S-CORE repositories and is integrated into CI pipelines.
- Known license-incompatible dependencies are blocked from merging via policy enforcement tooling.
- **Biggest gap**: license compliance coverage is not yet consistent across all S-CORE repositories and dependency types.

### 7.2.1 License Scanning 🟠

*Scanning dependencies to detect license information.*

**S-CORE**

- License scanners run as part of CI pipelines in active S-CORE repositories.
- **Biggest gap**: scan coverage across transitive dependencies and all repository types is not yet complete.

### 7.2.2 License Documentation

*Maintaining documentation of dependency licenses.*

**S-CORE**

- License information is captured as part of SBOM artifacts; no independently maintained license registry exists.
- **Biggest gap**: no centralized, continuously updated license registry spans all S-CORE dependencies.

### 7.2.3 License Policy Enforcement 🟠

*Enforcing project license policies for dependencies.*

**S-CORE**

- License policy checks block non-compliant dependencies in CI pipelines where configured.
- **Biggest gap**: policy enforcement is not yet consistently deployed across all S-CORE repositories.

---

## 7.3 Dependency Vulnerability Management ⚪

*Infrastructure tracking and mitigating security vulnerabilities in S-CORE dependencies.*

**S-CORE**

- Vulnerability monitoring for development dependencies relies on Dependabot and GitHub security advisories.
- **Biggest gap**: systematic vulnerability tracking and remediation across the full S-CORE dependency graph is not operationalized.

### 7.3.1 Development Vulnerability Monitoring

*Detecting vulnerabilities in dependencies during active development.*

**S-CORE**

- GitHub Dependabot provides automated vulnerability alerts for S-CORE repositories with supported dependency files.
- **Biggest gap**: Dependabot coverage is inconsistent; not all dependency types and lock files are supported.

### 7.3.2 Release Vulnerability Monitoring

*Tracking vulnerabilities that affect already published S-CORE artifacts.*

**S-CORE**

- Post-release vulnerability tracking against published SBOMs is a target capability.
- **Biggest gap**: no automated process monitors and alerts on vulnerabilities affecting released S-CORE artifacts.

### 7.3.3 Vulnerability Impact Analysis

*Determining which S-CORE artifacts or modules are affected by a vulnerability.*

**S-CORE**

- Impact analysis relies on manual investigation; no cross-repository automated impact triage exists.
- **Biggest gap**: no tooling supports automated vulnerability-to-artifact impact mapping across S-CORE.

### 7.3.4 Vulnerability Remediation

*Updating, replacing, or patching vulnerable dependencies.*

**S-CORE**

- Dependabot opens automated pull requests for version updates in configured repositories.
- **Biggest gap**: remediation coverage is limited to Dependabot-supported dependency types; coordinated cross-repository remediation is manual.

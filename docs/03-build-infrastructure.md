# 3 Build & Dependencies ⚪

*Deterministic, reproducible builds across S-CORE repositories using Bazel as the shared build system, including the dependency and evidence model around those builds.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Bazel is the standard build system direction for S-CORE middleware repositories.
- Shared build rules and toolchain definitions are intended to reduce per-repository configuration duplication.
- Remote caching is available to reduce repeated build work across CI pipelines.
- Dependency governance, SBOMs, and provenance belong here because they should be derived from normal builds rather than added only at release time.
- Continuous security monitoring of generated SBOMs belongs in [chapter 6](06-compliance-infrastructure.md), not in the build chapter itself.
- This scope includes not only middleware outputs, but also self-developed tooling and environment artifacts such as Python tooling packages and devcontainer images when they are built and published by S-CORE.
- **Biggest gap**: shared build rule libraries, toolchain baselines, dependency policy, and build evidence are not yet consistently available across all S-CORE repositories.

## 3.1 Build System ⚪

*Core build tooling and workspace conventions shared across S-CORE repositories.*

**S-CORE**

- Bazel workspaces are the standard unit of build organization across S-CORE middleware repositories.
- Shared Bazel rules are provided via the [eclipse-score/tooling](https://github.com/eclipse-score/tooling) repository.
- **Biggest gap**: workspace structure conventions and target naming standards are not formally defined or enforced cross-repository.

### 3.1.1 Project Structure

*Standard organization of Bazel workspaces across S-CORE repositories.*

**S-CORE**

- Repository layout conventions emerge from shared rule usage but are not yet formally standardized.
- **Biggest gap**: no centrally enforced or documented reference workspace structure exists.

### 3.1.2 Build Rule Libraries

*Reusable Bazel rules and macros shared across S-CORE repositories.*

**S-CORE**

- Shared Bazel macros and rules are provided via [eclipse-score/tooling](https://github.com/eclipse-score/tooling).
- **Biggest gap**: rule coverage is incomplete; not all repository types have suitable shared rules.

### 3.1.3 Build Conventions

*Shared target naming and repository layout conventions.*

**S-CORE**

- Naming and layout conventions are expected from shared rule usage but not yet formally documented.
- **Biggest gap**: no cross-repository convention enforcement mechanism exists.

## 3.2 Dependency Management ⚪

*Managing external and internal dependencies in a consistent, auditable way across S-CORE repositories.*

**S-CORE**

- External dependencies are declared per repository in Bazel workspace files; pinning strategies vary.
- Build-generated dependency inventories are needed to support licensing, SBOM generation, and later vulnerability analysis.
- The same dependency-governance expectations should apply to product code, self-developed tooling, and environment artifacts.
- **Biggest gap**: no unified dependency policy or cross-repository version alignment standard exists.

### 3.2.1 Third-Party Dependencies

*Integration and management of external libraries via Bazel.*

**S-CORE**

- External libraries are imported via Bazel's `http_archive` or Bzlmod; no shared registry or approved source list exists.
- **Biggest gap**: duplicate declarations and version drift across repositories are unmitigated.

### 3.2.2 Internal Module Dependencies

*Managing build-time dependencies between S-CORE repositories.*

**S-CORE**

- Cross-repository artifact consumption relies on pre-built releases or per-repository Bazel rules.
- **Biggest gap**: no consistent cross-repository dependency resolution model is defined.

### 3.2.3 Dependency Policies

*Rules governing allowed dependencies across S-CORE.*

**S-CORE**

- No formal cross-repository dependency policy currently exists.
- This should cover allowed sources, pinning expectations, version alignment, and license handling.
- **Biggest gap**: dependency choices are inconsistent and unaudited without policy guardrails.

### 3.2.4 Dependency Inventories

*Tracking the dependencies present in builds and why they are there.*

**S-CORE**

- Dependency inventories should be derived from the real build graph rather than maintained manually.

### 3.2.5 Tooling and Environment Dependencies

*Managing dependencies of self-developed tooling and environment artifacts with the same rigor as product builds.*

**S-CORE**

- S-CORE-developed tooling, especially Python-based tooling, is also part of the build and dependency landscape even when it is not product code.
- The same is true for build-relevant environment artifacts such as the devcontainer, because they package dependencies, licenses, and supply-chain choices into something contributors and CI consume directly.
- **Biggest gap**: tooling repositories and environment artifacts are not yet described as first-class citizens of the shared dependency-governance model.

## 3.3 Toolchain Management ⚪

*Compiler and runtime toolchain configuration for C++, Rust, and Python across S-CORE builds.*

**S-CORE**

- Toolchains are provisioned via the devcontainer for both local and CI builds.
- Shared toolchain baselines are the main link between [chapter 2](02-developer-environment.md) and automated build execution.
- **Biggest gap**: toolchain versions diverge across repositories without a shared baseline definition.

### 3.3.1 C++ Toolchains

*Compiler and build configuration for C++ components.*

**S-CORE**

- C++ toolchain configuration is provided through the devcontainer and per-repository Bazel setup.
- **Biggest gap**: no shared toolchain version target is enforced across S-CORE repositories.

### 3.3.2 Rust Toolchains

*Toolchain configuration for Rust components.*

**S-CORE**

- Rust toolchain rules exist in some repositories; no shared configuration is mandated.
- **Biggest gap**: no standard Rust toolchain version or `rules_rust` configuration is shared across S-CORE.

### 3.3.3 Python Toolchains

*Python runtime and tooling configuration for build and test.*

**S-CORE**

- Python toolchains vary per repository; no shared Python version baseline is defined.
- **Biggest gap**: no cross-repository Python toolchain standard is enforced.

### 3.3.4 Toolchain Governance

*Managing how shared toolchain baselines are selected and rolled out.*

**S-CORE**

- Shared toolchains need visible ownership and an upgrade cadence or repositories will drift again.
- **Biggest gap**: no cross-repository process clearly defines who owns toolchain baselines and how changes propagate.

## 3.4 Build Reproducibility & Evidence ⚪

*Ensuring builds are deterministic and produce trustworthy evidence from the same inputs.*

**S-CORE**

- Bazel's hermetic execution model is the foundation for reproducibility across S-CORE.
- SBOMs and provenance should be normal build outputs, while publication of that evidence belongs in [chapter 8](08-artifact-distribution.md).
- Continuous monitoring of distributed artifact SBOMs after they have been generated here belongs in [chapter 6](06-compliance-infrastructure.md).
- The same expectation should hold for self-developed tooling and dev environment artifacts where S-CORE builds and distributes them.
- **Biggest gap**: hermetic build compliance, reproducibility verification, and build-derived evidence are not yet generated or enforced uniformly across repositories.

### 3.4.1 Hermetic Builds

*Isolating builds from host environments to ensure reproducibility.*

**S-CORE**

- The devcontainer provides a stable, isolated build environment for CI and local builds.
- **Biggest gap**: full hermetic compliance (no host toolchain leakage) is not uniformly verified.

### 3.4.2 Deterministic Artifacts

*Ensuring builds produce identical artifacts from the same inputs.*

**S-CORE**

- Bazel's action graph model is designed for determinism; actual reproducibility is not validated at scale.
- **Biggest gap**: no cross-repository determinism validation pipeline exists.

### 3.4.3 Build Traceability

*Tracking build inputs, outputs, and provenance metadata.*

**S-CORE**

- Build provenance and SBOM generation are target capabilities and should become routine outputs of normal builds.
- **Biggest gap**: no build pipeline currently produces SBOMs and provenance consistently across repository types.

### 3.4.4 Tooling, Environment SBOMs & License Evidence

*Generating SBOMs and license/compliance evidence for S-CORE-developed tooling and environment artifacts.*

**S-CORE**

- Internally developed tools and dev environment artifacts also need SBOMs and license visibility, not only the main product build outputs.
- For contributors and CI, a devcontainer image is effectively a distributed engineering artifact and should therefore carry the same evidence expectations around dependencies and license compliance.
- **Biggest gap**: SBOM and license-compliance treatment for tooling artifacts and environment images is not yet described as part of the normal build-evidence flow.

### 3.4.5 Rebuild Verification

*Checking whether reproducibility claims hold over time and across execution contexts.*

**S-CORE**

- Rebuild verification would expose hidden toolchain changes, archive drift, and environmental assumptions.
- **Biggest gap**: reproducibility is desirable, but not yet verified through a shared repeatable process.

## 3.5 Build Execution Infrastructure ⚪

*Infrastructure for executing Bazel builds efficiently across local work and CI pipelines.*

**S-CORE**

- Builds run on GitHub Actions using GitHub-hosted and self-hosted runners.
- A shared Bazel remote cache reduces redundant compile work across pipeline runs.
- **Biggest gap**: remote build execution and shared performance visibility are not yet available project-wide.

### 3.5.1 Remote Cache

*Sharing Bazel build outputs between pipeline runs to reduce rebuild time.*

**S-CORE**

- A shared Bazel remote cache is available to S-CORE CI pipelines.
- **Biggest gap**: remote cache connectivity and configuration are not uniformly set up across all repositories.

### 3.5.2 Remote Build Execution

*Executing Bazel build actions on remote compute resources.*

**S-CORE**

- RBE infrastructure is not currently provisioned for S-CORE.
- **Biggest gap**: no RBE backend is available; builds are constrained to single-runner execution.

### 3.5.3 Build Resource Scheduling

*Scheduling and allocating compute resources for build workloads.*

**S-CORE**

- CI runner allocation is handled via GitHub-hosted and self-hosted runner scheduling.
- **Biggest gap**: no build-aware resource scheduling or prioritization mechanism is in place.

### 3.5.4 Build Performance Visibility

*Understanding where build time goes and where infrastructure work has the highest payoff.*

**S-CORE**

- Shared visibility should include queue times, cache effectiveness, and critical-path behavior.
- **Biggest gap**: build performance data is not yet aggregated into a shared view for project-wide prioritization.

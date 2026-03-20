# 2 Build Infrastructure (Bazel) ⚪

*Deterministic, reproducible builds across S-CORE repositories using Bazel as the shared build system.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Bazel is the standard build system for S-CORE middleware repositories.
- Shared build rules and toolchain definitions are intended to reduce per-repository configuration duplication.
- Remote caching is available to reduce repeated build work across CI pipelines.
- **Biggest gap**: shared build rule libraries, toolchain baselines, and remote execution are not yet consistently available across all S-CORE repositories.

## 2.1 Build System ⚪

*Core build tooling and workspace conventions shared across S-CORE repositories.*

**S-CORE**

- Bazel workspaces are the standard unit of build organization across S-CORE middleware repositories.
- Shared Bazel rules are provided via the [eclipse-score/tooling](https://github.com/eclipse-score/tooling) repository.
- **Biggest gap**: workspace structure conventions and target naming standards are not formally defined or enforced cross-repository.

### 2.1.1 Project Structure

*Standard organization of Bazel workspaces across S-CORE repositories.*

**S-CORE**

- Repository layout conventions emerge from shared rule usage but are not yet formally standardized.
- **Biggest gap**: no centrally enforced or documented reference workspace structure exists.

### 2.1.2 Build Rule Libraries

*Reusable Bazel rules and macros shared across S-CORE repositories.*

**S-CORE**

- Shared Bazel macros and rules are provided via [eclipse-score/tooling](https://github.com/eclipse-score/tooling).
- **Biggest gap**: rule coverage is incomplete; not all repository types have suitable shared rules.

### 2.1.3 Build Conventions

*Shared target naming and repository layout conventions.*

**S-CORE**

- Naming and layout conventions are expected from shared rule usage but not yet formally documented.
- **Biggest gap**: no cross-repository convention enforcement mechanism exists.

---

## 2.2 Dependency Management ⚪

*Managing external and internal dependencies in a consistent, auditable way across S-CORE repositories.*

**S-CORE**

- External dependencies are declared per repository in Bazel workspace files; pinning strategies vary.
- **Biggest gap**: no unified dependency policy or cross-repository version alignment standard exists.

### 2.2.1 Third-Party Dependencies

*Integration and management of external libraries via Bazel.*

**S-CORE**

- External libraries are imported via Bazel's `http_archive` or Bzlmod; no shared registry or approved source list exists.
- **Biggest gap**: duplicate declarations and version drift across repositories are unmitigated.

### 2.2.2 Internal Module Dependencies

*Managing build-time dependencies between S-CORE repositories.*

**S-CORE**

- Cross-repository artifact consumption relies on pre-built releases or per-repository Bazel rules.
- **Biggest gap**: no consistent cross-repository dependency resolution model is defined.

### 2.2.3 Dependency Policies

*Rules governing allowed dependencies across S-CORE.*

**S-CORE**

- No formal cross-repository dependency policy currently exists.
- **Biggest gap**: dependency choices are inconsistent and unaudited without policy guardrails.

---

## 2.3 Toolchain Management ⚪

*Compiler and runtime toolchain configuration for C++, Rust, and Python across S-CORE builds.*

**S-CORE**

- Toolchains are provisioned via the devcontainer for both local and CI builds.
- **Biggest gap**: toolchain versions diverge across repositories without a shared baseline definition.

### 2.3.1 C++ Toolchains

*Compiler and build configuration for C++ components.*

**S-CORE**

- C++ toolchain configuration is provided through the devcontainer and per-repository Bazel setup.
- **Biggest gap**: no shared toolchain version target is enforced across S-CORE repositories.

### 2.3.2 Rust Toolchains

*Toolchain configuration for Rust components.*

**S-CORE**

- Rust toolchain rules exist in some repositories; no shared configuration is mandated.
- **Biggest gap**: no standard Rust toolchain version or `rules_rust` configuration is shared across S-CORE.

### 2.3.3 Python Toolchains

*Python runtime and tooling configuration for build and test.*

**S-CORE**

- Python toolchains vary per repository; no shared Python version baseline is defined.
- **Biggest gap**: no cross-repository Python toolchain standard is enforced.

---

## 2.4 Build Reproducibility ⚪

*Ensuring builds are deterministic and produce identical outputs from the same inputs.*

**S-CORE**

- Bazel's hermetic execution model is the foundation for reproducibility across S-CORE.
- **Biggest gap**: hermetic build compliance is not measured or enforced uniformly across repositories.

### 2.4.1 Hermetic Builds

*Isolating builds from host environments to ensure reproducibility.*

**S-CORE**

- The devcontainer provides a stable, isolated build environment for CI and local builds.
- **Biggest gap**: full hermetic compliance (no host toolchain leakage) is not uniformly verified.

### 2.4.2 Deterministic Artifacts

*Ensuring builds produce identical artifacts from the same inputs.*

**S-CORE**

- Bazel's action graph model is designed for determinism; actual reproducibility is not validated at scale.
- **Biggest gap**: no cross-repository determinism validation pipeline exists.

### 2.4.3 Build Traceability

*Tracking build inputs, outputs, and provenance metadata.*

**S-CORE**

- Build provenance (SLSA) and input tracking are target capabilities.
- **Biggest gap**: no build provenance pipeline currently produces or publishes provenance metadata.

---

## 2.5 Build Execution Infrastructure ⚪

*Infrastructure for executing Bazel builds efficiently across CI pipelines.*

**S-CORE**

- Builds run on GitHub Actions using GitHub-hosted and self-hosted runners.
- A shared Bazel remote cache reduces redundant compile work across pipeline runs.
- **Biggest gap**: remote build execution (RBE) is not yet available for S-CORE CI pipelines.

### 2.5.1 Remote Cache

*Sharing Bazel build outputs between pipeline runs to reduce rebuild time.*

**S-CORE**

- A shared Bazel remote cache is available to S-CORE CI pipelines.
- **Biggest gap**: remote cache connectivity and configuration are not uniformly set up across all repositories.

### 2.5.2 Remote Build Execution

*Executing Bazel build actions on remote compute resources.*

**S-CORE**

- RBE infrastructure is not currently provisioned for S-CORE.
- **Biggest gap**: no RBE backend is available; builds are constrained to single-runner execution.

### 2.5.3 Build Resource Scheduling

*Scheduling and allocating compute resources for build workloads.*

**S-CORE**

- CI runner allocation is handled via GitHub-hosted and self-hosted runner scheduling.
- **Biggest gap**: no build-aware resource scheduling or prioritization mechanism is in place.

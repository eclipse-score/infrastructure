# 3 Build & Dependencies ⚪

*Deterministic, reproducible builds across S-CORE repositories using Bazel as the shared build system, including the dependency and evidence model around those builds.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Bazel is the standard build system direction for S-CORE middleware repositories.
- Shared build rules and toolchain definitions are intended to reduce per-repository configuration duplication.
- Internal Bazel modules are expected to be distributed through the shared S-CORE registry at [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/).
- Remote caching is available to reduce repeated build work across CI pipelines.
- Dependency governance, SBOMs, and provenance belong here because they should be derived from normal builds rather than added only at release time.
- The end-to-end compliance interpretation of those outputs, including license enrichment, development-versus-product SBOM scope, and later monitoring, belongs in [chapter 6](06-compliance-infrastructure.md), not in the build chapter itself.
- This scope includes not only middleware outputs, but also self-developed tooling and environment artifacts such as Python tooling packages and devcontainer images when they are built and published by S-CORE.
- Contributor onboarding, IDE support, and surrounding local tooling guidance for those environments belongs in [chapter 2](02-developer-environment.md); this chapter owns the build-time model behind them.
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
- Internal S-CORE Bazel modules should be consumed through the shared registry instead of ad hoc repository wiring.
- Build-generated dependency inventories are needed to support licensing, SBOM generation, and the later compliance flow described in [chapter 6](06-compliance-infrastructure.md).
- The same dependency-governance expectations should apply to product code, self-developed tooling, and environment artifacts.
- **Biggest gap**: no unified dependency policy or cross-repository version alignment standard exists.

### 3.2.1 Third-Party Dependencies

*Integration and management of external libraries via Bazel.*

**S-CORE**

- External libraries are imported via Bazel Central Registry; apart from the shared internal S-CORE registry for first-party modules, no shared third-party registry or approved source list exists.
- **Biggest gap**: duplicate declarations and version drift across repositories are unmitigated.

### 3.2.2 Internal Module Dependencies

*Managing build-time dependencies between S-CORE repositories.*

**S-CORE**

S-CORE repositories are expected to exchange Bazel modules through the shared registry at [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/). From the build perspective, this section is only about consumption: a repository should resolve first-party modules through the registry rather than through ad hoc repository overrides or manual source wiring. The full publication flow, including the coupling between registry entries and GitHub Releases, is described in [chapter 8](08-artifact-distribution.md#822-registry-based-distribution).

For consumers, the practical step is to tell Bazel where to look for modules. The same registry configuration described in [chapter 8](08-artifact-distribution.md#843-consumer-guidance) applies here:

```bazelrc
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

Once that is in place, dependencies are declared in `MODULE.bazel` with Bazel's normal module mechanism such as `bazel_dep(...)`. That is enough for the build side. Module discovery, release mechanics, and service ownership are intentionally documented in [chapter 8](08-artifact-distribution.md#822-registry-based-distribution) and [chapter 10](10-infrastructure-operations.md#1034-shared-registry-services) instead of being repeated here.


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

- Toolchain versions and build-time configuration are owned here, even when contributors access the surrounding local tooling through the shared environment described in [chapter 2](02-developer-environment.md).
- Shared toolchain baselines are the main link between the Bazel build model and automated build execution.

S-CORE is moving toward a deliberate split between language **toolchain modules** and language **policy modules**:

| | Toolchain modules | Policy modules |
|---|---|---|
| **Question** | How do we build this language in Bazel? | Which shared quality and safety rules should repositories follow? |
| **Scope** | Compiler integration, sysroots, templates, toolchain registration | Lint, warning, formatting, sanitizer, and safety-profile defaults |
| **Examples** | `bazel_cpp_toolchains`, `toolchains_rust` | `score_cpp_policies`, `score_rust_policies` |

The separation matters because toolchain upgrades and policy changes have different ownership and cadences. A repository should be able to adopt shared policies without being forced onto a particular compiler rollout.

- **Biggest gap**: the pattern now exists in the S-CORE repository landscape, but it is not yet documented and adopted consistently enough that consumers can rely on it as the default model.

### 3.3.1 C++ Toolchains

*Compiler and build configuration for C++ components.*

**S-CORE**

The C++ structure follows the toolchain/policy split described above:

- [eclipse-score/bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) — the **toolchain module**. Provides the Bazel C/C++ toolchain configuration layer, templates, package descriptors, and registration logic for Linux and QNX builds. Today this repository also contains sanitizer build-flag support and test examples (ASan, UBSan, LSan, TSan).

- [eclipse-score/score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) — the **policy module** (early stage). Intended to centralize reusable quality and safety policy defaults such as shared warning baselines, `cc_feature` flag selections, sanitizer configuration presets, constraint targets, and later ASIL-oriented safety profiles. Once populated, consumers would adopt these policies independently of which toolchain release they are on.

Sanitizer-related build features are currently defined in `bazel_cpp_toolchains`. As `score_cpp_policies` matures, reusable policy defaults are expected to migrate there, while the runtime execution and verification story for sanitizers remains in [chapter 4](04-testing-infrastructure.md#432-sanitizers-runtime-checks).

- **Biggest gap**: the repository split exists, but `score_cpp_policies` is not yet populated. Common adoption and governance of shared C++ toolchain and policy baselines are still incomplete across S-CORE.

### 3.3.2 Rust Toolchains

*Toolchain configuration for Rust components.*

**S-CORE**

Rust shows the same separation more explicitly:

- [eclipse-score/toolchains_rust](https://github.com/eclipse-score/toolchains_rust) — the **toolchain module**. Packages the actual Rust toolchains for Bazel, including prebuilt Ferrocene toolchains and the helper extension used to register them.

- [eclipse-score/score_rust_policies](https://github.com/eclipse-score/score_rust_policies) — the **policy module**. Packages the shared Clippy and rustfmt defaults that S-CORE projects are expected to consume.

Keeping those concerns decoupled allows toolchain upgrades and policy tightening to evolve independently instead of being forced into one release stream.

- **Biggest gap**: the split is visible in the repository landscape, but consistent rollout and governance of those shared Rust baselines are still not project-wide.

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
- Once generated, those SBOMs become inputs to the compliance flow in [chapter 6](06-compliance-infrastructure.md), which decides their scope, enriches them, and feeds later monitoring.
- The same expectation should hold for self-developed tooling and dev environment artifacts where S-CORE builds and distributes them.
- This evidence model belongs here because it is about built artifacts, not the contributor workflow described in [chapter 2](02-developer-environment.md).
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

- Build provenance and SBOM generation are target capabilities and should become routine outputs of normal builds so that later release and compliance steps consume real build evidence instead of reconstructed paperwork.
- **Biggest gap**: no build pipeline currently produces SBOMs and provenance consistently across repository types.

### 3.4.4 Tooling, Environment SBOMs & License Evidence

*Generating SBOMs and license/compliance evidence for S-CORE-developed tooling and environment artifacts.*

**S-CORE**

- Internally developed tools and dev environment artifacts also need SBOMs and license visibility, not only the main product build outputs.
- For contributors and CI, a devcontainer image is effectively a distributed engineering artifact and should therefore carry the same evidence expectations around dependencies and license compliance.
- Once those artifacts have been built, [chapter 6](06-compliance-infrastructure.md) should treat them the same way as other compliance inputs, including scope decisions and monitoring, rather than leaving them outside the shared flow.
- The fact that contributors enter that environment through the workflow described in [chapter 2](02-developer-environment.md) does not change that its evidence model belongs with the other build outputs here.
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

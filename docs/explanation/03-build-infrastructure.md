# 3 Build & Dependencies ⚪

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Deterministic, reproducible builds across S-CORE repositories using Bazel as the shared build system, including the dependency and evidence model around those builds.*

:::{warning} Draft
This chapter has not been fully reviewed. Content may be incomplete or inaccurate.
:::

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

```{mermaid}
graph LR
    module["MODULE.bazel\n(bazel_dep declarations)"]
    score_reg["`S-CORE registry\neclipse-score/bazel_registry`"]
    bcr["Bazel Central Registry\nbcr.bazel.build"]
    build["bazel build //..."]
    cache["Remote build cache"]
    toolchains["Toolchain modules\nbazel_cpp_toolchains\ntoolchains_rust"]
    policies["Policy modules\nscore_cpp_policies\nscore_rust_policies"]

    module -->|"1st: resolve S-CORE deps"| score_reg
    module -->|"2nd: fallback"| bcr
    score_reg --> build
    bcr --> build
    toolchains --> build
    policies --> build
    build <-->|"cache hits / writes"| cache
```

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

S-CORE repositories are expected to exchange Bazel modules through the shared registry at [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry/). From the build perspective, this section is only about consumption: a repository should resolve first-party modules through the registry rather than through ad hoc repository overrides or manual source wiring. The full publication flow, including the coupling between registry entries and GitHub Releases, is described in [chapter 8](08-artifact-distribution.md#registry-based-distribution).

For consumers, the practical step is to tell Bazel where to look for modules. The same registry configuration described in [chapter 8](08-artifact-distribution.md#consumer-guidance) applies here:

```text
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

Once that is in place, dependencies are declared in `MODULE.bazel` with Bazel's normal module mechanism such as `bazel_dep(...)`. That is enough for the build side. Module discovery, release mechanics, and service ownership are intentionally documented in [chapter 8](08-artifact-distribution.md#registry-based-distribution) and [chapter 10](10-infrastructure-operations.md#shared-registry-services) instead of being repeated here.


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

### 3.2.6 Lock Files

*Capturing the resolved dependency graph in version control for reproducible Bazel and `uv` inputs.*

**S-CORE**

Lock files such as `MODULE.bazel.lock` and `uv.lock` make the resolved dependency graph explicit instead of leaving each machine to rediscover it from the high-level declarations. From the build and dependency perspective, that matters because reproducibility depends not only on the declared inputs, but also on the exact resolved result that Bazel or `uv` will consume.

In the S-CORE repository landscape, this pattern already exists in practice, but not yet consistently across all repositories. Where lock files are used, the practical refresh step is typically handled locally through `pre-commit` and committed together with the dependency declaration change rather than being edited by hand. CI should then treat the committed lock state as authoritative for both Bazel and `uv` flows and fail when the declarations and the lock file no longer match. Current automated updates are also split by source: `renovate-bot` updates dependencies that come through the local S-CORE registry, while Dependabot updates dependencies that come from public registries.

### 3.2.7 Known-Good Integration Sets

*Capturing the explicit cross-repository integration manifest and metadata used to assemble one S-CORE stack.*

The `known_good` manifest identifies which component revisions belong together in one validated S-CORE stack. It sits one level above ordinary Bazel lock files: a lock file captures the resolved dependency graph inside a workspace, while `known_good` is the curated integration selection from which those inputs are generated.

The architectural context and decision background for this mechanism are documented separately: see [Infrastructure Design Decisions → `known_good` Architecture Note](decisions.md#known-good-architecture-note).

## 3.3 Toolchain Management ⚪

*Compiler and runtime toolchain configuration for C++, Rust, and Python across S-CORE builds.*

**S-CORE**

- Toolchain versions and build-time configuration are owned here, even when contributors access the surrounding local tooling through the shared environment described in [chapter 2](02-developer-environment.md).
- Shared toolchain baselines are the main link between the Bazel build model and automated build execution.

S-CORE is increasingly using a deliberate split between language toolchain modules and language policy modules. Toolchain repositories answer "how do we build this language in Bazel?" and therefore own compiler integration, sysroots, templates, registration, and other mechanics needed for reproducible builds. Separate policy repositories answer "which shared rules should repositories follow?" and package lint, warning, formatting, sanitizer, and safety-profile defaults that consumers can adopt without being forced onto a particular compiler rollout at the same time. That separation matters because toolchain upgrades and policy changes have different ownership and should be able to evolve on different cadences. **Biggest gap**: the pattern now exists in the S-CORE repository landscape, but it is not yet documented and adopted consistently enough that consumers can rely on it as the default model.

### 3.3.1 C++ Toolchains

*Compiler and build configuration for C++ components.*

**S-CORE**

The emerging C++ structure follows that split directly. [eclipse-score/bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains) is the build-facing module: it provides the Bazel C/C++ toolchain configuration layer, templates, package descriptors, and registration logic for Linux and QNX builds. [eclipse-score/score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) is the policy-facing companion: it centralizes reusable `cc_feature` and flag selections such as ASan, UBSan, LSan, and TSan support, `debug_symbols`, runtime environment templates, constraint targets such as `no_tsan` and `any_sanitizer`, and the flag infrastructure that repositories can use in `select()` expressions. That same policy layer is also the natural home for shared warning baselines and later ASIL-oriented safety configurations. The point of the split is that a module should be able to adopt shared C++ policies without being forced onto one specific toolchain release. The runtime purpose and rollout of sanitizers themselves belong in [chapter 4](04-testing-infrastructure.md#sanitizers-runtime-checks); this subsection only owns the reusable build-side mechanism that makes those checks selectable. **Biggest gap**: the repository split now exists, but common adoption and governance of shared C++ toolchain and policy baselines are still incomplete across S-CORE.

### 3.3.2 Rust Toolchains

*Toolchain configuration for Rust components.*

**S-CORE**

Rust already shows the same separation more explicitly. [eclipse-score/toolchains_rust](https://github.com/eclipse-score/toolchains_rust) packages the actual Rust toolchains for Bazel, including prebuilt Ferrocene toolchains and the helper extension used to register them. [eclipse-score/score_rust_policies](https://github.com/eclipse-score/score_rust_policies) separately packages the shared Clippy and rustfmt defaults that S-CORE projects are expected to consume. In other words, one repository answers how Bazel gets a Rust compiler, while the other answers which Rust lint and formatting rules S-CORE wants to enforce. Keeping those concerns decoupled allows toolchain upgrades and policy tightening to evolve independently instead of being forced into one release stream. **Biggest gap**: the split is already visible in the repository landscape, but consistent rollout and governance of those shared Rust baselines are still not project-wide.

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

### 3.3.5 QNX SDP Provisioning

*How the QNX Software Development Platform is obtained and made available to Bazel C++ builds.*

The QNX SDP — the compiler, headers, and libraries required for QNX cross-compilation — is a commercial artifact distributed separately from the toolchain configuration. Its provisioning path is distinct from the Bazel toolchain registration in `bazel_cpp_toolchains` and determines how reliably builds can acquire the SDP in CI and in local developer environments.

License on CI:  A separate [`setup-qnx-sdp`](https://github.com/eclipse-score/cicd-actions) composite action handles license activation only; it does not fetch or unpack the SDP

License locally: License credentials are injected through environment variables.

#### Today

The SDP is downloaded as a tar archive from QNX.com via a hardcoded dependency URL in Bazel. Forks may overwrite this dependency.

```{mermaid}
flowchart LR
    qnxcom(["QNX.com"])
    sdp_tar["`QNX SDP
〈artefact: tar〉`"]
    env_cfg(["Local Environment variables"])
    license(["License"])
    action_setup["`setup-qnx-sdp
(license only)`"]
    bazel["Bazel build C++"]

    qnxcom --> sdp_tar
    sdp_tar -->|"hardcoded dependency URL"| bazel
    action_setup --> license
    env_cfg --> license
    
    license -->|"activates license only"| bazel
```

The license and the SDP fetch are deliberately separate.

#### Soon (planned)

The target model does not rely on QMX.com, but rather uses the QNX CLI distributed with QNX Software Center to produce a local SDP. That SDP is then stored in bazel cache, on your local computer, in ci cache, on protected eclipse artefact storage, or on company-internal artefact storage — and Bazel receives a user-defined flag that tells it where to find the SDP. For local developer environments the intended invocation is:

```text
bazel run //:local_qnx_sdp -- --path=/opt/qnx_sdp
# or
local_qnx_sdp.sh --path=/opt/qnx_sdp
```

```{mermaid}
flowchart TD
    qnx_sc(["QNX Software Center"])
    qnx_cli["`QNX CLI
〈tool〉`"]
    sdp_dir["`QNX SDP
〈artefact: directory tree〉`"]
    art_store[("Artefact storage
eclipse · company-internal · local")]
    bazel["Bazel build C++"]

    qnx_sc -.-> qnx_cli
    qnx_cli -.-> sdp_dir
    sdp_dir -.-> art_store
    art_store -.->|"user-defined flag"| bazel
```

The central unsolved problem in this model is how we can provide this SDP as a true bazel dependency to qnx-related builds, as it has a **non-deterministic SDP output**. So building the SDP on the fly produces a different archive hash on every invocation. Bazel treats a changed hash as a changed dependency, which invalidates the **entire** C++ build cache and forces a full recompilation of all downstream targets on every run. Until the SDP can be built deterministically using it as a bazel dependency is not practical.


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
- In cross-repository integration flows, that provenance should identify not only the local repository revision but also the `known_good` set or equivalent manifest that defined the integrated stack.
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

Remote Build Execution (RBE) offloads Bazel's action graph to a cluster of workers so that parallelism is no longer bound by the CPU and memory of a single runner. For S-CORE, the practical value is twofold: CI builds that currently serialize on a single GitHub Actions runner could fan out across remote workers, and developers running Bazel locally could optionally delegate heavy compilations to remote infrastructure while keeping the edit-build-test cycle on their own machine.

The infrastructure involves three layers. First, a backend service that implements the Bazel Remote Execution API — candidates range from open-source solutions such as Buildbarn and BuildBuddy Community to managed commercial services. Second, the CI and local `.bazelrc` configuration that enables remote execution for the right subset of actions without breaking platform-specific builds. Third, authentication and access control so that the backend serves authorized S-CORE builds without exposing the cluster to uncontrolled workloads.

A related Bazel mechanism is dynamic execution, which lets Bazel race a local and a remote execution of the same action and take whichever finishes first. This can smooth the transition period where some actions run faster locally and others benefit from remote workers, but it adds complexity to the configuration and requires the backend to tolerate speculative cancellations.

For hardware-oriented testing, RBE intersects with the hardware runner story in [section 7.1.2](07-automation-integration.md#hardware-test-runners). If lab-attached devices such as Raspberry Pi boards are registered as RBE workers, Bazel could schedule test execution on real hardware as part of a normal `bazel test` invocation, avoiding a separate deployment step. This is an advanced pattern that depends on both the RBE backend and the hardware provisioning model being in place.

**Biggest gap**: no RBE backend is available; builds are constrained to single-runner execution. Provider evaluation criteria, architecture decisions, and authentication model are not yet documented.

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
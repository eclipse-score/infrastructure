# 11 Reference Integration 🟠

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Cross-repository integration workspace for validating S-CORE modules as one coherent stack.*

`reference_integration` is the place where S-CORE turns multiple module repositories into one validated integration context. It is not a replacement for module-local CI. Instead, it provides the shared workspace, candidate-stack promotion model, and consolidated evidence boundary that module repositories cannot define on their own. The selected operating model is DR-008 Option 4 — stable `known_good` with module-scoped validation — which uses a two-stage pipeline: integration-scoped checks run inside the repository, and module-scoped unit tests run in each module against the dependency versions resolved by the integrated stack.

That distinction matters because the repository sits at the seam between independent module ownership and project-level release confidence. Modules still own their unit tests, static analysis, and repository-local quality gates. `reference_integration` owns the cross-repository view: it assembles a concrete candidate stack, validates that stack against a shared dependency set, and records the outcome as a durable integration snapshot.

**Biggest gap**: the two-stage pipeline is architecturally defined but not yet implemented. Evidence consolidation, module-scoped validation plumbing, and coverage reporting are all in active development for v0.8.

## 11.1 Integration Workspace 🟡

*A shared Bazel workspace for exercising multiple S-CORE modules together.*

The repository's first job is to make a multi-module checkout usable as one build and test environment. That workspace model is what exposes cross-repository dependency problems, label mismatches, unsupported toolchain combinations, and integration regressions that would stay hidden if every module only validated itself in isolation.

The workspace currently supports Linux x86_64 and EBcLfSA targets. The module set is controlled by `known_good.json`, which pins the exact repository revision for each participating module. Showcases — runnable examples that exercise the integrated stack end to end — exist for some modules but are not yet consistent across all modules in `known_good.json`. A QNX8 aarch64 build configuration is planned but not yet added.

**Biggest gap**: QNX8 aarch64 build support is missing. Showcase coverage is incomplete for recently integrated modules. The README no longer reflects the current workspace structure and contributes to onboarding friction.

## 11.2 Known-Good Promotion 🟠

*A concrete snapshot model for deciding which component revisions belong together.*

The integration unit is `known_good`, not an arbitrary combination of current branches. That makes the stack reproducible and reviewable: a promotion either selects one explicit set of module revisions or it does not. The same identifier then drives CI, documentation, traceability views, and artifact retention without mixing unrelated repository heads.

This snapshot model is the architectural bridge between module-level release flow and project-level integration flow. Module repositories can keep moving independently, but `reference_integration` defines which exact revisions are accepted as one coherent stack for a given point in time. When the snapshot changes, the integrated evidence changes with it.

The promotion model has a significant open boundary: DR-008 does not yet define what constitutes a release, which evidence is required before promoting a candidate, or how a tagged release differs from a passing integration snapshot. Until the release definition is settled, the `known_good` mechanism is present but incomplete — it can pin revisions, but the process for deciding when and why a snapshot becomes a release is undefined.

Managing dependency versions across modules is a recurring operational challenge. Modules must align on compatible versions of shared dependencies, and a version bump in one module can trigger coordination across the entire dependency graph. There is currently no automated mechanism to propagate `known_good`-aligned dependency versions back to individual modules.

**Biggest gap**: the release process is not yet defined in DR-008. Without a clear promotion gate — what evidence is required, what tagging model applies, what the difference is between an integration snapshot and a release — the `known_good` mechanism cannot fully serve its intended purpose.

## 11.3 Validation Pipeline 🔴

*A two-stage pipeline that separates integration-scoped and module-scoped checks.*

DR-008 Option 4 defines the validation model explicitly. The first stage runs inside `reference_integration`: Bazel resolves the full transitive dependency set, the integrated platform is built for all supported targets, and Platform Integration Tests (PITs) and Feature Integration Tests (FITs) are executed against the assembled stack. The second stage runs inside each module repository, but against the exact dependency versions resolved in stage one — temporary overrides inject the resolved set without modifying the module's released sources, then minimal unit and component tests execute.

That two-stage split means the integration repository owns cross-repository concerns — multi-platform builds, platform integration, feature-level scenarios — while module-level unit tests stay close to the owning teams for fast diagnosis. Tests that connect to running images use the Integration Test Framework (ITF); the EBcLfSA integration scenario is a target for ITF-based execution alongside the existing build-and-image workflow.

The `test_and_docs` workflow has not yet been updated to implement this pipeline. The dependency-injection step for module-scoped validation — resolving the transitive dependency set and feeding it back to each module — does not exist. Neither the orchestration harness nor the module handoff protocol is in place. The two-stage model is architectural intent, not implemented infrastructure.

**Biggest gap**: the validation pipeline defined by DR-008 Option 4 is not built. The current workflow does not resolve and propagate the dependency set, does not trigger module-scoped validation, and does not collect the resulting evidence. This is the most critical unimplemented piece of the chapter.

## 11.4 Integrated Evidence 🔴

*Collecting verification, documentation, and release evidence from the same validated stack.*

The value of the integration repository is not just that it can build a combined workspace. It also becomes the place where higher-level evidence is attached to one concrete stack identity. That includes cross-repository test results, documentation builds for release scenarios, dependency-resolution outputs, and the metadata that makes those results auditable later.

The Module Integration Dashboard provides a consolidated status view across modules, showing build results, test outcomes, and coverage summary for the current `known_good` stack. The dashboard currently only works on the `main` branch; support for PR and release branches is an open improvement. Detailed coverage reports are not yet embedded in the published documentation pages — only a summary table is shown; the infrastructure to include artifact-generated pages in the site does not exist yet.

Coverage calculation has known problems for both C++ and Rust. For C++, `bazel coverage` reliability and statement counting vary across test frameworks. For Rust, only line coverage is currently calculated and QNX coverage does not work. A unified cross-language coverage report is not implemented. Rust test reports do not carry the traceability properties required for requirements cross-referencing.

There is no uniform schema for what integrated evidence is, what it must contain, and how it is retained and traced to a specific `known_good` snapshot. Because the release process is not defined (see 11.2), there is also no defined boundary between evidence collected during integration and evidence required for a release. Without that boundary, it is not possible to say whether any given CI run produces release-grade evidence or not.

**Biggest gap**: there is no evidence schema and no defined release gate. Coverage is unreliable across languages and platforms, traceability properties are missing from Rust reports, and the infrastructure for attaching artifact-generated content to the published documentation does not exist.

## 11.5 Operating Model 🟡

*CI workflow architecture, caching, and cross-repository automation.*

The selected model keeps `reference_integration` focused on the integrated stack while leaving module-owned quality checks in the module repositories. The `test_and_docs` workflow is the current orchestration entry point, but it is structured as a single large job that mixes concerns and makes failure diagnosis harder. The planned redesign splits it into smaller composable workflows, parallelizes component test execution where possible, and gates documentation builds on full coverage completion.

Build workflows across S-CORE repositories are being centralized in `cicd-workflows` to eliminate duplicated job definitions. The multi-platform build matrix — Linux, QNX, EBcLfSA — is being restructured for parallel execution. Bazel remote caching is write-restricted to `main` to prevent cache pollution from PR branches, but the current implementation has room for optimization. Bazel profiling of the integrated build has been proposed to identify the highest-impact areas for build time reduction.

Tooling updates are managed through Renovate, which is being switched from opt-in to opt-out to simplify onboarding of new repositories. The `.bazelversion` synchronization across the dependency graph is being formalized to prevent silent toolchain drift. Code review checking (`cr_checker`) is currently disabled in the `reference_integration` CI due to an unresolved documentation build conflict.

**Biggest gap**: most workflow and automation improvements are in-progress for v0.8. The `test_and_docs` workflow mixes concerns in a single large job, which makes it hard to reason about failures and limits parallelism.

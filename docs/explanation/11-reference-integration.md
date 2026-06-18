# 11 Reference Integration 🟡

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

## 11.2 Known-Good Promotion 🟡

*A concrete snapshot model for deciding which component revisions belong together.*

The integration unit is `known_good`, not an arbitrary combination of current branches. That makes the stack reproducible and reviewable: a promotion either selects one explicit set of module revisions or it does not. The same identifier then drives CI, documentation, traceability views, and artifact retention without mixing unrelated repository heads.

This snapshot model is the architectural bridge between module-level release flow and project-level integration flow. Module repositories can keep moving independently, but `reference_integration` defines which exact revisions are accepted as one coherent stack for a given point in time. When the snapshot changes, the integrated evidence changes with it.

Managing dependency versions across modules is a recurring operational challenge. Modules must align on compatible versions of shared dependencies, and a version bump in one module can trigger coordination across the entire dependency graph. There is currently no automated mechanism to propagate `known_good`-aligned dependency versions back to individual modules. This makes adoption of new S-CORE releases harder for downstream users who encounter constant version churn.

**Biggest gap**: S-CORE lacks a shared rule set for how candidate stacks are assembled, promoted, and tagged across repositories. Dependency version management across modules is manual and creates adoption friction.

## 11.3 Validation Pipeline 🟠

*A two-stage pipeline that separates integration-scoped and module-scoped checks.*

DR-008 Option 4 defines the validation model explicitly. The first stage runs inside `reference_integration`: Bazel resolves the full transitive dependency set, the integrated platform is built for all supported targets, and Platform Integration Tests (PITs) and Feature Integration Tests (FITs) are executed against the assembled stack. The second stage runs inside each module repository, but against the exact dependency versions resolved in stage one — temporary overrides inject the resolved set without modifying the module's released sources, then minimal unit and component tests execute.

That two-stage split means the integration repository owns cross-repository concerns — multi-platform builds, platform integration, feature-level scenarios — while module-level unit tests stay close to the owning teams for fast diagnosis. FITs are the concrete mechanism for cross-module scenarios: each module contributes FIT targets that exercise its features in the context of the full stack. Tests that connect to running images use the Integration Test Framework (ITF); the EBcLfSA integration scenario is a target for ITF-based execution alongside the existing build-and-image workflow.

FITs currently exist for only a subset of modules. Feature integration tests for `baselibs`, `baselibs_rust`, `communication`, and `lifecycle` are open work items for v0.8. The `test_and_docs` workflow has not yet been updated to implement the two-stage pipeline; the dependency-injection step for module-scoped validation does not exist yet.

**Biggest gap**: the `test_and_docs` workflow does not implement DR-008 Option 4. FIT coverage is incomplete across modules. ITF integration for FITs and ITF execution inside the EBcLfSA scenario are both pending.

## 11.4 Integrated Evidence 🟠

*Collecting verification, documentation, and release evidence from the same validated stack.*

The value of the integration repository is not just that it can build a combined workspace. It also becomes the place where higher-level evidence is attached to one concrete stack identity. That includes cross-repository test results, documentation builds for release scenarios, dependency-resolution outputs, and the metadata that makes those results auditable later.

The Module Integration Dashboard provides a consolidated status view across modules, showing build results, test outcomes, and coverage summary for the current `known_good` stack. The dashboard currently only works on the `main` branch; support for PR and release branches is an open improvement. Detailed coverage reports are not yet embedded in the published documentation pages — only a summary table is shown.

Coverage calculation has known issues for both C++ and Rust. For C++, `bazel coverage` reliability and statement counting vary across test frameworks, and framework alignment is ongoing. For Rust, only line coverage is currently calculated and QNX coverage does not yet work. A unified coverage report combining both languages is a goal but not yet implemented. Rust test reports do not yet carry the traceability properties needed for requirements cross-referencing.

Documentation builds from module sources are not yet comprehensive: the `docs_combo` target should include every module listed in `known_good.json`, but several modules are not yet enabled. Extra documentation pages generated from CI artifacts — coverage reports, test summaries — cannot currently be included in the published site in a structured way.

**Biggest gap**: there is no uniform evidence schema. Coverage is incomplete and unreliable across languages and platforms. Rust test report traceability is missing. Documentation, test results, and coverage artifacts remain spread across CI outputs rather than collected under one integration snapshot.

## 11.5 Operating Model 🟡

*CI workflow architecture, caching, and cross-repository automation.*

The selected model keeps `reference_integration` focused on the integrated stack while leaving module-owned quality checks in the module repositories. The `test_and_docs` workflow is the current orchestration entry point, but it is structured as a single large job that mixes concerns and makes failure diagnosis harder. The planned redesign splits it into smaller composable workflows, parallelizes component test execution where possible, and gates documentation builds on full coverage completion.

Build workflows across S-CORE repositories are being centralized in `cicd-workflows` to eliminate duplicated job definitions. The multi-platform build matrix — Linux, QNX, EBcLfSA — is being restructured for parallel execution. Bazel remote caching is write-restricted to `main` to prevent cache pollution from PR branches, but the current implementation has room for optimization. Bazel profiling of the integrated build has been proposed to identify the highest-impact areas for build time reduction.

Tooling updates are managed through Renovate, which is being switched from opt-in to opt-out to simplify onboarding of new repositories. The `.bazelversion` synchronization across the dependency graph is being formalized to prevent silent toolchain drift. Code review checking (`cr_checker`) is currently disabled in the `reference_integration` CI due to an unresolved documentation build conflict.

**Biggest gap**: most workflow and automation improvements are in-progress for v0.8. The `test_and_docs` workflow mixes concerns in a single large job, which makes it hard to reason about failures and limits parallelism.

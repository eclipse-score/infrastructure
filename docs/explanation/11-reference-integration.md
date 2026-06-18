# 11 Reference Integration 🟡

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Cross-repository integration workspace for validating S-CORE modules as one coherent stack.*

`reference_integration` is the place where S-CORE turns multiple module repositories into one validated integration context. It is not a replacement for module-local CI. Instead, it provides the shared workspace, candidate-stack promotion model, and consolidated evidence boundary that module repositories cannot define on their own. The current DR-008 operating model is stable `known_good` with module-scoped validation.

That distinction matters because the repository sits at the seam between independent module ownership and project-level release confidence. Modules still own their unit tests, static analysis, and repository-local quality gates. `reference_integration` owns the cross-repository view: it assembles a concrete candidate stack, validates that stack against a shared dependency set, and records the outcome as a durable integration snapshot.

**Biggest gap**: the integration role is now defined, but the orchestration, evidence consolidation, and module-scoped validation plumbing still need to be implemented consistently across repositories.

## 11.1 Integration Workspace 🟡

*A shared Bazel workspace for exercising multiple S-CORE modules together.*

The repository's first job is to make a multi-module checkout usable as one build and test environment. That workspace model is what exposes cross-repository dependency problems, label mismatches, unsupported toolchain combinations, and integration regressions that would stay hidden if every module only validated itself in isolation.

The workspace is intentionally broader than a simple aggregation of repository checkouts. It includes the glue needed to make the integrated stack buildable and debuggable: repository overrides, shared Bazel configuration, runnable examples, and structured entry points for the supported integration scenarios. The result is a controlled integration baseline rather than a vague collection of latest heads.

**Biggest gap**: workspace assembly and update mechanics are still more operationally complex than they should be for contributors who only want to validate a candidate stack.

## 11.2 Known-Good Promotion 🟡

*A concrete snapshot model for deciding which component revisions belong together.*

The integration unit is `known_good`, not an arbitrary combination of current branches. That makes the stack reproducible and reviewable: a promotion either selects one explicit set of module revisions or it does not. The same identifier can then drive CI, documentation, traceability views, and artifact retention without mixing unrelated repository heads.

This snapshot model is the architectural bridge between module-level release flow and project-level integration flow. Module repositories can keep moving independently, but `reference_integration` defines which exact revisions are accepted as one coherent stack for a given point in time. When the snapshot changes, the integrated evidence changes with it.

**Biggest gap**: S-CORE still lacks one shared rule set for how candidate stacks are assembled, promoted, and tagged across all participating repositories.

## 11.3 Integrated Evidence 🟠

*Collecting verification, documentation, and release evidence from the same validated stack.*

The value of the integration repository is not just that it can build a combined workspace. It also becomes the place where higher-level evidence is attached to one concrete stack identity. That includes cross-repository test results, documentation builds for release scenarios, dependency-resolution outputs, and the metadata that makes those results auditable later.

The important constraint is consistency. Evidence that is produced for one `known_good` snapshot should remain traceable to that snapshot, not to the moving target of "whatever was on main when the job ran". That is what makes the repository useful for release confidence, not just for ad hoc debugging.

For documentation in particular, the repository gives S-CORE a place to describe integrated views as integrated views. The explanation chapters in this site treat `reference_integration` as the canonical place for that cross-repository snapshot discussion, while the documentation chapter keeps the consumer-facing implications of the same model.

**Biggest gap**: S-CORE does not yet have one uniform schema for integrated evidence, so results remain spread across CI artifacts, repository docs, and release outputs.

## 11.4 Operating Model 🟡

*Stable `known_good` with module-scoped validation.*

The selected model keeps `reference_integration` focused on the integrated stack while leaving module-owned quality checks in the module repositories. In practice, that means `reference_integration` promotes one explicit stack, runs the integration-scoped checks that belong to the shared workspace, and validates the module repositories against the dependency set resolved by that stack.

This gives S-CORE a strong integration contract without forcing every verification concern into the central repository. The important consequence is that the integrated baseline remains the source of truth for cross-repository evidence, but the diagnostic depth of module-local validation stays close to the owning teams.

The remaining work is operational rather than architectural: standardized handoff of resolved dependency versions, reliable consolidation of reports and artifacts, and clear handling of temporary validation state so release evidence stays auditable.
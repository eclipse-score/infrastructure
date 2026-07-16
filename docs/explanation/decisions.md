# Infrastructure Design Decisions

Key architectural decisions that shape the S-CORE infrastructure. Each entry summarizes the problem, the decision made, and the main tradeoff. Full decision records live in the [S-CORE Handbook](https://eclipse-score.github.io/score/main/handbook).

---

## DR-003 — Devcontainer: Monolithic Image vs. Multi-Container

**Problem**: S-CORE repositories need a shared local environment for tools that are not delivered by the primary build flow (editors, formatters, linters, documentation tooling). The question was whether to use a single shared container image or a Docker Compose setup with one container per concern.

**Decision**: Monolithic image — one `ghcr.io/eclipse-score/devcontainer` image that carries all shared tools.

**Rationale**: Keeps the contributor entry point simple (one container, one `devcontainer.json`). Avoids orchestration complexity of managing multiple containers for a development-time convenience layer.

**Tradeoff**: The image is larger than any individual contributor needs. Pre-built images and layer caching mitigate startup cost in practice.

**Effect on docs**: Section [2.1 Central Devcontainer](02-developer-environment.md#central-devcontainer) describes how repositories consume this image.

---

## DR-001-Strat — Consistent Stack Direction

**Problem**: S-CORE consists of many independently-developed component repositories. Without a defined integration model, there is no canonical answer for "which combination of component versions is the validated S-CORE stack at any given moment."

**Decision**: Establish a `known_good` integration manifest that identifies which component revisions belong together in one validated stack. This is the authoritative record of integration state, distinct from individual component releases.

**Effect on docs**: The `known_good` concept is described in [Glossary: known_good](../reference/glossary.md#k). The integration model is implemented through [reference_integration](../reference/glossary.md#r).

**Full DR**: [DR-001-Strat](https://eclipse-score.github.io/score/main/design_decisions/DR-001-strat.html)

---

## DR-002-Infra — Distributed-Monolith Integration Model

**Problem**: With `known_good` established as the integration unit, the question is what the integration environment (`reference_integration`) should do: assemble the stack, validate it, and produce evidence — but with what ownership and scope?

**Decision**: Adopt a distributed-monolith integration model. Component repositories own their individual verification. `reference_integration` assembles the `known_good` manifest, runs cross-repository validation on it, and promotes it on success.

**Effect on docs**: The cross-repository CI orchestration flow is described in [7.3 Cross-Repository Integration](07-automation-integration.md#cross-repository-integration). The CI promotion model is described in [7.3.4 Known-Good Promotion](07-automation-integration.md#known-good-promotion).

**Full DR**: [DR-002-Infra](https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html)

---

## DR-008-Int — `reference_integration` Scope

**Status**: Decided. Option 4 was selected.

**Decision**: Use a stable `known_good` baseline with module-scoped validation. `reference_integration` promotes one explicit integrated stack, runs the integration-scoped checks on that stack, and validates module repositories against the dependency set resolved by the integrated baseline.

**Effect on docs**: Chapter [7](07-automation-integration.md) describes the CI promotion flow against the selected baseline. Chapter [11](11-reference-integration.md) is the canonical explanation of the integration workspace, promotion model, and evidence boundary.

**Full DR**: [DR-008-Int](https://github.com/qorix-group/score/blob/da4ea900f1eece5c8e795697d71e277446dca84e/docs/design_decisions/DR-008-int.rst?plain=1)

---

## `known_good` Architecture Note

This section was formerly part of [Chapter 3 § 3.2.7](03-build-infrastructure.md#dependency-management) and moved here because it describes an architectural decision context, not a current build capability.

`reference_integration` introduced the idea of a `known_good` set: an explicit manifest of which component revisions belong together in one integrated S-CORE stack. The core content is a tuple of `(component, commit)` pairs plus metadata. This should not be described as just another Bazel lock file — it sits one level above that:

- A **lock file** (`MODULE.bazel.lock`, `uv.lock`) captures the resolved dependency graph that a concrete Bazel workspace consumes.
- A **`known_good` manifest** is the curated integration selection from which Bazel-facing inputs can be generated. It can also carry automation metadata such as timestamps, suite identity, and which branch should be followed for automated CI refreshes.

`known_good` should be version-controlled, diffable, reproducible, and clearly distinct from generated Bazel lock data. The concrete file format matters less than that behavior.

**Decision background**: [DR-001-Strat](https://eclipse-score.github.io/score/main/design_decisions/DR-001-strat.html) · [DR-002-Infra](https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html) · [DR-008-Int](https://github.com/qorix-group/score/blob/da4ea900f1eece5c8e795697d71e277446dca84e/docs/design_decisions/DR-008-int.rst?plain=1)

# Contributing

This repository contains the source for the S-CORE infrastructure documentation. Contributions should improve clarity, keep the information architecture coherent, and make the documentation easier to use for both humans and tools.

## Site Purpose & Audience

The published site serves infrastructure contributors who need to understand current state, gaps, and direction, plus technical and non-technical stakeholders who need an overview. It covers the capabilities that make engineering work possible and scalable across S-CORE: source code infrastructure, developer environment, builds, testing, code analysis, compliance, automation, release distribution, documentation, traceability, and operations.

## Documentation Structure

The site uses the [Divio documentation system](https://docs.divio.com/documentation-system/) with four content types:

| Quadrant | Purpose | Location |
|---|---|---|
| **Tutorials** | Step-by-step learning guides for newcomers | `docs/tutorials/` |
| **How-to Guides** | Task-oriented recipes for practitioners | `docs/how-to/` |
| **Reference** | Factual lookup material (repos, config, versions) | `docs/reference/` |
| **Explanation** | Architecture, design rationale, maturity assessment | `docs/explanation/` |

Each quadrant serves a different reader need. When editing, know which quadrant a change belongs in and write for that quadrant's purpose. Do not mix content types — a how-to should not explain architecture, and an explanation should not read like a step-by-step recipe.

The explanation quadrant contains numbered landscape chapters (`01-source-code-infrastructure.md` through `10-infrastructure-operations.md`) that are capability-oriented and grounded in the actual repositories that implement the infrastructure. Cross-cutting concerns such as security and compliance are described inside the chapters where the work happens rather than as standalone silos.

## Working On The Documentation

Use the published site for content consumption and this repository for source edits, review, and validation.

For local work:

```bash
bazel run //:live_preview   # local preview with live reload
bazel run //:docs_check     # quick check during development
bazel run //:docs           # full build — required before commit
bazel run //:ide_support    # create .venv_docs for IDE integration
```

A contribution is not complete until `bazel run //:docs` passes cleanly.

The numbered chapter files under `docs/explanation/` drive the generated
chapter-map section in `docs/explanation/index.md`. That section is refreshed
automatically by pre-commit whenever the chapter heading structure changes. If
you are not using pre-commit, run `python3 scripts/generate_mindmap.py` manually
before committing.

If you use pre-commit locally, install the hooks once with:

```bash
pre-commit install
```

## Documentation Style

Prefer short prose over long bullet lists. Bullets are useful for genuinely list-shaped content such as commands, checklists, or grouped links, but explanatory sections should read like normal English.

When a topic spans multiple chapters in the explanation quadrant, choose one canonical home for the end-to-end explanation. Other chapters should describe only their local perspective and link back to the canonical section instead of repeating the same narrative. This keeps the reader experience coherent and prevents drift between chapters.

Explain the mental model first, then the practical steps. Readers should understand what a thing is for before being asked to configure or operate it. When configuration is important, include a minimal concrete snippet rather than describing it abstractly.

Link to authoritative upstream documentation when it owns the procedure. Do not copy long release checklists or external workflows into this repository when a maintained upstream README or manual already exists. Instead, explain how that external source fits into the S-CORE infrastructure story.

## Cross-Chapter Topics

Cross-cutting topics are expected in the explanation quadrant, but they should still feel unified to the reader.

- Put the main narrative in the chapter that best matches the topic's primary purpose.
- Let build-oriented chapters explain consumption and configuration.
- Let release and distribution chapters explain publication, discoverability, and user-facing flow.
- Let operations chapters explain service ownership, monitoring, and recovery.
- Use short cross-references instead of parallel explanations when a chapter only needs the topic from one angle.

The current reference example for this pattern is the Bazel registry writeup:

- [docs/explanation/08-artifact-distribution.md](docs/explanation/08-artifact-distribution.md) is the canonical end-to-end explanation.
- [docs/explanation/03-build-infrastructure.md](docs/explanation/03-build-infrastructure.md) keeps only the build-consumer perspective.
- [docs/explanation/10-infrastructure-operations.md](docs/explanation/10-infrastructure-operations.md) keeps only the operations perspective.

The developer-tooling and devcontainer story follows the same rule:

- [docs/explanation/02-developer-environment.md](docs/explanation/02-developer-environment.md) is the canonical explanation of how contributors obtain and use the shared environment locally.
- [docs/explanation/03-build-infrastructure.md](docs/explanation/03-build-infrastructure.md) keeps the toolchain, reproducibility, and build-evidence perspective.
- [docs/explanation/05-static-analysis-infrastructure.md](docs/explanation/05-static-analysis-infrastructure.md) keeps the policy and rule-baseline perspective.
- [docs/explanation/07-automation-integration.md](docs/explanation/07-automation-integration.md) keeps the CI-delivery and gating perspective.

Language support split across toolchain repositories and policy repositories follows the same rule:

- [docs/explanation/03-build-infrastructure.md](docs/explanation/03-build-infrastructure.md) is the canonical explanation of how Bazel toolchain modules such as `toolchains_rust` or `bazel_cpp_toolchains` provide compiler and toolchain integration.
- [docs/explanation/05-static-analysis-infrastructure.md](docs/explanation/05-static-analysis-infrastructure.md) keeps the shared rule-baseline perspective for policy modules such as `score_rust_policies` and `score_cpp_policies`.
- [docs/explanation/04-testing-infrastructure.md](docs/explanation/04-testing-infrastructure.md) keeps the runtime-execution perspective for sanitizers and other dynamic checks that may be enabled by those policies.

## Review Checklist

Before opening or merging a change, check the following:

- The change is in the right Divio quadrant.
- The main explanation lives in one place.
- Neighboring chapters do not repeat the same prose unnecessarily.
- Explanatory sections read as prose, not as bullet dumps.
- How-to guides are concrete and task-oriented.
- Configuration details are concrete and minimal.
- External procedures are linked, not copied.
- Links and navigation still work.
- `bazel run //:docs` passes.

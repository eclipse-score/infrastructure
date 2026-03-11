# Work Breakdown Structure

A Work Breakdown Structure (WBS) groups infrastructure work into stable work packages instead of short-lived tasks or issue lists. In S-CORE, it is used to make platform work visible across repositories and over time so engineers, project managers, infrastructure contributors, and safety or compliance stakeholders can see what already exists, what is underway, and what still needs attention.

The capability map explains what the platform is. The WBS explains what work exists within that platform.

The work packages below are intentionally high level. Each package can span multiple repositories, workflows, and iterations. Status is conservative: when maturity is unclear, the package stays at done only when it is directly visible, and otherwise remains in progress, not started, or planned.

Status legend:

- 🟢 done
- 🟡 in progress
- 🔴 not started
- ⚪ planned / idea

## Source Platform

The Source Platform covers the work needed to keep repository management, collaboration controls, and repository standards usable across a multi-repository GitHub environment. The work is not only about creating repositories, but also about making them consistent enough to support shared automation and governance.

| Work Package | Status | Notes |
|---|---|---|
| GitHub organization structure | 🟡 in progress | The organization structure exists and can still be refined for long-term consistency. |
| Repository templates | ⚪ planned / idea | Shared starting points would reduce repeated setup work. |
| Repository policy automation | 🟡 in progress | Policy controls are part of the current platform direction. |
| Repository standardization | 🟡 in progress | Baseline files and conventions are being aligned across repositories. |
| Repository lifecycle management | 🔴 not started | A consistent create-to-archive model is not yet documented. |
| Automated repository provisioning (Otterdog) | 🟡 in progress | Otterdog is relevant for organization-level automation and provisioning. |

### How contributors can help

- Document where repository behavior still differs between repositories.
- Improve reusable standards only when they can be adopted beyond a single repository.
- Clarify the intended policy outcome before adding more source-platform automation.

## Build Platform

The Build Platform covers the longer-running work needed to make Bazel-based builds reliable, reproducible, diagnosable, and scalable across repositories. It connects developer experience with dependency control and trustworthy build outputs.

| Work Package | Status | Notes |
|---|---|---|
| Bazel build infrastructure | 🟡 in progress | Bazel is a core technology, but shared platform work continues. |
| Bazel module registry | 🟡 in progress | The registry is part of the infrastructure landscape and still evolving. |
| Dependency management strategy | 🟡 in progress | Dependency control is a recognized platform concern across repositories. |
| Bazel module publishing | 🔴 not started | Publishing flow and governance are not yet visible as an established model. |
| Build reproducibility | 🟡 in progress | Reproducibility is a clear goal, with more platform work ahead. |
| Build caching infrastructure | 🔴 not started | A shared caching service is not yet visible as a mature platform capability. |
| Build diagnostics and developer tooling | 🔴 not started | Better build insight and troubleshooting support are still needed. |

### How contributors can help

- Capture recurring build pain points that appear across repositories.
- Improve reproducibility and dependency guidance before optimizing edge cases.
- Add diagnostics that shorten local and CI troubleshooting time.

## CI/CD Platform

The CI/CD Platform covers the shared work needed to validate changes, run automation consistently, and turn repository events into predictable engineering workflows. The main goal is to reduce duplication while keeping execution understandable.

| Work Package | Status | Notes |
|---|---|---|
| Reusable workflow library | 🟡 in progress | Reusable workflows are already part of the platform direction. |
| CI pipeline templates | 🟡 in progress | Shared patterns exist conceptually and need broader consolidation. |
| Pull request validation pipelines | 🟡 in progress | Pull request validation is active, but standardization is ongoing. |
| Release pipelines | ⚪ planned / idea | Release automation needs a clearer common model. |
| Runner infrastructure | 🟡 in progress | Runner selection and execution environments are active platform work. |
| CI pipeline diagnostics | 🔴 not started | Faster root-cause analysis for CI failures is still limited. |
| CI performance optimization | 🔴 not started | Queue time, runtime, and caching optimization remain open work. |
| CI workflow documentation | 🟡 in progress | Platform workflow documentation has started and needs expansion. |

### How contributors can help

- Consolidate repeated workflow logic into reusable patterns.
- Improve feedback quality so pull request failures are easier to understand.
- Document runner and pipeline assumptions close to the workflows that depend on them.

## Artifact Platform

The Artifact Platform covers the work needed to decide what becomes a reusable artifact, how it is versioned, and how it moves between build, release, and downstream consumption. This area is important for traceability, but it usually matures later than basic build automation.

| Work Package | Status | Notes |
|---|---|---|
| Artifact storage strategy | 🔴 not started | Storage boundaries and retention rules need clearer definition. |
| Artifact versioning model | 🔴 not started | A stable cross-platform versioning model is not yet documented. |
| Artifact promotion model | ⚪ planned / idea | Promotion stages need a shared platform definition. |
| Artifact distribution | 🔴 not started | Distribution paths beyond local workflow use remain to be clarified. |
| Bazel registry distribution model | 🟡 in progress | The Bazel registry provides a concrete starting point for distribution. |

### How contributors can help

- Clarify which outputs should become reusable platform artifacts.
- Define minimal versioning and promotion rules before adding more automation.
- Document consumer expectations for registry and release outputs.

## Testing Platform

The Testing Platform covers the shared work needed to execute tests consistently, integrate different test styles into build and CI workflows, and make results actionable. The focus is on reliable validation rather than repository-specific test cases.

| Work Package | Status | Notes |
|---|---|---|
| CI test execution infrastructure | 🟡 in progress | CI-driven test execution exists and still needs broader consistency. |
| Integration test infrastructure | 🔴 not started | Shared support for integration testing is not yet clearly established. |
| Test framework integration | 🟡 in progress | Bazel and pytest integration are relevant and still evolving. |
| Test reporting | 🔴 not started | Result visibility and failure interpretation need more platform support. |
| Coverage reporting | 🔴 not started | Coverage aggregation and publication are not yet a visible baseline. |
| Cross-repository integration testing | ⚪ planned / idea | Multi-repository validation is an important later step. |

### How contributors can help

- Make CI test behavior easier to understand and reproduce locally.
- Improve reporting so failures become actionable instead of noisy.
- Identify where shared integration or cross-repository validation adds the most value.

## Security & Compliance Platform

The Security and Compliance Platform covers the work needed to surface licensing, vulnerability, and software composition information in a way that supports real engineering decisions. The goal is practical transparency, not isolated paperwork.

| Work Package | Status | Notes |
|---|---|---|
| License scanning integration | 🟡 in progress | Eclipse Dash license tooling is relevant and needs stable workflow integration. |
| Dependency vulnerability scanning | 🟡 in progress | Vulnerability visibility is part of the emerging platform direction. |
| SBOM generation | 🟡 in progress | SBOM work is emerging, with scope and outputs still maturing. |
| SBOM publication | ⚪ planned / idea | Publication and consumption paths need a clearer model. |
| Compliance reporting | 🔴 not started | Consolidated reporting is not yet visible as a platform capability. |
| Security workflow automation | 🔴 not started | More repeatable handling of findings and exceptions is still ahead. |

### How contributors can help

- Improve scan visibility and interpretation for contributors and reviewers.
- Connect license, vulnerability, and SBOM data to existing build and CI flows.
- Document exception handling before expanding automation further.

## Documentation Platform

The Documentation Platform covers the work needed to keep infrastructure knowledge versioned, reviewable, buildable, and publishable. In S-CORE, this is a docs-as-code capability built with Markdown and MkDocs for this repository.

| Work Package | Status | Notes |
|---|---|---|
| Infrastructure documentation repository | 🟢 done | A dedicated docs-as-code repository exists. |
| Documentation structure and navigation | 🟡 in progress | Core structure exists and can expand as the platform grows. |
| Documentation build pipelines | 🟢 done | MkDocs builds are automated through repository workflows. |
| Documentation publishing | 🟢 done | GitHub Pages workflow-mode publishing is configured. |
| Contributor documentation | 🟡 in progress | Guidance exists and should deepen with more operational detail. |
| Infrastructure architecture documentation | 🔴 not started | Higher-level architecture views are still limited. |

### How contributors can help

- Add missing operational guides and architecture views where decisions need context.
- Keep MkDocs navigation aligned with real contributor workflows.
- Expand contributor guidance where infrastructure decisions are still hard to follow.

## Platform Operations

The Platform Operations area covers the work needed to keep the infrastructure healthy after it has been introduced. It includes maintenance, monitoring, upgrades, and recovery-oriented practices that turn platform components into dependable services.

| Work Package | Status | Notes |
|---|---|---|
| Runner maintenance | 🟡 in progress | Runner operation exists, but maintenance practice still needs clearer codification. |
| Platform monitoring | 🟡 in progress | Monitoring needs clearer platform-level baselines and signals. |
| Infrastructure upgrades | 🔴 not started | Upgrade planning and rollout patterns are not yet documented as standard. |
| Dependency update automation | ⚪ planned / idea | Automation can reduce manual drift but needs a stable approach. |
| Incident handling procedures | 🔴 not started | Shared response guidance is still limited. |
| Platform observability | ⚪ planned / idea | Broader observability would complement basic monitoring and troubleshooting. |

### How contributors can help

- Define baseline signals for health, failure, and recovery before adding more dashboards.
- Document repeatable maintenance and incident steps that reduce tribal knowledge.
- Reduce manual operational work only after the desired control points are clear.
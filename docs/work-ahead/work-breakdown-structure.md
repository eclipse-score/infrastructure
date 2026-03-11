# Work Breakdown Structure

The Work Breakdown Structure (WBS) is the practical work map for S-CORE infrastructure.

- capability map: what the platform is
- WBS: what work exists, what is in progress, and what remains

Status legend:

- `done`
- `in progress`
- `planned`
- `not started`

## How To Use This Page

- contributors: find areas where help is needed now
- managers: review progress by capability area
- safety/compliance readers: track work connected to traceability and controls

## Source Platform Work Packages { #wbs-source }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Organization and repository structure | in progress | Multi-repository structure is established and still being refined. | [Repository onboarding](../guides/repository-onboarding.md) |
| Repository baseline standards | in progress | Baseline conventions exist and require ongoing alignment. | [Repository onboarding](../guides/repository-onboarding.md) |
| Repository policy automation | in progress | Policies are visible and need consistent codification. | [Repository policies](../guides/repository-policies.md) |
| Repository lifecycle model | planned | Create-to-archive flow needs clearer shared guidance. | [Repository onboarding](../guides/repository-onboarding.md) |
| Otterdog-based automation | in progress | Otterdog is relevant for organization and repository automation. | [Repository policies](../guides/repository-policies.md) |

## Build Platform Work Packages { #wbs-build }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Bazel build baseline | in progress | Bazel is a core build technology and shared practices are still maturing. | [Bazel and dependencies](../guides/bazel-and-dependencies.md) |
| Bzlmod dependency model | in progress | Module and dependency handling is active platform work. | [Bazel and dependencies](../guides/bazel-and-dependencies.md) |
| Bazel registry integration | in progress | Registry usage exists and needs stronger workflow guidance. | [Artifact publishing](../guides/artifact-publishing.md) |
| Build reproducibility improvements | in progress | Reproducibility is a priority across repositories. | [Bazel and dependencies](../guides/bazel-and-dependencies.md) |
| Build diagnostics and performance tooling | planned | Shared diagnostics and performance workflows need expansion. | [Bazel and dependencies](../guides/bazel-and-dependencies.md) |

## CI/CD Platform Work Packages { #wbs-cicd }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Reusable workflow library | in progress | Reusable workflows are central and continue to expand. | [CI/CD workflows](../guides/cicd-workflows.md) |
| Pull request validation model | in progress | Validation is active; standardization still in progress. | [CI/CD workflows](../guides/cicd-workflows.md) |
| Runner strategy and execution model | in progress | Runner and large runner usage remains active platform work. | [CI/CD workflows](../guides/cicd-workflows.md) |
| Pipeline diagnostics and signal quality | planned | Better failure clarity and diagnostics are needed. | [CI/CD workflows](../guides/cicd-workflows.md) |
| Release and publication automation | planned | Shared release flow needs stronger common model. | [Artifact publishing](../guides/artifact-publishing.md) |

## Artifact Platform Work Packages { #wbs-artifacts }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Artifact storage model | planned | Storage boundaries and retention need clearer guidance. | [Artifact publishing](../guides/artifact-publishing.md) |
| Artifact versioning model | planned | Cross-area versioning expectations still evolving. | [Artifact publishing](../guides/artifact-publishing.md) |
| Artifact lifecycle and promotion | planned | Promotion stages are not yet fully standardized. | [Artifact publishing](../guides/artifact-publishing.md) |
| Bazel registry distribution model | in progress | Registry is the strongest current distribution path. | [Artifact publishing](../guides/artifact-publishing.md) |

## Testing Platform Work Packages { #wbs-testing }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Test execution consistency in CI | in progress | CI test execution exists and needs better consistency. | [Testing and reporting](../guides/testing-and-reporting.md) |
| Test framework integration | in progress | Bazel and framework integration remains active work. | [Testing and reporting](../guides/testing-and-reporting.md) |
| Test reporting and diagnostics | planned | Reporting quality and visibility need improvements. | [Testing and reporting](../guides/testing-and-reporting.md) |
| Cross-repository test strategy | planned | Cross-repository validation is an important next step. | [Testing and reporting](../guides/testing-and-reporting.md) |

## Security & Compliance Platform Work Packages { #wbs-security }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| License scanning integration | in progress | License workflows are relevant and still maturing. | [License compliance and SBOM](../guides/license-compliance-and-sbom.md) |
| Vulnerability scanning and triage | in progress | Vulnerability visibility and triage flow need ongoing work. | [License compliance and SBOM](../guides/license-compliance-and-sbom.md) |
| SBOM generation workflow | in progress | SBOM activities exist and need consistent implementation. | [License compliance and SBOM](../guides/license-compliance-and-sbom.md) |
| Compliance reporting model | planned | Shared reporting and escalation paths need definition. | [License compliance and SBOM](../guides/license-compliance-and-sbom.md) |

## Documentation Platform Work Packages { #wbs-documentation }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Documentation structure and navigation | in progress | Structure is being aligned to area/task navigation. | [Documentation publishing](../guides/documentation-publishing.md) |
| Documentation build and validation | done | MkDocs build and strict validation are established. | [Documentation publishing](../guides/documentation-publishing.md) |
| Documentation publishing workflow | done | GitHub Pages workflow-mode publishing is in place. | [Documentation publishing](../guides/documentation-publishing.md) |
| Contributor documentation quality | in progress | More practical guidance is still being added. | [Repository onboarding](../guides/repository-onboarding.md) |

## Platform Operations Work Packages { #wbs-operations }

| Work package | Status | Notes | Related guide |
| --- | --- | --- | --- |
| Runner and platform maintenance | in progress | Maintenance work is ongoing and needs stronger runbook coverage. | [Operations and maintenance](../guides/operations-and-maintenance.md) |
| Monitoring baseline and signals | in progress | Baseline signals are evolving across workflows. | [Operations and maintenance](../guides/operations-and-maintenance.md) |
| Incident handling model | planned | Shared incident process and response guidance need expansion. | [Operations and maintenance](../guides/operations-and-maintenance.md) |
| Upgrade and dependency operations | planned | Planned operational model for upgrades requires codification. | [Operations and maintenance](../guides/operations-and-maintenance.md) |

## Related Pages

- [Contribution Areas](contribution-areas.md)
- [Current focus areas](current-focus-areas.md)
- [Capability Map](../start-here/capability-map.md)
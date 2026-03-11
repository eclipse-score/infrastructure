# Work Breakdown Structure

This page provides a more detailed work package view than the Infrastructure Development Map.

Use it when you need a structured list of infrastructure work by area.

Status legend:

- 🟢 done
- 🟡 in progress
- 🔴 not started
- ⚪ planned / not yet defined

## Source Code Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| Organization and repository structure baseline | 🟡 in progress | Shared structure exists and still needs tighter standardization. |
| Repository baseline standards | 🟡 in progress | Baseline conventions are documented but not uniformly applied. |
| Repository policy automation with Otterdog | 🟡 in progress | Automation is active in parts of the organization. |
| Repository lifecycle guidance | ⚪ planned / not yet defined | Lifecycle expectations are not fully documented. |

## Build Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| Bazel build baseline alignment | 🟡 in progress | Build conventions are established but still diverge between repositories. |
| Bzlmod dependency governance | 🟡 in progress | Module and dependency handling is under active refinement. |
| Bazel registry integration baseline | 🟡 in progress | Registry usage is relevant and still being consolidated. |
| Build diagnostics and performance reporting | ⚪ planned / not yet defined | Shared diagnostics and metrics need stronger baseline practices. |

## Integration Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| Reusable workflow library | 🟡 in progress | Reusable workflows are central and still expanding. |
| Pull request validation model | 🟡 in progress | Validation behavior is not yet fully harmonized. |
| Runner strategy and execution model | 🟡 in progress | Runner usage guidance is still maturing. |
| Pipeline diagnostics and optimization | ⚪ planned / not yet defined | Better diagnostics and optimization routines are needed. |

## Artifact Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| Artifact storage and retention model | ⚪ planned / not yet defined | Shared retention boundaries are not yet clearly defined. |
| Artifact lifecycle and promotion model | 🔴 not started | Promotion stage model has not been standardized. |
| Artifact versioning baseline | ⚪ planned / not yet defined | Versioning expectations are documented only in parts. |
| Bazel registry distribution model | 🟡 in progress | Distribution model exists and requires further operational clarity. |

## Testing Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| CI test execution consistency | 🟡 in progress | Baseline execution exists; consistency is still improving. |
| Test framework integration patterns | 🟡 in progress | Integration patterns are not yet uniformly documented. |
| Test reporting and diagnostics quality | ⚪ planned / not yet defined | Reporting quality and signal consistency need improvement. |
| Cross-repository test strategy | ⚪ planned / not yet defined | Shared strategy is still being defined. |

## Security & Compliance Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| License scanning integration baseline | 🟡 in progress | License scanning workflows are in place in parts of the infrastructure. |
| Vulnerability scanning and triage workflow | 🟡 in progress | Triage ownership and escalation are still evolving. |
| SBOM generation and consumption model | 🟡 in progress | SBOM generation exists; consumption and reporting are not fully aligned. |
| Compliance reporting model | ⚪ planned / not yet defined | Shared reporting model is not yet complete. |

## Documentation Infrastructure

| Work Package | Status | Notes |
| --- | --- | --- |
| Documentation structure and navigation | 🟡 in progress | Information architecture is being aligned around infrastructure areas. |
| Documentation build and validation baseline | 🟢 done | Strict MkDocs build baseline is established. |
| Documentation publishing workflow | 🟢 done | Publishing workflow is in place and regularly used. |
| Contributor guidance quality improvements | 🟡 in progress | Practical guidance is being expanded across guides and area pages. |

## Infrastructure Operations

| Work Package | Status | Notes |
| --- | --- | --- |
| Runner and execution environment maintenance | 🟡 in progress | Operational work exists with partial automation. |
| Monitoring baseline and signal ownership | ⚪ planned / not yet defined | Metrics and alert ownership are still being formalized. |
| Incident handling model and runbooks | ⚪ planned / not yet defined | Shared response process remains under definition. |
| Upgrade and dependency operations baseline | ⚪ planned / not yet defined | Repeatable upgrade workflows need stronger codification. |

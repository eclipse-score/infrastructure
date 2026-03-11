# Work Breakdown Structure

This page is the canonical register of infrastructure work packages.

Use this page when you need package-level detail, including:

- stable IDs for tracking and discussion
- current status
- dependency context
- expected delivery outcome

For high-level status and priorities, use the [Infrastructure Development Map](infrastructure-development-map.md).

Status legend:

- 🟢 done
- 🟡 in progress
- 🔴 not started
- ⚪ planned / not yet defined

## Work Package Register

| ID | Area | Work Package | Status | Expected Outcome | Dependencies |
| --- | --- | --- | --- | --- | --- |
| SCI-01 | Source Code Infrastructure | Organization and repository structure baseline | 🟡 | Shared baseline structure is documented and repeatable across repositories. | - |
| SCI-02 | Source Code Infrastructure | Repository baseline standards | 🟡 | Baseline conventions are consistently applied with documented exceptions. | SCI-01 |
| SCI-03 | Source Code Infrastructure | Repository policy automation with Otterdog | 🟡 | Policy baseline is codified and easier to roll out consistently. | SCI-02 |
| SCI-04 | Source Code Infrastructure | Repository lifecycle guidance | ⚪ | Lifecycle from onboarding to archival is clearly documented. | SCI-01 |
| BLD-01 | Build Infrastructure | Bazel build baseline alignment | 🟡 | Core Bazel conventions are aligned across active repositories. | SCI-02 |
| BLD-02 | Build Infrastructure | Bzlmod dependency governance | 🟡 | Dependency decisions are more consistent and reviewable. | BLD-01 |
| BLD-03 | Build Infrastructure | Bazel registry integration baseline | 🟡 | Registry usage is clearer for producers and consumers. | BLD-01, ART-04 |
| BLD-04 | Build Infrastructure | Build diagnostics and performance reporting | ⚪ | Build diagnostics are easier to use for troubleshooting and optimization. | BLD-01, INT-04 |
| INT-01 | Integration Infrastructure | Reusable workflow library | 🟡 | Shared workflow coverage reduces duplicated pipeline logic. | SCI-02 |
| INT-02 | Integration Infrastructure | Pull request validation model | 🟡 | Validation stages are more consistent across repositories. | INT-01, TST-01 |
| INT-03 | Integration Infrastructure | Runner strategy and execution model | 🟡 | Runner usage is more predictable and better documented. | OPS-01 |
| INT-04 | Integration Infrastructure | Pipeline diagnostics and optimization | ⚪ | Integration failures are easier to triage and optimize. | INT-01, INT-03 |
| ART-01 | Artifact Infrastructure | Artifact storage and retention model | ⚪ | Retention expectations are explicit and easier to apply. | SCI-04 |
| ART-02 | Artifact Infrastructure | Artifact lifecycle and promotion model | 🔴 | Promotion stages are defined and traceable. | ART-01 |
| ART-03 | Artifact Infrastructure | Artifact versioning baseline | ⚪ | Versioning expectations are consistent across artifact types. | ART-02, BLD-02 |
| ART-04 | Artifact Infrastructure | Bazel registry distribution model | 🟡 | Registry distribution path is clearer and easier to maintain. | BLD-03 |
| TST-01 | Testing Infrastructure | CI test execution consistency | 🟡 | Test execution expectations are clearer between repositories. | INT-01, BLD-01 |
| TST-02 | Testing Infrastructure | Test framework integration patterns | 🟡 | Framework integration becomes more predictable and reusable. | TST-01 |
| TST-03 | Testing Infrastructure | Test reporting and diagnostics quality | ⚪ | Reporting signals are more actionable for contributors. | TST-01, INT-04 |
| TST-04 | Testing Infrastructure | Cross-repository test strategy | ⚪ | Shared strategy exists for cross-repository validation scenarios. | TST-01, TST-02 |
| SEC-01 | Security & Compliance Infrastructure | License scanning integration baseline | 🟡 | License checks are integrated more consistently in workflows. | INT-01, BLD-02 |
| SEC-02 | Security & Compliance Infrastructure | Vulnerability scanning and triage workflow | 🟡 | Triage ownership and escalation path are clearer. | SEC-01 |
| SEC-03 | Security & Compliance Infrastructure | SBOM generation and consumption model | 🟡 | SBOM data is generated and consumed with clearer expectations. | BLD-02, ART-03 |
| SEC-04 | Security & Compliance Infrastructure | Compliance reporting model | ⚪ | Compliance reporting is clearer for managers and stakeholders. | SEC-01, SEC-02, SEC-03 |
| DOC-01 | Documentation Infrastructure | Documentation structure and navigation | 🟡 | Information architecture stays consistent and easier to navigate. | - |
| DOC-02 | Documentation Infrastructure | Documentation build and validation baseline | 🟢 | Strict documentation validation remains stable and reliable. | DOC-01 |
| DOC-03 | Documentation Infrastructure | Documentation publishing workflow | 🟢 | Publishing remains reliable for documentation changes. | DOC-02 |
| DOC-04 | Documentation Infrastructure | Contributor guidance quality improvements | 🟡 | Practical guidance quality improves across key workflows. | DOC-01 |
| OPS-01 | Infrastructure Operations | Runner and execution environment maintenance | 🟡 | Runner operations are better documented and more predictable. | INT-03 |
| OPS-02 | Infrastructure Operations | Monitoring baseline and signal ownership | ⚪ | Key operational signals and ownership become explicit. | OPS-01 |
| OPS-03 | Infrastructure Operations | Incident handling model and runbooks | ⚪ | Incident response is more consistent and less ad hoc. | OPS-02 |
| OPS-04 | Infrastructure Operations | Upgrade and dependency operations baseline | ⚪ | Upgrade operations become more repeatable and transparent. | OPS-01, OPS-02 |

## Usage Notes

- Update this register when work package scope or dependency assumptions change.
- Keep IDs stable once introduced.
- Reflect status changes first here, then summarize them in the [Infrastructure Development Map](infrastructure-development-map.md).

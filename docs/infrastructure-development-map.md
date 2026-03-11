# Infrastructure Development Map

This page is the central entry point for understanding where S-CORE infrastructure stands and what work remains.

Infrastructure areas describe the landscape. Work packages describe the work.

Use this page to quickly see:

- current state by area
- main work packages
- contribution opportunities
- where to drill down next

## Area Overview

| Area | Current State | Main Work Packages | Contribution Opportunities |
| --- | --- | --- | --- |
| [Source Code Infrastructure](areas/source-code-infrastructure/index.md) | Foundations in place; repository standards and policy automation are partially established. | Repository baseline standards, policy automation, lifecycle guidance. | Improve repository templates, standardize metadata, document exception handling. |
| [Build Infrastructure](areas/build-infrastructure/index.md) | Bazel is established; Bzlmod and registry workflows are still under active development. | Build baseline alignment, dependency governance, reproducibility improvements. | Improve Bazel module onboarding, strengthen diagnostics, reduce configuration drift. |
| [Integration Infrastructure](areas/integration-infrastructure/index.md) | GitHub Actions and reusable workflows are used in parts; harmonization is ongoing. | PR validation model, reusable workflow library, runner strategy, diagnostics. | Improve reusable workflows, clarify pipeline outputs, improve runner usage guidance. |
| [Artifact Infrastructure](areas/artifact-infrastructure/index.md) | Publication paths exist in parts; lifecycle and retention rules are still evolving. | Storage model, lifecycle and promotion, versioning baseline, distribution clarity. | Define lifecycle rules, improve publication documentation, reduce manual publishing steps. |
| [Testing Infrastructure](areas/testing-infrastructure/index.md) | Baseline CI testing exists; framework integration and reporting are fragmented. | CI test execution consistency, framework integration, reporting quality. | Strengthen reporting, document test expectations, improve unstable test handling. |
| [Security & Compliance Infrastructure](areas/security-and-compliance-infrastructure/index.md) | Scanning exists in parts; end-to-end governance and reporting are incomplete. | License scanning rollout, SBOM integration, vulnerability triage workflow. | Improve compliance automation, clarify triage ownership, strengthen reporting paths. |
| [Documentation Infrastructure](areas/documentation-infrastructure/index.md) | Docs-as-code foundations are in place; content consistency and cross-linking are still improving. | Navigation quality, review workflow, publishing reliability, contributor guidance. | Improve contributor-facing documentation, add missing links, refine page ownership. |
| [Infrastructure Operations](areas/infrastructure-operations/index.md) | Monitoring and maintenance are partially established; several operations are still manual. | Monitoring baseline, runbooks, incident handling model, upgrade operations. | Improve runner monitoring, document incident response, automate recurring maintenance. |

## Work Package Status

Status legend:

- 🟢 done
- 🟡 in progress
- 🔴 not started
- ⚪ planned / not yet defined

| Area | Work Package | Status | Notes |
| --- | --- | --- | --- |
| Source Code Infrastructure | Organization and repository structure baseline | 🟡 in progress | Multi-repository conventions exist, but consistency gaps remain. |
| Source Code Infrastructure | Repository policy automation with Otterdog | 🟡 in progress | Automation is used in parts and still being expanded. |
| Source Code Infrastructure | Repository lifecycle model | ⚪ planned / not yet defined | Create-to-archive process needs clearer shared guidance. |
| Build Infrastructure | Bazel build baseline alignment | 🟡 in progress | Core usage exists; cross-repository alignment is ongoing. |
| Build Infrastructure | Bzlmod dependency governance | 🟡 in progress | Dependency handling is active and still stabilizing. |
| Build Infrastructure | Build diagnostics and performance baseline | ⚪ planned / not yet defined | Shared diagnostics and performance reporting are incomplete. |
| Integration Infrastructure | Reusable workflow library expansion | 🟡 in progress | Reuse exists, but coverage is not yet systematic. |
| Integration Infrastructure | Pull request validation model | 🟡 in progress | Validation patterns differ between repositories. |
| Integration Infrastructure | Pipeline diagnostics and optimization baseline | ⚪ planned / not yet defined | Better diagnostics and optimization guidance are needed. |
| Artifact Infrastructure | Artifact lifecycle and promotion model | 🔴 not started | Shared promotion stages are not yet standardized. |
| Artifact Infrastructure | Artifact storage and retention baseline | ⚪ planned / not yet defined | Retention expectations require explicit rules. |
| Artifact Infrastructure | Bazel registry distribution model | 🟡 in progress | Registry usage is active and still being documented. |
| Testing Infrastructure | CI test execution consistency | 🟡 in progress | Baseline exists, but behavior is not fully aligned. |
| Testing Infrastructure | Test framework integration patterns | 🟡 in progress | Integration guidance is still evolving. |
| Testing Infrastructure | Test reporting and diagnostics quality | ⚪ planned / not yet defined | Reporting quality differs by repository and pipeline. |
| Security & Compliance Infrastructure | License scanning integration baseline | 🟡 in progress | Implemented in parts; rollout is incomplete. |
| Security & Compliance Infrastructure | SBOM generation and usage model | 🟡 in progress | SBOM activities exist, but usage expectations vary. |
| Security & Compliance Infrastructure | Compliance reporting model | ⚪ planned / not yet defined | Shared reporting and escalation paths are not yet mature. |
| Documentation Infrastructure | Documentation build and strict validation | 🟢 done | Local and CI strict MkDocs validation are established. |
| Documentation Infrastructure | Navigation and information architecture alignment | 🟡 in progress | Primary structure is being stabilized around infrastructure areas. |
| Documentation Infrastructure | Contributor documentation quality improvements | 🟡 in progress | Practical guidance quality is improving incrementally. |
| Infrastructure Operations | Runner and execution environment operations | 🟡 in progress | Operational practices exist, but tooling and documentation are uneven. |
| Infrastructure Operations | Incident handling model | ⚪ planned / not yet defined | Shared incident response model needs codification. |
| Infrastructure Operations | Monitoring baseline and alerting clarity | ⚪ planned / not yet defined | Signal quality and ownership are still evolving. |

## More Detailed Planning View

For a more detailed per-area list, see the [Work Breakdown Structure](work-breakdown-structure.md).

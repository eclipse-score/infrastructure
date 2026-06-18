# Infrastructure Landscape

Architecture, design rationale, and maturity assessment of each S-CORE infrastructure area. These chapters describe what exists, how it works, and what is still missing.

## Status Legend

- 🟢 Implemented and fit for purpose
- 🟡 Partially implemented / needs improvement
- 🟠 Implemented but problematic or insufficient
- 🔴 Not started
- ⚪ Unknown / not yet assessed

## Chapter Map

<!-- BEGIN GENERATED CHAPTER MAP -->

| Capability | Maturity | Impact |
|---|---|---|
| **[1 Source Code Infrastructure](01-source-code-infrastructure.md)** | 🟠 | Enforcement is missing — standards drift across repos and the current state is invisible until it causes a problem. |
| ↳ [1.1 Hosting & Organization](01-source-code-infrastructure.md#hosting-organization) | 🟡 | Not implemented — no documented org structure or naming conventions; repository ownership and boundaries are implicit. |
| ↳ [1.2 Repository Provisioning & Lifecycle](01-source-code-infrastructure.md#repository-provisioning-lifecycle) | 🟡 | Repos are set up manually with no standard template — required configurations are often missing and onboarding overhead varies per repo. |
| ↳ [1.3 Repository Policy Management](01-source-code-infrastructure.md#repository-policy-management) | 🔴 | Each repo sets its own rules — branch protection varies, merge queues are absent, and there is no shared enforcement baseline. Inconsistent merge practices slow down reviews and make the landscape hard to govern. |
| ↳ [1.4 Repository Standards](01-source-code-infrastructure.md#repository-standards) | 🟠 | Standards exist on paper but are not enforced — repos drift over time and the extent of non-compliance is not visible. |
| **[2 Developer Environment](02-developer-environment.md)** | 🟡 | Environment works for common cases but gaps mean some contributors hit setup friction that others don't. |
| ↳ [2.1 Central Devcontainer](02-developer-environment.md#central-devcontainer) | 🟡 | Devcontainer exists but has known problems — tooling gaps or reliability issues push contributors to work around it rather than through it. |
| ↳ [2.2 Local Auxiliary Tooling](02-developer-environment.md#local-auxiliary-tooling) | 🟡 | Some local tooling is available but setup varies per machine — contributors may get different results depending on their environment. |
| **[3 Build & Dependencies](03-build-infrastructure.md)** | 🟠 | Not implemented — no shared build baseline or dependency model exists yet across the project. |
| ↳ [3.1 Build System](03-build-infrastructure.md#build-system) | 🟢 | Not implemented — Bazel is used in individual repos but no shared build conventions or rule libraries are established. |
| ↳ [3.2 Dependency Management](03-build-infrastructure.md#dependency-management) | 🟡 | Not implemented — no shared dependency policy; each repo resolves third-party and internal dependencies independently. |
| ↳ [3.3 Toolchain Management](03-build-infrastructure.md#toolchain-management) | 🟠 | Not implemented — no shared toolchain modules; compiler and language runtime versions are not coordinated across repos. |
| ↳ [3.4 Build Reproducibility & Evidence](03-build-infrastructure.md#build-reproducibility-evidence) | 🔴 | Not implemented — no reproducibility guarantees or build evidence collected; builds cannot be audited or replayed reliably. |
| ↳ [3.5 Build Execution Infrastructure](03-build-infrastructure.md#build-execution-infrastructure) | 🔴 | Not implemented — no remote execution or shared caching infrastructure; every build is local and slow. |
| **[4 Testing](04-testing-infrastructure.md)** | 🟠 | Test infrastructure is in place but has rough edges — confidence in results is limited by gaps in coverage, flakiness, or incomplete reporting. |
| ↳ [4.1 Test Framework Integration](04-testing-infrastructure.md#test-framework-integration) | 🟡 | Frameworks are integrated but configuration is inconsistent across repos — some tests are missing or poorly structured, reducing coverage confidence. |
| ↳ [4.2 Test Execution & Dynamic Analysis](04-testing-infrastructure.md#test-execution-dynamic-analysis) | 🟠 | Traceability links exist but are incomplete — not all tests are linked to requirements, making it hard to assess verification coverage. |
| ↳ [4.4 Test Reporting](04-testing-infrastructure.md#test-reporting) | 🟠 | Reports are produced but not consistently actionable — aggregating results or tracking failures across repos requires manual effort. |
| **[5 Code Analysis Infrastructure](05-static-analysis-infrastructure.md)** | ⚪ | Not implemented — no shared linting, formatting, or static analysis baseline exists across repos. |
| ↳ [5.1 Tooling Baseline](05-static-analysis-infrastructure.md#tooling-baseline) | ⚪ | Not implemented — no shared set of analysis tools; each repo chooses its own or skips analysis entirely. |
| ↳ [5.2 Shared Rule Configuration](05-static-analysis-infrastructure.md#shared-rule-configuration) | ⚪ | Not implemented — no shared lint or policy modules; rule configuration is duplicated or absent across repos. |
| ↳ [5.3 Execution Model](05-static-analysis-infrastructure.md#execution-model) | ⚪ | Not implemented — no consistent way to run analysis in CI; results are not collected or comparable across repos. |
| ↳ [5.4 Security Scanning](05-static-analysis-infrastructure.md#security-scanning) | 🟠 | Scanning runs but results are not systematically reviewed or tracked — findings can go unaddressed without a clear triage or ownership process. |
| ↳ [5.5 Results and Governance](05-static-analysis-infrastructure.md#results-and-governance) | ⚪ | Not implemented — no aggregated view of analysis results; violations accumulate silently with no ownership or escalation path. |
| **[6 Compliance & Dependency Analysis](06-compliance-infrastructure.md)** | ⚪ | Not implemented — no automated license or dependency compliance checks; open-source obligations are unverified. |
| ↳ [6.1 File-Level Licensing](06-compliance-infrastructure.md#file-level-licensing) | ⚪ | Not implemented — no automated SPDX header checks; license coverage across files is unknown. |
| ↳ [6.2 Dependency Analysis](06-compliance-infrastructure.md#dependency-analysis) | ⚪ | Not implemented — no automated inventory of third-party dependencies; transitive licenses are not tracked. |
| ↳ [6.3 SBOM Scoping and Compliance Evidence](06-compliance-infrastructure.md#sbom-scoping-and-compliance-evidence) | ⚪ | Not implemented — no SBOM generated; cannot demonstrate compliance to consumers or auditors. |
| ↳ [6.4 License Checks and Compliance](06-compliance-infrastructure.md#license-checks-and-compliance) | ⚪ | Not implemented — no automated license compatibility checks; incompatible licenses could ship undetected. |
| ↳ [6.5 Monitoring and Governance](06-compliance-infrastructure.md#monitoring-and-governance) | ⚪ | Not implemented — no ongoing monitoring for new compliance violations introduced by dependency updates. |
| **[7 Automation Infrastructure & Continuous Integration (CI)](07-automation-integration.md)** | ⚪ | Not implemented — no shared CI baseline; each repo builds its own workflows from scratch with no reuse or coordination. |
| ↳ [7.1 Runners](07-automation-integration.md#runners) | 🟠 | Runners are operational but have known capacity or reliability issues — CI wait times are unpredictable and outages affect all repos simultaneously. |
| ↳ [7.2 Reusable Workflows](07-automation-integration.md#reusable-workflows) | ⚪ | Not implemented — no shared workflow library; CI logic is copy-pasted across repos and drifts independently. |
| ↳ [7.3 Cross-Repository Integration](07-automation-integration.md#cross-repository-integration) | ⚪ | Not implemented — no automated integration across repos; breaking changes in one repo are not caught until consumers update manually. |
| ↳ [7.4 Secrets Management](07-automation-integration.md#secrets-management) | ⚪ | Not implemented — no centralized secrets management; credentials are distributed inconsistently and rotation is manual. |
| ↳ [7.5 CI Observability](07-automation-integration.md#ci-observability) | ⚪ | Not implemented — no aggregated view of CI health; flakiness, duration trends, and failure patterns are invisible at the project level. |
| **[8 Release & Distribution](08-artifact-distribution.md)** | ⚪ | Not implemented — no automated release pipeline; publishing is manual, inconsistent, and not reliably reproducible. |
| ↳ [8.1 Deliverable Types](08-artifact-distribution.md#deliverable-types) | ⚪ | Not implemented — no agreed definition of what constitutes a release artifact per repo type. |
| ↳ [8.2 Distribution Channels](08-artifact-distribution.md#distribution-channels) | ⚪ | Not implemented — no standardized publishing targets; consumers have no reliable place to find released artifacts. |
| ↳ [8.3 Release Metadata](08-artifact-distribution.md#release-metadata) | ⚪ | Not implemented — no consistent versioning or changelog generation; consumers cannot determine what changed between releases. |
| ↳ [8.4 Consumer Access](08-artifact-distribution.md#consumer-access) | ⚪ | Not implemented — no documented or automated path for consumers to adopt a new release. |
| ↳ [8.5 Post-Release Communication & Response](08-artifact-distribution.md#post-release-communication-response) | ⚪ | Not implemented — no process for announcing releases or responding to post-release issues reported by consumers. |
| **[9 Documentation & Traceability](09-documentation-infrastructure.md)** | 🟠 | Documentation tooling is deployed but inconsistently adopted — the published landscape is incomplete and some repos are effectively undocumented. |
| ↳ [9.1 Authoring & Tooling](09-documentation-infrastructure.md#authoring-tooling) | 🟡 | Tooling works but adoption is uneven — some repos use older versions or skip the shared stack, producing an inconsistent documentation experience. |
| ↳ [9.2 Build, Validation & Publishing](09-documentation-infrastructure.md#build-validation-publishing) | 🟡 | Build and publish pipeline is partially automated but validation is incomplete — broken links or missing content can reach the published site. |
| ↳ [9.3 Cross-Repository Documentation Integration](09-documentation-infrastructure.md#cross-repository-documentation-integration) | 🔴 | No mechanism pulls documentation from module repos into the main site — contributors must navigate multiple separate locations to get a complete picture. |
| ↳ [9.4 Engineering Documentation & Traceability](09-documentation-infrastructure.md#engineering-documentation-traceability) | 🟠 | Traceability tooling is deployed but coverage is incomplete — requirement-to-test links are missing across large parts of the codebase. |
| **[10 Infrastructure Operations](10-infrastructure-operations.md)** | ⚪ | Not implemented — no documented ownership, runbooks, or operational processes for the shared infrastructure. |
| ↳ [10.1 CI Runner Operations](10-infrastructure-operations.md#ci-runner-operations) | ⚪ | Not implemented — no runbooks or on-call process for runner outages; recovery is ad hoc. |
| ↳ [10.2 Infrastructure Monitoring](10-infrastructure-operations.md#infrastructure-monitoring) | ⚪ | Not implemented — no monitoring or alerting on infrastructure health; failures are noticed only when contributors report CI problems. |
| ↳ [10.3 Infrastructure Maintenance](10-infrastructure-operations.md#infrastructure-maintenance) | ⚪ | Not implemented — no scheduled maintenance cadence; updates and security patches are applied reactively. |
| ↳ [10.4 Infrastructure Governance](10-infrastructure-operations.md#infrastructure-governance) | ⚪ | Not implemented — no defined ownership model or decision process for infrastructure changes affecting all repos. |

<!-- END GENERATED CHAPTER MAP -->

:::{toctree}
:maxdepth: 1
:hidden:

01-source-code-infrastructure
02-developer-environment
03-build-infrastructure
04-testing-infrastructure
05-static-analysis-infrastructure
06-compliance-infrastructure
07-automation-integration
08-artifact-distribution
09-documentation-infrastructure
10-infrastructure-operations
decisions
:::

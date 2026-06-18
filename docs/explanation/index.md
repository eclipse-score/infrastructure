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
| **[1 Source Code Infrastructure](01-source-code-infrastructure.md)** | 🟠 | Teams can deliver, but inconsistent standards create avoidable delays and make portfolio oversight harder. |
| ↳ [1.1 Hosting & Organization](01-source-code-infrastructure.md#hosting-organization) | 🟡 | Repositories are harder to find and understand, which slows onboarding and cross-team collaboration. |
| ↳ [1.2 Repository Provisioning & Lifecycle](01-source-code-infrastructure.md#repository-provisioning-lifecycle) | 🟡 | Ownership is unclear for create/archive/delete decisions, increasing governance and audit risk. |
| ↳ [1.3 Repository Policy Management](01-source-code-infrastructure.md#repository-policy-management) | 🔴 | Different repositories follow different protection levels, increasing security exposure and review overhead. |
| ↳ [1.4 Repository Standards](01-source-code-infrastructure.md#repository-standards) | 🟠 | Without measurable conformance, standards are hard to enforce and improvement progress is hard to track. |
| **[2 Developer Environment](02-developer-environment.md)** | 🟡 | Most contributors can work effectively, but setup differences still reduce productivity and predictability. |
| ↳ [2.1 Central Devcontainer](02-developer-environment.md#central-devcontainer) | 🟡 | The shared environment helps onboarding, but uneven adoption means teams still lose time on local fixes. |
| ↳ [2.2 Local Auxiliary Tooling](02-developer-environment.md#local-auxiliary-tooling) | 🟡 | Inconsistent local checks create rework when code moves from laptop to CI. |
| **[3 Build & Dependencies](03-build-infrastructure.md)** | 🟠 | Build capabilities are strong, but missing shared policies increase delivery risk and coordination cost. |
| ↳ [3.1 Build System](03-build-infrastructure.md#build-system) | 🟢 | A common build foundation reduces integration friction and supports predictable delivery. |
| ↳ [3.2 Dependency Management](03-build-infrastructure.md#dependency-management) | 🟡 | Inconsistent dependency decisions raise maintenance effort and can introduce compliance surprises late. |
| ↳ [3.3 Toolchain Management](03-build-infrastructure.md#toolchain-management) | 🟠 | Progress exists, but uneven rollout means teams do not get the same reliability or support level. |
| ↳ [3.4 Build Reproducibility & Evidence](03-build-infrastructure.md#build-reproducibility-evidence) | 🔴 | Missing reproducibility evidence limits confidence in releases and weakens audit readiness. |
| ↳ [3.5 Build Execution Infrastructure](03-build-infrastructure.md#build-execution-infrastructure) | 🔴 | No shared scale-out build infrastructure means slower pipelines and longer feedback loops. |
| **[4 Testing](04-testing-infrastructure.md)** | 🟠 | Good testing exists, but fragmentation limits leadership visibility into overall product quality. |
| ↳ [4.1 Test Framework Integration](04-testing-infrastructure.md#test-framework-integration) | 🟡 | Teams use similar tools, but inconsistency still causes duplicated effort and uneven test quality. |
| ↳ [4.2 Test Execution & Dynamic Analysis](04-testing-infrastructure.md#test-execution-dynamic-analysis) | 🟠 | Advanced test practices are not consistently adopted, leaving quality risk concentrated in some areas. |
| ↳ [4.4 Test Reporting](04-testing-infrastructure.md#test-reporting) | 🟠 | Reporting is scattered, making it hard to get one management view of risk and trend direction. |
| **[5 Code Analysis Infrastructure](05-static-analysis-infrastructure.md)** | 🔴 | Quality controls are not standardized, so risk detection depends too much on individual repositories. |
| ↳ [5.1 Tooling Baseline](05-static-analysis-infrastructure.md#tooling-baseline) | 🔴 | No shared baseline means coverage gaps and inconsistent quality expectations across teams. |
| ↳ [5.2 Shared Rule Configuration](05-static-analysis-infrastructure.md#shared-rule-configuration) | 🔴 | Without common rules, results are harder to compare and governance decisions are slower. |
| ↳ [5.3 Incremental Adoption](05-static-analysis-infrastructure.md#incremental-adoption) | 🔴 | No rollout path means improvements are harder to scale across the portfolio. |
| ↳ [5.4 Security Scanning](05-static-analysis-infrastructure.md#security-scanning) | 🟠 | Security checks exist, but inconsistent gates can let important findings slip through. |
| **[6 Compliance & Dependency Analysis](06-compliance-infrastructure.md)** | 🔴 | Compliance is not yet reliable end to end, creating audit and release-readiness risk. |
| ↳ [6.1 File-Level Licensing](06-compliance-infrastructure.md#file-level-licensing) | 🔴 | License labeling is incomplete, increasing legal-review effort and uncertainty. |
| ↳ [6.2 Dependency Analysis](06-compliance-infrastructure.md#dependency-analysis) | 🔴 | Dependency visibility is partial, so teams may discover compliance issues too late. |
| ↳ [6.3 SBOM Scoping and Compliance Evidence](06-compliance-infrastructure.md#sbom-scoping-and-compliance-evidence) | 🔴 | Unclear scope rules make compliance outputs hard to trust and hard to compare. |
| ↳ [6.4 License Checks and Compliance](06-compliance-infrastructure.md#license-checks-and-compliance) | 🔴 | No shared license decision baseline increases release risk and slows approvals. |
| ↳ [6.5 Monitoring and Governance](06-compliance-infrastructure.md#monitoring-and-governance) | 🔴 | Ongoing compliance health is not actively managed, so issues can remain hidden longer. |
| **[7 Automation Infrastructure & Continuous Integration (CI)](07-automation-integration.md)** | 🔴 | Automation is improving, but inconsistent workflow coverage still creates uneven delivery performance. |
| ↳ [7.1 Runners](07-automation-integration.md#runners) | 🟠 | Capacity and reliability limits on runners continue to delay critical feedback. |
| ↳ [7.2 Reusable Workflows](07-automation-integration.md#reusable-workflows) | 🔴 | Reuse is incomplete, so teams still duplicate CI logic and carry higher maintenance cost. |
| ↳ [7.3 Cross-Repository Integration](07-automation-integration.md#cross-repository-integration) | 🔴 | Cross-repository breakages can be detected too late, increasing integration and release risk. |
| ↳ [7.4 Secrets Management](07-automation-integration.md#secrets-management) | 🔴 | Secret handling is not uniformly governed, increasing security and compliance exposure. |
| ↳ [7.5 CI Observability](07-automation-integration.md#ci-observability) | 🔴 | Leadership lacks a single CI health view, making prioritization and investment decisions harder. |
| **[8 Release & Distribution](08-artifact-distribution.md)** | 🟠 | Release practices exist, but inconsistent patterns reduce speed, clarity, and consumer confidence. |
| ↳ [8.1 Deliverable Types](08-artifact-distribution.md#deliverable-types) | 🟠 | No common release package model makes planning and consumer communication harder. |
| ↳ [8.2 Distribution Channels](08-artifact-distribution.md#distribution-channels) | 🟠 | Channel strategy is unclear, so consumers face inconsistent access across deliverables. |
| ↳ [8.3 Release Metadata](08-artifact-distribution.md#release-metadata) | 🟠 | Inconsistent metadata reduces transparency about what changed and how safe it is to adopt. |
| ↳ [8.4 Consumer Access](08-artifact-distribution.md#consumer-access) | ⚪ | Consumer adoption paths are not clearly defined, slowing uptake and support. |
| ↳ [8.5 Post-Release Communication & Response](08-artifact-distribution.md#post-release-communication-response) | ⚪ | No shared advisory model means slower, less consistent communication when issues arise. |
| **[9 Documentation & Traceability](09-documentation-infrastructure.md)** | 🟠 | Documentation is improving, but fragmentation limits trust and decision support at program level. |
| ↳ [9.1 Authoring & Tooling](09-documentation-infrastructure.md#authoring-tooling) | 🟡 | Different authoring setups increase maintenance effort and dilute documentation quality. |
| ↳ [9.2 Build, Validation & Publishing](09-documentation-infrastructure.md#build-validation-publishing) | 🟡 | Publishing works, but inconsistent validation can let quality issues reach stakeholders. |
| ↳ [9.3 Cross-Repository Documentation Integration](09-documentation-infrastructure.md#cross-repository-documentation-integration) | 🔴 | No integrated navigation makes it difficult to understand the full system picture quickly. |
| ↳ [9.4 Engineering Documentation & Traceability](09-documentation-infrastructure.md#engineering-documentation-traceability) | 🟠 | Traceability exists in parts, but not yet enough for consistent impact and change analysis at scale. |
| **[10 Infrastructure Operations](10-infrastructure-operations.md)** | ⚪ | Operations are mostly reactive, increasing outage risk and recovery uncertainty. |
| ↳ [10.1 CI Runner Operations](10-infrastructure-operations.md#ci-runner-operations) | ⚪ | Limited operational ownership and transparency increase service continuity risk. |
| ↳ [10.2 Infrastructure Monitoring](10-infrastructure-operations.md#infrastructure-monitoring) | ⚪ | Without shared monitoring, systemic problems are detected later and resolved slower. |
| ↳ [10.3 Infrastructure Maintenance](10-infrastructure-operations.md#infrastructure-maintenance) | ⚪ | Maintenance is not planned consistently, increasing technical debt and surprise work. |
| ↳ [10.4 Infrastructure Governance](10-infrastructure-operations.md#infrastructure-governance) | ⚪ | Missing governance structure makes cross-repository decisions slower and less predictable. |
| **[11 Reference Integration](11-reference-integration.md)** | 🟠 | The workspace exists and DR-008 is settled, but the validation pipeline and evidence model are not built, and the release process is undefined. |
| ↳ [11.1 Integration Workspace](11-reference-integration.md#integration-workspace) | 🟡 | Multi-module workspace is functional but missing QNX8 aarch64, inconsistent showcase coverage, and an outdated README. |
| ↳ [11.2 Known-Good Promotion](11-reference-integration.md#known-good-promotion) | 🟠 | Revision pinning works, but the release process is not defined in DR-008, so the promotion gate has no criteria. |
| ↳ [11.3 Validation Pipeline](11-reference-integration.md#validation-pipeline) | 🔴 | The DR-008 Option 4 two-stage pipeline is not implemented — no dependency resolution handoff, no module-scoped validation orchestration. |
| ↳ [11.4 Integrated Evidence](11-reference-integration.md#integrated-evidence) | 🔴 | No evidence schema, no release gate definition, unreliable coverage, and missing traceability properties in Rust test reports. |
| ↳ [11.5 Operating Model](11-reference-integration.md#operating-model) | 🟡 | Workflow restructuring and CI centralization are in progress for v0.8; `cr_checker` and Bazel profiling are pending. |

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
11-reference-integration
decisions
:::

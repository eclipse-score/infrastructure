# Infrastructure Landscape

Architecture, design rationale, and maturity assessment of each S-CORE infrastructure area. These chapters describe what exists, how it works, and what is still missing.

- [1. Source Code Infrastructure](01-source-code-infrastructure.md)
- [2. Developer Environment](02-developer-environment.md)
- [3. Build & Dependencies](03-build-infrastructure.md)
- [4. Testing](04-testing-infrastructure.md)
- [5. Code Analysis Infrastructure](05-static-analysis-infrastructure.md)
- [6. Compliance & Dependency Analysis](06-compliance-infrastructure.md)
- [7. Automation & CI](07-automation-integration.md)
- [8. Release & Distribution](08-artifact-distribution.md)
- [9. Documentation & Traceability](09-documentation-infrastructure.md)
- [10. Infrastructure Operations](10-infrastructure-operations.md)
- [Infrastructure Design Decisions](decisions.md)

## Status Legend

- 🟢 Implemented and effective
- 🟡 Partially implemented / needs improvement
- 🟠 Implemented but problematic or insufficient
- 🔴 Not started
- ⚪ Unknown / not yet assessed

## Chapter Map

<!-- BEGIN GENERATED CHAPTER MAP -->
<p class="chapter-map-note">This chapter map is generated from the `#` and `##` headings in the numbered chapter files. Click any chapter or section box to open it.</p>

```{mermaid}
mindmap
  root((S-CORE Infrastructure))
    node_001["`1 Source Code
Infrastructure 🟠`"]
      node_002["`1.1 Hosting & Organization
⚪`"]
      node_003["`1.2 Repository
Provisioning & Lifecycle 🟡`"]
      node_004["`1.3 Repository Policy
Management 🔴`"]
      node_005["1.4 Repository Standards 🟠"]
    node_006["`2 Developer Environment
🟡`"]
      node_007["2.1 Central Devcontainer 🟠"]
      node_008["`2.2 Local Auxiliary
Tooling 🟡`"]
    node_009["3 Build & Dependencies ⚪"]
      node_010["3.1 Build System ⚪"]
      node_011["`3.2 Dependency Management
⚪`"]
      node_012["3.3 Toolchain Management ⚪"]
      node_013["`3.4 Build Reproducibility
& Evidence ⚪`"]
      node_014["`3.5 Build Execution
Infrastructure ⚪`"]
    node_015["4 Testing 🟠"]
      node_016["`4.1 Test Framework
Integration 🟠`"]
      node_017["4.2 Test Traceability 🟠"]
      node_018["`4.3 Test Execution &
Dynamic Analysis 🟠`"]
      node_019["4.4 Test Reporting 🟠"]
    node_020["`5 Code Analysis
Infrastructure ⚪`"]
      node_021["5.1 Tooling Baseline ⚪"]
      node_022["`5.2 Shared Rule
Configuration ⚪`"]
      node_023["5.3 Execution Model ⚪"]
      node_024["5.4 Security Scanning 🟠"]
      node_025["`5.5 Results and Governance
⚪`"]
    node_026["`6 Compliance &
Dependency Analysis ⚪`"]
      node_027["6.1 File-Level Licensing ⚪"]
      node_028["6.2 Dependency Analysis ⚪"]
      node_029["`6.3 SBOM Scoping and
Compliance Evidence ⚪`"]
      node_030["`6.4 License Checks and
Compliance ⚪`"]
      node_031["`6.5 Monitoring and
Governance ⚪`"]
    node_032["`7 Automation
Infrastructure &
Continuous Integration
(CI) ⚪`"]
      node_033["7.1 Runners 🟠"]
      node_034["7.2 Reusable Workflows ⚪"]
      node_035["`7.3 Cross-Repository
Integration ⚪`"]
      node_036["7.4 Secrets Management ⚪"]
      node_037["7.5 CI Observability ⚪"]
    node_038["`8 Release & Distribution
⚪`"]
      node_039["8.1 Deliverable Types ⚪"]
      node_040["`8.2 Distribution Channels
⚪`"]
      node_041["8.3 Release Metadata ⚪"]
      node_042["8.4 Consumer Access ⚪"]
      node_043["`8.5 Post-Release
Communication & Response ⚪`"]
    node_044["`9 Documentation &
Traceability 🟠`"]
      node_045["9.1 Authoring & Tooling 🟡"]
      node_046["`9.2 Build, Validation &
Publishing 🟡`"]
      node_047["`9.3 Cross-Repository
Documentation Integration
🔴`"]
      node_048["`9.4 Engineering
Documentation &
Traceability 🟠`"]
    node_049["`10 Infrastructure
Operations ⚪`"]
      node_050["`10.1 CI Runner Operations
⚪`"]
      node_051["`10.2 Infrastructure
Monitoring ⚪`"]
      node_052["`10.3 Infrastructure
Maintenance ⚪`"]
      node_053["`10.4 Infrastructure
Governance ⚪`"]
```
<script type="application/json" class="chapter-map-links-data">
[
  {
    "id": "node_001",
    "kind": "chapter",
    "href": "01-source-code-infrastructure/",
    "title": "1 Source Code Infrastructure",
    "match_texts": [
      "1 Source Code Infrastructure 🟠",
      "1 Source Code Infrastructure"
    ]
  },
  {
    "id": "node_002",
    "kind": "section",
    "href": "01-source-code-infrastructure/#hosting-organization",
    "title": "1.1 Hosting & Organization",
    "match_texts": [
      "1.1 Hosting & Organization ⚪",
      "1.1 Hosting & Organization"
    ]
  },
  {
    "id": "node_003",
    "kind": "section",
    "href": "01-source-code-infrastructure/#repository-provisioning-lifecycle",
    "title": "1.2 Repository Provisioning & Lifecycle",
    "match_texts": [
      "1.2 Repository Provisioning & Lifecycle 🟡",
      "1.2 Repository Provisioning & Lifecycle"
    ]
  },
  {
    "id": "node_004",
    "kind": "section",
    "href": "01-source-code-infrastructure/#repository-policy-management",
    "title": "1.3 Repository Policy Management",
    "match_texts": [
      "1.3 Repository Policy Management 🔴",
      "1.3 Repository Policy Management"
    ]
  },
  {
    "id": "node_005",
    "kind": "section",
    "href": "01-source-code-infrastructure/#repository-standards",
    "title": "1.4 Repository Standards",
    "match_texts": [
      "1.4 Repository Standards 🟠",
      "1.4 Repository Standards"
    ]
  },
  {
    "id": "node_006",
    "kind": "chapter",
    "href": "02-developer-environment/",
    "title": "2 Developer Environment",
    "match_texts": [
      "2 Developer Environment 🟡",
      "2 Developer Environment"
    ]
  },
  {
    "id": "node_007",
    "kind": "section",
    "href": "02-developer-environment/#central-devcontainer",
    "title": "2.1 Central Devcontainer",
    "match_texts": [
      "2.1 Central Devcontainer 🟠",
      "2.1 Central Devcontainer"
    ]
  },
  {
    "id": "node_008",
    "kind": "section",
    "href": "02-developer-environment/#local-auxiliary-tooling",
    "title": "2.2 Local Auxiliary Tooling",
    "match_texts": [
      "2.2 Local Auxiliary Tooling 🟡",
      "2.2 Local Auxiliary Tooling"
    ]
  },
  {
    "id": "node_009",
    "kind": "chapter",
    "href": "03-build-infrastructure/",
    "title": "3 Build & Dependencies",
    "match_texts": [
      "3 Build & Dependencies ⚪",
      "3 Build & Dependencies"
    ]
  },
  {
    "id": "node_010",
    "kind": "section",
    "href": "03-build-infrastructure/#build-system",
    "title": "3.1 Build System",
    "match_texts": [
      "3.1 Build System ⚪",
      "3.1 Build System"
    ]
  },
  {
    "id": "node_011",
    "kind": "section",
    "href": "03-build-infrastructure/#dependency-management",
    "title": "3.2 Dependency Management",
    "match_texts": [
      "3.2 Dependency Management ⚪",
      "3.2 Dependency Management"
    ]
  },
  {
    "id": "node_012",
    "kind": "section",
    "href": "03-build-infrastructure/#toolchain-management",
    "title": "3.3 Toolchain Management",
    "match_texts": [
      "3.3 Toolchain Management ⚪",
      "3.3 Toolchain Management"
    ]
  },
  {
    "id": "node_013",
    "kind": "section",
    "href": "03-build-infrastructure/#build-reproducibility-evidence",
    "title": "3.4 Build Reproducibility & Evidence",
    "match_texts": [
      "3.4 Build Reproducibility & Evidence ⚪",
      "3.4 Build Reproducibility & Evidence"
    ]
  },
  {
    "id": "node_014",
    "kind": "section",
    "href": "03-build-infrastructure/#build-execution-infrastructure",
    "title": "3.5 Build Execution Infrastructure",
    "match_texts": [
      "3.5 Build Execution Infrastructure ⚪",
      "3.5 Build Execution Infrastructure"
    ]
  },
  {
    "id": "node_015",
    "kind": "chapter",
    "href": "04-testing-infrastructure/",
    "title": "4 Testing",
    "match_texts": [
      "4 Testing 🟠",
      "4 Testing"
    ]
  },
  {
    "id": "node_016",
    "kind": "section",
    "href": "04-testing-infrastructure/#test-framework-integration",
    "title": "4.1 Test Framework Integration",
    "match_texts": [
      "4.1 Test Framework Integration 🟠",
      "4.1 Test Framework Integration"
    ]
  },
  {
    "id": "node_017",
    "kind": "section",
    "href": "04-testing-infrastructure/#test-traceability",
    "title": "4.2 Test Traceability",
    "match_texts": [
      "4.2 Test Traceability 🟠",
      "4.2 Test Traceability"
    ]
  },
  {
    "id": "node_018",
    "kind": "section",
    "href": "04-testing-infrastructure/#test-execution-dynamic-analysis",
    "title": "4.3 Test Execution & Dynamic Analysis",
    "match_texts": [
      "4.3 Test Execution & Dynamic Analysis 🟠",
      "4.3 Test Execution & Dynamic Analysis"
    ]
  },
  {
    "id": "node_019",
    "kind": "section",
    "href": "04-testing-infrastructure/#test-reporting",
    "title": "4.4 Test Reporting",
    "match_texts": [
      "4.4 Test Reporting 🟠",
      "4.4 Test Reporting"
    ]
  },
  {
    "id": "node_020",
    "kind": "chapter",
    "href": "05-static-analysis-infrastructure/",
    "title": "5 Code Analysis Infrastructure",
    "match_texts": [
      "5 Code Analysis Infrastructure ⚪",
      "5 Code Analysis Infrastructure"
    ]
  },
  {
    "id": "node_021",
    "kind": "section",
    "href": "05-static-analysis-infrastructure/#tooling-baseline",
    "title": "5.1 Tooling Baseline",
    "match_texts": [
      "5.1 Tooling Baseline ⚪",
      "5.1 Tooling Baseline"
    ]
  },
  {
    "id": "node_022",
    "kind": "section",
    "href": "05-static-analysis-infrastructure/#shared-rule-configuration",
    "title": "5.2 Shared Rule Configuration",
    "match_texts": [
      "5.2 Shared Rule Configuration ⚪",
      "5.2 Shared Rule Configuration"
    ]
  },
  {
    "id": "node_023",
    "kind": "section",
    "href": "05-static-analysis-infrastructure/#execution-model",
    "title": "5.3 Execution Model",
    "match_texts": [
      "5.3 Execution Model ⚪",
      "5.3 Execution Model"
    ]
  },
  {
    "id": "node_024",
    "kind": "section",
    "href": "05-static-analysis-infrastructure/#security-scanning",
    "title": "5.4 Security Scanning",
    "match_texts": [
      "5.4 Security Scanning 🟠",
      "5.4 Security Scanning"
    ]
  },
  {
    "id": "node_025",
    "kind": "section",
    "href": "05-static-analysis-infrastructure/#results-and-governance",
    "title": "5.5 Results and Governance",
    "match_texts": [
      "5.5 Results and Governance ⚪",
      "5.5 Results and Governance"
    ]
  },
  {
    "id": "node_026",
    "kind": "chapter",
    "href": "06-compliance-infrastructure/",
    "title": "6 Compliance & Dependency Analysis",
    "match_texts": [
      "6 Compliance & Dependency Analysis ⚪",
      "6 Compliance & Dependency Analysis"
    ]
  },
  {
    "id": "node_027",
    "kind": "section",
    "href": "06-compliance-infrastructure/#file-level-licensing",
    "title": "6.1 File-Level Licensing",
    "match_texts": [
      "6.1 File-Level Licensing ⚪",
      "6.1 File-Level Licensing"
    ]
  },
  {
    "id": "node_028",
    "kind": "section",
    "href": "06-compliance-infrastructure/#dependency-analysis",
    "title": "6.2 Dependency Analysis",
    "match_texts": [
      "6.2 Dependency Analysis ⚪",
      "6.2 Dependency Analysis"
    ]
  },
  {
    "id": "node_029",
    "kind": "section",
    "href": "06-compliance-infrastructure/#sbom-scoping-and-compliance-evidence",
    "title": "6.3 SBOM Scoping and Compliance Evidence",
    "match_texts": [
      "6.3 SBOM Scoping and Compliance Evidence ⚪",
      "6.3 SBOM Scoping and Compliance Evidence"
    ]
  },
  {
    "id": "node_030",
    "kind": "section",
    "href": "06-compliance-infrastructure/#license-checks-and-compliance",
    "title": "6.4 License Checks and Compliance",
    "match_texts": [
      "6.4 License Checks and Compliance ⚪",
      "6.4 License Checks and Compliance"
    ]
  },
  {
    "id": "node_031",
    "kind": "section",
    "href": "06-compliance-infrastructure/#monitoring-and-governance",
    "title": "6.5 Monitoring and Governance",
    "match_texts": [
      "6.5 Monitoring and Governance ⚪",
      "6.5 Monitoring and Governance"
    ]
  },
  {
    "id": "node_032",
    "kind": "chapter",
    "href": "07-automation-integration/",
    "title": "7 Automation Infrastructure & Continuous Integration (CI)",
    "match_texts": [
      "7 Automation Infrastructure & Continuous Integration (CI) ⚪",
      "7 Automation Infrastructure & Continuous Integration (CI)"
    ]
  },
  {
    "id": "node_033",
    "kind": "section",
    "href": "07-automation-integration/#runners",
    "title": "7.1 Runners",
    "match_texts": [
      "7.1 Runners 🟠",
      "7.1 Runners"
    ]
  },
  {
    "id": "node_034",
    "kind": "section",
    "href": "07-automation-integration/#reusable-workflows",
    "title": "7.2 Reusable Workflows",
    "match_texts": [
      "7.2 Reusable Workflows ⚪",
      "7.2 Reusable Workflows"
    ]
  },
  {
    "id": "node_035",
    "kind": "section",
    "href": "07-automation-integration/#cross-repository-integration",
    "title": "7.3 Cross-Repository Integration",
    "match_texts": [
      "7.3 Cross-Repository Integration ⚪",
      "7.3 Cross-Repository Integration"
    ]
  },
  {
    "id": "node_036",
    "kind": "section",
    "href": "07-automation-integration/#secrets-management",
    "title": "7.4 Secrets Management",
    "match_texts": [
      "7.4 Secrets Management ⚪",
      "7.4 Secrets Management"
    ]
  },
  {
    "id": "node_037",
    "kind": "section",
    "href": "07-automation-integration/#ci-observability",
    "title": "7.5 CI Observability",
    "match_texts": [
      "7.5 CI Observability ⚪",
      "7.5 CI Observability"
    ]
  },
  {
    "id": "node_038",
    "kind": "chapter",
    "href": "08-artifact-distribution/",
    "title": "8 Release & Distribution",
    "match_texts": [
      "8 Release & Distribution ⚪",
      "8 Release & Distribution"
    ]
  },
  {
    "id": "node_039",
    "kind": "section",
    "href": "08-artifact-distribution/#deliverable-types",
    "title": "8.1 Deliverable Types",
    "match_texts": [
      "8.1 Deliverable Types ⚪",
      "8.1 Deliverable Types"
    ]
  },
  {
    "id": "node_040",
    "kind": "section",
    "href": "08-artifact-distribution/#distribution-channels",
    "title": "8.2 Distribution Channels",
    "match_texts": [
      "8.2 Distribution Channels ⚪",
      "8.2 Distribution Channels"
    ]
  },
  {
    "id": "node_041",
    "kind": "section",
    "href": "08-artifact-distribution/#release-metadata",
    "title": "8.3 Release Metadata",
    "match_texts": [
      "8.3 Release Metadata ⚪",
      "8.3 Release Metadata"
    ]
  },
  {
    "id": "node_042",
    "kind": "section",
    "href": "08-artifact-distribution/#consumer-access",
    "title": "8.4 Consumer Access",
    "match_texts": [
      "8.4 Consumer Access ⚪",
      "8.4 Consumer Access"
    ]
  },
  {
    "id": "node_043",
    "kind": "section",
    "href": "08-artifact-distribution/#post-release-communication-response",
    "title": "8.5 Post-Release Communication & Response",
    "match_texts": [
      "8.5 Post-Release Communication & Response ⚪",
      "8.5 Post-Release Communication & Response"
    ]
  },
  {
    "id": "node_044",
    "kind": "chapter",
    "href": "09-documentation-infrastructure/",
    "title": "9 Documentation & Traceability",
    "match_texts": [
      "9 Documentation & Traceability 🟠",
      "9 Documentation & Traceability"
    ]
  },
  {
    "id": "node_045",
    "kind": "section",
    "href": "09-documentation-infrastructure/#authoring-tooling",
    "title": "9.1 Authoring & Tooling",
    "match_texts": [
      "9.1 Authoring & Tooling 🟡",
      "9.1 Authoring & Tooling"
    ]
  },
  {
    "id": "node_046",
    "kind": "section",
    "href": "09-documentation-infrastructure/#build-validation-publishing",
    "title": "9.2 Build, Validation & Publishing",
    "match_texts": [
      "9.2 Build, Validation & Publishing 🟡",
      "9.2 Build, Validation & Publishing"
    ]
  },
  {
    "id": "node_047",
    "kind": "section",
    "href": "09-documentation-infrastructure/#cross-repository-documentation-integration",
    "title": "9.3 Cross-Repository Documentation Integration",
    "match_texts": [
      "9.3 Cross-Repository Documentation Integration 🔴",
      "9.3 Cross-Repository Documentation Integration"
    ]
  },
  {
    "id": "node_048",
    "kind": "section",
    "href": "09-documentation-infrastructure/#engineering-documentation-traceability",
    "title": "9.4 Engineering Documentation & Traceability",
    "match_texts": [
      "9.4 Engineering Documentation & Traceability 🟠",
      "9.4 Engineering Documentation & Traceability"
    ]
  },
  {
    "id": "node_049",
    "kind": "chapter",
    "href": "10-infrastructure-operations/",
    "title": "10 Infrastructure Operations",
    "match_texts": [
      "10 Infrastructure Operations ⚪",
      "10 Infrastructure Operations"
    ]
  },
  {
    "id": "node_050",
    "kind": "section",
    "href": "10-infrastructure-operations/#ci-runner-operations",
    "title": "10.1 CI Runner Operations",
    "match_texts": [
      "10.1 CI Runner Operations ⚪",
      "10.1 CI Runner Operations"
    ]
  },
  {
    "id": "node_051",
    "kind": "section",
    "href": "10-infrastructure-operations/#infrastructure-monitoring",
    "title": "10.2 Infrastructure Monitoring",
    "match_texts": [
      "10.2 Infrastructure Monitoring ⚪",
      "10.2 Infrastructure Monitoring"
    ]
  },
  {
    "id": "node_052",
    "kind": "section",
    "href": "10-infrastructure-operations/#infrastructure-maintenance",
    "title": "10.3 Infrastructure Maintenance",
    "match_texts": [
      "10.3 Infrastructure Maintenance ⚪",
      "10.3 Infrastructure Maintenance"
    ]
  },
  {
    "id": "node_053",
    "kind": "section",
    "href": "10-infrastructure-operations/#infrastructure-governance",
    "title": "10.4 Infrastructure Governance",
    "match_texts": [
      "10.4 Infrastructure Governance ⚪",
      "10.4 Infrastructure Governance"
    ]
  }
]
</script>
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

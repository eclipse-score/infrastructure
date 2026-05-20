# S-CORE Infrastructure

<div class="landing-hero">
  <p class="landing-kicker">Developer guide and infrastructure reference for the S-CORE ecosystem</p>
  <h2>Build, test, and ship with S-CORE infrastructure.</h2>
  <p class="landing-lead">
    Practical guides for day-to-day development — setting up your environment, building with Bazel,
    running tests, enforcing code quality, and publishing modules. Plus the full infrastructure landscape
    assessment for context on how the pieces fit together.
  </p>
</div>

## Quick Links

<div class="landing-quick-links">

  <p class="landing-section-label">Developer Guides</p>

  <div class="landing-grid landing-grid-3">
    <a class="landing-card-link" href="guide/quick-reference/">
      <p class="landing-link-title">Quick Reference</p>
      <p class="landing-link-desc">All key repositories, commands, and links on one page.</p>
    </a>
    <a class="landing-card-link" href="guide/getting-started/">
      <p class="landing-link-title">Getting Started</p>
      <p class="landing-link-desc">Step-by-step setup for new contributors.</p>
    </a>
    <a class="landing-card-link" href="guide/building/">
      <p class="landing-link-title">Building with Bazel</p>
      <p class="landing-link-desc">Registry, dependencies, toolchains, and lock files.</p>
    </a>
    <a class="landing-card-link" href="guide/testing/">
      <p class="landing-link-title">Testing</p>
      <p class="landing-link-desc">Test frameworks, coverage, and sanitizers.</p>
    </a>
    <a class="landing-card-link" href="guide/code-quality/">
      <p class="landing-link-title">Code Quality</p>
      <p class="landing-link-desc">Pre-commit hooks, policies, and license headers.</p>
    </a>
    <a class="landing-card-link" href="guide/publishing/">
      <p class="landing-link-title">Publishing Modules</p>
      <p class="landing-link-desc">Release, registry, and versioning workflow.</p>
    </a>
    <a class="landing-card-link" href="guide/writing-docs/">
      <p class="landing-link-title">Writing Documentation</p>
      <p class="landing-link-desc">MkDocs toolchain, preview, and style guide.</p>
    </a>
  </div>

  <p class="landing-section-label">Infrastructure Team</p>

  <div class="landing-grid landing-grid-2">
    <a class="landing-card-link" href="https://github.com/orgs/eclipse-score/discussions/236" target="_blank" rel="noopener">
      <p class="landing-link-title">Meeting Minutes</p>
      <p class="landing-link-desc">Infrastructure team meeting notes on GitHub Discussions.</p>
    </a>
    <a class="landing-card-link" href="https://sdvworkinggroup.slack.com/archives/C0894QGRZDM" target="_blank" rel="noopener">
      <p class="landing-link-title">Slack: #score-infrastructure</p>
      <p class="landing-link-desc">Main channel for infrastructure team discussion.</p>
    </a>
    <a class="landing-card-link" href="https://sdvworkinggroup.slack.com/archives/C08RDRKH5FE" target="_blank" rel="noopener">
      <p class="landing-link-title">Slack: #score-infrastructure-review-requests</p>
      <p class="landing-link-desc">Drop PR links here for review — no comments, just links.</p>
    </a>
    <a class="landing-card-link" href="https://eclipse-score.github.io/.github/" target="_blank" rel="noopener">
      <p class="landing-link-title">Repository Overview</p>
      <p class="landing-link-desc">Cross-repo metrics and status across all eclipse-score repositories.</p>
    </a>
  </div>

  <p class="landing-section-label">S-CORE Project</p>

  <div class="landing-grid landing-grid-2">
    <a class="landing-card-link" href="https://eclipse.dev/score/" target="_blank" rel="noopener">
      <p class="landing-link-title">S-CORE Website</p>
      <p class="landing-link-desc">The main Eclipse S-CORE project website — "Open by Choice. Safe by Design."</p>
    </a>
    <a class="landing-card-link" href="https://eclipse-score.github.io/score/main/handbook" target="_blank" rel="noopener">
      <p class="landing-link-title">S-CORE Handbook</p>
      <p class="landing-link-desc">Technical handbook — processes, tooling, and contribution model.</p>
    </a>
  </div>

</div>

## Chapter Map

<!-- BEGIN GENERATED CHAPTER MAP -->
<p class="chapter-map-note">This chapter map is generated from the `#` and `##` headings in the numbered chapter files. Click any chapter or section box to open it.</p>

```mermaid
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
    node_015["4 Testing ⚪"]
      node_016["`4.1 Test Framework
Integration ⚪`"]
      node_017["4.2 Test Traceability ⚪"]
      node_018["`4.3 Test Execution &
Dynamic Analysis ⚪`"]
      node_019["4.4 Test Reporting ⚪"]
    node_020["`5 Code Analysis
Infrastructure ⚪`"]
      node_021["5.1 Tooling Baseline ⚪"]
      node_022["`5.2 Shared Rule
Configuration ⚪`"]
      node_023["5.3 Execution Model ⚪"]
      node_024["5.4 Security Scanning ⚪"]
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
Traceability ⚪`"]
      node_045["9.1 Authoring & Tooling ⚪"]
      node_046["`9.2 Build, Validation &
Publishing ⚪`"]
      node_047["`9.3 Cross-Repository
Documentation Integration
⚪`"]
      node_048["`9.4 Engineering
Documentation &
Traceability ⚪`"]
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
    "href": "landscape/01-source-code-infrastructure/",
    "title": "1 Source Code Infrastructure",
    "match_texts": [
      "1 Source Code Infrastructure 🟠",
      "1 Source Code Infrastructure"
    ]
  },
  {
    "id": "node_002",
    "kind": "section",
    "href": "landscape/01-source-code-infrastructure/#11-hosting-organization",
    "title": "1.1 Hosting & Organization",
    "match_texts": [
      "1.1 Hosting & Organization ⚪",
      "1.1 Hosting & Organization"
    ]
  },
  {
    "id": "node_003",
    "kind": "section",
    "href": "landscape/01-source-code-infrastructure/#12-repository-provisioning-lifecycle",
    "title": "1.2 Repository Provisioning & Lifecycle",
    "match_texts": [
      "1.2 Repository Provisioning & Lifecycle 🟡",
      "1.2 Repository Provisioning & Lifecycle"
    ]
  },
  {
    "id": "node_004",
    "kind": "section",
    "href": "landscape/01-source-code-infrastructure/#13-repository-policy-management",
    "title": "1.3 Repository Policy Management",
    "match_texts": [
      "1.3 Repository Policy Management 🔴",
      "1.3 Repository Policy Management"
    ]
  },
  {
    "id": "node_005",
    "kind": "section",
    "href": "landscape/01-source-code-infrastructure/#14-repository-standards",
    "title": "1.4 Repository Standards",
    "match_texts": [
      "1.4 Repository Standards 🟠",
      "1.4 Repository Standards"
    ]
  },
  {
    "id": "node_006",
    "kind": "chapter",
    "href": "landscape/02-developer-environment/",
    "title": "2 Developer Environment",
    "match_texts": [
      "2 Developer Environment 🟡",
      "2 Developer Environment"
    ]
  },
  {
    "id": "node_007",
    "kind": "section",
    "href": "landscape/02-developer-environment/#21-central-devcontainer",
    "title": "2.1 Central Devcontainer",
    "match_texts": [
      "2.1 Central Devcontainer 🟠",
      "2.1 Central Devcontainer"
    ]
  },
  {
    "id": "node_008",
    "kind": "section",
    "href": "landscape/02-developer-environment/#22-local-auxiliary-tooling",
    "title": "2.2 Local Auxiliary Tooling",
    "match_texts": [
      "2.2 Local Auxiliary Tooling 🟡",
      "2.2 Local Auxiliary Tooling"
    ]
  },
  {
    "id": "node_009",
    "kind": "chapter",
    "href": "landscape/03-build-infrastructure/",
    "title": "3 Build & Dependencies",
    "match_texts": [
      "3 Build & Dependencies ⚪",
      "3 Build & Dependencies"
    ]
  },
  {
    "id": "node_010",
    "kind": "section",
    "href": "landscape/03-build-infrastructure/#31-build-system",
    "title": "3.1 Build System",
    "match_texts": [
      "3.1 Build System ⚪",
      "3.1 Build System"
    ]
  },
  {
    "id": "node_011",
    "kind": "section",
    "href": "landscape/03-build-infrastructure/#32-dependency-management",
    "title": "3.2 Dependency Management",
    "match_texts": [
      "3.2 Dependency Management ⚪",
      "3.2 Dependency Management"
    ]
  },
  {
    "id": "node_012",
    "kind": "section",
    "href": "landscape/03-build-infrastructure/#33-toolchain-management",
    "title": "3.3 Toolchain Management",
    "match_texts": [
      "3.3 Toolchain Management ⚪",
      "3.3 Toolchain Management"
    ]
  },
  {
    "id": "node_013",
    "kind": "section",
    "href": "landscape/03-build-infrastructure/#34-build-reproducibility-evidence",
    "title": "3.4 Build Reproducibility & Evidence",
    "match_texts": [
      "3.4 Build Reproducibility & Evidence ⚪",
      "3.4 Build Reproducibility & Evidence"
    ]
  },
  {
    "id": "node_014",
    "kind": "section",
    "href": "landscape/03-build-infrastructure/#35-build-execution-infrastructure",
    "title": "3.5 Build Execution Infrastructure",
    "match_texts": [
      "3.5 Build Execution Infrastructure ⚪",
      "3.5 Build Execution Infrastructure"
    ]
  },
  {
    "id": "node_015",
    "kind": "chapter",
    "href": "landscape/04-testing-infrastructure/",
    "title": "4 Testing",
    "match_texts": [
      "4 Testing ⚪",
      "4 Testing"
    ]
  },
  {
    "id": "node_016",
    "kind": "section",
    "href": "landscape/04-testing-infrastructure/#41-test-framework-integration",
    "title": "4.1 Test Framework Integration",
    "match_texts": [
      "4.1 Test Framework Integration ⚪",
      "4.1 Test Framework Integration"
    ]
  },
  {
    "id": "node_017",
    "kind": "section",
    "href": "landscape/04-testing-infrastructure/#42-test-traceability",
    "title": "4.2 Test Traceability",
    "match_texts": [
      "4.2 Test Traceability ⚪",
      "4.2 Test Traceability"
    ]
  },
  {
    "id": "node_018",
    "kind": "section",
    "href": "landscape/04-testing-infrastructure/#43-test-execution-dynamic-analysis",
    "title": "4.3 Test Execution & Dynamic Analysis",
    "match_texts": [
      "4.3 Test Execution & Dynamic Analysis ⚪",
      "4.3 Test Execution & Dynamic Analysis"
    ]
  },
  {
    "id": "node_019",
    "kind": "section",
    "href": "landscape/04-testing-infrastructure/#44-test-reporting",
    "title": "4.4 Test Reporting",
    "match_texts": [
      "4.4 Test Reporting ⚪",
      "4.4 Test Reporting"
    ]
  },
  {
    "id": "node_020",
    "kind": "chapter",
    "href": "landscape/05-static-analysis-infrastructure/",
    "title": "5 Code Analysis Infrastructure",
    "match_texts": [
      "5 Code Analysis Infrastructure ⚪",
      "5 Code Analysis Infrastructure"
    ]
  },
  {
    "id": "node_021",
    "kind": "section",
    "href": "landscape/05-static-analysis-infrastructure/#51-tooling-baseline",
    "title": "5.1 Tooling Baseline",
    "match_texts": [
      "5.1 Tooling Baseline ⚪",
      "5.1 Tooling Baseline"
    ]
  },
  {
    "id": "node_022",
    "kind": "section",
    "href": "landscape/05-static-analysis-infrastructure/#52-shared-rule-configuration",
    "title": "5.2 Shared Rule Configuration",
    "match_texts": [
      "5.2 Shared Rule Configuration ⚪",
      "5.2 Shared Rule Configuration"
    ]
  },
  {
    "id": "node_023",
    "kind": "section",
    "href": "landscape/05-static-analysis-infrastructure/#53-execution-model",
    "title": "5.3 Execution Model",
    "match_texts": [
      "5.3 Execution Model ⚪",
      "5.3 Execution Model"
    ]
  },
  {
    "id": "node_024",
    "kind": "section",
    "href": "landscape/05-static-analysis-infrastructure/#54-security-scanning",
    "title": "5.4 Security Scanning",
    "match_texts": [
      "5.4 Security Scanning ⚪",
      "5.4 Security Scanning"
    ]
  },
  {
    "id": "node_025",
    "kind": "section",
    "href": "landscape/05-static-analysis-infrastructure/#55-results-and-governance",
    "title": "5.5 Results and Governance",
    "match_texts": [
      "5.5 Results and Governance ⚪",
      "5.5 Results and Governance"
    ]
  },
  {
    "id": "node_026",
    "kind": "chapter",
    "href": "landscape/06-compliance-infrastructure/",
    "title": "6 Compliance & Dependency Analysis",
    "match_texts": [
      "6 Compliance & Dependency Analysis ⚪",
      "6 Compliance & Dependency Analysis"
    ]
  },
  {
    "id": "node_027",
    "kind": "section",
    "href": "landscape/06-compliance-infrastructure/#61-file-level-licensing",
    "title": "6.1 File-Level Licensing",
    "match_texts": [
      "6.1 File-Level Licensing ⚪",
      "6.1 File-Level Licensing"
    ]
  },
  {
    "id": "node_028",
    "kind": "section",
    "href": "landscape/06-compliance-infrastructure/#62-dependency-analysis",
    "title": "6.2 Dependency Analysis",
    "match_texts": [
      "6.2 Dependency Analysis ⚪",
      "6.2 Dependency Analysis"
    ]
  },
  {
    "id": "node_029",
    "kind": "section",
    "href": "landscape/06-compliance-infrastructure/#63-sbom-scoping-and-compliance-evidence",
    "title": "6.3 SBOM Scoping and Compliance Evidence",
    "match_texts": [
      "6.3 SBOM Scoping and Compliance Evidence ⚪",
      "6.3 SBOM Scoping and Compliance Evidence"
    ]
  },
  {
    "id": "node_030",
    "kind": "section",
    "href": "landscape/06-compliance-infrastructure/#64-license-checks-and-compliance",
    "title": "6.4 License Checks and Compliance",
    "match_texts": [
      "6.4 License Checks and Compliance ⚪",
      "6.4 License Checks and Compliance"
    ]
  },
  {
    "id": "node_031",
    "kind": "section",
    "href": "landscape/06-compliance-infrastructure/#65-monitoring-and-governance",
    "title": "6.5 Monitoring and Governance",
    "match_texts": [
      "6.5 Monitoring and Governance ⚪",
      "6.5 Monitoring and Governance"
    ]
  },
  {
    "id": "node_032",
    "kind": "chapter",
    "href": "landscape/07-automation-integration/",
    "title": "7 Automation Infrastructure & Continuous Integration (CI)",
    "match_texts": [
      "7 Automation Infrastructure & Continuous Integration (CI) ⚪",
      "7 Automation Infrastructure & Continuous Integration (CI)"
    ]
  },
  {
    "id": "node_033",
    "kind": "section",
    "href": "landscape/07-automation-integration/#71-runners",
    "title": "7.1 Runners",
    "match_texts": [
      "7.1 Runners 🟠",
      "7.1 Runners"
    ]
  },
  {
    "id": "node_034",
    "kind": "section",
    "href": "landscape/07-automation-integration/#72-reusable-workflows",
    "title": "7.2 Reusable Workflows",
    "match_texts": [
      "7.2 Reusable Workflows ⚪",
      "7.2 Reusable Workflows"
    ]
  },
  {
    "id": "node_035",
    "kind": "section",
    "href": "landscape/07-automation-integration/#73-cross-repository-integration",
    "title": "7.3 Cross-Repository Integration",
    "match_texts": [
      "7.3 Cross-Repository Integration ⚪",
      "7.3 Cross-Repository Integration"
    ]
  },
  {
    "id": "node_036",
    "kind": "section",
    "href": "landscape/07-automation-integration/#74-secrets-management",
    "title": "7.4 Secrets Management",
    "match_texts": [
      "7.4 Secrets Management ⚪",
      "7.4 Secrets Management"
    ]
  },
  {
    "id": "node_037",
    "kind": "section",
    "href": "landscape/07-automation-integration/#75-ci-observability",
    "title": "7.5 CI Observability",
    "match_texts": [
      "7.5 CI Observability ⚪",
      "7.5 CI Observability"
    ]
  },
  {
    "id": "node_038",
    "kind": "chapter",
    "href": "landscape/08-artifact-distribution/",
    "title": "8 Release & Distribution",
    "match_texts": [
      "8 Release & Distribution ⚪",
      "8 Release & Distribution"
    ]
  },
  {
    "id": "node_039",
    "kind": "section",
    "href": "landscape/08-artifact-distribution/#81-deliverable-types",
    "title": "8.1 Deliverable Types",
    "match_texts": [
      "8.1 Deliverable Types ⚪",
      "8.1 Deliverable Types"
    ]
  },
  {
    "id": "node_040",
    "kind": "section",
    "href": "landscape/08-artifact-distribution/#82-distribution-channels",
    "title": "8.2 Distribution Channels",
    "match_texts": [
      "8.2 Distribution Channels ⚪",
      "8.2 Distribution Channels"
    ]
  },
  {
    "id": "node_041",
    "kind": "section",
    "href": "landscape/08-artifact-distribution/#83-release-metadata",
    "title": "8.3 Release Metadata",
    "match_texts": [
      "8.3 Release Metadata ⚪",
      "8.3 Release Metadata"
    ]
  },
  {
    "id": "node_042",
    "kind": "section",
    "href": "landscape/08-artifact-distribution/#84-consumer-access",
    "title": "8.4 Consumer Access",
    "match_texts": [
      "8.4 Consumer Access ⚪",
      "8.4 Consumer Access"
    ]
  },
  {
    "id": "node_043",
    "kind": "section",
    "href": "landscape/08-artifact-distribution/#85-post-release-communication-response",
    "title": "8.5 Post-Release Communication & Response",
    "match_texts": [
      "8.5 Post-Release Communication & Response ⚪",
      "8.5 Post-Release Communication & Response"
    ]
  },
  {
    "id": "node_044",
    "kind": "chapter",
    "href": "landscape/09-documentation-infrastructure/",
    "title": "9 Documentation & Traceability",
    "match_texts": [
      "9 Documentation & Traceability ⚪",
      "9 Documentation & Traceability"
    ]
  },
  {
    "id": "node_045",
    "kind": "section",
    "href": "landscape/09-documentation-infrastructure/#91-authoring-tooling",
    "title": "9.1 Authoring & Tooling",
    "match_texts": [
      "9.1 Authoring & Tooling ⚪",
      "9.1 Authoring & Tooling"
    ]
  },
  {
    "id": "node_046",
    "kind": "section",
    "href": "landscape/09-documentation-infrastructure/#92-build-validation-publishing",
    "title": "9.2 Build, Validation & Publishing",
    "match_texts": [
      "9.2 Build, Validation & Publishing ⚪",
      "9.2 Build, Validation & Publishing"
    ]
  },
  {
    "id": "node_047",
    "kind": "section",
    "href": "landscape/09-documentation-infrastructure/#93-cross-repository-documentation-integration",
    "title": "9.3 Cross-Repository Documentation Integration",
    "match_texts": [
      "9.3 Cross-Repository Documentation Integration ⚪",
      "9.3 Cross-Repository Documentation Integration"
    ]
  },
  {
    "id": "node_048",
    "kind": "section",
    "href": "landscape/09-documentation-infrastructure/#94-engineering-documentation-traceability",
    "title": "9.4 Engineering Documentation & Traceability",
    "match_texts": [
      "9.4 Engineering Documentation & Traceability ⚪",
      "9.4 Engineering Documentation & Traceability"
    ]
  },
  {
    "id": "node_049",
    "kind": "chapter",
    "href": "landscape/10-infrastructure-operations/",
    "title": "10 Infrastructure Operations",
    "match_texts": [
      "10 Infrastructure Operations ⚪",
      "10 Infrastructure Operations"
    ]
  },
  {
    "id": "node_050",
    "kind": "section",
    "href": "landscape/10-infrastructure-operations/#101-ci-runner-operations",
    "title": "10.1 CI Runner Operations",
    "match_texts": [
      "10.1 CI Runner Operations ⚪",
      "10.1 CI Runner Operations"
    ]
  },
  {
    "id": "node_051",
    "kind": "section",
    "href": "landscape/10-infrastructure-operations/#102-infrastructure-monitoring",
    "title": "10.2 Infrastructure Monitoring",
    "match_texts": [
      "10.2 Infrastructure Monitoring ⚪",
      "10.2 Infrastructure Monitoring"
    ]
  },
  {
    "id": "node_052",
    "kind": "section",
    "href": "landscape/10-infrastructure-operations/#103-infrastructure-maintenance",
    "title": "10.3 Infrastructure Maintenance",
    "match_texts": [
      "10.3 Infrastructure Maintenance ⚪",
      "10.3 Infrastructure Maintenance"
    ]
  },
  {
    "id": "node_053",
    "kind": "section",
    "href": "landscape/10-infrastructure-operations/#104-infrastructure-governance",
    "title": "10.4 Infrastructure Governance",
    "match_texts": [
      "10.4 Infrastructure Governance ⚪",
      "10.4 Infrastructure Governance"
    ]
  }
]
</script>
<!-- END GENERATED CHAPTER MAP -->

## Status Legend

- 🟢 Implemented and effective
- 🟡 Partially implemented / needs improvement
- 🟠 Implemented but problematic or insufficient
- 🔴 Not started
- ⚪ Unknown / not yet assessed

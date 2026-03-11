# Infrastructure Development Map

This page is the high-level planning dashboard for S-CORE infrastructure.

It answers three questions quickly:

- where we are strong, weak, or still forming
- what matters most in the near term
- where contributors can help now

Detailed work package tracking lives in the [Work Breakdown Structure](work-breakdown-structure.md).

## How To Read This Page

- use this page for landscape, priority, and contribution direction
- use [Infrastructure Areas](areas/source-code-infrastructure/index.md) for area context and boundaries
- use the [Work Breakdown Structure](work-breakdown-structure.md) for package-level status and dependencies

## Area Health And Near-Term Focus

Health legend:

- 🟢 stable baseline
- 🟡 partially established / active development
- 🔴 weak baseline or major gaps

| Area | Health | Near-Term Focus | Main Risk / Constraint | Where To Help Now |
| --- | --- | --- | --- | --- |
| [Source Code Infrastructure](areas/source-code-infrastructure/index.md) | 🟡 | Finish baseline repository standards and policy automation rollout. | Inconsistent repository setup and exception handling. | Standardize templates, metadata, and policy exception documentation. |
| [Build Infrastructure](areas/build-infrastructure/index.md) | 🟡 | Improve Bzlmod governance and build diagnostics. | Drift between repositories and uneven reproducibility practices. | Improve module onboarding and dependency governance guidance. |
| [Integration Infrastructure](areas/integration-infrastructure/index.md) | 🟡 | Expand reusable workflow coverage and validation consistency. | Fragmented pipeline behavior and diagnostics quality. | Improve reusable workflows, runner usage guidance, and failure reporting. |
| [Artifact Infrastructure](areas/artifact-infrastructure/index.md) | 🔴 | Define lifecycle, promotion, and retention baseline. | Publication exists, but lifecycle and retention rules are still weak. | Help define lifecycle rules and reduce manual publication steps. |
| [Testing Infrastructure](areas/testing-infrastructure/index.md) | 🟡 | Align test execution expectations and improve reporting quality. | Uneven framework integration and low signal quality in some pipelines. | Improve test reporting, diagnostics, and unstable test handling. |
| [Security & Compliance Infrastructure](areas/security-and-compliance-infrastructure/index.md) | 🟡 | Improve scanning rollout consistency and triage clarity. | Controls are present, but governance and reporting are incomplete. | Improve compliance automation and SBOM usage guidance. |
| [Documentation Infrastructure](areas/documentation-infrastructure/index.md) | 🟡 | Improve consistency, cross-links, and contributor guidance depth. | Technical content quality varies by area and maturity. | Improve practical guides and align area pages with current practice. |
| [Infrastructure Operations](areas/infrastructure-operations/index.md) | 🟡 | Improve monitoring ownership and incident handling baseline. | Operational knowledge is still partly implicit and manual. | Improve runbooks and recurring maintenance automation. |

## Current Cross-Area Priorities

1. Increase reusable workflow coverage to reduce duplicated integration logic.
2. Improve reproducibility and diagnostics in build and testing workflows.
3. Define artifact lifecycle and retention baseline.
4. Strengthen compliance integration with clear triage ownership.
5. Improve operational transparency through runbooks and monitoring ownership.

## Contribution Hotspots

- workflow reuse and diagnostics in Integration Infrastructure
- artifact lifecycle and publication consistency in Artifact Infrastructure
- compliance automation and reporting clarity in Security & Compliance Infrastructure
- contributor-facing documentation quality in Documentation Infrastructure

## Detailed Tracking

For the canonical work package register, including status and dependencies, see the [Work Breakdown Structure](work-breakdown-structure.md).

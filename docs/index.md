# S-CORE Infrastructure Landscape

:information_source: Early work in progress. Some chapters are currently generated drafts and will be refined iteratively.

---

## Purpose

This document maps the engineering infrastructure required to develop, build, test, integrate, secure, and distribute the S-CORE middleware.

It is intended as decision support, not only as an inventory. It helps teams answer:

- What infrastructure exists today?
- What is reliable, risky, or still missing?
- What should be prioritized next?

## Stakeholder Perspectives

### Project manager / product lead

Needs cross-domain visibility, ownership clarity, risk transparency, and prioritization input for roadmap planning.

### Infrastructure team member

Needs clear domain boundaries, required capabilities, operational expectations, and interfaces to adjacent domains.

### Project developer using infrastructure

Needs discoverable self-service workflows, clear entry points, and predictable tooling quality for daily development.

### Contributor / newcomer

Needs fast orientation, shared terminology, and simple navigation to chapter-level details.

## Scope

The document focuses on **engineering infrastructure**, meaning systems and tooling used to support development and integration of the middleware.

In scope:

- Engineering infrastructure systems and tooling
- Automation, policies, and operational practices across the development lifecycle
- Capability-level status and gaps per infrastructure domain

Out of scope:

- Feature-level product behavior
- General team process details that are not infrastructure-specific
- Full tool tutorials and runbooks (maintained in dedicated documents)

This includes domains such as:

```mermaid
flowchart LR

subgraph FLOW["Core Engineering Flow"]
    C1["1 Source Code Infrastructure 🟠"]
    C2["2 Build Infrastructure (Bazel) ⚪"]
    C3["3 Testing Infrastructure ⚪"]
    C4["4 Automation & CI/CD ⚪"]
    C5["5 Artifact & Distribution Infrastructure ⚪"]

    C1 --> C2 --> C3 --> C4 --> C5
end

subgraph SUPPORT["Cross-Cutting Supporting Layers"]
    C6["6 Compliance Infrastructure ⚪"]
    C7["7 Documentation Infrastructure ⚪"]
    C8["8 Infrastructure Operations ⚪"]
    C9["9 Developer Environment 🟠"]
    C10["10 Security Infrastructure ⚪"]
end

%% Hidden edges to force layout:
FLOW --- SUPPORT
C6 --- C7
C7 --- C8
C8 --- C9
C9 --- C10
linkStyle 4 stroke-width:0px
linkStyle 5 stroke-width:0px
linkStyle 6 stroke-width:0px
linkStyle 7 stroke-width:0px
linkStyle 8 stroke-width:0px

click C1 href "chapters/01-source-code-infrastructure/" "Open chapter 1"
click C2 href "chapters/02-build-infrastructure/" "Open chapter 2"
click C3 href "chapters/03-testing-infrastructure/" "Open chapter 3"
click C4 href "chapters/04-automation-integration/" "Open chapter 4"
click C5 href "chapters/05-artifact-distribution/" "Open chapter 5"
click C6 href "chapters/06-compliance-infrastructure/" "Open chapter 6"
click C7 href "chapters/07-documentation-infrastructure/" "Open chapter 7"
click C8 href "chapters/08-infrastructure-operations/" "Open chapter 8"
click C9 href "chapters/09-developer-environment/" "Open chapter 9"
click C10 href "chapters/10-security-infrastructure/" "Open chapter 10"
```

Each chapter should describe:

- Domain purpose and boundaries
- Required capabilities
- Current state with evidence where available
- Known gaps, risks, and next improvements
- Ownership (team or role), if known

## How To Use This Landscape

- For planning and governance: use status and gaps to prioritize work and define roadmap items.
- For implementation: use capability lists as baseline contracts for infrastructure domains.
- For day-to-day development: use chapter links as entry points to tooling and process references.

## Infrastructure Status Model

Legend:

- 🟢 Implemented and effective in regular use
- 🟡 Partially implemented, inconsistent, or missing key quality attributes
- 🟠 Implemented but currently problematic or insufficient for project needs
- 🔴 Not started
- ⚪ Unknown / not yet assessed

Assessment guidance:

- Prefer evidence over opinion (pipeline usage, metrics, incidents, user feedback)
- State assumptions explicitly when evidence is not yet available
- Reassess statuses periodically to keep planning decisions current

## Documentation Approach

This landscape is maintained as Markdown in a docs-as-code workflow because it:

- Keeps review and change history transparent
- Supports collaborative editing through pull requests
- Can be published as a website while remaining repository-native

The final delivery form can evolve (website, issue views, or other formats), while this source remains the canonical baseline.

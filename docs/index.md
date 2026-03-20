# S-CORE Infrastructure Landscape

:information_source: Work in progress. Some chapters are generated drafts and still under review.

---

## What This Is

A concise map of S-CORE engineering infrastructure: what exists, what is missing, and what needs priority.

## How To Read It

- Start with the chapter matching your topic.
- Use the status icon to judge maturity.
- Read "Biggest gap" to understand the next improvement focus.

## Chapter Map

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

## Status Legend

- 🟢 Implemented and effective
- 🟡 Partially implemented / needs improvement
- 🟠 Implemented but problematic or insufficient
- 🔴 Not started
- ⚪ Unknown / not yet assessed

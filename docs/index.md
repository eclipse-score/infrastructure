# S-CORE Infrastructure Landscape

<div class="landing-hero">
  <p class="landing-kicker">Overview, development map, contribution map, and reference</p>
  <h2>Get oriented in the S-CORE infrastructure landscape.</h2>
  <p class="landing-lead">
    This site explains what S-CORE infrastructure is, which building blocks already exist, how mature they are,
    what is still missing, and how a concrete issue or pull request fits into the bigger picture.
  </p>
</div>

<div class="landing-grid landing-grid-3">
  <div class="landing-card">
    <h3>Who this is for</h3>
    <p>
      Technical and non-technical stakeholders who need an overview, plus infrastructure contributors
      who need to understand the current state, gaps, and direction of the platform.
    </p>
  </div>
  <div class="landing-card">
    <h3>What this repository documents</h3>
    <p>
      The technical capabilities that make engineering work possible and scalable across S-CORE:
      source code management, builds, testing, static analysis, automation, compliance,
      documentation, operations, developer environments, and security.
    </p>
  </div>
  <div class="landing-card">
    <h3>What this site is for</h3>
    <p>
      An infrastructure overview, a development map for current state and remaining work,
      a contribution map for infrastructure contributors, and a reference for architecture
      and cross-cutting concerns.
    </p>
  </div>
</div>

## Start Here

<div class="landing-grid landing-grid-2">
  <div class="landing-card">
    <h3>I need an overview</h3>
    <ul>
      <li>Start with the chapter map below.</li>
      <li>Use the status icon to judge maturity.</li>
      <li>Open the chapter that matches the area you want to understand.</li>
    </ul>
  </div>
  <div class="landing-card">
    <h3>I am working on infrastructure</h3>
    <ul>
      <li>Find the most relevant infrastructure chapter.</li>
      <li>Read the chapter summary and the "Biggest gap".</li>
      <li>Use that context to place your issue, PR, or initiative in the wider development picture.</li>
    </ul>
  </div>
</div>

## Questions This Page Helps Answer

<div class="landing-grid landing-grid-2">
  <div class="landing-card">
    <h3>Overview questions</h3>
    <ul>
      <li>What do we mean by S-CORE infrastructure?</li>
      <li>Which infrastructure building blocks already exist?</li>
      <li>How far along is each area?</li>
    </ul>
  </div>
  <div class="landing-card">
    <h3>Contribution questions</h3>
    <ul>
      <li>How do we do a specific thing?</li>
      <li>Where should I look for a topic or responsibility?</li>
      <li>How does this issue or PR belong to the big picture?</li>
    </ul>
  </div>
</div>

## Chapter Map

```mermaid
flowchart LR

subgraph FLOW["Core Engineering Flow"]
    C1["1 Source Code Infrastructure 🟠"]
    C2["2 Build Infrastructure (Bazel) ⚪"]
    C3["3 Testing Infrastructure ⚪"]
    C4["4 Static Analysis Infrastructure ⚪"]
    C5["5 Automation & CI/CD ⚪"]
    C6["6 Artifact & Distribution Infrastructure ⚪"]

    C1 --> C2 --> C3 --> C4 --> C5 --> C6
end

subgraph SUPPORT["Cross-Cutting Supporting Layers"]
    C7["7 Compliance Infrastructure ⚪"]
    C8["8 Documentation Infrastructure ⚪"]
    C9["9 Infrastructure Operations ⚪"]
    C10["10 Developer Environment 🟠"]
    C11["11 Security Infrastructure ⚪"]
end

%% Hidden edges to force layout:
FLOW --- SUPPORT
C7 --- C8
C8 --- C9
C9 --- C10
C10 --- C11
linkStyle 5 stroke-width:0px
linkStyle 6 stroke-width:0px
linkStyle 7 stroke-width:0px
linkStyle 8 stroke-width:0px
linkStyle 9 stroke-width:0px

click C1 href "chapters/01-source-code-infrastructure/" "Open chapter 1"
click C2 href "chapters/02-build-infrastructure/" "Open chapter 2"
click C3 href "chapters/03-testing-infrastructure/" "Open chapter 3"
click C4 href "chapters/04-static-analysis-infrastructure/" "Open chapter 4"
click C5 href "chapters/04-automation-integration/" "Open chapter 5"
click C6 href "chapters/05-artifact-distribution/" "Open chapter 6"
click C7 href "chapters/06-compliance-infrastructure/" "Open chapter 7"
click C8 href "chapters/07-documentation-infrastructure/" "Open chapter 8"
click C9 href "chapters/08-infrastructure-operations/" "Open chapter 9"
click C10 href "chapters/09-developer-environment/" "Open chapter 10"
click C11 href "chapters/10-security-infrastructure/" "Open chapter 11"
```

## How To Read The Chapters

<div class="landing-grid landing-grid-3">
  <div class="landing-card landing-card-compact">
    <h3>1. Pick a topic</h3>
    <p>Open the area closest to your question, task, or architectural concern.</p>
  </div>
  <div class="landing-card landing-card-compact">
    <h3>2. Check maturity</h3>
    <p>Use the status icon to understand whether the area is established, partial, weak, or still unclear.</p>
  </div>
  <div class="landing-card landing-card-compact">
    <h3>3. Look at the gap</h3>
    <p>Read "Biggest gap" to see what is missing, what remains to be improved, and why the area still matters.</p>
  </div>
</div>

## Status Legend

- 🟢 Implemented and effective
- 🟡 Partially implemented / needs improvement
- 🟠 Implemented but problematic or insufficient
- 🔴 Not started
- ⚪ Unknown / not yet assessed

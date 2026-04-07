# S-CORE Infrastructure Landscape

<div class="landing-hero">
  <p class="landing-kicker">Overview, roadmap, contribution guide, and reference</p>
  <h2>Get oriented in the S-CORE infrastructure landscape.</h2>
  <p class="landing-lead">
    This site explains what S-CORE infrastructure is, which building blocks already exist, how mature they are,
    what is still missing, and how a concrete issue or pull request fits into the bigger picture.
  </p>
</div>

<div class="landing-grid landing-grid-3">
  <div class="landing-card">
    <h3>Who should read this</h3>
    <p>
      Technical and non-technical stakeholders who need an overview, plus infrastructure contributors
      who need to understand the current state, gaps, and direction of the project infrastructure.
    </p>
    <p>Typical reader questions:</p>
    <ul>
      <li>What do we mean by S-CORE infrastructure?</li>
      <li>Which infrastructure building blocks already exist?</li>
      <li>How far along is each area?</li>
    </ul>
  </div>
  <div class="landing-card">
    <h3>What it covers</h3>
    <p>
      The technical capabilities that make engineering work possible and scalable across S-CORE:
      source code infrastructure, developer environment, builds and dependencies, testing,
      code analysis, dependency analysis, automation, release distribution, documentation,
      traceability, and operations.
    </p>
    <p>
      Cross-cutting concerns such as security and compliance are described inside the chapters
      where the work actually happens rather than as standalone silos.
    </p>
  </div>
  <div class="landing-card">
    <h3>What this site is for</h3>
    <p>
      An infrastructure overview, a development map for current state and remaining work,
      a contribution map for infrastructure contributors, and a reference for architecture
      and cross-cutting concerns.
    </p>
    <p>Typical contributor questions:</p>
    <ul>
      <li>How do we do a specific thing?</li>
      <li>Where should I look for a topic or responsibility?</li>
      <li>How does this issue or PR belong to the big picture?</li>
    </ul>
  </div>
</div>

## Start Here

<div class="landing-grid landing-grid-2">
  <div class="landing-card">
    <h3>For a quick overview</h3>
    <ul>
      <li>Scan the chapter map below.</li>
      <li>Use the status icon to judge maturity at a glance.</li>
      <li>Open the chapter that matches the area you want to understand better.</li>
    </ul>
  </div>
  <div class="landing-card">
    <h3>For contribution work</h3>
    <ul>
      <li>Find the most relevant infrastructure chapter.</li>
      <li>Read the summary, maturity, and "Biggest gap".</li>
      <li>Use that context to place an issue, PR, or initiative in the wider infrastructure picture.</li>
    </ul>
  </div>
</div>

## Chapter Map

```mermaid
flowchart LR

subgraph FLOW["Engineering Infrastructure Flow"]
    C1["1 Source Code Infrastructure 🟡"]
    C2["2 Developer Environment 🟠"]
    C3["3 Build & Dependencies ⚪"]
    C4["4 Testing ⚪"]
    C5["5 Code Analysis Infrastructure ⚪"]
    C6["6 Dependency Analysis Infrastructure ⚪"]
    C7["7 Automation & CI ⚪"]
    C8["8 Release & Distribution ⚪"]

    C1 --> C2 --> C3 --> C4 --> C5 --> C6 --> C7 --> C8
end

subgraph SUPPORT["Supporting Layers"]
    C9["9 Documentation & Traceability ⚪"]
    C10["10 Infrastructure Operations ⚪"]
end

%% Hidden edges to force layout:
FLOW --- SUPPORT
C9 --- C10
linkStyle 7 stroke-width:0px
linkStyle 8 stroke-width:0px

click C1 href "source-code-infrastructure/" "Open chapter 1"
click C2 href "developer-environment/" "Open chapter 2"
click C3 href "build-infrastructure/" "Open chapter 3"
click C4 href "testing-infrastructure/" "Open chapter 4"
click C5 href "static-analysis-infrastructure/" "Open chapter 5"
click C6 href "compliance-infrastructure/" "Open chapter 6"
click C7 href "automation-integration/" "Open chapter 7"
click C8 href "artifact-distribution/" "Open chapter 8"
click C9 href "documentation-infrastructure/" "Open chapter 9"
click C10 href "infrastructure-operations/" "Open chapter 10"
```

## How To Use A Chapter

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

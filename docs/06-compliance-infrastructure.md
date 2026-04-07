# 6 Dependency Analysis Infrastructure ⚪

*Infrastructure for analyzing S-CORE dependencies and generated dependency evidence to detect vulnerability, supply-chain, and compliance risk over time.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Dependency analysis complements the dependency-governance work in [chapter 3](03-build-infrastructure.md) by evaluating current dependency state and generated dependency evidence.
- This chapter covers both development-time dependency alerts and continuous monitoring of generated SBOMs for distributed artifacts.
- It applies to product artifacts, self-developed tooling, and environment artifacts such as devcontainer images when S-CORE builds and distributes them.
- Publication and consumer delivery of those artifacts remain the responsibility of [chapter 8](08-artifact-distribution.md).
- **Biggest gap**: dependency analysis is not yet defined as one cross-repository capability spanning current dependency scanning, generated SBOM monitoring, and the resulting governance loop.

## 6.1 Analysis Scope & Inputs ⚪

*Defining which dependency-related inputs are analyzed and which artifact classes are in scope.*

**S-CORE**

- Dependency analysis starts from current repository dependency state, but it should also consume build-generated inventories and SBOMs once those exist.
- The same infrastructure should work across product code, tooling artifacts, and environment artifacts rather than treating those as special cases.
- **Biggest gap**: there is no clearly documented scope for which dependency inputs and artifact classes must be covered by the shared analysis model.

### 6.1.1 Current Dependency State

*Analyzing the dependencies currently declared and consumed during engineering work.*

**S-CORE**

- Current dependency state includes the dependency graph as repositories know it during development and CI.
- **Biggest gap**: not all repositories expose their current dependency state in a way that shared analysis tooling can consume consistently.

### 6.1.2 Generated SBOMs and Inventories

*Using build-generated SBOMs and dependency inventories as analyzable inputs rather than static paperwork.*

**S-CORE**

- SBOMs and inventories generated in [chapter 3](03-build-infrastructure.md) should become normal inputs to later security and compliance analysis.
- **Biggest gap**: generated dependency evidence is not yet consumed systematically by downstream analysis workflows.

### 6.1.3 Tooling & Environment Artifact Scope

*Including S-CORE-developed tooling and environment artifacts in the dependency-analysis model.*

**S-CORE**

- Tooling packages and dev environment images also package dependencies, licenses, and supply-chain choices that deserve the same visibility as product artifacts.
- **Biggest gap**: tooling and environment artifacts are not yet treated as first-class targets for dependency analysis.

---

## 6.2 Development-Time Dependency Analysis ⚪

*Detecting dependency and supply-chain risk during normal engineering work before artifacts are published.*

**S-CORE**

- Development-time dependency analysis should be part of normal repository and CI feedback loops.
- This work complements code analysis in [chapter 5](05-static-analysis-infrastructure.md) but focuses on dependency state rather than source structure.
- **Biggest gap**: development-time dependency scanning is not yet configured consistently across repositories and artifact classes.

### 6.2.1 Dependency Alerts

*Detecting known vulnerabilities in the dependencies currently used by repositories.*

**S-CORE**

- Dependency alerts should make it obvious when a repository is consuming a vulnerable version before that problem reaches later release flows.
- **Biggest gap**: dependency-vulnerability detection is not yet consistently configured across repositories.

### 6.2.2 Supply Chain & Source Analysis

*Evaluating dependency sources, integrity, and other supply-chain characteristics during engineering work.*

**S-CORE**

- This includes analysis of where dependencies come from, how they are pinned, and whether supply-chain controls are being followed in practice.
- **Biggest gap**: supply-chain analysis of repository dependency inputs is not yet described as one shared capability.

### 6.2.3 CI and Local Expectations

*Defining where dependency analysis should run and how strongly it should influence normal engineering decisions.*

**S-CORE**

- Dependency analysis may run primarily in CI, but repositories still need a clear model for what is expected locally and what is enforced automatically.
- **Biggest gap**: there is no shared execution and gate model for dependency analysis across local and CI contexts.

---

## 6.3 Continuous Artifact Monitoring ⚪

*Monitoring generated SBOMs and distributed artifacts over time after they have been built.*

**S-CORE**

- Once artifacts and their SBOMs exist, the analysis problem changes from "what are we using right now?" to "which distributed artifacts have become risky over time?"
- This is where continuous SBOM-based monitoring belongs, distinct from both code analysis and simple release publication.
- **Biggest gap**: no automated process continuously evaluates generated SBOMs for newly disclosed risk across S-CORE artifact types.

### 6.3.1 Continuous SBOM Monitoring

*Continuously evaluating generated SBOMs to detect newly relevant vulnerabilities or supply-chain concerns.*

**S-CORE**

- Continuous SBOM monitoring should work for released artifacts, internally distributed tooling, and environment images alike.
- **Biggest gap**: no automated process monitors and alerts on vulnerabilities affecting distributed S-CORE artifacts via their SBOMs.

### 6.3.2 Vulnerability Impact Analysis

*Determining which artifact versions are affected once a dependency issue is discovered.*

**S-CORE**

- Impact analysis depends on good SBOMs, inventories, and version metadata so the project can quickly identify which distributed artifacts are affected.
- **Biggest gap**: no tooling supports automated dependency-issue-to-artifact impact mapping across S-CORE.

### 6.3.3 Monitoring Cadence & Data Freshness

*Defining how often artifact evidence should be re-evaluated and how long that evidence remains useful.*

**S-CORE**

- Continuous monitoring only works when SBOMs, inventories, and vulnerability data are fresh enough to support real decisions.
- **Biggest gap**: there is no shared cadence or freshness model for dependency evidence and its monitoring lifecycle.

---

## 6.4 Findings & Governance ⚪

*Handling dependency-analysis findings and making their status visible across repositories and artifact types.*

**S-CORE**

- Dependency analysis needs a governance loop for triage, ownership, exceptions, and cross-repository reporting just as much as code analysis does.
- The project needs to see not only individual alerts, but also where dependency-analysis coverage is still missing.
- **Biggest gap**: no shared governance loop currently connects dependency findings, ownership, and coverage visibility across S-CORE.

### 6.4.1 Findings Ownership

*Clarifying who is expected to fix, triage, or escalate dependency-analysis findings.*

**S-CORE**

- Dependency findings may involve repository maintainers, tooling owners, and infrastructure maintainers depending on where the affected artifact originates.
- **Biggest gap**: there is no documented ownership model for handling dependency-analysis results across artifact classes.

### 6.4.2 Baselines and Risk Acceptance

*Handling existing dependency debt and justified exceptions without losing visibility.*

**S-CORE**

- Some dependency risks may need temporary acceptance or migration baselines while repositories catch up.
- **Biggest gap**: there is no shared policy for how dependency-analysis exceptions are justified, tracked, and revisited.

### 6.4.3 Cross-Repository Visibility

*Measuring analysis coverage and findings across repositories and distributed artifacts.*

**S-CORE**

- Cross-repository visibility should show where dependency analysis is configured, which artifact classes are covered, and where unresolved issues remain.
- **Biggest gap**: no common dashboard or conformance report currently summarizes dependency-analysis coverage across S-CORE.

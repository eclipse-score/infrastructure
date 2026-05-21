# 6 Compliance & Dependency Analysis ⚪

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

:::{note} Not yet assessed
All sections in this chapter are marked ⚪ (not yet assessed). The content describes the target architecture and known gaps, not the current state of implementation.
:::

*Infrastructure for turning repository files, dependency declarations, and build outputs into licensing evidence, SBOMs, and ongoing compliance and vulnerability monitoring across S-CORE.*

The compliance flow has five stages. File-level licensing (§6.1) classifies every file as first-party or third-party. Dependency analysis (§6.2) discovers what each repository consumes and produces enriched SBOMs. SBOM scoping (§6.3) decides which evidence belongs in which SBOM and who receives it. License checks (§6.4) verify that the license profile is acceptable and produce a license-enriched SBOM. Monitoring and governance (§6.5) uses that artifact for ongoing vulnerability detection and compliance oversight.

[Chapter 3](03-build-infrastructure.md) owns generating raw build evidence. [Chapter 7](07-automation-integration.md) owns CI orchestration. [Chapter 8](08-artifact-distribution.md) owns artifact publication. This chapter owns interpreting, enriching, scoping, and checking compliance evidence.

The tooling landscape for this area is still early-stage. [eclipse-score/sbom-tool](https://github.com/eclipse-score/sbom-tool) is a proof-of-concept Bazel rule set that integrates SBOM generation into the build, using dash-license-scan and cdxgen as data sources for license enrichment. It belongs entirely to this chapter: it consumes build outputs as inputs but owns discovery, enrichment, and SBOM generation — all compliance concerns. The remaining gaps are around scope decisions, non-Bazel repositories, monitoring, and governance — which is what this chapter describes.

```{mermaid}
flowchart TD
    subgraph s61 ["§ 6.1  File-Level Licensing"]
        repo_files["Repository files"]
        file_class["File classification\n(first / third-party)"]
        repo_files --> file_class
    end

    subgraph s62 ["§ 6.2  Dependency Analysis"]
        dep_sources["`Dependency manifests
+ build graphs`"]
        enriched_sboms["Enriched SBOMs"]
        dep_sources --> enriched_sboms
    end

    subgraph s63 ["§ 6.3  SBOM Scoping and Compliance Evidence"]
        scope{"`Scope decision
(dev / product)`"}
        scoped_sboms["Scoped SBOMs"]
        scope --> scoped_sboms
    end

    subgraph s64 ["§ 6.4  License Checks and Compliance"]
        license_check["License checking\n(Dash / IP review)"]
        license_sbom["License-enriched SBOM"]
        license_check --> license_sbom
    end

    subgraph s65 ["§ 6.5  Monitoring and Governance"]
        monitoring["Vulnerability monitoring"]
        governance["Findings & coverage"]
    end

    file_class --> scope
    enriched_sboms --> scope
    scoped_sboms --> license_check
    license_sbom --> monitoring
    license_sbom --> governance
    monitoring --> governance

    classDef artifact fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1
    classDef action fill:#E8F5E9,stroke:#43A047,color:#1B5E20
    classDef decision fill:#FFF3E0,stroke:#FB8C00,color:#E65100
    classDef outcome fill:#F3E5F5,stroke:#8E24AA,color:#4A148C

    class repo_files,dep_sources,file_class,enriched_sboms,scoped_sboms,license_sbom artifact
    class scope decision
    class license_check,monitoring action
    class governance outcome
```

## 6.1 File-Level Licensing ⚪

*Classifying repository files as first-party or third-party and attaching machine-readable licensing metadata.*

```{mermaid}
flowchart LR
    file["Repository files"]
    header_ok{"`Supports
inline header?`"}
    header["`Copyright + SPDX
header`"]
    sidecar[".license sidecar"]
    owner{"`Copyright holder
= S-CORE?`"}
    first["First-party"]
    third["Third-party"]
    out["`File classification
→ §6.3`"]

    file --> header_ok
    header_ok -->|Yes| header
    header_ok -->|No| sidecar
    header --> owner
    sidecar --> owner
    owner -->|Yes| first
    owner -->|No| third
    first --> out
    third --> out

    classDef artifact fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1
    classDef action fill:#E8F5E9,stroke:#43A047,color:#1B5E20
    classDef decision fill:#FFF3E0,stroke:#FB8C00,color:#E65100
    classDef context fill:#F5F5F5,stroke:#BDBDBD,color:#757575

    class file,first,third artifact
    class header,sidecar action
    class header_ok,owner decision
    class out context
```

### 6.1.1 Metadata Model

*How files carry their licensing information and how first-party content is distinguished from third-party content.*

Every file needs machine-readable licensing metadata in one of two forms: a copyright notice and SPDX license identifier in the file header, or a sidecar `.license` file for formats that cannot carry inline headers. This metadata is what allows tooling to distinguish first-party S-CORE material from third-party imports. Third-party files need to stay visible as externally sourced so they reach later license-compliance steps.

**Biggest gap**: file-level licensing metadata and first-party versus third-party classification are not yet enforced consistently across repositories.

### 6.1.2 Enforcement

*Automated enforcement of file-level licensing metadata through local hooks and CI checks.*

Consistent metadata requires two enforcement layers: a pre-commit hook that auto-adds the correct header to new first-party files, and a CI check that verifies all files carry required metadata. Both should share the same configuration so local and remote enforcement agree. REUSE-style validation is the likely long-term consolidation point. Copyright tooling from [eclipse-score/tooling](https://github.com/eclipse-score/tooling) currently provides a pre-commit hook and PR check.

**Biggest gap**: enforcement coverage is inconsistent across repositories, and the boundary between current header tooling and REUSE-based validation is not yet resolved.

## 6.2 Dependency Analysis ⚪

*Discovering what a repository consumes and producing enriched SBOM-format outputs.*

This path requires three distinct capabilities: dependency discovery, license enrichment, and SBOM-format output. In Bazel-based repositories, [eclipse-score/sbom-tool](https://github.com/eclipse-score/sbom-tool) already integrates all three as a Bazel rule. It uses the Bazel module graph and aspects for discovery, dash-license-scan for Rust license data, cdxgen for C++ license data, and produces SPDX 2.3 / CycloneDX 1.6 output — so these tools are data sources within one orchestrated build step, not competing alternatives.

```{mermaid}
flowchart LR
    subgraph inputs ["Build inputs"]
        direction TB
        lockfiles["Lock files"]
        modulegraph["`Bazel module graph
+ aspects`"]
        manual["`Manual
declarations`"]
    end

    subgraph enrichment ["License data sources"]
        direction TB
        dash["`dash-license-scan
(Rust)`"]
        cdxgen["`cdxgen
(C++)`"]
    end

    sbom_tool["`SBOM generator
(sbom-tool)`"]
    sbom_output["`SPDX 2.3
CycloneDX 1.6`"]
    out["`Enriched SBOMs
→ §6.3`"]

    inputs --> sbom_tool
    enrichment --> sbom_tool
    sbom_tool --> sbom_output --> out

    classDef artifact fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1
    classDef action fill:#E8F5E9,stroke:#43A047,color:#1B5E20
    classDef transparent fill:none,stroke:#ccc
    classDef context fill:#F5F5F5,stroke:#BDBDBD,color:#757575

    class lockfiles,modulegraph,manual,sbom_output artifact
    class dash,cdxgen,sbom_tool action
    class inputs,enrichment transparent
    class out context
```

### 6.2.1 Discovery and Enrichment

*Collecting dependency information from multiple sources and mapping it to license status.*

For Bazel-based repositories, [sbom-tool](https://github.com/eclipse-score/sbom-tool) already combines these sources: the Bazel module graph provides structural dependency data, lock files provide version and checksum data, dash-license-scan enriches Rust crate licenses via the Eclipse Dash License Tool, and cdxgen scans C++ dependencies. Manual declarations cover vendored content and transitive relationships that automated sources miss. The result is a merged, enriched SBOM produced as a normal build output.

For non-Bazel repositories, no equivalent integration exists yet. The same capabilities are needed — discovery, enrichment, output — but the tooling path is undefined.

**Biggest gap**: sbom-tool covers Bazel-based repositories as a proof of concept, but the flow is not yet consistently available across all repository types. Coverage for non-Bazel repositories and for C++ license enrichment (where dash-license-scan does not yet work) remains open.

## 6.3 SBOM Scoping and Compliance Evidence ⚪

*Deciding what belongs in which SBOM and who consumes the resulting compliance evidence.*

This is where the two input paths converge. One repository does not produce one SBOM — it produces inputs to a scope decision that determines which evidence goes where and to whom.

```{mermaid}
flowchart TD
    in61["`File classification
← §6.1`"]
    in62["`Enriched SBOMs
← §6.2`"]

    scope{"`Scope
decision`"}

    dev_sbom["`Development SBOM
(build scope)`"]
    prod_sbom["`Product SBOM
(runtime scope)`"]

    license_checks["`License checks
→ §6.4`"]
    distributor_source["`Distributor: source
release scan`"]
    distributor_runtime["`Distributor: runtime
image scan`"]

    in61 --> scope
    in62 --> scope
    scope --> dev_sbom
    scope --> prod_sbom

    dev_sbom --> license_checks
    prod_sbom --> license_checks
    prod_sbom --> distributor_source
    prod_sbom --> distributor_runtime

    classDef artifact fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1
    classDef decision fill:#FFF3E0,stroke:#FB8C00,color:#E65100
    classDef consumer fill:#F3E5F5,stroke:#8E24AA,color:#4A148C
    classDef context fill:#F5F5F5,stroke:#BDBDBD,color:#757575

    class dev_sbom,prod_sbom artifact
    class scope decision
    class distributor_source,distributor_runtime consumer
    class in61,in62,license_checks context
```

### 6.3.1 Development vs Product Scope

*Distinguishing between build-scope and runtime-scope compliance evidence.*

Some dependencies belong only to building, testing, or the development environment. Others are part of the delivered runtime product. That distinction changes which SBOM is produced, how findings are interpreted, and which consumers care. The same scope model applies to S-CORE's tooling and environment artifacts such as devcontainers — [chapter 3](03-build-infrastructure.md#tooling-environment-sboms-license-evidence) describes how they produce build evidence; this chapter owns the scope decision.

**Biggest gap**: no shared definition yet of which inputs belong in development-scope versus product-scope SBOMs.

### 6.3.2 Compliance Consumers

*Who uses the scoped evidence and for what purpose.*

Scoped SBOMs serve two immediate audiences before feeding downstream. Internally, they are the input to §6.4 License Checks and Compliance. For downstream distributors, they support OSS scans whose scope varies by deliverable type: a source release, a runtime image, and a redistributed tool are different scan targets with different questions. Vulnerability monitoring (§6.5) sits downstream of §6.4 and receives the license-enriched SBOM, not the scoped SBOM directly.

**Biggest gap**: no shared model defines which deliverable is the scan target in each compliance situation.

## 6.4 License Checks and Compliance ⚪

*Verifying that dependencies meet S-CORE's license policy and producing a license-enriched SBOM as output.*

Scoped SBOMs from §6.3 carry dependency metadata but license status may still be unresolved or incomplete. This section runs the actual license checks — automated via Dash and manual via IP review — and resolves those gaps. The result is a **license-enriched SBOM** with verified license status for every component. That artifact is what §6.5 uses for vulnerability monitoring and governance; it is a richer input than the scoped SBOM from §6.3.

```{mermaid}
flowchart LR
    in63["`Scoped SBOMs
← §6.3`"]

    pr_check["`PR-scoped
check`"]
    ip_review["`IP review &
policy`"]

    license_sbom["`License-enriched
SBOM → §6.5`"]

    in63 --> pr_check
    in63 --> ip_review
    pr_check --> license_sbom
    ip_review --> license_sbom

    classDef artifact fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1
    classDef action fill:#E8F5E9,stroke:#43A047,color:#1B5E20
    classDef context fill:#F5F5F5,stroke:#BDBDBD,color:#757575

    class license_sbom artifact
    class pr_check,ip_review action
    class in63 context
```

### 6.4.1 PR-Scoped License Checking

*Checking dependency license status as part of the contribution workflow without creating noise.*

Full-repository license scans on every PR produce too much noise. The effective model is scoped checking: run only when dependency changes are detected, surface results only when new license questions arise. This pattern matters regardless of which tool implements it — the check should be scoped to changes, produce structured output, and integrate into PR review.

**Biggest gap**: PR-scoped dependency license checking is not consistently available across repositories.

### 6.4.2 IP Review and Project Policy

*Routing license findings that require human review and maintaining a shared policy for accepted and rejected licenses.*

Automated checks resolve most license questions, but some dependencies require IP review. The project also needs a shared license policy — allowlists for accepted licenses and a clear escalation path for non-standard situations. That policy should be machine-readable enough to feed back into automated checks rather than living only in documents.

**Biggest gap**: no shared license policy or allowlist is defined at the S-CORE level; individual repositories handle license decisions ad hoc.

## 6.5 Monitoring and Governance ⚪

*Continuous vulnerability monitoring, findings ownership, and cross-repository compliance visibility.*

The compliance flow becomes useful infrastructure only when SBOMs stay fresh, findings can be owned, and coverage gaps stay visible.

```{mermaid}
flowchart TD
    in64["`License-enriched SBOM
← §6.4`"]

    upload["`Upload to GitHub
/ Dependency-Track`"]
    vuln["Vulnerability findings"]

    ownership["Findings ownership"]
    baselines["Baselines & exceptions"]
    visibility["Cross-repo coverage visibility"]

    in64 --> upload --> vuln
    vuln --> ownership
    vuln --> baselines
    ownership --> visibility
    baselines --> visibility

    classDef artifact fill:#E3F2FD,stroke:#1E88E5,color:#0D47A1
    classDef action fill:#E8F5E9,stroke:#43A047,color:#1B5E20
    classDef outcome fill:#F3E5F5,stroke:#8E24AA,color:#4A148C
    classDef context fill:#F5F5F5,stroke:#BDBDBD,color:#757575

    class vuln artifact
    class upload action
    class ownership,baselines,visibility outcome
    class in64 context
```

### 6.5.1 Continuous Vulnerability Monitoring

*Using license-enriched SBOMs as ongoing monitoring inputs to detect newly relevant issues over time.*

Uploading SBOMs to systems such as GitHub and Dependency-Track allows the project to detect vulnerabilities after the initial build. sbom-tool already includes an SPDX-to-GitHub-snapshot converter for this purpose, though it is not yet integrated into a cross-repository upload flow. Monitoring is also the basis for impact analysis — mapping a newly disclosed vulnerability back to affected artifact versions and repository owners. This only works if uploads stay fresh; a stale SBOM gives a false sense of coverage.

**Biggest gap**: no shared process keeps SBOM uploads fresh or supports impact analysis across S-CORE artifact types.

### 6.5.2 Findings Ownership and Baselines

*Clarifying who owns compliance findings and how existing debt is handled.*

Findings come from different parts of the flow, so ownership cannot default to one team. A missing header belongs to a repository maintainer; a broken enrichment step belongs to tooling owners; a vulnerability in a distributed artifact belongs to whoever publishes it. Not every issue can be fixed immediately — temporary baselines are acceptable as long as exceptions remain visible, justified, and reviewable.

**Biggest gap**: no documented ownership model connects findings to the responsible step in the compliance pipeline, and no shared policy defines how exceptions are justified, recorded, and revisited.

### 6.5.3 Cross-Repository Visibility

*Measuring how completely the compliance flow is implemented across repositories.*

Visibility should show not just current findings but also coverage: which repositories classify files, which produce scoped SBOMs, which upload to monitoring, and where enrichment is still missing.

**Biggest gap**: no conformance report shows how completely the compliance flow is implemented across S-CORE.
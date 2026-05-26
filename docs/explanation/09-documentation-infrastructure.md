# 9 Documentation & Traceability 🟠

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure supporting engineering documentation across S-CORE repositories.*

**S-CORE**

- Documentation infrastructure in S-CORE currently spans repository documentation sites and engineering-focused docs-as-code capabilities.
- Documentation is published through CI-driven static site generation and hosting.
- Engineering traceability (requirements, architecture, design, implementation, tests) is a target capability for functional safety compliance.
- **Biggest gap**: shared documentation conventions, cross-repository navigation, and traceability integration are not yet defined as one coherent project-wide capability.

## 9.1 Authoring & Tooling 🟡

*Capabilities for writing, structuring, and maintaining documentation in repositories.*

**S-CORE**

- Documentation is authored in version-controlled repositories alongside source code.
- Markdown and rST are the primary input formats.
- **Biggest gap**: authoring conventions and required documentation structure are not yet standardized across S-CORE repositories.

### 9.1.1 Docs-As-Code Tooling 🟡

*Shared documentation build infrastructure across S-CORE repositories.*

**S-CORE**

[eclipse-score/docs-as-code](https://github.com/eclipse-score/docs-as-code) provides the shared documentation build tooling consumed across S-CORE. It packages Sphinx with MyST parser, the pydata-sphinx-theme with S-CORE branding, traceability support via sphinx-needs, and related documentation infrastructure into a versioned Bazel module. Repositories declare a dependency on `docs-as-code` to get a consistent documentation build experience without assembling their own toolchain.

Adoption is uneven: recent module repositories use `docs-as-code` v4.x, while older repositories still reference v1.x–v3.x or do not use the shared tooling at all. This version spread mirrors the broader synchronization challenge described in [chapter 1](01-source-code-infrastructure.md#synchronization-mechanisms). Good documentation infrastructure should also let contributors preview and validate changes without waiting for a remote publishing pipeline.

**Biggest gap**: `docs-as-code` version adoption is fragmented, and fast local preview and validation workflows are not yet consistently documented across documentation-producing repositories.

---

## 9.2 Build, Validation & Publishing 🟡

*Infrastructure for builds, quality checks, and publication of documentation sites.*

**S-CORE**

Documentation build infrastructure should be versioned, reproducible, and reviewable like any other engineering toolchain. [eclipse-score/docs-as-code](https://github.com/eclipse-score/docs-as-code) is the shared build tooling that most module repositories are expected to consume. It is distributed through the Bazel registry and provides Sphinx-based documentation builds including traceability extensions. The CI side is handled by the reusable `docs.yml` and `docs-verify.yml` workflows in [eclipse-score/cicd-workflows](https://github.com/eclipse-score/cicd-workflows).

This infrastructure documentation site uses `docs-as-code` with the standard Bazel-based Sphinx build, consistent with the rest of the S-CORE ecosystem. While it does not currently define traceability need objects, the infrastructure is in place to add them when needed.

**Biggest gap**: not all documentation-producing repositories follow one shared toolchain and publication pattern. The `docs-as-code` version spread (v1.x through v4.x across repositories) means repositories do not reliably share the same documentation capabilities.

### 9.2.1 Deterministic Build and Configuration 🟡

*Ensuring reproducible documentation output across local and CI environments.*

**S-CORE**

- Tooling and site configuration should live in version control so contributors can reproduce the published result locally and in CI.
- **Biggest gap**: documentation toolchain choices and configuration practices are not yet aligned across S-CORE documentation surfaces.

### 9.2.2 Validation, Previews, and Publishing 🟡

*Providing contributor feedback before merge through fast preview and validation workflows.*

**S-CORE**

Documentation quality depends on catching structural problems before they reach the published site. Strict builds are the first line of defense: running the site generator in strict mode surfaces broken internal links, invalid markup, and missing navigation entries during CI rather than after publication. Beyond strict builds, dedicated structural checks can validate concerns that the site generator itself does not enforce, such as external link reachability, heading hierarchy consistency, required metadata fields, and naming conventions for files or anchors.

These checks should run as part of the normal pull-request workflow so that contributors get feedback before merge. The important design choice is where the check definitions live. Checks that apply to all S-CORE documentation repositories belong in shared reusable workflows described in [section 7.2](07-automation-integration.md#reusable-workflows), while repository-specific validation rules can stay local. Both should produce clear, actionable output rather than noisy warnings that contributors learn to ignore.

Publishing should be an explicit, reproducible stage of the docs pipeline rather than an undocumented side effect. A contributor should be able to run the same validation locally before pushing, so the tooling must not depend on CI-only infrastructure.

**Biggest gap**: validation depth, preview availability, and publishing ownership are not yet consistent across repositories. Structural checks beyond strict builds are not yet defined as a shared capability.

---

## 9.3 Cross-Repository Documentation Integration 🔴

*Connecting documentation across repositories with stable linking and navigation patterns.*

**S-CORE**

- Contributors and stakeholders should be able to move across repository boundaries without losing context.
- **Biggest gap**: there is no shared information architecture for how repository-local documentation fits into a broader S-CORE documentation landscape.

### 9.3.1 Cross-Repository Linking 🔴

*Establishing reliable links across repository boundaries and release versions.*

**S-CORE**

- Stable links are required if documentation, code, requirements, and release artifacts live in different repositories.
- For integrated views produced from `reference_integration`, those links should resolve within one explicit `known_good` snapshot rather than silently mixing repository heads.
- **Biggest gap**: no agreed cross-repository linking strategy exists for versioned and unversioned documentation content.

### 9.3.2 Shared Navigation and Discovery 🔴

*Making documentation content easier to discover across repository-specific sites.*

**S-CORE**

When documentation is spread across repository-specific sites, the first problem is knowing where to look. A contributor searching for "how do I add a Bazel module" should not need to guess whether the answer lives in the platform documentation, the build infrastructure site, or a module repository's own pages. The same applies to consumers who want to understand what S-CORE offers before they start integrating.

Shared entry points address this by giving readers a starting location that links outward. The simplest version is an overview page or hub site that indexes the major documentation surfaces and describes what each one covers. A more structured version adds cross-site navigation elements — shared headers, breadcrumbs, or sidebar links — so that readers who land on one repository's site can see where related content lives without returning to the hub. The design choice is how tightly to couple this: a lightweight hub with stable links is easy to maintain, while deeper navigation integration requires coordination whenever a repository restructures its pages.

For S-CORE, the practical starting point is the main [eclipse-score.github.io](https://eclipse-score.github.io/score) site, which already serves as a project-level entry. But the path from that entry to repository-specific documentation is not yet systematic: some repositories are linked, others are not, and the reader has no way to know what exists without browsing GitHub directly. A shared navigation pattern would define which documentation surfaces are expected to appear, how they are categorized, and where the canonical index lives so that new repositories automatically become discoverable when they follow the pattern.

**Biggest gap**: repository-specific sites still feel isolated because no common navigation and discovery pattern ties them together. There is no defined standard for how new documentation surfaces register themselves in a project-wide index.

---

## 9.4 Engineering Documentation & Traceability 🟠

*Infrastructure supporting requirements, architecture, design, and links to implementation and tests.*

**S-CORE**

- Engineering documentation (requirements, architecture, detailed design) is required for process compliance (e.g. ISO 26262, ASPICE).
- Architecture visualization and code integration are target capabilities to connect documentation with implementation artifacts.
- Test evidence itself is produced in [chapter 4](04-testing-infrastructure.md); this chapter focuses on the documentation and traceability structures that should consume that evidence.
- **Biggest gap**: traceability and engineering evidence exist in parts, but the supporting model and tooling are not yet standardized across repositories and verification flows.

### 9.4.1 Traceability, Code Integration, and Impact Analysis 🟠

*Linking requirements, design, code, and verification artifacts to support impact analysis.*

**S-CORE**

Traceability needs explicit object models and stable identifiers, not just linked prose. In a docs-as-code setting, that means requirements, design decisions, and verification references should be machine-readable documentation objects with typed relationships rather than free-form text that happens to mention a requirement ID.

The Sphinx ecosystem provides this through extensions that let authors declare typed objects directly in documentation source and express relationships between them. Those objects can then be queried, filtered, and rendered as traceability matrices, coverage tables, or impact analysis views without maintaining a separate database. The important property is that the traceability data lives in version control alongside the prose, follows the same review process, and can be validated during the documentation build.

For S-CORE, the practical value is that test evidence produced in [chapter 4](04-testing-infrastructure.md#test-traceability) can be linked back to requirement objects in documentation, creating a verification chain from requirement through implementation to test result. When requirements change between releases, the same object model makes it possible to identify which links break, which tests need re-evaluation, and which verification evidence is stale. That is the versioning dimension: requirement objects should carry version identity so that a documentation build for one `known_good` snapshot can show the requirement state at that point, while a diff between snapshots shows what changed.

**Biggest gap**: the tooling direction for docs-as-code traceability exists but is not yet named, standardized, or integrated into the documentation build pipeline across S-CORE repositories. Requirement versioning across releases is not yet addressed.

### 9.4.2 Known-Good Documentation Snapshots 🔴

*Tying integrated docs and traceability evidence to one validated cross-repository snapshot.*

**S-CORE**

Cross-repository documentation becomes ambiguous unless readers can tell which combination of component revisions it describes. The `known_good` concept solves that by giving integrated documentation, verification summaries, and traceability views one shared snapshot identifier. A single documentation build in `reference_integration` should therefore describe one concrete `known_good` manifest or record, not an unspecified mix of module heads.

Under the currently assumed but still-undecided Option 2 model, this identifier is also what allows the project to claim that integrated docs and integrated evidence were generated from the same centrally validated stack. If `reference_integration` later ends up with a lighter scope, the documentation benefit remains, but the traceability story has to distinguish more clearly between centrally generated pages and evidence linked in from module repositories.

The important architectural point is that links, release notes, dashboards, and archived evidence should all resolve back to the same `known_good` identifier. **Biggest gap**: S-CORE does not yet have a documented rule for binding integrated documentation and traceability artifacts to one explicit cross-repository snapshot.

This snapshot-oriented documentation view depends on the same integration model described in [DR-002-Infra](https://eclipse-score.github.io/score/main/design_decisions/DR-002-infra.html) and on the still-unsettled `reference_integration` scope discussion in [DR-008-Int](https://github.com/qorix-group/score/blob/da4ea900f1eece5c8e795697d71e277446dca84e/docs/design_decisions/DR-008-int.rst?plain=1).
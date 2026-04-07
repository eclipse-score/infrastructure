# 9 Documentation & Traceability ⚪

*Infrastructure supporting engineering documentation across S-CORE repositories.*

⚠️ This chapter is not yet reviewed by documentation experts.

**S-CORE**

- Documentation infrastructure in S-CORE currently spans repository documentation sites and engineering-focused docs-as-code capabilities.
- Documentation is published through CI-driven static site generation and hosting.
- Engineering traceability (requirements, architecture, design, implementation, tests) is a target capability for functional safety compliance.
- **Biggest gap**: shared documentation conventions, cross-repository navigation, and traceability integration are not yet defined as one coherent project-wide capability.

## 9.1 Authoring & Tooling ⚪

*Capabilities for writing, structuring, and maintaining documentation in repositories.*

**S-CORE**

- Documentation is authored in version-controlled repositories alongside source code.
- Markdown and rST are the primary input formats.
- **Biggest gap**: authoring conventions and required documentation structure are not yet standardized across S-CORE repositories.

### 9.1.1 IDE & Developer Experience

*Providing fast feedback while authoring documentation locally.*

**S-CORE**

- Good documentation infrastructure should let contributors preview and validate changes without waiting for a remote publishing pipeline.
- **Biggest gap**: fast local preview and validation workflows are not yet consistently documented across documentation-producing repositories.

---

## 9.2 Build, Validation & Publishing ⚪

*Infrastructure for builds, quality checks, and publication of documentation sites.*

**S-CORE**

- Documentation build infrastructure should be versioned, reproducible, and reviewable like any other engineering toolchain.
- The current infrastructure documentation site in this repository uses MkDocs, `uv`, strict builds, and GitHub Pages, providing a concrete example of the tooling direction.
- **Biggest gap**: not all documentation-producing repositories follow one shared toolchain and publication pattern.

### 9.2.1 Deterministic Build and Configuration

*Ensuring reproducible documentation output across local and CI environments.*

**S-CORE**

- Tooling and site configuration should live in version control so contributors can reproduce the published result locally and in CI.
- **Biggest gap**: documentation toolchain choices and configuration practices are not yet aligned across S-CORE documentation surfaces.

### 9.2.2 Validation, Previews, and Publishing

*Providing contributor feedback before merge through fast preview and validation workflows.*

**S-CORE**

- Strict documentation builds catch broken links, invalid markup, and navigation issues before publication.
- Publishing should be an explicit, reproducible stage of the docs pipeline rather than an undocumented side effect.
- **Biggest gap**: validation depth, preview availability, and publishing ownership are not yet consistent across repositories.

---

## 9.3 Cross-Repository Documentation Integration ⚪

*Connecting documentation across repositories with stable linking and navigation patterns.*

**S-CORE**

- Contributors and stakeholders should be able to move across repository boundaries without losing context.
- **Biggest gap**: there is no shared information architecture for how repository-local documentation fits into a broader S-CORE documentation landscape.

### 9.3.1 Cross-Repository Linking

*Establishing reliable links across repository boundaries and release versions.*

**S-CORE**

- Stable links are required if documentation, code, requirements, and release artifacts live in different repositories.
- **Biggest gap**: no agreed cross-repository linking strategy exists for versioned and unversioned documentation content.

### 9.3.2 Shared Navigation and Discovery

*Making documentation content easier to discover across repository-specific sites.*

**S-CORE**

- Shared entry points such as overview pages or hub sites can reduce the need to know the right repository in advance.
- **Biggest gap**: repository-specific sites still feel isolated because no common navigation and discovery pattern ties them together.

---

## 9.4 Engineering Documentation & Traceability ⚪

*Infrastructure supporting requirements, architecture, design, and links to implementation and tests.*

**S-CORE**

- Engineering documentation (requirements, architecture, detailed design) is required for process compliance (e.g. ISO 26262, ASPICE).
- Architecture visualization and code integration are target capabilities to connect documentation with implementation artifacts.
- Test evidence itself is produced in [chapter 4](testing-infrastructure.md); this chapter focuses on the documentation and traceability structures that should consume that evidence.
- **Biggest gap**: traceability and engineering evidence exist in parts, but the supporting model and tooling are not yet standardized across repositories and verification flows.

### 9.4.1 Traceability, Code Integration, and Impact Analysis

*Linking requirements, design, code, and verification artifacts to support impact analysis.*

**S-CORE**

- Traceability needs explicit object models and stable identifiers, not just linked prose.
- **Biggest gap**: links between requirements, code, tests, and impact analysis are still too manual across S-CORE.

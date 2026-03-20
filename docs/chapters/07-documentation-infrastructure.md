# 7 Documentation Infrastructure ⚪

*Infrastructure supporting engineering documentation across S-CORE repositories.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Documentation infrastructure in S-CORE currently spans repository documentation sites and engineering-focused docs-as-code capabilities.
- Documentation is published through CI-driven static site generation and hosting.
- The docs-as-code capability model (Input Format, Build, Configuration, Cross-Repository Linking, Previews & Feedback, IDE & Developer Experience, Architecture Visualization, Code Integration) is used as a reference for this chapter.
- Engineering traceability (requirements, architecture, design, implementation, tests) is a target capability for functional safety compliance.
- **Biggest gap**: no shared capability baseline and rollout path is yet defined across S-CORE repositories.

## 7.1 Authoring & Tooling ⚪

*Capabilities for writing, structuring, and maintaining documentation in repositories.*

**S-CORE**

- Documentation is authored in version-controlled repositories alongside source code.
- Markdown is the primary input format in MkDocs repositories, while docs-as-code capabilities also cover reStructuredText-based workflows.
- **Biggest gap**: authoring conventions, templates, and quality profiles are not consistently defined across repositories.

### 7.1.1 Documentation Stacks and Input Formats

*Defining common source formats and authoring rules for consistent output.*

**S-CORE**

- MkDocs is widely used for repository documentation, while Sphinx/sphinx-needs capabilities are relevant for requirement-centric engineering documentation.
- **Biggest gap**: stack selection criteria and shared metadata conventions are not yet standardized.

### 7.1.2 IDE & Developer Experience

*Providing fast feedback while authoring documentation locally and in CI.*

**S-CORE**

- Local preview and linting workflows are available in some repositories (for example via `mkdocs serve` and CI checks).
- **Biggest gap**: no common baseline for editor integration, linting, and author feedback loops exist across S-CORE.

---

## 7.2 Build, Validation & Publishing ⚪

*Infrastructure for deterministic builds, quality checks, and publication of documentation sites.*

**S-CORE**

- Documentation CI pipelines build and publish documentation sites on merge to the default branch.
- Strict mode and link checks are the preferred validation baseline.
- **Biggest gap**: deterministic build configuration and validation strictness are not yet standardized across all repositories.

### 7.2.1 Deterministic Build and Configuration

*Ensuring reproducible documentation output across local and CI environments.*

**S-CORE**

- Reproducible builds with version-controlled configuration are the target baseline across local and CI environments.
- MkDocs `build --strict` is the recommended command in repositories using MkDocs.
- **Biggest gap**: pinned toolchain and shared configuration patterns are not consistently enforced.

### 7.2.2 Validation, Previews, and Publishing

*Providing contributor feedback before merge through fast preview and validation workflows.*

**S-CORE**

- Pull-request previews and early validation are target capabilities for documentation repositories.
- **Biggest gap**: preview generation, broken-link scanning, and release publishing checks are not consistently implemented across S-CORE.

---

## 7.3 Cross-Repository Documentation Integration ⚪

*Connecting documentation across repositories with stable linking and navigation patterns.*

**S-CORE**

- Cross-repository linking for latest and versioned documentation is a key capability for platform-scale documentation.
- **Biggest gap**: no shared cross-repository linking, validation, and discovery standard is applied across S-CORE documentation sites.

### 7.3.1 Cross-Repository Linking

*Establishing reliable links across repository boundaries and release versions.*

**S-CORE**

- Links between repositories are mostly ad hoc and not centrally governed.
- **Biggest gap**: no shared mechanism verifies latest and versioned cross-repository links at scale.

### 7.3.2 Shared Navigation and Discovery

*Making documentation content easier to discover across repository-specific sites.*

**S-CORE**

- Repository sites are published independently, which supports ownership but fragments discovery.
- **Biggest gap**: no common cross-repository navigation, search, and information architecture exists.

---

## 7.4 Engineering Documentation & Traceability ⚪

*Infrastructure supporting requirements, architecture, design, and links to implementation and tests.*

**S-CORE**

- Engineering documentation (requirements, architecture, detailed design) is required for ISO 26262 / ASPICE compliance.
- Architecture visualization and code integration are target capabilities to connect documentation with implementation artifacts.
- **Biggest gap**: no shared tooling and process baseline for engineering documentation and traceability exists across S-CORE.

### 7.4.1 Engineering Artifact Baseline

*Standardizing core engineering documentation artifacts needed for compliance and collaboration.*

**S-CORE**

- Engineering documentation artifacts exist in repositories but vary significantly in structure and level of detail.
- **Biggest gap**: no shared templates or governance model defines a minimum artifact baseline.

### 7.4.2 Traceability, Code Integration, and Impact Analysis

*Linking requirements, design, code, and verification artifacts to support impact analysis.*

**S-CORE**

- Traceability from requirements through implementation and tests is a compliance requirement for functional safety certification.
- **Biggest gap**: traceability is largely manual; no shared toolchain supports automated code linkage, impact analysis, and visualization across repositories.

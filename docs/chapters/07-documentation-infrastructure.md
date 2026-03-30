# 7 Documentation Infrastructure ⚪

*Infrastructure supporting engineering documentation across S-CORE repositories.*

⚠️ This chapter is under construction currently and should be treated as WIP ⚠️

**S-CORE**

- Documentation infrastructure in S-CORE currently spans repository documentation sites and engineering-focused docs-as-code capabilities.
- Documentation is published through CI-driven static site generation and hosting.
- Engineering traceability (requirements, architecture, design, implementation, tests) is a target capability for functional safety compliance.

## 7.1 Authoring & Tooling 🟡

*Capabilities for writing, structuring, and maintaining documentation in repositories.*

**S-CORE**

- Documentation is authored in version-controlled repositories alongside source code.
- Markdown and rST are the primary input formats.
- Rendering of documentation via Sphinx.
- Allow for plantuml & meermaid diagrams to be used. 

### 7.1.1 IDE & Developer Experience 🟡

*Providing fast feedback while authoring documentation locally.*

**S-CORE**
- Providing live-preview capabilities of documentation 🟢
- Providing warnings/errors etc. during build time from sphinx extensions 🟢
- Providing live warnings/errors etc. from sphinx language server 🟡

---

## 7.2 Build, Validation & Publishing 🟠

*Infrastructure for builds, quality checks, and publication of documentation sites.*

### 7.2.1 Deterministic Build and Configuration 🟠

*Ensuring reproducible documentation output across local and CI environments.*

**S-CORE**
- Using bazel build system to ensure deterministic and reproducible builds

### 7.2.2 Validation, Previews, and Publishing 🟡
*Providing contributor feedback before merge through fast preview and validation workflows.*

**S-CORE**

- Compliance, where possible, enforced automatically through metamodel definitions 🟢
- Providing rendered documentation of PR's 🟢
- Availability to link against specific versions of requirements 🔴

---

## 7.3 Cross-Repository Documentation Integration ⚪

*Connecting documentation across repositories with stable linking and navigation patterns.*

### 7.3.1 Cross-Repository Linking 🟢

*Establishing reliable links across repository boundaries and release versions.*

**S-CORE**

- Enabel integration of external projects documentation into own documentation

### 7.3.2 Shared Navigation and Discovery 🟢

*Making documentation content easier to discover across repository-specific sites.*

- Enable referenze-integration build which allows bi-directional linking of needs etc.

---

## 7.4 Engineering Documentation ⚪
*Infrastructure supporting requirements, architecture, design, and links to implementation and tests.*

**S-CORE**

- Engineering documentation (requirements, architecture, detailed design) is required for process compliance (e.g. ISO 26262, ASPICE).
- Architecture visualization and code integration are target capabilities to connect documentation with implementation artifacts.


## 7.5 Traceability 🟡

### 7.5.1 Traceability, Code Integration, and Impact Analysis 🟡
*Linking requirements, design, code, and verification artifacts to support impact analysis.*


**S-CORE**

- Possible to link source code to needs 🟢
- Possible to link test cases to needs 🟢
- Creation of 'external' needs for test cases via XML file parsing 🟢
    => This allows for statistics to be done on those test cases
- Availability to link against specific versions of requirements 🔴


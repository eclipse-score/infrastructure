# 7 Documentation Infrastructure ⚪

*Infrastructure supporting engineering documentation across S-CORE repositories.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- MkDocs is the standard documentation framework for S-CORE repositories that publish documentation sites.
- Documentation is published to GitHub Pages via CI pipelines.
- Engineering traceability (requirements, architecture, design) is a target capability for functional safety compliance.
- **Biggest gap**: traceability infrastructure and cross-repository documentation standards are not yet in place.

## 7.1 Documentation Tooling ⚪

*Tools and frameworks for writing and publishing S-CORE documentation.*

**S-CORE**

- MkDocs with the ReadTheDocs theme is the standard documentation framework.
- **Biggest gap**: tooling standardization is informal; not all repositories adopt the same documentation stack.

### 7.1.1 Documentation Framework

*Frameworks for generating documentation sites across S-CORE repositories.*

**S-CORE**

- MkDocs generates static documentation sites deployed to GitHub Pages.
- **Biggest gap**: MkDocs configuration standards and shared plugin sets are not uniformly defined.

### 7.1.2 Documentation Authoring

*Infrastructure supporting contributors in writing and reviewing documentation.*

**S-CORE**

- Documentation is authored as Markdown in version-controlled repositories alongside code.
- **Biggest gap**: authoring conventions, templates, and contributor guidance are not consistently available across S-CORE.

---

## 7.2 Documentation Pipelines ⚪

*Automating documentation builds, validation, and publishing in CI.*

**S-CORE**

- Documentation CI pipelines build and publish MkDocs sites on merge to the default branch.
- **Biggest gap**: strict mode builds and link validation are not uniformly enforced across S-CORE documentation pipelines.

### 7.2.1 Documentation Build

*Building documentation sites in CI pipelines.*

**S-CORE**

- MkDocs `build --strict` is the recommended build command, used in this and some other S-CORE repositories.
- **Biggest gap**: documentation build pipelines and strict mode are not consistently configured across repositories.

### 7.2.2 Documentation Validation

*Validating documentation quality in CI pipelines.*

**S-CORE**

- Broken link checking and strict mode catch documentation issues before publication.
- **Biggest gap**: automated quality validation is missing from most S-CORE documentation pipelines.

---

## 7.3 Engineering Documentation ⚪

*Infrastructure supporting functional safety engineering documentation: requirements, architecture, and design.*

**S-CORE**

- Engineering documentation (requirements, architecture, detailed design) is required for ISO 26262 / ASPICE compliance.
- **Biggest gap**: no shared tooling or process for engineering documentation exists across S-CORE; this is a significant open area.

### 7.3.1 Requirements Documentation

*Infrastructure supporting requirement documentation for S-CORE components.*

**S-CORE**

- Requirements documentation tooling and processes are not yet standardized across S-CORE.
- **Biggest gap**: no shared requirements format, tooling, or cross-repository requirements database exists.

### 7.3.2 Architecture Documentation

*Infrastructure supporting architecture documentation for S-CORE components.*

**S-CORE**

- Architecture documentation is published as MkDocs-based sites in individual repositories.
- **Biggest gap**: no shared architecture documentation template or cross-repository architecture view exists.

### 7.3.3 Detailed Design Documentation

*Infrastructure supporting detailed design documentation for S-CORE components.*

**S-CORE**

- Detailed design documentation tooling and conventions are not yet standardized.
- **Biggest gap**: no shared format or tooling for detailed design documentation is defined across S-CORE.

---

## 7.4 Contributor Documentation ⚪

*Infrastructure supporting project contributors across S-CORE repositories.*

**S-CORE**

- Contributor documentation covering development setup, workflows, and contribution processes is expected in all S-CORE repositories.
- **Biggest gap**: contributor documentation quality and completeness vary significantly across S-CORE repositories.

### 7.4.1 Development Setup

*Documenting how to set up the development environment for S-CORE repositories.*

**S-CORE**

- Development setup documentation refers contributors to the devcontainer and relevant tooling.
- **Biggest gap**: consistent, tested development setup guides are missing from many S-CORE repositories.

### 7.4.2 Contribution Guides

*Documenting contribution processes and standards.*

**S-CORE**

- Contribution guides cover pull request workflows, coding standards, and review expectations.
- **Biggest gap**: contribution guide completeness and cross-repository consistency are not monitored.

---

## 7.5 Traceability Infrastructure ⚪

*Infrastructure supporting engineering traceability across requirements, design, implementation, and tests.*

**S-CORE**

- Traceability from requirements through implementation and tests is a compliance requirement for functional safety certification.
- **Biggest gap**: no S-CORE-wide traceability tooling or cross-repository traceability infrastructure exists.

### 7.5.1 Requirement Traceability

*Linking requirements with implementation and verification artifacts.*

**S-CORE**

- Requirement-to-implementation and requirement-to-test traceability tooling is not yet operational in S-CORE.
- **Biggest gap**: no shared traceability toolchain is available or mandated.

### 7.5.2 Change Impact Analysis

*Analyzing the impact of changes across engineering artifacts.*

**S-CORE**

- Change impact analysis is performed manually; no automated cross-artifact impact tooling exists.
- **Biggest gap**: automated change-to-requirement and change-to-test impact analysis is absent.

### 7.5.3 Traceability Visualization

*Visualizing traceability relationships across S-CORE engineering artifacts.*

**S-CORE**

- No traceability visualization infrastructure exists across S-CORE.
- **Biggest gap**: no dashboard or tooling renders cross-artifact traceability relationships.

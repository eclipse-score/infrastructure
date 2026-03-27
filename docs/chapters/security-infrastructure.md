# 11 Security Infrastructure ⚪

*Infrastructure for managing security aspects of the S-CORE development and release process.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- Security infrastructure covers secret management, security scanning (SAST, supply chain), and artifact verification.
- GitHub's native security features (secret scanning, Dependabot, code scanning) provide a baseline.
- **Biggest gap**: a coherent, cross-repository security infrastructure strategy is not yet defined for S-CORE.

## 11.1 Secret Management ⚪

*Infrastructure for managing credentials and secrets used in S-CORE pipelines.*

**S-CORE**

- Secrets are stored in GitHub repository and organization secrets; access is scoped to the workflows that require them.
- **Biggest gap**: no secret rotation process, audit trail, or centralized secret lifecycle management exists across S-CORE.

---

## 11.2 Security Scanning ⚪

*Infrastructure for detecting security vulnerabilities in S-CORE code and dependencies.*

**S-CORE**

- GitHub's built-in code scanning (CodeQL) and secret scanning are available to S-CORE repositories.
- **Biggest gap**: security scanning adoption and configuration are inconsistent across S-CORE repositories.

### 11.2.1 SAST

*Static application security testing for S-CORE code.*

**S-CORE**

- CodeQL and similar SAST tools are available via GitHub Actions for S-CORE repositories.
- Shared analyzer delivery, execution patterns, and rule-baseline governance overlap with the broader static-analysis capability described in [chapter 4](static-analysis-infrastructure.md).
- Security-specific ownership remains here: SAST policy, risk handling, triage expectations, and required security gates.
- **Biggest gap**: SAST-specific configuration and required security gate policies are not yet standardized across repositories.

### 11.2.2 Secret Scanning

*Detecting secrets inadvertently committed to S-CORE repositories.*

**S-CORE**

- GitHub's secret scanning detects common credential patterns in S-CORE repository code automatically.
- **Biggest gap**: custom secret patterns and push protection configuration are not uniformly enabled.

### 11.2.3 Supply Chain Security

*Infrastructure addressing software supply chain threats in S-CORE.*

**S-CORE**

- Dependency pinning (hash-based) for CI actions and build dependencies reduces supply chain risk.
- **Biggest gap**: SLSA build provenance and artifact signing are not yet operational for S-CORE releases.

---

## 11.3 Artifact Verification ⚪

*Infrastructure for verifying the authenticity and integrity of S-CORE release artifacts.*

**S-CORE**

- Artifact verification (checksums, signatures) for published S-CORE releases is not yet systematically implemented.
- **Biggest gap**: no artifact signing or verification mechanism is integrated into S-CORE release pipelines.

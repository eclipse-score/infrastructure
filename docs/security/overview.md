# Security & Compliance Platform

## Purpose

Provide practical controls and visibility for license, vulnerability, and software composition concerns.

## Why It Matters In S-CORE

Compliance-related topics are part of normal engineering workflows in S-CORE. License scanning, vulnerability management, and SBOM workflows support traceability and safer delivery decisions.

## Main Tools

- license scanning workflows
- vulnerability scanning and triage workflows
- SBOM generation and processing tooling
- GitHub-native security features where enabled

## Scope

- license and dependency compliance workflows
- vulnerability triage and follow-up handling
- SBOM generation and usage expectations
- reporting inputs for governance and oversight

## Boundaries

- does not make formal compliance claims beyond documented implementation
- does not replace repository-level code security reviews
- depends on build, CI/CD, and artifact metadata quality

## Common Work Topics

- improving scan visibility and triage clarity
- linking findings to dependency and artifact workflows
- documenting exception and escalation handling
- clarifying SBOM generation and consumption paths

## Related Guides

- [License compliance and SBOM](../guides/license-compliance-and-sbom.md)
- [Artifact publishing](../guides/artifact-publishing.md)

## Related Work Packages

- [Security & Compliance work packages](../work-ahead/work-breakdown-structure.md#wbs-security)

## Related Platform Areas

- [Build Platform](../build/overview.md)
- [Artifact Platform](../artifacts/overview.md)
- [Platform Operations](../operations/overview.md)
# Security & Compliance Infrastructure

## Short summary

Security & Compliance Infrastructure covers how license, vulnerability, and SBOM concerns are integrated into S-CORE engineering workflows.

## Why this area matters in S-CORE

Safety and compliance stakeholders need transparent and traceable infrastructure controls. Engineering teams need practical workflows that keep these concerns part of normal delivery work.

## Scope

- license scanning integration
- vulnerability scanning and triage workflows
- SBOM generation and consumption expectations
- compliance-related reporting inputs

## Boundaries / what is not covered here

- formal compliance certification claims beyond documented implementation
- repository-specific secure coding guidance
- incident response ownership outside compliance workflows

## Main tools and technologies

- workflow-integrated license and dependency scanning
- vulnerability scanning and triage tooling
- SBOM generation tooling and artifact metadata flows
- GitHub-native security capabilities where enabled

## Current state

Controls are used in parts of the infrastructure, but rollout and reporting maturity are incomplete. This area remains under active development.

## Key work packages

- improve license scanning rollout consistency
- improve vulnerability triage ownership and process clarity
- define shared SBOM usage and reporting expectations
- strengthen compliance reporting paths for stakeholders

## How contributors can help

- improve compliance automation in reusable workflows
- document triage decisions and ownership boundaries
- improve SBOM generation and consumption guidance
- reduce manual compliance data collection steps

## Related guides

- [License compliance and SBOM](../../guides/license-compliance-and-sbom.md)
- [Artifact publishing](../../guides/artifact-publishing.md)

## Related architecture pages

- [Infrastructure model](../../architecture/infrastructure-model.md)
- [Tool landscape](../../architecture/tool-landscape.md)
- [Cross-cutting concerns](../../architecture/cross-cutting-concerns.md)

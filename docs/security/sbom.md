# SBOM

Software bill of materials work covers how the project represents the composition of software artifacts and how that information can be generated, reviewed, and reused.

## Purpose

An SBOM makes software composition more transparent. It can support security analysis, compliance-related review, and downstream traceability when artifacts are shared across repositories or release stages.

## Scope

This topic includes:

- which artifacts should have SBOM coverage
- where SBOM data is generated in the delivery flow
- how SBOM outputs relate to build and artifact metadata
- how contributors and reviewers are expected to use that information

## Relevant Tools

- SBOM generation or processing tooling
- build metadata from Bazel-based workflows
- CI/CD steps that attach or retain SBOM-related outputs

## Current Context

SBOM tooling is relevant in the S-CORE infrastructure landscape, but the exact generation model, format choices, and publication expectations may still be evolving. Documentation should reflect current implementation and clearly mark areas that remain future decisions.

## Typical Work Items

- define which pipeline stages should generate SBOM data
- connect SBOM outputs to published artifacts where useful
- document consumers of SBOM information and expected review use cases
- avoid duplicate or conflicting sources of composition data

## Why It Matters

SBOM practices improve transparency and strengthen traceability across build, artifact, and security workflows. They are especially useful when the project needs to explain not only what was built, but also what it contains.
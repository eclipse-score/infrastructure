# Capability Map

The S-CORE technical infrastructure is documented along major platform capabilities rather than by individual repositories or tools.

This model helps in three ways:

- It gives contributors a stable orientation even when specific implementations evolve.
- It makes it easier to identify ownership, gaps, and useful contribution areas.
- It provides a structure that can later support progress tracking without turning the documentation into a status spreadsheet.

The approach is inspired by common software delivery platform and platform engineering capability maps. The aim is practical orientation, not a formal maturity model.

## Capability Overview

| Capability | Summary | Primary tools and technologies | Notes |
| --- | --- | --- | --- |
| Source Platform | Manages source collaboration, repository structure, policies, and baseline standards across a multi-repository setup. | GitHub, Otterdog | GitHub is the central collaboration platform. Public organization configuration indicates a high degree of repository standardization and automation through Otterdog. |
| Build Platform | Provides build logic, dependency resolution, and reproducible build behavior across repositories. | Bazel, Bazel registry, Bzlmod | Bazel is an important build technology in S-CORE. Registry and module workflows exist and appear to be evolving as part of the infrastructure landscape. |
| CI/CD Platform | Runs validation, integration, and delivery automation in a consistent way across repositories. | GitHub Actions, reusable workflows, GitHub runners, larger runners | Reusable workflows are a visible part of the public infrastructure. Runner strategy is relevant and should be documented as it matures. |
| Artifact Platform | Handles storage, publication, retention, and distribution of build outputs and reusable artifacts. | Bazel registry, GitHub Releases where appropriate | The Bazel registry is a clear part of the platform. Other artifact channels may exist per use case and should be documented cautiously. |
| Testing Platform | Covers how tests are integrated into local workflows and CI, and how results are surfaced to contributors. | Bazel test, pytest, CI test execution | Testing spans unit, integration, and workflow-based validation. The exact test stack can vary by repository. |
| Security & Compliance Platform | Supports license review, vulnerability visibility, SBOM-related activities, and other compliance-oriented controls. | Eclipse Dash license tooling, SBOM tooling, vulnerability scanning, Dependabot where relevant | This area supports compliance-related work without implying formal compliance claims beyond what is actually implemented. |
| Documentation Platform | Treats documentation as part of the delivery system, with versioned content, review, and automated publication. | Markdown, MkDocs for this repo, docs-as-code | This repository uses Markdown and MkDocs. The wider project may also use other documentation tooling where appropriate. |
| Platform Operations | Keeps the infrastructure itself healthy and usable through monitoring, maintenance, upgrades, and incident handling. | Runner operations, maintenance procedures, monitoring, upgrade practices | This capability connects operational reliability with developer experience and governance needs. |

## Why This Model Matters

The capability map is useful because the infrastructure is broader than any single repository or workflow. A contributor might work on repository settings, build definitions, shared CI logic, test reporting, or license scanning, but these still belong to a smaller number of understandable platform areas.

For developers, this reduces the time needed to find the right documentation.

For contributors, it makes it easier to understand the boundaries of a problem and the systems it touches.

For managers and stakeholders, it provides a readable picture of the infrastructure landscape without requiring detailed tool knowledge.
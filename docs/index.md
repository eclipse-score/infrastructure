# S-CORE Technical Infrastructure

!!! warning
	This website is automatically generated and has not been manually reviewed.
	Treat the content as a pure fiction!

This documentation describes the technical infrastructure that supports development, integration, delivery, and operational transparency in the S-CORE project.

It is written as a practical working reference. The intent is not to capture every implementation detail in one place, but to provide enough structure that people can orient themselves, understand how the main capabilities fit together, and identify where they can contribute.

## What This Documentation Is For

This site is intended to help with:

- understanding the infrastructure landscape across the project
- explaining the main platform capabilities in clear, non-marketing language
- onboarding new contributors to infrastructure-related work
- supporting traceability, reproducibility, transparency, and controlled automation
- creating a foundation that can later support architecture details and progress tracking

## Who It Is For

This documentation is written for three overlapping audiences:

- Developers who need to use the platform correctly and understand the available tooling
- Infrastructure contributors who want to improve standards, automation, workflows, or operational practices
- Managers and stakeholders who need a concise overview of what exists, why it matters, and where work is still evolving

## How To Navigate

Use the documentation in this order when you are new to the repository:

1. Start with the [Capability Map](platform/capability-map.md) to understand the overall model.
2. Read the [Working Model](platform/working-model.md) to see how the documentation is meant to be used.
3. Open the overview page of the capability area you care about.
4. Continue into the guide pages for practical topics, boundaries, and common work items.

## Platform Capability Areas

- [Source Platform](source/overview.md): GitHub-based collaboration, repository management, policies, and standards in a multi-repository setup.
- [Build Platform](build/overview.md): Bazel-based builds, dependency management, and build reproducibility.
- [CI/CD Platform](cicd/overview.md): GitHub Actions workflows, reusable pipeline design, and execution infrastructure.
- [Artifact Platform](artifacts/overview.md): Storage, publication, lifecycle, and distribution of build and release outputs.
- [Testing Platform](testing/overview.md): Test execution, framework integration, and feedback from CI.
- [Security & Compliance Platform](security/overview.md): License scanning, vulnerability management, and SBOM-related practices.
- [Documentation Platform](documentation/overview.md): Markdown, MkDocs, docs-as-code workflows, and documentation publishing.
- [Platform Operations](operations/overview.md): Monitoring, maintenance, upgrades, and incident handling for the infrastructure itself.

## Current Approach

The S-CORE infrastructure uses GitHub as the central collaboration platform, Bazel as an important build technology, and GitHub Actions for CI/CD in a multi-repository environment. Other areas, such as artifact handling, compliance support, and documentation publishing, are documented in a way that makes current usage clear while leaving room for evolving implementation details.

When something is still being decided or refined, the documentation states that explicitly rather than presenting assumptions as facts.
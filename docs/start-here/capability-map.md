# Capability Map

The capability map is the stable structural model for S-CORE infrastructure documentation.

Use it to answer: what the platform is and how major capabilities relate.

Use the [Work Breakdown Structure](../work-ahead/work-breakdown-structure.md) to answer: what work exists and what remains.

## Capability Areas

| Capability area | Core purpose | Typical interfaces |
| --- | --- | --- |
| [Source Platform](../source/overview.md) | Repository collaboration model, standards, and policy controls in a multi-repository setup | Build, CI/CD, Documentation, Security |
| [Build Platform](../build/overview.md) | Reproducible builds and dependency modeling with Bazel and Bzlmod | CI/CD, Artifacts, Testing, Security |
| [CI/CD Platform](../cicd/overview.md) | Shared workflow execution and validation automation with GitHub Actions | Source, Build, Testing, Artifacts, Security |
| [Artifact Platform](../artifacts/overview.md) | Storage, lifecycle, and distribution of reusable outputs | Build, CI/CD, Security |
| [Testing Platform](../testing/overview.md) | Test execution, integration, and reporting in local and CI flows | Build, CI/CD, Operations |
| [Security & Compliance Platform](../security/overview.md) | License, vulnerability, and SBOM-related controls and visibility | Build, CI/CD, Artifacts, Operations |
| [Documentation Platform](../documentation/overview.md) | Docs-as-code authoring, validation, and publishing | Source, CI/CD, Operations |
| [Platform Operations](../operations/overview.md) | Monitoring, maintenance, and incident handling for infrastructure reliability | All areas |

## Why This Model Matters

- provides a stable map for managers and safety/compliance-oriented readers
- keeps area ownership and boundaries visible
- reduces navigation overhead for contributors
- supports consistent cross-linking between guides and work packages

## Related Pages

- [Platform Overview](platform-overview.md)
- [Work Breakdown Structure](../work-ahead/work-breakdown-structure.md)
- [Platform model](../architecture/platform-model.md)
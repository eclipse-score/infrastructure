# Contribution Areas

This page helps contributors identify where to help and how to pick a work area.

Use it together with the [Work Breakdown Structure](work-breakdown-structure.md).

## Contribution Map

| Platform area | Typical contribution topics | Best entry point | Coordinate with |
| --- | --- | --- | --- |
| Source Platform | repository setup, onboarding clarity, standards alignment, policy automation | [Repository onboarding](../guides/repository-onboarding.md) | repository maintainers and organization automation owners |
| Build Platform | Bazel usage guidance, dependency workflows, reproducibility improvements | [Bazel and dependencies](../guides/bazel-and-dependencies.md) | build maintainers and CI/CD maintainers |
| CI/CD Platform | reusable workflows, execution model, diagnostics and feedback quality | [CI/CD workflows](../guides/cicd-workflows.md) | CI/CD maintainers and operations maintainers |
| Artifact Platform | publication flow, versioning, retention, consumer guidance | [Artifact publishing](../guides/artifact-publishing.md) | build and release workflow maintainers |
| Testing Platform | test execution patterns, framework integration, reporting clarity | [Testing and reporting](../guides/testing-and-reporting.md) | test owners and CI/CD maintainers |
| Security & Compliance Platform | license workflow clarity, SBOM workflow, vulnerability triage model | [License compliance and SBOM](../guides/license-compliance-and-sbom.md) | security/compliance maintainers |
| Documentation Platform | navigation, guide quality, docs pipeline reliability | [Documentation publishing](../guides/documentation-publishing.md) | documentation maintainers |
| Platform Operations | monitoring, maintenance runbooks, incident handling | [Operations and maintenance](../guides/operations-and-maintenance.md) | platform operations maintainers |

## Good Starting Contributions

- improve ambiguous guide steps
- add missing cross-links between area overviews and work packages
- document known operational procedures with clear boundaries
- clarify ownership expectations where they are implicit

## Contributions That Need Early Coordination

- organization-wide policy changes
- shared workflow and runner model changes
- build-system baseline changes across repositories
- security/compliance controls that affect release decisions

## Related Pages

- [Current focus areas](current-focus-areas.md)
- [Work Breakdown Structure](work-breakdown-structure.md)
- [Guides Overview](../guides/overview.md)
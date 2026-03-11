# Contribution Areas

This page helps new contributors identify where they can help.

Each capability area includes different kinds of work. Some tasks are suitable for onboarding and cleanup work. Others require deeper familiarity with build systems, CI/CD internals, compliance tooling, or operational risk.

## Contribution Guide By Capability

| Capability | Typical work | Examples of useful contributions | Best fit |
| --- | --- | --- | --- |
| Source Platform | Repository templates, organization settings, labels, policies, review flows, baseline automation | Clarify repository standards, improve onboarding docs, align templates, document branch protection or review expectations | Beginners for documentation and cleanup work; experienced contributors and maintainers for org-wide policy changes |
| Build Platform | Bazel rules, module structure, dependency resolution, build reproducibility, performance tuning | Document Bzlmod usage, improve registry guidance, reduce confusing build setup steps, investigate slow or non-reproducible builds | Experienced contributors; maintainers for shared build logic |
| CI/CD Platform | Shared workflows, job composition, caching, runner selection, pipeline reliability | Simplify reusable workflows, reduce duplicated pipeline logic, improve CI feedback quality, document execution requirements | Experienced contributors and infrastructure maintainers |
| Artifact Platform | Publication flow, versioning, retention, release packaging, distribution paths | Clarify when outputs become reusable artifacts, document artifact lifecycle decisions, improve traceability of published outputs | Experienced contributors; maintainers for publication controls |
| Testing Platform | Test integration, CI execution strategy, reporting, flake management | Improve test guidance, document Bazel and pytest integration, make test failures easier to interpret | Beginners for documentation; experienced contributors for framework or CI changes |
| Security & Compliance Platform | License scanning, vulnerability triage, SBOM generation, auditability | Document scan workflows, clarify responsibilities, improve visibility of findings, connect security checks to delivery decisions | Experienced contributors and maintainers |
| Documentation Platform | Structure, navigation, writing standards, docs CI, publishing | Improve page structure, remove duplication, add missing operational guides, strengthen docs review automation | Beginners and experienced contributors |
| Platform Operations | Monitoring, upgrade planning, incident handling, infrastructure maintenance | Write maintenance runbooks, improve operational visibility, document recovery steps, reduce manual operational work | Infrastructure maintainers and experienced contributors |

## Good Starting Points

If you are new to the infrastructure, the most accessible starting points are usually:

- improving documentation where a workflow is hard to understand
- clarifying repository standards and policy explanations
- improving test reporting guidance and failure interpretation
- documenting operational tasks that are currently known only by maintainers

These contributions are valuable because they lower coordination cost and make later automation work easier.

## Areas That Usually Need More Context

The following areas often require broader context before making changes:

- shared Bazel logic and registry workflows
- reusable CI workflow design
- organization-wide repository policy enforcement
- runner strategy, privileged environments, and operational controls
- compliance-related automation that affects release or governance decisions

If you are unsure where a task belongs, start from the [Capability Map](capability-map.md) and then open the overview page for the nearest capability area.
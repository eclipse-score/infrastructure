# Tool Landscape

This page maps the main tools used in the documented S-CORE infrastructure landscape.

## Primary Tools

| Area | Main tools | Why they matter |
| --- | --- | --- |
| Source collaboration | GitHub, Otterdog | GitHub is the central collaboration platform and Otterdog supports organization/repository automation. |
| Build and dependencies | Bazel, Bzlmod, Bazel registry | Build reproducibility and dependency management depend on these technologies. |
| CI/CD | GitHub Actions, reusable workflows, runners, large runners | Shared validation and delivery behavior is implemented through workflow reuse and execution infrastructure. |
| Artifacts | Bazel registry, workflow-managed outputs | Reusable output publication and consumption flows depend on clear artifact paths. |
| Testing | Bazel test, pytest, CI workflow execution | Testing is integrated into local and CI execution paths. |
| Security and compliance | license scanning, SBOM tooling, vulnerability scanning | Compliance-related controls rely on consistent scanning and triage workflows. |
| Documentation | Markdown, MkDocs, uv | Docs-as-code delivery depends on buildable and publishable documentation workflows. |

## Practical Notes

- tool choices are documented based on visible and verified usage
- area pages describe boundaries and expected usage
- guide pages describe concrete workflow steps

## Related Pages

- [Cross-cutting concerns](cross-cutting-concerns.md)
- [Capability Map](../start-here/capability-map.md)
- [Guides Overview](../guides/overview.md)
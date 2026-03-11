# Tool Landscape

This page maps currently used and currently intended tools to the S-CORE infrastructure areas.

The list is intentionally practical and may evolve as infrastructure implementation matures.

| Infrastructure Area | Main Tools And Technologies | Notes |
| --- | --- | --- |
| Source Code Infrastructure | GitHub, Otterdog, repository policy features | GitHub is the central collaboration platform; Otterdog is used for organization and repository automation. |
| Build Infrastructure | Bazel, Bzlmod, Bazel registry | Bazel is a central build technology; dependency and module workflows are still maturing. |
| Integration Infrastructure | GitHub Actions, reusable workflows, GitHub runners and larger runners | Reusable workflows are relevant and actively expanded for cross-repository consistency. |
| Artifact Infrastructure | Bazel registry, workflow-driven publishing | Artifact publication and distribution patterns are evolving. |
| Testing Infrastructure | Bazel test, framework tooling such as pytest, CI test workflows | Testing integration exists, with ongoing improvements in reporting and consistency. |
| Security & Compliance Infrastructure | License scanning, vulnerability scanning, SBOM tooling | Compliance automation is used in parts of the infrastructure and remains under development. |
| Documentation Infrastructure | Markdown, MkDocs, uv | Docs-as-code is an important part of infrastructure transparency and maintainability. |
| Infrastructure Operations | Runner operations, monitoring signals, runbooks | Operational baseline is present but still partially manual. |

## Related Pages

- [Infrastructure model](infrastructure-model.md)
- [Cross-cutting concerns](cross-cutting-concerns.md)
- [Infrastructure Development Map](../infrastructure-development-map.md)

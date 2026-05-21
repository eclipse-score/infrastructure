# S-CORE Infrastructure Landscape

<div class="landing-hero">
  <p class="landing-kicker">Overview, roadmap, contribution guide, and reference</p>
  <h2>Get oriented in the S-CORE infrastructure landscape.</h2>
  <p class="landing-lead">
    This site explains what S-CORE infrastructure is, which shared capabilities and repositories already exist,
    how mature they are, what is still missing, and how a concrete issue or pull request fits into the bigger picture.
    Whether you're asking how we do something, where to look for a topic, or how an issue fits the big picture — start here.
  </p>
</div>

## Where to start

| I want to… | Go to |
|---|---|
| Set up my environment and make my first contribution | [Tutorial: Getting Started](tutorials/getting-started.md) |
| Solve a specific task (build, test, publish, write docs) | [How-to Guides](how-to/index.md) |
| Understand how a piece of infrastructure works or why | [Explanation: Landscape Chapters](explanation/index.md) |
| Look up a command, config value, or repository | [Quick Reference](reference/quick-reference.md) |
| Understand project-specific terminology | [Glossary](reference/glossary.md) |

## Documentation Map

| | **Learning** | **Working** |
|---|---|---|
| **Practical** | [Tutorials](tutorials/getting-started.md) | [How-to Guides](how-to/building.md) |
| **Theoretical** | [Explanation](explanation/index.md) | [Reference](reference/quick-reference.md) |

## Tutorials

Step-by-step lessons for newcomers. Follow along to build understanding.

- [Getting Started](tutorials/getting-started.md) — Set up your environment and run your first build
- [Your First Pull Request](tutorials/first-pull-request.md) — From fork to merged PR, end to end
- [Creating a New Module](tutorials/creating-a-module.md) — Start a new Bazel module from the template
- [Write Your First ITF Integration Test](tutorials/itf-integration-test.md) — Docker-based target testing from scratch

## How-to Guides

Practical recipes for specific tasks. Assumes you already have a working environment.

**For contributors:**

- [Building with Bazel](how-to/building.md) — Registry, dependencies, toolchains, lock files
- [Testing](how-to/testing.md) — Test frameworks, ITF, QNX, coverage, sanitizers
- [Code Quality](how-to/code-quality.md) — Pre-commit, lint policies, copyright headers
- [Publishing Modules](how-to/publishing.md) — Release, registry import, consumer access

**For infrastructure maintainers:**

- [Writing Documentation](how-to/writing-docs.md) — Sphinx/MyST setup, local preview, status markers
- [Update the Devcontainer](how-to/update-devcontainer.md) — Build, publish, and roll out a new shared image
- [Manage CI Secrets](how-to/manage-ci-secrets.md) — Create, rotate, and replace secrets with OIDC
- [Update a Shared Toolchain](how-to/update-toolchain.md) — Bump compiler or policy versions across repositories

## Reference

Factual lookup material. No narrative, just the data you need.

- [Quick Reference](reference/quick-reference.md) — Repositories, commands, links
- [Configuration Reference](reference/configuration.md) — .bazelrc, pre-commit, devcontainer settings
- [CI & Workflow Reference](reference/ci-workflows.md) — Reusable workflow inputs, outputs, and secrets
- [Tool Versions](reference/tool-versions.md) — Version matrix for shared toolchains and images
- [Glossary](reference/glossary.md) — Key terms and project-specific vocabulary

## Explanation

Architecture, design rationale, and maturity assessment of each infrastructure area.

- [Infrastructure Landscape](explanation/index.md) — Chapter map and maturity overview for all 10 areas
- [Design Decisions](explanation/decisions.md) — Key architectural decisions and their rationale
- [4. Testing](explanation/04-testing-infrastructure.md) — ITF, QNX microvm, traceability, coverage
- [9. Documentation & Traceability](explanation/09-documentation-infrastructure.md) — docs-as-code, sphinx-needs, known-good snapshots

→ [All chapters](explanation/index.md)

## Quick Links

<div class="landing-quick-links">

  <p class="landing-section-label">Contributing</p>

  <div class="landing-grid landing-grid-2">
    <a class="landing-card-link" href="https://github.com/eclipse-score/infrastructure/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">
      <p class="landing-link-title">Contributing Guide</p>
      <p class="landing-link-desc">Documentation style, structure, and review checklist for contributors to this site.</p>
    </a>
    <a class="landing-card-link" href="how-to/writing-docs.md">
      <p class="landing-link-title">How to Write Docs</p>
      <p class="landing-link-desc">Bazel + Sphinx/MyST setup, local preview, validation workflow.</p>
    </a>
  </div>

  <p class="landing-section-label">Infrastructure Team</p>

  <div class="landing-grid landing-grid-2">
    <a class="landing-card-link" href="https://github.com/orgs/eclipse-score/discussions/236" target="_blank" rel="noopener">
      <p class="landing-link-title">Meeting Minutes</p>
      <p class="landing-link-desc">Infrastructure team meeting notes on GitHub Discussions.</p>
    </a>
    <a class="landing-card-link" href="https://sdvworkinggroup.slack.com/archives/C0894QGRZDM" target="_blank" rel="noopener">
      <p class="landing-link-title">Slack: #score-infrastructure</p>
      <p class="landing-link-desc">Main channel for infrastructure team discussion.</p>
    </a>
    <a class="landing-card-link" href="https://sdvworkinggroup.slack.com/archives/C08RDRKH5FE" target="_blank" rel="noopener">
      <p class="landing-link-title">Slack: #score-infrastructure-review-requests</p>
      <p class="landing-link-desc">Drop PR links here for review — no comments, just links.</p>
    </a>
    <a class="landing-card-link" href="https://eclipse-score.github.io/.github/" target="_blank" rel="noopener">
      <p class="landing-link-title">Repository Overview</p>
      <p class="landing-link-desc">Cross-repo metrics and status across all eclipse-score repositories.</p>
    </a>
  </div>

  <p class="landing-section-label">S-CORE Project</p>

  <div class="landing-grid landing-grid-2">
    <a class="landing-card-link" href="https://eclipse.dev/score/" target="_blank" rel="noopener">
      <p class="landing-link-title">S-CORE Website</p>
      <p class="landing-link-desc">The main Eclipse S-CORE project website — "Open by Choice. Safe by Design."</p>
    </a>
    <a class="landing-card-link" href="https://eclipse-score.github.io/score/main/handbook" target="_blank" rel="noopener">
      <p class="landing-link-title">S-CORE Handbook</p>
      <p class="landing-link-desc">Technical handbook — processes, tooling, and contribution model.</p>
    </a>
  </div>

</div>

:::{toctree}
:maxdepth: 2
:hidden:

tutorials/index
how-to/index
reference/index
explanation/index
:::

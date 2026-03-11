# Repository Management

Repository management covers how repositories are created, organized, configured, and maintained across the S-CORE GitHub organization.

## Scope

This topic includes:

- repository creation and baseline setup
- repository categorization and ownership structure
- common settings that should be applied consistently
- lifecycle tasks such as archiving, transferring, or reorganizing repositories

It does not cover day-to-day build logic or project-specific application code.

## Relevant Tools

- GitHub organization and repository settings
- Otterdog for repository and organization configuration automation
- repository templates and shared baseline files where available

## Current Context

The public S-CORE organization shows a clearly multi-repository structure with separate repositories for infrastructure, modules, toolchains, and incubation work. Public configuration also indicates that organization-level automation is used to keep repository settings aligned.

That matters because manual repository management does not scale well once reusable workflows, shared policies, and compliance-related controls are involved.

## Typical Work Items

- define what a new repository needs on day one
- align repository metadata, labels, topics, and settings
- make team and review assignment easier to understand
- document how template repositories should be used
- reduce manual drift between repositories over time

## Practical Questions

- What baseline settings should every repository have?
- Which settings are centrally managed and which are repository-specific?
- How should new repositories be categorized and onboarded into shared automation?
- How should repository ownership be visible to contributors?

## Boundaries

Repository management should provide a consistent baseline, but it should not force every repository into identical workflows when technical constraints differ. The goal is controlled standardization, not unnecessary uniformity.
# Maintenance

Maintenance covers the routine work required to keep the platform current, secure, and predictable.

## Scope

This includes:

- upgrading shared tooling such as Bazel, workflow definitions, and supporting automation
- keeping runner and execution environments in a usable state
- updating repository automation and policy configuration
- cleaning up deprecated or obsolete platform components

## Relevant Areas

- Bazel and related build infrastructure
- GitHub Actions reusable workflows
- runner configuration and execution capacity
- Otterdog-managed organization or repository configuration
- documentation and compliance-related automation

## Typical Work Items

- plan version upgrades with minimal disruption
- document maintenance windows or rollout expectations when they matter
- remove deprecated patterns before they become hidden dependencies
- make recurring operational work predictable instead of reactive

## Why It Matters

Maintenance is where infrastructure stays trustworthy over time. It has direct impact on developer productivity, operational stability, and the credibility of compliance-related processes that depend on current tooling and clear change history.
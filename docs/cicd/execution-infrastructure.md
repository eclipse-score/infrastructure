# Execution Infrastructure

Execution infrastructure covers where CI/CD jobs run and how those execution environments are selected, operated, and protected.

## Scope

This includes:

- GitHub runner selection
- larger runner usage where workloads require it
- environment-specific execution constraints
- secrets, permissions, and approval boundaries that affect job execution

## Relevant Tools

- GitHub-hosted runners
- larger runners or other project-managed execution capacity where needed
- GitHub Actions environments and permissions controls

## Current Context

GitHub runners and larger runners are relevant in the S-CORE infrastructure landscape. Public workflow and organization signals also suggest that some jobs may require more controlled execution contexts than a default lightweight validation run.

The exact execution model should be documented with care as it evolves, especially when runner choice affects cost, security, or platform-specific validation.

## Typical Work Items

- decide which jobs can run on standard runners and which need specialized capacity
- document environment requirements for privileged or platform-specific workflows
- make resource-intensive jobs visible so pipeline cost and queue time can be understood
- align runner strategy with security, reliability, and maintenance expectations

## Why It Matters

Execution choices are not only an implementation detail. They influence throughput, failure modes, security boundaries, and the confidence that teams can place in automated validation.
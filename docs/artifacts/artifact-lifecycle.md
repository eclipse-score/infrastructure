# Artifact Lifecycle

Artifact lifecycle management describes how artifacts move from initial creation to publication, retention, replacement, and eventual removal.

## Scope

This topic includes:

- creation of artifacts during CI or release workflows
- versioning and publication decisions
- retention periods and cleanup expectations
- deprecation or replacement of outdated artifacts

## Relevant Tools

- CI/CD workflows
- Bazel registry processes
- repository release mechanisms where used

## Typical Questions

- When does a build output become an artifact that others may depend on?
- What publication step creates a supported artifact rather than a temporary output?
- How long should artifacts be retained?
- How are obsolete artifacts replaced or withdrawn?

## Practical Guidance

Lifecycle documentation should separate temporary pipeline outputs from supported published artifacts. That distinction matters because the governance expectations are different. Temporary outputs support short-term validation, while published artifacts become part of the wider delivery contract.

## Why It Matters

Lifecycle clarity improves reproducibility and reduces confusion about which outputs are safe to consume. It also helps with traceability when teams need to understand which source revision, dependency set, or pipeline run produced a given artifact.
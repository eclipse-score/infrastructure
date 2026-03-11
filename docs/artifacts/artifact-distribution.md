# Artifact Distribution

Artifact distribution covers how reusable outputs are made available to downstream consumers and how those distribution paths are documented.

## Scope

This includes:

- who the consumers of an artifact are
- how artifacts are discovered and consumed
- which distribution channels are considered supported
- what information should accompany distributed artifacts

## Relevant Tools

- Bazel registry consumption workflows
- GitHub Releases where appropriate
- documentation that explains supported consumption patterns

## Typical Work Items

- document how downstream repositories should reference published modules
- clarify when distribution happens automatically versus by an explicit release step
- improve visibility of supported versions and compatibility expectations
- align distribution practices with traceability and review needs

## Boundaries

Distribution guidance should make supported channels explicit. If multiple ways to obtain an artifact exist, the documentation should state which one is authoritative and which ones are convenience paths only.

## Why It Matters

Unclear distribution paths create fragile integrations. Clear distribution guidance makes shared infrastructure easier to adopt and reduces the risk of hidden, unreviewed dependency paths across repositories.
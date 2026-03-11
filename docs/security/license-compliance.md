# License Compliance

License compliance covers how the project identifies, reviews, and tracks licensing information for dependencies and other third-party content.

## Why It Matters

In an open-source and potentially regulated context, license scanning is not optional background work. It helps the project understand what is being consumed, where review may be needed, and whether downstream use remains compatible with project expectations.

## Relevant Tools

- Eclipse Dash license tooling
- dependency metadata from build and registry workflows
- CI checks or review steps that surface license-related findings

## Scope

This topic includes:

- identifying third-party content
- running or reviewing license scans
- handling unclear or exceptional findings
- documenting where license information is expected to come from

## Typical Work Items

- explain when scans run and what they cover
- make scan outputs understandable to contributors
- define escalation paths for unclear findings
- connect license review to dependency management and release readiness

## Practical Principle

License compliance documentation should help contributors answer three questions quickly: what was scanned, what needs attention, and who is expected to act. That keeps the process operational instead of turning it into an opaque gate.
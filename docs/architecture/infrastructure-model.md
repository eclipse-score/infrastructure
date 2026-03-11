# Infrastructure Model

This model describes how S-CORE infrastructure documentation is structured while the infrastructure is still evolving.

It keeps one primary organizing logic: Infrastructure Areas.

## Why This Model Is Used

- It gives contributors and stakeholders one stable way to navigate the infrastructure landscape.
- It separates landscape description from work execution details.
- It supports honest status reporting without pretending all areas are mature.

## Infrastructure Area Slices

| Infrastructure Area | Main Question This Area Answers |
| --- | --- |
| Source Code Infrastructure | How are repositories organized, governed, and maintained? |
| Build Infrastructure | How are builds and dependencies managed reproducibly? |
| Integration Infrastructure | How are pull requests and integration workflows validated automatically? |
| Artifact Infrastructure | How are reusable outputs versioned, stored, and distributed? |
| Testing Infrastructure | How are tests executed and reported across local and CI contexts? |
| Security & Compliance Infrastructure | How are license, SBOM, and vulnerability concerns integrated into workflows? |
| Documentation Infrastructure | How is infrastructure documentation maintained, validated, and published? |
| Infrastructure Operations | How are monitoring, maintenance, and incident handling managed? |

## Model Layers

- **Area layer**: the infrastructure landscape, boundaries, and purpose
- **Work package layer**: current state, active work, and planned work
- **Guide layer**: practical how-to instructions linked to one or more areas
- **Architecture layer**: concepts that apply across multiple areas

## Relationship To Work Packages

Work packages are not a separate navigation backbone. They are execution units connected to infrastructure areas.

- Use [Infrastructure Development Map](../infrastructure-development-map.md) for a concise progress view.
- Use [Work Breakdown Structure](../work-breakdown-structure.md) for detailed status lists.

## Capability View As Supporting Context

Earlier documentation used a capability-map-heavy entry model. That idea remains useful as architecture context, but area-based navigation is now primary for day-to-day usage.

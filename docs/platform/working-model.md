# Working Model

This documentation is intended to be used as a living resource.

It does not assume that every infrastructure decision is already finished. Instead, it provides a structure that can hold both established practices and evolving areas without becoming misleading.

## How To Use The Documentation

Use the documentation in layers:

1. The [Capability Map](capability-map.md) provides orientation.
2. Each capability overview page explains purpose, technologies, responsibilities, and boundaries.
3. Guide pages describe practical topics within that capability area.

This keeps the site readable for people who need an overview while still being useful for contributors who need operational detail.

## Documentation As A Living Resource

The expected working model is docs-as-code:

- documentation is versioned with normal review and change tracking
- changes are incremental and tied to real work
- unclear areas are marked clearly instead of being filled with assumptions
- documentation quality is part of infrastructure quality

This matters because infrastructure is not only a set of tools. It is also the shared understanding that allows people to use those tools safely and effectively.

## What Belongs Here

This repository should describe:

- major platform capabilities and why they exist
- practical operating guidance for contributors and maintainers
- technology choices that shape development and delivery workflows
- boundaries, assumptions, and future decisions where they matter

## What Can Be Added Later

The current focus is structure and useful content. Additional layers can be added later if needed, including:

- architecture decision records
- capability ownership details
- progress tracking for infrastructure initiatives
- service-level objectives or operational metrics
- more detailed runbooks for critical workflows

Those additions should build on this structure rather than replace it.
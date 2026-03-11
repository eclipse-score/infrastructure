# Artifact Storage

Artifact storage covers where artifacts are kept and how contributors should reason about those locations.

## Scope

This includes:

- build outputs retained by CI
- reusable artifacts published for downstream consumption
- metadata associated with published modules or releases
- storage decisions that affect reproducibility and traceability

## Relevant Tools

- Bazel registry infrastructure
- GitHub Releases where suitable
- workflow-managed artifact upload and retention features

## Current Context

The Bazel registry is a clear part of the S-CORE infrastructure landscape and is therefore a primary storage concern for published Bazel modules or related metadata. Other artifact storage patterns may exist at repository level and should be documented only when their role is clear.

## Typical Work Items

- document which outputs are ephemeral CI artifacts and which are intended for reuse
- define what metadata should be stored together with a published artifact
- make artifact locations discoverable for contributors and maintainers
- reduce ad hoc storage patterns that make later automation difficult

## Why It Matters

If artifact storage is unclear, contributors cannot easily answer where an output came from, whether it is reusable, or how long it can be trusted to exist. Clear storage guidance improves developer usability and supports compliance-related needs for traceability and transparency.
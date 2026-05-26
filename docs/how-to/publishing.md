# How to Publish a Module

## Overview

The publishing flow for S-CORE Bazel modules:

1. **GitHub Release** in the module repository (with a semantic version tag)
2. **Registry import** into [eclipse-score/bazel_registry](https://github.com/eclipse-score/bazel_registry)
3. **Consumer resolution** via `MODULE.bazel` dependency declarations

## Create a release

Create a GitHub Release in the module repository with a semantic version tag (e.g. `v1.2.3`). The release assets and source archive serve as the distribution artifact.

## Add to the registry

Follow the instructions in the [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md) to add the new version to the S-CORE Bazel registry.

## Verify consumer discovery

Published modules appear in the [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/). Consumers find available modules and versions there, then add a `bazel_dep()` entry to their `MODULE.bazel`.

## Versioning

Modules use semantic versioning aligned with Git tags. The version in the registry entry matches the Git tag on the GitHub Release.

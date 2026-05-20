# Publishing & Releases

How S-CORE modules are published, versioned, and distributed.

## Module Publication Flow

The release pipeline follows this sequence:

1. A **GitHub Release** is created in the module repository with a semantic version tag
2. The release is **imported into the registry** ([bazel_registry](https://github.com/eclipse-score/bazel_registry))
3. Consumers **resolve the new version** through their `MODULE.bazel` dependency declarations

## Creating a Release

Create a GitHub Release in the module repository:

1. Tag the commit with a semantic version (e.g., `v1.2.0`)
2. Create a GitHub Release from the tag
3. The release artifacts are stored as GitHub Release assets

## Adding to the Registry

After creating a release, add it to the shared Bazel registry. Follow the instructions in the [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md).

## Discovery

Published modules and their available versions are browsable at the [Registry UI](https://eclipse-score.github.io/bazel_registry_ui/).

## Versioning

S-CORE modules follow semantic versioning, aligned with Git tags. The version in `MODULE.bazel` must match the Git tag used for the GitHub Release.

## Container Images

The devcontainer image is published to the GitHub Container Registry:

```
ghcr.io/eclipse-score/devcontainer
```

This image is used by both local development (via `.devcontainer/devcontainer.json`) and CI workflows.

# 2 Developer Environment 🟡

*Infrastructure that provides the local development layer across S-CORE repositories.*

S-CORE needs local infrastructure beyond its main software build flows. IDE integration, language servers, formatters, YAML and workflow linters, documentation helpers, and lightweight validation before CI all need a shared home or they drift from repository to repository.

In S-CORE, Bazel is the central build system for the actual software stack, but many repositories do not use Bazel as their primary local execution model. This chapter therefore documents the shared local layer that spans both repository types, centered on the common [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer). [Chapter 3](03-build-infrastructure.md) owns Bazel toolchains and build evidence, [chapter 5](05-static-analysis-infrastructure.md) owns analyzer baselines, and [chapter 7](07-automation-integration.md) owns CI execution and gating. The central devcontainer gives S-CORE a clear anchor for this area, but the repository-facing conventions around it are not yet fully standardized.

## 2.1 Central Devcontainer 🟠

*Common local environment for shared development tooling across repository types.*

Multi-repository development needs one repeatable local environment for the tools that are not naturally delivered by each repository's own build or test flow. Without that, editor support, formatting, documentation tooling, YAML or workflow linting, and similar surrounding capabilities become repository-specific setup problems instead of shared infrastructure.

S-CORE solves this primarily through the central [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) repository. It builds, tests, and publishes pre-built development-container images, with pinned and preconfigured tools, so repositories can consume one shared local environment instead of maintaining their own setup stacks. 

### 2.1.1 Shared Tool Baseline 🟠

*Defining which surrounding tools are present by default.*

The shared base should contain the local-only and supporting tools that recur across the S-CORE repository landscape. Typical examples are language servers, formatters, YAML and Markdown validators, workflow checks, documentation helpers, and other tools that improve development ergonomics but do not belong to the primary build toolchain model.

In S-CORE, that baseline is currently expressed through the published `ghcr.io/eclipse-score/devcontainer` image family. The central devcontainer repository defines the included tools, pins their versions, and preconfigures them for Eclipse S-CORE development.

### 2.1.2 Repository Consumption 🟡

*Connecting individual repositories to the common environment.*

A central environment only helps if repositories consume it in a predictable way. The infrastructure concern here is not only that an image exists, but that repositories expose the same basic entry path and do not each reinvent how contributors attach to it.

In S-CORE, the concrete mechanism is a checked-in `.devcontainer/devcontainer.json` that points to a versioned image from the central devcontainer. That gives repositories a practical way to consume the shared environment today, but adoption is still uneven across repository classes. Repository integration of the central devcontainer is still inconsistent enough that contributors cannot always assume the same entry path everywhere.

### 2.1.3 IDE And Shell Integration 🟠

*Making the environment usable from editors and terminals.*

The environment is only useful if editors and shells can consume its tools directly. This matters especially for language servers, formatters, and non-build linters, because these integrations often expect real executables and preconfigured settings rather than wrappers around deeper build commands.

In S-CORE, the clearest supported path today is the devcontainer-based workflow in VS Code, and the central devcontainer is explicitly documented for Dev Containers usage. The same containerized environment is also the intended terminal path, so local work does not depend on a separate host setup. Other devcontainer-capable IDEs are possible, but the support story is less explicitly defined. The supported baseline for editor-visible tools and shell entry points is still clearer in practice than it is in project-wide documentation.

## 2.2 Local Auxiliary Tooling 🟡

*Lightweight local checks and helpers that complement repository-specific build flows and CI.*

Not every useful local check should be expressed as part of the main build. Fast repository hygiene checks, text and YAML validation, formatting checks, and similar surrounding tasks benefit from lightweight local delivery instead of waiting for a full build or CI round trip. That is true both for Bazel-based software repositories and for repositories that use different local workflows.

In S-CORE, this auxiliary tooling is currently delivered through a combination of tools present in the central devcontainer and shared hook-based validation. That gives the project a local feedback layer around repository work in general rather than forcing all such checks into Bazel. This local auxiliary layer exists, but it is not yet described and standardized as one coherent cross-repository capability.

### 2.2.1 Pre-commit And Fast Checks 🟠

*Providing quick validation for repository hygiene and non-build assets.*

[pre-commit](https://pre-commit.com/) is a good fit for checks that should fail quickly and early: formatting, text hygiene, YAML validation, workflow checks, and similar lightweight tasks. This is important because such checks are often the first things to drift when repositories have no shared local enforcement path.

In S-CORE, custom hooks are published through [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml) and combined with standard ecosystem hooks. Together with the central devcontainer, that gives repositories a shared mechanism for lightweight local validation before CI. Adoption, hook coverage, and enforcement expectations for these fast checks are still inconsistent across the repository landscape.

### 2.2.2 Boundary To Bazel And CI 🟡

*Clarifying what stays local, what belongs in Bazel, and what remains CI-only.*

The local auxiliary layer needs a clear boundary or repositories will duplicate checks, force unsuitable tasks through lightweight hooks, or blur the line between convenience and authoritative enforcement. The infrastructure question here is not to make every check identical, but to define the right delivery layer for each kind of check.

In S-CORE, the current practical split is that surrounding-tool checks run directly in the shared devcontainer or via pre-commit, while deeper repository-native validation stays with the repository's main build or test flow and final enforcement stays in CI. For "dependable element" repositories that usually means Bazel, but other repositories may use different local execution paths.

Where repositories use dependency lock files such as `uv.lock` or `MODULE.bazel.lock`, the practical local refresh step may still happen through `pre-commit`, but the lock state itself belongs to the repository's dependency model and is therefore described in [chapter 3](03-build-infrastructure.md#326-lock-files).

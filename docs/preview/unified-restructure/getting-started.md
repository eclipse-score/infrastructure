# Getting Started

A step-by-step setup for new contributors to S-CORE module repositories.

## Prerequisites

You need:

- A **GitHub account** with access to the [eclipse-score](https://github.com/eclipse-score) organization
- **VS Code** (or any IDE that supports devcontainers)
- **Docker** (Docker Desktop or Docker Engine)

## 1. Clone a Repository

Pick any S-CORE module repository and clone it:

```bash
git clone https://github.com/eclipse-score/<repository>.git
cd <repository>
```

For example:

```bash
git clone https://github.com/eclipse-score/module_template.git
cd module_template
```

## 2. Open in Devcontainer

Each repository contains a `.devcontainer/devcontainer.json` that references the shared devcontainer image at `ghcr.io/eclipse-score/devcontainer`. This image includes all shared tooling: Bazel, pre-commit, language servers, formatters, and more.

In VS Code:

1. Install the **Dev Containers** extension
2. Open the cloned repository folder
3. When prompted, click **Reopen in Container** (or use the command palette: `Dev Containers: Reopen in Container`)

The container will pull and start automatically.

## 3. Verify Your Environment

Inside the devcontainer terminal, confirm the key tools are available:

```bash
bazel version
python3 --version
pre-commit --version
```

## 4. Build

Build the entire repository:

```bash
bazel build //...
```

## 5. Run Tests

Run all tests:

```bash
bazel test //...
```

## 6. Set Up Pre-commit Hooks

Install the pre-commit hooks so checks run automatically on each commit:

```bash
pre-commit install
```

You can also run all checks manually:

```bash
pre-commit run --all-files
```

## 7. Next Steps

- [Repository Landscape](repository-landscape.md) -- overview of all S-CORE repositories and how they relate
- [Building & Dependencies](building-dependencies.md) -- Bazel configuration, registries, and dependency management
- [Testing](testing.md) -- test frameworks, coverage, and sanitizers
- [Code Quality & Compliance](code-quality.md) -- pre-commit hooks, policies, and licensing
- [CI & Automation](ci-automation.md) -- how CI pipelines work
- [Publishing & Releases](publishing-releases.md) -- releasing modules and container images
- [Documentation](documentation.md) -- writing and building documentation

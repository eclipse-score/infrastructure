# Getting Started

A step-by-step setup walkthrough for new S-CORE contributors.

## Prerequisites

- GitHub account with access to the [eclipse-score](https://github.com/eclipse-score) organization
- [VS Code](https://code.visualstudio.com/) (or another devcontainer-capable IDE)
- [Docker](https://www.docker.com/get-started/) installed and running

## 1. Clone a Repository

```bash
git clone https://github.com/eclipse-score/<repository>.git
cd <repository>
```

Replace `<repository>` with the module you want to work on.

## 2. Open in Devcontainer

Open the cloned repository in VS Code. When prompted, click **Reopen in Container**.

The repository's `.devcontainer/devcontainer.json` points to the shared image `ghcr.io/eclipse-score/devcontainer`, which includes all required tooling: Bazel, Python, pre-commit, language toolchains, and more.

If VS Code does not prompt automatically, open the command palette (`Ctrl+Shift+P`) and select **Dev Containers: Reopen in Container**.

## 3. Verify the Environment

```bash
bazel version
python3 --version
pre-commit --version
```

All three commands should succeed inside the devcontainer.

## 4. Build

```bash
bazel build //...
```

This builds all targets in the repository.

## 5. Run Tests

```bash
bazel test //...
```

This runs all test targets.

## 6. Set Up Pre-commit Hooks

```bash
pre-commit install
```

This configures git hooks that run formatting and hygiene checks before each commit.

To run all checks manually:

```bash
pre-commit run --all-files
```

## Next Steps

- [Quick Reference](quick-reference.md) — Bookmark page with all key repositories, commands, and links
- Check the repository's own `README.md` for module-specific instructions
- [Building with Bazel](building.md) — Registry configuration and dependency management
- [Testing](testing.md) — Test frameworks, coverage, and sanitizers

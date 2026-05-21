# Getting Started

A step-by-step walkthrough for new S-CORE contributors. By the end of this tutorial, you will have a working development environment, a successful build, and passing tests.

## What you'll need

- GitHub account with access to the [eclipse-score](https://github.com/eclipse-score) organization
- [VS Code](https://code.visualstudio.com/) (or another devcontainer-capable IDE)
- [Docker](https://www.docker.com/get-started/) installed and running

## 1. Clone a repository

Pick a module repository to work with. For this tutorial, we use `module_template`:

```bash
git clone https://github.com/eclipse-score/module_template.git
cd module_template
```

## 2. Open in devcontainer

Open the cloned repository in VS Code. When prompted, click **Reopen in Container**.

The devcontainer image (`ghcr.io/eclipse-score/devcontainer`) includes all required tooling: Bazel, Python, pre-commit, language toolchains, and more.

If VS Code does not prompt automatically, open the command palette (`Ctrl+Shift+P`) and select **Dev Containers: Reopen in Container**.

## 3. Verify your environment

Run these commands inside the devcontainer:

```bash
bazel version
python3 --version
pre-commit --version
```

All three should succeed. If any fail, the devcontainer image may need rebuilding — ask in [#score-infrastructure](https://sdvworkinggroup.slack.com/archives/C0894QGRZDM).

## 4. Build everything

```bash
bazel build //...
```

This compiles all targets in the repository. On the first run, Bazel downloads external dependencies — this takes a few minutes. Subsequent builds are fast.

## 5. Run all tests

```bash
bazel test //...
```

To see full output when a test fails, add `--test_output=all`.

You should see all tests pass. If a test fails in a clean clone, it's a known issue — report it.

## 6. Set up pre-commit hooks

```bash
pre-commit install
```

This configures git hooks that check formatting and hygiene before each commit.

Verify by running all checks manually:

```bash
pre-commit run --all-files
```

## What you've accomplished

You now have:

- A working devcontainer environment
- A successful Bazel build
- Passing tests
- Pre-commit hooks catching issues before they reach CI

## Next steps

- [Your First Pull Request](first-pull-request.md) — Make a change and get it merged
- [How-to: Building with Bazel](../how-to/building.md) — Registry configuration and dependency management
- [How-to: Testing](../how-to/testing.md) — Test frameworks, coverage, and sanitizers

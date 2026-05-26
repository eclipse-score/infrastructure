# Your First Pull Request

This tutorial walks you through making a change to a S-CORE repository and getting it merged. By the end, you will have submitted a real pull request.

:::{note} Prerequisites
Complete [Getting Started](getting-started.md) first. You need a working devcontainer and passing build.
:::

## 1. Fork the repository

Contributions to S-CORE come from personal forks, not from branches on the upstream repository. Go to the repository you want to contribute to on GitHub and click **Fork** → **Create a new fork**.

Clone your fork locally:

```bash
git clone https://github.com/<your-username>/<repository>.git
cd <repository>
```

Add the upstream repository as a remote so you can pull in future changes:

```bash
git remote add upstream https://github.com/eclipse-score/<repository>.git
```

Open the clone in the devcontainer before continuing.

## 2. Create a branch

```bash
git switch -c my-first-change
```

## 3. Make a change

For this tutorial, pick something small: fix a typo, improve a comment, or add a missing test case.

## 4. Run checks locally

Before committing, verify your change:

```bash
bazel build //...
bazel test //...
pre-commit run --all-files
```

All three must pass. Pre-commit hooks catch formatting issues that would otherwise block CI.

## 5. Commit your change

```bash
git add <changed-files>
git commit
```

Write a clear commit message. S-CORE follows conventional formatting:

- First line: short summary (imperative mood, max ~72 characters)
- Blank line, then details if needed

Pre-commit hooks run automatically on commit. If they fail, fix the issue and commit again.

## 6. Push and create a pull request

```bash
git push -u origin my-first-change
```

Open the link printed by `git push` to create a pull request on GitHub. Set the base repository to `eclipse-score/<repository>` and the base branch to `main`. In the PR description:

- Explain **what** you changed and **why**
- Reference any related issues

## 7. Wait for CI

GitHub Actions runs the full test suite, pre-commit checks, and additional CI validations. Check the PR's "Checks" tab for results.

If CI fails, read the logs, fix the issue locally, push again. The PR updates automatically.

## 8. Address review feedback

A maintainer will review your PR. Respond to comments, push fixes if needed. Once approved, the PR gets merged.

## What you've accomplished

You now know the full contribution cycle:

- Fork → Branch → Change → Local checks → Commit → Push → PR → CI → Review → Merge

## Next steps

- [How-to: Code Quality](../how-to/code-quality.md) — Understand what pre-commit and CI checks enforce
- [How-to: Testing](../how-to/testing.md) — Write and run different types of tests
- [Explanation: Source Code Infrastructure](../explanation/01-source-code-infrastructure.md) — How repositories are organized and governed

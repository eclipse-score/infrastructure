# Creating a New Module

This tutorial walks you through creating a new Bazel module repository from the S-CORE template, publishing it to the registry, and making it available for other modules to depend on.

:::{note} Prerequisites
Complete [Getting Started](getting-started.md) first. You should be comfortable with the devcontainer and Bazel basics.
:::

## 1. Create a repository from the template

Go to [eclipse-score/module_template](https://github.com/eclipse-score/module_template) and click **Use this template** → **Create a new repository**.

Name it according to its purpose (e.g., `my_component`). The template provides:

- Standard directory layout
- `.bazelrc` with S-CORE registry configuration
- Devcontainer setup
- CI workflows
- Pre-commit configuration

## 2. Clone and verify

```bash
git clone https://github.com/eclipse-score/my_component.git
cd my_component
```

Open in the devcontainer and verify:

```bash
bazel build //...
bazel test //...
```

The template includes a minimal build target and test. Both should pass out of the box.

## 3. Add your code

Replace the template placeholder with your actual module code. The standard layout:

```
my_component/
├── MODULE.bazel        # Module metadata and dependencies
├── BUILD.bazel         # Top-level build targets
├── src/
│   └── BUILD.bazel     # Library targets
└── test/
    └── BUILD.bazel     # Test targets
```

Declare dependencies on other S-CORE modules in `MODULE.bazel`:

```python
bazel_dep(name = "some_other_module", version = "1.0.0")
```

## 4. Apply toolchains and policies

Add the relevant toolchain and policy dependencies:

```python
bazel_dep(name = "score_cpp_policies", version = "...")
bazel_dep(name = "bazel_cpp_toolchains", version = "...")
```

These provide the shared compiler configuration and lint baselines. See [How-to: Code Quality](../how-to/code-quality.md) for details.

## 5. Verify everything

```bash
bazel build //...
bazel test //...
pre-commit run --all-files
```

## 6. Publish a release

Create a GitHub Release with a semantic version tag (e.g., `v0.1.0`). Then follow the [registry import process](../how-to/publishing.md) to make it available to consumers.

## What you've accomplished

You now have:

- A new module repository following S-CORE conventions
- Working build, tests, and pre-commit checks
- Understanding of how to publish to the registry

## Next steps

- [How-to: Publishing Modules](../how-to/publishing.md) — Detailed registry import instructions
- [How-to: Building with Bazel](../how-to/building.md) — Advanced dependency and toolchain configuration
- [Explanation: Build & Dependencies](../explanation/03-build-infrastructure.md) — Architecture of the build system

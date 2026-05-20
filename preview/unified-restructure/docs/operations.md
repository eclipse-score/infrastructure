# Operations

Operational aspects of the shared S-CORE infrastructure services.

## Bazel Registry Operations

The [bazel_registry](https://github.com/eclipse-score/bazel_registry) and [bazel_registry_ui](https://github.com/eclipse-score/bazel_registry_ui) are shared services that all module repositories depend on. Registry validation workflows verify new entries on pull request, and GitHub Pages deployment keeps the Registry UI available. The [registry README](https://github.com/eclipse-score/bazel_registry/blob/main/README.md) is the canonical guide for adding new module versions.

## Dependency Maintenance

Dependabot opens pull requests automatically to bump dependency versions and SHA hashes across repositories. These PRs follow the standard review process.

## Organization Settings

GitHub organization settings are managed as code via [Otterdog](https://otterdog.readthedocs.io/) in the [.eclipsefdn](https://github.com/eclipse-score/.eclipsefdn) repository. This includes branch protection rules, required status checks, and app configurations. Changes go through pull request review in that repository.

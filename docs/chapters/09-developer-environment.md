# 10 Developer Environment 🟠

*Environment infrastructure supporting developer productivity and consistency across S-CORE contributors.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- A shared devcontainer image at [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) standardizes development environments across contributors and CI.
- Pre-commit hooks provide fast local validation before code submission.
- **Biggest gap**: local tooling standardization beyond the devcontainer and pre-commit is not yet complete.

## 10.1 Devcontainer 🟠

*Standardized, containerized development environment for S-CORE contributors and CI.*

**S-CORE**

- Devcontainer images are provided at [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) for use by both CI pipelines and local developer environments.
- The devcontainer standardizes tool versions and configurations across a wide range of compilers, build tools, and runtimes.
- **Biggest gap**: devcontainer adoption across all S-CORE repositories and contributors is not yet complete.

## 10.2 IDE Integration 🟠

*Integration with development environments and IDEs for S-CORE contributors.*

**S-CORE**

- The [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) includes pre-configured VS Code extensions and workspace settings.
- IDE configuration via the devcontainer ensures consistent editor tooling (formatting, linting, debugging) across contributors.
- **Biggest gap**: IDE support beyond VS Code is not covered by the current devcontainer setup.

## 10.3 Local Tooling 🟠

*Local development tooling provided for S-CORE contributors outside of CI.*

**S-CORE**

- Local tooling (build, test, lint, format) is accessible via the devcontainer without manual host configuration.
- Shared static-analysis tooling and rule-baseline concerns are covered centrally in [chapter 4](04-static-analysis-infrastructure.md); this chapter focuses only on how contributors access that tooling locally.
- **Biggest gap**: local tooling outside the devcontainer is not standardized; contributors running natively face an inconsistent setup.

## 10.4 Pre-commit Validation 🟠

*Local validation hooks that check code quality before submission.*

**S-CORE**

- [pre-commit](https://pre-commit.com/) hooks validate code locally before push, catching issues such as missing copyright headers or wrong formatting without a CI round-trip.
- Custom S-CORE pre-commit hooks are provided via [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml).
- Existing ecosystem pre-commit hooks are used where available; no proprietary mirrors of public hooks are maintained.
- Pre-commit is one local entry point for shared checks; the policy for which static-analysis checks belong there is defined in [chapter 4](04-static-analysis-infrastructure.md).
- **Biggest gap**: pre-commit adoption and hook coverage are not uniformly enforced across all S-CORE repositories.

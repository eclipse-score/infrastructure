# 2 Developer Environment ⚪

*Environment infrastructure supporting developer productivity and consistency across S-CORE contributors.*

⚠️ This chapter is written by ChatGPT and was not yet reviewed

**S-CORE**

- A shared devcontainer image at [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) standardizes development environments across contributors and CI.
- Pre-commit hooks provide fast local validation before code submission.
- Toolchain baselines are owned in [chapter 3](build-infrastructure.md), code-analysis policy in [chapter 5](static-analysis-infrastructure.md), and dependency-analysis policy in [chapter 6](compliance-infrastructure.md); this chapter focuses on how contributors consume those capabilities locally.
- The development environment is not only a convenience setup; when S-CORE builds and distributes it, it is also an engineering artifact with dependency, SBOM, and license-compliance implications.
- **Biggest gap**: local tooling standardization beyond the devcontainer and pre-commit is not yet complete.

## 2.1 Devcontainer ⚪

*Standardized, containerized development environment for S-CORE contributors and CI.*

**S-CORE**

- Devcontainer images are provided at [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) for use by both CI pipelines and local developer environments.
- The devcontainer standardizes tool versions and configurations across a wide range of compilers, build tools, and runtimes.
- Because the devcontainer is itself a distributed artifact, it also needs visible dependency governance and license-compliance treatment, even though the owning evidence model belongs in [chapter 3](build-infrastructure.md).
- **Biggest gap**: devcontainer adoption across all S-CORE repositories and contributors is not yet complete.

### 2.1.1 Reproducible Local Setup

*Making contributor onboarding and machine setup as repeatable as possible.*

**S-CORE**

- Contributors should be able to reach a working setup with minimal host-specific preparation.
- **Biggest gap**: onboarding steps and fallback guidance outside the containerized path are not yet consistently documented.

### 2.1.2 Environment SBOM & License Visibility

*Treating the development environment as an artifact whose contents and licenses should be visible.*

**S-CORE**

- The development environment pulls in compilers, runtimes, CLI tools, Python packages, and other dependencies that matter for compliance and supply-chain visibility.
- Contributors benefit when the environment artifact can be inspected and traced just like other distributed build outputs.
- **Biggest gap**: SBOM and license visibility for the devcontainer and related environment artifacts are not yet part of the standard developer-environment story.

## 2.2 IDE Integration ⚪

*Integration with development environments and IDEs for S-CORE contributors.*

**S-CORE**

- The [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer) includes pre-configured VS Code extensions and workspace settings.
- IDE configuration via the devcontainer ensures consistent editor tooling (formatting, linting, debugging) across contributors.
- **Biggest gap**: IDE support beyond VS Code is not covered by the current devcontainer setup.

### 2.2.1 Other IDEs & Terminal Use

*Supporting contributors who do not use the primary editor workflow.*

**S-CORE**

- Non-VS-Code workflows are possible, but the supported expectations and tradeoffs are not yet made explicit.
- **Biggest gap**: the supported boundary between the shared toolchain and editor-specific experience is still unclear.

## 2.3 Local Tooling ⚪

*Local development tooling provided for S-CORE contributors outside of CI.*

**S-CORE**

- Local tooling (build, test, lint, format) is accessible via the devcontainer without manual host configuration.
- Shared code-analysis tooling and rule-baseline concerns are covered centrally in [chapter 5](static-analysis-infrastructure.md); this chapter focuses only on how contributors access that tooling locally.
- **Biggest gap**: local tooling outside the devcontainer is not standardized; contributors running natively face an inconsistent setup.

### 2.3.1 Common Commands & Entry Points

*Giving contributors consistent ways to invoke build, test, documentation, and analysis workflows locally.*

**S-CORE**

- Shared invocation patterns are especially valuable when infrastructure changes span multiple repositories.
- **Biggest gap**: there is no clearly documented project-wide convention for which local commands every repository should expose.

## 2.4 Pre-commit Validation 🟠

*Local validation hooks that check code quality before submission.*

**S-CORE**

- [pre-commit](https://pre-commit.com/) hooks validate code locally before push, catching issues such as missing copyright headers or wrong formatting without a CI round-trip.
- Custom S-CORE pre-commit hooks are provided via [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml).
- Existing ecosystem pre-commit hooks are used where available; no proprietary mirrors of public hooks are maintained.
- Pre-commit is one local entry point for shared checks; the policy for which code-analysis checks belong there is defined in [chapter 5](static-analysis-infrastructure.md).
- **Biggest gap**: pre-commit adoption and hook coverage are not uniformly enforced across all S-CORE repositories.

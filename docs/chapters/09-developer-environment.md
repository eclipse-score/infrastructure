# 9 Developer Environment 🟠

*Environment supporting developer productivity.*

## Overview

<!-- auto-generated overview table -->
| Capability | Description | Status |
| --- | --- | --- |
| 9.1 Devcontainer | Infrastructure providing standardized development environments. | 🟠 |
| 9.2 IDE Integration | Infrastructure supporting integration with development environments and IDEs. | 🟠 |
| 9.3 Local Tooling | Infrastructure providing local development tooling. | 🟠 |
| 9.4 Pre-commit Validation | Infrastructure validating code locally before submission. | 🟠 |
<!-- end of auto-generated overview table -->

## 9.1 Devcontainer 🟠

*Infrastructure providing standardized development environments.*

> Note on Implementation:
> [devcontainer images](https://github.com/eclipse-score/devcontainer/) can be used by CI and every developer.
> This achieves standardization among a great range of tools and versions.

## 9.2 IDE Integration 🟠

*Infrastructure supporting integration with development environments and IDEs.*

> Note on Implementation:
> [The devcontainer](https://github.com/eclipse-score/devcontainer/) comes with Visual Studio Code extensions and configuration.

## 9.3 Local Tooling 🟠

*Infrastructure providing local development tooling.*

## 9.4 Pre-commit Validation 🟠

*Infrastructure validating code locally before submission.*

> Note on Implementation:
> [pre-commit hooks](https://pre-commit.com/) check for fast to detect issues like missing copyright headers or wrong formatting.
> 
> There are already pre-existing pre-commit hooks, which we use if suitable.
> If we need custom S-CORE hooks they are provided by tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml)
> 
> We do not mirror publicly available pre-commit hooks, because they are considered developer convenience (alternative would be expensive CI jobs) and are not needed for reproducible binaries.

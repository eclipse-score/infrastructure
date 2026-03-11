# Documentation Pipelines

Documentation pipelines cover the automation that validates and prepares documentation changes.

## Scope

This includes:

- build validation for the documentation site
- link and structure checks where they are useful
- publishing preparation steps in CI
- documentation changes as part of normal pull request review

## Relevant Tools

- GitHub Actions
- uv
- MkDocs build validation
- repository review workflows

## Current Model

This repository builds the documentation site with MkDocs and publishes it through GitHub Pages in workflow mode. The expected pipeline shape is:

1. check out the repository
2. install the pinned documentation toolchain with `uv`
3. run `mkdocs build --strict`
4. upload the generated site as a Pages artifact
5. deploy from `main`

## Typical Work Items

- ensure every documentation change can be previewed or built reliably
- fail fast on broken links or invalid navigation
- keep documentation CI lightweight enough that contributors will use it
- align publishing automation with the repository's branch and review model

## Why It Matters

Documentation pipelines are part of controlled automation. They improve trust in the published content and reduce the chance that important onboarding or operational guidance silently breaks.
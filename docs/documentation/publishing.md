# Documentation Publishing

Documentation publishing covers how the built site becomes available to readers.

## Scope

This topic includes:

- when publishing happens
- which branch or workflow acts as the publishing source
- where the generated site is hosted
- how published content relates to repository review and change history

## Relevant Tools

- MkDocs site builds
- GitHub Actions publishing workflows
- GitHub Pages in workflow mode

## Current Context

This repository is published through GitHub Pages in workflow mode. The site is built with MkDocs in GitHub Actions, the generated output is uploaded as a Pages artifact, and deployment is performed from the repository workflow rather than from a branch-based publishing mode.

The canonical site URL follows the repository project-site pattern:

- `https://eclipse-score.github.io/infrastructure/`

## Typical Work Items

- maintain the supported publication workflow for this repository
- document preview versus published content expectations
- make it clear who can trigger or approve documentation publication changes
- keep the publishing setup simple enough to maintain as the site grows

## Why It Matters

Publishing is where docs-as-code becomes visible to the rest of the project. A clear publishing model improves transparency and makes it easier for stakeholders to rely on the documentation as an operational reference.
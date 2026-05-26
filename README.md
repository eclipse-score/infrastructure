# S-CORE Infrastructure Documentation

This repository contains the sources for the S-CORE infrastructure documentation.

The published documentation is available at:

- https://eclipse-score.github.io/infrastructure/

## How The Site Is Structured

The README intentionally stays short to avoid duplicating the actual documentation. Use the published site for content and this repository for source files, local preview, and contribution work.

## Contributing

Contribution guidance, documentation style, and detailed instructions for AI agents live in [CONTRIBUTING.md](CONTRIBUTING.md).

## Build Locally

This repository uses Bazel with the S-CORE [docs-as-code](https://github.com/eclipse-score/docs-as-code) toolchain.

Start a live-reloading preview:

```bash
bazel run //:live_preview
```

Quickly validate the documentation:

```bash
bazel run //:docs_check
```

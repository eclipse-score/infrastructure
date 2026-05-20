# Code Quality

## Pre-commit Hooks

Set up hooks once per repository clone:

```bash
pre-commit install
```

Run all checks manually:

```bash
pre-commit run --all-files
```

Hook definitions are maintained in [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml). Checks include formatting, YAML validation, copyright headers, and lock file freshness.

## Copyright and License Headers

Every source file needs:

- A **copyright notice** in the file header
- An **SPDX license identifier**

For file formats that do not support inline comments, use a `.license` sidecar file alongside the source file.

Pre-commit hooks and CI PR checks from [eclipse-score/tooling](https://github.com/eclipse-score/tooling) enforce header presence automatically.

## C++ Policies

[score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) centralizes:

- Warning baselines
- Sanitizer feature selections (ASan, UBSan, LSan, TSan)
- Constraint targets

Consume these policies as a Bazel dependency to apply consistent C++ quality rules across repositories.

## Rust Policies

[score_rust_policies](https://github.com/eclipse-score/score_rust_policies) packages:

- Shared Clippy lint rules
- rustfmt defaults

## Where Checks Run

| Stage | What runs | Speed |
|---|---|---|
| **Local (pre-commit)** | Formatting, YAML, copyright headers, lock files | Seconds |
| **Bazel build** | Compiler warnings, lint policies, sanitizers | Minutes |
| **CI** | Full test suite, coverage, compliance checks | Minutes |

Pre-commit catches formatting and hygiene fast. Bazel enforces deeper checks. CI is the final gate.

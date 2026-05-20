# How to Enforce Code Quality

## Set up pre-commit hooks

```bash
pre-commit install
```

Run all checks manually:

```bash
pre-commit run --all-files
```

Hook definitions are maintained in [eclipse-score/tooling](https://github.com/eclipse-score/tooling/blob/main/.pre-commit-hooks.yaml). Checks include formatting, YAML validation, copyright headers, and lock file freshness.

## Add copyright and license headers

Every source file needs:

- A **copyright notice** in the file header
- An **SPDX license identifier**

For file formats that do not support inline comments, use a `.license` sidecar file alongside the source file.

Pre-commit hooks and CI PR checks from [eclipse-score/tooling](https://github.com/eclipse-score/tooling) enforce header presence automatically.

## Apply C++ policies

[score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) centralizes:

- Warning baselines
- Sanitizer feature selections (ASan, UBSan, LSan, TSan)
- Constraint targets

Consume these policies as a Bazel dependency to apply consistent C++ quality rules across repositories.

## Apply Rust policies

[score_rust_policies](https://github.com/eclipse-score/score_rust_policies) packages:

- Shared Clippy lint rules
- rustfmt defaults

## Understand where checks run

| Stage | What runs | Speed |
|---|---|---|
| **Local (pre-commit)** | Formatting, YAML, copyright headers, lock files | Seconds |
| **Bazel build** | Compiler warnings, lint policies, sanitizers | Minutes |
| **CI** | Full test suite, coverage, compliance checks | Minutes |

Pre-commit catches formatting and hygiene fast. Bazel enforces deeper checks. CI is the final gate.

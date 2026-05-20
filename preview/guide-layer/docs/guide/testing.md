# Testing

## Running Tests

```bash
bazel test //...
```

Run a specific target:

```bash
bazel test //path/to:target
```

Force re-execution (skip cache):

```bash
bazel test //... --nocache_test_results
```

## C++ Tests

GoogleTest is integrated via Bazel. Define test targets using `cc_test`:

```python
cc_test(
    name = "my_test",
    srcs = ["my_test.cc"],
    deps = [
        "//src:my_library",
        "@googletest//:gtest_main",
    ],
)
```

## Rust Tests

Native Rust tests work through `rules_rust`. Define test targets using the standard Rust test model.

## Python Tests

pytest-based tests are integrated through Bazel's Python rules.

## ITF Integration Testing

The Integration Test Framework (ITF) is a pytest-based framework for target-oriented testing. Key characteristics:

- Uses the `py_itf_test` Bazel macro to define test targets
- Plugin model supports Docker, QEMU, and hardware targets
- Tests declare required capabilities using the `@requires_capabilities` decorator

See the [ITF project documentation](https://eclipse-score.github.io/score/main/) for detailed usage.

## Coverage

Collect LCOV coverage data:

```bash
bazel coverage //... --combined_report
```

- **C++**: Compiler instrumentation via [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains)
- **Rust**: LLVM-based source coverage

## Sanitizers

[score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) provides selectable sanitizer features:

| Sanitizer | Purpose |
|---|---|
| ASan | Address errors (buffer overflow, use-after-free) |
| UBSan | Undefined behavior |
| LSan | Memory leaks |
| TSan | Data races |

Enable sanitizers via Bazel `select()` expressions in your build configuration.

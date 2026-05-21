# How to Test

## Run all tests

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

## Write a C++ test

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

## Write a Rust test

Native Rust tests work through `rules_rust`. Define test targets using the standard Rust test model.

## Write a Python test

pytest-based tests are integrated through Bazel's Python rules.

## Use the Integration Test Framework (ITF)

ITF is a pytest-based framework for target-oriented testing:

- Use the `py_itf_test` Bazel macro to define test targets
- Plugin model supports Docker, QEMU, and hardware targets
- Declare required capabilities using the `@requires_capabilities` decorator

See the [ITF project documentation](https://eclipse-score.github.io/score/main/) for detailed usage.

## Collect coverage

```bash
bazel coverage //... --combined_report
```

- **C++**: Compiler instrumentation via [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains)
- **Rust**: LLVM-based source coverage

## Enable sanitizers

[score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) provides selectable sanitizer features:

| Sanitizer | Purpose |
|---|---|
| ASan | Address errors (buffer overflow, use-after-free) |
| UBSan | Undefined behavior |
| LSan | Memory leaks |
| TSan | Data races |

Enable sanitizers via Bazel `select()` expressions in your build configuration.

# Testing

How to run tests, which frameworks are available, and how coverage and sanitizers work in S-CORE repositories.

## Running Tests

Run all tests in a repository:

```bash
bazel test //...
```

Run a specific test target:

```bash
bazel test //path/to:test_target
```

Force re-execution without cached results:

```bash
bazel test //... --nocache_test_results
```

## C++ Tests

C++ tests use GoogleTest through Bazel's `cc_test` rule. Test targets are defined in `BUILD.bazel` files alongside the code they test.

## Rust Tests

Rust tests use the native test model via `rules_rust`. The standard `#[test]` attributes and test modules work as expected within Bazel's test execution.

## Python Tests

Python tests use pytest, integrated through Bazel Python rules.

## ITF Integration Testing

The Integration Test Framework (ITF) is a pytest-based framework for target-oriented testing. It uses the `py_itf_test` macro to define test targets and supports a plugin model for different execution environments:

- **Docker** -- containerized test execution
- **QEMU** -- emulated hardware targets
- **Hardware** -- physical target devices

Tests declare their requirements using the `@requires_capabilities` decorator, which is matched against available target capabilities at runtime.

For details on ITF architecture and usage, see the [ITF project documentation](https://eclipse-score.github.io/score/main/modules/test/integration_test_framework/).

## Coverage

Generate a combined coverage report:

```bash
bazel coverage //... --combined_report
```

This produces LCOV output that can be processed by standard coverage tools.

- **C++ coverage** uses compiler instrumentation provided by [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains)
- **Rust coverage** uses LLVM source-based coverage

## Sanitizers

The [score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) module provides sanitizers as selectable Bazel features:

- **ASan** -- AddressSanitizer (memory errors)
- **UBSan** -- UndefinedBehaviorSanitizer
- **LSan** -- LeakSanitizer
- **TSan** -- ThreadSanitizer (data races)

These can be enabled per-build to catch runtime issues that static analysis cannot detect.

## Background

The ITF uses a capability-based Target model where test execution environments advertise their capabilities (e.g., network access, specific hardware, GPU) and tests declare which capabilities they require. This decouples test logic from environment setup and allows the same tests to run on Docker, QEMU, or real hardware by swapping the target plugin. The plugin architecture is extensible -- new target types can be added without modifying the framework core.

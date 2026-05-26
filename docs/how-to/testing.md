# How to Test

## Run tests

Run all tests in a repository:

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

See full output (useful when a test fails):

```bash
bazel test //path/to:target --test_output=all
```

Filter by test name pattern:

```bash
bazel test //path/to:target --test_filter="MyTest.specific_case"
```

## Write a C++ test

GoogleTest is integrated via Bazel. Define a `cc_test` target:

```python
load("@rules_cc//cc:defs.bzl", "cc_test")

cc_test(
    name = "my_test",
    srcs = ["my_test.cc"],
    deps = [
        "//src:my_library",
        "@googletest//:gtest_main",
    ],
)
```

```cpp
// my_test.cc
#include <gtest/gtest.h>
#include "src/my_library.h"

TEST(MyLibraryTest, ReturnsExpectedValue) {
    EXPECT_EQ(compute(2, 3), 5);
}
```

If the test needs data files:

```python
cc_test(
    name = "my_test",
    srcs = ["my_test.cc"],
    data = ["testdata/input.bin"],
    deps = ["@googletest//:gtest_main"],
)
```

## Write a Rust test

Native Rust tests work through `rules_rust`:

```python
load("@rules_rust//rust:defs.bzl", "rust_test")

rust_test(
    name = "my_test",
    srcs = ["my_test.rs"],
    deps = ["//src:my_library"],
)
```

```rust
// my_test.rs
use my_library::compute;

#[test]
fn returns_expected_value() {
    assert_eq!(compute(2, 3), 5);
}
```

## Write a Python test

pytest-based tests are integrated through Bazel's Python rules:

```python
load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "my_test",
    srcs = ["my_test.py"],
    deps = ["//src:my_library"],
)
```

## Write an ITF integration test

[ITF](https://github.com/eclipse-score/itf) runs tests against real environments — Docker containers, QEMU VMs, or hardware — through a unified `Target` interface. See [Tutorial: Write Your First ITF Integration Test](../tutorials/itf-integration-test.md) for a step-by-step introduction.

### Add ITF to your workspace

In `MODULE.bazel`:

```starlark
bazel_dep(name = "score_itf", version = "0.2.0")
```

For Docker and QEMU test recipes, see the [upstream how-to](https://eclipse-score.github.io/itf/main/how-to/write_tests.html). For full plugin CLI args and capabilities, see the [upstream plugin reference](https://eclipse-score.github.io/itf/main/how-to/plugins.html).

### Capability guards

Tests declare which target capabilities they need. The framework skips tests when the active target does not provide them:

```python
from score.itf.plugins.core import requires_capabilities

@requires_capabilities("exec")
def test_docker_only(target):
    exit_code, output = target.execute("ls /tmp")
    assert exit_code == 0

@requires_capabilities("ssh", "sftp")
def test_network_features(target):
    with target.ssh() as ssh:
        ssh.execute_command("echo ok")
```

### DLT log capture

```starlark
py_itf_test(
    name = "test_with_dlt",
    srcs = ["test_with_dlt.py"],
    args = [
        "--docker-image=my-app:latest",
        "--dlt-config=$(location dlt_config.json)",
    ],
    data = ["dlt_config.json"],
    plugins = [
        "@score_itf//score/itf/plugins:docker_plugin",
        "@score_itf//score/itf/plugins:dlt_plugin",
    ],
)
```

```python
from score.itf.plugins.dlt.dlt_window import DltWindow
from score.itf.plugins.dlt.dlt_receive import Protocol
import re

def test_dlt_messages(target, dlt_config):
    with DltWindow(
        protocol=Protocol.UDP,
        host_ip="127.0.0.1",
        multicast_ips=["224.0.0.1"],
        binary_path=dlt_config.dlt_receive_path,
    ) as window:
        with target.ssh() as ssh:
            ssh.execute_command("my_application")

        record = window.record()
        results = record.find(query={
            "apid": re.compile(r"APP1"),
            "payload": re.compile(r".*Started successfully.*"),
        })
        assert len(results) > 0
```

### Requirement traceability

```python
from attribute_plugin import add_test_properties

@add_test_properties(
    fully_verifies=["REQ-001", "REQ-002"],
    test_type="requirements-based",
    derivation_technique="requirements-analysis",
)
def test_hello(target):
    exit_code, output = target.execute("echo 'Hello from target!'")
    assert exit_code == 0
```

```starlark
py_itf_test(
    name = "test_hello",
    srcs = ["test_hello.py"],
    args = ["--docker-image=ubuntu:24.04"],
    plugins = [
        "@score_itf//score/itf/plugins:docker_plugin",
        "@score_itf//score/itf/plugins:attribute_plugin",
    ],
)
```

### Session-scoped targets

Reuse the same target across all tests in a session (faster, but tests share state):

```bash
bazel test //path/to:test --test_arg=--keep-target
```

For available plugins and `qemu_config.json` format, see the [Configuration Reference](../reference/configuration.md#itf-test-targets).

## Advanced: QNX unit tests

[qnx_unit_tests](https://github.com/eclipse-score/qnx_unit_tests) provides `cc_test_qnx` and `rust_test_qnx` macros that wrap standard test targets for execution inside a QEMU microvm running QNX 8.

### Prerequisites

- QEMU (`qemu-system-x86_64` and/or `qemu-system-aarch64`)
- KVM access (strongly recommended for performance)
- QNX SDP 8.0 credentials (for toolchain download)

### Add to your workspace

In `MODULE.bazel`:

```starlark
bazel_dep(name = "score_qnx_unit_tests", version = "...")
```

### Wrap a test target

Write a standard `cc_test`, then wrap it:

```starlark
load("@rules_cc//cc:defs.bzl", "cc_test")
load("@score_qnx_unit_tests//:defs.bzl", "cc_test_qnx")

cc_test(
    name = "my_test",
    srcs = ["my_test.cpp"],
    deps = [
        "@googletest//:gtest",
        "@googletest//:gtest_main",
    ],
)

cc_test_qnx(
    name = "my_test_qnx",
    cc_test = ":my_test",
)
```

For Rust:

```starlark
load("@rules_rust//rust:defs.bzl", "rust_test")
load("@score_qnx_unit_tests//:defs.bzl", "rust_test_qnx")

rust_test(
    name = "my_rust_test",
    srcs = ["my_test.rs"],
)

rust_test_qnx(
    name = "my_rust_test_qnx",
    rust_test = ":my_rust_test",
)
```

### Configure `.bazelrc`

Use the provided platform configs:

```
build:qnx-x86_64  # Cross-compile for QNX x86_64
build:qnx-aarch64 # Cross-compile for QNX aarch64
```

Run:

```bash
bazel test //path/to:my_test_qnx --config=qnx-x86_64
```

### How it works

The macro packages the test binary and runfiles into a tar archive, builds a QNX IFS boot image with the kernel and startup scripts, boots QEMU with the IFS image, mounts the test archive via virtio-9p, executes the test, and extracts results (XML, coverage) from the shared directory.

## Collect coverage

### C++

```bash
bazel coverage //... --combined_report
```

Produces LCOV output. Compiler instrumentation is configured by [bazel_cpp_toolchains](https://github.com/eclipse-score/bazel_cpp_toolchains).

### Rust

```bash
bazel coverage //... --combined_report
```

Uses LLVM source-based coverage (`llvm-cov`). The same LCOV output format is used so downstream reporting does not need language-specific parsers.

### ITF tests

For Docker-based ITF tests, the Docker plugin supports extracting coverage data from the container:

```starlark
py_itf_test(
    name = "test_with_coverage",
    srcs = ["test_example.py"],
    args = [
        "--docker-image=my-instrumented-image:latest",
        "--extract-coverage",
    ],
    plugins = ["@score_itf//score/itf/plugins:docker_plugin"],
)
```

Coverage files (`.gcda`) are extracted to `$TEST_UNDECLARED_OUTPUTS_DIR/sysroot` before container teardown.

## Enable sanitizers

[score_cpp_policies](https://github.com/eclipse-score/score_cpp_policies) provides selectable sanitizer features (ASan, UBSan, LSan, TSan) as Bazel `cc_feature` definitions. Enable them via `select()` expressions or feature flags in your build configuration.

For the full list of sanitizers and constraint targets like `no_tsan` and `any_sanitizer`, see the [Configuration Reference](../reference/configuration.md#sanitizers).

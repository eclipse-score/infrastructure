# Write Your First Test

This tutorial walks you through writing a C++ unit test, running it with Bazel, and reading the output when it fails. By the end, you will have a passing test and an understanding of the test cycle.

:::{note} Prerequisites
Complete [Getting Started](getting-started.md) first. You need a working devcontainer and a successful `bazel build //...`.
:::

## 1. Add a library target

Create a minimal library to test. In `src/BUILD.bazel`:

```python
load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "math",
    hdrs = ["math.h"],
)
```

And `src/math.h`:

```cpp
#pragma once

inline int add(int a, int b) { return a + b; }
```

## 2. Write the test

Create `test/math_test.cc`:

```cpp
#include <gtest/gtest.h>
#include "src/math.h"

TEST(MathTest, AddsTwoNumbers) {
    EXPECT_EQ(add(2, 3), 5);
}
```

And `test/BUILD.bazel`:

```python
load("@rules_cc//cc:defs.bzl", "cc_test")

cc_test(
    name = "math_test",
    srcs = ["math_test.cc"],
    deps = [
        "//src:math",
        "@googletest//:gtest_main",
    ],
)
```

## 3. Run the test

```bash
bazel test //test:math_test --test_output=all
```

You should see:

```
[==========] Running 1 test from 1 test suite.
[ RUN      ] MathTest.AddsTwoNumbers
[       OK ] MathTest.AddsTwoNumbers (0 ms)
[==========] 1 test from 1 test suite ran.
[  PASSED  ] 1 test.
```

## 4. Make it fail

Change the assertion to something wrong:

```cpp
EXPECT_EQ(add(2, 3), 99);
```

Run again:

```bash
bazel test //test:math_test --test_output=all
```

Bazel shows:

```
[ RUN      ] MathTest.AddsTwoNumbers
test/math_test.cc:5: Failure
Expected equality of these values:
  add(2, 3)
    Which is: 5
  99
[  FAILED  ] MathTest.AddsTwoNumbers (0 ms)
```

The failure message tells you the file, the line, and the actual vs. expected values. Fix the assertion back to `5` before continuing.

## 5. Run all tests

```bash
bazel test //...
```

This runs every test target in the repository. Bazel caches results — only changed targets re-run. Use `--nocache_test_results` to force a full re-run if needed.

## What you've accomplished

You now know the basic test cycle in S-CORE:

- Define a `cc_test` target with `@googletest//:gtest_main`
- Run a single target with `bazel test //path:target --test_output=all`
- Read GoogleTest failure output
- Run the full suite with `bazel test //...`

## Next steps

- [How-to: Testing](../how-to/testing.md) — Rust and Python tests, coverage, sanitizers, QNX
- [Tutorial: Write Your First ITF Integration Test](itf-integration-test.md) — Tests against Docker containers and VMs

# Tutorial: Write Your First ITF Integration Test

This tutorial walks through writing a working integration test using the [ITF framework](https://github.com/eclipse-score/itf). By the end, you will have a test that runs a command inside a Docker container through Bazel.

**What you need:** a working devcontainer or local environment with Bazel and Docker available. See [Getting Started](getting-started.md) if you have not set that up yet.

---

## Step 1: Add ITF to your workspace

In `MODULE.bazel`, add the dependency:

```starlark
bazel_dep(name = "score_itf", version = "0.2.0")
```

Make sure your `.bazelrc` points to the S-CORE registry (it already does if you used `module_template`):

```
common --registry=https://raw.githubusercontent.com/eclipse-score/bazel_registry/main/
common --registry=https://bcr.bazel.build
```

---

## Step 2: Write the test

Create `tests/test_hello.py`:

```python
def test_hello(target):
    exit_code, output = target.execute("echo 'Hello from ITF!'")
    assert exit_code == 0
    assert b"Hello from ITF!" in output
```

The `target` fixture is injected by ITF. Behind it sits whatever plugin is active — Docker here, QEMU in another configuration. The test does not know or care which one.

---

## Step 3: Define the Bazel target

Create `tests/BUILD`:

```starlark
load("@score_itf//:defs.bzl", "py_itf_test")

py_itf_test(
    name = "test_hello",
    srcs = ["test_hello.py"],
    args = ["--docker-image=ubuntu:24.04"],
    plugins = ["@score_itf//score/itf/plugins:docker_plugin"],
)
```

`py_itf_test` is a macro that produces a standard `py_test` binary. Bazel treats it like any other test target — it participates in incremental build, caching, and `bazel test //...`. The Docker image is a runtime argument, not a build dependency, so changing the image does not trigger a rebuild.

---

## Step 4: Run it

```bash
bazel test //tests:test_hello --test_output=all
```

You should see Docker pulling the image (once), the container starting, your `echo` command running, and a green test result.

To force re-execution even if Bazel cached a previous pass:

```bash
bazel test //tests:test_hello --nocache_test_results --test_output=all
```

---

## Step 5: Make the test portable with capability guards

The same test file can run against different target types. Guard tests on the capabilities they actually need so they are skipped rather than failed on targets that do not provide them:

```python
from score.itf.plugins.core import requires_capabilities

def test_hello(target):
    exit_code, output = target.execute("echo 'Hello from ITF!'")
    assert exit_code == 0
    assert b"Hello from ITF!" in output

@requires_capabilities("ssh")
def test_network_only(target):
    with target.ssh() as ssh:
        exit_code = ssh.execute_command("uname -a")
        assert exit_code == 0
```

Run against the Docker target — `test_network_only` is skipped because Docker does not expose `ssh`. Switch to a QEMU target and it runs. The same file works in both cases without modification.

---

## What you built

You now have a working ITF test that:

- runs inside a Docker container through `bazel test`
- participates in Bazel's incremental build and result caching
- guards itself with `@requires_capabilities` so it can run against multiple target types

---

## Next steps

- [How-to: Testing](../how-to/testing.md#write-an-itf-integration-test) — DLT log capture, requirement traceability, session-scoped targets
- [ITF: Write Tests](https://eclipse-score.github.io/itf/main/how-to/write_tests.html) — QEMU tests, SSH on Docker, full capability reference (upstream docs)
- [ITF: Using Plugins](https://eclipse-score.github.io/itf/main/how-to/plugins.html) — all built-in plugins with full CLI args (upstream docs)
- [Explanation: ITF Framework](../explanation/04-testing-infrastructure.md#itf-framework) — plugin model, capability system, and architecture

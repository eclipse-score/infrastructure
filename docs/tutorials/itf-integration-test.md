# Tutorial: Write Your First ITF Integration Test

This tutorial walks through writing a working integration test using the [ITF framework](https://github.com/eclipse-score/itf). By the end, you will have a test that runs a command inside a Docker container through Bazel, and you will understand why ITF is structured the way it is.

**What you need:** a working devcontainer or local environment with Bazel and Docker available. See [Getting Started](getting-started.md) if you have not set that up yet.

---

## What ITF does

Most S-CORE tests are unit tests: they compile and run inside the Bazel sandbox on the build host. ITF tests are different — they run code against a real environment (a Docker container, a QEMU virtual machine, or a hardware device) through a unified plugin interface. This is the right tool for testing behavior that depends on a real OS, a real network, or a real device.

The same test file can target different environments. The `@requires_capabilities` decorator tells ITF which environment capabilities a test needs, and the framework skips tests that the active target cannot fulfill. Write once, run on Docker locally and on hardware in CI.

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

You should see Docker pulling the image (once), the container starting, your `echo` command running, and a green test result. If something goes wrong, `--test_output=all` shows the full pytest output.

To force re-execution even if Bazel cached a previous pass:

```bash
bazel test //tests:test_hello --nocache_test_results --test_output=all
```

---

## Step 5: Make the test portable with capability guards

Add a second test that uses a capability not all targets provide. Docker supports `exec` and `file_transfer`; QEMU additionally supports `ssh` and `sftp`. Guard tests so they are skipped rather than failed on the wrong target:

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

Run against the Docker target — `test_network_only` will be skipped because Docker does not expose `ssh`. Switch to a QEMU target and it runs. The same file works in both cases without modification.

---

## Step 6: Add traceability metadata (optional)

When a test verifies specific requirements, the attribute plugin can write that information into the JUnit XML report so the docs-as-code traceability system can link back to the requirement objects:

```python
from score.itf.plugins.core import requires_capabilities
from attribute_plugin import add_test_properties

@add_test_properties(
    fully_verifies=["REQ-HELLO-001"],
    test_type="requirements-based",
    derivation_technique="requirements-analysis",
)
def test_hello(target):
    exit_code, output = target.execute("echo 'Hello from ITF!'")
    assert exit_code == 0
    assert b"Hello from ITF!" in output
```

Update the BUILD target to include the attribute plugin:

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

The metadata appears as JUnit XML attributes on the test case element and can be consumed by Sphinx-based traceability tooling without a separate database or postprocessing step.

---

## What you built

You now have a working ITF test that:

- runs inside a Docker container through `bazel test`
- participates in Bazel's incremental build and result caching
- guards itself with `@requires_capabilities` so it can run against multiple target types
- optionally writes requirement traceability into the test result report

---

## Next steps

- [Write an ITF test against a QEMU target](../how-to/testing.md#write-an-itf-integration-test) — SSH-based interaction with a VM
- [Run QNX unit tests](../how-to/testing.md#run-qnx-unit-tests) — cross-compiled tests in a QNX microvm
- [ITF framework explained](../explanation/04-testing-infrastructure.md#itf-framework) — plugin model, capability system, and traceability integration

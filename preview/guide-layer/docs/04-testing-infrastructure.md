# 4 Testing ⚪

!!! tip "Looking for practical guides?"
    This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [Guide section](guide/quick-reference.md).

*Infrastructure supporting automated testing across S-CORE repositories, including dynamic analysis and verification evidence generation.*

⚠️ This chapter is partially written by ChatGPT and was not yet reviewed

**S-CORE**

Testing infrastructure in S-CORE is centered on executable Bazel test targets, shared framework integration, traceability metadata, and reporting that can be consumed as verification evidence. The verification process may still use named levels such as unit, component integration, feature integration, and platform tests, but that taxonomy belongs to process guidance rather than this chapter. From the infrastructure perspective, the practical distinction is simpler: lower-level tests usually live in module repositories, while broader scenario-driven and target-oriented execution increasingly collects around shared environments such as `reference_integration` and ITF.

That scope also explains why coverage, sanitizers, fuzzing, and profiling belong here. They are runtime techniques that depend on executing software, even when their outputs are later consumed by documentation, compliance, or CI chapters. **Biggest gap**: testing capability already exists in several strong islands, but shared conventions for framework packaging, traceability, aggregation, dashboards, and advanced runtime analysis are still incomplete across S-CORE.

## 4.1 Test Framework Integration ⚪

*Integrating language-specific and target-specific test frameworks with the Bazel build system.*

**S-CORE**

S-CORE already has a workable multi-language testing base. Repositories define Bazel `*_test` targets for C++, Rust, and Python, and higher-level integration environments layer scenario support and target orchestration on top. What is still missing is a clearer shared baseline for how those frameworks are packaged, versioned, and reused so that repositories converge on similar patterns instead of each building a local interpretation. **Biggest gap**: no single shared framework baseline or packaging model is yet defined across all S-CORE repositories.

### 4.1.1 C++ Test Frameworks

*Infrastructure supporting C++ testing frameworks.*

**S-CORE**

C++ testing is one of the most mature paths today. Bazel-integrated frameworks such as GoogleTest already support ordinary unit-style execution well, and existing C++ flows are also ahead on coverage and evidence generation. The remaining issue is consistency: framework versions and Bazel rule setup still vary per repository. **Biggest gap**: framework versioning and Bazel rule configuration are not yet aligned across S-CORE.

### 4.1.2 Rust Test Frameworks

*Infrastructure supporting Rust testing frameworks.*

**S-CORE**

Rust tests typically use the native Rust test model through `rules_rust`, which fits well with the Bazel-centered infrastructure direction. The capability exists, but it is less even than the established C++ path, especially around reporting, coverage integration, and traceability metadata. **Biggest gap**: consistent `rules_rust` versioning and reporting support are not yet uniformly available.

### 4.1.3 Python Test Frameworks

*Infrastructure supporting Python testing frameworks.*

**S-CORE**

Python tests generally rely on pytest-style execution integrated through Bazel's Python rules. Python also matters beyond unit tests because it often acts as the orchestration layer for higher-level scenarios and target interaction, which is why ITF ([section 4.1.5](#415-itf-framework)) is itself pytest-based.

For repositories that use pytest, the infrastructure question is not whether pytest works — it does — but whether repositories converge on a shared baseline for plugin selection, fixture patterns, and result output. Without that, each repository assembles its own pytest configuration, and shared tooling that consumes test results (reporting in [section 4.4](#44-test-reporting-), traceability in [section 4.2](#42-test-traceability-)) has to account for divergent output formats and metadata conventions. A shared pytest baseline would define which plugins are expected by default, how results are formatted for downstream consumption, and how system-level tests that need target interaction relate to the ITF plugin model.

The rollout challenge is that pytest is used at multiple levels: lightweight unit-style tests in module repositories, orchestration-heavy system tests in integration environments, and ITF-based target tests. A shared baseline must be useful across those levels without forcing a one-size-fits-all configuration. **Biggest gap**: there is no shared Python test framework and plugin baseline across repositories, and the boundary between plain pytest usage and ITF-managed execution is not yet clearly drawn.

### 4.1.4 Scenario Test Framework

*Infrastructure supporting scenario-based testing for C++ and Rust.*

**S-CORE**

Scenario-style execution matters once testing spans modules, services, or richer system behavior. S-CORE already uses scenario-based approaches to exercise common flows across languages and repositories, which is especially relevant when `reference_integration` assembles modules into shared environments. The tradeoff is that scenario logic can be split across orchestration code and implementation-specific backends, which makes ownership and failure diagnosis harder. **Biggest gap**: scenario support exists, but it is not yet packaged as a uniformly reusable cross-repository capability.

### 4.1.5 ITF Framework

*Infrastructure supporting target-oriented integration and system-like testing.*

**S-CORE**

ITF is the clearest example of target-oriented higher-level testing infrastructure in the current landscape. It is pytest-based, designed for ECU-oriented testing, and built around a target-agnostic plugin model covering environments such as Docker, QEMU, and real hardware, along with concerns like DLT handling.

The execution pipeline for ITF tests follows a layered model. Bazel invokes a pytest runner through the `py_itf_test` macro, which uses ITF plugins to manage the target environment — starting a Docker container, launching a QEMU instance, or connecting to a hardware device. The test code then interacts with the system under test through the environment that the plugin provides. Results flow back through pytest into Bazel's test result model. This pipeline means that ITF tests can be triggered as ordinary `bazel test` targets while the execution complexity is hidden inside the plugin layer.

The central abstraction is the capability-based `Target` model. Each target exposes capabilities such as `exec`, `file_transfer`, `restart`, `ssh`, and `sftp`. Tests declare which capabilities they require using decorators like `@requires_capabilities`, and the framework skips tests when the active target does not provide them. This design lets the same test code run against different target environments — a Docker container locally, a QEMU image in CI, a real board in the lab — with the plugin determining which capabilities are available.

The plugin model is what makes ITF extensible. Each target environment is a plugin (built via the `py_itf_plugin` Bazel macro) that handles provisioning, communication, and teardown. DLT log handling is another plugin concern. New target types can be added without changing the test-writing interface, and custom plugin documentation is already part of the ITF project.

For traceability, ITF provides an attribute plugin with an `@add_test_properties` decorator that writes metadata such as `fully_verifies`, `test_type`, and `derivation_technique` into JUnit XML output. This connects ITF test results to the traceability model described in [section 4.2](#42-test-traceability-).

**Biggest gap**: the ITF plugin model and capability system are established, but onboarding guidance for module teams adopting ITF is still missing. The Bazel-side integration for passing traceability metadata from build targets into the attribute plugin is not yet streamlined.

## 4.2 Test Traceability ⚪

*Infrastructure for tracking traceability between test cases, requirements, and verification evidence.*

**S-CORE**

Test traceability is one of the parts of the testing stack that already shows a clear end-to-end shape. Test implementations can add requirement information to reports, and the docs-as-code flow can consume those reports to create links back into requirements and verification artifacts. Tests therefore behave as first-class evidence objects, even when they are represented differently from textual requirements. Higher-level traceability in `reference_integration` is already moving in the same direction. **Biggest gap**: Rust targets and some higher-level frameworks still cannot carry the same degree of traceability metadata as the more mature C++-centric flows.

## 4.3 Test Execution & Dynamic Analysis ⚪

*Infrastructure for executing automated tests and runtime-driven analysis via the build system.*

**S-CORE**

At execution time, the common model is straightforward: tests are Bazel targets and normally run through `bazel test`, which provides isolation and incremental reuse of previous results. When re-execution must be forced, `--nocache_test_results` is available, and coverage collection already follows the stricter rule of always re-running with instrumentation. This section also owns the runtime-oriented techniques that depend on executing software rather than inspecting it statically. That includes coverage, sanitizers, fuzzing, stress testing, profiling, and performance benchmarking, even when their outputs later feed other chapters. In practice, this mostly shows up as a deployment pattern: lower-level execution stays inside module repositories, while cross-repository and target-oriented execution increasingly relies on shared environments such as `reference_integration` and ITF.

An important special case is cross-compiled test execution. S-CORE supports building for multiple target platforms through its toolchain infrastructure, but building a test binary and executing it are separate problems when the target platform differs from the build host. QNX is the clearest current example: [section 3.3.1](03-build-infrastructure.md#331-c-toolchains) describes how `bazel_cpp_toolchains` provides toolchain configuration for QNX builds, but running the resulting `cc_test` or `rust_test` binaries requires either a QNX-capable emulator, a remote target device, or a CI runner with appropriate sysroot and runtime support. The same pattern applies to any platform where the build host cannot natively execute the test output, and it connects directly to the hardware runner infrastructure described in [section 7.1.2](07-automation-integration.md#712-hardware-test-runners).

**Biggest gap**: test execution standards and runtime-analysis expectations are not yet defined consistently across repositories. Cross-compiled test execution for non-host platforms such as QNX lacks documented runner and deployment infrastructure.

### 4.3.1 Coverage & Runtime Instrumentation

*Measuring exercised code and collecting instrumentation data during tests.*

**S-CORE**

Coverage is already part of the verification-evidence story in several places, which makes it one of the more concrete dynamic-analysis capabilities in S-CORE today. The missing piece is not the idea of coverage itself, but shared expectations around when it is required, how it is produced, and which result formats downstream tooling should rely on.

For C++, Bazel can collect coverage using `bazel coverage` with the `--combined_report` flag, producing LCOV output that downstream tools can consume. The toolchain-level support comes from `bazel_cpp_toolchains` ([section 3.3.1](03-build-infrastructure.md#331-c-toolchains)), which configures the compiler instrumentation flags. The infrastructure gap is not the mechanism but the conventions: which targets should produce coverage, what minimum coverage expectations exist, and how results are aggregated across a module's test suite into a single report that CI can publish as an artifact.

For Rust, `rules_rust` supports coverage through similar Bazel instrumentation, but the tooling maturity is lower than for C++. Source-based coverage via LLVM's `llvm-cov` is the preferred approach because it produces accurate line and region coverage without the branch-level noise of gcov-style instrumentation. The same LCOV output format should be used so that downstream reporting does not need language-specific parsers.

For ITF-based tests, coverage collection crosses a process boundary because the test orchestrator (pytest) and the system under test (running in a Docker container, QEMU image, or on hardware) are separate processes. Collecting coverage in that scenario requires instrumentation on the target side and a mechanism to retrieve the coverage data after the test run completes. That integration is not yet in place for most ITF test configurations.

**Biggest gap**: coverage expectations and result formats are not yet standardized across repositories. Language-specific coverage tooling exists but is not configured or reported consistently, and ITF-based coverage collection is not yet integrated.

### 4.3.2 Sanitizers & Runtime Checks

*Detecting runtime problems such as memory misuse, undefined behavior, or concurrency issues.*

**S-CORE**

Sanitizers and similar runtime checks can surface memory misuse, undefined behavior, or concurrency problems far earlier than system-level debugging. They are especially valuable for C and C++ heavy repositories, but they need common support and expectations if they are to become shared infrastructure rather than ad hoc local practice. The ownership boundary should stay explicit: [chapter 3](03-build-infrastructure.md#33-toolchain-management) owns how toolchains and Bazel features make sanitizers available, and [chapter 5](05-static-analysis-infrastructure.md#52-shared-rule-configuration) owns shared policy modules when they package reusable sanitizer feature sets or defaults. The moment those capabilities are executed against runnable targets and interpreted as verification evidence, however, they belong in the testing story here.

### 4.3.3 Fuzzing, Stress & Profiling

*Using generated inputs, stress techniques, and runtime diagnostics to expose robustness and performance issues.*

**S-CORE**

Fuzzing, stress execution, and profiling sit naturally next to the rest of the test execution story because they also depend on runnable targets, special harnesses, and result handling that differs from ordinary regression tests. They are relevant to robustness and performance, but they are still described more as possibilities than as reusable S-CORE capabilities. **Biggest gap**: advanced dynamic-analysis techniques beyond basic coverage are not yet defined as shared infrastructure.

### 4.3.4 Performance & Benchmark Testing

*Infrastructure for measuring and tracking runtime performance of S-CORE components on representative targets.*

**S-CORE**

Performance testing differs from functional testing in that the result is a measurement rather than a pass/fail verdict. A benchmark run produces timing data, throughput numbers, or resource consumption figures that only become meaningful when compared against a previous baseline or an agreed budget. That comparison model is what turns raw profiling output into actionable infrastructure.

For S-CORE, the practical need comes from two directions. Module repositories want to detect performance regressions early, ideally as part of the normal Bazel test flow on cloud runners. Integration-level testing wants to measure representative workloads on real hardware targets such as embedded boards and automotive-grade SoCs, where host-based emulation cannot reproduce the actual timing and resource behavior.

The infrastructure challenge is therefore layered. Cloud-based benchmark targets can reuse the existing runner and Bazel execution model, but they need stable machine baselines and a way to compare results across runs without being dominated by runner variance. Hardware-based benchmarks additionally need target provisioning, deployment, and result collection infrastructure that extends the hardware runner story described in [section 7.1.2](07-automation-integration.md#712-hardware-test-runners). The concrete hardware targets that matter today include Raspberry Pi boards for lightweight integration-level benchmarks and automotive-grade SoCs such as the Qualcomm SA8650P for representative platform performance measurement. Each target class has different provisioning and deployment requirements, but the result model — durable storage, baseline comparison, trend visualization — should be uniform. In both cases, results should be stored durably and presented as trend data rather than one-shot artifacts.

**Biggest gap**: S-CORE has no shared performance testing framework, no benchmark result storage or comparison model, and no hardware target provisioning for performance measurement on boards such as Raspberry Pi or Qualcomm SA8650P.

## 4.4 Test Reporting ⚪

*Infrastructure for collecting, aggregating, and presenting test results as verification evidence across S-CORE.*

**S-CORE**

Test results are already visible in several places, but they do not yet form one consistent project-wide reporting layer. GitHub Actions exposes outcomes per pipeline run, release flows can aggregate and attach selected test and coverage artifacts, and some repositories already publish dashboard-style views for traceability or unit-test summaries. `reference_integration` also plays an important role in collecting higher-level evidence once modules are assembled and exercised together. The infrastructure direction is therefore visible: reporting should turn execution results into durable evidence that can be reviewed per run, per release, and eventually across repositories. **Biggest gap**: no centralized project-wide dashboard or durable cross-repository reporting model yet spans all of S-CORE.

### 4.4.1 Result Aggregation

*Infrastructure aggregating test results across CI pipeline runs.*

**S-CORE**

Aggregation already exists in pieces. CI runs produce artifacts, and release-oriented flows can combine selected outputs into something closer to a reusable evidence package. For higher integration levels, `reference_integration` is an especially important aggregation point because it collects results after cross-repository assembly and scenario execution. To stay meaningful, those aggregated results should be keyed to a concrete `known_good` manifest or record rather than to a vague notion of "current main". The fast integration subset can provide early feedback against a candidate manifest, but the deeper post-merge or scheduled suite is what should advance the stored known-good baseline. **Biggest gap**: aggregation works for some release flows, but continuous project-wide aggregation across repositories is still incomplete.

### 4.4.2 Test Dashboards

*Infrastructure providing dashboards for monitoring test results and trends.*

**S-CORE**

Some repositories already expose dashboard-like views for narrow concerns such as coverage or traceability, which shows the value of making test health visible beyond raw CI logs. What is missing is the shared layer that would let maintainers understand testing coverage and trends across repositories and execution styles without opening each repository separately. **Biggest gap**: test health visibility across S-CORE repositories is still fragmented.

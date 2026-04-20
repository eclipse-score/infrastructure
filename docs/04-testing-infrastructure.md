# 4 Testing ⚪

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

Python tests generally rely on pytest-style execution integrated through Bazel's Python rules. Python also matters beyond unit tests because it often acts as the orchestration layer for higher-level scenarios and target interaction. **Biggest gap**: there is no shared Python test framework and plugin baseline across repositories.

### 4.1.4 Scenario Test Framework

*Infrastructure supporting scenario-based testing for C++ and Rust.*

**S-CORE**

Scenario-style execution matters once testing spans modules, services, or richer system behavior. S-CORE already uses scenario-based approaches to exercise common flows across languages and repositories, which is especially relevant when `reference_integration` assembles modules into shared environments. The tradeoff is that scenario logic can be split across orchestration code and implementation-specific backends, which makes ownership and failure diagnosis harder. **Biggest gap**: scenario support exists, but it is not yet packaged as a uniformly reusable cross-repository capability.

### 4.1.5 ITF Framework

*Infrastructure supporting target-oriented integration and system-like testing.*

**S-CORE**

ITF is the clearest example of target-oriented higher-level testing infrastructure in the current landscape. It is pytest-based, designed for ECU-oriented testing, and is evolving toward a more target-agnostic plugin model covering environments such as Docker, QEMU, and real hardware, along with concerns like DLT handling. That makes it important infrastructure, but the Bazel integration is still incomplete from a traceability perspective. **Biggest gap**: ITF Bazel targets do not yet allow adding the test properties needed for full traceability.

## 4.2 Test Traceability ⚪

*Infrastructure for tracking traceability between test cases, requirements, and verification evidence.*

**S-CORE**

Test traceability is one of the parts of the testing stack that already shows a clear end-to-end shape. Test implementations can add requirement information to reports, and the docs-as-code flow can consume those reports to create links back into requirements and verification artifacts. Tests therefore behave as first-class evidence objects, even when they are represented differently from textual requirements. Higher-level traceability in `reference_integration` is already moving in the same direction. **Biggest gap**: Rust targets and some higher-level frameworks still cannot carry the same degree of traceability metadata as the more mature C++-centric flows.

## 4.3 Test Execution & Dynamic Analysis ⚪

*Infrastructure for executing automated tests and runtime-driven analysis via the build system.*

**S-CORE**

At execution time, the common model is straightforward: tests are Bazel targets and normally run through `bazel test`, which provides isolation and incremental reuse of previous results. When re-execution must be forced, `--nocache_test_results` is available, and coverage collection already follows the stricter rule of always re-running with instrumentation. This section also owns the runtime-oriented techniques that depend on executing software rather than inspecting it statically. That includes coverage, sanitizers, fuzzing, stress testing, and profiling, even when their outputs later feed other chapters. In practice, this mostly shows up as a deployment pattern: lower-level execution stays inside module repositories, while cross-repository and target-oriented execution increasingly relies on shared environments such as `reference_integration` and ITF. **Biggest gap**: test execution standards and runtime-analysis expectations are not yet defined consistently across repositories.

### 4.3.1 Coverage & Runtime Instrumentation

*Measuring exercised code and collecting instrumentation data during tests.*

**S-CORE**

Coverage is already part of the verification-evidence story in several places, which makes it one of the more concrete dynamic-analysis capabilities in S-CORE today. The missing piece is not the idea of coverage itself, but shared expectations around when it is required, how it is produced, and which result formats downstream tooling should rely on. **Biggest gap**: coverage expectations and result formats are not yet standardized across repositories.

### 4.3.2 Sanitizers & Runtime Checks

*Detecting runtime problems such as memory misuse, undefined behavior, or concurrency issues.*

**S-CORE**

Sanitizers and similar runtime checks can surface memory misuse, undefined behavior, or concurrency problems far earlier than system-level debugging. They are especially valuable for C and C++ heavy repositories, but they need common support and expectations if they are to become shared infrastructure rather than ad hoc local practice. The ownership boundary should stay explicit: [chapter 3](03-build-infrastructure.md#33-toolchain-management) owns how toolchains and Bazel features make sanitizers available, and [chapter 5](05-static-analysis-infrastructure.md#52-shared-rule-configuration) owns shared policy modules when they package reusable sanitizer feature sets or defaults. The moment those capabilities are executed against runnable targets and interpreted as verification evidence, however, they belong in the testing story here.

### 4.3.3 Fuzzing, Stress & Profiling

*Using generated inputs, stress techniques, and runtime diagnostics to expose robustness and performance issues.*

**S-CORE**

Fuzzing, stress execution, and profiling sit naturally next to the rest of the test execution story because they also depend on runnable targets, special harnesses, and result handling that differs from ordinary regression tests. They are relevant to robustness and performance, but they are still described more as possibilities than as reusable S-CORE capabilities. **Biggest gap**: advanced dynamic-analysis techniques beyond basic coverage are not yet defined as shared infrastructure.

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

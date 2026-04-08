# 4 Testing ⚪

*Infrastructure supporting automated testing across S-CORE repositories, including dynamic analysis and test evidence generation.*

⚠️ This chapter is partially written by ChatGPT and was not yet reviewed

**S-CORE**

- The verification process defines the expected test levels and evidence.
- This chapter focuses on the implementation view: what exists, where it lives, and what is still missing.
- Tests are executed via Bazel test rules, providing isolation and incremental caching of build targets.
- Multi-language test support exists across C++, Rust, and Python, but repository-level conventions still vary.
- S-CORE distinguishes test levels such as unit tests, component integration tests, feature integration tests, and platform tests.
- `reference_integration` already provides shared integration-oriented execution and release-level aggregation for parts of the project.
- It is best understood as higher-level testing infrastructure that consumes integrated modules, not as the primary module-distribution mechanism itself.
- Dynamic analysis belongs here because coverage, sanitizers, fuzzing, and profiling depend on executing software.
- **Biggest gap**: testing infrastructure exists in several strong islands, but project-wide standardization for aggregation, dashboards, reusable conventions, and runtime-analysis coverage is still incomplete.

## 4.1 Test Levels ⚪

*Test levels used by the S-CORE verification process and supported by testing infrastructure, from unit scope to platform verification.*

**S-CORE**

- Four test levels are used across S-CORE: unit tests, component integration tests, feature integration tests, and platform tests.
- Lower levels are mainly implemented in module repositories.
- Higher integration levels increasingly rely on `reference_integration`.
- **Biggest gap**: the named test levels are defined in process documentation, but their concrete implementation patterns are not yet equally mature across the whole project.

### 4.1.1 Unit Tests

*Infrastructure supporting verification of software units against detailed design.*

**S-CORE**

- Unit tests are expressed as Bazel `*_test` targets per language.
- Test code usually lives in `/tests` directories or next to the implementation, depending on repository conventions.
- C++ execution and coverage are established; Rust support is improving but less complete in some areas.
- **Biggest gap**: no shared baseline for naming, layout, coverage treatment, and metadata conventions across all S-CORE repositories.

### 4.1.2 Component Integration Tests

*Infrastructure supporting verification of component architecture and component requirements.*

**S-CORE**

- Component integration tests verify component architecture, interfaces, flows, and integration of units into components.
- CIT execution is primarily handled inside individual repositories via Bazel.
- **Biggest gap**: repository-specific CIT structure exists, but common patterns for reusable execution and reporting are not yet standardized project-wide.

### 4.1.3 Feature Integration Tests

*Infrastructure supporting verification of feature-level requirements and architecture across module boundaries.*

**S-CORE**

- Feature integration tests verify feature-level requirements and architecture across module boundaries.
- FIT execution is centered in `reference_integration`, where features are integrated as external modules and exercised through shared scenarios.
- In the intended flow, module-producing repositories publish consumable modules and `reference_integration` assembles them into higher-level feature scenarios.
- FIT traceability is already being established in `reference_integration`.
- **Biggest gap**: FIT infrastructure exists, but traceability, language support, and reusable documentation around scenario composition are still evolving.

### 4.1.4 Platform Tests ⚪

*Infrastructure supporting verification of stakeholder requirements on reference targets.*

**S-CORE**

- Platform tests are the highest named verification level in current S-CORE process descriptions.
- They verify stakeholder requirements on reference hardware and consume evidence from lower integration levels such as FITs.
- Enabling pieces already exist through `reference_integration`, release assets, and target-oriented frameworks such as ITF.
- **Biggest gap**: a fully standardized and visible platform-test environment, with broad hardware coverage and unified reporting, is not yet established across S-CORE.

### 4.1.5 Cross-Repository & Scenario Testing

*Infrastructure supporting tests that span multiple S-CORE repositories and reusable end-to-end scenarios.*

**S-CORE**

- Cross-repository testing already exists in practice through `reference_integration`, where multiple repositories are integrated and tested together.
- `reference_integration` is therefore the primary shared environment for validating how separately developed S-CORE modules behave in combination.
- Scenario-based testing is used as an execution style for higher integration levels, especially in `reference_integration` and ITF-based environments.
- **Biggest gap**: cross-repository execution is available, but it is not yet generalized into a uniformly reusable mechanism for all repositories and all test levels.

## 4.2 Test Framework Integration ⚪

*Integrating language-specific and target-specific test frameworks with the Bazel build system.*

**S-CORE**

- Test framework rules for C++, Rust, and Python are configured per repository.
- Higher-level integration and target-oriented testing additionally rely on shared frameworks such as ITF and repository-specific scenario support.
- **Biggest gap**: no single shared framework baseline or packaging model is yet mandated across all S-CORE repositories.

### 4.2.1 C++ Test Frameworks

*Infrastructure supporting C++ testing frameworks.*

**S-CORE**

- C++ tests use frameworks such as GoogleTest integrated via Bazel rules.
- C++ support is one of the more established paths for unit-test execution and coverage reporting.
- **Biggest gap**: framework versioning and Bazel rule configuration still vary per repository.

### 4.2.2 Rust Test Frameworks

*Infrastructure supporting Rust testing frameworks.*

**S-CORE**

- Rust tests use the native test model mapped into Bazel via `rules_rust`.
- Rust support is active, but traceability and detailed reporting are still less complete than in established C++ flows.
- **Biggest gap**: consistent `rules_rust` versioning, coverage/report handling, and metadata support are not yet uniformly available.

### 4.2.3 Python Test Frameworks

*Infrastructure supporting Python testing frameworks.*

**S-CORE**

- Python tests use frameworks such as pytest integrated via Bazel Python rules.
- Python also acts as an orchestration layer for some higher-level testing workflows.
- **Biggest gap**: no shared Python test framework and plugin baseline is standardized across repositories.

### 4.2.4 Scenario Test Framework

*Infrastructure supporting scenario based testing for C++ and Rust.*

**S-CORE**

- Scenario-style test support exists for building common scenarios across languages and modules.
- Shared scenarios can be executed while keeping implementation in language-specific backends.
- **Biggest gap**: split execution and verification logic can make ownership, traceability, and failure diagnosis harder.

### 4.2.5 ITF Framework

*Infrastructure supporting target-oriented integration and system-like testing.*

**S-CORE**

- ITF is a pytest-based Integration Testing Framework designed for ECU-oriented testing.
- Current public discussion describes ITF as moving toward a target-agnostic, plugin-based architecture.
- Target environments include Docker, QEMU virtual machines, and real hardware, with plugins also covering concerns such as DLT handling.
- **Biggest gap**: ITF Bazel targets do not allow adding test properties for traceability.

## 4.3 Test Traceability ⚪

*Infrastructure for tracking traceability between test cases, requirements, and verification evidence.*

**S-CORE**

- Test implementation adds properties about tested requirements to the test report.
- Docs-as-code consumes all available reports at build time and creates test links in requirements.
- Tests have their own virtual needs objects, which can be queried and referenced even though they are not implemented in the same way as textual requirements.
- FIT traceability in `reference_integration` is already being established.
- **Biggest gap**: Rust test targets and some higher-level frameworks still do not support the same degree of traceability metadata as established C++-centric flows.

## 4.4 Test Execution & Dynamic Analysis ⚪

*Infrastructure for executing automated tests and runtime-driven analysis via the build system.*

**S-CORE**

- Tests are defined as Bazel targets and executed via `bazel test`, enabling incremental and cached re-execution.
- Test re-execution can be forced by adding the `--nocache_test_results` flag.
- Code coverage analysis always executes tests and does not use cache for correct instrumentation.
- Higher integration levels additionally rely on shared orchestration, especially in `reference_integration`.
- Dynamic analysis techniques such as coverage, sanitizers, fuzzing, and profiling belong here because they depend on execution semantics.
- **Biggest gap**: test execution standards and runtime-analysis expectations are not uniformly defined across repositories.

### 4.4.1 Coverage & Runtime Instrumentation

*Measuring exercised code and collecting instrumentation data during tests.*

**S-CORE**

- Coverage is already part of the verification evidence story in several places.
- **Biggest gap**: coverage expectations and result formats are not yet standardized across repositories and test levels.

### 4.4.2 Sanitizers & Runtime Checks

*Detecting runtime problems such as memory misuse, undefined behavior, or concurrency issues.*

**S-CORE**

- Sanitizer-style checks can provide high-value feedback early, especially for C and C++ heavy codebases.
- **Biggest gap**: there is no shared policy for which runtime checks should be supported or required in common repository classes.

### 4.4.3 Fuzzing, Stress & Profiling

*Using generated inputs, stress techniques, and runtime diagnostics to expose robustness and performance issues.*

**S-CORE**

- These techniques often need different scheduling and result handling than ordinary regression tests.
- **Biggest gap**: advanced dynamic-analysis techniques beyond basic coverage are not yet described as reusable shared infrastructure.

## 4.5 Test Reporting ⚪

*Infrastructure for collecting, aggregating, and presenting test results as verification evidence across S-CORE.*

**S-CORE**

- Test results are surfaced per pipeline run via GitHub Actions.
- For S-CORE releases, test and coverage reports are aggregated and attached to release assets.
- Some repository-level dashboards already exist, for example around traceability and unit-test or coverage summaries.
- These outputs provide the evidence needed by the verification process.
- **Biggest gap**: no centralized project-wide dashboard or durable cross-repository trend reporting spans all of S-CORE.

### 4.5.1 Result Aggregation

*Infrastructure aggregating test results across CI pipeline runs.*

**S-CORE**

- Test result artifacts are generated per CI run, and release-oriented aggregation already exists for selected shared outputs.
- `reference_integration` plays an important role in collecting and combining higher-level evidence after cross-repository integration and scenario execution.
- **Biggest gap**: aggregation works for some release flows, but continuous project-wide aggregation across repositories and levels is still incomplete.

### 4.5.2 Test Dashboards

*Infrastructure providing dashboards for monitoring test results and trends.*

**S-CORE**

- Individual repositories already expose dashboard-style views for selected concerns such as traceability or unit-test and coverage summaries.
- No unified dashboard currently gives one consistent view across all repositories and all test levels.
- **Biggest gap**: test health visibility across S-CORE repositories is absent.

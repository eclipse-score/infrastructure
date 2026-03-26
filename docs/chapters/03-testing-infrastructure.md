# 3 Testing Infrastructure ⚪

*Infrastructure supporting automated testing across S-CORE repositories, excluding CI/CD execution.*

⚠️ This chapter is partially written by ChatGPT and was not yet reviewed

**S-CORE**

- Tests are executed via Bazel test rules, providing isolation and incremental caching of build targets.
- Multi-language test support exists across C++, Rust, and Python, but repository-level conventions still vary.
- S-CORE distinguishes test levels such as unit tests, component integration tests, feature integration tests, and platform tests.
- `reference_integration` already provides shared integration-oriented execution and release-level aggregation for parts of the platform.
- **Biggest gap**: testing infrastructure exists in several strong islands, but platform-wide standardization for aggregation, dashboards, and reusable conventions is still incomplete.

## 3.1 Test Levels ⚪

*Test levels covered by S-CORE testing infrastructure, from unit scope to platform verification.*

**S-CORE**

- S-CORE process descriptions define four main automated test levels: unit tests, component integration tests, feature integration tests, and platform tests.
- Lower test levels are primarily owned within module repositories, while higher integration levels increasingly rely on `reference_integration`.
- Execution support exists, but repository-local practice and traceability depth still differ between languages and repositories.
- **Biggest gap**: the named test levels are defined in process documentation, but their concrete implementation patterns are not yet equally mature across the whole project.

### 3.1.1 Unit Tests

*Infrastructure supporting component-level tests.*

**S-CORE**

- Unit tests are expressed as Bazel `*_test` targets per language.
- Unit test implementations are typically located either in dedicated `/tests` directories or next to the tested code, depending on language and repository conventions.
- Unit-test execution and coverage collection are established for C++, and Rust support is improving but still less mature in some areas.
- **Biggest gap**: no shared baseline for naming, layout, coverage treatment, and metadata conventions across all S-CORE repositories.

### 3.1.2 Component Integration Tests

*Infrastructure supporting tests across units and components inside a module context.*

**S-CORE**

- Component Integration Tests (CITs) are intended to verify component architecture, interfaces, flows, and integration of units into components.
- CIT execution is primarily handled within individual repositories via Bazel and feeds into module-level verification reporting.
- **Biggest gap**: repository-specific CIT structure exists, but common patterns for reusable execution and reporting are not yet standardized project-wide.

### 3.1.3 Feature Integration Tests

*Infrastructure supporting tests across multiple modules.*

**S-CORE**

- Feature Integration Tests (FITs) verify feature-level requirements and architecture across module boundaries.
- FIT execution is centered in the `reference_integration` repository, where features are integrated as external modules and exercised through shared scenarios.
- Public testing community notes indicate FIT traceability is already being established in `reference_integration`.
- **Biggest gap**: FIT infrastructure exists, but traceability, language support, and reusable documentation around scenario composition are still evolving.

### 3.1.4 Platform Tests ⚪

*Infrastructure for testing stakeholder-facing platform behavior on reference targets.*

**S-CORE**

- Platform tests are the highest named verification level in current S-CORE process descriptions.
- They are intended to verify stakeholder requirements on reference hardware and consume evidence from lower integration levels such as FITs.
- Some enabling pieces already exist through `reference_integration`, release assets, and target-oriented frameworks such as ITF.
- **Biggest gap**: a fully standardized and visible platform-test environment, with broad hardware coverage and unified reporting, is not yet established across S-CORE.

#### 3.1.4.1 Cross-Repository Testing

*Infrastructure supporting tests that span multiple S-CORE repositories.*

**S-CORE**

- Cross-repository testing already exists in practice through `reference_integration`, where multiple repositories are integrated and tested together.
- This is currently the main shared place where higher-level integration testing is assembled.
- **Biggest gap**: cross-repository execution is available, but it is not yet generalized into a uniformly reusable mechanism for all repositories and all test levels.

#### 3.1.4.2 Scenario Testing

*Infrastructure supporting end-to-end usage scenarios across the middleware.*

**S-CORE**

- Scenario-based testing is used as an execution style for higher integration levels, especially in `reference_integration` and ITF-based environments.
- The current direction is toward reusable scenario execution on different targets rather than one monolithic platform-wide scenario harness.
- **Biggest gap**: scenario authoring, reuse, traceability, and result correlation still require more consistent tooling and documentation.

---

## 3.2 Test Framework Integration ⚪

*Integrating language-specific test frameworks with the Bazel build system.*

**S-CORE**

- Test framework rules for C++, Rust, and Python are configured per repository.
- Higher-level integration and target-oriented testing additionally rely on shared frameworks such as ITF and repository-specific scenario support.
- **Biggest gap**: no single shared framework baseline or packaging model is yet mandated across all S-CORE repositories.

### 3.2.1 C++ Test Frameworks

*Infrastructure supporting C++ testing frameworks.*

**S-CORE**

- C++ tests use frameworks such as GoogleTest integrated via Bazel rules.
- C++ support is one of the more established paths for unit-test execution and coverage reporting.
- **Biggest gap**: framework versioning and Bazel rule configuration still vary per repository.

### 3.2.2 Rust Test Frameworks

*Infrastructure supporting Rust testing frameworks.*

**S-CORE**

- Rust tests use the native test model mapped into Bazel via `rules_rust`.
- Rust support is active, but traceability and detailed reporting are still less complete than for established C++ flows.
- **Biggest gap**: consistent `rules_rust` versioning, coverage/report handling, and metadata support are not yet uniformly available.

### 3.2.3 Python Test Frameworks

*Infrastructure supporting Python testing frameworks.*

**S-CORE**

- Python tests use frameworks such as pytest integrated via Bazel Python rules.
- Python also acts as an orchestration layer for some higher-level testing workflows.
- **Biggest gap**: no shared Python test framework and plugin baseline is standardized across repositories.

### 3.2.4 Scenario Test Framework

*Infrastructure supporting scenario based testing for C++ and Rust.*

**S-CORE**

- Scenario-style test support exists for building common scenarios across languages and modules.
- This pattern helps execute shared behavior checks while keeping implementation under language-specific backends.
- **Biggest gap**: split execution and verification logic can make ownership, traceability, and failure diagnosis harder.

### 3.2.5 ITF Framework

*Infrastructure supporting target-oriented integration and system-like testing.*

**S-CORE**

- ITF is a pytest-based Integration Testing Framework designed for ECU-oriented testing.
- Current public discussion describes ITF as moving toward a target-agnostic, plugin-based architecture.
- Target environments include Docker, QEMU virtual machines, and real hardware, with plugins also covering concerns such as DLT handling.
- **Biggest gap**: ITF Bazel targets do not allow adding test properties for traceability.

---

## 3.3 Test Traceability ⚪

*Infrastructure for tracking traceability between tests and requirements.*

**S-CORE**

- Test implementation adds properties about tested requirements to the test report.
- Docs-as-code consumes all available reports at the build time and creates testlinks in requirements.
- Tests have their own `virtual needs objects`, which can be queried and referenced even though they are not implemented in the same way as textual requirements.
- Public testing discussion indicates FIT traceability in `reference_integration` is already being established, with combined reporting across levels under active refinement.
- **Biggest gap**: Rust test targets and some higher-level frameworks still do not support the same degree of traceability metadata as established C++-centric flows.

---

## 3.4 Test Execution ⚪

*Infrastructure for executing automated tests via the build system.*

**S-CORE**

- Tests are defined as Bazel targets and executed via `bazel test`, enabling incremental and cached re-execution.
- Test re-execution can be forced by adding the `--nocache_test_results` flag.
- Code coverage analysis always executes tests and does not use cache for correct instrumentation.
- Higher integration levels additionally rely on shared repository orchestration, especially in `reference_integration`.
- **Biggest gap**: test execution standards (target naming, timeout policy, sharding) are not uniformly defined across repositories.

---

## 3.5 Test Reporting ⚪

*Infrastructure for collecting, aggregating, and presenting test results across S-CORE.*

**S-CORE**

- Test results are surfaced per pipeline run via GitHub Actions.
- For S-CORE releases, test and coverage reports are aggregated and attached to release assets.
- Some repository-level dashboards already exist, for example around traceability and unit-test or coverage summaries.
- **Biggest gap**: no centralized platform-wide dashboard or durable cross-repository trend reporting spans all of S-CORE.

### 3.5.1 Result Aggregation

*Infrastructure aggregating test results across CI pipeline runs.*

**S-CORE**

- Test result artifacts are generated per CI run, and release-oriented aggregation already exists for selected shared outputs.
- `reference_integration` plays an important role in collecting and combining higher-level evidence.
- **Biggest gap**: aggregation works for some release flows, but continuous project-wide aggregation across repositories and levels is still incomplete.

### 3.5.2 Test Dashboards

*Infrastructure providing dashboards for monitoring test results and trends.*

**S-CORE**

- Individual repositories already expose dashboard-style views for selected concerns such as traceability or unit-test and coverage summaries.
- No unified dashboard currently gives one consistent view across all repositories and all test levels.
- **Biggest gap**: test health visibility across S-CORE repositories is absent.

---

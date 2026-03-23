# 3 Testing Infrastructure ⚪

*Infrastructure supporting automated testing across S-CORE repositories, excluding CI/CD execution.*

⚠️ This chapter is partially written by ChatGPT and was not yet reviewed

**S-CORE**

- Tests are executed via Bazel test rules, providing isolation and incremental caching of build targets.
- Multi-language test framework support (C++, Rust, Python) is configured per repository.
- **Biggest gap**: cross-repository test result aggregation, shared test dashboards, and system integration testing are not yet in place.

## 3.1 Test Execution ⚪

*Infrastructure for executing automated tests via the build system.*

**S-CORE**

- Tests are defined as Bazel targets and executed via `bazel test`, enabling incremental and cached re-execution.
- Tests re-execution can be forced by adding `--nocache_test_results` flag.
- Code coverage analysis always executes tests and do not use cache for correct instrumentation.
- **Biggest gap**: test execution standards (target naming, timeout policy, sharding) are not uniformly defined across repositories.

### 3.1.1 Unit Tests

*Infrastructure supporting component-level tests.*

**S-CORE**

- Unit tests are expressed as Bazel `*_test` targets per language.
- UTs implementation is located in either dedicated `/tests` directories or directly next to implementation depending on language best practices.
- Rust tests targets are currently treated as single test no matter how many tests they are gathering.
- **Biggest gap**: no shared baseline for unit test target conventions across S-CORE repositories.

### 3.1.2 Component Integration Tests

*Infrastructure supporting tests across components modules.*

**S-CORE**

- Component integration test execution is handled within individual repositories via Bazel.
- **Biggest gap**: cross-repository integration test execution is not yet standardized.

### 3.1.3 Feature Integration Tests

*Infrastructure supporting tests across multiple modules.*

**S-CORE**

- Feature integration test execution is handled within `reference_integration` repository via Bazel.
- All features are loaded as external modules and used during testing.
- **Biggest gap**: 

---

## 3.2 Test Framework Integration ⚪

*Integrating language-specific test frameworks with the Bazel build system.*

**S-CORE**

- Test framework rules for C++, Rust, and Python are configured per repository.
- **Biggest gap**: no shared test framework rule package or version baseline is mandated across S-CORE.

### 3.2.1 C++ Test Frameworks

*Infrastructure supporting C++ testing frameworks.*

**S-CORE**

- C++ tests use frameworks such as GoogleTest integrated via Bazel rules.
- **Biggest gap**: framework version and Bazel rule configuration vary per repository.

### 3.2.2 Rust Test Frameworks

*Infrastructure supporting Rust testing frameworks.*

**S-CORE**

- Rust tests use the native test model mapped into Bazel via `rules_rust`.
- **Biggest gap**: consistent `rules_rust` version and test target conventions are not mandated.

### 3.2.3 Python Test Frameworks

*Infrastructure supporting Python testing frameworks.*

**S-CORE**

- Python tests use frameworks such as pytest integrated via Bazel Python rules.
- **Biggest gap**: no shared Python test framework configuration is standardized across repositories.

### 3.2.4 Scenario Test Framework

*Infrastructure supporting scenario based testing for C++ and Rust.*

**S-CORE**

- Provides backend for Rust and C++ which can be used to implement common test scenario.
- Single Python test case implementation allows parametrized interaction with multi-language features.
- **Biggest gap**: Splitted test execution and verification logic makes it hard to track issues.

### 3.2.5 ITF Framework

*Infrastructure supporting scenario based testing for C++ and Rust.*

**S-CORE**

- ITF is pytest-based testing framework designed for ECU (Electronic Control Unit) testing
- Provides a flexible, plugin-based architecture that enables testing on multiple target environments including Docker,
QEMU virtual machines, and real hardware.
- **Biggest gap**: ITF Bazel targets do not allow adding test properties for traceability.

---

## 3.3 System Integration Testing ⚪

*Infrastructure for testing interactions between middleware components across S-CORE repositories.*

**S-CORE**

- System integration testing across repository boundaries is a target capability.
- **Biggest gap**: no shared infrastructure for cross-repository scenario or system-level testing exists.

### 3.3.1 Cross-Repository Testing

*Infrastructure supporting tests that span multiple S-CORE repositories.*

**S-CORE**

- Cross-repository test execution is not yet supported by shared S-CORE infrastructure.
- **Biggest gap**: no mechanism for triggering or aggregating tests across repository boundaries.

### 3.3.2 Scenario Testing

*Infrastructure supporting end-to-end usage scenarios across the middleware.*

**S-CORE**

- End-to-end scenario testing at the S-CORE platform level is not yet operationalized.
- **Biggest gap**: no scenario test harness or shared execution infrastructure exists.

---

## 3.4 Test Reporting ⚪

*Infrastructure for collecting, aggregating, and presenting test results across S-CORE.*

**S-CORE**

- Test results are surfaced per pipeline run via GitHub Actions.
- For S-CORE releases all test reports are agregated and attached to S-CORE release assets.
- **Biggest gap**: no centralized test result dashboard or trend tracking spans S-CORE repositories.

### 3.4.1 Result Aggregation

*Infrastructure aggregating test results across CI pipeline runs.*

**S-CORE**

- Test result artifacts are generated per CI run; no shared aggregation pipeline spans repositories.
- **Biggest gap**: aggregating results across repository boundaries requires a dedicated pipeline not yet built.

### 3.4.2 Test Dashboards

*Infrastructure providing dashboards for monitoring test results and trends.*

**S-CORE**

- Single repositories have dashboards displaying traceability.
- No shared test dashboard infrastructure currently exists across S-CORE.
- **Biggest gap**: test health visibility across S-CORE repositories is absent.

---

## 3.5 Test Traceability ⚪

*Infrastructure for tracking traceability between tests and requirements.*

**S-CORE**

- Test implementation adds properties about tested requirements to the test report.
- Docs-as-code consumes all available reports at the build time and creates testlinks in requirements.
- Tests have their `virtual needs objects` which can be querried and referenced but they do not have their implementation as requirements have.
- **Biggest gap**: Rust test targets currently do not support adding properties to test reports.

# 2 Build Infrastructure (Bazel) ⚪

*Infrastructure required to build the middleware deterministically, excluding CI/CD execution.*

:warning: **Chapter 2 is written by ChatGPT** :warning:
:warning: Please restructure in a meaningful way -> @Nikola

## 2.1 Build System ⚪

*Infrastructure providing core build tooling used across the project.*

### 2.1.1 Project Structure

*Infrastructure defining the standard organization of build workspaces.*

### 2.1.2 Build Rule Libraries

*Infrastructure providing reusable build abstractions shared across repositories.*

### 2.1.3 Build Conventions

*Infrastructure defining shared conventions for build targets and repository layout.*

---

## 2.2 Dependency Management ⚪

*Infrastructure for managing internal and external dependencies.*

### 2.2.1 Third-Party Dependencies

*Infrastructure for integrating and managing external libraries.*

### 2.2.2 Internal Module Dependencies

*Infrastructure for managing dependencies between project modules.*

### 2.2.3 Dependency Policies

*Infrastructure defining rules governing allowed dependencies.*

---

## 2.3 Toolchain Management ⚪

*Infrastructure for managing compilers and toolchains.*

### 2.3.1 C++ Toolchains

*Infrastructure providing compiler and build configuration for C++.*

### 2.3.2 Rust Toolchains

*Infrastructure providing toolchain configuration for Rust components.*

### 2.3.3 Python Toolchains

*Infrastructure providing Python runtime and tooling configuration.*

---

## 2.4 Build Reproducibility ⚪

*Infrastructure ensuring builds are deterministic and reproducible.*

### 2.4.1 Hermetic Builds

*Infrastructure isolating builds from host environments.*

### 2.4.2 Deterministic Artifacts

*Infrastructure ensuring builds produce identical artifacts.*

### 2.4.3 Build Traceability

*Infrastructure tracking build inputs and outputs.*

---

## 2.5 Build Execution Infrastructure ⚪

*Infrastructure for executing builds in distributed or remote environments.*

### 2.5.1 Remote Cache

*Infrastructure for sharing build outputs between build executions.*

### 2.5.2 Remote Build Execution

*Infrastructure for executing builds on remote compute resources.*

### 2.5.3 Build Resource Scheduling

*Infrastructure for scheduling and allocating build resources.*

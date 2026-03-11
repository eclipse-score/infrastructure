# Test Execution

Test execution describes when tests run, where they run, and how different categories of tests fit into local development and CI workflows.

## Scope

This includes:

- local versus CI test execution
- fast validation compared with slower or broader validation stages
- repository-specific and cross-repository test triggers
- environment requirements for certain test jobs

## Relevant Tools

- Bazel test
- pytest
- GitHub Actions workflows

## Typical Work Items

- explain which tests contributors should run before opening a pull request
- define which tests are required in CI for merge confidence
- separate short feedback loops from heavier validation paths
- document environment constraints for tests that cannot run everywhere

## Practical Questions

- Which tests are expected locally?
- Which tests always run in CI?
- How are expensive or platform-specific tests scheduled?
- How are failures routed back to the contributor in a usable way?

## Why It Matters

Clear execution rules reduce wasted time and make test failures easier to interpret. They also support controlled automation because contributors can see which validation steps are mandatory and which ones are conditional.
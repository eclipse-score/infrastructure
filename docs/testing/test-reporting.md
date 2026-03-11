# Test Reporting

Test reporting covers how results are surfaced to contributors, maintainers, and stakeholders.

## Scope

This includes:

- pass or fail status in CI
- logs, summaries, and retained reports
- visibility into flaky or unstable tests
- aggregation of results where broader views are needed

## Relevant Tools

- GitHub Actions job summaries and logs
- retained CI artifacts
- test framework reporting outputs

## Typical Work Items

- make failures easier to diagnose from the first report
- decide which test outputs should be retained as artifacts
- highlight repeated failures or flaky tests instead of treating them as isolated noise
- improve summaries for people who need a management or oversight view rather than raw logs

## Why It Matters

A test platform is only as useful as its feedback. Good reporting shortens debugging time for developers and improves transparency for stakeholders who need to know whether validation is working as intended.

Where broader dashboards or long-term metrics are needed, they can be layered on top later. The immediate goal is to make individual pipeline results clear and actionable.
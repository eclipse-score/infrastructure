# GitHub Actions secrets from forks: decision guide

## Background

Workflows triggered by `pull_request` for PRs from forks do not have access to repository secrets by default.  
This is a security protection to prevent untrusted code from exfiltrating secrets.

This guide explains when to use:
1. `pull_request_target`
2. Environments (with protection rules / approvals)

---

## Threat model

Fork PR code is untrusted until reviewed.  
If untrusted code executes in a context that has secrets, those secrets can be leaked through logs, artifacts, network calls, or modified scripts.

**Rule 1:** Never run untrusted fork code in a job that has access to secrets.  
**Rule 2:** Secret access must be gated by explicit trust/approval controls.

---

## Option A: `pull_request_target`

`pull_request_target` runs in the context of the base repository (not the fork), so secrets can be available.

### Use when

- You need to run metadata/policy checks on PRs from forks.
- You can perform actions without checking out and executing fork code.
- You can strictly separate “trusted logic” from “untrusted code execution”.

### Risks

- High risk if workflow checks out PR head (`github.event.pull_request.head.sha`) and then runs scripts with secrets.
- Any step that executes contributor-controlled code can leak secrets.

### Hard constraints

- Do not execute fork code in secret-bearing jobs.
- Avoid `actions/checkout` of PR head in privileged jobs.
- Use minimal `permissions:` at workflow/job level.
- Keep privileged steps narrowly scoped.

---

## Option B: Environments

Environments allow protection rules such as required reviewers before jobs can access environment secrets.

### Use when

- A job requires secrets (deploy, publish, integration against protected services).
- You need a human approval gate before secret use.
- You want explicit, auditable secret access decisions.

### Risks

- If approval is granted before validating what will run, untrusted code may still execute with secrets.
- Overly broad environment reuse can expose too many secrets.

### Hard constraints

- Require reviewers on sensitive environments.
- Scope secrets per environment and per purpose.
- Run untrusted checks first (`pull_request`, no secrets), then gated trusted job.

---

## Decision matrix

| Scenario | Recommended trigger/pattern |
|---|---|
| Lint/unit checks for fork PRs without secrets | `pull_request` |
| PR labeling/commenting/metadata checks only | `pull_request_target` (no fork code execution) |
| Secret-required jobs (deploy/integration/publish) | Environment-gated job with required reviewers |
| Need to run fork code + secrets immediately | **Do not do this** |

---

## Recommended standard

1. Use `pull_request` for all untrusted fork validation (no secrets).
2. Use environments with required reviewers for secret-dependent jobs.
3. Use `pull_request_target` only for trusted automation that does not execute fork code.
4. Keep `permissions:` least-privilege and never print secret values.

---

## Safe workflow patterns

### 1) Untrusted checks (no secrets)

```yaml
name: PR checks (untrusted)
on:
  pull_request:

permissions:
  contents: read

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run lint/tests (no secrets)
        run: |
          echo "run safe checks"
```

### 2) Privileged workflow logic without running fork code

```yaml
name: PR metadata checks
on:
  pull_request_target:

permissions:
  contents: read
  pull-requests: write

jobs:
  policy:
    runs-on: ubuntu-latest
    steps:
      - name: Validate PR metadata only
        run: echo "check labels/title/body without executing PR code"
```

### 3) Secret access behind environment approval

```yaml
name: Gated integration
on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  integration:
    runs-on: ubuntu-latest
    environment: ci-secrets-gated
    steps:
      - uses: actions/checkout@v4
      - name: Run integration with approved secrets
        env:
          API_TOKEN: ${{ secrets.API_TOKEN }}
        run: |
          echo "run trusted integration flow"
```

---

## Common mistakes to avoid

- Using `pull_request_target` + checkout of fork head + secret usage.
- Granting broad `permissions: write-all`.
- Reusing one environment for unrelated secrets.
- Logging command output that can contain sensitive values.

---

## Acceptance criteria mapping

- **Provide guide when to use which approach**: Decision matrix + “Use when” sections.
- **Focus on constraints and security implications**: Threat model, risks, hard constraints, and anti-patterns.

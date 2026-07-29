# GitHub Actions secrets from forks: decision guide

## Background

Workflows triggered by `pull_request` for pull requests from forks do **not** have access to repository secrets by default.  
This is a security control to prevent untrusted code from exfiltrating secrets.

This guide defines when to use each of the following options:

1. `pull_request` (unprivileged validation)
2. `pull_request_target` (metadata/policy automation only)
3. Environment-gated privileged jobs
4. Fork code with immediate secret access (**not allowed**)

---

## Threat model

Code from a fork PR is untrusted until maintainers review and trust it.

If untrusted code runs in a context that has secrets, secrets can be leaked via:
- logs,
- uploaded artifacts,
- network calls,
- modified scripts/actions.

**Rule 1:** Never run untrusted fork code in a job that has access to secrets.  
**Rule 2:** Secret access must be gated by explicit trust and approval controls.  
**Rule 3:** Use least privilege for both `permissions:` and secret scope.

---

## Option 1: `pull_request` (unprivileged validation)

`pull_request` is the default trigger for validating fork PR code safely, without secrets.

### Use when

- Running linting, formatting, unit tests, static analysis.
- Executing contributor code is necessary.
- No repository/environment secret is required.

### Risks

- Limited coverage for tests requiring protected credentials or external private services.
- Teams may try unsafe workarounds to “enable secrets”.

### Hard constraints

- Keep this path secret-free.
- Use minimal `permissions:` (typically `contents: read`).
- Do not add privileged operations here.

---

## Option 2: `pull_request_target` (metadata/policy automation only)

`pull_request_target` runs in the context of the base repository, so secrets can be available.

### Use when

- Running trusted automation on PR metadata/policy:
  - title/body/label validation,
  - comment automation,
  - non-code policy checks.
- You can avoid checking out and executing fork PR code.

### Risks

- **High risk** if the workflow checks out PR head (`github.event.pull_request.head.sha`) and runs it with secrets.
- Any execution of contributor-controlled code in this context may leak secrets.

### Hard constraints

- Do **not** execute fork code in secret-bearing jobs.
- Avoid `actions/checkout` of PR head in privileged contexts.
- Keep permissions minimal and steps narrowly scoped.

---

## Option 3: Environment-gated privileged jobs

Environments provide protection rules (for example, required reviewers) before jobs can access environment secrets.

### Use when

- A job requires secrets (deploy, publish, privileged integration tests).
- You need explicit human approval before secret usage.
- You want auditable access controls.

### Risks

- If approval is granted without validating what will run, untrusted code may still run with secrets.
- Overly broad environment design can overexpose secrets.

### Hard constraints

- Require reviewers on sensitive environments.
- Scope secrets per environment and purpose.
- Run untrusted checks first (`pull_request`), then run gated privileged jobs.

---

## Option 4: Fork code + immediate secret access (disallowed)

This means executing untrusted fork code directly in a secret-bearing context without trust gates.

### Status

**Do not use.**

### Why disallowed

- This is the direct path to secret exfiltration.
- It defeats the security boundary for fork contributions.

---

## Decision matrix and repository standard

| Option | Typical use case | Fork PR | Secrets needed | Runs untrusted fork code | Gate / control | Recommendation |
|---|---|---|---|---|---|---|
| **1. `pull_request` (unprivileged)** | Lint, unit tests, static analysis | Yes | No | Yes | No secrets, minimal `permissions` | **Default for fork PR validation** |
| **2. `pull_request_target` (metadata/policy only)** | Labeling, commenting, policy checks | Yes | Sometimes | **No** | Never checkout/execute PR head in privileged jobs | **Use only for trusted automation** |
| **3. Environment-gated job** | Deploy/publish/integration with secrets | Yes/No | Yes | Only after trust decision | Required reviewers + scoped environment secrets | **Preferred for secret-dependent execution** |
| **4. Fork code + immediate secrets** | Run contributor code directly with secrets | Yes | Yes | Yes | N/A | **Do not use** |

### Repository standard

1. Use `pull_request` for all untrusted validation without secrets.
2. Use `pull_request_target` only for trusted metadata/policy automation that does not run fork code.
3. Use environment protection rules for all secret-dependent jobs.
4. Never run untrusted fork code in any secret-bearing context.
5. Apply least privilege to `permissions:` and secret scope in every workflow.

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

### 2) Trusted metadata automation (`pull_request_target`) without running fork code

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

- Using `pull_request_target` and checking out PR head, then using secrets.
- Granting broad `permissions: write-all`.
- Reusing one environment for unrelated secrets.
- Approving privileged jobs before validating what code will run.
- Printing sensitive values or secret-derived output to logs.

---

## Acceptance criteria mapping

- **Provide guide when to use which approach**:  
  Covered by the 4-option model, per-option “Use when”, and the decision matrix.
- **Focus on constraints and security implications**:  
  Covered by threat model, risks, hard constraints, disallowed pattern, and anti-patterns.

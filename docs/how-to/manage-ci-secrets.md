# How to Manage CI Secrets

This guide covers creating, scoping, rotating, and replacing static secrets with federated identity (OIDC) in S-CORE CI workflows.

## Secret scopes in GitHub Actions

GitHub provides three secret scopes:

| Scope | Where set | Who can use it |
|---|---|---|
| Repository | Repository → Settings → Secrets | Workflows in that repository |
| Organization | Org → Settings → Secrets | Workflows in repositories where the secret is granted |
| Environment | Repository → Settings → Environments | Workflows that target that environment |

**Default to the narrowest scope that works.** Use environment secrets for deploy-time credentials that should be gated by environment protection rules (e.g. requiring a reviewer before a secret is accessible).

## Create a new secret

1. Decide on the scope (repository, organization, or environment).
2. Go to the appropriate Settings → Secrets page on GitHub.
3. Click **New secret** (or **New repository secret** / **New organization secret**).
4. Give the secret a clear, uppercase, underscore-separated name (e.g. `REGISTRY_TOKEN`).
5. Paste the secret value and save.

To reference it in a workflow:

```yaml
env:
  MY_TOKEN: ${{ secrets.MY_TOKEN }}
```

Or pass it directly to a step:

```yaml
- name: Authenticate
  run: some-tool login
  env:
    TOKEN: ${{ secrets.MY_TOKEN }}
```

## Rotate a secret

1. Generate the new credential in the upstream service (GitHub PAT, API key, etc.).
2. Update the secret value in GitHub Settings.
3. Verify that workflows using the secret still succeed after rotation.
4. Revoke the old credential.

Rotation should happen on a regular cadence (e.g. annually for long-lived PATs) or immediately when a credential is suspected to be compromised.

## Replace a static secret with OIDC

OIDC lets CI jobs request short-lived credentials from a cloud provider instead of storing long-lived static secrets. This is the preferred pattern for cloud access where the provider supports it.

### How it works

```
GitHub Actions job → requests OIDC token from GitHub
                   → exchanges token at cloud provider
                   → receives short-lived credential
                   → calls cloud provider API
```

The cloud provider is configured to trust GitHub's OIDC issuer and to grant access to tokens with specific claims (e.g. the repository name, branch, or environment).

### Example: AWS

1. In AWS IAM, create an OIDC identity provider for `token.actions.githubusercontent.com`.
2. Create an IAM role with a trust policy that allows GitHub tokens from your repository and branch.
3. In the workflow, use the `aws-actions/configure-aws-credentials` action — no static secret needed:

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/my-role
      aws-region: eu-central-1
```

For other providers, the pattern is the same: create the OIDC trust on the provider side, then use the appropriate GitHub Action to request credentials.

## Cross-repository token provisioning

S-CORE workflows sometimes need to act across repositories (e.g. opening a PR in another repo). The `cicd-actions` repository provides a composite action for this:

```yaml
- uses: eclipse-score/cicd-actions/get-app-token@<version>
  with:
    app-id: ${{ secrets.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}
```

This uses a GitHub App instead of a personal access token, which gives better audit trails and allows fine-grained repository-level permissions.

## Least-privilege checklist

Before creating a new secret or token, check:

- [ ] Does this credential need write access, or is read-only sufficient?
- [ ] Can OIDC replace this static credential?
- [ ] Is the secret scoped to the narrowest necessary scope (repo vs. org)?
- [ ] Is there a documented rotation cadence?
- [ ] Is the credential usage visible in workflow logs (without leaking the value)?

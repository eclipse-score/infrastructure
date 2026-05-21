# How to Update the Shared Devcontainer

This guide is for infrastructure maintainers who need to publish a new version of the shared development container image and roll it out to consuming repositories.

The devcontainer image is built and published from [eclipse-score/devcontainer](https://github.com/eclipse-score/devcontainer). Repositories consume it via a `.devcontainer/devcontainer.json` that pins an image version.

## 1. Make the change in eclipse-score/devcontainer

Clone and branch the [devcontainer repository](https://github.com/eclipse-score/devcontainer), then make your change:

- **Adding a tool**: add the installation step to the Dockerfile, pin the version explicitly
- **Updating a pinned tool version**: update the pin in the Dockerfile
- **Changing VS Code extensions**: update the `devcontainer.json` extension list

Run the devcontainer locally to verify the change before pushing:

```bash
# Build the image locally
docker build -t devcontainer-test .

# Smoke-test the tools you changed
docker run --rm devcontainer-test <tool> --version
```

Open a pull request and get it reviewed. CI will build and test the image.

## 2. Publish the new image

After merge, the CI workflow in the devcontainer repository builds and pushes a new image to the GitHub Container Registry:

```
ghcr.io/eclipse-score/devcontainer:<tag>
```

Confirm the image is published:

```bash
docker pull ghcr.io/eclipse-score/devcontainer:<new-tag>
```

## 3. Roll out to consuming repositories

Repositories that pin the devcontainer image need their `.devcontainer/devcontainer.json` updated to the new tag.

**Automated rollout via Dependabot**: repositories with Dependabot configured for Docker image updates will receive an automated PR when a new image is published. Review and merge these PRs.

**Manual update**: for repositories without automated updates, open a PR that changes the image tag:

```json
{
  "image": "ghcr.io/eclipse-score/devcontainer:<new-tag>"
}
```

### Staged rollout

Do not merge updates to all repositories at once. If the new image has a problem, a staged rollout limits the blast radius:

1. Start with low-risk or infrastructure-team-owned repositories
2. Verify builds and dev workflows still work
3. Proceed to the remaining repositories

If a problem is found after rollout has started, consider whether reverting is faster than fixing forward.

## 4. Verify

After rollout, confirm that:

- `bazel build //...` and `bazel test //...` still pass in a representative repository
- `pre-commit run --all-files` succeeds
- Language servers and editor tooling work as expected inside the new container

## Rollback

To roll back to the previous image, revert the `.devcontainer/devcontainer.json` change in the affected repositories (or create a PR that pins the previous tag).

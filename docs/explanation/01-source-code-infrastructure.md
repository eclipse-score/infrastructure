# 1 Source Code Infrastructure 🟠

:::{tip} Looking for practical guides?
This chapter is part of the infrastructure landscape assessment. For step-by-step how-tos and quick references, see the [How-to Guides](../how-to/index.md).
:::

*Infrastructure for hosting and governing repositories consistently across the S-CORE project.*

```{mermaid}
graph TD
    eclipsefdn["`.eclipsefdn`
otterdog config"]
    otterdog["otterdog"]
    github_org["eclipse-score
GitHub organization"]
    repos["Module repositories"]
    template["`eclipse-score/module_template`"]
    github_profile["`.github`
org profile & conformance"]

    eclipsefdn -->|defines org policy| otterdog
    otterdog -->|"applies: branch protection,
required checks, Actions allowlist"| github_org
    github_org -->|hosts| repos
    template -->|bootstraps new| repos
    github_profile -.->|discovery surface| github_org
```

## 1.1 Hosting & Organization 🟡

*Provide a stable, discoverable, and scalable hosting foundation for all S-CORE repositories.*

All S-CORE repositories are hosted on GitHub at [github.com/eclipse-score](https://github.com/eclipse-score), aligned with Eclipse Foundation governance. A shared organization enables organization-level settings, applications, and automation to be managed centrally. The organization profile page ([eclipse-score/.github](https://github.com/eclipse-score/.github)) serves as a discovery surface that links to shared repository inventories, standards, and cross-project guidance.

Discoverability depends not only on hosting location but on repository naming, metadata, topics, and consistent descriptions. Without a shared standard, repositories drift in how they present themselves, which increases onboarding friction as the repository landscape grows.

**Biggest gap**: names dont match bazel modules, topics and metadata missing, horrible descriptions of repos., documentation, HowTos, guidanace.


## 1.2 Repository Provisioning & Lifecycle 🟡

*Infrastructure for creating, initializing, updating, and archiving repositories and executing lifecycle operations. (Otterdog)*

Repository provisioning in S-CORE starts with creating the repository itself and attaching it to the shared organizational governance model. The infrastructure concern here is the durable repository state around creation, ownership, protection, archival, and other lifecycle transitions, not the detailed engineering baseline inside the repository.

Organization-level repository state is still managed centrally. Desired settings such as applications, branch protection, and required checks are defined through the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet), and lifecycle transitions are configuration changes instead of one-off admin actions.

**Biggest gap**: ownership and approval of repository lifecycle changes are not clearly defined end to end (create, archive, delete).

---

## 1.3 Repository Policy Management 🔴

*Infrastructure for managing and synchronizing repository policies such as branch protection, and application thereof at scale. (Otterdog)*

Repository policy covers the organization-level settings that govern how repositories behave: branch protection rules, required status checks, merge strategies, and which GitHub Actions are allowed to run. The infrastructure concern is not each individual rule but the system that makes policy intent explicit, reviewable, and enforceable at scale rather than hidden in per-repository admin pages.

In S-CORE, policy intent is expressed centrally via the infrastructure-as-code tool [otterdog](https://otterdog.readthedocs.io/en/latest/userguide/) in the [S-CORE configuration file](https://github.com/eclipse-score/.eclipsefdn/blob/main/otterdog/eclipse-score.jsonnet). That makes policy changes reviewable as pull requests and exceptions explicit rather than silent. The same mechanism can restrict which GitHub Actions are allowed to run in the organization — an important supply-chain concern because third-party actions execute with the permissions of the workflow that calls them. An allowlist strategy classifies actions as approved, under review, or blocked, and the enforcement mechanism should prevent unapproved actions from running rather than merely warning about them.

**Biggest gap**: there is no common policy definition or enforcement strategy, and the current state of policy across repositories is not well documented or visible. Few repositories apply policies. GitHub Actions allowlisting is not yet implemented or documented as a security baseline.

### 1.3.1 PR Merge Strategy 🟢

S-CORE repositories use GitHub's **Squash and merge** method when merging pull
requests into main. The other methods — **Create a merge commit** and **Rebase
and merge** — are disabled. Exceptions exist.

The guiding principle: the pull request is the unit of review and integration.
The resulting squash commit is the corresponding unit in the permanent main
branch history.

:::{important} GitHub merge methods vs. local Git operations
GitHub's three merge methods are distinct from similarly named local Git operations (`git merge`, `git rebase`, `git rebase -i`).

This policy covers only how an accepted pull request is recorded on main. It
does not prescribe how many commits a contributor creates locally, whether they
use merge or rebase during development, or whether fixup commits appear inside
the PR branch.

After review has started, avoid rewriting published history unless coordinated
with reviewers — it can invalidate commit-based review context.
:::

#### The three strategies

| Method | Result on main | PR boundary marker | Intermediate commits land on main |
|---|---|---|---|
| Create a merge commit | All PR commits + merge commit | Yes (merge commit) ✅ | Yes ❌ |
| **Squash and merge** | One new commit | Yes (squash commit) ✅ | No ✅ |
| Rebase and merge | Each PR commit recreated | No ❌ | Yes ❌ |

##### Create a merge commit

GitHub creates a new commit on main with two parents: the tip of the PR branch
and the previous tip of main. All PR commits land on main as-is, followed by
this merge commit. The result is a non-linear history — `git log --graph` shows
the branch forking off and rejoining.

A PR that synced with main during development (via `Merge branch 'main' into
feature`) will also have those sync merge commits in the history.

*All these commits end up in main history*

:::{mermaid}
%%{init: {'themeVariables': {'fontSize': '11px', 'git0': '#2171b5', 'git1': '#6baed6', 'gitInv0': '#fff', 'gitInv1': '#fff'}}}%%
gitGraph
   commit id: "prev"
   branch feature
   checkout feature
   commit id: "implement"
   checkout main
   commit id: "other PR"
   checkout feature
   merge main id: "sync main"
   commit id: "fix review"
   commit id: "fix review 2"
   commit id: "nit"
   commit id: "address comment"
   checkout main
   merge feature id: "Merge #42"
:::

After merging, main contains all PR commits plus the merge commit. The branch is
visible as a fork in history.

**Pros**

- Preserves the full commit history exactly as developed, including per-author
  attribution.
- The merge commit marks the PR boundary structurally — `git branch -d` detects
  the branch as merged, `git revert -m 1` reverts the entire PR as a unit, and
  `git bisect` can narrow to individual commits within the PR.
- Safe for branches that continue to be used after merging.

**Cons**

- Merge commits from upstream syncs and work-in-progress "fix findings" commits
  both land on main, weakening `git log` unless authors curate commits before
  merging.
- `git bisect` may land on intermediate commits that do not build or pass tests.
- History becomes non-linear, which some tools and people find harder to follow.

##### Squash and merge

GitHub combines all PR commits into a single new commit and appends it to main
as a fast-forward. No merge commit is added — main stays linear. The squashed
commit has a new SHA with no structural link to the original PR branch. The
original PR commits are not ancestors of main: they remain visible in the GitHub
PR view but are not part of the permanent Git history and will not be present in
clones once the branch is deleted.

:::{mermaid}
%%{init: {'themeVariables': {'fontSize': '11px'}}}%%
gitGraph
   commit id: "prev"
   branch feature
   checkout feature
   commit id: "implement"
   checkout main
   commit id: "other PR"
   checkout feature
   merge main id: "sync main"
   commit id: "fix review"
   commit id: "fix review 2"
   commit id: "nit"
   commit id: "address comment"
   checkout main
   commit id: "squash(#42)"
:::

After merging, main contains one new commit per PR. Intermediate commits are
excluded from main history.

**Pros**

- One commit per PR on main — clean, linear, easy to scan and bisect at PR
  granularity.
- Work-in-progress and "fix findings" commits are excluded automatically,
  without requiring local cleanup.
- `git log`, `git bisect`, and `git revert` all operate at PR granularity — the
  meaningful unit for this project.
- No local history curation required before merging.

**Cons**

- The squashed commit has a new SHA — `git branch -d` does not detect the
  original branch as merged.
- Individual commits within the PR cannot be bisected or reverted from main.
- A squash-merged branch should not be reused — start new work from a fresh
  branch based on the updated main.
- Detailed development history depends on the GitHub PR record rather than the
  cloned repository.

To revert a squash-merged PR, use an ordinary revert:

```
git revert <squash-commit>
```

##### Rebase and merge

GitHub replays each PR commit one by one onto the tip of main, creating new
commits with the same content but new SHAs and updated committer information. No
merge commit is added. The result is a linear history with no structural marker
for the PR boundary.

:::{mermaid}
%%{init: {'themeVariables': {'fontSize': '11px'}}}%%
gitGraph
   commit id: "prev"
   branch feature
   checkout feature
   commit id: "implement"
   checkout main
   commit id: "other PR"
   checkout feature
   merge main id: "sync main"
   commit id: "fix review"
   commit id: "fix review 2"
   commit id: "nit"
   commit id: "address comment"
   checkout main
   commit id: "implement '"
   commit id: "fix review '"
   commit id: "fix review 2 '"
   commit id: "nit '"
   commit id: "address comment '"
:::

After merging, main contains each PR commit recreated as a new commit (new SHA,
same content). History is linear but there is no marker for the PR boundary.

**Pros**

- Linear history, with each individual commit landing on main separately.
- Useful when a PR contains genuinely distinct, independently meaningful
  changes.

**Cons**

- All intermediate commits — work-in-progress and "fix findings" — land on main,
  requiring the same local curation discipline as create a merge commit.
- `git bisect` may land on intermediate commits that do not build or pass tests.
- Replayed commits get new SHAs — `git branch -d` does not detect the branch as
  merged, and original commit signatures are not preserved as verified.
- No structural marker for the PR boundary.

#### Why S-CORE uses squash and merge

The typical S-CORE PR has one substantive commit and several "fix findings"
follow-ups. Those follow-up commits are review artifacts — they exist so
reviewers can see what changed in response to feedback. They carry no
independent value in the permanent history of main.

"Create a merge commit" and "rebase and merge" both land those intermediate
commits on main. Avoiding this would require every contributor to manually
curate their branch before merging. Which contradicts reviewability. Squash and
merge produces the desired result consistently:

- one reviewed change
- one commit on main
- one commit to bisect
- one commit to revert
- one PR containing the detailed review and development history

This separates two concerns: the pull request records how a change was developed
and reviewed; the squash commit records the accepted result in the permanent
project history.

#### Commit message

Because the PR title becomes the squash commit title, it should clearly describe
the resulting change... as a PR title should anyway. The PR reference (e.g.
`(#42)`) as added by GitHub should be retained in the final commit title for
easier tracking.

e.g. *Add Windows platform configuration (#42)*

#### Commit history during review

Contributors are not required to produce a polished commit series inside a PR.
Adding separate commits to address review comments is encouraged — reviewers can
then see exactly what changed since the last review round without re-reading the
full diff.

Before review begins, contributors may freely reorganize their local history.
After review begins, force-pushed history rewrites should be avoided. No local
squashing is required - or desired - before merging. GitHub performs the final
squash after approval.

#### Known limitations

##### Multiple authors

A squash merge replaces the individual PR commits with one new commit on main.
This does not itself change copyright ownership or licensing. However, if
attribution is not preserved correctly, it reduces the authorship and
contribution provenance directly visible in the Git history. This may conflict
with S-CORE's licensing and attribution requirements, including the information
maintained in NOTICE files.

Recommendation: In practice, most PRs have one primary author. When multiple
people contribute to the same PR, preserve their attribution using Git's
Co-authored-by trailers. GitHub normally adds these automatically when squashing
commits from multiple authors, but the final commit message should still be
verified before merging.

Working on the same feature does not automatically mean that copyright is
shared. Minor, purely mechanical changes, such as correcting a typo, will often
not constitute a separately copyright-protected contribution.

Existing copyright, DCO, CLA, licensing, and internal IP requirements still
apply. If attribution cannot be represented adequately in one squash commit,
resolve this before merging or split the work into separate PRs.

*Note: We have discussed this with lawyers, but we are not lawyers, and this
documentation is not legal advice. If you have questions about licensing,
copyright, or other legal matters, consult a qualified legal professional.*

##### Distinct topics

A PR should represent one coherent change.
When changes need to remain independently identifiable, revertible, or
releasable, submit them as separate PRs instead.

---

## 1.4 Repository Standards 🟠

*Define, propagate, and measure standard repository elements to reduce unnecessary variation.*

Standards reduce unnecessary variation across the S-CORE repository landscape. To be effective, they need to be centrally defined, technically synchronized into repositories, and measurably adopted. These three concerns — definition, propagation, and conformance visibility — form a complete system only when they are all in place together.

S-CORE has the beginnings of central standards but has not yet closed the loop to synchronized enforcement and visible conformance. The [module_template](https://github.com/eclipse-score/module_template) provides a bootstrap baseline for new Bazel-module repositories, and shared tooling and policy modules define some common expectations. However, these elements do not yet add up to a coherent cross-repository standardization system with automated rollout and drift detection.

**Biggest gap**: standards, synchronization, and conformance visibility are not yet operationalized as one coherent system.

### 1.4.1 Repository Metadata 🟠

*Define standard project metadata such as LICENSE, README, and governance files.*

Metadata expectations exist, but rollout is not yet complete across repositories. Discoverability and governance depend on consistent metadata being present and kept current.

For Bazel modules, [eclipse-score/module_template](https://github.com/eclipse-score/module_template) partially addresses this by giving new repositories a common starting set of metadata and governance files instead of requiring each maintainer to assemble them from scratch. That is useful as a bootstrap baseline, but it only covers repositories that fit the template and it does not by itself keep existing repositories aligned over time.

**Biggest gap**: metadata standards exist only partially in enforceable form, and the current bootstrap support is limited to Bazel-module-style repositories.

### 1.4.2 Tooling Configuration Standards 🟠

*Define shared configuration for linters and development tools.*

Shared conventions are starting to emerge, but not yet synchronized.

The same template also gives Bazel modules a partial starter baseline for repository-local tooling configuration, such as the initial Bazel wiring, editor settings, and starter workflow files. That helps new Bazel-based repositories begin from a more consistent shape, but it is still only a bootstrap aid for one repository class rather than a cross-project standardization mechanism.

Repository-local tooling configuration is only one part of the broader repository-standard surface. Cross-repository collection and publication of repository facts, adoption, and drift belong with [conformance reporting](#conformance-reporting), not as a tooling-only concern.

**Biggest gap**: no clearly enforced baseline/override model exists across repository classes, and the current template-based help is limited to Bazel modules.

### 1.4.3 Synchronization Mechanisms 🔴

*Applying shared standards into repositories through repeatable technical mechanisms.*

Synchronization can be driven by central configuration, reusable templates, generated repository settings, or other automation rather than manual copying. The infrastructure concern is not a single mandated mechanism, but that shared standards can be propagated predictably, reviewed, and rolled out at scale.

Migration support matters alongside synchronization, because existing repositories will not all converge at the same speed. New-repository templates can help with bootstrap, but they are not the same thing as synchronization once repositories already exist and start to drift.

**Biggest gap**: no alignment on a synchronization mechanism.

### 1.4.4 Conformance Reporting 🟠

*Showing which repositories follow the shared baseline and where drift remains.*

- Conformance visibility is necessary if synchronization is meant to be measurable rather than aspirational.
- Adoption and drift should be tracked so migration work can be prioritized instead of discovered reactively.
- Cross-repository reporting should make deviations visible early enough to support planned migration rather than reactive cleanup.
- Cross-repository consistency of standards and related policy expectations is not yet reliably measured.
- A practical reporting tool should be able to collect structured repository facts such as the Bazel version or module baseline in use, whether central reusable workflows such as `cicd-workflows/daily.yml` are consumed, whether `pre-commit` is configured, and where repositories intentionally diverge from the shared baseline.
- One suitable delivery model is generated Markdown stored in [eclipse-score/.github](https://github.com/eclipse-score/.github) and linked from the organization start page at [github.com/eclipse-score](https://github.com/eclipse-score/), so the conformance view becomes part of the normal project discovery surface rather than a hidden internal report.

**Biggest gap**: no definition of what needs to be measured, how to measure it.

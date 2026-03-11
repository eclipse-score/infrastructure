# Repository Standards

Repository standards define the baseline structure and conventions that make S-CORE repositories easier to use and easier to automate.

## Scope

This topic includes:

- naming conventions
- expected baseline files and directory structure
- shared workflow and template usage
- documentation and metadata conventions

It does not replace project-specific technical design or team-level engineering decisions.

## Relevant Tools

- GitHub repository templates
- shared CI workflow references
- baseline documentation and contribution files
- Otterdog-managed defaults where applicable

## Current Signals

Public repositories in the S-CORE organization show clear naming patterns such as `score_*` for core modules and `inc_*` for incubation work. A module template repository is also visible, which suggests that repository bootstrapping and standardization are treated as intentional infrastructure concerns.

## Typical Standards To Document

- required or recommended repository files
- minimum documentation expectations
- how reusable workflows should be referenced
- conventions for module naming and categorization
- how repositories expose ownership and contribution guidance

## Typical Work Items

- reduce drift between repositories by documenting the baseline clearly
- update templates when a better standard emerges
- remove ad hoc setup steps that should be part of the standard
- make standards visible enough that contributors can follow them without guessing

## Practical Principle

Standards should remove avoidable variation. They should not introduce ceremony that makes local development or contribution harder without a clear benefit.
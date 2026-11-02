---
name: commit-message-guidelines
description: >-
  Write and review Git commit messages using the required header format, body,
  and footer conventions, including agent co-author trailers. Use when creating
  a Git commit or drafting, revising, or reviewing a commit message.
---

# Commit Message Format

## Overview

Follow
[Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) as
the baseline. The rules below add personal restrictions and conventions.

Base the message on the changes intended for the commit. When working in a
repository, inspect those changes; for a normal staged commit, inspect the
staged changes. Exclude unrelated changes to the working tree.

Use supplied context to explain motivation. Do not invent rationale, testing
results, issue resolution, or compatibility claims. If the available context
does not establish why a change was made, describe the supported behavior change
without guessing.

Enclose commands, identifiers, and file paths in single backticks throughout the
commit message. See the backticks documentation below for details and
exceptions.

Compose body and footer prose in short lines. Before returning the message,
ensure each prose line is at most 72 characters, including spaces, punctuation,
and backticks. Keep indivisible code references or URLs intact on their own line
when they exceed 72 characters. Keep Git metadata trailers (for instance,
`Signed-off-by`) on one line, even when they exceed 72 characters.

## Commit Message Header

```
<type>[(optional scope)][!]: <short summary>
```

Aim for a header of about 50 characters or fewer; do not exceed 72 characters.

### Type

The type must be one of the following:

| Type       | Description                                        |
| ---------- | -------------------------------------------------- |
| `build`    | Build system or external dependencies              |
| `ci`       | CI configuration or workflows                      |
| `chore`    | Repository maintenance not covered by another type |
| `docs`     | Documentation only                                 |
| `feat`     | New feature                                        |
| `fix`      | Bug fix                                            |
| `perf`     | Performance improvements                           |
| `refactor` | Restructuring without changing behavior            |
| `revert`   | Reversal of an earlier commit                      |
| `style`    | Formatting changes without changing behavior       |
| `test`     | Add or update tests                                |

Choose the type that describes the primary purpose of the change. Supporting
tests or documentation do not change that type: a bug fix with regression tests
is `fix`, and a feature with documentation is `feat`. Use `chore` only when no
more specific type applies.

For a revert, identify the reverted commit by hash in the body and explain why
it is being reverted.

### Scope

The scope should identify the feature or package affected.

Reuse an established scope when one fits. Otherwise, omit the scope. Ask about
introducing a new scope only when it would materially improve clarity.

### Summary

The summary should:

- Use imperative, present tense.
- Start lowercase unless the first word is a case-sensitive identifier or proper
  name.
- Omit the trailing period.

## Commit Message Body

When a body is present, separate it from the header with exactly one blank line.

The body is optional when the header fully explains a straightforward change.
Include a body when motivation, previous and new behavior, or important
constraints add useful context. Avoid repeating the header.

Use natural tense when describing previous behavior.

## Commit Message Footer

Required footers still apply when the body is omitted. Separate the footer
section from the body, or from the header when there is no body, with exactly
one blank line.

### Breaking Changes and Deprecations

Omit the trailing period from the summary on `BREAKING CHANGE` and `DEPRECATED`
lines. Use normal sentence punctuation in the description and migration
instructions below them.

Use the following format for breaking-change footers:

```
BREAKING CHANGE: <short summary>

<description with migration instructions>
```

When a change deprecates supported behavior, include a `DEPRECATED` footer with
a recommended update path.

Use the following format for deprecation footers:

```
DEPRECATED: <short summary>

<description with recommended update path>
```

Any sections following breaking changes or deprecations should be separated by
a single blank line.

### Issue References

Use `Closes` for completed feature or task issues and `Fixes` for resolved bug
reports. Use `References` when an issue or pull request is related but is not
resolved by the commit. Choose one label per issue. Use one issue reference per
line. When multiple label groups are present, list them alphabetically:
`Closes`, then `Fixes`, then `References`.

For a commit that completes feature issue #81 and relates to pull request #93,
the correct format is:

```
Closes: #81
References: #93
```

This is incorrect:

```
References: #81, #93
```

### Attribution Trailers

When applicable, use `Reviewed-by`, `Tested-by`, and `Reported-by` to credit
reviews, testing, and problem reports. Use `Co-authored-by` to credit additional
authors. Use the following format, with one trailer per person and contribution
type:

```
<token>: <name> <<email address>>
```

For each attribution trailer, verify three facts from the supplied context: the
contributor's name, email address, and role. Omit the trailer if any fact is
missing. A user's statement indicating they tested it does not identify an agent
as the tester. Authorship alone does not establish review or testing credit. Use
`Signed-off-by` according to the repository's contribution policy.

When recording changes created by one or more agents, include a `Co-authored-by`
trailer for each contributing agent listed in the
[known agent identities](references/agent-information.md). Follow the identity
and permitted-name rules in the linked reference; omit trailers for unlisted
agents.

An agent qualifies for co-authorship when it contributed to the changes included
in the commit. Drafting or formatting only the commit message does not qualify.

Include only one co-author trailer for each distinct name and email address
pair, even when multiple contributing agents share it.

When amending or squashing commits, preserve existing co-author trailers for
contributions that remain in the resulting changes, subject to the identity
rules above. Existing trailers establish recorded attribution; do not infer
additional roles from them.

Keep issue references and attribution trailers together in one consecutive block
at the end of the message, with no blank lines between them.

## Backticks

Use backticks when referring to a code symbol, such as `enqueue`. Use plain text
when describing the general concept, such as insertion. Keep backticks around
standalone code references, including overlong paths. Leave type, scope, and
trailer labels unquoted.

When referring to these files generally, use the names below without backticks.
Use the exact filename or path in backticks when that detail matters.

| Use       | Avoid                               |
| --------- | ----------------------------------- |
| AGENTS.md | `AGENTS.md`                         |
| CLAUDE.md | `CLAUDE.md`                         |
| README    | `README`, `README.txt`, `README.md` |

## Final Check

Before returning the commit message, verify that it accurately describes the
intended changes and makes no unsupported claims. Check the header and prose
lengths, code quoting, type and scope, breaking-change and deprecation markers,
issue labels, and confirmed attribution against these rules.

## Examples

These examples assume the described facts are established, any scopes used
already exist, and listed agents contributed to the changes.

### Header Only

```
docs: clarify local setup requirements
```

### Header with Agent Co-Author Trailer

```
docs: clarify README setup instructions

Co-authored-by: Codex <noreply@openai.com>
```

### Bug Fix with Regression Tests

```
fix: preserve `0` when applying timeout defaults

A timeout of `0` was replaced by the default, preventing callers from
disabling the timeout. Apply the default only when the value is absent
and add regression coverage for `0`.

Fixes: #26
```

### Revert with Rationale

```
revert: restore synchronous indexing

Revert `7e4b9c2` because background indexing allowed searches to return
stale results immediately after an update.
```

### Breaking Change with Migration Instructions and Trailers

```
feat(api)!: paginate project responses

Large workspaces could exceed the response size limit when listing
projects. Return a bounded page with a cursor for the next request.

BREAKING CHANGE: `GET /projects` now returns an object

Read projects from `items` instead of treating the response as an array.
To fetch the next page, pass `nextCursor` as the `cursor` query
parameter.

Closes: #12
Co-authored-by: Cursor <cursoragent@cursor.com>
```

### Deprecation with Recommended Update Path

```
feat(auth): accept scoped access tokens

Scoped tokens let integrations request only the permissions they need.
Existing API keys continue to work during the transition.

DEPRECATED: legacy API keys

Create a scoped access token in account settings and replace the API key
used by your integration. Send the token in the `Authorization` header
using the `Bearer` scheme.
```

### Multiple Footers and Agent Co-Author Trailers

```
feat(search): add an option to clear all filters

Clearing a complex search required removing each filter individually.
Provide one action that resets the filters and refreshes the results.

Closes: #78
Closes: #90
References: #57
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Claude <noreply@anthropic.com>
Co-authored-by: Cursor <cursoragent@cursor.com>
```

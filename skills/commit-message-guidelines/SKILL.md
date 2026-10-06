---
name: commit-message-guidelines
description: >
  Write and review Git commit messages using the required header format, body,
  and footer conventions, including agent co-author trailers. Use when creating
  a Git commit or drafting, revising, or reviewing a commit message.
---

# Commit Message Format

## Overview

Follow
[Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) as
the baseline. The rules below add personal restrictions and conventions.

Enclose every command, identifier, and file path in single backticks, including
in header and footer summaries. Function names cease to be identifiers when they
are ordinary words: write `enqueue` for the function, or "insertion" for the
generic operation. Keep backticks around standalone code references, including
overlong paths. Leave type, scope, and trailer labels unquoted.

Compose body and footer prose in short lines, aiming for 60 characters. Before
returning the message, ensure each prose line is at most 72 characters,
including spaces, punctuation, and backticks. Keep indivisible code references
or URLs intact on their own line when they exceed 72 characters. Keep Git
metadata trailers (for instance, `Signed-off-by`) on one line, even when they
exceed 72 characters.

## Commit Message Header

```
<type>[(optional scope)][!]: <short summary>
```

Aim for a header of about 50 characters or fewer; do not exceed 72 characters.

Use `!` only for breaking changes. Every `!` header must be paired with a
`BREAKING CHANGE` footer that includes migration instructions.

### Type

The type must be one of the following:

| Type       | Description                             |
| ---------- | --------------------------------------- |
| `build`    | Build system or external dependencies   |
| `ci`       | CI configuration or workflows           |
| `docs`     | Documentation only                      |
| `feat`     | New feature                             |
| `fix`      | Bug fix                                 |
| `perf`     | Performance improvements                |
| `refactor` | Restructuring without changing behavior |
| `test`     | Add or update tests                     |

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

Separate the header from the body with exactly one blank line. Use the body to
explain why the change is needed. When useful, compare previous and new
behavior, using natural tense for previous behavior.

## Commit Message Footer

### Breaking Changes and Deprecations

Omit the trailing period from the summary on `BREAKING CHANGE` and `DEPRECATED`
lines. Code identifiers in these summaries require backticks (for example,
`offset`). Use normal sentence punctuation in the description and migration
instructions below them.

Describe breaking changes using the following format, including migration
instructions:

```
BREAKING CHANGE: <short summary>

<description with migration instructions>
```

Describe deprecations using the following format, including a recommended update
path:

```
DEPRECATED: <short summary>

<description with recommended update path>
```

Any sections following breaking changes or deprecations should be separated by
a single blank line.

### Issue References

Use `Closes` for completed feature or task issues and `Fixes` for resolved bug
reports. Use `References` when an issue or pull request is related but is not
resolved by the commit. Choose one label per issue. When multiple label groups
are present, list them alphabetically: `Closes`, then `Fixes`, then
`References`.

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

Keep issue references and attribution trailers together in one consecutive block
at the end of the message, with no blank lines between them.

## Final Check

Before returning the commit message, check the header and prose lengths, code
quoting in the header, body, and footers, issue labels, and confirmed
attribution against these rules.

## Examples

### Header Only

```
docs: clarify local setup requirements
```

### Breaking Change with Migration Instructions

```
feat(api)!: paginate project responses

Large workspaces could exceed the response size limit when listing
projects. Return a bounded page with a cursor for the next request.

BREAKING CHANGE: `GET /projects` now returns an object

Read projects from `items` instead of treating the response as an array.
To fetch the next page, pass `nextCursor` as the `cursor` query
parameter.
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

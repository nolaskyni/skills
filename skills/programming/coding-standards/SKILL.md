---
name: coding-standards
description: >-
  Apply the user's coding conventions for file structure, formatting, naming,
  language features, types, comments, documentation, and tooling across CSS,
  HTML, JSON, Markdown, Python, shell, TOML, and TypeScript. Use whenever
  writing, editing, refactoring, or reviewing files in these languages.
---

# Coding Standards

## Overview

Use this skill when writing, editing, refactoring, or reviewing code so that it
follows explicit conventions rather than unstated habits. When a codebase
already has its own conventions, follow them over the ones in this skill.

These rules don't apply to code that an agent writes only for agents to use,
such as a throwaway script that checks an idea. They apply to all other code,
including examples shown to the user, wherever the code is stored.

## Language References

Before writing or reviewing a file, read the reference for its language. Read
only the references for the languages you are touching.

When the language reference leaves a relevant style question unanswered, read
the section of its linked guide that answers it. Use the current guide rather
than relying on memory. If it can't be retrieved, tell the user, then follow the
reference and your knowledge of the guide.

The following table lists the reference for each language:

| Language   | Files                                                                  | Reference                  |
| ---------- | ---------------------------------------------------------------------- | -------------------------- |
| CSS        | `*.css`                                                                | `references/css.md`        |
| HTML       | `*.html`                                                               | `references/html.md`       |
| JSON       | `*.json`, `*.jsonc`, `*.geojson`, `*.code-workspace`                   | `references/json.md`       |
| Markdown   | `*.md`                                                                 | `references/markdown.md`   |
| Python     | `*.py`, `*.pyi`                                                        | `references/python.md`     |
| Shell      | `*.sh`, `*.zsh`, `*.fish`, scripts without an extension, startup files | `references/shell.md`      |
| TOML       | `*.toml`                                                               | `references/toml.md`       |
| TypeScript | `*.ts`, `*.tsx`                                                        | `references/typescript.md` |

## Naming

Choose names that read clearly where they are used, not only where they are
defined. Clarity matters more than brevity: a reader must be able to understand
what a name refers to without looking up its definition. Follow these rules for
every name:

- Spell words out. Write `number_of_choices`, not `n_choices` or `num_choices`,
  and `message`, not `msg`. Keep abbreviations that are more familiar than their
  expansions, such as `id`, `url`, and `http`, and conventional short names,
  such as `i` for a loop index or `x` and `y` for coordinates.
- Include every word needed to make the meaning unambiguous, and drop words that
  repeat what the type or surrounding context already says. Write `user.name`,
  not `user.user_name`.
- Name variables, parameters, and types for their role, not their type. Write
  `greeting`, not `string`, and `contacts`, not `contact_list`.
- When a value is a plain number or string, name its unit or format, because the
  type doesn't tell the reader what it measures. Write `timeout_seconds`, not
  `timeout`, and `created_at_utc`, not `created_at`. Spell out units as well,
  such as `sampling_rate_hertz`, not `sampling_rate_hz`, and
  `delay_milliseconds`, not `delay_ms`, unless the abbreviation is more familiar
  than the name, as with `utc`. A count needs no unit when its name says what it
  counts, such as `number_of_samples` or `samples_per_segment`. If the type
  already says this, as a `Duration` or a time-zone-aware `datetime` does, leave
  it out of the name.
- Name functions that have side effects as imperative verb phrases, such as
  `sort()` or `send_request()`. Name functions without side effects for what
  they return, using a noun phrase, such as `distance_to(point)`, or a past
  participle, such as `sorted()`.
- Name Boolean values, and functions that return them, as assertions about their
  subject, such as `is_empty`, `has_children`, or `has_permission(user)`.

Use the case style that the language reference sets for each kind of name, such
as `snake_case` for Python functions. Treat each acronym, initialism, or
abbreviation as one unit with uniform case: all capitals where the word would
start with a capital letter, and all lowercase where it would start with a
lowercase letter or the style is lowercase throughout. The following table shows
examples for each case style:

| Style        | Use                        | Avoid                      |
| ------------ | -------------------------- | -------------------------- |
| `PascalCase` | `EncodeUTF8`, `HTTPServer` | `EncodeUtf8`, `HttpServer` |
| `camelCase`  | `parseURL`, `urlString`    | `parseUrl`, `URLString`    |
| `snake_case` | `parse_json`, `user_id`    | `parse_JSON`, `user_ID`    |

When two capitalized abbreviations meet, keep each in uniform case rather than
changing one to make the boundary visible. If the result is hard to read, add a
word that says how they relate or choose a different name. Write
`HTMLToXMLConverter`, not `HTMLXMLConverter` or `HTMLXmlConverter`.

Keep the exact spelling of names that come from outside the code you are
writing, such as standard library or third-party APIs, even when they don't
follow these rules.

## Comments

Write a comment only when it tells the reader something the code can't: why the
code exists, or why it works the way it does. Don't restate what the code does
when names and structure already make that clear.

Base every stated reason on supplied context, such as the user's instructions,
linked issues, commit history, or existing documentation. The one exception is a
design choice you make in the same change: you can state the reason you made it.
Don't invent rationale, such as compatibility, performance, or workaround
claims, for code whose reasons you don't know. If the context doesn't establish
a reason, omit the comment, or, if the code's behavior isn't obvious, briefly
describe what it does.

Also follow these rules for comments:

- Don't describe the edit itself, such as "Updated to use the new API." That
  belongs in the commit message.
- Don't leave commented-out code.
- When changing code, update or remove any comments it invalidates.

Write comments as complete sentences in present tense, starting with a capital
letter and ending with a period. Keep an identifier's case when it starts a
comment. Short inline comments can be fragments; start a fragment with a capital
letter and omit the final period. Leave tool directives, such as `# noqa`,
exactly as the tool requires.

Write comments as plain text that reads cleanly without rendering. Put
identifiers in backticks, and use `-` bullets or indented code examples where
they help. Don't use markup that only works when rendered, such as bold or
italic emphasis, `[<link-text>](<url>)` links, headings, or tables. State
emphasis in words, and give links as bare URLs.

This formatting applies to line and block comments. For documentation comments
that tools render, such as Python docstrings or JSDoc comments, follow the
language reference.

## Documentation Comments

Documentation comments, such as Python docstrings and JSDoc comments, describe
the interface of a function, class, or module: its parameters, attributes,
return values, and raised errors, often with their types. Linters can check that
the documented parameters match the signature, but not that the types,
descriptions, and stated behavior are still correct, so the comment can become
wrong without anything failing.

Whenever you change a function, class, or module, review its documentation
comment in the same change:

- Add, remove, or rename entries to match the parameters, attributes, and return
  values in the code.
- Update each type to match the signature or type hint.
- Update the errors listed as raised.
- Check that stated requirements and behavior, such as input order or skipped
  values, still hold.
- Update examples so that they still run and show the current output.

## Tooling

Each language reference names the formatter, the linter, and, where the language
has one, the type checker for its files. Where one exists, a configuration file
for each tool is in `assets/`. Existing user authorization applies to the
configuration changes described here; don't ask the user to approve them again.
Use the tools and their configuration as follows:

- When the project configures one of these tools, use that configuration. Don't
  change it, or add rule suppressions to it, without asking the user.
- When the project has no configuration:
  - In a new project that you create, copy into the project root only the
    configuration files that the language references name for the languages the
    project will use. For example, copy `assets/ruff.toml` and `assets/mypy.ini`
    for a Python project, but not `assets/tsconfig.json`. If the folder or
    repository already has files, such as data or a README file, ask the user
    first, as for an existing project.
  - In an existing project, ask the user before adding the configuration. Until
    they agree, pass it on the command line for the files you change.
  - For a single file outside any project, such as a standalone script, pass the
    configuration on the command line instead of copying it.
- Run these tools on every file you change before reporting the work as done. Do
  not format or fix files you didn't otherwise change, because unrelated changes
  make the real change harder to review.
- Fix findings introduced by your changes and existing findings that must be
  resolved to complete the requested change correctly. Report unrelated existing
  findings separately; changing a file doesn't authorize cleaning up the rest of
  it.
- When automatic fixes or formatting could change content outside the requested
  scope, inspect the proposed edits before applying them. Use the tool's change
  preview, or apply it to a temporary copy and compare the result with the
  original. A check that only lists affected files is insufficient. Make scoped
  corrections manually when applying the full result would change unrelated
  content or overwrite user edits.
- When code must break a rule, as when it follows a signature defined elsewhere,
  suppress only that rule on that line, name the rule, and tell the user. Never
  suppress every rule at once.
- Report any finding you couldn't fix.

For every project, also use the `assets/.editorconfig` file under the same
rules. Its `[*]` section sets the encoding, line endings, and default
indentation of every file, and its other sections set the indentation and line
length of each language in the table, so that editors write files as the
formatters do. When you copy the file, keep the `[*]` section and only the
sections for languages the project will use, and remove the patterns for other
languages from shared sections. For example, in a project without TypeScript,
change `[*.{css,geojson,html,json,jsonc,md,toml,ts,tsx}]` to
`[*.{css,geojson,html,json,jsonc,md,toml}]`. When a project starts using a
language that its `.editorconfig` file has no section for, add that section from
`assets/.editorconfig`. In an existing project, ask the user before adding it.
EditorConfig has no command-line option, so until the user agrees to add the
file, follow its settings yourself in files that no formatter covers, such as
YAML files. Oxfmt reads indentation and line width from the `.editorconfig`
file, and its own configuration overrides only the options it sets. Any section
you add to a project's `.editorconfig` file must therefore match the formatter
configuration for the same files.

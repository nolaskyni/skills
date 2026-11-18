---
name: tutoring
description: >-
  Plan, teach, and assess learning across sessions: design and revise learning
  paths toward a subject, project, or paper; teach through adaptive explanations
  and guided practice; and quiz the user on a subject, document, or codebase,
  then report gaps and misconceptions. Use when the user wants to learn or
  understand a topic, practice a skill, revisit earlier learning, be quizzed or
  tested on their understanding, or get a learning path, study plan, or
  curriculum. Not for ordinary factual lookups, routine task updates, or running
  software tests.
---

# Tutoring

## Overview

Help the user build understanding that lasts and that they can use. This skill
works in three modes, each with its own reference file:

- **Planning**: design, resume, or revise a multi-session learning path toward a
  subject, project, or paper. Read the
  [planning reference](references/planning.md).
- **Teaching**: explain topics and guide practice. Read the
  [teaching reference](references/teaching.md).
- **Assessment**: quiz the user and report what their answers demonstrate. Read
  the [assessment reference](references/assessment.md).

## Choose the Mode

Choose the mode from the user's request:

- A request to create, resume, or revise a learning path, study plan, or
  curriculum selects planning.
- A request to be quizzed, tested, or checked on understanding selects
  assessment.
- Any other request to learn, understand, practice, or revisit a topic selects
  teaching.

Teaching includes its own checks of understanding. A check within a lesson
doesn't select assessment.

Read only the reference for the selected mode. When a request asks for more than
one mode, such as a path and its first lesson, use them in the order requested.

When the user asks to switch modes, such as "Quiz me on this" after a lesson,
first pause the current activity: report the results of a partial quiz, or
record the resume point of a lesson. Then read the new mode's reference before
continuing.

Don't switch modes on your own. Offer the next mode instead, such as a quiz
after a lesson or teaching on gaps after a quiz, and wait for the user to
accept.

## Notes

Teaching and assessment share one topic record for each topic. Planning keeps a
separate path record for each learning goal, which links to the topic records.
All three modes use the same configuration.

Keep each mode usable in the conversation without saved notes. Honor an explicit
request not to save without changing the user's recorded saving preference.

### Set Up Saving

At the start of a session, resolve the configuration path using the operating
system and actual environment values. Check the resolved path even when the user
hasn't asked to save notes. Apply workspace restrictions to that path, and read
the configuration if it exists and access is allowed.

Use the following paths:

- On Linux and macOS, read `XDG_CONFIG_HOME` on its own, for example with
  `printenv XDG_CONFIG_HOME`. Use `$XDG_CONFIG_HOME/tutoring/config.json`. If
  `XDG_CONFIG_HOME` is unset, empty, or not an absolute path, use
  `~/.config/tutoring/config.json`.
- On Windows, use `%LOCALAPPDATA%\tutoring\config.json`.

Resolve `~` to the user's home directory and environment variables to their
values. The configuration uses these properties:

- `notesDirectoryPath`: the absolute path to the learning-notes directory.
- `isNoteSavingEnabled`: a Boolean recording the user's saving preference.

If saving is disabled, don't create or update records, and continue in the
conversation. Don't ask again about a recorded saving preference unless the user
changes it.

If configuration is missing, use established choices for the saving preference
and notes location, asking only for information still missing.

When saving is enabled, use the user's selected folder. If they select Obsidian,
offer a `Learning` folder inside their existing vault and verify that the vault
exists. Otherwise, offer an ordinary `Learning` folder in their `Documents`
directory. Obsidian isn't required. Follow another location the user chooses.

When no location is recorded or chosen, a request to save doesn't choose one.
Offer the default and wait for the user's choice before creating directories,
writing the configuration, or saving a record.

Resolve the selected notes directory to an absolute path and create it if it
doesn't exist. Create the configuration's parent directory if needed, then write
`notesDirectoryPath` and set `isNoteSavingEnabled` to `true`.

When saving is disabled, record `isNoteSavingEnabled: false`.
`notesDirectoryPath` is optional while saving is disabled; don't require a
directory merely to record that preference.

Read back and parse the configuration to verify the recorded preference and
path. Report setup failures without implying that persistence is ready. Keep
personal paths out of the skill itself.

Check that the configuration is valid and the selected directory is accessible.
If configuration is invalid or a configured directory is missing or
inaccessible, report the problem. Don't silently choose another location.
Continue without saving until the problem is resolved, and make that limitation
clear.

### Find and Update Records

Within the selected directory, find and read the existing record before
continuing: the topic record when teaching or assessing, and the path record
when planning. If several records might match, ask which to use.

When no record exists, create one: a topic record named after the topic, or a
path record named for the learning goal and distinct from topic records. Don't
overwrite an unrelated file with the same name.

Use `coding-standards` for the destination's Markdown conventions when it's
available; otherwise, follow the existing notes' conventions. Read the selected
template before creating a record. For Obsidian records, use the Obsidian
template, name the file in title case with spaces, and start sections at `#`
without a title heading or `title` property. For ordinary Markdown files, use
the plain Markdown template. For a new ordinary Markdown record, pass the
formatter configuration from `coding-standards` explicitly when no project
configuration applies.

Preserve existing user content and structure. If the user chooses another
location or format, follow that choice.

Read the current file before editing it so you preserve the user's changes.
After creating or updating a record, read back the changed portions to confirm
that the intended update was written. Report the file's full path. If saving
fails, say so rather than implying that progress was preserved.

For the structure of a topic record, read the
[topic records reference](references/topic-records.md). The planning reference
describes path records.

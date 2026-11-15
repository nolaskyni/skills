---
name: learning-path
description: >-
  Design, resume, and revise multi-session learning paths for studying a
  subject, completing a project, or understanding a paper. Use when the user
  asks for a learning path, study plan, curriculum, or sequence toward a
  learning goal. Not for a focused explanation, factual lookup, or quiz that
  doesn't ask for a learning path.
---

# Learning Path

## Overview

Build an adaptable sequence toward what the user wants to understand or do. Keep
the overall path coarse and make the next milestone concrete. Revise the
sequence as learning evidence and the user's goals change.

This skill handles planning. Use `teach` for instruction and `quiz` for
assessment when available. If either is unavailable, provide the requested help
directly without requiring installation.

The path is guidance, not an access restriction. If the user requests an
advanced topic before planned prerequisites are complete, follow that request
and offer relevant prerequisite support without requiring completion first.

## Establish the Destination and Starting Point

Use the request, prior context, and available learning records to establish the
following:

- **Destination**: what the user wants to understand or be able to do, including
  any subject emphasis, project, or paper the path serves.
- **Starting point**: relevant prior knowledge and experience. Distinguish
  self-reported background from understanding demonstrated in earlier work.
- **Constraints**: available study time, deadlines, and limits on the scope.

Ask only about missing information that would materially change the path. State
reasonable assumptions for the rest and provide a useful initial plan.

For a project or paper, connect the learning outcomes to that destination rather
than expanding the path into a general subject curriculum.

Treat outcomes and time estimates as planning targets, not promises of
completion. When the destination appears too large for the available time,
explain the tradeoff and offer a narrower scope.

## Build the Milestone Sequence

Organize the path around observable outcomes rather than a list of topics or
readings. Include prerequisites that support the destination, and order
milestones so that later work builds on earlier outcomes.

Present the initial path in this order:

1. **Destination and constraints**: summarize the intended outcome, starting
   point, and available time.
2. **Milestone overview**: give a coarse sequence. For each milestone, state
   what the user aims to explain or do and which earlier outcomes it depends on.
3. **Next milestone in detail**: specify its outcome, relevant prerequisite
   support, practice, learning resources, and checkpoint. End with a concrete
   first action.

Give the next milestone more detail than distant milestones. Leave later session
plans provisional rather than specifying every future lesson, exercise, and
reading before learning evidence is available.

Use checkpoint evidence to decide whether to continue, add support, or revise
the sequence. Completing a reading or covering a lesson doesn't by itself
demonstrate the milestone outcome.

## Select Resources, Practice, and Checkpoints

For the next milestone, choose a small set of learning resources that support
its outcome and fit the user's starting point and available time. For each
resource, identify the relevant portion and explain what it helps the user
understand or do. Prefer a targeted selection over assigning an entire book,
course, or reading list.

Check that recommended resources exist and support the stated purpose. If you
can't verify a resource or its relevant portion, make that limitation explicit
rather than inventing a title, link, or section reference.
Take each title, chapter or section number, and time estimate from the content
you retrieved, not from memory. If the retrieved content doesn't show a number
clearly, refer to that portion by its title instead.

Pair the resources with practice that uses the milestone's knowledge or skill.
State what the user will produce, explain, or investigate rather than assigning
reading alone.

Define a checkpoint that tests the milestone outcome through observable work or
an explanation. State what evidence would support moving on and what would call
for more support. Use `teach` and `quiz` for the learning and assessment
workflows described in the Overview; don't reproduce those workflows in the
path.

## Save the Path

Keep the path usable in the conversation without requiring saved notes. Honor an
explicit request not to save without changing the user's persistent saving
preference.

Use the learning configuration shared with `teach` and `quiz`. Resolve its path
from the operating system and actual environment values:

- On Linux and macOS, read `XDG_CONFIG_HOME` on its own. If its value is an
  absolute path, use `$XDG_CONFIG_HOME/learning/config.json`. Otherwise, use
  `~/.config/learning/config.json`.
- On Windows, use `%LOCALAPPDATA%\learning\config.json`.

Resolve environment variables and the home directory before accessing the path.
Apply workspace restrictions, and read the configuration if it exists and access
is allowed. It uses these properties:

- `notesDirectoryPath`: the absolute path to the learning-notes directory.
- `isNoteSavingEnabled`: a Boolean recording the saving preference.

When saving is disabled, don't create or update learning records or ask again
about the recorded preference. Continue planning in the conversation.

If configuration is missing, use established choices and ask only for the saving
preference or location still needed. Don't require a directory when saving is
disabled.

When saving is enabled, use the user's selected directory. For Obsidian, offer a
`Learning` folder inside an existing vault and verify that the vault exists.
Otherwise, offer a `Learning` folder in their `Documents` directory. Follow
another location the user chooses.
When no location is recorded or chosen, a request to save doesn't choose one.
Offer the default and wait for the user's choice before creating directories,
writing the configuration, or saving the path.

Create the selected notes directory and configuration parent directory if
needed. Record the saving preference and, when enabled, the absolute notes
directory in the configuration. Read back and parse the configuration to verify
the recorded values.

If configuration is invalid or a configured directory is missing or
inaccessible, report the problem and continue without saving. Don't silently
choose another location or imply that persistence is ready.

Within the selected directory, find and read the existing path record before
updating it. If several records could match, ask which to use. When none exists,
create a separate record named for the learning goal, distinguishing it from
topic notes. Don't overwrite an unrelated file.

Use `coding-standards` for the destination's Markdown conventions when
available; otherwise, follow the existing notes' conventions. Preserve user
content and structure.

After creating or updating a path record, read back the changed portions to
verify the intended content. Report its full path. If saving fails, say so
rather than implying that the path was preserved.

## Structure the Path Record

For a new path record, use the following sections:

| Section                        | Contents                                                                                                        |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Destination                    | What the user wants to understand or do, including the subject emphasis, project, or paper.                     |
| Starting Point and Constraints | Relevant background, evidence already available, study time, deadlines, and scope limits.                       |
| Milestones                     | The coarse sequence of outcomes and dependencies, with concise progress summaries.                              |
| Next Milestone                 | The detailed outcome, prerequisite support, resources, practice, checkpoint, and first action.                  |
| Topic Records                  | Links to existing topic records, identifying which milestones they inform.                                      |
| Revision Log                   | Brief dated entries stating what changed in the path and why, with links to supporting evidence when available. |

Keep planned work distinct from material covered and understanding demonstrated.
In progress summaries, identify assistance and unassessed outcomes rather than
reducing each milestone to a completed checkbox.

Link to the topic records used by `teach` and `quiz` for detailed explanations,
session logs, and learning evidence. Keep only the summary needed to explain the
planning decision in the path record. Don't copy the topic logs or create empty
topic records merely to fill the links section.

When no topic record exists, use available conversation evidence and state what
remains unknown. A missing record doesn't prevent planning.

For an existing path, map this information to the user's structure rather than
imposing these headings or reorganizing unrelated content.

## Resume and Revise the Path

When resuming, read the existing path and the topic records relevant to the next
milestone or requested revision. Use their objectives, current understanding,
open gaps, and resume points. Follow links to session evidence when needed to
understand a progress judgment.

Reconcile the recorded next step with the user's current goal, constraints, and
available evidence. Preserve the destination and unaffected milestones unless
the user's request or new evidence calls for changing them. Don't restart the
entire path merely because a new planning session begins.

Use independently demonstrated outcomes to avoid unnecessary repetition. For
assisted or unassessed outcomes needed by the next milestone, plan a fresh check
before deciding what support is needed. Don't treat assistance as independent
understanding or missing evidence as a demonstrated gap.

Revise the relevant milestone outcomes, dependencies, resources, practice, or
time estimates when evidence or goals change. Give the revised next milestone
the same concrete detail as an initial next milestone, and explain what changed
and why.

When saving is enabled, update the path's progress summaries and Next Milestone,
and add a dated Revision Log entry for substantive changes. Link to supporting
topic evidence rather than copying session logs. Preserve earlier revision
entries, and verify the saved changes as described in the "Save the Path"
section.

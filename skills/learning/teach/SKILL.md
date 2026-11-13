---
name: teach
description: >-
  Teach topics through adaptive explanations, guided practice, and review. Use
  when the user wants to learn or understand a subject, practice a skill, or
  revisit earlier learning. Ordinary factual lookups and routine task updates
  don't require a tutoring session.
---

# Teach

## Overview

Help the user build understanding that lasts and that they can use, instead of
only covering material. Clear explanations feel productive but fade quickly
unless the learner does the thinking. Explain briefly, then have the user
recall, explain, predict, or apply what they just learned. Use teaching
techniques that are supported by evidence. Don't tailor lessons to supposed
learning styles.

## Establish the Learning Target

Use the request, prior context, and existing topic notes to establish the
following:

- **Topic**: what the user wants to learn, narrowed to fit the session.
- **Goal**: what they need to understand or be able to do afterward.
- **Starting point**: knowledge demonstrated in earlier answers or work. When
  that evidence is missing, use a brief diagnostic question rather than relying
  only on a self-rating.
- **Time**: the available session length and whether the user wants continued
  study across sessions.

Ask only about missing information that would materially change the lesson.
State reasonable defaults for the rest and begin.

Don't make a diagnostic a prerequisite to a clear request for an explanation.
Explain the requested idea, then use the user's response to adjust the depth and
support.

For a structured lesson, state a few learning objectives as things the user will
be able to explain or do. For a focused explanation, use the requested outcome
directly rather than expanding it into a course.

When resuming, use the recorded resume point and the user's current goal. Don't
require clearing unrelated gaps before teaching the requested material.

## Build an Accurate Model

Start from knowledge the user has demonstrated. Connect each new idea to that
knowledge and explain the relationship. Give the overall structure before
introducing details.

Use concrete examples to establish meaning, then connect them to the general
principle. Vary examples and include non-examples to show where the principle
applies and where it doesn't. Choose examples-first or principle-first according
to the user's goal and demonstrated knowledge.

When using an analogy, explain both the correspondence and where it stops
applying. Distinguish a simplified teaching model from the fuller account.

For mathematical material, define symbols and state assumptions before using
them. Explain why important steps in a derivation are valid, and identify
approximations or restrictions on the result. Connect equations to the concepts
they express rather than presenting algebra alone.

Address misconceptions by explaining the incorrect idea, why it can seem
plausible, and the evidence or reasoning that corrects it. Don't attribute a
misconception to the user unless their answers support that judgment.

Check uncertain claims against reliable sources. Distinguish established
knowledge, interpretation, and unresolved questions. Give source references for
further study and make uncertainty explicit.

## Use Diagrams Purposefully

Use a visual when it clarifies the structure, process, or relationship being
taught. Choose the representation that fits: Mermaid for compact flows,
dependencies, sequences, and states; tables for comparisons; plots for
quantitative relationships; and sketches when spatial layout matters.

Keep each visual focused on one idea. Explain its notation, labels, and
connections, including what arrows represent. Relate it to the verbal
explanation and identify simplifications that might mislead the learner.

Use visuals in practice by asking the user to trace a process, predict what
changes, or explain a relationship. Accept answers in words unless diagram
construction or notation is itself the learning objective.

Check that the visual agrees with the explanation. Inspect its rendered form
when rendering is available. Otherwise, provide a readable text alternative
rather than relying on diagram source alone.

## Teach in Manageable Steps

Introduce one idea at a time. Choose from the following techniques according to
the learning objective and the user's demonstrated knowledge, rather than
applying every technique in every lesson:

- **Worked examples with fading**: for an unfamiliar procedure, demonstrate a
  solution and explain the important decisions. Then leave some steps for the
  user before moving to independent practice. Skip support they have already
  shown they don't need.
- **Self-explanation**: ask the user to explain why a step or conclusion
  follows. Focus on important or uncertain reasoning rather than requiring
  explanations of every routine step.
- **Elaborative interrogation**: ask why a fact holds or how it connects to
  something the user already knows. Check their explanation and correct
  connections that don't hold.
- **Retrieval practice**: ask the user to recall, explain, predict, or apply an
  idea before showing the answer. Distinguish independent retrieval from
  repeating an explanation or following a supplied solution.
- **Interleaving**: after the user can handle problem types separately, mix them
  so they practice choosing an approach as well as carrying it out.
- **Spaced practice**: revisit earlier material after a delay. Use a fresh
  question or application to check what the user can retrieve; rereading notes
  alone doesn't establish that they remember it.

Keep explanations short enough to leave room for practice. When the user
struggles, use their answer to identify the difficulty and adjust the support.
Explain directly when they lack the knowledge needed to reason further or ask
for an explanation.

### Pause or Change Direction

Let the user skip an exercise, pause, stop, or change topics without requiring a
closing exercise. Don't infer a knowledge gap from a skipped or unanswered
exercise.

When the user pauses or stops, briefly identify what was covered, what remains
uncertain, and where to resume. Honor an explicit request to stop without a
summary. Save the stopping point according to the "Notes" section.

When the user returns, use their current goal, the session context, and the
topic record to resume rather than restarting setup. If they change topics,
follow that direction and preserve unfinished work in the original topic's
record when saving is enabled.

## Check Understanding and Respond

Check understanding with short questions that ask the user to recall, explain,
predict, or apply. Ask one question at a time and wait for the answer. Don't
rely on "Does that make sense?" as evidence of understanding.

Judge the reasoning expressed in the answer against the material and reliable
sources. Clarify ambiguous answers before drawing conclusions.

Respond to the evidence:

- **Correct**: confirm briefly, then move on or increase the difficulty.
- **Partly correct**: identify what is right, then ask about the missing part.
- **Misconception**: explain the incorrect reasoning and its correction, then
  check the idea with a fresh question.
- **Stuck**: give hints one at a time, from general to specific. Explain
  directly when the user lacks a prerequisite or requests the answer.

After assistance, use a fresh question or application to check independent
understanding. Repeating a supplied answer doesn't establish it.

For mathematical answers, distinguish difficulty with notation from difficulty
with the concept. Accept an explanation in words unless the notation itself is
being learned or assessed.

To check confidence calibration, ask for confidence before giving feedback and
compare it with demonstrated performance. Don't treat confidence as evidence of
correctness.

Adjust the pace to the answers. Revisit prerequisites after repeated errors, and
skip support the user has demonstrated they don't need.

## Notes

Use one shared topic record across teaching and assessment sessions. Each skill
can read and update that record without requiring the other skill to be
installed.

### Find the Topic Record

At the start of a learning session, resolve the configuration path using the
operating system and actual environment values. Check the resolved path even
when the user hasn't asked to save notes. Apply workspace restrictions to that
path, and read the configuration if it exists and access is allowed.

Use the following paths:

- On Linux and macOS, read `XDG_CONFIG_HOME` on its own, for example with
  `printenv XDG_CONFIG_HOME`. Use `$XDG_CONFIG_HOME/learning/config.json`. If
  `XDG_CONFIG_HOME` is unset, empty, or not an absolute path, use
  `~/.config/learning/config.json`.
- On Windows, use `%LOCALAPPDATA%\learning\config.json`.

Resolve `~` to the user's home directory and environment variables to their
values. The configuration uses these properties:

- `notesDirectoryPath`: the absolute path to the topic-notes directory.
- `isNoteSavingEnabled`: a Boolean recording the user's saving preference.

If saving is disabled, don't create or update notes. Don't ask again about a
recorded saving preference unless the user changes it.

If configuration is missing, use established choices for the saving preference
and notes location, asking only for information still missing.

When saving is enabled, use the user's selected folder. If they select Obsidian,
default to a `Learning` folder inside their existing vault and verify that the
vault exists. Otherwise, offer an ordinary `Learning` folder in their
`Documents` directory. Obsidian isn't required.

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
If configuration is invalid or a previously configured directory is missing or
inaccessible, report the problem. Don't silently choose another location.
Continue the lesson or assessment without saving until the problem is resolved,
and make that limitation clear.

Within the selected directory, find and read the existing topic record before
continuing the topic. If several records might match, ask which to use. Create a
note named after the topic when no record exists; don't overwrite an unrelated
file with the same name.

Use `coding-standards` for the destination's Markdown conventions. Read the
selected template before creating a note. For Obsidian notes, use the Obsidian
template, name the file in title case with spaces, and start sections at `#`
without a title heading or `title` property. For ordinary Markdown files, use
the plain Markdown template. For a new ordinary Markdown note, pass the
formatter configuration from `coding-standards` explicitly when no project
configuration applies.

Preserve existing user content and structure. If the user chooses another
location or format, follow that choice.

### Structure the Topic Record

For new notes, use the
[Obsidian template](assets/obsidian/topic-note-obsidian.md) or the
[plain Markdown template](assets/topic-note-markdown.md).

Use the following sections for new topic notes:

| Section               | Contents                                                                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Objectives            | What the user wants to understand or be able to do.                                                                          |
| Key Ideas             | Concise explanations, definitions, assumptions, and source references.                                                       |
| Examples              | Worked examples, applications, diagrams, or derivations covered during learning.                                             |
| Current Understanding | What the user has demonstrated independently, what required assistance, and what remains unassessed or ungraded.             |
| Open Gaps             | Demonstrated gaps and misconceptions, with discovery dates and links to the supporting session evidence.                     |
| Resume Point          | Where the session stopped and the next question, exercise, or concept to revisit.                                            |
| Log                   | Dated entries recording what was taught or assessed, the user's responses, assistance supplied, and the resulting judgments. |

Keep the current-state sections concise and update them as learning progresses.
Keep the dated log as the supporting history rather than copying the full
conversation.

For existing notes, map this information to the user's structure rather than
imposing these headings or reorganizing unrelated content.

### Update and Verify Notes

When saving is enabled, update the topic record after a completed exercise, a
change in demonstrated understanding, or a pause or end to the session. Read the
current file before editing so you preserve user changes.

Record evidence rather than inferred mastery. Treat copied work and answers
completed with hints, corrections, or a supplied solution as assisted. Record
independent evidence from a fresh attempt without that support. Keep skipped
material unassessed and unresolved judgments ungraded.

During assessment, record answers and assistance without putting deferred
judgments or unrevealed solutions into learner-visible notes. Add that feedback
at the selected feedback time.

Mark an open gap resolved only after a fresh, unassisted question or application
demonstrates understanding. Preserve the earlier evidence and record the
resolution and its date.

If an agent error affected the record, correct the current understanding and add
a dated correction explaining which earlier judgment changed.

Update the resume point and append a dated session entry. After saving, read
back the changed portions to confirm that the intended update was written.
Report the updated file's full path. If saving fails, say so rather than
implying that progress was preserved.

## Consolidate and Revisit

At the end of a lesson, invite the user to summarize the main ideas from memory.
Correct and complete their account. For a focused explanation, offer a brief
check without requiring a closing exercise.

Update the topic record according to the "Notes" section. Distinguish material
covered from understanding demonstrated, and preserve unresolved questions and
the resume point.

Suggest spaced review across later sessions, for example the next day, a few
days later, and a week later. Present these as example intervals, not a fixed
schedule. Leave the user to initiate the review.

When the user returns, read Objectives and Resume Point to establish the goal
and stopping point. Use Current Understanding and Open Gaps to select review
material related to that goal. Check the dated Log for the evidence behind those
judgments, and use Key Ideas and Examples for explanations and source
references. Ask for recall or application before showing the explanation again.
Don't require clearing unrelated gaps before continuing.

When the user requests an assessment, use `quiz` when available. Otherwise,
assess the agreed scope directly, follow the requested feedback timing, and
distinguish independent understanding, assistance, and unassessed material.

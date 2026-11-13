---
name: quiz
description: >-
  Assess the user's understanding of a topic with questions, then report what
  they understand, where the gaps are, and which misconceptions to correct.
  Topics can be any subject, a document, or a codebase. Use when the user asks
  to be tested, quizzed, or checked on their understanding. Intended for
  assessment and practice rather than introducing a new subject.
---

# Quiz

## Overview

Assess what the user can explain and do, rather than what they have read or find
familiar. Match questions to their goal and judge answers against the material
or reliable sources.

Distinguish assessment of independent understanding from practice with feedback.
Hints, corrections, and explanations change what later answers demonstrate.
Report those answers as assisted, and keep unassessed material separate from
demonstrated gaps.

Offer explanations or practice on gaps afterward. Use the `teach` skill when
available; its absence doesn't prevent you from providing help.

## Set the Scope

Use the request and prior context to establish the following:

- **Material**: the subject, document, or part of a codebase to assess, and the
  boundaries of the test.
- **Purpose**: what the user needs to demonstrate, such as readiness for an
  exam, understanding a paper, or explaining code before running it.
- **Length**: the requested number of questions, or five by default.
- **Mode**: assessment with feedback at the end by default, or practice with
  feedback after each answer. A request for immediate feedback selects practice.

Ask only about missing information that would materially change the test. State
reasonable defaults for the rest and begin without requiring confirmation.

In assessment mode, defer correctness judgments, corrections, answer keys, and
teaching until the end. In practice mode, give brief feedback after each answer
and allow another attempt. If the user changes modes, follow their request and
distinguish answers given before and after assistance.

Read existing topic notes when available. Within the requested scope, sample
relevant open gaps and revisit previously resolved gaps. Don't let unrelated
gaps displace the material the user asked to assess.

## Write Good Questions

Match each question to the learning objective. Include recall when facts,
terminology, or fluent retrieval matter. To assess understanding, ask the user
to do one of the following:

- Explain a concept in their own words.
- Predict an outcome, including what changes when an assumption fails.
- Trace a process, derivation, or flow of data.
- Justify a choice of method or design and explain its tradeoffs.
- Find the flaw in an argument, derivation, or description.
- Apply an idea to an unfamiliar case.

Avoid trivia unrelated to the objective, trick questions, and wording that gives
away the answer. Prefer free-response questions. When using multiple-choice
questions, make the incorrect options reflect plausible misconceptions.

Base questions on the supplied material or reliable sources. For a document or
codebase, read the relevant passages or code before writing questions.

Before asking a question, establish what makes an answer acceptable and what
evidence supports that judgment. For questions with a definite answer, verify
the answer and reasoning. For open-ended questions, establish a rubric that
allows defensible alternatives.

Use verification appropriate to the subject:

- Check factual claims and interpretations against relevant sources, including
  their context, assumptions, and limitations.
- Check calculations and technical claims through a suitable method, such as
  substitution, a separate derivation, or executing relevant code.
- For interpretive answers, assess support from the material and the reasoning
  rather than agreement with one preferred interpretation.
- For practical skills, assess observable work against explicit criteria.

An agent's confidence or another agent's agreement isn't sufficient
verification. Check for missing cases, conflicting evidence, and valid
alternative answers before using the key or rubric.

If you can't establish a defensible basis for assessment, choose another
question. If uncertainty emerges after asking, leave the item ungraded until it
is resolved. Don't record an unresolved judgment as a learner gap.

### Mathematical Questions

- Make the question unambiguous about the quantities, domain, and given
  assumptions.
- Define notation unless interpreting it is being tested.
- Accept equivalent expressions and valid alternative methods.
- Distinguish notation difficulties from conceptual errors.

Verify these questions and judge their answers by the same rules as other
questions.

### Diagram-Based Questions

Use a diagram when interpreting structure or relationships serves the learning
objective, such as tracing a state transition or finding an incorrect
connection. Choose the representation that fits: Mermaid for compact flows,
dependencies, sequences, and states; a plot for quantitative relationships; or a
sketch when spatial layout matters.

Keep the diagram legible. Explain unfamiliar notation unless that notation is
being tested. Accept answers in words unless constructing a diagram is part of
the objective, and distinguish notation difficulties from gaps in subject
knowledge.

Check labels, annotations, and visible diagram source for answer leakage.
Withhold corrected or completed diagrams until the selected feedback time. If
the user requests help, record the assistance as you would another hint.

Check that the diagram agrees with the intended question and answer. Inspect the
rendered result when rendering is available. Otherwise, provide an equivalent
readable text representation that preserves the question without supplying its
solution.

## Run the Test

Ask one question at a time, identify the topic it covers, and wait for the
user's answer before continuing.

Don't give hints unless the user requests help. Keep the initial answer separate
from later attempts, and record what assistance was supplied. In assessment
mode, a requested hint applies to that question; it doesn't change the feedback
timing for other questions.

Accept "I don't know" as an answer without pressuring the user to guess. Adjust
difficulty to the answers: probe further after strong answers and return to
fundamentals after answers that reveal gaps.

When feedback is deferred, acknowledge answers without indicating whether they
are correct. Keep clarification questions neutral so they don't reveal the
missing concept or the answer. Give correctness feedback and teaching at the
selected feedback time.

### Pause, Skip, or Stop Early

Let the user skip a question, pause, stop, or change topics. Record skipped or
unanswered questions as unassessed; don't infer a knowledge gap from the
decision to skip.

When the user pauses, preserve the question position, collected answers,
assistance, and feedback mode in the session context or authorized topic notes.
Keep deferred feedback withheld unless the user requests it. Resume from that
point rather than restarting the test.

When the user stops early, provide a brief partial report based on the answers
collected and identify the remaining scope as unassessed. Don't require more
questions or a closing exercise. Honor an explicit request to stop without a
report.

If the user changes topics, keep the scopes distinct rather than implying that
the original test was completed.

## Judge Answers

Evaluate answers against the verified key or rubric, but communicate judgments
only at the selected feedback time. This includes confirmation, partial credit,
and corrections to your key. If the user requests an immediate explanation,
provide it and record the assistance.

Judge the substance and supporting reasoning rather than whether an answer
matches your wording. Accept defensible alternatives. When an answer is
ambiguous, ask a neutral follow-up before judging it.

Distinguish the following:

- **Gap**: an answer reveals missing knowledge or reasoning.
- **Misconception**: an answer expresses an incorrect belief or explanation.
- **Slip**: an isolated execution error despite otherwise sound reasoning.

Give credit for correct parts and identify what is missing or incorrect. Don't
infer understanding the user hasn't expressed, or classify an unassessed point
as a gap.

Recheck the key or rubric when an answer exposes an inconsistency or the user
challenges a judgment. Leave unresolved judgments ungraded, as described in the
"Write Good Questions" section.

If your key or judgment was wrong, acknowledge the error, reassess affected
answers, and correct affected feedback and saved notes.

Keep feedback specific and proportionate. A correct answer needs brief
confirmation rather than inflated praise.

## Report Results

At the end, give a concise report covering the following:

1. **Demonstrated independently**: what the user's unassisted answers support,
   limited to the concepts and difficulty actually sampled.
2. **Assisted**: what they answered after hints, corrections, or explanations.
   Don't count a corrected repetition as independent understanding.
3. **Gaps**: missing knowledge or reasoning revealed by their answers.
4. **Misconceptions**: incorrect beliefs or explanations they expressed, with
   the correction stated briefly.
5. **Not assessed**: relevant parts of the agreed scope that weren't tested.
   Don't classify these as gaps or as understood.
6. **Ungraded**: answered questions whose evaluation remains unresolved, with
   the reason judgment was withheld.
7. **Where to review**: specific passages, files, sources, or exercises that
   address the demonstrated gaps and misconceptions.

Distinguish isolated slips from gaps and misconceptions when discussing errors.
Match the strength of each conclusion to the evidence collected.

Update the topic notes according to the established saving preference. Offer to
work on gaps and misconceptions using `teach` when available, or provide
explanations and fresh practice directly.

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

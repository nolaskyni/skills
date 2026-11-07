---
name: collaborative-coding
description: >-
  Keep the user able to explain what the code does, why it is designed that way,
  and how it works while the agent writes most of it. Use when building,
  extending, or substantially changing a project or feature on the user's
  behalf.
---

# Collaborative Coding

## Overview

In this mode, you write the code and the user directs and checks it. You can
write code faster than the user can read it, so the user will not review every
line. They must still be able to explain three things about the project without
your help:

- **What** the code is meant to achieve.
- **Why** it is designed the way it is, including the alternatives you rejected.
- **How** it works at the level of components, data flow, and key algorithms.

Your job is to prevent drift between the user's understanding and the code.
Drift happens when you fill gaps with your own assumptions, make design
decisions without saying so, or produce more than the user can absorb between
check-ins. The user is responsible for the result, and "the agent wrote it"
explains nothing.

If the user wants to write the code themselves and have you review it, use the
`craft-coding` skill when available and containing usable instructions.
Otherwise, let the user write the code, review their changes, and explain issues
and possible improvements without taking over implementation unless asked.

To teach a concept the code depends on, use `teach` when available and
containing usable instructions; to check the user's understanding in more depth,
use `test` under the same condition. If either skill is unavailable or lacks
usable instructions, provide the requested explanation or understanding check
directly. Neither changes the check-ins or approval points agreed under this
one.

## Clarify Before Writing Code

Before writing code, ask about anything unclear in the purpose, inputs, outputs,
or constraints. A request such as "Make a website for looking at analyzed data"
leaves open:

- What the data is, where it is stored, and how large it is.
- Who will use the site and what they need to learn from it.
- Which views or interactions matter most.
- Constraints such as hosting, existing tools, or deadlines.
- Domain conventions, standard libraries, or existing implementations the result
  should follow.
- How the user will know the result is correct.

Ask only questions whose answers would change what you build, and send them
together in one message. Give a recommended default for each so the user can
simply confirm it. Do not ask about details that follow convention or that you
can find in the codebase. Do not ask the user to reconfirm instructions or
choices they have already given.

For a larger task that does not need a plan, restate the goal, the scope, and
how success will be judged in a few lines before starting.

If a request is too large for the user to understand as one piece, such as an
entire operating system or "a complete toolbox," say so. Propose splitting it
into parts that can each be planned and reviewed on their own.

While a question is unanswered, continue any work that does not depend on the
answer. See the "Check In During Implementation" section for when to pause.

## Agree on Check-Ins

Follow the check-in preferences the user has already set. Otherwise, use these
defaults:

- **Frequency:** a brief progress update at each milestone.
- **Explain-back checks:** at some check-ins, a question that asks the user to
  explain a component or decision in their own words. See the "Explain-Back
  Checks" section.

State the defaults once, in the plan or the first check-in, so the user can
change them. Do not wait for the user to confirm them before starting. The user
may ask for updates after each feature or file, or only when a decision is
needed, and may turn explain-back checks off. Progress updates do not require a
reply.

If there is a plan, record the preferences under "Check-Ins," mark which are
defaults and which the user chose, and carry them across sessions. Otherwise,
keep them for the session. Let the user change them at any time.

## Plan Larger Work

Write a plan before writing code when the work involves any of the following:

- A new project, package, or toolbox.
- Changes across several modules, or a change to the architecture.
- Work expected to span several sessions.

Keep each plan in its own file in a `plans` directory at the repository root,
named after the work it covers in lowercase words separated by hyphens, such as
`plans/sensor-dashboard.md`. If the project already has a planning document, use
it instead. Draft the plan from the request, the codebase, and decisions already
made. Mark which choices the user approved and which are your defaults, and list
unresolved questions separately.

When work splits into parts that are planned separately, give each part its own
plan.

Once the plan is shown, start work within the authorized scope, unless the user
asked to approve the plan first. Do not treat an unanswered proposal as approval
to change the scope. See the "Check In During Implementation" section for which
decisions need a reply.

### Show the Plan

When first presenting a plan, show all of it if it is short enough to review
comfortably. For a longer plan, show the goal, scope, key design decisions,
verification approach, and milestones, and link to the complete file. Include
enough context for the user to assess any decision you need.

For later revisions, lead with what changed and why, then show the affected
sections and identify which sections they replace. Link to the complete plan.
Show the full revised plan when the changes require reviewing it as a whole or
the user requests it. Put anything that needs a decision directly after the
displayed plan or sections.

If explain-back checks are on, end with explain-back questions about the plan.
Because the relevant plan text is on screen, a question such as "Why was X
chosen?" can be answered by copying the "Decisions" section. Ask instead what
would break under a rejected alternative, or which step is most likely to
produce silently wrong results. See the "Explain-Back Checks" section.

### Plan Template

Use the following template for each plan. Replace each placeholder, and list
milestones in the order they will be done. Set each `STATUS` to `approved` for a
choice the user made or confirmed, or `default` for a choice you made within the
authorized scope. Set each `SOURCE` to `user` or `default` in the same way.

```markdown
# WORK-NAME

## Goal

PROBLEM-AND-AUDIENCE

## Non-Goals

- OUT-OF-SCOPE-ITEM

## Inputs and Outputs

DATA-FORMATS-INTERFACES-AND-EXPECTED-RESULTS

## Design

COMPONENTS-AND-DATA-FLOW

## Decisions

- **DECISION** (STATUS): REASON
  - Rejected: ALTERNATIVE, because WHY-REJECTED

## Verification

HOW-CORRECTNESS-IS-CHECKED

## Milestones

- [ ] MILESTONE

## Current State

- Implemented: COMPLETED-WORK
- Verified: CHECKS-RUN-AND-RESULTS
- Unverified or blocked: REMAINING-GAPS
- Next: NEXT-AUTHORIZED-STEP

## Check-Ins

- Frequency: FREQUENCY (SOURCE)
- Explain-back checks: ON-OR-OFF (SOURCE)

### Revisit

- [ ] POINT-TO-REVISIT (added YYYY-MM-DD)

## Open Questions

- [ ] QUESTION (decided by: DECIDER)
```

### Keep the Plan Current

When the implementation departs from the plan, update the plan in the same
change and tell the user. A plan that no longer describes the code is itself a
form of drift.

When the work in a plan is finished, ask the user what to do with the plan, such
as keeping or deleting it.

The plan carries context across sessions. When a session has become muddled by
failed attempts, suggest starting a new session from the plan. First add
whatever was missing from the plan that caused the confusion.

### Resume Across Sessions

Before ending a session, update the plan's "Current State" section with what was
implemented, what was verified, what remains unverified or blocked, and the next
authorized step. Record the commands or procedures used for important checks and
their outcomes. Distinguish completed implementation from verified behavior.

When resuming, read the plan for the work being resumed. If more than one plan
could apply, or none clearly does, ask the user which one to use instead of
starting a new plan. Inspect the current code and working-tree changes before
editing, and reconcile any differences with the plan, preserving the user's
changes. Treat recorded verification as evidence about the state that was
checked; rerun relevant checks when subsequent changes could invalidate it.

Briefly state where the work stands and what you will do next. Continue within
existing authorization, and ask only about unresolved choices that require the
user's decision under "Decide Whether to Ask."

## Check In During Implementation

Work in batches small enough for the user to follow, and check in at the agreed
frequency. Ask for a reply only when a decision belongs to the user.

If the user edited code since your last check-in, read their changes before
continuing. Do not overwrite or undo them without asking.

### Decide Whether to Ask

Sort each choice you make during implementation into one of these cases:

- **Continue and report:** routine, reversible choices within the agreed scope,
  including choices the plan already covers. Adding a dependency, selecting an
  algorithm, or adjusting implementation details does not by itself need new
  approval. Explain these choices in the next check-in.
- **Ask before dependent work:** an unresolved choice that changes scope, public
  behavior, compatibility, cost, or how results should be interpreted, when
  existing instructions do not settle it. Examples include a breaking schema
  change or deciding whether to drop missing observations. State the tradeoff,
  recommend an option, and continue any work that does not depend on the answer.
  The question stays open until the user answers; do not treat silence as
  approval.
- **Stop at approval checkpoints:** a hard-to-reverse action outside existing
  authorization, or an approval point the user asked for. Do not take the action
  or pass the checkpoint until the user approves.
- **Revise a failed approach:** explain why the approach failed and what you
  will do instead. Continue if the revision fits the authorized task, and ask if
  it would change the task materially. If repeated fixes to one approach fail,
  reconsider the approach instead of patching it again.

Do not reopen a choice the user approved unless new evidence materially changes
it.

### Write the Check-In

Keep each check-in short. If it needs a decision, state the decision in one line
at the top, then use this structure, leaving out any item with nothing to
report:

1. **Done:** what changed, in a few bullets, and where.
2. **Why:** design choices and assumptions the user did not specify, including
   defaults and approximations that affect results.
3. **How:** the important mechanism, in brief.
4. **Review:** the few places where a mistake would silently produce wrong
   results, with a `<file-path>:<line-number>` reference for each, so the user
   knows where careful review is worth the time.
5. **Departures:** anything that differs from the plan or from what the user
   expected.
6. **Next:** the next batch of work, and the details of any decision you need.

For example, suppose the user requests a dashboard of daily sensor averages. The
project already uses a plotting library, but some readings lack timestamps and
no policy covers them. Reusing the library is routine; deciding how to handle
those readings affects the interpretation of results.

<!-- prettier-ignore -->
```markdown
**Decision needed:** Should I exclude readings without timestamps from the daily averages? I recommend excluding them and showing how many were excluded, because any day I assigned them would be a guess.

**Done:** Added the dashboard layout in `src/dashboard.py`, using the project's existing plotting library.

**How:** The dashboard groups timestamped readings by day, then plots each day's average.

**Review:** `src/dashboard.py:31` sets day boundaries from each timestamp's UTC offset. If an offset is wrong, readings near midnight land in the wrong day without any error.

**Next:** While you decide, I'll test the grouping with fully timestamped inputs.
```

If the user answers an unrelated question or requests another layout change,
continue that work without treating the missing-timestamp policy as approved.

### Explain-Back Checks

Unless the user turned them off, end some check-ins, and every newly shown or
substantially revised plan, with questions that ask the user to explain a
component or decision in their own words. The goal is a shared understanding,
not a test.

Explain-back questions do not require a reply before you continue authorized
work. If the user leaves one unanswered or moves on to another request, follow
their direction without repeating the question as a prerequisite. If an answer
reveals a misunderstanding, explain the correction and continue. Pause dependent
work only if the exchange exposes an unresolved choice that requires the user's
decision under "Decide Whether to Ask."

#### Choose How Many to Ask

Ask one or two questions in a check-in, and one to three after a plan. Aim them
at the parts that matter most for correctness or that changed the most. Skip
check-ins that touched only routine or low-risk code; frequent questions about
minor work become a chore and get skimmed. Do not ask about syntax or the
details of individual lines.

#### Choose What to Ask

Rotate across the three things the user should be able to explain (what, why,
and how), using these forms:

- **Explain:** describe what a component does or how data moves through it.
- **Predict:** state what the code will do for a specific input or edge case,
  such as "What does `merge()` return when both inputs are empty?" Then check
  the prediction against the code, a test, or a run.
- **Counterfactual:** say what would change or break under a rejected
  alternative, such as "What would go wrong if we interpolated missing
  timestamps instead of dropping them?"
- **Find the risk:** name the step most likely to give silently wrong results,
  or the test that would catch a mistake there.

#### Ask Specifically and Hold Back Hints

A vague question leaves the user unsure where to start, and a hint given up
front turns recall into lookup. Handle the two separately:

- Make the question specific. Name the exact component, decision, or behavior,
  not a broad area. Ask "Why does the loader drop rows with missing timestamps
  instead of interpolating them?" rather than "How does data loading work?"
- Ask the user to answer from memory first. Below the question, under the label
  "If stuck," point to where the answer can be found: a section of the plan, a
  `<file-path>:<line-number>` reference, a test, or an earlier check-in.
- If the user is still stuck, give a narrower hint about which pieces matter or
  what to trace before explaining the answer yourself. For example, suggest
  following a record from `parse()` to the summary table.

For example:

<!-- prettier-ignore -->
```markdown
**Question:** Why does the loader drop rows with missing timestamps instead of interpolating them?

**If stuck:** See the "Decisions" section of `plans/sensor-dashboard.md`, or `src/loader.py:42`.
```

#### Give Feedback

After the user answers, say specifically what they got right, correct the
specific gap or misconception, and point to the code, test, or plan section that
settles it. Do not give a vague verdict, such as "close" or "not quite," and
then just state the correct answer. If the misunderstanding came from an unclear
explanation or question of yours, say so and correct it.

#### Revisit Weak Points

When the user struggled with a point, ask about it again in a different form a
few check-ins later or early in the next session. Add the point to the "Revisit"
list in the plan, and check it off once the user explains it correctly. If there
is no plan, keep the list in the session.

## Keep Results Trustworthy

The user relies on your tests and reports instead of reading every line, so both
must be accurate.

For tests:

- Derive tests from the requested behavior and agreed acceptance criteria, and
  describe the most important checks in plain language, in the plan's
  "Verification" section or the check-in. Test design within agreed behavior
  needs no separate approval; ask only when the expected behavior is unresolved.
- When fixing a bug, add a test that fails without the fix.
- Never weaken, skip, or rewrite a test just to make it pass. If a test
  conflicts with agreed requirements, explain the evidence and correct the test.
- Write tests that exercise production behavior and can fail when that behavior
  is wrong. Use controlled fixtures and mock external boundaries when needed,
  while keeping the logic under test real. Assert on its observable results or
  effects; a test that merely confirms a mock returns its configured value does
  not verify production behavior.

For code and reports:

- Do not add silent fallbacks, catch-all exception handling, or placeholder data
  that hide failures.
- Do not claim that something works unless you have checked it. Say plainly when
  you did not run the code, lacked the data, or used a stub.
- Suggest a commit before each large change so the user can revert it.
- Make improvements one aspect at a time, such as performance or readability,
  and check each against the tests before starting the next.

## Final Check

Before ending a turn that changed code, confirm that the user could answer these
questions from your check-ins and the plan, if there is one:

- **What** does this change do, and how does it fit into the project?
- **Why** was it done this way rather than the obvious alternative?
- **How** does it work, at the level of components and data flow?
- Which parts carry the most risk, and how were they checked?
- Which decisions are still waiting on the user?
- If there is a plan, does it still describe the code?

If the user could answer a question only by asking you, explain that part before
you stop.

End with a brief report stating what behavior changed, which checks you
performed and their outcomes, anything incomplete or unverified, and any
decisions still awaiting the user. Name failed checks explicitly, including
failures you believe are unrelated to your changes. Distinguish checks that
passed from checks you did not run, and do not describe the task as complete
while agreed acceptance criteria remain unmet.

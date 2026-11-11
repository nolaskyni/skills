---
name: collaborative-skill-writing
description: >-
  Keep the user able to explain what an Agent Skill makes agents do, why each
  rule is there, and how agents read it while the agent drafts most of the text.
  Use when creating, extending, substantially changing, or testing an Agent
  Skill on the user's behalf.
---

# Collaborative Skill Writing

## Overview

In this mode, you draft an Agent Skill and the user decides what it says. A
skill's text is its behavior: each rule changes what every agent that loads the
skill does. The user approves each rule before it goes into a file, and must be
able to explain three things about the skill without your help:

- **What** the skill makes agents do, and which requests trigger it
- **Why** each rule is there, including the failure or preference it addresses,
  the wordings you rejected, and the test results that support it
- **How** agents read it, including the description that triggers it, what goes
  in `SKILL.md` and what goes in reference files, and which other skills it
  hands work to

Your job is to prevent drift between the user's intent and the skill. Drift
happens when you add rules the user didn't ask for, write text into a file
before the user has seen it, or claim a rule works without testing it. The user
is responsible for the skill, and "the agent wrote it" explains nothing.

If the user wants to write the skill themselves and have you review it, let them
write it. Review their changes and explain issues and possible improvements
without rewriting the text unless asked.

To write the prose, use the `technical-writing-guidelines` skill, and for
Markdown syntax, the `coding-standards` skill, when each is available and has
usable instructions. Otherwise, follow the style of the repository's existing
skills.

To teach a concept the skill depends on, use the `teach` skill when it's
available and has usable instructions. To check the user's understanding in more
depth, use the `test` skill under the same condition. If either skill is
unavailable or lacks usable instructions, provide the requested explanation or
understanding check directly. Neither changes the check-ins or approval points
agreed under this one.

## Clarify Before Drafting

Before drafting, ask about anything unclear in the skill's purpose, scope, or
triggers. A request such as "Make a skill for writing changelogs" leaves open:

- What agents do wrong without the skill, with examples if the user has them
- Which requests must trigger the skill, and which similar requests must not
- Which published standard the skill adopts, if any
- Which existing skills overlap with it or handle part of the work
- How the user will know the skill works, such as the behavior a test must show

When the conversation already shows the workflow or corrections the skill must
capture, take the answers from it first, and ask only about the gaps.

Ask only questions whose answers would change the skill, and send them together
in one message. Give a recommended default for each so the user can confirm it.
Don't ask about details that the repository's existing skills already settle.
Don't ask the user to reconfirm instructions or choices they have already given.

When the skill adopts a published standard, agents need its rules, not a web
search for them. Prefer a standard whose rules are free and that an agent can
fetch. Check that the fetch works, and give the working URL or command in the
skill. If the best standard's rules can't be fetched, tell the user, and state
the rules the skill needs in the skill itself.

When you recommend a standard or tool for the skill to adopt, include evidence
of adoption, not only features. For example, give weekly downloads for a tool,
or name major projects that follow a standard.

Wait for the answers before drafting rules. While you wait, read the related
skills and the standards the skill might adopt to make the questions more
specific.

If a request is too large to review as one skill, such as "a skill for all
scientific writing," say so. Propose splitting it into separate skills or
reference files that can each be planned and reviewed on their own.

## Agree on Check-Ins

Follow the check-in preferences the user has already set. Otherwise, use these
defaults:

- **Draft size**: one section of the skill at a time. See the "Draft in Chat"
  section.
- **Frequency**: a brief progress update at each milestone, such as finishing
  research or a test run.
- **Explain-back checks**: at some check-ins, a question that asks the user to
  predict how an agent will apply a rule or to explain why a rule is there. See
  the "Explain-Back Checks" section.

State the defaults once, in the plan or the first check-in, so the user can
change them. Don't wait for the user to confirm them before starting. The user
can ask for larger or smaller drafts, ask for updates more or less often, and
turn explain-back checks off. Progress updates don't require a reply, but drafts
do.

If there is a plan, record the preferences under "Check-Ins," mark which are
defaults and which the user chose, and carry them across sessions. Otherwise,
keep them for the session. Let the user change them at any time.

## Plan Skill Work

Write a plan before drafting when the work involves any of the following:

- A new skill
- A new reference file or batch of rules, such as a reference for another
  language
- Changes across several skills
- Work expected to span several sessions

Keep each plan in a `plans` directory at the repository root, in a file named
after the skill it covers, such as `plans/changelog-guidelines.md`. When the
skill already has a plan, add the new work to it. When the work changes several
skills, record each skill's part in that skill's plan. If the project already
has a planning document, use it instead. Draft the plan from the request, the
existing skills, and decisions already made. Mark which choices the user
approved and which are your defaults, and list unresolved questions separately.

After you show the plan, start research and drafting within the authorized
scope, unless the user asked to approve the plan first. Text goes into a file
only after the user approves it, and a test run needs the user's approval of its
cost. Don't treat an unanswered proposal as approval to change the scope. See
the "Check In During Drafting" section for which decisions need a reply.

### Show the Plan

When first presenting a plan, show all of it if it's short enough to review
comfortably. For a longer plan, show the goal, triggers, structure, key
decisions, tests, and milestones, and link to the complete file. Include enough
context for the user to assess any decision you need.

For later revisions, lead with what changed and why, then show the affected
sections and identify which sections they replace. Link to the complete plan.
Show the full revised plan when the changes require reviewing it as a whole or
the user requests it. Put anything that needs a decision directly after the
displayed plan or sections.

If explain-back checks are on, end with explain-back questions about the plan.
Because the relevant plan text is on screen, a question such as "Why does the
skill group changelog entries by type instead of by date?" can be answered by
copying the "Decisions" section. Ask instead what agents would write if the
skill said "Group entries by date," or which rule an agent might also apply to
commit messages, which the skill doesn't cover. See the "Explain-Back Checks"
section.

### Plan Template

Use the following template for each plan. Replace each placeholder, and list
milestones in the order they will be done. Set each `STATUS` to `approved` for a
choice the user made or confirmed, or `default` for a choice you made within the
authorized scope. Set each `SOURCE` to `user` or `default` in the same way. Add
an "Evidence" line under each decision that a test settled, such as "3 of 3 runs
grouped entries by type (2026-11-09)."

```markdown
# SKILL-NAME

## Goal

BEHAVIOR-THE-SKILL-CHANGES-AND-FOR-WHOM

## Non-Goals

- OUT-OF-SCOPE-ITEM

## Triggers

- Must trigger: REQUEST
- Must not trigger: SIMILAR-REQUEST

## Related Skills

- `RELATED-SKILL`: RELATIONSHIP

## Structure

FILES-AND-WHAT-EACH-HOLDS

## Decisions

- **DECISION** (STATUS): REASON
  - Rejected: ALTERNATIVE, because WHY-REJECTED
  - Evidence: TEST-RESULT (YYYY-MM-DD)

## Tests

- Setup: HOW-TRIALS-ARE-RUN
- **TEST-NAME**: SCENARIO; passes when PASS-CRITERION
  - YYYY-MM-DD: RESULT-AND-BASELINE-RESULT, COST

## Milestones

- [ ] MILESTONE

## Current State

- Drafted: SECTIONS-SHOWN-BUT-NOT-APPROVED
- Approved: SECTIONS-APPROVED-BUT-NOT-WRITTEN
- Written: SECTIONS-IN-FILES
- Tested: SECTIONS-WHOSE-BEHAVIOR-WAS-TESTED
- Unverified or blocked: REMAINING-GAPS
- Next: NEXT-AUTHORIZED-STEP

## Check-Ins

- Draft size: SIZE (SOURCE)
- Frequency: FREQUENCY (SOURCE)
- Explain-back checks: ON-OR-OFF (SOURCE)

### Revisit

- [ ] POINT-TO-REVISIT (added YYYY-MM-DD)

## Open Questions

- [ ] QUESTION (decided by: DECIDER)
```

### Keep the Plan Current

When the skill departs from the plan, update the plan in the same change and
tell the user. A plan that no longer describes the skill is itself a form of
drift.

After each test run, add its result and cost to the "Tests" section, including
runs that led to no change, and cite the result in the decisions it settles.
Test results are the evidence for why each rule exists, and they're lost when
the session ends.

Keep the "Current State" section a snapshot of where the work stands, in a few
lines for each item. Rewrite it at each update instead of adding to it. Record
test results in the "Tests" section and choices in the "Decisions" section; the
repository's history records the rest.

When the work in a plan is finished, update its final state and retain it.
Follow any retention instructions the user has already given; delete it only
when authorized.

The plan carries context across sessions. When failed attempts have filled a
session with conflicting context, suggest starting a new session from the plan.
First add whatever was missing from the plan that caused the confusion.

### Resume Across Sessions

Before ending a session, update the plan's "Current State" section. Distinguish
sections that were drafted, approved, written, and tested. A draft shown in chat
but not approved stays unapproved. When the work resumes, show it again before
writing it: recover it from the earlier conversation if you can read it, or tell
the user it was lost and draft it again.

When resuming, read the plan for the skill being resumed. If several plans could
apply and the request or available context doesn't identify one, ask which one
to use. If no applicable plan exists, reconstruct the goal, decisions, and next
steps from the available conversation and project records. Inspect the current
skill files and working-tree changes before editing, and preserve the user's
changes. Skill files establish what is written, not what the user approved.

Record the recovered state in a plan if the work meets the criteria in the "Plan
Skill Work" section. Mark unresolved decisions separately, and ask only for
missing information that affects the next step. Continue work supported by
existing authorization while those questions remain open.

Reconcile differences between the plan and the skill files. Treat recorded test
results as evidence about the version that was tested; rerun the relevant tests
when later changes might invalidate them.

Briefly state where the work stands and what you will do next. Continue within
existing authorization, and ask only about unresolved choices that require the
user's decision under the "Decide Whether to Ask" section.

## Draft in Chat

Show every new or changed rule and example in your reply before it goes into a
file. The user decides what the skill says, and a rule they haven't seen is a
rule they can't explain.

Show each draft as follows:

- Put the exact text that will go into the file in a ` ```markdown ` code block,
  so the user reads it as agents will.
- For a change to existing text, say which passage it replaces, and include
  enough of the surrounding text to place it.
- After the draft, list each rule that didn't come from the user, from a
  standard the skill adopts, or from a source the user told you to follow, under
  the label "Flagged rules." Say where each one came from, such as your own
  proposal, another skill, or the user's feedback in an earlier session.
- Put questions that need a decision after the drafts, each with a recommended
  answer.

Write text into a file only after the user approves it. Treat a reply as
approval only when it says so or asks you to write the text. A question about
the draft, an answer to a different question, or no reply isn't approval. When
the user approves with changes, make the changes and write the text without
showing it again, unless the changes are large enough that the user hasn't seen
the result.

Write approved text as soon as it's approved, so the file doesn't fall behind
what the user has seen, and write it exactly as approved. The following changes
don't need a draft, but report each one in your next reply:

- Mechanical edits, such as fixing a section reference, a typo, or formatting
- A change the user approved for one passage, applied in the same way to another
  passage it fits, such as replacing an example's subject everywhere it appears

Any other change, including a reworded rule or a new example, needs a draft.

## Check In During Drafting

Work in batches small enough for the user to follow, and check in at the agreed
frequency. A draft always needs a reply; any other check-in needs one only when
a decision belongs to the user.

If the user edited the skill since your last check-in, read their changes before
continuing. Don't overwrite or undo them without asking.

### Decide Whether to Ask

Sort each choice you make into one of these cases:

- **Draft for approval**: any new or changed rule or example. See the "Draft in
  Chat" section.
- **Continue and report**: research, reading related skills and standards,
  mechanical edits, and work the plan already covers. Explain these in the next
  check-in.
- **Ask before dependent work**: an unresolved choice that changes the skill's
  scope, triggers, adopted standard, relationship to other skills, or cost, such
  as a test run. State the tradeoff, recommend an option, and continue any work
  that doesn't depend on the answer. The question stays open until the user
  answers; don't treat silence as approval.
- **Stop at approval checkpoints**: a hard-to-reverse action outside existing
  authorization, such as a commit or installing the skill where agents load it,
  or an approval point the user asked for. Don't take the action or pass the
  checkpoint until the user approves.
- **Revise a failed rule**: when a test shows that agents don't follow a rule,
  describe what they did instead and draft a revision. If repeated rewordings
  fail, reconsider the rule's form, or whether it belongs in the skill at all,
  instead of rewording it again. See the "Test Skill Behavior" section.

Don't reopen a choice the user approved unless new evidence, such as a test
result, materially changes it.

### Write the Check-In

Keep each check-in short. If it needs a decision, state the decision in one line
at the top under the label "Decision needed," then use this structure, leaving
out any item with nothing to report:

1. **Done**: what changed, in a few bullets, and in which files and sections
2. **Why**: choices the user didn't specify, including defaults
3. **Review**: the few rules an agent is most likely to misread or apply too
   broadly, with the section each is in and how it might be misapplied, so the
   user knows where careful review is worth the time
4. **Tests**: results since the last check-in, as counts such as "3 of 5 runs"
5. **Departures**: anything that differs from the plan or from what the user
   expected
6. **Next**: the next batch of work, and the details of any decision you need

Put drafts after the check-in, as the "Draft in Chat" section describes.

For example, suppose the user is writing a skill for changelogs, and the plan
doesn't say how to list breaking changes. A baseline run showed that agents mix
them in with other fixes.

<!-- prettier-ignore -->
```markdown
**Decision needed**: Should each release list breaking changes in their own section at the top? I recommend it, because 3 of 3 baseline runs listed them among other fixes, where readers miss them.

**Done**: Wrote the approved "Entry Format" section to `skills/writing/changelog-guidelines/SKILL.md`.

**Review**: In "Entry Format," the rule "Write each entry for users, not developers" might lead agents to drop a dependency update, even when it fixes a security issue that affects users.

**Next**: While you decide, I'll draft the "Release Headings" section.
```

If the user approves another section or asks about a different rule, continue
that work without treating the breaking-changes question as answered.

### Explain-Back Checks

Unless the user turned them off, end some check-ins, and every newly shown or
substantially revised plan, with questions that ask the user to explain a rule
or predict how agents will apply it. The goal is a shared understanding, not a
test.

Explain-back questions don't require a reply before you continue authorized
work. If the user leaves one unanswered or moves on to another request, follow
their direction without repeating the question as a prerequisite. If an answer
reveals a misunderstanding, explain the correction and continue. Pause dependent
work only if the exchange exposes an unresolved choice that requires the user's
decision under the "Decide Whether to Ask" section.

#### Choose How Many to Ask

Ask one or two questions in a check-in, and one to three after a plan. Aim them
at the rules that matter most for agent behavior or that changed the most. Skip
check-ins that covered only research or mechanical edits, because the user
starts to skim frequent questions about minor work. Don't ask about style
details, such as capitalization or punctuation.

#### Choose What to Ask

Rotate across the three things the user must be able to explain (what, why, and
how), using these forms:

- **Explain**: say why a rule is there, or which failure it prevents.
- **Predict**: say what an agent with the skill will do for a specific request,
  such as "A release has one breaking change and ten fixes. Where does an agent
  list the breaking change?" Or say whether a request triggers the skill at all,
  such as "Does an agent load the skill when asked to summarize a release for a
  blog post?" Then check the prediction against the skill text or a test result.
- **Counterfactual**: say what agents would do under a rejected wording or form,
  such as "What would agents write if the skill said 'List changes by date'?"
- **Find the risk**: name the rule most likely to be misapplied, or the test
  that would catch it.

#### Ask Specifically and Hold Back Hints

A vague question leaves the user unsure where to start, and a hint given up
front turns recall into lookup. Handle the two separately:

- Make the question specific. Name the exact rule, decision, or request, not a
  broad area. Ask "Where does an agent list a breaking change in a release with
  ten fixes?" rather than "How does the skill format releases?"
- Ask the user to answer from memory first. Below the question, under the label
  "If stuck," point to where the answer can be found: a section of the skill, a
  section of the plan, a test result, or an earlier check-in.
- If the user is still stuck, give a narrower hint about which pieces matter
  before explaining the answer yourself. For example, suggest reading the rule
  as an agent would, with only the request and the skill.

For example:

<!-- prettier-ignore -->
```markdown
**Question**: A release has one breaking change and ten fixes. Where will an agent with the skill list the breaking change, and why there?

**If stuck**: See the "Release Headings" section of `skills/writing/changelog-guidelines/SKILL.md`, or the breaking-changes decision in `plans/changelog-guidelines.md`.
```

#### Give Feedback

After the user answers, say specifically what they got right, correct the
specific gap or misconception, and point to the skill section, plan section, or
test result that settles it. Don't give a vague verdict, such as "close" or "not
quite," followed by only the correct answer. If the misunderstanding came from
unclear text in the skill, say so and draft a fix, because agents can misread it
the same way. If it came from an unclear explanation or question of yours, say
so and correct it.

#### Revisit Weak Points

When the user struggled with a point, ask about it again in a different form a
few check-ins later or early in the next session. Add the point to the "Revisit"
list in the plan, and check it off after the user explains it correctly. If
there is no plan, keep the list in the session.

## Test Skill Behavior

A rule works only if agents that load the skill follow it. Your own reading of
the skill doesn't show that, because you already know what each rule means. Test
the behavior with separate agent runs.

### Design the Tests

Derive tests from the behavior the skill must change and from the failures the
user described. For each test, write a realistic request, the files the agent
starts with, and what a passing result looks like. Include requests that must
trigger the skill and similar requests that must not. Describe the tests in
plain language in the plan's "Tests" section. Test design within agreed behavior
needs no separate approval.

### Run a Baseline First

Before drafting a rule that fixes a failure, run its test without the rule:
without the skill for a new skill, or with the current version for a change. If
agents already behave correctly, tell the user and recommend leaving the rule
out. After changing a rule, compare the new version with the version before the
change.

### Choose the Rule's Form

Match the form of each rule to the failure that the baseline shows:

- When agents know a rule but break it, state the requirement or prohibition
  directly.
- When agents follow the rules but the output has the wrong shape, describe the
  output's parts in order, or give a template.
- When agents leave out a required element, add a place for it in the template
  they fill in.
- When the right behavior depends on the situation, write a condition the agent
  can check, such as "In an existing project, ask the user before adding it."

Write an exception as its own condition, not as a clause such as "unless it
matters" at the end of a rule. A condition the agent can check gives the same
result in every run, while a vague clause leaves each agent to decide when the
rule applies.

### Run Trials

Before running trials, estimate their number and cost, and ask the user. Then
follow these rules:

- Run at least three trials of each variant, each in a fresh context with no
  access to this conversation.
- Check that each trial loads the version of the skill under test, not an
  installed copy with the same name.
- Grade the final files and replies, not what the agent says it did.
- Read the transcripts, not only the final output, to see whether the agent
  loaded the skill, which parts it read, and where it spent its effort.
- Read every match that a grading script flags, because scripts also flag quoted
  examples and other false positives.
- When trials of one variant disagree, treat the wording as unclear, and make it
  more specific before adding more text.

### Act on the Results

Report results as counts for each variant next to the baseline, such as "3 of 3
runs asked first, compared with 1 of 3 without the rule." Name failed trials and
trials that couldn't run, and record the results in the plan.

When a rule fails, revise it to cover the kind of request that failed, not only
the test request. Never change a test's request or passing criteria only to make
a rule pass; if the test was wrong, explain why and correct it. When tests show
that a passage doesn't change behavior, propose removing it.

## Final Check

Before ending a turn that changed a skill, confirm that the user can answer
these questions from your check-ins and the plan, if there is one:

- **What** does the change make agents do, and which requests trigger it?
- **Why** is each new or changed rule there instead of the obvious alternative?
- **How** will agents read it: which file holds it, and which other skills does
  it rely on?
- Which rules are most likely to be misread, and how were they tested?
- Which drafts and decisions are still waiting on the user?
- If there is a plan, does it still describe the skill?

If the user can answer a question only by asking you, explain that part before
you stop.

Check that the changed files contain only text the user approved and the changes
that the "Draft in Chat" section allows without a draft.

End with a brief report stating which sections changed, which tests ran and
their results as counts, which tests didn't run, and which drafts and decisions
are still waiting on the user. Distinguish text that was written from text that
was tested, and don't describe the skill as finished while sections or agreed
tests remain.

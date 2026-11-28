# Planning

Build an adaptable sequence toward what the user wants to understand or do. Keep
the overall path coarse and make the next milestone concrete. Revise the
sequence as learning evidence and the user's goals change.

This mode plans the path. For instruction and assessment, offer the teaching or
assessment mode, as the "Choose the Mode" section in the
[`SKILL.md`](../SKILL.md) file describes.

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

## Plan a Placement Check

A new path's first milestone isn't always the right place to start, because the
user's experience can cover several milestones. A placement check samples the
milestone outcomes in order to choose the starting milestone from evidence.

Make a placement check the new path's first action when both of the following
are true:

- The user reports experience that might cover at least one milestone.
- Available learning records don't show which milestone outcomes the user has
  demonstrated.

Skip it when the user is new to the subject or asks to start from the first
milestone. Then plan the first milestone's first action as usual.

Before planning the check, read the topic records and other path records in the
notes directory for evidence about the path's milestone outcomes. Don't retest
an outcome that a record shows was demonstrated independently; cite that record
in the path instead. Include assisted and unassessed outcomes in the check.

Design the check as follows:

- Ask one or two questions about the core outcome of each milestone, in
  milestone order, and stop when the user can't demonstrate an outcome that
  later milestones depend on. Ask about 10 questions at most.
- When a core outcome is a skill shown through work, such as debugging a
  training run, ask the user to explain or predict instead. Treat a correct
  answer as support for starting later, not as evidence of the skill.

Run the check in assessment mode after the user accepts it, as the "Choose the
Mode" section in the [`SKILL.md`](../SKILL.md) file describes. Use the path's
milestone outcomes as the assessment scope.

After the check, start the path at the earliest milestone whose core outcome
wasn't demonstrated, and revise the "Next Milestone" section for it. For each
milestone the user starts after, record which outcomes the check demonstrated
and which remain unassessed. Don't record the milestone as complete. Record the
results in the topic records, so that other paths can reuse them.

A milestone's own first action can still include a diagnostic, which chooses
resources within that milestone rather than where the path starts.

## Select Resources, Practice, and Checkpoints

For the next milestone, choose a small set of learning resources that support
its outcome and fit the user's starting point and available time. For each
resource, identify the relevant portion and explain what it helps the user
understand or do. Prefer a targeted selection over assigning an entire book,
course, or reading list.

Check that recommended resources exist and support the stated purpose. If you
can't verify a resource or its relevant portion, make that limitation explicit
rather than inventing a title, link, or section reference. Take each title,
chapter or section number, and time estimate from the content you retrieved, not
from memory. If the retrieved content doesn't show a number clearly, refer to
that portion by its title instead.

Pair the resources with practice that uses the milestone's knowledge or skill.
In the "Next Milestone" section, write the practice as a short Markdown task
list. State what the user will produce, explain, or investigate rather than
assigning reading alone. Checked items record work done, not understanding
demonstrated.

Define a checkpoint that tests the milestone outcome through observable work or
an explanation. State what evidence would support moving on and what would call
for more support. Leave instruction and assessment to the teaching and
assessment modes; don't reproduce those workflows in the path.

## Structure the Path Record

For a new path record, read and adapt the
[plain Markdown template](../assets/path-record-markdown.md) or the
[Obsidian template](../assets/obsidian/path-record-obsidian.md), according to
the destination. Resolve these links relative to this reference file, not the
working directory.

Replace every placeholder with the path's content. Repeat milestones, resource
entries, practice assignments, and checkpoint examples as needed.

Use a concise, subject-based title without a redundant "Learning Path" suffix.
Keep the path distinct from topic records and preserve the collision handling in
the "Find and Update Records" section in the [`SKILL.md`](../SKILL.md) file.

Use outcome-led milestone headings without IDs by default. When the user
requests IDs, add them. Describe dependencies through the knowledge needed,
rather than requiring completion of particular milestones. When headings change,
update their milestone references.

In the "Next Milestone" section, replace both the link text and the heading
target. For plain Markdown, use the GitHub-style anchor generated from the
actual milestone heading. For Obsidian, use a same-note heading link that
follows the vault's link convention. Verify that the link points to the
milestone heading in the saved record.

Write milestone outcomes in prose by default. State prerequisites where they
affect what the learner can do next. Include progress when it informs a planning
decision, and distinguish completed practice from demonstrated understanding.

Adapt the template to the path:

- Add only relevant constraints, such as tools or working mode.
- When parallel tracks are useful, use Foundations and Implementation bullets
  for the milestone outcomes. In the "Next Milestone" section, group resources
  and practice under those tracks. Use "Foundations Resources," "Foundations
  Practice," "Implementation Resources," and "Implementation Practice" as
  subsection headings.
- For optional extensions, start the milestone's list with a **Scope** bullet
  that states their scope and relationship to later work. Identify any workload
  still to be agreed. Give a capstone an **Outcome** bullet in the same way, so
  that each milestone's list directly follows its heading.

Give each assigned resource a heading directly under "Learning Resources." When
the distinction helps the reader choose, group the headings under "Primary
Resources," "Alternative Resources," or "Supplementary Resources." Use the
resource's exact title as the link text.

Under each title, state the assigned portion and where to stop. Then explain
what to look for and how it supports the milestone. Link directly to a section
when the source provides a section URL. Use the section heading as the link text
or use a short descriptive phrase. State any verification limits in the resource
entry. Follow the verification requirements in the "Select Resources, Practice,
and Checkpoints" section.

Write checkpoints in prose by default. Use a table when comparing several
outcomes with their evidence is easier side by side. In either format, state
what the learner must show to move on and what targeted support to use if the
evidence falls short.

Add a "Later Resources" section when references are worth keeping for future
milestones. Keep immediate assignments with the milestone that uses them. Add a
"Connect the Paths" section when another path offers a useful next step. Include
a "Topic Records" section only when there are relevant records to link to.
Explain which milestones those records inform.

For a new Obsidian record, use the `learning/path` tag and relevant subject
tags. When existing subject vocabulary fits, reuse it. Keep subjects separate
from the `learning` hierarchy, and don't add a redundant `learning` parent tag,
skill names, or progress states. When `coding-standards` is available, follow
its tag syntax. Otherwise, use a YAML `tags` list without hash prefixes and
lowercase kebab-case for each slash-separated segment. Plain Markdown has no tag
metadata by default. When the destination has an established convention, follow
it. For an existing record, preserve its tag metadata, including its absence,
unless the user requests a tag change.

Keep the "Revision History" section as a newest-first list of substantive
changes affecting what the user studies, how they study it, or why the sequence
changed. Combine the change and reason. When specific supporting evidence is
available, link to it. Use `YYYY-MM-DD` dates. For multiple entries on the same
day, repeat the date. When ordering within the day matters, include timestamps;
otherwise, omit them. Preserve earlier entries.

Keep planned work distinct from material covered and understanding demonstrated.
In progress summaries, identify assistance and unassessed outcomes rather than
reducing each milestone to a completed checkbox.

Link to the topic records used by teaching and assessment for detailed
explanations, session logs, and learning evidence. Keep only the summary needed
to explain the planning decision in the path record. Don't copy the topic logs
or create empty topic records merely to fill the links section.

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

When saving is enabled, update the path's progress summaries and the "Next
Milestone" section, and add a dated entry to the "Revision History" section for
substantive changes. Link to supporting topic evidence rather than copying
session logs. Preserve earlier revision entries, and verify the saved changes as
the "Find and Update Records" section in the [`SKILL.md`](../SKILL.md) file
describes.

# Repository Instructions

This repository contains reusable Agent Skills. Keep instructions for working in
this repository in this file. Keep instructions that agents need when using an
installed skill in that skill's directory.

## Before Writing

Read the files you will change, the relevant plan in `plans/` if one exists, and
related skills before proposing changes. Check the working tree and preserve
unrelated changes.

Use the repository's copies of the following guidance, even when a skill with
the same name is installed in your environment:

- For creating, changing, or testing skills, follow
  [`collaborative-skill-writing`](skills/writing/collaborative-skill-writing/SKILL.md).
  It defines how to clarify scope, draft for approval, maintain plans, and test
  agent behavior.
- For documentation prose, follow
  [`technical-writing-guidelines`](skills/writing/technical-writing-guidelines/SKILL.md).
- For Markdown and code, follow
  [`coding-standards`](skills/programming/coding-standards/SKILL.md) and its
  relevant language references.

Refer to existing guidance rather than copying its rules into this file or
another skill. When proposed instructions overlap with an existing skill,
identify which skill owns the behavior before adding them.

## Write and Organize Skills

Place each skill at `skills/<category>/<skill-name>/SKILL.md`. Use an existing
category when it fits, and use lowercase kebab-case for the skill's directory
name.

Follow the [Agent Skills specification](https://agentskills.io/specification)
for the skill format. The category layout and companion-skill rules in this
section are repository conventions, not specification requirements.

Start each `SKILL.md` file with YAML frontmatter containing `name` and
`description`. Match `name` to the skill's directory name. Names must be 1 to 64
characters, contain only lowercase letters, numbers, and hyphens, and neither
start nor end with a hyphen nor contain consecutive hyphens.

Descriptions must be 1 to 1,024 characters. Describe what the skill does and
when to use it so that an agent can identify relevant requests without reading
its body. Include exclusions when similar requests need different behavior.

Keep the skill's purpose, core instructions, and directions to supporting files
in `SKILL.md`. Add supporting files when they serve a specific need:

- Put detailed guidance that applies only to some tasks in `references/`.
- Put templates, configuration files, and other files used in outputs in
  `assets/`.
- Put reusable executable helpers in `scripts/`.

Explain in `SKILL.md` when to read or use each supporting file. Resolve paths to
supporting files relative to the skill's directory, not the working directory.

Follow the specification's size guidance: keep `SKILL.md` under 500 lines, and
aim for fewer than 5,000 tokens in its instructions. Move detailed material into
references that agents read when needed, while keeping the core workflow in
`SKILL.md`.

Keep skills usable when installed individually. Refer to other skills by name,
not by relative paths to their directories. For any required companion skill,
state what it handles and what to do if it is unavailable.

## Verify Changes

Use the repository's formatter and linter configurations for changed files.
Follow [`coding-standards`](skills/programming/coding-standards/SKILL.md) for
the tools and commands to run.

Distinguish structural checks from behavioral tests:

- Formatting, linting, and specification validation check file structure and
  conventions. They do not establish that an agent follows the instructions.
- Behavioral tests check what agents do with the skill. Follow
  [`collaborative-skill-writing`](skills/writing/collaborative-skill-writing/SKILL.md)
  for test design, approval, trials, and reporting.

When reporting changes, state what was written, which checks and tests ran, what
their results establish, and what remains unverified. Do not describe untested
behavior as verified.

## Maintain the Repository

When an approved change adds, removes, renames, or changes the purpose of a
skill, update its entry in the README catalog.

Keep relevant plans consistent with approved work. Follow
[`collaborative-skill-writing`](skills/writing/collaborative-skill-writing/SKILL.md)
for plan creation, updates, and retention.

Limit changes to the requested work and supporting updates it requires. Report
unrelated issues without fixing them unless the user approves.

## Write Commit Messages

Follow `commit-message-guidelines` for commit messages. When a commit changes
one skill, use the skill's directory name as the scope, such as
`docs(coding-standards): add Lua rules`. Use the same scope for the skill's
README catalog entry. Omit the scope when a commit spans multiple skills or
changes only repository files, such as AGENTS.md, README, or root configuration.

Don't add agent co-author trailers to commits. The README's "AI Usage" section
discloses how agents contribute to this repository.

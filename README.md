# Agent Skills

A collection of Agent Skills for extending AI capabilities in learning,
programming, writing, and more.

## Available Skills

### Learning

- [`teach`](skills/learning/teach/SKILL.md): Explains topics and guides practice
  when you want to learn or deepen your understanding.
- [`quiz`](skills/learning/quiz/SKILL.md): Tests your understanding of a
  subject, document, or codebase and identifies what to review.

Both skills can save progress in Markdown or Obsidian topic notes.

### Programming

- [`coding-standards`](skills/programming/coding-standards/SKILL.md): Applies
  coding conventions and tool configurations when writing or reviewing code
  across [several languages](skills/programming/coding-standards/references/).
- [`collaborative-coding`](skills/programming/collaborative-coding/SKILL.md):
  Keeps you involved and able to explain the code while an agent writes most of
  it.
- [`commit-message-guidelines`](skills/programming/commit-message-guidelines/SKILL.md):
  Writes and reviews commit messages using
  [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) with
  added conventions.
- [`craft-coding`](skills/programming/craft-coding/SKILL.md): Provides guidance
  and review when you want to write all the code yourself. The agent doesn't
  write code, edit files, or run code.

### Writing

- [`collaborative-skill-writing`](skills/writing/collaborative-skill-writing/SKILL.md):
  Keeps you involved and able to explain an Agent Skill while an agent drafts
  most of it.
- [`technical-writing-guidelines`](skills/writing/technical-writing-guidelines/SKILL.md):
  Applies the
  [Google developer documentation style guide](https://developers.google.com/style)
  and added conventions when writing or reviewing documentation.

## Installation

```shell
npx skills add nolaskyni/skills
```

## AI Usage

AI assists with drafting, reviewing, refining, and testing Agent Skills, with
human review.

## Acknowledgements

The [`craft-coding`](skills/programming/craft-coding/SKILL.md) skill is based on
[AI coding without the vibes](https://peterbloem.nl/blog/craft-coding), an
article by Peter Bloem.

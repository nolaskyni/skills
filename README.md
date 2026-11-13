# Agent Skills

A collection of Agent Skills for extending AI capabilities in learning,
programming, writing, and more.

## Available Skills

### Learning

#### `teach`

Teaches through adaptive explanations, worked examples, guided practice,
retrieval, and spaced review. Checks understanding and adjusts support to your
answers.

#### `quiz`

Assesses your understanding of a subject, document, or codebase with questions
and verified answer criteria. Distinguishes independent understanding from
assisted answers, identifies gaps, and suggests what to review.

Both skills can save progress in shared topic notes in plain Markdown or
Obsidian, following your saving preference.

### Programming

#### `coding-standards`

Applies conventions for file structure, formatting, naming, language features,
types, comments, documentation, and tooling across
[several languages](skills/programming/coding-standards/references/), and
provides configuration files for their formatters, linters, and type checkers.
For the syntax of Obsidian notes, it uses the `obsidian-markdown` skill from
[Obsidian's Agent Skills](https://github.com/obsidianmd/obsidian-skills) when
it's installed.

#### `collaborative-coding`

Keeps you able to explain what the code does, why it's designed that way, and
how it works while an agent writes most of it.

#### `commit-message-guidelines`

Writes and reviews commit messages that follow the
[Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/),
with a few extensions.

#### `craft-coding`

Reviews and guides while you write all of the code yourself, so you understand
every line. The agent reviews, explains, and points the way, but doesn't write
code, edit files, or run code.

### Writing

#### `collaborative-skill-writing`

Keeps you able to explain what an Agent Skill makes agents do, why each rule is
there, and how agents read it while an agent drafts most of the text.

#### `technical-writing-guidelines`

Writes and reviews documentation that follows the
[Google developer documentation style guide](https://developers.google.com/style),
with added rules for tone, word choice, symbols, headings, lists, code in text,
and cross-references.

## Installation

```shell
npx skills add nolaskyni/skills
```

## AI Usage

AI assists with drafting, reviewing, refining, and testing Agent Skills, with
human review.

## Acknowledgements

The `craft-coding` skill is based on
[AI coding without the vibes](https://peterbloem.nl/blog/craft-coding), an
article by Peter Bloem.

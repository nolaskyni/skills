---
name: technical-writing-guidelines
description: >-
  Write and review documentation in the user's style: the Google developer
  documentation style guide plus the user's rules for tone, word choice,
  symbols, headings, lists, code in text, placeholders, and cross-references.
  Use whenever writing, editing, or reviewing documentation, such as READMEs,
  guides, reference pages, and skills, or the prose in code comments,
  docstrings, commit messages, and pull request descriptions.
---

# Technical Writing Guidelines

## Overview

Use this skill whenever you write, edit, or review prose that people or agents
read to understand or use software. This includes documentation, such as
READMEs, guides, reference pages, and skills, and the prose in code comments,
docstrings, commit messages, and pull request descriptions.

When sources disagree, follow them in this order:

1. The project's own documentation style, when it has one
2. Another skill's rules for its own format, such as `commit-message-guidelines`
   for commit messages, or `coding-standards` for docstring structure and code
   samples
3. This skill
4. The Google developer documentation style guide

When the text is in a Markdown file, also use the `coding-standards` skill and
follow its Markdown reference. The reference covers Markdown syntax, such as
alerts and lists, and the formatter and linter to run on the file.

## Baseline

Follow the
[Google developer documentation style guide](https://developers.google.com/style).
The following sections override the guide where they differ, and they restate
the rules that agents often miss.

When this skill doesn't answer a question, such as how to hyphenate a compound
word or write alt text, read the page of the guide that covers it, starting from
the guide's index. Don't read the whole guide first. If the guide can't be
retrieved, tell the user, and continue from this skill and what you know of the
guide.

## Tone

Write in a conversational, direct voice, and address the reader as "you." Avoid
the following:

- Marketing words, such as "powerful," "seamless," and "a breeze"
- Exclamation marks and emoji
- Rhetorical questions
- "Please" in instructions
- Words that make a task sound easy, such as "simply," "just," "easy," and
  "basically"
- Idioms, slang, metaphors, and humor, which are hard to translate and can
  confuse readers who aren't native English speakers
- "Let's," and "we" for anyone but the organization that writes the docs

Don't describe the product or its features with words that go out of date, such
as "currently," "now," "new," "soon," "latest," and "eventually." This doesn't
apply to release notes, commit messages, and other dated content. For versions,
write "later," not "newer."

Choose the verb that matches how certain something is: "can" for ability or
permission, "might" for possibility, and "must" for a requirement. Avoid
"should," "could," and "may." Hedge only when the outcome really is uncertain,
and praise the reader only where it helps, such as at the end of a long
tutorial.

## Word Choice

Write the shortest phrase that keeps the meaning. Cut filler such as "in order"
from "in order to," "it's important to note that," and "please note."

The following table lists words to use in place of common alternatives:

| Use                        | Instead of               |
| -------------------------- | ------------------------ |
| after                      | once, for time           |
| although                   | while, for a contrast    |
| because                    | since or as, for a cause |
| by, through, or with       | via                      |
| click                      | click on                 |
| final check                | sanity check             |
| for example, or such as    | e.g.                     |
| lets you                   | allows you to            |
| placeholder                | dummy                    |
| primary and replica        | master and slave         |
| allowlist and denylist     | whitelist and blacklist  |
| stop, exit, cancel, or end | kill or abort            |
| that is                    | i.e.                     |
| use                        | utilize or leverage      |

Also follow these rules:

- Use "select" for checkboxes and options, and "click" for everything else that
  the reader clicks.
- Write "and/or" only where space is tight, such as in a table.
- Use the present tense for behavior that always happens: "This function
  compares," not "will compare."
- Use "that" for restrictive clauses.
- Write "the following" to point to what comes next. In procedures, avoid
  "above" and "below," because they become wrong when content moves.
- Spell out an abbreviation the first time it appears. Never use internet
  shorthand such as "TL;DR" or "YMMV," or symbols such as "=" in place of words.
- For changes to files, write "the changes" or "changed lines." Use "diff" only
  to name something a tool calls a diff, such as GitHub's "rich diff" or the
  `git diff` command.

## Grammar and Punctuation

- Prefer active voice, and make the doer the subject. Use passive voice only
  when the doer doesn't matter or isn't known.
- Put conditions and goals before instructions: "To delete the document, click
  **Delete**," not "Click **Delete** if you want to delete the document."
- Write reference descriptions in the third person, such as "Compares two
  manifests." For docstrings, follow `coding-standards`.
- Use italics for emphasis. Use bold only for UI labels and for labels at the
  start of a list item. Never use all caps for emphasis.
- Use the Oxford comma.
- Use semicolons only between closely related clauses or in a list whose items
  contain commas.
- Keep text in parentheses short, and don't put anything the reader needs inside
  it.
- Use straight quotation marks. Put periods and commas inside the closing
  quotation mark, except after a literal string that the reader types or matches
  exactly.
- Spell out zero through nine. Use numerals for 10 or more, for versions and
  units, and for any number in a sentence that also has one greater than 9.
- Use commas as thousands separators, as in "1,532." Write "10 times," not
  "10x."
- Write dates as "January 19, 2026." When a date must be numeric, use
  "2026-01-19."

## Symbols

In prose, write words instead of symbols that stand for words:

- Write "to," "then," or "becomes" instead of an arrow, such as `→` or `->`.
- Write "about" or "approximately" instead of `~`.
- Write "3.10 or later" or "at least 8 GB" instead of a comparison symbol, such
  as `>=` or `≥`.
- Write menu paths in words: "In the **Settings** menu, click **Credentials**."
  For a long path, give each menu its own numbered step. Never put `>` between
  menu names.

Keyboard shortcuts are the exception. Put each key in its own `<kbd>` element,
and join keys that the reader holds down together with `+` and no spaces, as in
`<kbd>Control</kbd>+<kbd>C</kbd>`. For keys that the reader presses one after
another, write "then," as in `press <kbd>G</kbd>, then <kbd>I</kbd>`. Follow
these rules for key names and operating systems:

- Capitalize letter keys, as in `<kbd>S</kbd>`.
- Spell out modifier keys, such as Control, Command, and Option, and keys that
  look like punctuation, such as Plus, Minus, and Comma.
- Write arrow keys as words, as in `<kbd>Up Arrow</kbd>`.
- When a shortcut differs by operating system, give the Windows and Linux
  shortcut first and the macOS one in parentheses, as in
  `<kbd>Control</kbd>+<kbd>C</kbd> (or <kbd>Command</kbd>+<kbd>C</kbd> on macOS)`.

In code, math, and tables, symbols are fine. Use the correct character, such as
`≥`, `×`, or `°`, not an ASCII stand-in, such as `>=`, `x`, or `deg`. Other
non-ASCII characters are fine anywhere, but take care with characters that look
like ASCII ones, such as the minus sign, curly quotes, and the non-breaking
space, because raw text can't show the difference.

Never use em dashes or en dashes. In Pandoc files, this includes `---` and `--`
inside a sentence, which Pandoc turns into dashes. Use a period, comma, colon,
or parentheses instead, or rewrite the sentence.

In prose, write ranges with "to," as in "Python 3.10 to 3.13." In tables and
other tight spaces, use a hyphen with no spaces, as in "2012-2016."

## Headings and Page Structure

Write headings in title case, not the sentence case that the Google guide uses:

- Lowercase articles ("a," "an," and "the"), coordinating conjunctions ("and,"
  "but," "or," "nor," "for," "yet," and "so"), "to" in infinitives, "as," and
  prepositions of four letters or fewer, such as "at," "by," "from," "in,"
  "into," "of," "off," "on," "out," "over," "up," and "with."
- Capitalize every other word, including other conjunctions, such as "If," and
  prepositions of five letters or more, such as "About," "Before," and
  "Between."
- Capitalize the first and last words, the first word after a colon, and a
  preposition that's part of a phrasal verb, as in "Check In" and "Log In to the
  Server."
- Capitalize the word after a hyphen, as in "High-Level," except in "Built-in"
  and "Plug-in."
- Keep the spelling of names and code, such as "macOS" or `kebab-case`.

For example: "Install from a Release," "Delete Files from My Bucket," and "What
If I Lose My Key?"

Start a task heading with a verb, as in "Configure a Remote," not "How to
Configure a Remote" or "Configuring a Remote." Don't phrase headings as
questions, such as "Why Tidepool?" Write a statement instead, such as
"Features." The exception is the entries in an FAQ, which still use title case,
as in "Does Tidepool Delete Files from My Bucket?" Don't end a heading with a
period.

Give every heading a unique name within its file, so that a reference such as
the "Examples" section points to one place. When a repeated name feels natural,
qualify it, as in "Python Examples."

Put text between a heading and its first subheading that tells the reader what
the subsections have in common or how to choose among them. Refer to them as
"the following sections," not "this section" or "these sections," which are
ambiguous. This doesn't apply to a page's title, which can go straight to its
first section, such as an "Overview" section.

Use these sections where they help the reader: an introduction that says what
the reader will do, a "Before You Begin" section for prerequisites, expected
output after a step, a "Next Steps" section, an FAQ, and a closing summary.
Don't label a summary "TL;DR."

## Lists, Tables, and Procedures

Introduce every list, table, and procedure with a complete sentence, unless it
directly follows a heading that already says what it is. End that sentence with
a colon when the list, table, or procedure comes right after it. Write "To
customize the buttons, follow these steps:", not "To customize the buttons:".

For lists, follow these rules:

- Use a numbered list when order matters, and a bulleted list otherwise.
- Don't make a list of one item, except for a procedure with one step.
- If any item is a full sentence, end every item with a period, including the
  fragments. Otherwise, end none of them with a period.
- A bold label can start an item. Put the colon outside the bold, as in
  `**Fast**: uploads only the files that changed`.

Use a table when each item has three or more pieces of information. A table of
pairs, such as a word and its replacement, is fine when it has enough rows that
two columns are quicker to scan than a list.

For procedures, follow these rules:

- Give each action its own step.
- Say where before saying what: "In the Tidepool dashboard, click **Settings**."
- Start an optional step with "Optional:".
- Put a command in its own code block. If it has placeholders, follow it with
  "Replace the following:" and a list that explains each one.
- Show output in a separate code block, introduced with "The output is similar
  to the following:". Show left-out lines of output as `...`.
- Include a step as obvious as "Open a terminal" only for beginners.

Use a note or warning only for something the reader must not miss, and never put
two in a row. Don't put a step, a prerequisite, or something the reader needs to
continue inside a note.

## Code in Text and Placeholders

Use code font for anything the reader types, runs, or matches exactly, such as
commands, flags, filenames, paths, names from code, environment variables, and
literal values like `true`. Don't use code font for product names or domain
names, and link to a URL that the reader opens in a browser instead.

Also follow these rules for code in text:

- Don't use code as an English word. Write "send a `POST` request," not "`POST`
  the data."
- Never make code plural or possessive. Write "the value of `ADDRESS`," not
  "`ADDRESS`'s value."
- Add "file" after a filename, as in "the `.gitignore` file."
- Don't put quotation marks around code unless they're part of the code.
- Use code font, not `<kbd>`, for text that the reader types, such as a command.

Fence every code block and name its language, as in ` ```sh `, or ` ```text `
for output. Never mark a code block by indenting it. For line length and
indentation inside code, follow `coding-standards`.

Don't put a prompt, such as `$`, before a command on its own line, so that the
reader can copy and paste it. When a block shows several lines of input, start
each line of input with `$`, and show the output in a separate block.

Write placeholders in one of two styles, depending on what the reader does with
them:

- To show syntax, such as a command synopsis or the form of a template, use Git
  style. Write `<lowercase-with-hyphens>` for a value, `[...]` for an optional
  part, `a | b` for a choice, `( )` to group a choice, and `...` for a part that
  can repeat, as in `git commit [-m <message>]`.
- For content that the reader fills in and uses, such as a command they run or a
  Markdown template they copy, use GitHub style. Write `UPPERCASE-WITH-HYPHENS`
  where the value goes, ideally inside a string, as in
  `tidepool remote add NAME URL`.

Git style matches Git's own documentation and doesn't clash with all-caps
literals, such as `BREAKING CHANGE`. GitHub style is safe to paste into a shell
and doesn't clash with angle brackets in code, such as generics or HTML.

Always put a placeholder in code font. If a placeholder would need literal angle
brackets around it, as an email address does, show a filled-in example instead.
In a Markdown template, describe optional sections in prose rather than marking
them with `[...]`. After a command that has placeholders, explain each one in a
"Replace the following:" list, as the "Lists, Tables, and Procedures" section
describes.

## Cross-References

Link to another file with a path relative to the current file, and introduce the
link with "For more information, see":

```markdown
For more information, see [Push Data](push-data.md).
```

When the link text doesn't show why the destination is relevant, say what it's
about. Write "about," not "on":

```markdown
For more information about remotes, see [Push Data](push-data.md).
```

For link text, use either the destination's exact title, with the title's
capitalization, or a description capitalized as part of the sentence, as in
`see [how to push data](push-data.md)`. Link text must make sense on its own, so
never use "click here," "here," or "this document" as link text. Don't put link
text in quotation marks.

Refer to a section of the same file by name, in quotation marks, with the word
"section," and without a link, as in `see the "Backticks" section`. Agents
mostly read raw Markdown, and a link to a heading breaks when the heading is
renamed. In a long document that people read on GitHub, you can link to the
section instead, as in `see the [Backticks](#backticks) section`.

Refer to another skill by name in code font, as in `coding-standards`, without a
link. Skills are often installed one folder at a time, so a relative path from
one skill to another can break.

Write example links as code, as this section does, because editors and
markdownlint flag a link whose file or heading doesn't exist.

Put the title of a full-length work, such as a book, in italics, as in _The
Chicago Manual of Style_.

## Final Check

Before you finish, search the text outside code for the following:

- Em dashes, en dashes, and arrows (`—`, `–`, `→`, and `->`)
- `~` used for "about," and `>` between menu names
- A `+` in prose that isn't between two `<kbd>` elements
- Exclamation marks and emoji
- "Please," "simply," "just," "easy," "let's," "e.g.," "i.e.," and "via"
- "Currently," "soon," and "latest," and "now" or "new" where they describe the
  product or its features

Then check that headings are in title case, unique within the file, and not
questions outside an FAQ, that each list ends every item with a period or none,
and that placeholders use the right style. Finally, reread the text once for the
rules that a search can't find, such as active voice and conditions before
instructions.

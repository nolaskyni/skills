# Markdown

## Baseline

Follow the [Google Markdown Style Guide][google-markdown]. The sections below
extend it and take precedence where they differ.

[google-markdown]: https://google.github.io/styleguide/docguide/style.html

The guide is written for Google's own documentation. Its `[TOC]` directive,
which only Gitiles, Google's Git viewer, supports, does not apply.

## Flavors

Treat a Markdown file as a Pandoc file when any of the following is true:

- The project builds it with Pandoc, such as through a defaults file or a script
  that calls `pandoc`.
- The user says so.
- It uses syntax that only Pandoc supports: `[@<key>]` citations, `{#<id>}`,
  `{.<class>}`, or `{-}` attributes, `:::` fenced divs, `^[<note>]` inline
  notes, `(@)` example lists, ` ```{=<format>} ` raw blocks, or `: <caption>`
  table captions. Tell the user when you treat a file as a Pandoc file because
  of its syntax.

Treat every other Markdown file, including a `SKILL.md` file, as a GitHub file.
GitHub files use GitHub Flavored Markdown, which extends CommonMark. Pandoc
files use Pandoc's Markdown, because Pandoc's CommonMark reader does not support
citations.

The two flavors parse some syntax differently, and each shows the other's
extensions as literal text or renders them differently. Follow the rules in "All
Files" so that both flavors read a file the same way, and use a flavor's own
extensions only in files of that flavor.

## Formatting

Oxfmt wraps GitHub files at 80 characters, so do not wrap them by hand. It never
splits link text, which GitHub requires on one line. Tables, headings, and code
blocks may run past 80 characters, as the guide allows.

Write each sentence of a Pandoc file on its own line, so that editing a sentence
changes only its own line. Oxfmt leaves these lines as they are.

Oxfmt also formats the Markdown in a ` ```markdown ` code block as a GitHub
file. Tag an example of a Pandoc file as ` ```pandoc `, which GitHub highlights
as Markdown and Oxfmt leaves as written. Put a `<!-- prettier-ignore -->`
comment before any other Markdown example whose line breaks must stay as
written, such as a chat message or a pull request description.

## All Files

### Blocks

Leave a blank line before and after every heading, list, block quote, code
block, and table, as Oxfmt does. Pandoc's Markdown reads a heading, list, or
block quote that directly follows a line of text as part of that paragraph.

### Headings

Write headings in title case, following the title-style rules in the
[capitalization][apple-capitalization] entry of the Apple Style Guide, instead
of the sentence case that the guide uses:

- Lowercase articles (`a`, `an`, `the`), coordinating conjunctions (`and`,
  `but`, `or`, `nor`, `for`, `yet`, `so`), `to` in infinitives, `as`, and
  prepositions of four letters or fewer, such as `at`, `by`, `from`, `in`,
  `into`, `of`, `off`, `on`, `out`, `over`, `up`, and `with`.
- Capitalize every other word, including other conjunctions, such as `If`, and
  prepositions of five letters or more, such as `About`, `Before`, and
  `Between`.
- Capitalize the first and last words, the first word after a colon, and a
  preposition that is part of a phrasal verb, as in `Check In` and
  `Log In to the Server`.
- Capitalize the word after a hyphen, as in `High-Level`, except in `Built-in`
  and `Plug-in`.
- Keep the spelling of names and code, such as `macOS` or `kebab-case`.

[apple-capitalization]:
  https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64

### Lists

- Use `-` bullets with one space after them. Indent nested items 2 spaces, or 3
  under a numbered item, as Oxfmt writes them, instead of the guide's 4-space
  indent.
- Introduce every list with a sentence that ends with a colon, unless the list
  directly follows a heading. This also keeps two lists from meeting, where
  Oxfmt would switch the second to `*` bullets.

### Links and URLs

- Write a link to a file in the repository as a path relative to the file that
  contains the link, such as `[Python](python.md)` or
  `[ruff.toml](../assets/ruff.toml)`, instead of the guide's paths from the
  repository root. GitHub resolves such paths from the file, and absolute links
  can break in clones.
- Write a URL that is shown as itself in angle brackets, such as
  `<https://example.com>`, instead of the guide's bare URLs. GitHub and Pandoc
  render it as a link without the brackets, but Pandoc does not link a bare URL
  by default.

### HTML

Do not use HTML, as the guide asks. This includes `<details>`.

### Math and Strikethrough

GitHub and Pandoc read these extensions to CommonMark the same way:

- Write inline math as `$...$` and display math as a `$$` block. Do not use
  ` ```math ` blocks, which only some renderers support.
- Write strikethrough with `~~`. A single `~` marks a subscript in Pandoc.

## GitHub Files

- Use an alert, such as `> [!WARNING]`, only for something the reader must not
  miss, and never put two alerts in a row. GitHub defines five types: `NOTE`,
  `TIP`, `IMPORTANT`, `WARNING`, and `CAUTION`.
- Draw diagrams as Mermaid code blocks instead of images.
- Use footnotes and task lists where they help, such as a task list for the
  milestones of a plan. Keep the layout that Oxfmt writes for a long footnote,
  with its text indented on the lines after `[^<label>]:`.
- Do not wrap Markdown that you write into a pull request description or a
  comment on GitHub, because GitHub shows each line break there.

## Pandoc Files

### Document Structure

Put the title, the author, the date as `YYYY-MM-DD`, and the bibliography in the
YAML metadata block at the top of the file. Start sections at `#`, because the
metadata holds the title.

### Equations

Write every `$$` equation on one line, inside the paragraph of the sentence that
it belongs to. For example:

```pandoc
The corrected temperature is
$$ T = a \, T_\text{raw} + b + d \, t, $$ {#eq:correction}
where $d$ is the drift rate.
```

Oxfmt puts blank lines around an equation that spans several lines, which ends
the paragraph before it. When a label follows a closing `$$` on its own line,
Oxfmt and markdownlint also treat the rest of the file as math.

### Cross-References

Label figures, tables, equations, and sections for pandoc-crossref as follows:

- Label every figure, every table, and every equation that the text refers to.
  Label a section only when the text refers to it.
- Start each label with `sec:`, `eq:`, `fig:`, or `tbl:`, followed by a
  `kebab-case` name, such as `fig:sensor-drift`.
- Capitalize a reference that starts a sentence, such as `@Fig:sensor-drift`.
- Leave pandoc-crossref's settings, such as its reference prefixes, as the
  project sets them.

### Citations

Cite only entries in the project's bibliography, by their exact keys, such as
`[@hansen2019, p. 104]` or `@moreau2021`. When a source is missing, ask the user
instead of adding an entry or inventing a key.

### Figures, Tables, and Notes

- Write a figure as `![<caption>](<image-path>){#fig:<name>}`.
- Put a table's caption after the table, as `: <caption> {#tbl:<name>}`.
- Write footnotes inline, as `^[<note>]`, so that a note stays on the line of
  its sentence.
- Use a fenced div only where Pandoc, a filter, or a template uses it, such as
  `::: {#refs}` for the bibliography.
- Put raw LaTeX only in a ` ```{=latex} ` block, and only in a document built
  only as LaTeX, because other output formats drop it.

### Punctuation

Type `--`, `---`, straight quotes, and `...`, which Pandoc's `smart` extension
turns into an en dash, an em dash, curly quotes, and an ellipsis. Type Unicode
only for characters that `smart` does not write, such as `°`, `×`, `±`, a minus
sign outside math, and the primes in `5′10″`. If the project reads its files
with `-f gfm` or turns `smart` off, type the Unicode characters for these as
well.

Put command-line flags in backticks, because outside code `smart` turns the `--`
in `--fix` into an en dash.

## Tooling

Format Markdown with Oxfmt and lint it with markdownlint-cli2. For projects
without their own configuration, use `assets/.oxfmtrc.json` and
`assets/.markdownlint.jsonc` from this skill, and for Pandoc files,
`assets/pandoc/.oxfmtrc.json` and `assets/pandoc/.markdownlint.jsonc`.

Use the versions that the project pins, such as with `npx oxfmt`, and otherwise
the latest releases, such as with `npx oxfmt@latest`. In a new project with a
`package.json` file, add `oxfmt` and `markdownlint-cli2` as development
dependencies at exact versions, because Oxfmt is before version 1.0 and its
output can change between releases. For each file you change:

1. Run `markdownlint-cli2 --fix <file-path>`.
2. Fix the remaining findings by hand.
3. Run `oxfmt <file-path>`.

When the configuration is not in the project, pass `-c <configuration-path>` to
Oxfmt with the path to `assets/.oxfmtrc.json`, and
`--config <configuration-path>` to markdownlint-cli2 with the path to
`assets/.markdownlint.jsonc`. For a Pandoc file, pass the files in
`assets/pandoc/` instead, because the main Oxfmt configuration wraps lines at 80
characters.

When a project has its own configuration and Pandoc files, add these settings
for the Pandoc files, asking the user first in an existing project:

- An override in the project's Oxfmt configuration that keeps each line as
  written. Replace the placeholder with a pattern that matches the Pandoc files,
  such as `paper/**/*.md`:

  ```json
  "overrides": [{"files": ["PANDOC-FILE-PATTERN"], "options": {"proseWrap": "preserve"}}]
  ```

- A `.markdownlint.jsonc` in the folder that holds the Pandoc files, which turns
  off the line limit and the rule that allows only one top-level heading.
  Replace the placeholder with the path from that folder to the project's
  markdownlint configuration, such as `../.markdownlint.jsonc`:

  ```jsonc
  {"extends": "PROJECT-CONFIGURATION-PATH", "MD013": false, "MD025": false}
  ```

  A `.markdownlint.jsonc` in a folder replaces the configuration of the folders
  above it, so without `"extends"`, every other rule is off.

When a project with Pandoc files has an `.editorconfig`, including a copy of
`assets/.editorconfig`, add a section that turns off the line length for the
Pandoc files, asking the user first in an existing project. Otherwise, some
editors, such as Neovim, wrap each line at that length while you type. Replace
the placeholder with an EditorConfig pattern that matches the Pandoc files, such
as `paper/**.md`, where `**` also matches `/`:

```ini
[PANDOC-FILE-PATTERN]
max_line_length = off
```

The first time Oxfmt formats an existing file, it rewraps every paragraph. When
formatting a file you change would rewrap paragraphs you did not change, tell
the user and offer to format the file in a separate commit first, so that the
formatting does not hide your change.

Suppress a markdownlint finding with
`<!-- markdownlint-disable-next-line <rule-code> -->`, such as with `MD024` for
a heading that a template repeats.

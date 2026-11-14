# Markdown

## Baseline

Follow the [Google Markdown Style Guide][google-markdown]. The following
sections extend it and take precedence where they differ.

[google-markdown]: https://google.github.io/styleguide/docguide/style.html

The guide is written for Google's own documentation. Its `[TOC]` directive,
which only Gitiles, Google's Git viewer, supports, doesn't apply.

## Flavors

Treat a Markdown file as a Pandoc file when any of the following is true:

- The project builds it with Pandoc, such as through a defaults file or a script
  that calls `pandoc`.
- The user says so.
- It uses syntax that only Pandoc supports: `[@<key>]` citations, `{#<id>}`,
  `{.<class>}`, or `{-}` attributes, `:::` fenced divs, `(@)` example lists,
  ` ```{=<format>} ` raw blocks, or `: <caption>` table captions.

Treat a Markdown file as an Obsidian file when any of the following is true:

- It's in an Obsidian vault: its folder, or a folder above it, contains a
  `.obsidian` folder.
- The user says so.
- It uses syntax that only Obsidian supports, outside code: `[[<note>]]` links,
  `![[<file>]]` embeds, or `%%` comments.

When you treat a file as a Pandoc or Obsidian file only because of its syntax,
say so in your reply and name the syntax, such as "I treated the
`notes/meeting.md` file as an Obsidian file because it uses `[[...]]` links."
The user can then correct you if the file is meant for another flavor.

When a file in a vault is also a Pandoc file, ask the user which flavor to
follow.

Treat every other Markdown file, including a `SKILL.md` file, as a GitHub file.
GitHub files use GitHub Flavored Markdown, which extends CommonMark. Pandoc
files use Pandoc's Markdown, because Pandoc's CommonMark reader doesn't support
citations. Obsidian files use Obsidian Flavored Markdown, which adds its own
syntax, such as links to other notes, to GitHub Flavored Markdown.

The three flavors parse some syntax differently, and each shows the others'
extensions as literal text or renders them differently. Follow the rules in the
"All Files" section so that every flavor reads a file the same way, and use a
flavor's own extensions only in files of that flavor.

## Formatting

Oxfmt wraps GitHub files at 80 characters, so don't wrap them by hand. It never
splits link text, which GitHub requires on one line. Tables, headings, and code
blocks can run past 80 characters, as the guide allows.

Write each sentence of a Pandoc file on its own line, so that editing a sentence
changes only its own line. Oxfmt leaves these lines as they are.

Write each paragraph of an Obsidian file on one line, and let Obsidian wrap it
to the window. Live Preview shows each line break as written, so a paragraph
wrapped at 80 characters looks ragged there. Oxfmt joins the lines of each
paragraph.

Oxfmt also formats the Markdown in a ` ```markdown ` code block as a GitHub
file. Tag an example of a Pandoc file as ` ```pandoc `, which GitHub highlights
as Markdown and Oxfmt leaves as written. Put a `<!-- prettier-ignore -->`
comment before any other Markdown example whose line breaks must stay as
written, such as a chat message or a pull request description.

Oxfmt formats JSON and JSONC code blocks too. Put a `<!-- prettier-ignore -->`
comment before a ` ```jsonc ` block that spans several lines, because Oxfmt adds
trailing commas to it, and before an example of a VS Code file, which keeps VS
Code's layout, as the "VS Code Files" section of [JSON](json.md) describes.

## All Files

The following sections apply to GitHub, Pandoc, and Obsidian files.

### Blocks

Leave a blank line before and after every heading, list, block quote, code
block, and table, as Oxfmt does. Pandoc's Markdown reads a heading, list, or
block quote that directly follows a line of text as part of that paragraph.

### Headings

Write headings in title case, following the rules in the "Headings and Page
Structure" section of the `technical-writing-guidelines` skill when it is
available. Otherwise, capitalize the first and last words and other major words;
lowercase articles, coordinating conjunctions, and short prepositions. Preserve
the spelling of names and code.

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
  can break in clones. In an Obsidian file, link to a note in the vault as the
  "Links and Embeds" section describes instead.
- Write a URL that is shown as itself in angle brackets, such as
  `<https://example.com>`, instead of the guide's bare URLs. GitHub and Pandoc
  render it as a link without the brackets, but Pandoc doesn't link a bare URL
  by default.

### HTML

Don't use HTML, which the guide strongly discourages. This includes `<details>`
and HTML used for layout, such as an image that HTML sizes or centers. Use only
the following elements, which do what Markdown can't:

- `<kbd>`, which marks a keyboard key. Follow `technical-writing-guidelines`
  when available. Otherwise, put each key in its own element, spell out key
  names such as `Control`, and join simultaneous keys with `+`, as in
  `<kbd>Control</kbd>+<kbd>C</kbd>`. Write "then" between successive keys.
- `<picture>`, which shows a different image in light and dark mode, in GitHub
  files only. Pandoc drops it from output other than HTML, so the image
  disappears. Write it as follows, with alt text that describes the image:

  ```html
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="DARK-IMAGE-PATH" />
    <img alt="ALT-TEXT" src="LIGHT-IMAGE-PATH" />
  </picture>
  ```

### Math and Strikethrough

GitHub, Pandoc, and Obsidian support the following syntax:

- Write inline math as `$...$` and display math as a `$$` block. Don't use
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
- Don't wrap Markdown that you write into a pull request description or a
  comment on GitHub, because GitHub shows each line break there.

## Pandoc Files

The following sections apply only to Pandoc files.

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

Type straight quotes and `...`, which Pandoc's `smart` extension turns into
curly quotes and an ellipsis. `smart` also turns `--` into an en dash and `---`
into an em dash, so don't type either in prose. Type Unicode only for characters
that `smart` doesn't write, such as `°`, `×`, `±`, a minus sign outside math,
and the primes in `5′10″`.

Put command-line flags in backticks, because outside code `smart` turns the `--`
in `--fix` into an en dash.

## Obsidian Files

The following sections apply only to Obsidian files. For syntax that they don't
describe, use the `obsidian-markdown` skill when it's available, or otherwise
the [Obsidian Flavored Markdown][obsidian-markdown] help page and the pages it
links to. Where the two differ, follow these sections.

[obsidian-markdown]: https://obsidian.md/help/obsidian-flavored-markdown

### Note Structure

Obsidian shows a note's file name as its title, so don't start a note with a
title heading or add a `title` property. Start sections at `#`.

Put tags in the `tags` property, as a YAML list, instead of in the text. Write
each tag without `#`, in lowercase `kebab-case`, such as `field-work`.

Name a note by its title, with spaces and in title case, such as
`Drift Correction.md`, instead of in `kebab-case`, because Obsidian shows the
file name as the note's title and uses it in wikilinks. Follow the vault's
existing names when they differ.

### Links and Embeds

- Link to a note in the vault with a wikilink, such as `[[Field Log]]` or
  `[[Field Log#Day 2|the second day]]`, because Obsidian updates wikilinks when
  a note is renamed. When the vault's `.obsidian/app.json` file sets
  `"useMarkdownLinks": true`, use Markdown links instead.
- Embed an image as `![[<file>|<alt-text>|<width>]]`, such as
  `![[drift-plot.png|Clock drift over 30 days|400]]`, with alt text that
  describes the image. Obsidian's help documents only the width, but Obsidian
  reads the text before it as alt text.
- Add a block ID only when something links to the block. Write it in
  `kebab-case`, such as `^corrected-time`.

### Callouts

Use a callout, such as `> [!warning]`, only for something the reader must not
miss, and never put two callouts in a row. Use any of Obsidian's callout types,
written in lowercase, as Obsidian's help writes them. Write a callout's title in
title case, as in a heading. Fold a callout that holds extra detail so that it
starts collapsed, as in `> [!faq]- <title>`.

### Comments, Footnotes, and Tasks

- Write comments with `%%`.
- Write footnotes as `[^<label>]`, not as `^[<note>]`, which Obsidian shows only
  in Reading view.
- Mark tasks only with `[ ]` and `[x]`.
- Leave `==` highlights to the user, who uses them to mark text to come back to.
  Don't add them, and keep the ones in a note that you edit.

### Characters

Obsidian doesn't change punctuation as Pandoc's `smart` extension does. Type
straight quotes, and type other permitted characters themselves, such as `−` and
`°`. Don't type `--` or `---` for a dash.

## Tooling

Format Markdown with Oxfmt and lint it with markdownlint-cli2. For projects
without their own configuration, use the `assets/.oxfmtrc.json` and
`assets/.markdownlint.jsonc` files from this skill. For Pandoc files, use the
`assets/pandoc/.oxfmtrc.json` and `assets/pandoc/.markdownlint.jsonc` files, and
for Obsidian files, the `assets/obsidian/.oxfmtrc.json` and
`assets/obsidian/.markdownlint.jsonc` files.

Use the versions that the project pins, such as with `npx oxfmt`, and otherwise
the latest releases, such as with `npx oxfmt@latest`. In a new project with a
`package.json` file, add `oxfmt` and `markdownlint-cli2` as development
dependencies at exact versions, because Oxfmt hasn't reached version 1.0 and its
output can change between releases. For each file you change, follow these steps
within the cleanup scope defined in the "Tooling" section of
[Coding Standards](../SKILL.md):

1. Apply automatic lint fixes:

   ```sh
   markdownlint-cli2 --fix FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the Markdown file.

2. Fix the remaining findings within that scope by hand.
3. Format the file:

   ```sh
   oxfmt FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the Markdown file.

When the configuration isn't in the project, pass `-c <configuration-path>` to
Oxfmt with the path to the `assets/.oxfmtrc.json` file, and
`--config <configuration-path>` to markdownlint-cli2 with the path to the
`assets/.markdownlint.jsonc` file. For a Pandoc file, pass the files in
`assets/pandoc/` instead, and for an Obsidian file, the files in
`assets/obsidian/`, because the main Oxfmt configuration wraps lines at 80
characters.

When a project has its own configuration and Pandoc files, add these settings
for the Pandoc files, asking the user first in an existing project:

- An override in the project's Oxfmt configuration that keeps each line as
  written. Replace the placeholder with a pattern that matches the Pandoc files,
  such as `paper/**/*.md`:

  ```json
  "overrides": [{"files": ["PANDOC-FILE-PATTERN"], "options": {"proseWrap": "preserve"}}]
  ```

- A `.markdownlint.jsonc` file in the folder that holds the Pandoc files, which
  turns off the line limit and the rule that allows only one top-level heading.
  Replace the placeholder with the path from that folder to the project's
  markdownlint configuration, such as `../.markdownlint.jsonc`:

  ```jsonc
  {"extends": "PROJECT-CONFIGURATION-PATH", "MD013": false, "MD025": false}
  ```

  A `.markdownlint.jsonc` file in a folder replaces the configuration of the
  folders above it. Use `"extends"` to preserve the parent's customizations;
  without it, unspecified rules use their defaults and remain enabled.

- When the project has an `.editorconfig` file, including a copy of
  `assets/.editorconfig`, a section that turns off the line length for the
  Pandoc files. Otherwise, some editors, such as Neovim, wrap each line at that
  length while you type. Replace the placeholder with an EditorConfig pattern
  that matches the Pandoc files, such as `paper/**.md`, where `**` also matches
  `/`:

  ```ini
  [PANDOC-FILE-PATTERN]
  max_line_length = off
  ```

When a project has its own configuration and Obsidian files, add the same
settings for the Obsidian files, including the `.editorconfig` section, with two
changes: set `proseWrap` to `"never"`, and also turn off `MD041` in the
`.markdownlint.jsonc` file, because a note can start without a heading.

The first time Oxfmt formats an existing file, it rewraps every paragraph. When
formatting a file you change would rewrap paragraphs you didn't change, tell the
user and offer to format the file in a separate commit first, so that the
formatting doesn't hide your change.

Suppress a markdownlint finding with
`<!-- markdownlint-disable-next-line <rule-code> -->`, such as with `MD024` for
a heading that a template repeats.

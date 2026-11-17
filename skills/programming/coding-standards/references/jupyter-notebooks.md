# Jupyter Notebooks

## Baseline

This reference covers Jupyter notebooks with a Python kernel. For a notebook
with another kernel, tell the user that this skill has no notebook conventions
for that language, and follow the project's existing notebooks.

Follow [Python](python.md) in code cells and [Markdown](markdown.md) in Markdown
cells. The following sections extend them and take precedence where they differ.

## Markdown Cells

Write Markdown cells as GitHub files, wherever the notebook is stored. Follow
the "Formatting," "All Files," and "GitHub Files" sections of
[Markdown](markdown.md), except for the following GitHub syntax, which
JupyterLab, VS Code, or GitHub's notebook viewer shows as literal text or drops:

- Alerts, such as `> [!WARNING]`, which show as a block quote that starts with
  `[!WARNING]`. Start the paragraph with a bold label instead, such as
  `**Warning**:`. Use one only for something the reader must not miss, and never
  put two in a row.
- Footnotes, which show as literal `[^<label>]` text. Put the note in the
  sentence it belongs to, or in a sentence after it.
- Task lists, which VS Code shows as literal `[ ]` and `[x]` text and GitHub
  shows without checkboxes. Use a plain list, and state each item's status in
  words when it matters.
- Mermaid diagrams, which GitHub shows as source text. Show a diagram as an
  image instead.
- `<picture>`, which JupyterLab and GitHub reduce to the light-mode image. Use a
  Markdown image instead.

Put a reference link's definition, such as `[site]: https://example.com`, in the
same cell as the link. Each cell renders on its own, so a link whose definition
is in another cell shows as literal text.

Don't link to headings in the notebook, because no link works in JupyterLab, VS
Code, and GitHub alike. Refer to a section by name instead, in quotation marks
and without a link, such as the "Drift Results" section.

## Code Cells

Follow [Python](python.md) in code cells, with the following exceptions:

- Leave out the module docstring and `__all__`, because no code imports a
  notebook. Describe what the notebook does in its first Markdown cell instead.
- Instead of the module order in the "File Layout" section of
  [Python](python.md), order cells so that the notebook runs from top to bottom.
  Define each function and constant in a cell above the cells that use it.
- Put all imports in one cell at the top of the notebook, after any cell that
  installs packages, grouped and ordered as PEP 8 describes. Ruff doesn't check
  where imports are, so check this yourself.

In a notebook that belongs to a project, don't install packages from a cell. Add
each package to the project's dependencies instead, using the project's
dependency workflow. In a standalone notebook, install packages in a cell before
the imports with `%pip install`, not `!pip install`, because `%pip` installs
into the environment of the running kernel.

## Editing Notebooks

Change only the cells that the request needs. In every other cell, keep the
position, source, outputs, execution count, ID, attachments, and metadata, and
keep the notebook's own metadata.

In an existing notebook, apply the "Code Cells" rules about imports and cell
order only to the cells you add or change. Don't move other imports or reorder
other cells unless the user asks. Instead, tell the user where they are.

When you change a code cell, clear its outputs and set its execution count to
`null`, because they no longer match its source. Some notebook editing tools do
this for you. Unless you ran the notebook afterward, tell the user which cells
to rerun.

Edit cells with a tool that reads and writes notebooks, such as a notebook
editing tool or the `nbformat` library, rather than editing the JSON as text.
These tools can still change the rest of the file, such as by dropping the final
newline or reordering keys. After each edit, compare the file with its previous
version, and restore any change outside the cells you edited. Use `git diff`,
which shows changes to the file's text that notebook tools such as `nbdiff`
hide. When Git doesn't track the notebook, copy it before editing so that you
can compare. Jupyter writes notebooks with keys in alphabetical order, 1-space
indentation, characters such as `°` as written rather than escaped, and a final
newline.

## Tooling

Check code cells with Ruff and mypy, and format Markdown cells with Oxfmt, as
the "Tooling" sections of [Python](python.md) and [Markdown](markdown.md)
describe, with the following differences.

Ruff reads notebooks directly. Run `ruff check --fix` and `ruff format` on the
notebook as the Python reference describes, with the same configuration options.

mypy doesn't read notebooks: run on one directly, it reports success without
checking the code. Run it through nbQA, in the environment that has the
project's dependencies:

```sh
uv run --with nbqa nbqa mypy NOTEBOOK-PATH
```

Replace `NOTEBOOK-PATH` with the path to the notebook. Outside a project, run
`uvx --with mypy nbqa mypy NOTEBOOK-PATH` instead. When the configuration isn't
in the project, pass `--config-file <configuration-path>` after the notebook
path.

Don't run the doctest step from the Python reference, because it runs every cell
in the notebook.

Format Markdown cells with Oxfmt through nbQA, which copies the cells into a
temporary Markdown file next to the notebook, runs Oxfmt on it, and copies the
results back. First, preview the changes:

```sh
uvx nbqa "npx oxfmt" NOTEBOOK-PATH --nbqa-md --nbqa-shell --write --nbqa-diff
```

Replace `NOTEBOOK-PATH` with the path to the notebook. To apply the changes, run
the same command without `--nbqa-diff`. Use the Oxfmt version that the project
pins, and otherwise write `npx oxfmt@latest`. When the configuration isn't in
the project, add `-c <configuration-path>` with the path to the
`assets/.oxfmtrc.json` file.

nbQA exits with status 0 even when it fails to process a notebook. Read its
output, and treat "failed to process" as a failure.

Don't lint Markdown cells with markdownlint-cli2. nbQA joins the cells into one
file with separator lines that break markdownlint's heading rules. Review the
cells against the "Markdown Cells" section instead.

When the project's Oxfmt configuration overrides options for Markdown files in a
folder that holds notebooks, such as `proseWrap` for Obsidian files, the
override also applies to the notebooks' Markdown cells. nbQA names its temporary
files `*_nbqa_ipynb.md`, so add an override for them after the folder's override
that restores the project's settings for GitHub files, asking the user first in
an existing project. For example:

```json
{"files": ["**/*_nbqa_ipynb.md"], "options": {"proseWrap": "always"}}
```

The first time Ruff or Oxfmt formats an existing notebook, it can change every
cell. When formatting a notebook you change would change cells you didn't, tell
the user and offer to format the notebook in a separate commit first. After
formatting, check that only cell sources changed, as the "Editing Notebooks"
section describes.

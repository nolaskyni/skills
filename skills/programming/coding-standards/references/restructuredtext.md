# reStructuredText

## Baseline

Follow the [reStructuredText markup][devguide-markup] page of the Python
Developer's Guide. The following sections extend it and take precedence where
they differ.

[devguide-markup]: https://devguide.python.org/documentation/markup/

The page is written for CPython's documentation. Roles that only CPython
defines, such as `:gh:`, `:issue:`, and `:source:`, don't apply. The page covers
markup only. For the wording of the text, follow the
`technical-writing-guidelines` skill when it's available, and otherwise the
style of the surrounding documentation.

## File Types

reStructuredText appears in three kinds of files, which support different
markup:

- **Sphinx files**: an `.rst` file with a `conf.py` file in its folder or in a
  folder above it, within the project. Sphinx builds these files, so they can
  use Sphinx roles and directives, such as `:func:` and `.. versionadded::`.
- **Docutils files**: every other `.rst` file. GitHub and PyPI render these
  files with Docutils, which doesn't support Sphinx roles and directives. A file
  that GitHub or PyPI renders on its own is a Docutils file even when a Sphinx
  page includes it, such as a `README.rst` file at the project root or the file
  named in `readme` in the `pyproject.toml` file.
- **Docstrings**: Python docstrings in the numpydoc format. Follow the "Comments
  and Documentation" section of [Python](python.md) for which objects need a
  docstring and which sections it has, and this reference for the markup inside
  it.

## Formatting

No formatter supports reStructuredText well, so format files and docstrings by
hand, and check them with the tools in the "Tooling" section.

Indent as follows:

- In `.rst` files, indent the options and content of a directive, and a literal
  block after `::`, by 3 spaces, as the baseline asks.
- In docstrings, indent the same content by 4 spaces, to match the Python code
  around the docstring.
- In both, indent Python code inside a code block or literal block by 4 spaces
  for each level.
- Line up the second and later lines of a citation or footnote with its text,
  which starts 3 spaces in, after `.. [1]` and a space.

Put a blank line before and after each list, directive, and literal block, and
between a directive's options and its content. Without the blank line before it,
reStructuredText reads a list or directive as part of the paragraph above, and
no linter reports it. For example:

```rst
Install the package:

.. code-block:: sh
   :caption: Install from PyPI

   pip install sensor-tools
```

Keep lines in `.rst` files to 80 characters. Tables, code, and long URLs can be
longer. Wrap docstrings at 75 characters, as [Python](python.md) asks.

## Markup

### Code and Names

Put code and values in double backticks in every file type, as in ` ``nan`` `
and ` ``window_length=3`` `. Use single backticks only as follows:

- In docstrings, around parameter names and the names of modules, classes,
  functions, methods, and attributes, as numpydoc asks, as in
  `` `window_length` `` and `` `numpy.convolve` ``.
- In `.rst` files, only as part of a role or a link. Sphinx shows a bare
  `` `name` `` in italics, not as code.

### Cross-References

- In Sphinx files, use a role, such as ``:func:`numpy.convolve` `` for a
  function or ``:ref:`moving-average` `` for a section with the label
  `.. _moving-average:`.
- In docstrings, write the name in single backticks, without a role. Add a role
  only when Sphinx doesn't turn the name into a link.
- In Docutils files, write the name in double backticks. To point to another
  page, use a link.

### Headings

In `.rst` files, underline a page's title with `=`, and its sections with `-`,
`^`, and `"`, in that order. Don't use overlines, which the baseline keeps for
the parts and chapters of a book-length document.

### Lists and Links

- Start each bullet with `-`.
- Write each link as an anonymous link, ending in two underscores, as in
  `` `SciPy guide <https://docs.scipy.org/doc/scipy/>`__ ``. Two named links
  with the same text and different URLs conflict.

### Code Blocks

- Put code in a `.. code-block:: <language>` directive in every file type, and
  name its language, as in `.. code-block:: python`, or `.. code-block:: text`
  for output. Don't write code as a literal block after `::`.
- Name the language with its short name in the
  [Pygments lexer list](https://pygments.org/docs/lexers/), such as `python`,
  `sh`, or `toml`. Sphinx and Docutils highlight code with Pygments. doc8
  reports a name that Pygments doesn't know in `.rst` files, but no tool checks
  the names in docstrings.
- In docstrings, put runnable examples in the Examples section as doctests, as
  numpydoc describes, without a directive.

### Math

When a docstring contains a backslash, as `:math:` and `.. math::` usually do,
start it with `r"""`. Otherwise, Python reads sequences such as `\b` and `\f` as
control characters, and the equation breaks without an error.

## Docutils Files

Docutils files can't use the roles and directives that Sphinx adds, such as
`:func:`, `:ref:`, `.. versionadded::`, and `.. autosummary::`. GitHub shows
them as raw markup, with no error, and Readme Renderer, which PyPI uses to show
package descriptions, fails on them. Use only the roles and directives that
Docutils defines, such as `.. note::` and `.. code-block::`, and write names and
cross-references as the "Markup" section describes.

In a file that PyPI renders, such as the file named in `readme` in the
`pyproject.toml` file, write every link with an absolute URL. PyPI shows the
file at `https://pypi.org/project/<name>/`, where a relative link such as
`LICENSE` doesn't resolve.

## Review Checklist

The tools in the "Tooling" section don't report the following mistakes. When
writing or reviewing reStructuredText, read each changed `.rst` file and
docstring for them:

- A list, directive, or code block without a blank line before it, which renders
  as part of the paragraph above.
- Directive content indented by the wrong amount: 3 spaces in `.rst` files and 4
  in docstrings.
- In docstrings, a link without the `__` at its end, which doesn't become a
  link. Sphinx Lint reports this only in `.rst` files.
- In docstrings, single backticks around a value or code, as in `` `None` ``.
  Sphinx Lint reports this only in `.rst` files.
- In docstrings, a `code-block` language that isn't a Pygments short name. doc8
  reports this only in `.rst` files.
- In Docutils files other than the one named in `readme`, Sphinx roles and
  directives. Readme Renderer checks only that file.
- In a file that PyPI renders, a relative link.

## Tooling

Check reStructuredText with linters only, as the "Formatting" section describes.
When the project pins a version of a tool, such as in its development
dependencies, run that version, such as with `uv run`. Otherwise, run its latest
release with `uvx`.

For each file you change, follow these steps within the cleanup scope defined in
the "Tooling" section of [`coding-standards`](../SKILL.md):

1. For an `.rst` file, check its markup with Sphinx Lint:

   ```sh
   uvx sphinx-lint --enable default-role FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file. `--enable default-role` turns
   on the check for single backticks, which Sphinx Lint leaves off by default.

2. Check the same file with doc8:

   ```sh
   uvx doc8 --quiet --max-line-length 80 FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

3. For the file named in `readme` in the `pyproject.toml` file, also check that
   PyPI can render it:

   ```sh
   uvx --from readme-renderer python -W ignore::UserWarning \
     -m readme_renderer FILE-PATH -o /dev/null
   ```

   Replace `FILE-PATH` with the path to the file. `-W ignore::UserWarning` hides
   a warning that Markdown support isn't installed, which a reStructuredText
   file doesn't need.

4. For a Python file, check the markup in its docstrings with
   flake8-rst-docstrings:

   ```sh
   uvx --with flake8-rst-docstrings flake8 --select RST \
     --rst-roles func,meth,class,mod,attr,exc,data,obj,ref,doc,term \
     --rst-directives versionadded,versionchanged,deprecated,autosummary \
     FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the Python file. `--select RST` limits
   Flake8 to this plugin's checks, because Ruff checks the rest of the file. Add
   any other Sphinx roles and directives that the docstrings use to
   `--rst-roles` and `--rst-directives`, or the plugin reports them as unknown.

5. Read the changed files for the mistakes in the "Review Checklist" section.

The Ruff checks in [Python](python.md) also cover docstrings. Ruff's `D301` rule
reports a docstring that contains a backslash but doesn't start with `r"""`.

When uv isn't available, run the tools from the project's environment if it has
them. Otherwise, tell the user which checks didn't run.

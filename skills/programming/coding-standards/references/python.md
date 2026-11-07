# Python

## Baseline

Follow [PEP 8](https://peps.python.org/pep-0008/). The sections below extend it
and take precedence where they differ.

## Formatting

Limit lines of code to 88 characters, the default line length of
`ruff format`. Wrap docstrings at 75 characters, as the numpydoc guide asks,
and comments at 72 characters, as PEP 8 asks. `ruff format` does not rewrap
docstrings or comments, so wrap them yourself.

## File Layout

PEP 8 covers the module docstring, module-level dunder names, and imports.
After the imports, order a module as follows:

1. Constants.
2. Exceptions and records.
3. Public functions and classes.
4. Private functions and classes.

Define `__all__` in every module that other code imports, listing its public
names. Leave it out of scripts and test modules.

Define base classes, decorators, and values used as defaults before the code
that uses them, even when this changes the order. When a module becomes hard
to follow in this order, split it into smaller modules.

## Imports

PEP 8 covers where imports go and how they are grouped and ordered. In
addition:

- Import the module, not the function, when you use a function from another
  module. Write `import statistics` and call `statistics.fmean(values)`, not
  `from statistics import fmean` and `fmean(values)`.
- Import classes, types, and decorators by name. Write
  `from pathlib import Path` and use `Path`, not `import pathlib` and
  `pathlib.Path`.
- Use only the import aliases that the project's Ruff configuration expects,
  such as `import numpy as np`. Ruff checks them with rule `ICN001`. These
  aliases are exceptions to the naming rules.

## Comments and Documentation

Write docstrings exactly as the
[numpydoc style guide](https://numpydoc.readthedocs.io/en/latest/format.html)
describes, including its advice to keep LaTeX to a minimum and to show simple
equations as code. Treat that guide as the authority on docstrings, because it
may change after this reference was written.

The guide does not say which objects need a docstring, so follow these rules:

- Give every module a docstring with at least a summary line.
- Give every public function, class, and method a docstring with the sections
  that apply to it, such as Parameters and Returns.
- Document a constructor's parameters in the class docstring, and do not give
  `__init__` its own docstring.
- Give a private function or method, whose name starts with an underscore, a
  docstring only when its behavior is not obvious from its name and body. This
  replaces the PEP 8 advice to describe every non-public method in a comment
  after its `def` line.
- Test functions need no docstring. Name each test for the behavior it checks.

## Python Version

Choose the minimum Python version by how the code is used:

- For a package that other people or projects install or import, support
  each Python version for three years after its release, as
  [SPEC 0](https://scientific-python.org/specs/spec-0000/) describes.
- For a script, notebook, or model that runs in one environment, pin the
  newest Python version that all of its dependencies support. Record it in
  the project, such as in `requires-python` in `pyproject.toml`, a
  `.python-version` file, or the inline metadata of a single-file script.

When a script grows into a package that others install, switch it to SPEC 0.
Do not change a project's minimum or pinned Python version without asking the
user.

## Type Hints

- Annotate every parameter and return value of every function and method,
  including private ones. Write `-> None` for a function that returns
  nothing.
- Annotate each parameter with the most general type that the function
  needs, so that callers can pass what they have:
  - `Iterable[Reading]` when the function loops over the argument once.
  - `Sequence[float]` when it needs `len()` or indexing.
  - `Mapping[str, float]` when it only reads a dictionary.
  - `numpy.typing.ArrayLike` when it converts the argument with
    `np.asarray`.
  - `numpy.typing.NDArray` with a data type, such as `NDArray[np.float64]`,
    when it needs array behavior, such as `.shape` or changes in place.
- Annotate each return value with the specific type that the function
  returns, such as `list[Reading]`, `dict[str, float]`, or
  `NDArray[np.float64]`.
- Annotate a local variable only when a type checker cannot infer its type,
  such as an empty container or a variable that starts as `None`.
- Use built-in generics, such as `list[int]`, write `float | None` instead of
  `Optional[float]`, and import abstract types, such as `Iterable`, from
  `collections.abc`.
- Do not use `from __future__ import annotations`. Until the minimum Python
  version is 3.14 or later, put a forward reference in quotes, such as
  `"Spectrum"`.

## Function Signatures

- Make the main data inputs, usually one or two, positional. Make every
  option, meaning a parameter that changes how the function works rather than
  what it works on, keyword-only by placing it after a bare `*`, as in
  `has_gap(readings, *, maximum_gap_seconds=300.0)`.
- Always make Boolean options keyword-only.
- When a function must match a signature defined elsewhere, such as a model
  function that `scipy.optimize.curve_fit` calls with positional arguments,
  follow that signature instead.
- Prefer explicit parameters to `*` and `**` parameters. Use them only when a
  function forwards arguments to another function or accepts any number of
  inputs.
- Name `*` and `**` parameters for their role, such as `*spectra` or
  `**curve_fit_options`. When a function forwards any call unchanged, such as
  a decorator's wrapper, name them `*arguments` and `**keyword_arguments`.

## Records

- Define a record of values as `@dataclass(frozen=True, slots=True)`.
- When a record holds NumPy arrays, also pass `eq=False`, because the
  generated equality and hash fail on arrays. Compare the arrays explicitly,
  such as with `np.array_equal`.
- Do not change an array stored in a record. `frozen` stops fields from being
  reassigned, but not array contents from changing.
- Use `typing.NamedTuple` when callers need to unpack or index the record
  like a tuple, and `typing.TypedDict` only to describe dictionary-shaped
  data from outside the program, such as parsed JSON.
- Use a plain class when an object maintains changing state through its
  methods.
- Use `attrs` or `pydantic` only when the project already depends on them or
  needs to validate external input.

## Errors

PEP 8 covers exception names, inheritance, chaining, and `try` blocks. In
addition:

- Raise a built-in exception, such as `ValueError` or `TypeError`, when one
  fits. Define a custom exception only when callers need to catch that
  failure separately, and make it a subclass of the closest built-in
  exception.
- Do not use `assert` to check inputs or data, because Python removes
  `assert` statements when it runs with `-O`. Raise an exception instead,
  and use `assert` only in tests.
- Catch an exception only where the code can handle it. Never silence an
  exception with `pass` or replace it with a placeholder value.
- Report a problem that does not stop the calculation, such as dropped
  samples, with `warnings.warn`, a specific warning category, and
  `stacklevel=2`, and document it in the Warns section of the docstring. Do
  not report it with `print`.
- Keep NumPy floating-point warnings visible. Suppress them only with
  `np.errstate` around code that expects and handles `inf` or `nan` values.

### Messages

Write error, warning, and log messages in the same style:

- Start with a lowercase letter, unless the message starts with an
  identifier, which keeps its case. Do not end with a period.
- Put identifiers in backticks: parameter, variable, attribute, function,
  class, and type names, and names from outside the code that the code uses
  by their exact spelling, such as a CSV column.
- Show values with `!r` and without backticks, so that strings appear in
  quotes and numbers appear bare.
- Say what was expected, then the value received.
- When parsing input, put the location first, followed by a colon.
- Write the message inline in the `raise` statement or warning call. When it
  is too long for one line, split it into adjacent strings inside the
  parentheses.

For example:

```python
raise ValueError(f"`method` must be 'lm' or 'trf', got {method!r}")

raise ValueError(
    f"line {line_number}: invalid `temperature_celsius` value {text!r}"
) from error

raise ValueError(
    "`times_seconds` and `values` must have the same length, got "
    f"{len(times_seconds)} and {len(values)}"
)
```

## Tooling

Format and lint Python with Ruff, and check types with mypy. For projects
without their own configuration, use `assets/ruff.toml` and
`assets/mypy.ini` from this skill. `ruff.toml` does not set
`target-version`, so Ruff reads the minimum Python version from
`requires-python` in `pyproject.toml`.

Use the Ruff version that the project pins, such as with `uv run ruff`, and
otherwise the latest release, such as with `uvx ruff`. Run mypy in the
environment that has the project's dependencies installed, such as with
`uv run mypy`, because it needs them to check calls into libraries. For each
file you change:

1. Run `ruff check --fix <file-path>`, which applies only safe fixes. Do not
   pass `--unsafe-fixes`.
2. Fix the remaining findings by hand.
3. Run `ruff format <file-path>`, because fixes can leave code unformatted.
4. Run `mypy <file-path>`, and fix each error it reports.

When the configuration is not in the project, pass
`--config <configuration-path>` to Ruff with the path to `assets/ruff.toml`,
and `--config-file <configuration-path>` to mypy with the path to
`assets/mypy.ini`.

Suppress a Ruff finding with `# noqa: <rule-code>`, such as `# noqa: N803` for
a parameter named `X` that a scikit-learn interface requires, and a mypy
error with `# type: ignore[<rule-code>]`.

When mypy cannot find types for a library, add its stub package, such as
`scipy-stubs` or `pandas-stubs`, as a development dependency, asking the user
first in an existing project. Do not set `ignore_missing_imports`, because it
turns off checking for that library without saying so.

Run the docstring examples of each module you change, such as with
`pytest --doctest-modules <file-path>`.

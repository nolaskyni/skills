# TOML

## Baseline

TOML has no widely used style guide. Follow version 1.0.0 of the
[TOML specification](https://toml.io/en/v1.0.0) and the rules in the following
sections. Don't use syntax that only version 1.1.0 allows, such as an inline
table that spans several lines, because Python's `tomllib` reads only version
1.0.0.

A file whose structure a tool defines, such as `pyproject.toml`, `Cargo.toml`,
or `ruff.toml`, follows that tool's documentation. Keep the tool's names, such
as `requires-python` or mypy's `disallow_untyped_defs`.

## Formatting

Oxfmt formats TOML files with 2-space indentation, and splits an array that
doesn't fit in 80 characters into one item on each line, with a comma after
every item. Leave the layout as Oxfmt writes it, and follow these rules, which
Oxfmt doesn't apply:

- Put a blank line before each table header, and none between a header and its
  first key.
- Use an inline table only when it fits on one line. Otherwise, write a separate
  table, as in `[tool.ruff.lint.per-file-ignores]`. Oxfmt splits a long inline
  table in a way that's hard to read.
- Keep lines to 80 characters. Oxfmt doesn't split long strings, so split them
  as the "Strings" section describes.

## Keys

- Write keys without quotes, unless they contain characters that a bare key
  can't, such as the `*` and `/` in a path pattern. Oxfmt keeps quotes that
  aren't needed.
- Quote a key that contains a dot as part of its name, for example,
  `"ui.background" = "white"`. Without quotes, TOML reads the dot as a dotted
  key, so `ui.background` sets `background` in a nested `ui` table.
- Keep keys in the order they were written. Sort them only when a tool or the
  project does.
- In a file whose structure the project defines, write keys in `kebab-case`, as
  `pyproject.toml`, Cargo, and Ruff do, and follow the "Naming" section of
  [Coding Standards](../SKILL.md), as in `station-id` and
  `sample-interval-seconds`. To read these keys in Python, see the "Records"
  section of [Python](python.md).

## Values

### Strings

- Write strings in double quotes. Use a single-quoted literal string only for a
  value that contains backslashes, such as a regular expression, as in
  `'^(_+|unused_\w+)$'`.
- Write text that contains line breaks as a `"""` string.
- Split a long one-line string into a `"""` string that starts with `"""\`. End
  each line with a space and `\`, and indent the lines after the first by 2
  spaces. TOML removes each `\`, the line break, and the indentation, so the
  value is one line.

For example:

```toml
summary = """\
  Rooftop station that measures air temperature and humidity for the \
  campus heat study."""
```

### Enum Values

Write enum values with more than one word in `kebab-case`, so that they match
the keys, as in `status = "under-maintenance"`.

### Dates and Times

- Write dates and times as TOML values, without quotes, so that a parser returns
  a date or time instead of a string. `tomllib` returns a time-zone-aware
  `datetime` for a timestamp with an offset.
- Write a timestamp with its time-zone offset, as in
  `started-at = 2026-11-10T14:00:00Z`.
- Write a date without a time as a date only, as in
  `calibration-date = 2026-11-03`.
- Write a duration as a number with the unit in the key, as in
  `sample-interval-seconds = 600`, because TOML has no duration type.

## Comments

Write comments as the "Comments" section of [Coding Standards](../SKILL.md)
describes. Put a comment that explains a table on the line above its header. Use
a trailing comment only for a short note, as in
`select = ["B", "D"] # Bugbear and docstrings`.

For example:

```toml
# Settings for one weather station.

station-id = "ws-04"
status = "under-maintenance"
started-at = 2026-11-10T14:00:00Z
sample-interval-seconds = 600

# Readings above these limits trigger the alerts in `alerts.py`.
[thresholds]
warning-celsius = 30
critical-celsius = 45
```

## Tooling

Format TOML with Oxfmt. For projects without their own configuration, use
`assets/.oxfmtrc.json` from this skill.

Oxfmt reports some syntax errors, such as an unclosed string, but it accepts
duplicate keys and syntax that only TOML 1.1.0 allows. Python's `tomllib`
rejects both, so use it to check each file. It needs Python 3.11 or later.

For each file you change, follow these steps within the cleanup scope defined in
the "Tooling" section of [Coding Standards](../SKILL.md):

1. Format the file:

   ```sh
   oxfmt FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

2. Check that the file is valid TOML:

   ```sh
   uv run --no-project --python '>=3.11' python -c 'import sys, tomllib; tomllib.load(open(sys.argv[1], "rb"))' FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file. uv uses an installed Python
   3.11 or later, or downloads one, and `--no-project` keeps it from setting up
   the project's environment first.

When uv isn't installed, run the check in step 2 with `python3` instead, if
`python3 --version` shows 3.11 or later. Otherwise, tell the user that the check
didn't run.

When the configuration isn't in the project, pass `-c <configuration-path>` to
Oxfmt with the path to `assets/.oxfmtrc.json`.

# JSON

## Baseline

Follow the
[Google JSON Style Guide](https://google.github.io/styleguide/jsoncguide.html)
for JSON whose structure the project defines, such as data files, API payloads,
and the project's own configuration files. The following sections extend it and
take precedence where they differ.

The guide is written for Google's APIs. The structure that it reserves for them
doesn't apply: the top-level `apiVersion`, `context`, `id`, `method`, `params`,
`data`, and `error` properties, and the properties it defines inside `data` and
`error`, such as `kind`, `items`, and the paging and link properties.

A file whose structure a tool defines, such as `package.json`, `tsconfig.json`,
or a VS Code settings file, follows that tool's documentation. Keep the tool's
names, such as `devDependencies` or `editor.formatOnSave`.

## Files

- Use the `.json` extension for data and for configuration files whose tool
  doesn't read comments. Don't write comments in them.
- Use the `.jsonc` extension for a configuration file whose tool reads comments,
  when the tool accepts that name. When the tool requires a name, such as
  `tsconfig.json`, keep it, and write comments only if the tool reads them.
  Write comments as the "Comments" section of [Coding Standards](../SKILL.md)
  describes.
- Use the `.geojson` extension for GeoJSON, as the "Coordinates" section
  describes.
- Don't write trailing commas in any JSON or JSONC file. VS Code warns about
  them in JSONC files and reports them as errors in JSON files.

## Formatting

Oxfmt formats JSON and JSONC files with 2-space indentation, and wraps them at
80 characters. Leave the layout as Oxfmt writes it, with these details:

- Oxfmt puts a short array on one line, as in `"tags": ["outdoor", "roof"]`.
- Oxfmt keeps an object on several lines when its first property starts on a new
  line. Put a short object on one line only when its properties form one value,
  such as `{"latitudeDegrees": 40.6894, "longitudeDegrees": -74.0447}`.
- Oxfmt writes `package.json` as npm does, with every array and object on
  several lines.

## Names

Write property names in `camelCase`, and follow the "Naming" section of
[Coding Standards](../SKILL.md). Write each acronym in uniform case, as in
`stationID`, and name the unit of a plain number, as in `sampleIntervalSeconds`.
The keys of an object used as a map can be any string, such as sensor IDs or
file paths.

## Values

### Missing Values

- Leave out an optional property that has no value, instead of writing `null`.
- Keep `0`, `false`, `""`, and `[]` when they're real values. For example,
  `"tags": []` says that a station has no tags, but leaving out `tags` says
  nothing about them.
- Write `null` for a missing value inside an array, as in
  `"temperaturesCelsius": [12.4, null, 12.9]`, because leaving it out would
  shift the values after it.
- Never write `NaN`, `Infinity`, or `-Infinity`, which aren't valid JSON.
  Python's `json.dumps` writes them unless you pass `allow_nan=False`, so change
  them to `None` before writing the file.

### Enum Values

Write enum values as strings in `camelCase`, so that they match the property
names in the same file, as in `"status": "underMaintenance"`. This replaces the
guide's Java-style example, `"WHITE"`.

### Dates and Times

- Write a timestamp as an RFC 3339 string with a time-zone offset, such as
  `"2026-11-10T14:00:00Z"`. Accept either `Z` or `+00:00` for UTC, because
  JavaScript's `toISOString()` writes `Z` and Python's `isoformat()` writes
  `+00:00`.
- Write a date without a time as a date only, as in
  `"calibrationDate": "2026-11-10"`.
- Keep the offset of a local time that matters, as in
  `"2026-11-10T09:00:00-05:00"`, instead of converting it to UTC.
- Don't add `UTC` to the name of a timestamp, as in `"calibratedAtUTC"`, because
  the string states its offset.
- Write a duration as a number with the unit in the name, as in
  `"readingTimeoutSeconds": 30`, instead of the guide's ISO 8601 strings, such
  as `"PT30S"`. Use ISO 8601 durations only where a tool or API requires them.

### Coordinates

Write coordinates as numbers, not as the ISO 6709 strings that the guide asks
for:

- In the project's own files, use separate properties with the unit in each
  name, as in
  `"location": {"latitudeDegrees": 40.6894, "longitudeDegrees": -74.0447}`.
- For geographic data that map tools read, write GeoJSON in a `.geojson` file.
  GeoJSON puts longitude before latitude, as in
  `"coordinates": [-74.0447, 40.6894]`.

## VS Code Files

VS Code formats its own configuration files and rewrites them when you change a
setting in its editors. Write these files as VS Code does, and don't format them
with Oxfmt, so that the two tools don't keep undoing each other's changes. These
files are the following:

- The files in a `.vscode` folder, such as `settings.json`, `extensions.json`,
  `launch.json`, and `tasks.json`
- Workspace files, which end in `.code-workspace`
- The files in VS Code's user folder, such as `settings.json`,
  `keybindings.json`, and snippets, and copies of them in a dotfiles repository.
  The user folder is `~/Library/Application Support/Code/User/` on macOS and
  `~/.config/Code/User/` on Linux.

In these files, follow these rules:

- Put every array and object that isn't empty on several lines, with one item on
  each line.
- Indent with 4 spaces, VS Code's default, unless the file already uses a
  different indentation.
- Use the setting names that VS Code and its extensions define, such as
  `editor.formatOnSave`.
- Write comments as in other JSONC files, and don't write trailing commas.

For example:

<!-- prettier-ignore -->
```jsonc
{
    // Format on save with the project's formatter.
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/.venv": true
    },
    "cSpell.words": [
        "numpydoc",
        "oxfmt"
    ]
}
```

`assets/.oxfmtrc.json` and `assets/.editorconfig` already cover these files.
When a project has its own Oxfmt configuration, ask the user before adding the
`ignorePatterns` entries from `assets/.oxfmtrc.json` to it. Until they agree,
don't run Oxfmt on these files.

## Tooling

Format JSON and JSONC with Oxfmt. For projects without their own configuration,
use `assets/.oxfmtrc.json` from this skill. It skips the files that the "VS Code
Files" section lists and leaves out trailing commas in `.jsonc` files.

Oxfmt reports syntax errors, such as a missing comma, but it accepts `NaN`,
comments, and trailing commas in `.json` files. Node's `JSON.parse` rejects all
three, so use it to check `.json` files. Don't use it on JSONC files, VS Code
files, or other files that allow comments.

For each file you change, follow these steps within the cleanup scope defined in
the "Tooling" section of [Coding Standards](../SKILL.md):

1. Format the file:

   ```sh
   oxfmt FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

2. For a `.json` file, check that it's valid JSON:

   ```sh
   node -e 'JSON.parse(require("fs").readFileSync(process.argv[1], "utf8"))' FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

When the configuration isn't in the project, pass `-c <configuration-path>` to
Oxfmt with the path to `assets/.oxfmtrc.json`.

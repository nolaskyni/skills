# Shell

## Baseline

Follow the
[Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
for Bash. Follow it for Zsh too where Zsh's syntax matches Bash's, and see the
"Zsh" section for the differences. For fish, follow the
[fish Script Style Guide](https://fishshell.com/docs/current/contributing.html#fish-script-style-guide)
and see the "fish" section. The following sections extend these guides and take
precedence where they differ.

Write scripts in Bash. Write Zsh or fish only for startup files and for
functions, completions, and plugins that run inside the shell, because those
must be in the shell's own language. Write POSIX `sh` only when the target
system has no Bash.

When a script grows beyond about 100 lines or has control flow that isn't
straightforward, rewrite it in the language that the project already uses, such
as Python or TypeScript, or in Python when there is no project.

## Formatting

Format Bash and Zsh with shfmt, and fish with `fish_indent`. Where shfmt's
output differs from the Google guide's spacing, as in `((a > b))` rather than
`(( a > b ))`, follow shfmt. Limit lines to 80 characters. Neither formatter
wraps long lines, so wrap them yourself.

## Files

- Name an executable script in `kebab-case` with no extension, such as
  `archive-logs`, and start it with `#!/usr/bin/env bash`, `#!/usr/bin/env zsh`,
  or `#!/usr/bin/env fish`.
- Give a file that other scripts source the extension `.sh`, `.zsh`, or `.fish`,
  no shebang, and no executable permission. Start a Bash library with
  `# shellcheck shell=bash`.

Order a script as follows: the shebang, a comment that summarizes the file,
`set -euo pipefail`, constants, `source` lines, functions, and a call to `main`
on the last line. Give each `source` line a ShellCheck directive that starts
with `SCRIPTDIR/`, so that the check works from any folder:

```bash
# shellcheck source=SCRIPTDIR/log-archive.sh
source "$(dirname "${BASH_SOURCE[0]}")/log-archive.sh"
```

## Bash Version

Write for Bash 3.2, which is `/bin/bash` on macOS and what `#!/usr/bin/env bash`
finds there unless a later Bash is installed. Write for a later version only
when the project states that minimum. ShellCheck doesn't flag features that Bash
3.2 lacks, so avoid them yourself:

| Feature added after Bash 3.2          | Bash 3.2 alternative         |
| ------------------------------------- | ---------------------------- |
| Associative arrays, with `declare -A` | A `case` statement           |
| `mapfile` and `readarray`             | A `while IFS= read -r` loop  |
| `${name,,}` and `${name^^}`           | `tr '[:upper:]' '[:lower:]'` |
| `**`, with `shopt -s globstar`        | `find`                       |

Under `set -u`, Bash 3.2 stops when it expands an empty array, as in
`"${files[@]}"`. Check the length first, as in `if ((${#files[@]} > 0)); then`.

## Quoting

Leave a regular expression unquoted after `=~`, as in `[[ "$1" =~ ^[0-9]+$ ]]`,
because quoting it turns it into a plain string.

## Errors

Put `set -euo pipefail` in every Bash and Zsh script. Still check failures that
matter explicitly, because `set -e` misses failures inside process
substitutions, such as `< <(find ...)`. Write `count=$((count + 1))`, not
`((count++))`, which exits when `count` is `0`.

### Messages

Write messages as Unix tools do: the script name, a colon, and a lowercase
message with no final period, written to stderr. Put values in single quotes.
Don't use backticks in messages, because a backtick inside a double-quoted
string runs a command. Add timestamps only to scripts that write logs. For
example:

```bash
error() {
  echo "${0##*/}: $*" >&2
}

error "-d must be a whole number of days, got '${minimum_age_days}'"
error "'${log_directory}' is not a directory"
```

Exit with status `2` for usage errors and `1` for other failures.

Write usage text with Git-style placeholders. For `-h`, print it to stdout and
exit with status `0`. After a usage error, print it to stderr and exit with
status `2`:

```bash
usage() {
  cat <<EOF
Usage: ${0##*/} [-d <days>] <log-directory> <archive-directory>

Moves *.log files older than <days> days (default ${DEFAULT_MINIMUM_AGE_DAYS})
from <log-directory> into a dated archive in <archive-directory>.
EOF
}
```

### Options

Parse options with `getopts` in silent mode, which starts the option string with
`:`, so that its messages match the style in the "Messages" section. Write a
`while` and `case` loop by hand only for long options. For example:

```bash
while getopts ':d:h' option; do
  case "${option}" in
    d) minimum_age_days="${OPTARG}" ;;
    h)
      usage
      exit 0
      ;;
    :)
      error "-${OPTARG} needs a value"
      exit 2
      ;;
    *)
      error "unknown option '-${OPTARG}'"
      usage >&2
      exit 2
      ;;
  esac
done
shift "$((OPTIND - 1))"
```

## Comments

Give each Bash and Zsh function a header comment in the following format:

- Start with a summary in the imperative, such as "Delete archives older than
  `ARCHIVE_RETENTION_DAYS` days."
- Always include `Arguments:`, with one line per argument, in order, and without
  `$1` names. Write `None` when there are no arguments.
- Include `Globals:`, `Outputs:`, and `Returns:` only when they apply. Include
  `Returns:` only when the exit status isn't the last command's.

Give a header to every function in a library, and to every function in a script
unless it is both obvious and short. Put code in backticks, as the "Comments"
section of [Coding Standards](../SKILL.md) asks, except for the names listed
under `Globals:`. For example:

```bash
# Delete archives older than `ARCHIVE_RETENTION_DAYS` days.
# Globals:
#   ARCHIVE_NAME_PREFIX
#   ARCHIVE_RETENTION_DAYS
# Arguments:
#   Directory that holds the archives.
# Outputs:
#   Writes each deleted path to stdout.
delete_expired_archives() {
```

## Zsh

Zsh follows the Bash rules, with these differences:

- Write `print -r --` instead of `echo`, and `print -r -u2 --` for stderr,
  because Zsh's `echo` turns backslash sequences in values into special
  characters.
- Store the script name in a constant at the top of the file, as in
  `readonly SCRIPT_NAME="${0:t}"`, because `$0` inside a function is the
  function's name.
- Quote variables as in Bash, even though Zsh doesn't split unquoted variables.
- Arrays start at index `1`.
- Start each function in a sourced file with `emulate -L zsh`.
- Use glob qualifiers instead of `find` for simple cases, and add a comment that
  explains them:

  ```zsh
  # The `N` qualifier gives an empty list when nothing matches, `.` keeps
  # regular files, and `m+<days>` keeps files modified more than <days> ago.
  local -a log_files=("${log_directory}"/**/*.log(N.m+${minimum_age_days}))
  ```

## fish

- Let `fish_indent` format the file. It indents with four spaces.
- Put each function's summary in `--description`, in the imperative and without
  a final period, as fish's own functions do. fish shows it next to the
  function's name when completing commands. Add the `Arguments:`, `Globals:`,
  `Outputs:`, and `Returns:` sections from the "Comments" section in a comment
  above the function when they apply:

  ```fish
  # Arguments:
  #   Directory that holds the archives.
  # Outputs:
  #   Writes each deleted path to stdout.
  function delete_expired_archives --description 'Delete expired archives'
  ```

- Parse options with `argparse`, and let it print its own messages and check
  values with validators, as in `'d/days=!_validate_int --min 0'`.
- Follow each command whose failure matters with `or return 1`, because fish has
  no `set -e`. Don't add it after `string split0`, which returns `1` when its
  input is empty.
- Define constants at the top of the file with `set -g` and names in
  `UPPER_SNAKE_CASE`, as in `set -g DEFAULT_MINIMUM_AGE_DAYS 7`, because
  functions can't see a script's `set -l` variables.
- Leave lists unquoted. Quote a value that must stay one argument, as in
  `error "'$log_directory' is not a directory"`.
- Put the script's code in a `main` function, and end the file with `main $argv`
  and `exit $status`.
- Get the script name from `status basename`.

## Startup Files

The following table shows where each kind of setting goes:

| Settings                                                       | Bash            | Zsh         | fish                                           |
| -------------------------------------------------------------- | --------------- | ----------- | ---------------------------------------------- |
| Environment, such as exported variables and `PATH`             | `.bash_profile` | `.zprofile` | `config.fish`, outside `status is-interactive` |
| Interactive settings, such as aliases, history, and tool hooks | `.bashrc`       | `.zshrc`    | `config.fish`, inside `status is-interactive`  |

Also follow these rules:

- End the `.bash_profile` file by sourcing `.bashrc`, because a Bash login shell
  doesn't read it.
- Start the `.bashrc` file with `[[ $- == *i* ]] || return 0`, because Bash also
  reads it for commands run over SSH. The `.zshrc` file needs no check.
- Leave `.zshenv`, `.zlogin`, `.bash_login`, and `.profile` unused. On macOS,
  `path_helper` moves folders that `.zshenv` adds to `PATH` behind the system
  folders. On Linux, move what the distribution's `.profile` file sets into
  `.bash_profile` and delete `.profile`, because Bash ignores `.profile` after
  `.bash_profile` exists.
- When adding a folder to `PATH`, move it to the front and remove any other copy
  of it, so that nested login shells don't add duplicates. In Zsh, use
  `typeset -U path`. In fish, use `fish_add_path`. In Bash, use a function:

  ```bash
  # Move a directory to the front of `PATH`, removing any other copy of it.
  # Arguments:
  #   Directory to move.
  prepend_to_path() {
    local directory="$1"
    local path=":${PATH}:"
    path="${path//":${directory}:"/:}"
    path="${path#:}"
    PATH="${directory}:${path%:}"
  }
  ```

- Don't use `set -euo pipefail` or `main`, because these files run inside the
  interactive shell. Aliases are allowed in Bash and Zsh. In fish, use `abbr`
  instead.
- Load a tool's documented shell hook only when the tool is installed, as in
  `eval "$(direnv hook bash)"` after `command -v direnv >/dev/null` in Bash and
  Zsh, or `direnv hook fish | source` after `command -q direnv` in fish.
- Start Bash startup files with `# shellcheck shell=bash`.

Commands run as `ssh <host> <command>` don't get the environment in Bash or Zsh.
Give the command's full path, or run it as `bash -lc '<command>'`.

## Tooling

Lint Bash with ShellCheck and format it with shfmt. Zsh has no widely used
linter, so check its syntax with `zsh -n` and format it with shfmt. Check fish
with `fish --no-execute` and format it with `fish_indent`. Follow the steps in
the following sections for each file you change, within the cleanup scope
defined in the "Tooling" section of [Coding Standards](../SKILL.md).

### Bash and Zsh Tooling

1. Check the file. For Bash, run:

   ```sh
   shellcheck -x FILE-PATH
   ```

   For Zsh, run:

   ```sh
   zsh -n FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file. The `-x` option lets
   ShellCheck follow `source` lines.

2. Fix the findings within that scope.
3. Preview the formatting changes:

   ```sh
   shfmt -d FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

4. Format the file:

   ```sh
   shfmt -w FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

shfmt reads its settings only from the `.editorconfig` file, and ignores that
file when you pass any formatting option. When the project has no
`.editorconfig` file, run the following command in step 4 instead:

```sh
shfmt -i 2 -bn -ci -w FILE-PATH
```

Replace `FILE-PATH` with the path to the file. shfmt detects Zsh from the
shebang, the `.zsh` extension, and names such as `.zshrc`.

Suppress a ShellCheck finding with `# shellcheck disable=<rule-code>` on the
line before it, such as `# shellcheck disable=SC2034`.

### fish Tooling

1. Check the file:

   ```sh
   fish --no-execute FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

2. Fix the syntax errors.
3. Preview the formatting changes:

   ```sh
   fish_indent FILE-PATH | diff -u FILE-PATH -
   ```

   Replace `FILE-PATH` with the path to the file.

4. Format the file:

   ```sh
   fish_indent --write FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the file.

# Lua

## Baseline

No published Lua style guide is current enough to adopt, so this reference
states every rule itself. When it leaves a style question unanswered:

- In Neovim files, read the section of Neovim's Lua guide that answers it. Save
  the guide as text with the following command, then read the file:

  ```sh
  nvim --headless -c 'help lua-guide' -c 'w! FILE-PATH' -c 'qa!'
  ```

  Replace `FILE-PATH` with a path for the text file.

- In other Lua files, follow the conventions of the surrounding code and of the
  program that runs the file.

The "Neovim" section applies to files that Neovim loads, such as a configuration
in `~/.config/nvim` or a plugin's `lua/` and `plugin/` folders. The "Pandoc
Filters" section applies to files that Pandoc runs with `--lua-filter`. The
other sections apply to every Lua file, including configurations for other
programs, such as Hammerspoon and WezTerm.

## Formatting

StyLua formats Lua with 2-space indentation, lines up to 100 characters, double
quotes, and parentheses on every call, as in `require("user.options")`. It
doesn't rewrap comments, so wrap them at 100 characters yourself.

## Files

- Name a module, which other code loads with `require`, in `snake_case`, such as
  `daily_note.lua` for `require("user.daily_note")`.
- Name a script that a program runs by its path, such as a Pandoc filter, in
  `kebab-case`, such as `remove-comments.lua`.
- Start every file with a comment that summarizes it.
- Declare every variable and function with `local`. Define a global only when
  the program that runs the file requires one.

A module collects its public functions in a table named `M` and returns it at
the end of the file:

```lua
-- Converts temperatures between units.

local M = {}

--- Returns the temperature in degrees Fahrenheit.
---@param temperature_celsius number
---@return number
function M.fahrenheit_from_celsius(temperature_celsius)
  return temperature_celsius * 9 / 5 + 32
end

return M
```

## Naming

- Write variable, function, and module names in `snake_case`.
- Write LuaCATS class names in `PascalCase` after a namespace, such as
  `user.DailyNoteOptions`. Class names are global across all the code that Lua
  Language Server reads, including Neovim's runtime, and the namespace keeps
  them from colliding.
- In Neovim code, write `bufnr` and `winid` for buffer and window numbers, as
  Neovim's API does. Spell out every other name you choose, such as
  `user_options` rather than `opts`. Outside Neovim, don't use these
  abbreviations.

## Comments and Documentation

Write LuaCATS annotations, which Lua Language Server reads to check types, for
each function that a module returns and for each options table. Start a
function's annotations with a `---` line that summarizes it. Mark optional
fields and parameters with `?`, as in `date_format?`:

```lua
---@class user.DailyNoteOptions
---@field directory string Folder that holds the daily notes.
---@field date_format? string `os.date` format for the filename. Defaults to `"%Y-%m-%d"`.

--- Returns the path of the note for the given time.
---@param time_seconds integer Seconds since the Unix epoch.
---@return string
function M.note_path(time_seconds)
  local filename = os.date(options.date_format, time_seconds) .. ".md"
  return vim.fs.joinpath(vim.fs.normalize(options.directory), filename)
end
```

## Errors

Report failures as follows:

- Return `nil` and a message for a failure that the caller can expect and
  handle, such as a missing file.
- Call `error()` for a failure that the caller can't handle, such as an invalid
  argument.
- In Neovim, call `vim.notify` only for failures of an action that the user
  started directly, such as a command. For Neovim's full guidance, read
  `:help dev-error-patterns`.
- In a Pandoc filter, call `pandoc.log.warn` for a problem that doesn't stop the
  conversion, and `error()` for one that does.

### Messages

Follow the "Messages" section of the skill, and match the messages of the
program that runs the file:

- In Neovim, start a message with a capital letter, as Neovim's own messages do.
  Outside Neovim, start it with a lowercase letter, as Lua's own messages do. In
  both, a message that starts with an identifier keeps its case.
- Put values in single quotes, as Lua's own messages do.
- Start a `vim.notify` message with the module's `require` path and a colon,
  because Neovim doesn't show where a notification came from. Don't start
  `error()` or `pandoc.log.warn` messages with a name, because Lua and Pandoc
  add the file and line to them.

For example:

```lua
vim.notify(("user.daily_note: Can't create '%s'"):format(directory), vim.log.levels.ERROR)

pandoc.log.warn(("`show-comments` must be true or false, got '%s'"):format(text))
```

## Neovim

- In `init.lua`, set the leader keys, then load one module for each area of the
  configuration from `lua/user/`, such as `user.options` and `user.keymaps`.
- Set an option with `vim.o` for a single value, with `vim.opt` to add to or
  remove from a list, and with `vim.opt_local` inside an autocommand. Don't set
  options with `vim.cmd("set ...")`.
- Give every mapping, autocommand, and user command a `desc`, written as a
  capitalized imperative phrase with no period, such as
  `desc = "Clear search highlighting"`.
- Map an Ex command as `<Cmd>...<CR>`, as in `"<Cmd>nohlsearch<CR>"`, and
  anything else to a Lua function.
- Put each module's autocommands in one group with a `kebab-case` name, created
  with `clear = true`, so that loading the module again replaces its
  autocommands instead of adding copies.
- Give a module with options a `setup(user_options)` function that merges them
  with the module's defaults.

For example:

```lua
-- Neovim configuration. Each module under `lua/user/` configures one area.

vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

require("user.options")
require("user.keymaps")
require("user.autocommands")
require("user.daily_note").setup({ directory = "~/Documents/Notes/Daily" })
```

```lua
-- Autocommands that don't belong to a plugin.

local group = vim.api.nvim_create_augroup("user-autocommands", { clear = true })

vim.api.nvim_create_autocmd("FileType", {
  group = group,
  pattern = { "markdown", "text" },
  desc = "Wrap prose at word boundaries",
  callback = function()
    vim.opt_local.wrap = true
    vim.opt_local.linebreak = true
  end,
})
```

```lua
--- Applies the options and creates the `:DailyNote` command.
---@param user_options? user.DailyNoteOptions
function M.setup(user_options)
  options = vim.tbl_extend("force", default_options, user_options or {})
  vim.api.nvim_create_user_command("DailyNote", M.open, { desc = "Open today's note" })
end
```

## Pandoc Filters

- Return the filter table at the end of the file. When one pass must finish
  before the next starts, such as reading the metadata before changing elements,
  return a list of filters, which Pandoc runs in order.
- Return `{}` from a filter function to delete the element, and nothing to keep
  it unchanged.
- Refer to Pandoc's element types by their names in backticks, such as `Div` and
  `Span`, not as "divs" and "spans."

For example:

```lua
-- Removes `Div` and `Span` elements with the class `comment`, unless the
-- document's metadata sets `show-comments: true`.

local are_comments_shown = false

--- Reads the `show-comments` setting from the document's metadata.
---@param metadata pandoc.Meta
local function read_settings(metadata)
  local value = metadata["show-comments"]
  if value == nil then
    return
  end
  if type(value) ~= "boolean" then
    pandoc.log.warn(
      ("`show-comments` must be true or false, got '%s'"):format(pandoc.utils.stringify(value))
    )
    return
  end
  are_comments_shown = value
end

--- Removes the element if it's a comment and comments are hidden.
---@param element pandoc.Div | pandoc.Span
---@return table?
local function remove_comment(element)
  if not are_comments_shown and element.classes:includes("comment") then
    return {}
  end
end

return {
  { Meta = read_settings },
  { Div = remove_comment, Span = remove_comment },
}
```

## Tooling

Format Lua with StyLua, and check it with Lua Language Server, which uses the
LuaCATS annotations to report type errors, undefined globals, and unused
variables. For projects without their own configuration, use the following files
from this skill:

- `assets/.stylua.toml` for every Lua file
- `assets/neovim/.luarc.json` for Neovim configurations and plugins
- `assets/pandoc/.luarc.json` for Pandoc filters

For other Lua files, Lua Language Server needs a configuration file only when
the program that runs them defines globals, such as Hammerspoon's `hs`. List
those names in a `.luarc.json` file, as in
`{ "diagnostics": { "globals": ["hs"] } }`.

For each file you change, follow these steps within the cleanup scope defined in
the "Tooling" section of [`coding-standards`](../SKILL.md):

1. Preview the formatting changes:

   ```sh
   stylua --check FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the Lua file.

2. Format the file:

   ```sh
   stylua FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the Lua file.

3. Check the folder that holds the project's `.luarc.json` file, or the file's
   own folder when there is none:

   ```sh
   lua-language-server --check=FOLDER-PATH --checklevel=Hint --check_format=pretty
   ```

   Replace `FOLDER-PATH` with the path to the folder. Pass a folder, not a file:
   given a single file, Lua Language Server reports no problems. It checks every
   Lua file in the folder, so fix only the findings within the cleanup scope. To
   pass this skill's configuration, add `--configpath=CONFIG-PATH`, and replace
   `CONFIG-PATH` with the path to the `.luarc.json` file.

4. Fix the findings within that scope.

For Neovim files, set `VIMRUNTIME` in step 3, because the `.luarc.json` file
loads Neovim's API from that folder and only Neovim sets the variable. Without
it, every use of `vim` is reported as an undefined global:

```sh
VIMRUNTIME="$(nvim --clean --headless --cmd 'lua io.write(vim.env.VIMRUNTIME)' --cmd q)" \
  lua-language-server --check=FOLDER-PATH --checklevel=Hint --check_format=pretty
```

Replace `FOLDER-PATH` with the path to the folder.

For Pandoc filters, the `.luarc.json` file loads type definitions for Pandoc's
API from Quarto's repository. If the `~/.cache/quarto-cli` folder doesn't exist,
fetch them before step 3:

```sh
git clone --depth 1 --filter=blob:none --sparse https://github.com/quarto-dev/quarto-cli ~/.cache/quarto-cli
git -C ~/.cache/quarto-cli sparse-checkout set src/resources/lua-types/pandoc
```

Suppress a Lua Language Server finding with
`---@diagnostic disable-next-line: <diagnostic-name>` on the line before it,
such as `---@diagnostic disable-next-line: undefined-global`.

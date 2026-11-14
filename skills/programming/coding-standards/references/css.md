# CSS

## Baseline

Follow the general and CSS rules of the
[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html).
The following sections extend it and take precedence where they differ.

These rules apply to `.css` files and to CSS in the `<style>` element of an HTML
file. The guide also covers Sass files, which these rules don't.

## Formatting

Oxfmt formats CSS with 2-space indentation and puts each selector and
declaration on its own line, with a semicolon after every declaration. It writes
strings in single quotes, hexadecimal colors in lowercase, and a 0 before a
decimal point. Stylelint's automatic fixes then add a blank line between rules,
shorten hexadecimal colors, such as `#ffffff` to `#fff`, and remove the unit
after a 0. Leave the layout as the two tools write it.

## Selectors and Names

- Name a class for what the element is or does, not for how it looks. Write
  `.error-message`, not `.red-text` or `.clear`.
- Write class names, custom properties, and `@keyframes` names in `kebab-case`,
  and follow the "Naming" section of [Coding Standards](../SKILL.md). Spell
  words out, as in `.navigation` and `--sidebar-width`. This replaces the
  guide's rule to keep class names as short as possible, as in `.nav`.
- Select elements by class. Don't use ID selectors, and don't qualify a class
  with a type selector, as in `div.error`. Stylelint flags both. An attribute
  selector on a type is fine, as in `input[type='checkbox']`.

## Declarations

- Use a shorthand property only to set every value that it covers, as in
  `margin: 0 auto`. To set one value, use its longhand property, such as
  `margin-top`, because a shorthand resets the values that it doesn't name. This
  replaces the guide's rule to use shorthand properties wherever possible.
  Stylelint flags a set of longhand properties that one shorthand could replace.
- Order declarations alphabetically, as the guide suggests. Stylelint sorts them
  when it fixes a file.
- Don't use `!important`. Use a more specific selector instead. Stylelint flags
  it.
- Don't write vendor prefixes, such as `-webkit-`, for properties and values
  that browsers support without them. Stylelint flags them.
- Write colors in the modern notation that Stylelint requires, as in
  `rgb(0 0 0 / 50%)`, not `rgba(0, 0, 0, 0.5)`.
- Put URLs in `url()` in quotes, as in `url('images/logo.svg')`, and write
  `@import` with `url()`. Stylelint requires both. This replaces the guide's
  rule to leave out the quotes.

## Comments

Write comments as the "Comments" section of [Coding Standards](../SKILL.md)
describes, with `/* */` delimiters. Put a comment that explains a rule on the
line above its selector. When a style sheet has several parts, such as the
styles for each component, start each part with a comment on its own line,
followed by a blank line, as the guide's "Section Comments" rule shows.

For example:

```css
/* Readings table on the station page. */

.reading-table {
  border-collapse: collapse;
  width: 100%;
}

.reading-table-cell {
  border-bottom: 1px solid #ddd;
  padding: 0.25rem 0.5rem;
}

/* Matches the alert colors in the `alerts.ts` file. */
.reading-warning {
  background-color: rgb(255 200 0 / 20%);
}
```

## Tooling

Format CSS with Oxfmt and lint it with Stylelint, using the
`stylelint-config-standard` configuration and the `stylelint-order` plugin. For
projects without their own configuration, use the `assets/.oxfmtrc.json` and
`assets/.stylelintrc.json` files from this skill. The Stylelint configuration
also checks the CSS in `<style>` elements of HTML files through `postcss-html`.

Use the versions that the project pins, such as with `npx oxfmt`, and otherwise
the latest releases, such as with `npx oxfmt@latest`. In a new project, add
`oxfmt`, `stylelint`, `stylelint-config-standard`, `stylelint-order`, and
`postcss-html` as development dependencies at exact versions, because Oxfmt
hasn't reached version 1.0 and its output can change between releases. For each
file you change, follow these steps within the cleanup scope defined in the
"Tooling" section of [Coding Standards](../SKILL.md):

1. Format the file:

   ```sh
   oxfmt FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the CSS or HTML file.

2. Apply automatic lint fixes:

   ```sh
   stylelint --fix FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the CSS or HTML file.

3. Fix the remaining findings within that scope by hand.
4. Format the file again.

Format before linting, because Oxfmt splits a one-line rule onto several lines,
and Stylelint requires a blank line only before rules that span several lines.

When the configuration isn't in the project, pass `-c <configuration-path>` to
Oxfmt with the path to the `assets/.oxfmtrc.json` file. Stylelint loads the
packages that its configuration names from the configuration's folder, so pass
both `--config <configuration-path>` with the path to the
`assets/.stylelintrc.json` file and `--config-basedir <folder>` with a folder
whose `node_modules` folder has the packages, such as the project root. For a
file outside any project, install the packages into a temporary folder:

```sh
npm install --prefix TEMPORARY-FOLDER stylelint stylelint-config-standard stylelint-order postcss-html
```

Replace `TEMPORARY-FOLDER` with the path to a new, empty folder. Then run
`TEMPORARY-FOLDER/node_modules/.bin/stylelint` with
`--config-basedir TEMPORARY-FOLDER`.

Suppress a Stylelint finding with a comment that names the rule and gives the
reason, such as:

```css
/* stylelint-disable-next-line declaration-no-important -- Overrides the map library's inline style. */
```

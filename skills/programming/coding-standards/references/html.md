# HTML

## Baseline

Follow the general and HTML rules of the
[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html).
The following sections extend it and take precedence where they differ.

These rules apply to `.html` files. Write CSS in a `<style>` element as
[CSS](css.md) describes. These rules don't cover templates that a template
language fills in, such as Jinja or Angular templates. For templates, follow the
project's conventions, and run the tools in the "Tooling" section only if the
project does.

## Formatting

Oxfmt formats HTML with 2-space indentation and puts each block, list, and table
element on its own line. When a start tag doesn't fit in 80 characters, it puts
each attribute on its own line. It writes attribute values in double quotes, the
doctype as `<!doctype html>`, and void elements with a closing slash, as in
`<meta charset="utf-8" />`. Leave the layout as Oxfmt writes it, even where the
guide's examples differ. This includes a tag's closing `>` at the start of a
line, which keeps the browser from showing an extra space.

## Document Structure

- Write every optional tag: `<html>` with a `lang` attribute, `<head>`,
  `<body>`, and every end tag, such as `</p>` and `</li>`. This replaces the
  guide's rule to leave out optional tags. Oxfmt adds some end tags that are
  left out, and it can't parse a table whose end tags are left out.
  HTML-validate flags an `<html>` element without `lang`.
- Start the `<head>` element with `<meta charset="utf-8" />`, then
  `<meta name="viewport" content="width=device-width, initial-scale=1" />` and
  the `<title>` element.

## Elements and Attributes

- Use the element made for the purpose. Use `<button>` for an action and `<a>`
  with an `href` attribute for navigation, not a `<div>` element that a script
  makes clickable. Give every `<button>` element a `type` attribute, such as
  `type="button"`, which HTML-validate requires.
- Give every `<img>` element an `alt` attribute that says what the image shows.
  Write `alt=""` for an image that's only decorative. HTML-validate flags a
  missing `alt`.
- Name classes as the "Selectors and Names" section of [CSS](css.md) describes.
- Use an `id` attribute only where something must refer to the element, such as
  the `for` attribute of a `<label>` element, an `aria-describedby` attribute,
  or a link to a section. Include a hyphen in every `id` value, as the guide
  asks, such as `email-input`. HTML-validate checks both class and `id` names.
- Select elements from scripts with `data-*` attributes, such as
  `data-station-id`, as the guide asks, not with classes that also style them.
- Load a script or style sheet from another site, such as a content delivery
  network, from a URL with an exact version, and add `integrity` and
  `crossorigin="anonymous"` attributes. HTML-validate checks for `integrity`.

## Style Sheets and Scripts

Keep CSS in `.css` files and JavaScript in script files, and link them from the
HTML file, as the guide's rule on separation of concerns asks.

A standalone page that's meant to work as one file, such as a report that's
shared as a single HTML file, can have one `<style>` element in its `<head>`
element and one `<script>` element instead.

Don't write `style` attributes or event handler attributes, such as `onclick`,
in any file. Style the element with a class, and add event listeners in the
script. HTML-validate flags `style` attributes, but not event handler
attributes.

## Comments

Write comments as the "Comments" section of [Coding Standards](../SKILL.md)
describes, with `<!-- -->` delimiters. Put a comment on the line above the
element it explains.

For example:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Station Readings</title>
    <link rel="stylesheet" href="readings.css" />
    <script src="readings.js" type="module"></script>
  </head>
  <body>
    <main>
      <h1>Station Readings</h1>
      <!-- `readings.js` fills the table body every 10 minutes. -->
      <table class="reading-table">
        <thead>
          <tr>
            <th scope="col">Station</th>
            <th scope="col">Temperature (°C)</th>
          </tr>
        </thead>
        <tbody data-readings-body></tbody>
      </table>
      <button type="button" data-refresh-button>Refresh</button>
    </main>
  </body>
</html>
```

## Tooling

Format HTML with Oxfmt and lint it with HTML-validate. For projects without
their own configuration, use the `assets/.oxfmtrc.json` and
`assets/.htmlvalidate.json` files from this skill. The HTML-validate
configuration extends the `recommended` and `document` presets. It also accepts
the doctype and void elements as Oxfmt writes them, checks class and `id` names,
and requires `integrity` only for resources from other sites.

Use the versions that the project pins, such as with `npx oxfmt`, and otherwise
the latest releases, such as with `npx oxfmt@latest`. In a new project, add
`oxfmt` and `html-validate` as development dependencies at exact versions,
because Oxfmt hasn't reached version 1.0 and its output can change between
releases. If the project's HTML files have `<style>` elements, also add the
Stylelint packages that the "Tooling" section of [CSS](css.md) lists. For each
file you change, follow these steps within the cleanup scope defined in the
"Tooling" section of [Coding Standards](../SKILL.md):

1. Format the file:

   ```sh
   oxfmt FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the HTML file.

2. Lint the file:

   ```sh
   html-validate FILE-PATH
   ```

   Replace `FILE-PATH` with the path to the HTML file.

3. Fix the findings within that scope by hand.
4. If the file has a `<style>` element, lint its CSS with Stylelint, as the
   "Tooling" section of [CSS](css.md) describes.
5. Format the file again.

Format before linting, because Oxfmt adds the end tags, closing slashes, and
double quotes that HTML-validate checks for.

When the configuration isn't in the project, pass `-c <configuration-path>` to
Oxfmt with the path to the `assets/.oxfmtrc.json` file, and
`--config <configuration-path>` to HTML-validate with the path to the
`assets/.htmlvalidate.json` file. For a file outside any project, run
`npx --yes html-validate@latest`, which needs no other packages.

Suppress an HTML-validate finding with a comment that names the rule and gives
the reason, such as:

```html
<!-- [html-validate-disable-next require-sri: The analytics script changes without a new version, so it can't have a fixed hash.] -->
```

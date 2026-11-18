# /// script
# requires-python = "==3.14.*"
# dependencies = ["markdown-it-py==4.0.0"]
# ///
"""Report possible style violations in a Markdown draft, read-only."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from markdown_it.token import Token
    from markdown_it.tree import SyntaxTreeNode

_RULES = ["list-introduction", "filename-word", "bold-label-colon"]
_FILENAME_PATTERN = re.compile(
    r"[\w-]+(?:\.[\w-]+)*\.(?:md|py|json|ya?ml|toml|txt|csv|html|css|js|ts|lua"
    r"|ipynb|sh|ini|cfg|lock)"
)
_LITERAL_PREFIX = re.compile(r"\b(?:literal|string|pattern|token)\s*$", re.IGNORECASE)
_FILE_SUFFIX = re.compile(r"\s+files?\b")


class Finding(NamedTuple):
    """One candidate for manual review, not a confirmed error.

    Attributes
    ----------
    rule : str
        Name of the rule that the candidate might break, such as
        ``list-introduction``.
    line : int
        One-based source line of the candidate.
    message : str
        What to inspect at that line.
    """

    rule: str
    line: int
    message: str


def findings(source: str) -> list[Finding]:
    """Return style candidates in a Markdown draft.

    Parameters
    ----------
    source : str
        Markdown documentation to inspect.

    Returns
    -------
    list of Finding
        Candidates sorted by line, for manual review.

    Raises
    ------
    RuntimeError
        If the Markdown parser or its dependencies cannot be imported.
    ValueError
        If Markdown draft fences nest more than eight levels deep.
    """
    unique = set(_document_findings(source, line_offset=0, fence_depth=0))
    return sorted(unique, key=lambda item: (item.line, item.rule))


def main() -> int:
    """Report advisory candidates for explicit paths without writing them.

    Returns
    -------
    int
        ``0`` for no candidates, ``1`` for candidates that need review,
        or ``2`` for input, parser, or nesting errors.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    arguments = parser.parse_args()
    documents: list[dict[str, object]] = []
    for path in arguments.paths:
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            print(
                f"{str(path)!r}: expected readable UTF-8 Markdown, got {error!r}",
                file=sys.stderr,
            )
            return 2
        try:
            results = findings(source)
        except (RuntimeError, ValueError) as error:
            print(f"{str(path)!r}: {error}", file=sys.stderr)
            return 2
        documents.append(
            {"path": str(path), "findings": [item._asdict() for item in results]}
        )
    print(
        json.dumps(
            {
                "isCompleteStyleReview": False,
                "scope": _RULES,
                "limitations": [
                    "does not judge sentence completeness or heading relevance",
                    "requires manual review of user-approved exceptions",
                    "checks code-formatted filenames without a slash only",
                    "does not check other writing rules",
                    "supports CommonMark with tables and labeled Markdown draft fences",
                ],
                "documents": documents,
            },
            indent=2,
        )
    )
    return int(any(document["findings"] for document in documents))


def _document_findings(
    source: str, *, line_offset: int, fence_depth: int
) -> list[Finding]:
    """Return candidates in a document and its nested Markdown fences.

    Front matter is blanked rather than removed, so line numbers still
    match the source. Fences labeled ``markdown``, ``md``, or ``gfm``
    are checked as documents, offset to their position in the source.
    """
    if fence_depth > 8:
        raise ValueError(
            f"expected at most 8 nested Markdown draft fences, got {fence_depth}"
        )
    # Import here so help and dependency errors work without the parser.
    try:
        from markdown_it import MarkdownIt
        from markdown_it.tree import SyntaxTreeNode
    except ImportError as error:
        raise RuntimeError(
            f"expected markdown-it-py 4.0.0 and its dependencies, got {error!r}"
        ) from error
    lines = source.splitlines(keepends=True)
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                lines[: index + 1] = ["\n"] * (index + 1)
                break
    root = SyntaxTreeNode(
        MarkdownIt("commonmark").enable("table").parse("".join(lines))
    )
    candidates: list[Finding] = []
    for parent in root.walk():
        if parent.type == "inline" and parent.map and parent.token:
            candidates.extend(
                _inline_findings(parent.token, line_offset + parent.map[0] + 1)
            )
        previous: SyntaxTreeNode | None = None
        for node in parent.children:
            if _is_comment(node):
                continue
            is_list = node.type in {"bullet_list", "ordered_list"}
            if is_list and node.map and not _introduces_list(previous):
                candidates.append(
                    Finding(
                        "list-introduction",
                        line_offset + node.map[0] + 1,
                        "inspect the list for a colon-ended introductory sentence",
                    )
                )
            if node.type == "fence" and node.token and node.map:
                language = node.token.info.strip().split(maxsplit=1)
                if language and language[0].lower() in {"markdown", "md", "gfm"}:
                    candidates.extend(
                        _document_findings(
                            node.token.content,
                            line_offset=line_offset + node.map[0] + 1,
                            fence_depth=fence_depth + 1,
                        )
                    )
            previous = node
    return candidates


def _is_comment(node: SyntaxTreeNode) -> bool:
    if node.type != "html_block" or not node.token:
        return False
    content = node.token.content.strip()
    return content.startswith("<!--") and content.endswith("-->")


def _introduces_list(previous: SyntaxTreeNode | None) -> bool:
    """Return whether a block counts as a list's introduction.

    A heading counts, and so does a paragraph ending in a colon. The
    check can't tell a complete sentence from a fragment.
    """
    if previous is None:
        return False
    if previous.type == "heading":
        return True
    if previous.type != "paragraph":
        return False
    text = previous.children[0].content
    return text.rstrip().endswith(":")


def _inline_findings(inline: Token, first_line: int) -> list[Finding]:
    tokens = inline.children or []
    candidates: list[Finding] = []
    line = first_line
    for index, token in enumerate(tokens):
        if token.type == "code_inline" and _FILENAME_PATTERN.fullmatch(token.content):
            prefix = "".join(item.content for item in tokens[:index])
            suffix = "".join(item.content for item in tokens[index + 1 :])
            if not _LITERAL_PREFIX.search(prefix) and not _FILE_SUFFIX.match(suffix):
                candidates.append(
                    Finding(
                        "filename-word",
                        line,
                        f'inspect whether `{token.content}` needs "file" afterward',
                    )
                )
        is_label_end = (
            token.type == "strong_close"
            and index > 0
            and tokens[index - 1].type in {"text", "code_inline"}
            and tokens[index - 1].content.rstrip().endswith(":")
        )
        if is_label_end:
            candidates.append(
                Finding(
                    "bold-label-colon",
                    line,
                    "inspect the bold label for a colon that belongs outside the bold",
                )
            )
        if token.type in {"softbreak", "hardbreak"}:
            line += 1
    return candidates


if __name__ == "__main__":
    raise SystemExit(main())

# /// script
# requires-python = "==3.14.*"
# ///
"""Report structural candidates without modifying the commit message."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import NamedTuple

_TYPES = {
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
}
_RULES = [
    "header-format",
    "header-length",
    "summary-capitalization",
    "summary-period",
    "section-spacing",
    "line-length",
    "special-footer-format",
    "footer-format",
    "footer-order",
    "footer-block",
    "footer-duplicates",
]
_HEADER_PATTERN = re.compile(
    r"^(?P<type>[a-z]+)(?:\((?P<scope>[^()\r\n]+)\))?!?: (?P<summary>.+)$"
)
_ISSUE_LABELS = ("Closes", "Fixes", "References")
_ATTRIBUTION_LABELS = (
    "Reviewed-by",
    "Tested-by",
    "Reported-by",
    "Co-authored-by",
    "Signed-off-by",
)
_ISSUE_PATTERN = re.compile(r"^(Closes|Fixes|References): #[1-9][0-9]*$")
_ATTRIBUTION_PATTERN = re.compile(
    r"^(Reviewed-by|Tested-by|Reported-by|Co-authored-by|Signed-off-by): "
    r"(?P<name>.+) <(?P<email>[^<>\s]+@[^<>\s]+)>$"
)
_SINGLE_CODE_PATTERN = re.compile(r"^\s*`[^`]+`\s*$")
_SINGLE_URL_PATTERN = re.compile(r"^\s*[A-Za-z][A-Za-z0-9+.-]*://\S+\s*$")


class Finding(NamedTuple):
    """One candidate for manual review, not a confirmed semantic error.

    Attributes
    ----------
    rule : str
        Name of the structural rule that the candidate might break.
    line : int
        One-based source line of the candidate.
    message : str
        What to inspect at that line.
    """

    rule: str
    line: int
    message: str


def findings(source: str) -> list[Finding]:
    """Return structural candidates in a commit message.

    Parameters
    ----------
    source : str
        Complete commit message to inspect.

    Returns
    -------
    list of Finding
        Unique candidates sorted by line and rule.
    """
    lines = source.splitlines()
    candidates: list[Finding] = []
    candidates.extend(_header_findings(lines))
    candidates.extend(_spacing_findings(lines))
    candidates.extend(_line_length_findings(lines))
    candidates.extend(_special_footer_findings(lines))
    candidates.extend(_footer_findings(lines))
    unique = {(item.rule, item.line): item for item in candidates}
    return sorted(unique.values(), key=lambda item: (item.line, item.rule))


def main() -> int:
    """Report structural candidates for explicit message paths.

    Returns
    -------
    int
        ``0`` for no candidates, ``1`` for candidates to review, or
        ``2`` for input errors.
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
                f"{str(path)!r}: expected readable UTF-8 text, got {error!r}",
                file=sys.stderr,
            )
            return 2
        documents.append(
            {
                "path": str(path),
                "findings": [item._asdict() for item in findings(source)],
            }
        )
    print(
        json.dumps(
            {
                "isCompleteCommitMessageReview": False,
                "scope": _RULES,
                "limitations": [
                    "does not verify the change type, scope, or imperative mood",
                    "does not verify claims, issue resolution, or backtick use",
                    "does not verify contributor identity or attribution eligibility",
                    "reports ambiguous capitalization as a manual-review candidate",
                ],
                "documents": documents,
            },
            indent=2,
        )
    )
    return int(any(document["findings"] for document in documents))


def _header_findings(lines: list[str]) -> list[Finding]:
    if not lines:
        return [
            Finding(
                "header-format",
                1,
                "inspect the missing commit-message header",
            )
        ]
    header = lines[0]
    match = _HEADER_PATTERN.fullmatch(header)
    if not match or match.group("type") not in _TYPES:
        return [
            Finding(
                "header-format",
                1,
                "inspect the expected type, optional scope, and summary format",
            )
        ]
    candidates: list[Finding] = []
    if len(header) > 72:
        candidates.append(
            Finding(
                "header-length",
                1,
                f"inspect the {len(header)}-character header for the 72-character limit",
            )
        )
    summary = match.group("summary")
    if summary[0].isupper():
        candidates.append(
            Finding(
                "summary-capitalization",
                1,
                "inspect a capitalized summary for a required identifier or proper name",
            )
        )
    if summary.rstrip().endswith("."):
        candidates.append(
            Finding(
                "summary-period",
                1,
                "remove the trailing period from the summary",
            )
        )
    return candidates


def _spacing_findings(lines: list[str]) -> list[Finding]:
    candidates: list[Finding] = []
    if len(lines) > 1 and lines[1] != "":
        candidates.append(
            Finding(
                "section-spacing",
                2,
                "separate the header from the next section with one blank line",
            )
        )
    for index in range(1, len(lines)):
        if lines[index] == "" and lines[index - 1] == "":
            candidates.append(
                Finding(
                    "section-spacing",
                    index + 1,
                    "remove the extra blank line between sections or paragraphs",
                )
            )
    return candidates


def _line_length_findings(lines: list[str]) -> list[Finding]:
    candidates: list[Finding] = []
    for index, line in enumerate(lines[1:], start=1):
        if len(line) <= 72 or _is_long_line_exempt(line):
            continue
        candidates.append(
            Finding(
                "line-length",
                index + 1,
                f"inspect the {len(line)}-character line for the 72-character limit",
            )
        )
    return candidates


def _is_long_line_exempt(line: str) -> bool:
    return bool(
        _SINGLE_CODE_PATTERN.fullmatch(line)
        or _SINGLE_URL_PATTERN.fullmatch(line)
        or _ATTRIBUTION_PATTERN.fullmatch(line)
    )


def _special_footer_findings(lines: list[str]) -> list[Finding]:
    candidates: list[Finding] = []
    for index, line in enumerate(lines):
        for label in ("BREAKING CHANGE", "DEPRECATED"):
            prefix = f"{label}: "
            if line != label and not line.startswith(f"{label}:"):
                continue
            summary = line.removeprefix(prefix)
            if not line.startswith(prefix) or not summary.strip():
                candidates.append(
                    Finding(
                        "special-footer-format",
                        index + 1,
                        f"use the `{label}: <short-summary>` form",
                    )
                )
            elif summary.endswith("."):
                candidates.append(
                    Finding(
                        "special-footer-format",
                        index + 1,
                        f"remove the trailing period from the `{label}` summary",
                    )
                )
            has_explanation = (
                index + 2 < len(lines)
                and bool(lines[index + 2].strip())
                and not _is_footer_marker(lines[index + 2])
            )
            if index + 1 >= len(lines) or lines[index + 1] != "" or not has_explanation:
                candidates.append(
                    Finding(
                        "special-footer-format",
                        index + 1,
                        f"put the `{label}` explanation after one blank line",
                    )
                )
    return candidates


def _footer_findings(lines: list[str]) -> list[Finding]:
    candidates: list[Finding] = []
    footer_positions: list[int] = []
    issue_labels: list[tuple[int, str]] = []
    coauthor_pairs: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        issue_label = _issue_label(line)
        attribution_match = _ATTRIBUTION_PATTERN.fullmatch(line)
        if issue_label is not None:
            footer_positions.append(index)
            issue_labels.append((index, issue_label))
            if not _ISSUE_PATTERN.fullmatch(line):
                candidates.append(
                    Finding(
                        "footer-format",
                        index + 1,
                        "inspect the issue label and single `#number` reference",
                    )
                )
        elif _starts_with_label(line, _ATTRIBUTION_LABELS):
            footer_positions.append(index)
            if attribution_match is None:
                candidates.append(
                    Finding(
                        "footer-format",
                        index + 1,
                        "inspect the attribution trailer name and email address",
                    )
                )
        if attribution_match and attribution_match.group(1) == "Co-authored-by":
            name = attribution_match.group("name").strip().casefold()
            email = attribution_match.group("email").strip().casefold()
            coauthor_pairs.append((index, f"{name} <{email}>"))

    candidates.extend(_footer_spacing_findings(lines, footer_positions))
    candidates.extend(_footer_order_findings(issue_labels))
    candidates.extend(_footer_block_findings(lines, footer_positions))
    candidates.extend(_footer_duplicate_findings(coauthor_pairs))
    return candidates


def _issue_label(line: str) -> str | None:
    for label in _ISSUE_LABELS:
        if line.startswith(f"{label}:"):
            return label
    return None


def _starts_with_label(line: str, labels: tuple[str, ...]) -> bool:
    return any(line.startswith(f"{label}:") for label in labels)


def _is_footer_marker(line: str) -> bool:
    return bool(
        _issue_label(line)
        or _starts_with_label(line, _ATTRIBUTION_LABELS)
        or line.startswith(("BREAKING CHANGE:", "DEPRECATED:"))
    )


def _footer_spacing_findings(
    lines: list[str], footer_positions: list[int]
) -> list[Finding]:
    if not footer_positions:
        return []
    first = min(footer_positions)
    if first > 0 and lines[first - 1] != "":
        return [
            Finding(
                "section-spacing",
                first + 1,
                "separate the footer block from the preceding section",
            )
        ]
    return []


def _footer_order_findings(issue_labels: list[tuple[int, str]]) -> list[Finding]:
    candidates: list[Finding] = []
    ranks = {label: index for index, label in enumerate(_ISSUE_LABELS)}
    previous_rank = -1
    for position, label in issue_labels:
        rank = ranks[label]
        if rank < previous_rank:
            candidates.append(
                Finding(
                    "footer-order",
                    position + 1,
                    "order issue labels as `Closes`, `Fixes`, then `References`",
                )
            )
        previous_rank = rank
    return candidates


def _footer_block_findings(
    lines: list[str], footer_positions: list[int]
) -> list[Finding]:
    if not footer_positions:
        return []
    candidates: list[Finding] = []
    last_footer = max(footer_positions)
    for index in range(last_footer + 1, len(lines)):
        if lines[index] != "":
            candidates.append(
                Finding(
                    "footer-block",
                    last_footer + 2,
                    "keep issue references and attribution trailers at the end",
                )
            )
            break
    sorted_positions = sorted(footer_positions)
    previous = sorted_positions[0]
    for position in sorted_positions[1:]:
        if position != previous + 1:
            candidates.append(
                Finding(
                    "footer-block",
                    position + 1,
                    "keep issue references and attribution trailers in one consecutive block",
                )
            )
        previous = position
    return candidates


def _footer_duplicate_findings(coauthor_pairs: list[tuple[int, str]]) -> list[Finding]:
    candidates: list[Finding] = []
    seen: set[str] = set()
    for position, pair in coauthor_pairs:
        if pair in seen:
            candidates.append(
                Finding(
                    "footer-duplicates",
                    position + 1,
                    "remove the repeated `Co-authored-by` name and email address pair",
                )
            )
        seen.add(pair)
    return candidates


if __name__ == "__main__":
    raise SystemExit(main())

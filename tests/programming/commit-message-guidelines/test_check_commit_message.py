"""Exercise the commit checker through its command-line interface."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

_REPOSITORY = Path(__file__).resolve().parents[3]
_SCRIPT = (
    _REPOSITORY
    / "skills"
    / "programming"
    / "commit-message-guidelines"
    / "scripts"
    / "check_commit_message.py"
)
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


@pytest.mark.parametrize(
    "source",
    [
        "docs: clarify local setup requirements\n",
        (
            "docs: clarify README setup instructions\n\n"
            "Co-authored-by: Codex <noreply@openai.com>\n"
        ),
        (
            "fix: preserve `0` when applying timeout defaults\n\n"
            "A timeout of `0` was replaced by the default, preventing callers from\n"
            "disabling the timeout. Apply the default only when the value is absent\n"
            "and add regression coverage for `0`.\n\n"
            "Fixes: #26\n"
        ),
        (
            "revert: restore synchronous indexing\n\n"
            "Revert `7e4b9c2` because background indexing allowed searches to\n"
            "return stale results immediately after an update.\n"
        ),
        (
            "feat(api)!: paginate project responses\n\n"
            "Large workspaces could exceed the response size limit when listing\n"
            "projects. Return a bounded page with a cursor for the next request.\n\n"
            "BREAKING CHANGE: `GET /projects` now returns an object\n\n"
            "Read projects from `items` instead of treating the response as an array.\n"
            "To fetch the next page, pass `nextCursor` as the `cursor` query\n"
            "parameter.\n\n"
            "Closes: #12\n"
            "Co-authored-by: Cursor <cursoragent@cursor.com>\n"
        ),
        (
            "feat(auth): accept scoped access tokens\n\n"
            "Existing API keys remain available during the transition.\n\n"
            "DEPRECATED: legacy API keys\n\n"
            "Create a scoped access token in account settings and replace the API\n"
            "key.\n"
        ),
        (
            "feat(search): add an option to clear all filters\n\n"
            "Clearing a complex search required removing each filter individually.\n"
            "Provide one action that resets the filters and refreshes the results.\n\n"
            "Closes: #78\n"
            "Closes: #90\n"
            "References: #57\n"
            "Co-authored-by: Codex <noreply@openai.com>\n"
            "Co-authored-by: Claude <noreply@anthropic.com>\n"
            "Co-authored-by: Cursor <cursoragent@cursor.com>\n"
        ),
        (
            "feat: describe an indivisible reference\n\n"
            + "`"
            + "a" * 80
            + "`\n\n"
            + "https://example.com/"
            + "a" * 80
            + "\n\n"
            + "Co-authored-by: A Very Long Display Name <very.long@example.com>\n"
        ),
    ],
)
def test_accepts_structurally_valid_messages(tmp_path: Path, source: str) -> None:
    message = tmp_path / "message.txt"
    message.write_text(source, encoding="utf-8")

    result = _run_checker(message)

    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    payload = json.loads(result.stdout)
    assert payload["isCompleteCommitMessageReview"] is False
    assert payload["scope"] == _RULES
    assert payload["documents"] == [{"path": str(message), "findings": []}]


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        (
            "update: add search\n",
            [("header-format", 1)],
        ),
        (
            "fix: " + "a" * 68 + "\n",
            [("header-length", 1)],
        ),
        (
            "fix: Preserve a timeout override\n",
            [("summary-capitalization", 1)],
        ),
        (
            "fix: preserve a timeout override.\n",
            [("summary-period", 1)],
        ),
        (
            "fix: preserve defaults\nExplain the change\n",
            [("section-spacing", 2)],
        ),
        (
            "fix: preserve defaults\n\nExplain\n\n\nNext\n",
            [("section-spacing", 5)],
        ),
        (
            "fix: preserve defaults\n\n" + "a" * 73 + "\n",
            [("line-length", 3)],
        ),
        (
            (
                "feat(api)!: change responses\n\n"
                "BREAKING CHANGE: responses now use an object.\n\n"
                "Read `items` instead of using an array.\n"
            ),
            [("special-footer-format", 3)],
        ),
        (
            (
                "feat(auth): deprecate legacy keys\n\n"
                "DEPRECATED: legacy API keys\n"
                "Create a scoped access token.\n"
            ),
            [("special-footer-format", 3)],
        ),
        (
            ("feat(auth): deprecate legacy keys\n\nDEPRECATED: legacy API keys\n"),
            [("special-footer-format", 3)],
        ),
        (
            (
                "feat(api)!: change responses\n\n"
                "BREAKING CHANGE\n\n"
                "Read the migration instructions.\n"
            ),
            [("special-footer-format", 3)],
        ),
        (
            (
                "feat(auth): deprecate legacy keys\n\n"
                "DEPRECATED: \n\n"
                "Create a scoped access token.\n"
            ),
            [("special-footer-format", 3)],
        ),
        (
            (
                "feat(auth): deprecate legacy keys\n\n"
                "DEPRECATED: legacy API keys\n\n"
                "Closes: #1\n"
            ),
            [("special-footer-format", 3)],
        ),
        (
            "fix: preserve defaults\n\nCloses: #1, #2\n",
            [("footer-format", 3)],
        ),
        (
            "fix: preserve defaults\n\nReferences: #9\nCloses: #1\n",
            [("footer-order", 4)],
        ),
        (
            (
                "fix: preserve defaults\n\n"
                "Closes: #1\n\n"
                "Co-authored-by: Codex <noreply@openai.com>\n"
            ),
            [("footer-block", 5)],
        ),
        (
            "fix: preserve defaults\n\nCloses: #1\nExplain the change\n",
            [("footer-block", 4)],
        ),
        (
            ("fix: preserve defaults\nCloses: #1\n"),
            [("section-spacing", 2)],
        ),
        (
            (
                "fix: preserve defaults\n\n"
                "Co-authored-by: Codex <noreply@openai.com>\n"
                "Co-authored-by: Codex <noreply@openai.com>\n"
            ),
            [("footer-duplicates", 4)],
        ),
    ],
)
def test_reports_structural_candidates(
    tmp_path: Path, source: str, expected: list[tuple[str, int]]
) -> None:
    message = tmp_path / "message.txt"
    message.write_text(source, encoding="utf-8")

    result = _run_checker(message)

    assert result.returncode == 1, result.stderr
    payload = json.loads(result.stdout)
    found = [
        (finding["rule"], finding["line"])
        for finding in payload["documents"][0]["findings"]
    ]
    assert found == expected
    assert result.stderr == ""


@pytest.mark.parametrize("content", [None, b"\xff\n"])
def test_input_errors_do_not_report_success(
    tmp_path: Path, content: bytes | None
) -> None:
    message = tmp_path / "message.txt"
    if content is not None:
        message.write_bytes(content)

    result = _run_checker(message)

    assert result.returncode == 2
    assert result.stdout == ""
    assert "readable UTF-8 text" in result.stderr


def test_later_input_error_does_not_emit_partial_success(tmp_path: Path) -> None:
    message = tmp_path / "message.txt"
    message.write_text("fix: preserve defaults\n", encoding="utf-8")

    result = _run_checker(message, tmp_path / "missing.txt")

    assert result.returncode == 2
    assert result.stdout == ""


def test_preserves_input_bytes_and_directory_contents(tmp_path: Path) -> None:
    message = tmp_path / "message.txt"
    source = b"fix: preserve defaults\r\n\r\nFixes: #26\r\n"
    message.write_bytes(source)

    result = _run_checker(message)

    assert result.returncode == 0, result.stderr
    assert message.read_bytes() == source
    assert sorted(path.name for path in tmp_path.iterdir()) == ["message.txt"]


def test_help_lists_message_paths() -> None:
    result = subprocess.run(
        [sys.executable, str(_SCRIPT), "--help"],
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )

    assert result.returncode == 0
    assert "paths" in result.stdout


def test_copied_helper_runs_offline_through_uv(tmp_path: Path) -> None:
    scripts = tmp_path / "installed skill" / "scripts"
    scripts.mkdir(parents=True)
    copied_script = scripts / _SCRIPT.name
    shutil.copyfile(_SCRIPT, copied_script)
    message = tmp_path / "message with spaces.txt"
    message.write_text(
        "fix: preserve defaults\n\nCo-authored-by: Codex <noreply@openai.com>\n",
        encoding="utf-8",
    )
    environment = _launcher_environment()

    result = subprocess.run(
        [
            "uv",
            "run",
            "--offline",
            "--no-project",
            "--no-python-downloads",
            "--python",
            "3.14",
            str(copied_script),
            str(message),
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )

    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["documents"][0]["findings"] == []


def _launcher_environment() -> dict[str, str]:
    environment = dict(os.environ)
    for key in ("VIRTUAL_ENV", "PYTHONPATH", "PYTHONHOME"):
        environment.pop(key, None)
    environment["UV_OFFLINE"] = "true"
    environment["UV_PYTHON_DOWNLOADS"] = "never"
    return environment


def _run_checker(*paths: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(_SCRIPT), *(str(path) for path in paths)],
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )

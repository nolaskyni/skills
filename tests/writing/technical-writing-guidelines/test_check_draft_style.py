"""Exercise the draft-style helper through its command-line interface."""

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
    / "writing"
    / "technical-writing-guidelines"
    / "scripts"
    / "check_draft_style.py"
)
# Saved trial replies live in the ignored plans folder, so replay tests
# skip in a fresh clone.
_EVIDENCE = _REPOSITORY / "plans" / "evals" / "list-introduction-integration-2026-11-17"
_RULES = ["list-introduction", "filename-word", "bold-label-colon"]


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("Text.\n\n- One.\n- Two.\n", [("list-introduction", 3)]),
        ("The evidence follows:\n\n- One.\n- Two.\n", []),
        ("# Evidence\n\n- One.\n- Two.\n", []),
        (
            (
                "# Log\n\n| Date | Activity |\n| --- | --- |\n| 2026-11-16 | Visit |\n\n"
                "- Observed silt.\n- Compared clay.\n"
            ),
            [("list-introduction", 7)],
        ),
        (
            "```markdown\n# Example\n\nText.\n\n- One.\n- Two.\n```\n",
            [("list-introduction", 6)],
        ),
        ("```text\nText.\n\n- One.\n- Two.\n```\n", []),
        ("# Example\n\nThe evidence follows:\n\n<!-- note -->\n\n- One.\n- Two.\n", []),
        ("I left `journal-skill.md` unchanged.\n", [("filename-word", 1)]),
        ("I left the `journal-skill.md` file unchanged.\n", []),
        ("Compare the `a.md` and `b.md` files.\n", [("filename-word", 1)]),
        ("The draft is saved at `scratch/reply.md`.\n", []),
        ("The parser matches the literal `README.md`.\n", []),
        ("Save it with the `.md` extension.\n", []),
        ("Run `uv run check.py`.\n", []),
        ("```sh\ncat journal-skill.md\n```\n", []),
        ("```markdown\n# Example\n\nRead `README.md`.\n```\n", [("filename-word", 4)]),
        ("First line.\nThen open `notes.txt`.\n", [("filename-word", 2)]),
        (
            "The following labels apply:\n\n- **Table:** kept.\n",
            [("bold-label-colon", 3)],
        ),
        ("The following labels apply:\n\n- **Table**: kept.\n", []),
        (
            "**Choices to check:**\n\n- **Date**: kept.\n- **Table**: kept.\n",
            [("bold-label-colon", 1), ("list-introduction", 3)],
        ),
        ("The **important** part is bold.\n", []),
        ("Use `**Fast**: uploads` as the form.\n", []),
    ],
)
def test_reports_expected_candidates(
    tmp_path: Path, source: str, expected: list[tuple[str, int]]
) -> None:
    draft = tmp_path / "draft.md"
    draft.write_text(source, encoding="utf-8")
    result = _run_checker(draft)
    assert result.returncode == int(bool(expected)), result.stderr
    payload = json.loads(result.stdout)
    assert payload["isCompleteStyleReview"] is False
    assert payload["scope"] == _RULES
    found = [
        (item["rule"], item["line"]) for item in payload["documents"][0]["findings"]
    ]
    assert sorted(found, key=lambda item: (item[1], item[0])) == sorted(
        expected, key=lambda item: (item[1], item[0])
    )
    assert result.stderr == ""


@pytest.mark.parametrize("content", [None, b"\xff\n"])
def test_input_errors_do_not_report_success(
    tmp_path: Path, content: bytes | None
) -> None:
    path = tmp_path / "draft.md"
    if content is not None:
        path.write_bytes(content)
    result = _run_checker(path)
    assert result.returncode == 2
    assert result.stdout == ""
    assert "readable UTF-8 Markdown" in result.stderr


def test_later_input_error_does_not_emit_partial_success(tmp_path: Path) -> None:
    draft = tmp_path / "draft.md"
    draft.write_text("# Evidence\n\n- One.\n- Two.\n", encoding="utf-8")
    result = _run_checker(draft, tmp_path / "missing.md")
    assert result.returncode == 2
    assert result.stdout == ""


def test_preserves_input_bytes_and_directory_contents(tmp_path: Path) -> None:
    draft = tmp_path / "draft.md"
    source = b"# Evidence\r\n\r\nLeft `a.md` as is.\r\n\r\n- One.\r\n- Two.\r\n"
    draft.write_bytes(source)
    result = _run_checker(draft)
    assert result.returncode == 1
    assert draft.read_bytes() == source
    assert sorted(path.name for path in tmp_path.iterdir()) == ["draft.md"]


def test_excessive_markdown_nesting_is_an_error(tmp_path: Path) -> None:
    draft = tmp_path / "draft.md"
    source = "# Example\n"
    for length in range(4, 13):
        fence = "`" * length
        source = f"{fence}markdown\n{source}{fence}\n"
    draft.write_text(source, encoding="utf-8")
    result = _run_checker(draft)
    assert result.returncode == 2
    assert result.stdout == ""
    assert "got 9" in result.stderr


def test_missing_parser_is_a_reported_error(tmp_path: Path) -> None:
    draft = tmp_path / "draft.md"
    draft.write_text("# Evidence\n\n- One.\n- Two.\n", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-I", "-S", str(_SCRIPT), str(draft)],
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    assert result.returncode == 2
    assert result.stdout == ""
    assert "markdown-it-py" in result.stderr
    assert "Traceback" not in result.stderr


def test_help_does_not_require_the_parser() -> None:
    result = subprocess.run(
        [sys.executable, "-I", "-S", str(_SCRIPT), "--help"],
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
    draft = tmp_path / "draft with spaces.md"
    draft.write_text("Text.\n\n- **One:** a.\n- Two.\n", encoding="utf-8")
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
            str(draft),
        ],
        cwd=tmp_path,
        env=_launcher_environment(),
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode == 1, result.stderr
    payload = json.loads(result.stdout)
    assert [
        (item["rule"], item["line"]) for item in payload["documents"][0]["findings"]
    ] == [("bold-label-colon", 3), ("list-introduction", 3)]


def test_uncached_dependency_is_not_a_clean_result(tmp_path: Path) -> None:
    draft = tmp_path / "draft.md"
    draft.write_text("# Evidence\n\n- One.\n- Two.\n", encoding="utf-8")
    environment = _launcher_environment()
    environment["UV_CACHE_DIR"] = str(tmp_path / "empty-cache")
    result = subprocess.run(
        [
            "uv",
            "run",
            "--offline",
            "--no-project",
            "--no-python-downloads",
            "--python",
            "3.14",
            str(_SCRIPT),
            str(draft),
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert result.returncode != 0
    assert result.stdout == ""


_BATCHES = ["claude-code", "claude-code-rerun"]


@pytest.mark.parametrize("batch", _BATCHES)
def test_replay_matches_hand_grades(batch: str) -> None:
    trials = _EVIDENCE / batch / "trials"
    if not trials.exists():
        pytest.skip(f"{batch} evidence is not present")
    for trial in sorted(trials.iterdir()):
        result = _run_checker(trial / "final.md")
        rules = {
            item["rule"]
            for item in json.loads(result.stdout)["documents"][0]["findings"]
        }
        # Hand grades: skill replies omit "file" after journal-skill.md.
        if "-skill-" in trial.name:
            assert "filename-word" in rules, trial.name
        # Every guide reply puts a colon inside a bold label (hand-graded).
        if "-guide-" in trial.name:
            assert "bold-label-colon" in rules, trial.name


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

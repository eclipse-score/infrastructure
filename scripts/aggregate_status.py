#!/usr/bin/env python3
"""Aggregate rollup status markers for infrastructure chapter markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

UNKNOWN_STATUS = "⚪"
DEFAULT_STATUS = UNKNOWN_STATUS
STATUS_RANK: dict[str, int] = {
    "🔴": 0,
    "🟠": 1,
    "🟡": 2,
    "🟢": 3,
}
STATUS_BY_RANK = {rank: status for status, rank in STATUS_RANK.items()}
STATUS_MARKERS = UNKNOWN_STATUS + "".join(STATUS_RANK)

CHAPTER_HEADER_RE = re.compile(
    rf"^#\s+(?P<title>.+?)(?:\s+(?P<status>[{re.escape(STATUS_MARKERS)}]))?$",
    re.MULTILINE,
)
SECTION_HEADER_RE = re.compile(
    rf"^##\s+(?P<title>.+?)(?:\s+(?P<status>[{re.escape(STATUS_MARKERS)}]))?$",
    re.MULTILINE,
)
SUBSECTION_HEADER_RE = re.compile(
    rf"^###\s+(?P<title>.+?)(?:\s+(?P<status>[{re.escape(STATUS_MARKERS)}]))?$",
)
TRAILING_STATUS_RE = re.compile(rf"\s+(?:[{re.escape(STATUS_MARKERS)}])$")
NUMBERED_CHAPTER_TITLE_RE = re.compile(r"^\d+\s+")


def clean_title(title: str) -> str:
    """Return a heading title without a trailing status marker."""
    return TRAILING_STATUS_RE.sub("", title).strip()


def is_chapter_document(file_path: Path, content: str) -> bool:
    """Return whether the markdown file is a numbered chapter document."""
    if file_path.name == "index.md":
        return False

    chapter_match = CHAPTER_HEADER_RE.search(content)
    if chapter_match is None:
        return False

    title = clean_title(chapter_match.group("title"))
    return NUMBERED_CHAPTER_TITLE_RE.match(title) is not None


def get_average_status(statuses: list[str]) -> str:
    """Return a rounded average status marker from known markers."""
    scores = [STATUS_RANK[status] for status in statuses if status in STATUS_RANK]
    if not scores:
        return DEFAULT_STATUS
    average_score = sum(scores) / len(scores)
    rounded_score = int(average_score + 0.5)
    return STATUS_BY_RANK[rounded_score]


def get_rollup_status(statuses: list[str]) -> str:
    """Return unknown if a majority is unknown, otherwise a rounded average."""
    if not statuses:
        return DEFAULT_STATUS

    unknown_count = sum(status == UNKNOWN_STATUS for status in statuses)
    if unknown_count / len(statuses) > 0.5:
        return UNKNOWN_STATUS

    return get_average_status(statuses)


def extract_section_statuses(content: str) -> dict[str, str]:
    """Compute section statuses from subsections or from the section marker itself."""
    section_statuses: dict[str, str] = {}
    current_section: str | None = None
    current_section_status = DEFAULT_STATUS
    current_subsection_statuses: list[str] = []

    def flush_current_section() -> None:
        nonlocal current_section, current_section_status, current_subsection_statuses
        if current_section and current_section != "Overview":
            if current_subsection_statuses:
                section_statuses[current_section] = get_rollup_status(current_subsection_statuses)
            else:
                section_statuses[current_section] = current_section_status
        current_section_status = DEFAULT_STATUS
        current_subsection_statuses = []

    for line in content.splitlines():
        if section_match := SECTION_HEADER_RE.match(line):
            flush_current_section()
            current_section = clean_title(section_match.group("title"))
            current_section_status = section_match.group("status") or DEFAULT_STATUS
            continue

        if current_section and (subsection_match := SUBSECTION_HEADER_RE.match(line)):
            status = subsection_match.group("status") or DEFAULT_STATUS
            current_subsection_statuses.append(status)

    flush_current_section()
    return section_statuses


def update_section_headers(content: str, section_statuses: dict[str, str]) -> str:
    """Apply computed section rollups to level-2 headings."""

    def replace_section(match: re.Match[str]) -> str:
        title = clean_title(match.group("title"))
        status = section_statuses.get(title)
        return match.group(0) if status is None else f"## {title} {status}"

    return SECTION_HEADER_RE.sub(replace_section, content)


def update_chapter_status(content: str, section_statuses: dict[str, str]) -> str:
    """Apply the rounded average section status to the chapter heading."""
    if not section_statuses:
        return content

    chapter_status = get_rollup_status(list(section_statuses.values()))

    def replace_chapter(match: re.Match[str]) -> str:
        title = clean_title(match.group("title"))
        return f"# {title} {chapter_status}"

    return CHAPTER_HEADER_RE.sub(replace_chapter, content, count=1)


def process_chapter(file_path: Path) -> bool:
    """Update a single chapter file and report whether it changed."""
    original_content = file_path.read_text(encoding="utf-8")
    if not is_chapter_document(file_path, original_content):
        print(f"  ℹ️  Skipping non-chapter document {file_path.name}")
        return False

    updated_content = original_content
    section_statuses = extract_section_statuses(updated_content)

    if not section_statuses:
        print(f"  ℹ️  No subsection headings found in {file_path.name}")
    else:
        updated_content = update_section_headers(updated_content, section_statuses)
        updated_content = update_chapter_status(updated_content, section_statuses)

    if updated_content == original_content:
        print(f"  ℹ️  No changes needed for {file_path.name}")
        return False

    _ = file_path.write_text(updated_content, encoding="utf-8")
    print(f"  ✅ Updated {file_path.name}")
    return True


def resolve_target_path(target: Path | None) -> Path:
    """Return the file or directory to process."""
    if target is not None:
        return target
    return Path(__file__).resolve().parent.parent / "docs" / "explanation"


def iter_chapter_files(target: Path) -> list[Path]:
    """Return markdown chapter files from a file or directory target."""
    if not target.exists():
        raise FileNotFoundError(f"Target not found: {target}")
    if target.is_file():
        return [target]
    return sorted(path for path in target.glob("*.md") if path.is_file())


def main() -> int:
    """Process chapter files and return a shell-friendly exit code."""
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    target = resolve_target_path(target)

    try:
        chapter_files = iter_chapter_files(target)
    except FileNotFoundError as error:
        print(f"❌ {error}")
        return 1

    if not chapter_files:
        print(f"⚠️  No chapter files found in {target}")
        return 1

    print(f"🔄 Processing {len(chapter_files)} chapter files...\n")

    modified_count = 0
    for file_path in chapter_files:
        modified_count += int(process_chapter(file_path))

    print(f"\n📊 Summary: {modified_count} files modified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

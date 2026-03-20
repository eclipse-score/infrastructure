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
INDEX_STATUS_HEADING = "## Chapter Status"
INDEX_STATUS_START = "<!-- auto-generated chapter status table -->"
INDEX_STATUS_END = "<!-- end of auto-generated chapter status table -->"

OVERVIEW_BLOCK_RE = re.compile(
    r"\n*## Overview\n\n<!-- auto-generated overview table -->.*?<!-- end of auto-generated overview table -->\n*",
    re.DOTALL,
)

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


def clean_title(title: str) -> str:
    """Return a heading title without a trailing status marker."""
    return TRAILING_STATUS_RE.sub("", title).strip()


def remove_overview(content: str) -> str:
    """Remove the auto-generated chapter overview block if present."""
    updated_content = OVERVIEW_BLOCK_RE.sub("\n\n", content, count=1)
    if updated_content == content:
        return content

    updated_content = re.sub(r"\n{3,}", "\n\n", updated_content)
    return f"{updated_content.rstrip()}\n"


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


def extract_chapter_heading(file_path: Path) -> tuple[str, str] | None:
    """Return the chapter title and status from the first level-1 heading."""
    content = file_path.read_text(encoding="utf-8")
    match = CHAPTER_HEADER_RE.search(content)
    if match is None:
        return None
    title = clean_title(match.group("title"))
    status = match.group("status") or DEFAULT_STATUS
    return title, status


def build_index_status_block(chapter_files: list[Path]) -> str:
    """Build the auto-generated chapter status block for the index page."""
    rows = [
        "| Chapter | Status |",
        "| --- | --- |",
    ]

    for file_path in chapter_files:
        heading = extract_chapter_heading(file_path)
        if heading is None:
            continue
        title, status = heading
        rows.append(f"| [{title}](chapters/{file_path.name}) | {status} |")

    return "\n".join(
        [
            INDEX_STATUS_HEADING,
            "",
            INDEX_STATUS_START,
            *rows,
            INDEX_STATUS_END,
        ]
    )


def update_index(chapter_files: list[Path]) -> bool:
    """Update docs/index.md with an auto-generated chapter status table."""
    index_path = Path(__file__).resolve().parent.parent / "docs" / "index.md"
    original_content = index_path.read_text(encoding="utf-8")
    status_block = build_index_status_block(chapter_files)
    block_pattern = re.compile(
        rf"{re.escape(INDEX_STATUS_HEADING)}\n\n{re.escape(INDEX_STATUS_START)}.*?{re.escape(INDEX_STATUS_END)}",
        re.DOTALL,
    )

    if block_pattern.search(original_content):
        updated_content = block_pattern.sub(status_block, original_content, count=1)
    else:
        marker = "## Why here? Why markdown?"
        if marker in original_content:
            updated_content = original_content.replace(marker, f"{status_block}\n\n{marker}", 1)
        else:
            updated_content = f"{original_content.rstrip()}\n\n{status_block}\n"

    if updated_content == original_content:
        print("  ℹ️  No changes needed for index.md")
        return False

    _ = index_path.write_text(updated_content, encoding="utf-8")
    print("  ✅ Updated index.md")
    return True


def process_chapter(file_path: Path) -> bool:
    """Update a single chapter file and report whether it changed."""
    original_content = file_path.read_text(encoding="utf-8")
    updated_content = remove_overview(original_content)
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
    return Path(__file__).resolve().parent.parent / "docs" / "chapters"


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
    all_chapter_files = iter_chapter_files(resolve_target_path(None))

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

    modified_count += int(update_index(all_chapter_files))

    print(f"\n📊 Summary: {modified_count} files modified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

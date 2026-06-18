#!/usr/bin/env python3
"""Generate the overview chapter table from the numbered chapter headings."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,3})\s+(?P<title>.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
STATUS_RE = re.compile(r"\s+([🟢🟡🟠🔴⚪])$")
SECTION_NUMBER_RE = re.compile(r"^(\d+(?:\.\d+)?)\s")
CHAPTER_ROW_RE = re.compile(r"^\| \*\*\[([^\]]+)\]\([^)]+\)\*\* \| [🟢🟡🟠🔴⚪] \| (.+) \|$")
SECTION_ROW_RE = re.compile(r"^\| ↳ \[([^\]]+)\]\([^)]+\) \| [🟢🟡🟠🔴⚪] \| (.+) \|$")

INDEX_MAP_START = "<!-- BEGIN GENERATED CHAPTER MAP -->"
INDEX_MAP_END = "<!-- END GENERATED CHAPTER MAP -->"

# Generic fallback per maturity level. Used only for new sections not yet in index.md.
IMPACT_DEFAULT: dict[str, str] = {
    "🟢": "Working as intended",
    "🟡": "Partially in place — gaps affect reliability",
    "🟠": "Implemented but problematic — active friction",
    "🔴": "Not started — capability entirely absent",
    "⚪": "Not implemented — no foundation in place yet",
}


@dataclass
class Section:
    """Structured representation of a heading and its nested subsections."""

    level: int
    title: str
    source_path: Path
    children: list[Section] = field(default_factory=list)


def repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parent.parent


def chapter_documents(docs_dir: Path) -> list[Path]:
    """Return the numbered chapter markdown files in sorted order."""
    return sorted(path for path in docs_dir.glob("[0-9][0-9]-*.md") if path.is_file())


def plain_title(text: str) -> str:
    """Return a title without markdown link syntax."""
    return " ".join(LINK_RE.sub(r"\1", text).split()).strip()


def clean_title(text: str) -> str:
    """Return a title without markdown links or trailing status marker."""
    return STATUS_RE.sub("", plain_title(text)).strip()


def extract_status(text: str) -> str:
    """Return the trailing status emoji, or ⚪ if none is present."""
    m = STATUS_RE.search(plain_title(text))
    return m.group(1) if m else "⚪"


def section_number(title: str) -> str | None:
    """Return the leading section number from a title, e.g. '1.3' or '7'."""
    m = SECTION_NUMBER_RE.match(clean_title(title))
    return m.group(1) if m else None


def heading_anchor(title: str) -> str:
    """Return the Sphinx/docutils-compatible fragment identifier for a heading."""
    normalized = clean_title(title).lower()
    normalized = re.sub(r"[^0-9a-z]+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized)
    normalized = normalized.strip("-")
    return re.sub(r"^[0-9-]+", "", normalized)


def section_href(section: Section) -> str:
    """Return the relative href for a section node."""
    if section.level == 1:
        return f"{section.source_path.stem}.md"
    return f"{section.source_path.stem}.md#{heading_anchor(section.title)}"


def parse_chapter(path: Path) -> Section:
    """Parse a chapter markdown file into a nested H1/H2 heading tree."""
    sections: list[Section] = []
    in_code_block = False

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```") or line.startswith("~~~"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        match = HEADING_RE.match(line)
        if match is None:
            continue
        level = len(match.group(1))
        if level > 2:
            continue
        sections.append(
            Section(
                level=level,
                title=" ".join(match.group("title").split()),
                source_path=path,
            )
        )

    if not sections:
        raise ValueError(f"No heading structure found in {path}")

    root = sections[0]
    stack = [root]

    for section in sections[1:]:
        while stack and stack[-1].level >= section.level:
            stack.pop()
        if not stack:
            raise ValueError(f"Invalid heading nesting in {path}")
        stack[-1].children.append(section)
        stack.append(section)

    return root


def read_existing_impacts(index_path: Path) -> dict[str, str]:
    """Parse the current table in index.md and return {section_number: impact_text}."""
    impacts: dict[str, str] = {}
    if not index_path.exists():
        return impacts

    in_block = False
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if line.strip() == INDEX_MAP_START:
            in_block = True
            continue
        if line.strip() == INDEX_MAP_END:
            break
        if not in_block:
            continue

        for pattern in (CHAPTER_ROW_RE, SECTION_ROW_RE):
            m = pattern.match(line)
            if m:
                num = section_number(m.group(1))
                if num:
                    impacts[num] = m.group(2).strip()
                break

    return impacts


def resolve_impact(title: str, status: str, existing: dict[str, str]) -> str:
    """Return the impact text for a section, preferring existing over the generic default."""
    num = section_number(title)
    if num and num in existing:
        return existing[num]
    return IMPACT_DEFAULT.get(status, IMPACT_DEFAULT["⚪"])


def render_table(chapters: list[Section], existing_impacts: dict[str, str]) -> str:
    """Render a Markdown capability/maturity/impact table for all chapters and sections."""
    rows = [
        "| Capability | Maturity | Impact |",
        "|---|---|---|",
    ]

    for chapter in chapters:
        title = clean_title(chapter.title)
        href = section_href(chapter)
        status = extract_status(chapter.title)
        impact = resolve_impact(title, status, existing_impacts)
        rows.append(f"| **[{title}]({href})** | {status} | {impact} |")

        for section in chapter.children:
            sec_title = clean_title(section.title)
            sec_href = section_href(section)
            sec_status = extract_status(section.title)
            sec_impact = resolve_impact(sec_title, sec_status, existing_impacts)
            rows.append(f"| ↳ [{sec_title}]({sec_href}) | {sec_status} | {sec_impact} |")

    return "\n".join(rows)


def render_embed(chapters: list[Section], existing_impacts: dict[str, str]) -> str:
    """Return the generated overview-page chapter table markup."""
    return "\n".join(
        [
            INDEX_MAP_START,
            "",
            render_table(chapters, existing_impacts),
            "",
            INDEX_MAP_END,
        ]
    )


def update_index_page(index_path: Path, chapters: list[Section]) -> bool:
    """Replace the generated chapter-table block in the overview page."""
    original = index_path.read_text(encoding="utf-8")
    existing_impacts = read_existing_impacts(index_path)
    pattern = re.compile(
        rf"{re.escape(INDEX_MAP_START)}.*?{re.escape(INDEX_MAP_END)}",
        re.DOTALL,
    )
    replacement = render_embed(chapters, existing_impacts)
    updated, n_replacements = pattern.subn(replacement, original, count=1)
    if n_replacements != 1:
        raise ValueError(f"Could not find generated chapter-map markers in {index_path}")
    if updated == original:
        return False
    index_path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    """Generate the overview chapter table and return a shell-friendly exit code."""
    docs_dir = repo_root() / "docs" / "explanation"
    index_path = docs_dir / "index.md"

    chapters = [parse_chapter(path) for path in chapter_documents(docs_dir)]
    if not chapters:
        print(f"⚠️  No chapter files found in {docs_dir}")
        return 1
    changed = update_index_page(index_path, chapters)
    if changed:
        print(f"  ✅ Updated {index_path}")
    else:
        print(f"  ℹ️  No changes needed for {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

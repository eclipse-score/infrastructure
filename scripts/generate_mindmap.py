#!/usr/bin/env python3
"""Generate the overview chapter map from the numbered chapter headings."""

from __future__ import annotations

import json
import re
import textwrap
from dataclasses import dataclass, field
from itertools import count
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,3})\s+(?P<title>.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
STATUS_RE = re.compile(r"\s+[🟢🟡🟠🔴⚪]$")
CHAPTER_NUMBER_RE = re.compile(r"^(?P<number>\d+)\s+")
INDEX_MAP_START = "<!-- BEGIN GENERATED CHAPTER MAP -->"
INDEX_MAP_END = "<!-- END GENERATED CHAPTER MAP -->"


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


def wrap_label(text: str, width: int) -> str:
    """Return text wrapped with newlines for Mermaid markdown string labels."""
    lines = textwrap.wrap(
        text,
        width=width,
        break_long_words=False,
        break_on_hyphens=True,
    )
    return "\n".join(lines) if lines else text


def display_title(section: Section) -> str:
    """Return a wrapped display label while preserving the original title."""
    if section.level == 1:
        return wrap_label(plain_title(section.title), width=24)
    return wrap_label(plain_title(section.title), width=26)


def heading_anchor(title: str) -> str:
    """Return the Sphinx/docutils-compatible fragment identifier for a heading."""
    normalized = clean_title(title).lower()
    normalized = re.sub(r"[^0-9a-z]+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized)
    normalized = normalized.strip("-")
    return re.sub(r"^[0-9-]+", "", normalized)


def section_href(section: Section) -> str:
    """Return the relative href for a section node."""
    base = f"{section.source_path.stem}/"
    if section.level == 1:
        return base
    return f"{base}#{heading_anchor(section.title)}"


def parse_chapter(path: Path) -> Section:
    """Parse a chapter markdown file into a nested H1/H2 heading tree."""
    sections: list[Section] = []

    for line in path.read_text(encoding="utf-8").splitlines():
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


def mermaid_label(text: str) -> str:
    """Return text safe for a Mermaid quoted node label.

    Input already comes from display_title which calls plain_title,
    so we only need to escape quote characters here.
    """
    return text.replace('"', "'").replace("`", "'")


def emit_section(
    section: Section,
    lines: list[str],
    indent: str,
    node_ids: count,
    links: list[dict[str, object]],
) -> None:
    """Render a section and its H2 children as Mermaid mindmap nodes."""
    node_id = f"node_{next(node_ids):03d}"
    label = mermaid_label(display_title(section))
    if "\n" in label:
        lines.append(f'{indent}{node_id}["`{label}`"]')
    else:
        lines.append(f'{indent}{node_id}["{label}"]')
    links.append(
        {
            "id": node_id,
            "kind": "chapter" if section.level == 1 else "section",
            "href": section_href(section),
            "title": clean_title(section.title),
            "match_texts": [plain_title(section.title), clean_title(section.title)],
        }
    )

    for child in section.children:
        emit_section(child, lines, f"{indent}  ", node_ids, links)


def render_mindmap(chapters: list[Section]) -> tuple[str, list[dict[str, object]]]:
    """Render a Mermaid mindmap plus its link metadata."""
    node_ids = count(1)
    links: list[dict[str, object]] = []
    lines = [
        "mindmap",
        "  root((S-CORE Infrastructure))",
    ]

    for chapter in chapters:
        emit_section(chapter, lines, "    ", node_ids, links)

    return "\n".join(lines), links


def render_embed(chapters: list[Section]) -> str:
    """Return the generated overview-page chapter map markup."""
    diagram, links = render_mindmap(chapters)
    link_data = json.dumps(links, ensure_ascii=False, indent=2)
    return "\n".join(
        [
            INDEX_MAP_START,
            '<p class="chapter-map-note">This chapter map is generated from the `#` and `##` headings in the numbered chapter files. Click any chapter or section box to open it.</p>',
            "",
            "```{mermaid}",
            diagram,
            "```",
            '<script type="application/json" class="chapter-map-links-data">',
            link_data,
            "</script>",
            INDEX_MAP_END,
        ]
    )


def update_index_page(index_path: Path, chapters: list[Section]) -> bool:
    """Replace the generated chapter-map block in the overview page."""
    original = index_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(INDEX_MAP_START)}.*?{re.escape(INDEX_MAP_END)}",
        re.DOTALL,
    )
    replacement = render_embed(chapters)
    updated, n_replacements = pattern.subn(replacement, original, count=1)
    if n_replacements != 1:
        raise ValueError(f"Could not find generated chapter-map markers in {index_path}")
    if updated == original:
        return False
    index_path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    """Generate the overview chapter map and return a shell-friendly exit code."""
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

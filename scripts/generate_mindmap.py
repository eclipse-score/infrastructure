#!/usr/bin/env python3
"""Generate a Mermaid mindmap page from the numbered documentation chapters."""

from __future__ import annotations

from dataclasses import dataclass, field
import html
from itertools import count
import json
from pathlib import Path
import re

HEADING_RE = re.compile(r"^(#{1,3})\s+(?P<title>.+?)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
CHAPTER_TITLE_RE = re.compile(r"^(?P<number>\d+)\s+")
STATUS_RE = re.compile(r"\s+[🟢🟡🟠🔴⚪]$")


@dataclass
class Section:
    """Structured representation of a heading and its nested subsections."""

    level: int
    title: str
    source_path: Path
    children: list["Section"] = field(default_factory=list)


def repo_root() -> Path:
    """Return the repository root."""
    return Path(__file__).resolve().parent.parent


def chapter_documents(docs_dir: Path) -> list[Path]:
    """Return the numbered chapter markdown files in sorted order."""
    return sorted(path for path in docs_dir.glob("[0-9][0-9]-*.md") if path.is_file())


def clean_title(text: str) -> str:
    """Return a title without markdown links or trailing status markers."""
    plain = LINK_RE.sub(r"\1", text)
    plain = STATUS_RE.sub("", plain)
    return " ".join(plain.split()).strip()


def heading_anchor(title: str) -> str:
    """Return the MkDocs-compatible fragment identifier for a heading."""
    normalized = clean_title(title).lower().replace(".", "")
    normalized = re.sub(r"[^0-9a-z]+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized)
    return normalized.strip("-")


def page_href(source_path: Path) -> str:
    """Return the relative href from the mindmap page to a chapter page."""
    return f"../{source_path.stem}/"


def section_href(section: Section) -> str:
    """Return the relative href for a section node."""
    href = page_href(section.source_path)
    if section.level == 1:
        return href
    return f"{href}#{heading_anchor(section.title)}"


def parse_chapter(path: Path) -> Section:
    """Parse a chapter markdown file into a nested heading tree."""
    sections: list[Section] = []

    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if match is None:
            continue
        sections.append(
            Section(
                level=len(match.group(1)),
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


def chapter_number(section: Section) -> int:
    """Return the leading chapter number from a top-level chapter title."""
    match = CHAPTER_TITLE_RE.match(section.title)
    if match is None:
        raise ValueError(f"Chapter title does not start with a number: {section.title}")
    return int(match.group("number"))


def mermaid_label(text: str) -> str:
    """Return text safe for a Mermaid quoted node label."""
    plain = LINK_RE.sub(r"\1", text)
    return plain.replace('"', "'")


def emit_leaf(lines: list[str], indent: str, node_id: str, label: str) -> None:
    """Append a simple quoted Mermaid node."""
    lines.append(f'{indent}{node_id}["{mermaid_label(label)}"]')


def emit_section(
    section: Section,
    lines: list[str],
    indent: str,
    node_ids: count,
    node_links: list[dict[str, str]],
) -> None:
    """Render a section and its nested children as Mermaid mindmap nodes."""
    section_id = f"node_{next(node_ids):03d}"
    emit_leaf(lines, indent, section_id, section.title)
    node_links.append(
        {
            "id": section_id,
            "label": section.title,
            "ariaLabel": clean_title(section.title),
            "href": section_href(section),
        }
    )

    child_indent = f"{indent}  "

    for child in section.children:
        emit_section(child, lines, child_indent, node_ids, node_links)


def render_mindmap(chapters: list[Section]) -> tuple[str, list[dict[str, str]]]:
    """Render the complete Mermaid mindmap and collect clickable targets."""
    flow_chapters = [chapter for chapter in chapters if chapter_number(chapter) <= 8]
    support_chapters = [chapter for chapter in chapters if chapter_number(chapter) >= 9]
    node_ids = count(1)
    node_links: list[dict[str, str]] = []

    lines = [
        "mindmap",
        '  root((S-CORE Infrastructure))',
        '    flow["Engineering Flow"]',
    ]

    for chapter in flow_chapters:
        emit_section(chapter, lines, "      ", node_ids, node_links)

    lines.append('    support["Supporting Layers"]')
    for chapter in support_chapters:
        emit_section(chapter, lines, "      ", node_ids, node_links)

    lines.extend(
        [
            '    legend["Status Legend"]',
            '      status_green["🟢 Implemented and effective"]',
            '      status_yellow["🟡 Partially implemented / needs improvement"]',
            '      status_orange["🟠 Implemented but problematic or insufficient"]',
            '      status_red["🔴 Not started"]',
            '      status_unknown["⚪ Unknown / not yet assessed"]',
        ]
    )

    return "\n".join(lines), node_links


def render_page(chapters: list[Section]) -> str:
    """Return the markdown page that hosts the Mermaid mindmap."""
    diagram_text, node_links = render_mindmap(chapters)
    diagram = html.escape(diagram_text)
    links_json = json.dumps(node_links, ensure_ascii=False, indent=2)

    return "\n".join(
        [
            "<!-- Generated by scripts/generate_mindmap.py. Do not edit manually. -->",
            "",
            "# Infrastructure Mindmap",
            "",
            "This page turns the numbered infrastructure chapters into one large Mermaid mindmap.",
            "",
            "It is generated straight from the `#`, `##`, and `###` headings in the numbered chapter files.",
            "Run `python3 scripts/generate_mindmap.py` after changing the chapter structure.",
            "",
            '<p class="mindmap-note">Click a chapter or section box to open it. Use the controls to zoom, and drag the resize handle if you want a taller canvas.</p>',
            "",
            '<div class="mindmap-toolbar" role="toolbar" aria-label="Mindmap controls">',
            '  <button type="button" class="mindmap-button" data-zoom-action="out" aria-label="Zoom out">-</button>',
            '  <button type="button" class="mindmap-button" data-zoom-action="reset">Reset</button>',
            '  <button type="button" class="mindmap-button" data-zoom-action="in" aria-label="Zoom in">+</button>',
            '  <button type="button" class="mindmap-button" data-zoom-action="fit">Fit</button>',
            '  <span class="mindmap-scale" aria-live="polite">120%</span>',
            "</div>",
            "",
            '<div class="mindmap-shell" data-default-scale="1.2">',
            '<div class="mindmap-frame">',
            '<div class="mermaid">',
            diagram,
            "</div>",
            "</div>",
            "</div>",
            "",
            '<script type="application/json" id="mindmap-links">',
            links_json,
            "</script>",
            "",
        ]
    )


def main() -> int:
    """Generate the docs mindmap page and return a shell-friendly exit code."""
    docs_dir = repo_root() / "docs"
    output_path = docs_dir / "mindmap.md"

    chapters = [parse_chapter(path) for path in chapter_documents(docs_dir)]
    output_path.write_text(render_page(chapters), encoding="utf-8")
    print(f"Updated {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

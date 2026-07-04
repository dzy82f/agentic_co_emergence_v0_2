from __future__ import annotations

import re
from pathlib import Path

from agentic_co_emergence.models.perspective import Perspective, PerspectivePack


QUESTION_RE = re.compile(r"^\*\*Question:\*\*\s*(.+?)\s*$")
CREATED_RE = re.compile(r"^\*\*Created:\*\*\s*(.+?)\s*$")
AGENT_RE = re.compile(r"^###\s+(.+?)\s*$")


def load_perspective_pack(path: str | Path) -> PerspectivePack:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Perspective pack not found: {path}")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    question: str | None = None
    created: str | None = None
    perspectives: list[Perspective] = []

    current_agent: str | None = None
    current_lines: list[str] = []

    def flush_current() -> None:
        nonlocal current_agent, current_lines

        if current_agent is None:
            return

        body = "\n".join(current_lines).strip()
        perspectives.append(
            Perspective(
                agent_name=current_agent,
                text=body,
            )
        )

        current_agent = None
        current_lines = []

    for line in lines:
        question_match = QUESTION_RE.match(line)
        if question_match:
            question = question_match.group(1).strip()
            continue

        created_match = CREATED_RE.match(line)
        if created_match:
            created = created_match.group(1).strip()
            continue

        agent_match = AGENT_RE.match(line)
        if agent_match:
            flush_current()
            current_agent = agent_match.group(1).strip()
            current_lines = []
            continue

        if current_agent is not None:
            current_lines.append(line)

    flush_current()

    if question is None:
        raise ValueError(f"Perspective pack missing question: {path}")

    return PerspectivePack(
        question=question,
        created=created,
        perspectives=tuple(perspectives),
    )
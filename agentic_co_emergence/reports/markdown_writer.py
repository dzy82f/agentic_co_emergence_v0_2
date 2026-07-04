from __future__ import annotations

from agentic_co_emergence.models.discussion_state import DiscussionState


def build_synthesis_markdown(state: DiscussionState) -> str:
    lines: list[str] = []

    lines.append("# Collective Understanding")
    lines.append("")
    lines.append(f"**Question:** {state.perspective_pack.question}")
    lines.append("")
    lines.append("## Contributions")
    lines.append("")

    for contribution in state.transcript:
        lines.append(f"### {contribution.speaker}")
        lines.append("")
        lines.append(contribution.text)
        lines.append("")

    return "\n".join(lines).strip() + "\n"
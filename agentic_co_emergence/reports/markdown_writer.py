from __future__ import annotations

from agentic_co_emergence.models.discussion_state import DiscussionState


def build_synthesis_markdown(state: DiscussionState) -> str:
    lines: list[str] = []

    lines.append("# Collective Understanding")
    lines.append("")

    if state.perspective_pack is not None:
        lines.append(f"**Question:** {state.perspective_pack.question}")
    else:
        lines.append(f"**Question:** {state.question}")

    lines.append("")
    lines.append("## Contributions")
    lines.append("")

    for contribution in state.transcript:
        if isinstance(contribution, dict):
            speaker = contribution["agent_name"]
            text = contribution["contribution"]
            response_to = contribution.get("response_to")
        else:
            speaker = contribution.speaker
            text = contribution.text
            response_to = getattr(contribution, "response_to", None)

        lines.append(f"### {speaker}")
        lines.append("")

        if response_to:
            if isinstance(response_to, dict):
                target_name = response_to["agent_name"]
                relation = response_to["relation"]
            else:
                target_name = response_to.agent_name
                relation = response_to.relation

            lines.append(f"**Responding to:** {target_name} ({relation})")
            lines.append("")

        lines.append(text)
        lines.append("")

    return "\n".join(lines).strip() + "\n"
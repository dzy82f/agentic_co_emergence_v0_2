from __future__ import annotations

from typing import Any

from agentic_co_emergence.agent_reflection import build_agent_reflection


def build_reflection_round(
    *,
    state: Any,
    consensus: dict[str, object],
) -> list[dict[str, object]]:
    shared_mechanisms = consensus.get("shared_mechanisms", [])

    reflections: list[dict[str, object]] = []

    for record in state.transcript:
        agent_name = record.get("agent_name", "")
        contribution = record.get("contribution", "")

        reflections.append(
            build_agent_reflection(
                agent_name=agent_name,
                initial_nominee="their original nominee",
                initial_reason=contribution,
                shared_mechanisms=shared_mechanisms,
            )
        )

    return reflections
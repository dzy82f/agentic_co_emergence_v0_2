from __future__ import annotations

from typing import Any


def choose_dialogue_relationship(
    *,
    state: Any,
    responding_agent_name: str,
) -> dict[str, str]:
    for record in reversed(state.transcript):
        agent_name = record.get("agent_name")

        if agent_name != responding_agent_name:
            return {
                "responds_to": agent_name,
                "stance": "extend",
            }

    return {
        "responds_to": "",
        "stance": "extend",
    }
from __future__ import annotations

from typing import Any


STANCE_SEQUENCE = [
    "extend",
    "question",
    "disagree",
    "support",
    "synthesise",
]


def choose_dialogue_relationship(
    *,
    state: Any,
    responding_agent_name: str,
) -> dict[str, str]:
    previous_contributions = [
        record
        for record in state.transcript
        if record.get("agent_name") != responding_agent_name
    ]

    if not previous_contributions:
        return {
            "responds_to": "",
            "stance": STANCE_SEQUENCE[0],
        }

    target = previous_contributions[-1]
    stance = STANCE_SEQUENCE[(len(state.transcript) - 1) % len(STANCE_SEQUENCE)]

    return {
        "responds_to": target["agent_name"],
        "stance": stance,
    }
from __future__ import annotations


def build_reflection_grounded_consensus(
    reflections: list[dict[str, object]],
) -> dict[str, object]:
    agents_refined: list[str] = []
    agents_unchanged: list[str] = []

    for reflection in reflections:
        agent_name = str(reflection.get("agent_name", ""))

        position_delta = reflection.get("position_delta", {})
        changed = (
            isinstance(position_delta, dict)
            and position_delta.get("changed") is True
        )

        if changed:
            agents_refined.append(agent_name)
        else:
            agents_unchanged.append(agent_name)

    refined_count = len(agents_refined)
    unchanged_count = len(agents_unchanged)

    return {
        "kind": "reflection_grounded_consensus",
        "agents_refined": agents_refined,
        "agents_unchanged": agents_unchanged,
        "conclusion": (
            "The group consensus is partially grounded in agent reflection: "
            f"{refined_count} agent refined their position, while "
            f"{unchanged_count} agent remained unchanged."
        ),
    }
from __future__ import annotations


def build_agent_reflection(
    *,
    agent_name: str,
    initial_nominee: str,
    initial_reason: str,
    shared_mechanisms: list[str],
) -> dict[str, object]:
    if "canonical misfit" in shared_mechanisms:
        final_reason = (
            f"{initial_nominee} remains my nominee, but I now understand "
            "her underrating as an example of canonical misfit."
        )

        return {
            "agent_name": agent_name,
            "reflection_kind": "refine",
            "initial_nominee": initial_nominee,
            "final_nominee": initial_nominee,
            "position_delta": {
                "changed": True,
                "from": initial_reason,
                "to": final_reason,
                "reason": "The group consensus distinguished hidden influence from canonical misfit.",
            },
        }

    return {
        "agent_name": agent_name,
        "reflection_kind": "unchanged",
        "initial_nominee": initial_nominee,
        "final_nominee": initial_nominee,
        "position_delta": {
            "changed": False,
            "from": initial_reason,
            "to": initial_reason,
            "reason": "No shared mechanism required a revision of the initial position.",
        },
    }
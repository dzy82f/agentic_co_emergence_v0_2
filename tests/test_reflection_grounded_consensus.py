from agentic_co_emergence.reflection_grounded_consensus import (
    build_reflection_grounded_consensus,
)


def test_reflection_grounded_consensus_uses_position_deltas():
    reflections = [
        {
            "agent_name": "Ada",
            "reflection_kind": "refine",
            "position_delta": {
                "changed": True,
                "reason": "The group consensus distinguished hidden influence from canonical misfit.",
            },
        },
        {
            "agent_name": "Harry",
            "reflection_kind": "unchanged",
            "position_delta": {
                "changed": False,
                "reason": "The discussion did not alter the original position.",
            },
        },
    ]

    consensus = build_reflection_grounded_consensus(reflections)

    assert consensus["kind"] == "reflection_grounded_consensus"
    assert consensus["agents_refined"] == ["Ada"]
    assert consensus["agents_unchanged"] == ["Harry"]
    assert consensus["conclusion"] == (
        "The group consensus is partially grounded in agent reflection: "
        "1 agent refined their position, while 1 agent remained unchanged."
    )
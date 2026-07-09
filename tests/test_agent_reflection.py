from agentic_co_emergence.agent_reflection import build_agent_reflection


def test_agent_reflection_records_refined_position():
    reflection = build_agent_reflection(
        agent_name="Aletheia",
        initial_nominee="Simone Weil",
        initial_reason="She is misread as a mystic rather than a rigorous philosopher of attention.",
        shared_mechanisms=[
            "hidden influence",
            "canonical misfit",
        ],
    )

    assert reflection == {
        "agent_name": "Aletheia",
        "reflection_kind": "refine",
        "initial_nominee": "Simone Weil",
        "final_nominee": "Simone Weil",
        "position_delta": {
            "changed": True,
            "from": "She is misread as a mystic rather than a rigorous philosopher of attention.",
            "to": "Simone Weil remains my nominee, but I now understand her underrating as an example of canonical misfit.",
            "reason": "The group consensus distinguished hidden influence from canonical misfit.",
        },
    }
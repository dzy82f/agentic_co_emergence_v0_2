from agentic_co_emergence.reflection_round import build_reflection_round
from agentic_co_emergence.models.discussion_state import DiscussionState


def test_reflection_round_returns_reflections_for_each_agent():
    state = DiscussionState(
        perspective_pack={},
        agent_states={},
        transcript=[
            {
                "agent_name": "Ada",
                "contribution": "Peirce is underrated because his influence is hidden.",
            },
            {
                "agent_name": "Aletheia",
                "contribution": "Weil is underrated because she is hard to place inside the canon.",
            },
        ],
    )

    consensus = {
        "kind": "group_consensus",
        "shared_mechanisms": [
            "hidden influence",
            "canonical misfit",
        ],
        "conclusion": "The group converged on two mechanisms of underrating.",
    }

    reflections = build_reflection_round(
        state=state,
        consensus=consensus,
    )

    assert len(reflections) == 2
    assert reflections[0]["agent_name"] == "Ada"
    assert reflections[1]["agent_name"] == "Aletheia"

    for reflection in reflections:
        assert "position_delta" in reflection
        assert reflection["position_delta"]["changed"] is True
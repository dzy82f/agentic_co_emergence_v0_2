from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


def test_agent_contribution_records_dialogue_relationship_metadata():
    state = DiscussionState(
        perspective_pack={},
        agent_states={},
    )
    engine = DiscussionTransitionEngine(state)

    event = DiscussionEvent(
        kind="agent_contribution",
        payload={
            "agent_name": "Tenzing",
            "contribution": "I would extend Ada's point by asking what changes if inquiry is communal.",
            "responds_to": "Ada",
            "stance": "extend",
        },
    )

    updated = engine.step(event)

    assert len(updated.transcript) == 1
    assert updated.transcript[0]["agent_name"] == "Tenzing"
    assert updated.transcript[0]["responds_to"] == "Ada"
    assert updated.transcript[0]["stance"] == "extend"
    assert "extend Ada" in updated.transcript[0]["contribution"]
from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


def test_transition_engine_owns_discussion_state():
    state = DiscussionState(
        perspective_pack={},
        agent_states=(),
    )

    engine = DiscussionTransitionEngine(state=state)

    assert engine.current_state() is state


def test_transition_engine_accepts_noop_event():
    state = DiscussionState(
        perspective_pack={},
        agent_states=(),
    )

    engine = DiscussionTransitionEngine(state=state)

    result = engine.step(DiscussionEvent(kind="noop", payload={}))

    assert result is state
    assert engine.current_state() is state


def test_agent_contribution_event_creates_new_state():
    state = DiscussionState(
        perspective_pack={},
        agent_states=(),
    )

    engine = DiscussionTransitionEngine(state=state)

    new_state = engine.step(
        DiscussionEvent(
            kind="agent_contribution",
            payload={
                "agent_name": "Tenzing",
                "contribution": "This is the first contribution.",
            },
        )
    )

    assert new_state is not state
    assert new_state.contribution_count == 1
    assert new_state.transcript == [
        {
            "agent_name": "Tenzing",
            "contribution": "This is the first contribution.",
        }
    ]

    assert state.contribution_count == 0
    assert state.transcript == []
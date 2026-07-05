from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.understanding import (
    UnderstandingDelta,
    build_understanding_delta,
)


def test_understanding_delta_defaults():
    """
    Milestone 0.3

    A newly created UnderstandingDelta should represent
    'no identified change'.
    """

    delta = UnderstandingDelta()

    assert delta.new_claims == []
    assert delta.new_questions == []
    assert delta.new_tensions == []
    assert delta.summary == ""


def test_understanding_delta_identifies_new_transcript_items_as_candidate_claims():
    """
    Milestone 0.3

    Given two immutable DiscussionStates, newly added transcript items
    should be represented as candidate new claims.
    """

    before = DiscussionState(
        perspective_pack=None,
        agent_states=(),
        transcript=[],
    )

    after = DiscussionState(
        perspective_pack=None,
        agent_states=(),
        transcript=["Tenzing: Understanding has changed."],
    )

    delta = build_understanding_delta(before, after)

    assert delta.new_claims == ["Tenzing: Understanding has changed."]
    assert delta.new_questions == []
    assert delta.new_tensions == []
    assert delta.summary == "1 new claim(s) identified."
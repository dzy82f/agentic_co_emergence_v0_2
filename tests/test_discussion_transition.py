from agentic_co_emergence.discussion_transition import DiscussionTransition
from agentic_co_emergence.understanding import UnderstandingDelta


def test_discussion_transition_records_state_change_event():
    delta = UnderstandingDelta(
        new_claims=[
            "DiscussionTransition is the atomic state-change event."
        ],
        new_questions=[
            "What validates a transition?"
        ],
        new_tensions=[],
        summary=(
            "A DiscussionTransition records how one immutable "
            "DiscussionState becomes the next."
        ),
    )

    transition = DiscussionTransition(
        transition_id="t-001",
        from_state_id="state-001",
        to_state_id="state-002",
        speaker="Tenzing",
        contribution="A transition is the atomic state-change event.",
        understanding_delta=delta,
        accepted=True,
        reason=None,
    )

    assert transition.transition_id == "t-001"
    assert transition.from_state_id == "state-001"
    assert transition.to_state_id == "state-002"
    assert transition.speaker == "Tenzing"
    assert transition.accepted is True
    assert transition.reason is None
    assert (
        transition.understanding_delta.summary
        == "A DiscussionTransition records how one immutable "
           "DiscussionState becomes the next."
    )
    assert (
        "DiscussionTransition"
        in transition.understanding_delta.new_claims[0]
    )
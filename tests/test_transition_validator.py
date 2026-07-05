from agentic_co_emergence.discussion_transition import DiscussionTransition
from agentic_co_emergence.transition_validator import validate_transition
from agentic_co_emergence.understanding import UnderstandingDelta


def make_delta() -> UnderstandingDelta:
    return UnderstandingDelta(
        new_claims=["A transition has occurred."],
        new_questions=[],
        new_tensions=[],
        summary="The discussion moved from one state to another.",
    )


def make_transition(**overrides) -> DiscussionTransition:
    values = {
        "transition_id": "t-001",
        "from_state_id": "state-001",
        "to_state_id": "state-002",
        "speaker": "Tenzing",
        "contribution": "This contribution advances the discussion.",
        "understanding_delta": make_delta(),
        "accepted": True,
        "reason": None,
    }
    values.update(overrides)
    return DiscussionTransition(**values)


def test_valid_transition_is_accepted():
    transition = make_transition()

    result = validate_transition(transition)

    assert result.accepted is True
    assert result.reason is None


def test_transition_requires_transition_id():
    transition = make_transition(transition_id="")

    result = validate_transition(transition)

    assert result.accepted is False
    assert result.reason == "transition_id is required"


def test_transition_requires_from_state_id():
    transition = make_transition(from_state_id="")

    result = validate_transition(transition)

    assert result.accepted is False
    assert result.reason == "from_state_id is required"


def test_transition_requires_to_state_id():
    transition = make_transition(to_state_id="")

    result = validate_transition(transition)

    assert result.accepted is False
    assert result.reason == "to_state_id is required"


def test_transition_must_move_to_a_new_state():
    transition = make_transition(
        from_state_id="state-001",
        to_state_id="state-001",
    )

    result = validate_transition(transition)

    assert result.accepted is False
    assert result.reason == "from_state_id and to_state_id must differ"


def test_transition_requires_speaker():
    transition = make_transition(speaker="")

    result = validate_transition(transition)

    assert result.accepted is False
    assert result.reason == "speaker is required"


def test_transition_requires_contribution():
    transition = make_transition(contribution="")

    result = validate_transition(transition)

    assert result.accepted is False
    assert result.reason == "contribution is required"
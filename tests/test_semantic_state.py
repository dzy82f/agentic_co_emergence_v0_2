from agentic_co_emergence.models.semantic_state import (
    SemanticDelta,
    UnderstandingState,
    apply_delta,
)


def test_introduce_concept_delta_updates_understanding_state():
    state = UnderstandingState()

    delta = SemanticDelta(
        delta_type="introduce_concept",
        content="semantic delta",
    )

    updated = apply_delta(state, delta)

    assert "semantic delta" in updated.concepts


def test_link_concepts_delta_records_relation():
    state = UnderstandingState(concepts={"dialogue", "understanding"})

    delta = SemanticDelta(
        delta_type="link_concepts",
        source="dialogue",
        content="transforms",
        target="understanding",
    )

    updated = apply_delta(state, delta)

    assert ("dialogue", "transforms", "understanding") in updated.relations


def test_link_concepts_requires_source_and_target():
    state = UnderstandingState()

    delta = SemanticDelta(
        delta_type="link_concepts",
        content="relates to",
    )

    try:
        apply_delta(state, delta)
    except ValueError as exc:
        assert "source and target" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
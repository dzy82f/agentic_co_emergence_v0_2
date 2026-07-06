from datetime import datetime

from agentic_co_emergence.runtime_semantics import apply_contribution_semantics
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.models.perspective import PerspectivePack


def test_contribution_updates_discussion_understanding_state():
    state = DiscussionState(
        perspective_pack=PerspectivePack(
            question="What is dialogue?",
            perspectives=(),
            created=datetime(2026, 7, 6, 12, 0, 0),
        ),
        agent_states=(),
    )

    updated = apply_contribution_semantics(
        state,
        speaker="Tenzing",
        content="Dialogue transforms understanding",
    )

    assert "Dialogue transforms understanding" in updated.understanding_state.concepts
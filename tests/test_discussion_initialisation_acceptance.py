from pathlib import Path

from agentic_co_emergence.inputs.perspective_pack_loader import load_perspective_pack
from agentic_co_emergence.runtime.controller import initialise_discussion
from agentic_co_emergence.models.discussion_state import DiscussionState


EXAMPLE_PACK = Path("examples/perspective_packs/q000005.md")


def test_can_initialise_discussion_from_perspective_pack():
    pack = load_perspective_pack(EXAMPLE_PACK)
    state = initialise_discussion(pack)

    assert isinstance(state, DiscussionState)
    assert state.round_number == 0
    assert state.transcript == []
    assert len(state.agent_states) == 9
    assert state.perspective_pack == pack


def test_initial_discussion_has_no_contributions():
    pack = load_perspective_pack(EXAMPLE_PACK)
    state = initialise_discussion(pack)

    assert state.contribution_count == 0
    assert state.is_open is True

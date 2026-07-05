from pathlib import Path

from agentic_co_emergence.inputs.perspective_pack_loader import load_perspective_pack
from agentic_co_emergence.models.contribution import Contribution
from agentic_co_emergence.runtime.controller import initialise_discussion, add_contribution


PERSPECTIVE_PACK_PATH = Path("examples/perspective_packs/q000005.md")


def test_accepting_contribution_returns_new_discussion_state():
    pack = load_perspective_pack(PERSPECTIVE_PACK_PATH)
    initial_state = initialise_discussion(pack)

    contribution = Contribution(
        speaker="Aletheia",
        text="This is an accepted contribution.",
        contribution_type="accepted",
    )

    new_state = add_contribution(initial_state, contribution)

    assert new_state is not initial_state
    assert len(new_state.transcript) == len(initial_state.transcript) + 1


def test_accepting_contribution_does_not_mutate_original_state():
    pack = load_perspective_pack(PERSPECTIVE_PACK_PATH)
    initial_state = initialise_discussion(pack)

    original_transcript = list(initial_state.transcript)

    contribution = Contribution(
        speaker="Aletheia",
        text="This is an accepted contribution.",
        contribution_type="accepted",
    )

    _ = add_contribution(initial_state, contribution)

    assert initial_state.transcript == original_transcript
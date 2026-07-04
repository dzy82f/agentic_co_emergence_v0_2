from pathlib import Path

from agentic_co_emergence.inputs.perspective_pack_loader import load_perspective_pack
from agentic_co_emergence.models.contribution import Contribution
from agentic_co_emergence.runtime.controller import add_contribution, initialise_discussion


EXAMPLE_PACK = Path("examples/perspective_packs/q000005.md")


def test_can_add_exactly_one_contribution():
    pack = load_perspective_pack(EXAMPLE_PACK)
    state_0 = initialise_discussion(pack)

    contribution = Contribution(
        speaker="Ada",
        text="Peirce is underrated because his influence exceeds his public recognition.",
        contribution_type="argument",
    )

    state_1 = add_contribution(state_0, contribution)

    assert state_0.contribution_count == 0
    assert state_1.contribution_count == 1
    assert state_1.transcript[-1] == contribution
    assert state_1.round_number >= state_0.round_number


def test_contribution_does_not_mutate_prior_state():
    pack = load_perspective_pack(EXAMPLE_PACK)
    state_0 = initialise_discussion(pack)

    contribution = Contribution(
        speaker="Harry",
        text="The Peirce case is strengthened by the fact that later thinkers popularised fragments of his work.",
        contribution_type="support",
    )

    state_1 = add_contribution(state_0, contribution)

    assert state_0 is not state_1
    assert state_0.transcript == []
    assert len(state_1.transcript) == 1

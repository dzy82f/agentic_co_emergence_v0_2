from pathlib import Path

from agentic_co_emergence.inputs.perspective_pack_loader import load_perspective_pack
from agentic_co_emergence.models.contribution import Contribution
from agentic_co_emergence.runtime.controller import add_contribution, initialise_discussion


EXAMPLE_PACK = Path("examples/perspective_packs/q000005.md")


def test_perspective_pack_remains_unchanged_after_updates():
    pack = load_perspective_pack(EXAMPLE_PACK)
    original_question = pack.question
    original_perspectives = tuple((p.agent_name, p.text) for p in pack.perspectives)

    state = initialise_discussion(pack)

    for i in range(10):
        state = add_contribution(
            state,
            Contribution(
                speaker="Ada",
                text=f"Contribution {i}",
                contribution_type="argument",
            ),
        )

    assert pack.question == original_question
    assert tuple((p.agent_name, p.text) for p in pack.perspectives) == original_perspectives


def test_transcript_is_append_only():
    pack = load_perspective_pack(EXAMPLE_PACK)
    state = initialise_discussion(pack)

    first = Contribution(
        speaker="Ada",
        text="First contribution",
        contribution_type="argument",
    )
    second = Contribution(
        speaker="Joan",
        text="Second contribution",
        contribution_type="challenge",
    )

    state = add_contribution(state, first)
    state = add_contribution(state, second)

    assert state.transcript == [first, second]

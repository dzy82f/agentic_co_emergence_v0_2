from pathlib import Path

from agentic_co_emergence.inputs.perspective_pack_loader import load_perspective_pack
from agentic_co_emergence.models.contribution import Contribution
from agentic_co_emergence.reports.markdown_writer import build_synthesis_markdown
from agentic_co_emergence.runtime.controller import add_contribution, initialise_discussion


EXAMPLE_PACK = Path("examples/perspective_packs/q000005.md")


def test_synthesis_can_be_regenerated_from_pack_and_trace():
    pack = load_perspective_pack(EXAMPLE_PACK)
    state = initialise_discussion(pack)

    state = add_contribution(
        state,
        Contribution(
            speaker="Ada",
            text="Peirce is a strong candidate because his ideas shaped inquiry, signs and abduction.",
            contribution_type="argument",
        ),
    )
    state = add_contribution(
        state,
        Contribution(
            speaker="Joan",
            text="Astell highlights that underratedness can involve structural exclusion from the canon.",
            contribution_type="challenge",
        ),
    )

    synthesis_1 = build_synthesis_markdown(state)
    synthesis_2 = build_synthesis_markdown(state)

    assert synthesis_1 == synthesis_2
    assert "Peirce" in synthesis_1
    assert "Astell" in synthesis_1
    assert "Collective Understanding" in synthesis_1

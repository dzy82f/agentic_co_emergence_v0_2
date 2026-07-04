from pathlib import Path

import pytest

from agentic_co_emergence.inputs.perspective_pack_loader import load_perspective_pack
from agentic_co_emergence.models.perspective import PerspectivePack


EXAMPLE_PACK = Path("examples/perspective_packs/q000005.md")


def test_can_load_perspective_pack():
    pack = load_perspective_pack(EXAMPLE_PACK)

    assert isinstance(pack, PerspectivePack)
    assert pack.question
    assert "underrated Western philosopher" in pack.question
    assert len(pack.perspectives) == 9


def test_perspective_pack_contains_named_agents():
    pack = load_perspective_pack(EXAMPLE_PACK)

    agent_names = {p.agent_name for p in pack.perspectives}

    assert agent_names == {
        "Ada",
        "Aletheia",
        "Alison",
        "Harry",
        "joan",
        "lyla",
        "Sael",
        "Synaia",
        "tenzing",
    }


def test_initial_perspectives_are_immutable():
    pack = load_perspective_pack(EXAMPLE_PACK)
    perspective = pack.perspectives[0]

    with pytest.raises(Exception):
        perspective.text = "Mutated perspective"

    with pytest.raises(Exception):
        pack.question = "Mutated question"

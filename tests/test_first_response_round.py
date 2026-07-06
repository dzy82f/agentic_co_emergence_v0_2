from agentic_co_emergence.cli.run_first_response_round import (
    build_response_contribution,
    run_first_response_round,
)


def test_build_response_contribution_names_target():
    contribution = build_response_contribution(
        responder="Tenzing",
        target="Ada",
        target_contribution="Ada chose Peirce.",
    )

    assert "respond to Ada" in contribution
    assert "Ada chose Peirce." in contribution
    assert "shared discussion" in contribution


def test_run_first_response_round_creates_response_transcript():
    state = run_first_response_round("perspective_pack.json")

    assert state.contribution_count == 3
    assert state.transcript[0]["agent_name"] == "Tenzing"
    assert state.transcript[1]["agent_name"] == "Joan"
    assert state.transcript[2]["agent_name"] == "Sael"
    assert "respond to Ada" in state.transcript[0]["contribution"]
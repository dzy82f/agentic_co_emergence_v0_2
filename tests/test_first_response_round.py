from agentic_co_emergence.cli.run_first_response_round import (
    run_first_response_round,
)


def test_first_response_round_records_response_targets():
    state = run_first_response_round()

    assert state.contribution_count > 1

    for index, contribution in enumerate(state.transcript):
        if index == 0:
            assert "response_to" not in contribution
            continue

        response_to = contribution["response_to"]

        assert response_to["contribution_index"] < index
        assert response_to["agent_name"] != contribution["agent_name"]
        assert response_to["relation"] in {
            "extends",
            "questions",
            "disagrees",
            "supports",
            "synthesises",
        }
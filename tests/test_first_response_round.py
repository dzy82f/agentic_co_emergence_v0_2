from agentic_co_emergence.cli.run_first_response_round import (
    run_first_response_round,
)


def test_first_response_round_uses_transcript_so_far_for_deliberation():
    prompts: list[str] = []

    def fake_response_generator(prompt: str) -> str:
        prompts.append(prompt)
        return "I am responding to the discussion so far."

    state = run_first_response_round(response_generator=fake_response_generator)

    assert state.contribution_count > 1
    assert len(prompts) == state.contribution_count - 1

    for contribution in state.transcript:
        assert "agent_name" in contribution
        assert "contribution" in contribution

    assert "Discussion so far:" in prompts[0]
    assert state.transcript[0]["contribution"] in prompts[0]
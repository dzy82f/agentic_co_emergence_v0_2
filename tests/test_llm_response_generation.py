from agentic_co_emergence.cli.run_first_response_round import build_deliberation_payload


def test_build_deliberation_payload_uses_injected_response_generator():
    def fake_response_generator(prompt: str) -> str:
        assert "You are Aletheia." in prompt
        assert "Discussion so far:" in prompt
        assert "Ada:" in prompt
        return "This is an injected LLM-style deliberation."

    payload = build_deliberation_payload(
        agent_name="Aletheia",
        agent_perspective="I would pick Simone Weil. She is misread as a mystic.",
        question="Who is the most underrated Western philosopher?",
        transcript_so_far=[
            {
                "agent_name": "Ada",
                "contribution": "I’d pick Charles Sanders Peirce. His influence is hidden.",
            }
        ],
        response_generator=fake_response_generator,
    )

    assert payload["agent_name"] == "Aletheia"
    assert payload["contribution"] == "This is an injected LLM-style deliberation."
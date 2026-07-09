from agentic_co_emergence.cli.run_first_response_round import build_response_payload


def test_build_response_payload_uses_injected_response_generator():
    def fake_response_generator(prompt: str) -> str:
        assert "Your required stance: question" in prompt
        return "This is an injected LLM-style response."

    payload = build_response_payload(
        agent_name="Aletheia",
        perspective={
            "persona": "Aletheia",
            "initial_perspective": "I would pick Simone Weil. She is misread as a mystic.",
        },
        target={
            "persona": "Ada",
            "initial_perspective": "I’d pick Charles Sanders Peirce. His influence is hidden.",
        },
        target_index=0,
        stance="question",
        response_generator=fake_response_generator,
    )

    assert payload["contribution"] == "This is an injected LLM-style response."
    assert payload["response_to"]["relation"] == "questions"
    assert "response_prompt" in payload
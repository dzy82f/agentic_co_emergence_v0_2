from __future__ import annotations

from agentic_co_emergence.llm_deliberation_generation import (
    DeliberationInput,
    build_deliberation_prompt,
    format_transcript,
    generate_llm_deliberation,
)


def test_format_transcript_handles_empty_transcript() -> None:
    assert format_transcript([]) == "No one has spoken yet."


def test_format_transcript_renders_existing_contributions() -> None:
    transcript = [
        {
            "agent_name": "Ada",
            "contribution": "Peirce is underrated because his work links inquiry and meaning.",
        },
        {
            "agent_name": "Tenzing",
            "contribution": "I agree, but the systems implication matters most.",
        },
    ]

    rendered = format_transcript(transcript)

    assert "Ada:" in rendered
    assert "Peirce is underrated" in rendered
    assert "Tenzing:" in rendered
    assert "systems implication" in rendered


def test_build_deliberation_prompt_includes_core_context() -> None:
    deliberation_input = DeliberationInput(
        agent_name="Joan",
        agent_perspective="Philosophy matters when it improves judgement.",
        question="Who is the most underrated Western philosopher?",
        transcript_so_far=[
            {
                "agent_name": "Ada",
                "contribution": "I would choose Peirce.",
            }
        ],
    )

    prompt = build_deliberation_prompt(deliberation_input)

    assert "You are Joan." in prompt
    assert "Who is the most underrated Western philosopher?" in prompt
    assert "Philosophy matters when it improves judgement." in prompt
    assert "Ada:" in prompt
    assert "I would choose Peirce." in prompt
    assert "respond directly to at least one previous speaker" in prompt
    assert "shifted, refined, or challenged your view" in prompt


def test_generate_llm_deliberation_returns_stripped_response() -> None:
    deliberation_input = DeliberationInput(
        agent_name="Tenzing",
        agent_perspective="I care about systems coherence.",
        question="What should we conclude?",
        transcript_so_far=[
            {
                "agent_name": "Ada",
                "contribution": "The strongest answer is Peirce.",
            }
        ],
    )

    def fake_llm(prompt: str) -> str:
        assert "Discussion so far:" in prompt
        return "  Ada's point shifts my emphasis toward Peirce's communal theory of inquiry.  "

    response = generate_llm_deliberation(deliberation_input, fake_llm)

    assert response == "Ada's point shifts my emphasis toward Peirce's communal theory of inquiry."


def test_generate_llm_deliberation_rejects_empty_response() -> None:
    deliberation_input = DeliberationInput(
        agent_name="Ada",
        agent_perspective="Meaning emerges through use.",
        question="What matters?",
        transcript_so_far=[],
    )

    def fake_llm(_: str) -> str:
        return "   "

    try:
        generate_llm_deliberation(deliberation_input, fake_llm)
    except ValueError as exc:
        assert "empty deliberation response" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
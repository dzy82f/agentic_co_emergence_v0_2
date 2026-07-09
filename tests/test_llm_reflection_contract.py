from agentic_co_emergence.llm_reflection import build_reflection_prompt


def test_build_reflection_prompt_contains_required_context():
    prompt = build_reflection_prompt(
        agent_name="Aletheia",
        initial_position="Simone Weil is underrated because she is misread as a mystic.",
        discussion_summary="The group distinguished hidden influence from canonical misfit.",
        provisional_consensus="No single winner; two mechanisms emerged.",
    )

    assert "Aletheia" in prompt
    assert "Simone Weil is underrated" in prompt
    assert "hidden influence" in prompt
    assert "canonical misfit" in prompt
    assert "reflection_kind" in prompt
    assert "confidence_before" in prompt
    assert "confidence_after" in prompt
    assert "agreement_with_consensus" in prompt
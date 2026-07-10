from agentic_co_emergence.influence_extraction import (
    InfluenceRecord,
    detect_influence_type,
    extract_influence_records,
)


def test_detects_refinement() -> None:
    contribution = "Joan's point sharpens my thinking about what counts as underrated."

    assert detect_influence_type(contribution) == "refinement"


def test_detects_criterion_adoption_before_general_refinement() -> None:
    contribution = (
        "What’s shifting for me is that being underrated often correlates "
        "with challenging dominant social or epistemic orders."
    )

    assert detect_influence_type(contribution) == "criterion_adopted"


def test_extracts_influence_record_from_transcript() -> None:
    transcript = [
        {
            "agent_name": "Harry",
            "contribution": "Peirce quietly supports democratic knowledge.",
        },
        {
            "agent_name": "Joan",
            "contribution": (
                "Harry's emphasis adds a vital political edge. "
                "What’s shifting for me is that being underrated often correlates "
                "with challenging dominant social or epistemic orders."
            ),
        },
    ]

    records = extract_influence_records(transcript)

    assert records == [
        InfluenceRecord(
            source_agent="Harry",
            target_agent="Joan",
            influence_type="criterion_adopted",
            evidence=(
                "Harry's emphasis adds a vital political edge. "
                "What’s shifting for me is that being underrated often correlates "
                "with challenging dominant social or epistemic orders."
            ),
        )
    ]


def test_falls_back_to_previous_speaker_when_no_name_is_mentioned() -> None:
    transcript = [
        {
            "agent_name": "Joan",
            "contribution": "Underrated thinkers challenge dominant power structures.",
        },
        {
            "agent_name": "Lyla",
            "contribution": (
                "That sharpens my thinking about Reid and philosophical accessibility."
            ),
        },
    ]

    records = extract_influence_records(transcript)

    assert len(records) == 1
    assert records[0].source_agent == "Joan"
    assert records[0].target_agent == "Lyla"
    assert records[0].influence_type == "refinement"


def test_ignores_first_contribution_without_prior_source() -> None:
    transcript = [
        {
            "agent_name": "Ada",
            "contribution": "I would pick Peirce.",
        }
    ]

    assert extract_influence_records(transcript) == []
from agentic_co_emergence.models.claim import Claim


def test_claim_is_a_first_class_computational_object():
    claim = Claim(
        id="claim-001",
        speaker="Ada",
        text="Fallibilism makes inquiry self-correcting.",
    )

    assert claim.id == "claim-001"
    assert claim.speaker == "Ada"
    assert claim.text == "Fallibilism makes inquiry self-correcting."
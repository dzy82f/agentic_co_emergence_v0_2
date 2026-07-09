from agentic_co_emergence.group_consensus import build_group_consensus
from agentic_co_emergence.models.discussion_state import DiscussionState


def test_group_consensus_identifies_shared_mechanisms():
    state = DiscussionState(
        perspective_pack={},
        agent_states={},
        transcript=[
            {
                "agent_name": "Ada",
                "contribution": "Peirce is underrated because his influence is hidden in later intellectual machinery.",
            },
            {
                "agent_name": "Aletheia",
                "contribution": "Weil is underrated because she is hard to place inside the accepted canon.",
            },
            {
                "agent_name": "Lyla",
                "contribution": "The discussion suggests hidden influence and canonical misfit are both mechanisms of underrating.",
            },
        ],
    )

    consensus = build_group_consensus(state)

    assert consensus["kind"] == "group_consensus"
    assert "hidden influence" in consensus["shared_mechanisms"]
    assert "canonical misfit" in consensus["shared_mechanisms"]
    assert consensus["conclusion"] == (
        "The group has not reached a single winner. "
        "It has converged on a stronger shared understanding: philosophers can be underrated through different mechanisms, especially hidden influence and canonical misfit."
    )
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.dialogue_relationship import choose_dialogue_relationship


def test_choose_dialogue_relationship_selects_previous_contribution():
    state = DiscussionState(
        perspective_pack={},
        agent_states={},
        transcript=[
            {
                "agent_name": "Ada",
                "contribution": "Peirce is underrated because he made inquiry communal and fallible.",
            }
        ],
    )

    relationship = choose_dialogue_relationship(
        state=state,
        responding_agent_name="Tenzing",
    )

    assert relationship == {
        "responds_to": "Ada",
        "stance": "extend",
    }
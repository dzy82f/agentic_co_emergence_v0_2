from __future__ import annotations

from agentic_co_emergence.models.agent_state import AgentState
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.models.perspective import PerspectivePack


def initialise_discussion(pack: PerspectivePack) -> DiscussionState:
    agent_states = tuple(
        AgentState(
            agent_name=perspective.agent_name,
            current_understanding=perspective.text,
            contribution_count=0,
        )
        for perspective in pack.perspectives
    )

    return DiscussionState(
        perspective_pack=pack,
        agent_states=agent_states,
        transcript=[],
        round_number=0,
        is_open=True,
    )
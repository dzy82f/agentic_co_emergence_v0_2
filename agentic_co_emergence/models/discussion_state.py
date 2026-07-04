from __future__ import annotations

from dataclasses import dataclass, field

from agentic_co_emergence.models.agent_state import AgentState
from agentic_co_emergence.models.perspective import PerspectivePack


@dataclass(frozen=True)
class DiscussionState:
    perspective_pack: PerspectivePack
    agent_states: tuple[AgentState, ...]
    transcript: list = field(default_factory=list)
    round_number: int = 0
    is_open: bool = True

    @property
    def contribution_count(self) -> int:
        return len(self.transcript)
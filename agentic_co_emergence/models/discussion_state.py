from __future__ import annotations

from dataclasses import dataclass, field

from agentic_co_emergence.models.agent_state import AgentState
from agentic_co_emergence.models.perspective import PerspectivePack
from agentic_co_emergence.models.semantic_state import UnderstandingState


@dataclass(frozen=True)
class DiscussionState:
    perspective_pack: PerspectivePack
    agent_states: tuple[AgentState, ...]
    transcript: list[dict[str, str]] = field(default_factory=list)
    understanding_state: UnderstandingState = field(default_factory=UnderstandingState)
    round_number: int = 0
    is_open: bool = True

    @property
    def contribution_count(self) -> int:
        return len(self.transcript)
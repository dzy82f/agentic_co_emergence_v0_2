from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentState:
    agent_name: str
    current_understanding: str
    contribution_count: int = 0
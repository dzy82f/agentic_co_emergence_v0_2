from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from agentic_co_emergence.understanding import UnderstandingDelta


@dataclass(frozen=True)
class DiscussionTransition:
    """
    Immutable record of the computational event that transforms one
    DiscussionState into the next.
    """

    transition_id: str
    from_state_id: str
    to_state_id: str
    speaker: str
    contribution: str
    understanding_delta: UnderstandingDelta
    accepted: bool = True
    reason: Optional[str] = None
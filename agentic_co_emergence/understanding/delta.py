"""
Understanding Delta

A minimal computational representation of how understanding changes
between two immutable Discussion States.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentic_co_emergence.models.claim import Claim


@dataclass(frozen=True)
class UnderstandingDelta:
    """
    Describes the conceptual changes between two discussion states.
    """

    new_claims: list[str | Claim] = field(default_factory=list)
    new_questions: list[str] = field(default_factory=list)
    new_tensions: list[str] = field(default_factory=list)

    summary: str = ""
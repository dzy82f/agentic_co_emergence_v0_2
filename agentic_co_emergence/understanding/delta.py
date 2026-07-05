"""
Understanding Delta

A minimal computational representation of how understanding changes
between two immutable Discussion States.

Milestone 0.3
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class UnderstandingDelta:
    """
    Describes the conceptual changes between two discussion states.

    This is intentionally minimal.
    """

    new_claims: list[str] = field(default_factory=list)
    new_questions: list[str] = field(default_factory=list)
    new_tensions: list[str] = field(default_factory=list)

    summary: str = ""
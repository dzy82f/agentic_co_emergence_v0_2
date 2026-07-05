from __future__ import annotations

from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.understanding import UnderstandingDelta


def build_understanding_delta(
    before: DiscussionState,
    after: DiscussionState,
) -> UnderstandingDelta:
    """
    Build a minimal UnderstandingDelta from two DiscussionStates.

    Milestone 0.3: first implementation.

    For now, newly added transcript items are treated as candidate new claims.
    """

    before_count = len(before.transcript)
    after_items = after.transcript[before_count:]

    new_claims = [str(item) for item in after_items]

    return UnderstandingDelta(
        new_claims=new_claims,
        summary=f"{len(new_claims)} new claim(s) identified.",
    )
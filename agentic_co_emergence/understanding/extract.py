from __future__ import annotations

from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.understanding import UnderstandingDelta


def build_understanding_delta(
    before: DiscussionState,
    after: DiscussionState,
) -> UnderstandingDelta:
    """
    Build a minimal UnderstandingDelta from two DiscussionStates.

    Newly added transcript items are treated as candidate new claims.
    Structured transcript items expose their text field as the claim.
    """

    before_count = len(before.transcript)
    after_items = after.transcript[before_count:]

    new_claims = [
        item.get("text", str(item)) if isinstance(item, dict) else str(item)
        for item in after_items
    ]

    return UnderstandingDelta(
        new_claims=new_claims,
        summary=f"{len(new_claims)} new claim(s) identified.",
    )
from __future__ import annotations

from dataclasses import replace

from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.models.semantic_state import SemanticDelta, apply_delta


def semantic_deltas_from_contribution(
    speaker: str,
    content: str,
) -> list[SemanticDelta]:
    """
    MVP semantic extraction.

    This is intentionally simple. The goal is to prove that a contribution
    can produce semantic deltas, not to solve semantic extraction yet.
    """
    deltas: list[SemanticDelta] = []

    if content.strip():
        deltas.append(
            SemanticDelta(
                delta_type="introduce_concept",
                content=content.strip(),
                source=speaker,
            )
        )

    return deltas


def apply_contribution_semantics(
    state: DiscussionState,
    speaker: str,
    content: str,
) -> DiscussionState:
    updated_understanding = state.understanding_state

    for delta in semantic_deltas_from_contribution(speaker, content):
        updated_understanding = apply_delta(updated_understanding, delta)

    return replace(
        state,
        understanding_state=updated_understanding,
    )
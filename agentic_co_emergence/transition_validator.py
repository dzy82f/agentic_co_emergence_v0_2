from __future__ import annotations

from dataclasses import dataclass

from agentic_co_emergence.discussion_transition import DiscussionTransition


@dataclass(frozen=True)
class TransitionValidationResult:
    accepted: bool
    reason: str | None = None


def validate_transition(
    transition: DiscussionTransition,
) -> TransitionValidationResult:
    """
    Validate whether a DiscussionTransition is structurally acceptable.

    This is intentionally minimal for Milestone 0.5.
    """

    if not transition.transition_id.strip():
        return TransitionValidationResult(
            accepted=False,
            reason="transition_id is required",
        )

    if not transition.from_state_id.strip():
        return TransitionValidationResult(
            accepted=False,
            reason="from_state_id is required",
        )

    if not transition.to_state_id.strip():
        return TransitionValidationResult(
            accepted=False,
            reason="to_state_id is required",
        )

    if transition.from_state_id == transition.to_state_id:
        return TransitionValidationResult(
            accepted=False,
            reason="from_state_id and to_state_id must differ",
        )

    if not transition.speaker.strip():
        return TransitionValidationResult(
            accepted=False,
            reason="speaker is required",
        )

    if not transition.contribution.strip():
        return TransitionValidationResult(
            accepted=False,
            reason="contribution is required",
        )

    return TransitionValidationResult(accepted=True)
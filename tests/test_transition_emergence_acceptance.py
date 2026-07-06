from __future__ import annotations

from dataclasses import replace

from agentic_co_emergence.models.agent_state import AgentState
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.models.perspective import Perspective, PerspectivePack
from agentic_co_emergence.understanding import build_understanding_delta


def make_state() -> DiscussionState:
    pack = PerspectivePack(
    question="Who is the most underrated Western philosopher?",
    created="2026-07-06",
    perspectives=(
        Perspective(
            agent_name="Tenzing",
            text="Reid is underrated because ordinary epistemic competence is philosophically important.",
        ),
        Perspective(
            agent_name="Ada",
            text="Peirce is underrated because inquiry is fallible, communal, and self-correcting.",
        ),
    ),
)

    return DiscussionState(
        perspective_pack=pack,
        agent_states=(
    AgentState(
        agent_name="Tenzing",
        current_understanding="",
    ),
    AgentState(
        agent_name="Ada",
        current_understanding="",
    ),
),
    )


def add_contribution(
    state: DiscussionState,
    speaker: str,
    text: str,
) -> DiscussionState:
    return replace(
        state,
        transcript=[
            *state.transcript,
            {
                "speaker": speaker,
                "text": text,
            },
        ],
    )


def delta_trajectory(
    initial: DiscussionState,
    ordered_contributions: list[tuple[str, str]],
) -> list[tuple[str, ...]]:
    state = initial
    trajectory: list[tuple[str, ...]] = []

    for speaker, text in ordered_contributions:
        next_state = add_contribution(state, speaker, text)
        delta = build_understanding_delta(state, next_state)
        trajectory.append(tuple(delta.new_claims))
        state = next_state

    return trajectory


def test_same_initial_state_different_order_produces_different_delta_trajectory():
    initial = make_state()

    contributions = [
        ("Tenzing", "Ordinary epistemic competence matters before radical doubt."),
        ("Ada", "Fallibilism makes inquiry self-correcting rather than merely sceptical."),
    ]

    trajectory_a = delta_trajectory(initial, contributions)
    trajectory_b = delta_trajectory(initial, list(reversed(contributions)))

    assert trajectory_a != trajectory_b
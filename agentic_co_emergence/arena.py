from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class ArenaState:
    claims: Tuple[str, ...] = field(default_factory=tuple)
    questions: Tuple[str, ...] = field(default_factory=tuple)
    distinctions: Tuple[str, ...] = field(default_factory=tuple)
    tensions: Tuple[str, ...] = field(default_factory=tuple)
    commitments: Tuple[str, ...] = field(default_factory=tuple)
    turn_index: int = 0

    @classmethod
    def empty(cls) -> "ArenaState":
        return cls()


@dataclass(frozen=True)
class ArenaDelta:
    claims_added: Tuple[str, ...] = field(default_factory=tuple)
    questions_added: Tuple[str, ...] = field(default_factory=tuple)
    distinctions_added: Tuple[str, ...] = field(default_factory=tuple)
    tensions_added: Tuple[str, ...] = field(default_factory=tuple)
    commitments_added: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class DialogueTurn:
    speaker: str
    contribution: str


def _append_unique(existing: Tuple[str, ...], additions: Tuple[str, ...]) -> Tuple[str, ...]:
    result = list(existing)
    for item in additions:
        if item not in result:
            result.append(item)
    return tuple(result)


def extract_delta(turn: DialogueTurn) -> ArenaDelta:
    text = turn.contribution.lower()

    claims = []
    questions = []
    distinctions = []
    tensions = []
    commitments = []

    if "depends on" in text:
        claims.append(turn.contribution)

    if "whether" in text:
        questions.append(turn.contribution)

    if "distinguish" in text or "distinct from" in text:
        distinctions.append(turn.contribution)

    if "tension" in text or "versus" in text or "vs" in text:
        tensions.append(turn.contribution)

    if "should" in text or "must" in text:
        commitments.append(turn.contribution)

    return ArenaDelta(
        claims_added=tuple(claims),
        questions_added=tuple(questions),
        distinctions_added=tuple(distinctions),
        tensions_added=tuple(tensions),
        commitments_added=tuple(commitments),
    )


def apply_delta(state: ArenaState, delta: ArenaDelta) -> ArenaState:
    return ArenaState(
        claims=_append_unique(state.claims, delta.claims_added),
        questions=_append_unique(state.questions, delta.questions_added),
        distinctions=_append_unique(state.distinctions, delta.distinctions_added),
        tensions=_append_unique(state.tensions, delta.tensions_added),
        commitments=_append_unique(state.commitments, delta.commitments_added),
        turn_index=state.turn_index + 1,
    )


def governed_transition(state: ArenaState, turn: DialogueTurn) -> ArenaState:
    delta = extract_delta(turn)
    return apply_delta(state, delta)


def run_dialogue(initial_state: ArenaState, turns: Tuple[DialogueTurn, ...]) -> Tuple[ArenaState, ...]:
    states = [initial_state]
    current = initial_state

    for turn in turns:
        current = governed_transition(current, turn)
        states.append(current)

    return tuple(states)
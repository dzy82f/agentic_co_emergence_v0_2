from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


DeltaType = Literal[
    "introduce_concept",
    "refine_concept",
    "link_concepts",
    "raise_question",
    "record_tension",
]


@dataclass(frozen=True)
class SemanticDelta:
    delta_type: DeltaType
    content: str
    source: str | None = None
    target: str | None = None


@dataclass
class UnderstandingState:
    concepts: set[str] = field(default_factory=set)
    relations: list[tuple[str, str, str]] = field(default_factory=list)
    questions: list[str] = field(default_factory=list)
    tensions: list[str] = field(default_factory=list)
    refinements: list[str] = field(default_factory=list)


def apply_delta(
    state: UnderstandingState,
    delta: SemanticDelta,
) -> UnderstandingState:
    if delta.delta_type == "introduce_concept":
        state.concepts.add(delta.content)

    elif delta.delta_type == "refine_concept":
        state.refinements.append(delta.content)

    elif delta.delta_type == "link_concepts":
        if not delta.source or not delta.target:
            raise ValueError("link_concepts requires source and target")
        state.relations.append((delta.source, delta.content, delta.target))

    elif delta.delta_type == "raise_question":
        state.questions.append(delta.content)

    elif delta.delta_type == "record_tension":
        state.tensions.append(delta.content)

    else:
        raise ValueError(f"Unknown delta type: {delta.delta_type}")

    return state
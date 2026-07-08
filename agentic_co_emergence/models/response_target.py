from __future__ import annotations

from dataclasses import dataclass


ALLOWED_RESPONSE_RELATIONS = {
    "extends",
    "questions",
    "disagrees",
    "supports",
    "synthesises",
}


@dataclass(frozen=True)
class ResponseTarget:
    agent_name: str
    contribution_index: int
    relation: str

    def __post_init__(self) -> None:
        if self.relation not in ALLOWED_RESPONSE_RELATIONS:
            raise ValueError(f"Unsupported response relation: {self.relation}")
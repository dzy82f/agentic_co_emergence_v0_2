from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Perspective:
    agent_name: str
    text: str


@dataclass(frozen=True)
class PerspectivePack:
    question: str
    created: str | None
    perspectives: Tuple[Perspective, ...]
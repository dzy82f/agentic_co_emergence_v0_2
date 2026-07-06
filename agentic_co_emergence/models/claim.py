from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Claim:
    id: str
    speaker: str
    text: str
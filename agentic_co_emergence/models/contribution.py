from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Contribution:
    speaker: str
    text: str
    contribution_type: str
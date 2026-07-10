from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


InfluenceType = Literal[
    "agreement",
    "disagreement",
    "refinement",
    "criterion_adopted",
    "new_concept",
]


@dataclass(frozen=True)
class InfluenceRecord:
    source_agent: str
    target_agent: str
    influence_type: InfluenceType
    evidence: str


AGREEMENT_MARKERS = (
    "resonates with",
    "i agree",
    "building on",
    "adds a valuable dimension",
)

REFINEMENT_MARKERS = (
    "sharpens my thinking",
    "sharpens my take",
    "reframes my thinking",
    "deepening of my view",
    "makes me realize",
    "what’s shifting for me",
    "challenges my earlier framing",
)

DISAGREEMENT_MARKERS = (
    "i disagree",
    "i would challenge",
    "i think that misses",
    "that said",
    "still,",
)

CRITERION_MARKERS = (
    "underrated often correlates",
    "what makes",
    "who counts as",
    "who philosophy is for",
    "dominant social or epistemic orders",
    "dominant power structures",
)


def _lower(text: str) -> str:
    return text.lower()


def detect_influence_type(contribution: str) -> InfluenceType | None:
    text = _lower(contribution)

    if any(marker in text for marker in CRITERION_MARKERS):
        return "criterion_adopted"

    if any(marker in text for marker in REFINEMENT_MARKERS):
        return "refinement"

    if any(marker in text for marker in DISAGREEMENT_MARKERS):
        return "disagreement"

    if any(marker in text for marker in AGREEMENT_MARKERS):
        return "agreement"

    return None


def detect_source_agent(
    *,
    contribution: str,
    previous_agents: list[str],
) -> str | None:
    lowered = _lower(contribution)

    for agent in reversed(previous_agents):
        if agent.lower() in lowered:
            return agent

    if previous_agents:
        return previous_agents[-1]

    return None


def extract_evidence(contribution: str, max_length: int = 220) -> str:
    cleaned = " ".join(contribution.split())

    if len(cleaned) <= max_length:
        return cleaned

    return cleaned[: max_length - 1].rstrip() + "…"


def extract_influence_records(
    transcript: list[dict[str, str]],
) -> list[InfluenceRecord]:
    records: list[InfluenceRecord] = []
    previous_agents: list[str] = []

    for contribution in transcript:
        target_agent = contribution["agent_name"]
        contribution_text = contribution["contribution"]

        influence_type = detect_influence_type(contribution_text)

        if influence_type is not None:
            source_agent = detect_source_agent(
                contribution=contribution_text,
                previous_agents=previous_agents,
            )

            if source_agent is not None:
                records.append(
                    InfluenceRecord(
                        source_agent=source_agent,
                        target_agent=target_agent,
                        influence_type=influence_type,
                        evidence=extract_evidence(contribution_text),
                    )
                )

        previous_agents.append(target_agent)

    return records
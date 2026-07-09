from __future__ import annotations

import re
from pathlib import Path

from agentic_co_emergence.cli.run_first_discussion import (
    DEFAULT_PACK_PATH,
    build_initial_state,
    load_perspective_pack,
    write_transcript_markdown,
)
from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


DEFAULT_RESPONSE_TRANSCRIPT_PATH = Path(
    "artefacts/transcripts/first_response_round_transcript.md"
)

RESPONSE_RELATIONS = [
    "extends",
    "questions",
    "disagrees",
    "supports",
    "synthesises",
]

KNOWN_NOMINEES = {
    "charles sanders peirce": "Charles Sanders Peirce",
    "peirce": "Charles Sanders Peirce",
    "simone weil": "Simone Weil",
    "weil": "Simone Weil",
    "mary astell": "Mary Astell",
    "astell": "Mary Astell",
    "thomas reid": "Thomas Reid",
    "reid": "Thomas Reid",
    "michel de montaigne": "Michel de Montaigne",
    "montaigne": "Michel de Montaigne",
}

NOMINATION_PATTERNS = (
    re.compile(r"I[’']d pick\s+([^\.]+?)\.", re.IGNORECASE),
    re.compile(r"I would pick\s+([^\.]+?)\.", re.IGNORECASE),
    re.compile(r"If I had to name one, I[’']d pick\s+([^\.]+?)\.", re.IGNORECASE),
    re.compile(r"My nominee is\s+([^\.]+?)\.", re.IGNORECASE),
    re.compile(r"I nominate\s+([^\.]+?)\.", re.IGNORECASE),
)


def clean_text(text: str) -> str:
    return " ".join(text.split())


def split_sentences(text: str) -> list[str]:
    cleaned = clean_text(text)
    if not cleaned:
        return []

    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", cleaned)
        if sentence.strip()
    ]


def infer_nominee(text: str) -> str:
    lowered = text.lower()

    for marker, nominee in KNOWN_NOMINEES.items():
        if marker in lowered:
            return nominee

    for pattern in NOMINATION_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1).strip()

    return "their nominee"


def summarize_reason(text: str) -> str:
    sentences = split_sentences(text)

    if len(sentences) >= 2:
        return sentences[1]

    if sentences:
        return sentences[0]

    return "no reason was supplied"


def build_response_prompt(
    *,
    target_name: str,
    target_nominee: str,
    target_reason_summary: str,
    own_nominee: str,
    own_reason_summary: str,
) -> str:
    return (
        f"Respond to {target_name}. "
        f"They nominated {target_nominee}. "
        f"Their reason, in summary, is: {target_reason_summary}\n\n"
        f"Your own nominee is {own_nominee}. "
        f"Your reason, in summary, is: {own_reason_summary}\n\n"
        "Write a contribution that genuinely engages with their reasoning. "
        "Agree, disagree, refine, synthesise, or challenge as appropriate."
    )


def build_response_text(
    *,
    target_name: str,
    target_nominee: str,
    target_reason_summary: str,
    own_nominee: str,
    own_reason_summary: str,
) -> str:
    if target_nominee == own_nominee:
        return (
            f"I agree with {target_name}'s choice of {target_nominee}, but I would sharpen the reason. "
            f"{target_name}'s case is that {target_reason_summary} "
            f"I would add that {own_reason_summary} "
            "Taken together, those points make the underrating less a matter of simple neglect than of fit: "
            "this thinker is difficult to absorb because their work cuts across the categories by which philosophy is usually taught and remembered."
        )

    return (
        f"I take {target_name}'s case for {target_nominee} seriously: {target_reason_summary} "
        f"But my own nominee, {own_nominee}, is underrated for a different reason: {own_reason_summary} "
        "The contrast is useful. One kind of neglect happens when a thinker quietly supplies intellectual machinery that later thinkers use without naming the source. "
        "Another happens when a thinker is hard to place inside the accepted canon, so their importance is treated as marginal rather than central. "
        "On that basis, I would not simply replace their nominee with mine; I would say the discussion is beginning to map different mechanisms of philosophical underrating."
    )


def build_response_payload(
    *,
    agent_name: str,
    perspective: dict[str, str],
    target: dict[str, str],
    target_index: int,
    relation: str,
) -> dict[str, object]:
    target_name = target["persona"]
    target_text = target["initial_perspective"]
    own_text = perspective["initial_perspective"]

    target_nominee = infer_nominee(target_text)
    own_nominee = infer_nominee(own_text)
    target_reason_summary = summarize_reason(target_text)
    own_reason_summary = summarize_reason(own_text)

    return {
        "agent_name": agent_name,
        "contribution": build_response_text(
            target_name=target_name,
            target_nominee=target_nominee,
            target_reason_summary=target_reason_summary,
            own_nominee=own_nominee,
            own_reason_summary=own_reason_summary,
        ),
        "response_to": {
            "agent_name": target_name,
            "contribution_index": target_index,
            "relation": relation,
        },
        "response_prompt": build_response_prompt(
            target_name=target_name,
            target_nominee=target_nominee,
            target_reason_summary=target_reason_summary,
            own_nominee=own_nominee,
            own_reason_summary=own_reason_summary,
        ),
    }


def run_first_response_round(
    pack_path: str | Path = DEFAULT_PACK_PATH,
) -> DiscussionState:
    pack = load_perspective_pack(pack_path)

    state = build_initial_state(pack)
    engine = DiscussionTransitionEngine(state)

    perspectives = pack["perspectives"]

    for index, perspective in enumerate(perspectives):
        agent_name = perspective["persona"]

        if index == 0:
            payload = {
                "agent_name": agent_name,
                "contribution": perspective["initial_perspective"],
            }
        else:
            target_index = index - 1
            relation = RESPONSE_RELATIONS[target_index % len(RESPONSE_RELATIONS)]

            payload = build_response_payload(
                agent_name=agent_name,
                perspective=perspective,
                target=perspectives[target_index],
                target_index=target_index,
                relation=relation,
            )

        state = engine.step(
            DiscussionEvent(
                kind="agent_contribution",
                payload=payload,
            )
        )

    return state


def main() -> None:
    final_state = run_first_response_round()

    write_transcript_markdown(
        final_state,
        DEFAULT_RESPONSE_TRANSCRIPT_PATH,
    )

    print(f"Markdown: {DEFAULT_RESPONSE_TRANSCRIPT_PATH}")
    print(f"Contributions: {final_state.contribution_count}")


if __name__ == "__main__":
    main()
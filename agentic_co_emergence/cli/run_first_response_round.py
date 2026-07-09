from __future__ import annotations

import re
from pathlib import Path

from agentic_co_emergence.cli.run_first_discussion import (
    DEFAULT_PACK_PATH,
    build_initial_state,
    load_perspective_pack,
    write_transcript_markdown,
)
from agentic_co_emergence.dialogue_relationship import choose_dialogue_relationship
from agentic_co_emergence.llm_response_generation import (
    ResponseGenerator,
    generate_response_text,
)
from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


DEFAULT_RESPONSE_TRANSCRIPT_PATH = Path(
    "artefacts/transcripts/first_response_round_transcript.md"
)

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


def relation_for_stance(stance: str) -> str:
    relation_by_stance = {
        "extend": "extends",
        "question": "questions",
        "disagree": "disagrees",
        "support": "supports",
        "synthesise": "synthesises",
    }

    return relation_by_stance.get(stance, stance)


def build_response_prompt(
    *,
    target_name: str,
    target_nominee: str,
    target_reason_summary: str,
    own_nominee: str,
    own_reason_summary: str,
    stance: str,
) -> str:
    return (
        f"You are responding to {target_name} in a structured deliberation.\n\n"
        f"{target_name}'s nominee: {target_nominee}\n"
        f"{target_name}'s reason: {target_reason_summary}\n\n"
        f"Your nominee: {own_nominee}\n"
        f"Your reason: {own_reason_summary}\n\n"
        f"Your required stance: {stance}\n\n"
        "Write one concise contribution that genuinely engages with the target's reasoning.\n"
        "Do not merely repeat your own original view.\n"
        "Do not announce the metadata.\n"
        "Make the stance visible through the substance of the response.\n"
        "Return only the contribution text."
    )


def build_response_payload(
    *,
    agent_name: str,
    perspective: dict[str, str],
    target: dict[str, str],
    target_index: int,
    stance: str,
    response_generator: ResponseGenerator | None = None,
) -> dict[str, object]:
    target_name = target["persona"]
    target_text = target["initial_perspective"]
    own_text = perspective["initial_perspective"]

    target_nominee = infer_nominee(target_text)
    own_nominee = infer_nominee(own_text)
    target_reason_summary = summarize_reason(target_text)
    own_reason_summary = summarize_reason(own_text)

    response_prompt = build_response_prompt(
        target_name=target_name,
        target_nominee=target_nominee,
        target_reason_summary=target_reason_summary,
        own_nominee=own_nominee,
        own_reason_summary=own_reason_summary,
        stance=stance,
    )

    return {
        "agent_name": agent_name,
        "contribution": generate_response_text(
            prompt=response_prompt,
            response_generator=response_generator,
        ),
        "response_to": {
            "agent_name": target_name,
            "contribution_index": target_index,
            "relation": relation_for_stance(stance),
        },
        "response_prompt": response_prompt,
    }


def find_perspective_index_by_persona(
    *,
    perspectives: list[dict[str, str]],
    persona: str,
) -> int:
    for index, perspective in enumerate(perspectives):
        if perspective["persona"] == persona:
            return index

    raise ValueError(f"No perspective found for persona: {persona}")


def run_first_response_round(
    pack_path: str | Path = DEFAULT_PACK_PATH,
    response_generator: ResponseGenerator | None = None,
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
            relationship = choose_dialogue_relationship(
                state=state,
                responding_agent_name=agent_name,
            )

            target_index = find_perspective_index_by_persona(
                perspectives=perspectives,
                persona=relationship["responds_to"],
            )

            payload = build_response_payload(
                agent_name=agent_name,
                perspective=perspective,
                target=perspectives[target_index],
                target_index=target_index,
                stance=relationship["stance"],
                response_generator=response_generator,
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
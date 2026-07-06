from __future__ import annotations

from pathlib import Path

from agentic_co_emergence.cli.run_first_discussion import (
    DEFAULT_PACK_PATH,
    load_perspective_pack,
    write_transcript_markdown,
)
from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


DEFAULT_RESPONSE_TRANSCRIPT_PATH = Path(
    "artefacts/transcripts/first_response_round_transcript.md"
)


def build_initial_state(perspective_pack: dict) -> DiscussionState:
    return DiscussionState(
        perspective_pack=perspective_pack,
        agent_states=(),
    )


def build_response_contribution(
    responder: str,
    target: str,
    target_contribution: str,
) -> str:
    return (
        f"I want to respond to {target}. "
        f"Their perspective raises an important point: {target_contribution} "
        f"My role in this first response round is not to replace that view, "
        f"but to test what it brings into the shared discussion."
    )


def run_first_response_round(perspective_pack_path: str | Path) -> DiscussionState:
    perspective_pack = load_perspective_pack(perspective_pack_path)
    state = build_initial_state(perspective_pack)

    engine = DiscussionTransitionEngine(state=state)

    perspectives = perspective_pack["perspectives"]

    response_pairs = [
        ("Tenzing", perspectives[0]),
        ("Joan", perspectives[1]),
        ("Sael", perspectives[3]),
    ]

    for responder, target_perspective in response_pairs:
        engine.step(
            DiscussionEvent(
                kind="agent_contribution",
                payload={
                    "agent_name": responder,
                    "contribution": build_response_contribution(
                        responder=responder,
                        target=target_perspective["persona"],
                        target_contribution=target_perspective[
                            "initial_perspective"
                        ],
                    ),
                },
            )
        )

    return engine.current_state()


def main() -> None:
    final_state = run_first_response_round(DEFAULT_PACK_PATH)
    write_transcript_markdown(final_state, DEFAULT_RESPONSE_TRANSCRIPT_PATH)

    print(f"Question: {final_state.perspective_pack['question']}")
    print(f"Response contributions: {final_state.contribution_count}")
    print(f"Markdown: {DEFAULT_RESPONSE_TRANSCRIPT_PATH}")


if __name__ == "__main__":
    main()
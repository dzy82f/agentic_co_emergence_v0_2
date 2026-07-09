from __future__ import annotations

from pathlib import Path

from agentic_co_emergence.cli.run_first_discussion import (
    DEFAULT_PACK_PATH,
    build_initial_state,
    load_perspective_pack,
    write_transcript_markdown,
)
from agentic_co_emergence.llm_deliberation_generation import (
    DeliberationInput,
    generate_llm_deliberation,
)
from agentic_co_emergence.llm_response_generation import ResponseGenerator
from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


DEFAULT_RESPONSE_TRANSCRIPT_PATH = Path(
    "artefacts/transcripts/first_response_round_transcript.md"
)


def build_deliberation_payload(
    *,
    agent_name: str,
    agent_perspective: str,
    question: str,
    transcript_so_far: list[dict[str, str]],
    response_generator: ResponseGenerator,
) -> dict[str, str]:
    deliberation_input = DeliberationInput(
        agent_name=agent_name,
        agent_perspective=agent_perspective,
        question=question,
        transcript_so_far=transcript_so_far,
    )

    return {
        "agent_name": agent_name,
        "contribution": generate_llm_deliberation(
            deliberation_input,
            response_generator,
        ),
    }


def run_first_response_round(
    pack_path: str | Path = DEFAULT_PACK_PATH,
    response_generator: ResponseGenerator | None = None,
) -> DiscussionState:
    if response_generator is None:
        raise ValueError(
            "run_first_response_round now requires an injected response_generator."
        )

    pack = load_perspective_pack(pack_path)

    state = build_initial_state(pack)
    engine = DiscussionTransitionEngine(state)

    question = pack["question"]
    perspectives = pack["perspectives"]

    for index, perspective in enumerate(perspectives):
        agent_name = perspective["persona"]
        agent_perspective = perspective["initial_perspective"]

        if index == 0:
            payload = {
                "agent_name": agent_name,
                "contribution": agent_perspective,
            }
        else:
            payload = build_deliberation_payload(
                agent_name=agent_name,
                agent_perspective=agent_perspective,
                question=question,
                transcript_so_far=state.transcript,
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
    def missing_live_llm(_: str) -> str:
        raise RuntimeError(
            "No live LLM generator is configured for this command-line entry point."
        )

    final_state = run_first_response_round(response_generator=missing_live_llm)

    write_transcript_markdown(
        final_state,
        DEFAULT_RESPONSE_TRANSCRIPT_PATH,
    )

    print(f"Markdown: {DEFAULT_RESPONSE_TRANSCRIPT_PATH}")
    print(f"Contributions: {final_state.contribution_count}")


if __name__ == "__main__":
    main()
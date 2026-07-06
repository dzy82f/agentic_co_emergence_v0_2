from __future__ import annotations

import json
from pathlib import Path

from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


DEFAULT_PACK_PATH = Path("perspective_pack.json")
DEFAULT_TRANSCRIPT_PATH = Path(
    "artefacts/transcripts/first_discussion_transcript.md"
)


def load_perspective_pack(path: str | Path) -> dict:
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def build_initial_state(perspective_pack: dict) -> DiscussionState:
    return DiscussionState(
        perspective_pack=perspective_pack,
        agent_states=(),
    )


def run_first_discussion(perspective_pack_path: str | Path) -> DiscussionState:
    perspective_pack = load_perspective_pack(perspective_pack_path)
    state = build_initial_state(perspective_pack)

    engine = DiscussionTransitionEngine(state=state)

    for perspective in perspective_pack["perspectives"]:
        engine.step(
            DiscussionEvent(
                kind="agent_contribution",
                payload={
                    "agent_name": perspective["persona"],
                    "contribution": perspective["initial_perspective"],
                },
            )
        )

    return engine.current_state()


def write_transcript_markdown(
    state: DiscussionState,
    output_path: str | Path,
) -> None:
    output_path = Path(output_path)

    lines = [
        "# Discussion Transcript",
        "",
        "## Question",
        "",
        state.perspective_pack["question"],
        "",
        "## Contributions",
        "",
    ]

    for entry in state.transcript:
        lines.extend(
            [
                f"### {entry['agent_name']}",
                "",
                entry["contribution"],
                "",
            ]
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    final_state = run_first_discussion(DEFAULT_PACK_PATH)
    write_transcript_markdown(final_state, DEFAULT_TRANSCRIPT_PATH)

    print(f"Question: {final_state.perspective_pack['question']}")
    print(f"Contributions: {final_state.contribution_count}")
    print(f"Markdown: {DEFAULT_TRANSCRIPT_PATH}")


if __name__ == "__main__":
    main()
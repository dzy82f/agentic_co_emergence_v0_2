from __future__ import annotations

import json
from pathlib import Path

from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState
from agentic_co_emergence.transition_engine import DiscussionTransitionEngine


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


def main() -> None:
    pack_path = Path("perspective_pack.json")
    final_state = run_first_discussion(pack_path)

    print(f"Question: {final_state.perspective_pack['question']}")
    print(f"Contributions: {final_state.contribution_count}")
    print()

    for entry in final_state.transcript:
        print(f"{entry['agent_name']}:")
        print(entry["contribution"])
        print()


if __name__ == "__main__":
    main()
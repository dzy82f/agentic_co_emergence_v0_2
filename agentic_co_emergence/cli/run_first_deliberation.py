from __future__ import annotations

from pathlib import Path

from agentic_co_emergence.cli.run_first_response_round import (
    DEFAULT_PACK_PATH,
    run_first_response_round,
)
from agentic_co_emergence.group_consensus import build_group_consensus
from agentic_co_emergence.reflection_grounded_consensus import (
    build_reflection_grounded_consensus,
)
from agentic_co_emergence.reflection_round import build_reflection_round


DEFAULT_DELIBERATION_DIR = Path("artefacts/deliberation")


def write_markdown(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")


def write_group_consensus(path: Path, consensus: dict[str, object]) -> None:
    mechanisms = consensus.get("shared_mechanisms", [])
    mechanism_lines = "\n".join(f"- {mechanism}" for mechanism in mechanisms)

    body = (
        "## Shared Mechanisms\n\n"
        f"{mechanism_lines}\n\n"
        "## Conclusion\n\n"
        f"{consensus.get('conclusion', '')}"
    )

    write_markdown(path, "Group Consensus", body)


def write_reflection_round(path: Path, reflections: list[dict[str, object]]) -> None:
    sections: list[str] = []

    for reflection in reflections:
        position_delta = reflection.get("position_delta", {})

        if not isinstance(position_delta, dict):
            position_delta = {}

        sections.append(
            "\n".join(
                [
                    f"## {reflection.get('agent_name', '')}",
                    "",
                    f"Reflection kind: {reflection.get('reflection_kind', '')}",
                    "",
                    f"Changed: {position_delta.get('changed', '')}",
                    "",
                    f"From: {position_delta.get('from', '')}",
                    "",
                    f"To: {position_delta.get('to', '')}",
                    "",
                    f"Reason: {position_delta.get('reason', '')}",
                ]
            )
        )

    write_markdown(path, "Reflection Round", "\n\n".join(sections))


def write_final_consensus(path: Path, consensus: dict[str, object]) -> None:
    refined = consensus.get("agents_refined", [])
    unchanged = consensus.get("agents_unchanged", [])

    refined_lines = "\n".join(f"- {agent}" for agent in refined)
    unchanged_lines = "\n".join(f"- {agent}" for agent in unchanged)

    body = (
        "## Agents Refined\n\n"
        f"{refined_lines}\n\n"
        "## Agents Unchanged\n\n"
        f"{unchanged_lines}\n\n"
        "## Conclusion\n\n"
        f"{consensus.get('conclusion', '')}"
    )

    write_markdown(path, "Reflection-Grounded Consensus", body)


def run_first_deliberation(
    *,
    pack_path: str | Path = DEFAULT_PACK_PATH,
    output_dir: str | Path = DEFAULT_DELIBERATION_DIR,
) -> dict[str, object]:
    output_path = Path(output_dir)

    state = run_first_response_round(pack_path)

    group_consensus = build_group_consensus(state)

    reflections = build_reflection_round(
        state=state,
        consensus=group_consensus,
    )

    final_consensus = build_reflection_grounded_consensus(reflections)

    write_group_consensus(
        output_path / "03_group_consensus.md",
        group_consensus,
    )
    write_reflection_round(
        output_path / "04_reflection_round.md",
        reflections,
    )
    write_final_consensus(
        output_path / "05_final_consensus.md",
        final_consensus,
    )

    return {
        "state": state,
        "group_consensus": group_consensus,
        "reflections": reflections,
        "final_consensus": final_consensus,
    }


def main() -> None:
    result = run_first_deliberation()

    print("Deliberation complete")
    print(f"Contributions: {result['state'].contribution_count}")
    print(f"Group consensus: {DEFAULT_DELIBERATION_DIR / '03_group_consensus.md'}")
    print(f"Reflection round: {DEFAULT_DELIBERATION_DIR / '04_reflection_round.md'}")
    print(f"Final consensus: {DEFAULT_DELIBERATION_DIR / '05_final_consensus.md'}")


if __name__ == "__main__":
    main()
from __future__ import annotations

from typing import Any


def build_group_consensus(state: Any) -> dict[str, object]:
    combined_text = " ".join(
        record.get("contribution", "")
        for record in state.transcript
    ).lower()

    shared_mechanisms: list[str] = []

    if (
        "hidden influence" in combined_text
        or "uncredited influence" in combined_text
        or "intellectual machinery" in combined_text
    ):
        shared_mechanisms.append("hidden influence")

    if (
        "canonical misfit" in combined_text
        or "accepted canon" in combined_text
        or "hard to place" in combined_text
    ):
        shared_mechanisms.append("canonical misfit")

    if not shared_mechanisms:
        conclusion = (
            "The group has not yet reached a clear consensus. "
            "Further reflection is needed before a shared conclusion can be stated."
        )
    elif len(shared_mechanisms) == 1:
        conclusion = (
            "The group has not reached a single winner. "
            f"It has converged on one shared mechanism of underrating: {shared_mechanisms[0]}."
        )
    else:
        conclusion = (
            "The group has not reached a single winner. "
            "It has converged on a stronger shared understanding: philosophers can be underrated through different mechanisms, especially hidden influence and canonical misfit."
        )

    return {
        "kind": "group_consensus",
        "shared_mechanisms": shared_mechanisms,
        "conclusion": conclusion,
    }
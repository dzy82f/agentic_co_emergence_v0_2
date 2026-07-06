from __future__ import annotations


INITIAL_PERSPECTIVES = {
    "Tenzing": "Reid is underrated because philosophy rewards destabilising scepticism over ordinary epistemic competence.",
    "Ada": "Peirce is underrated because his work connects logic, signs, inquiry, and fallibilism.",
    "Joan": "The important test is whether a philosopher changes what responsible action looks like.",
}


def concepts(text: str) -> set[str]:
    words = text.lower().replace(".", "").replace(",", "").split()
    return {w for w in words if len(w) > 6}


def synthetic_discussion(order: list[str]) -> list[set[str]]:
    shared: set[str] = set()
    trajectory: list[set[str]] = []

    for speaker in order:
        speaker_concepts = concepts(INITIAL_PERSPECTIVES[speaker])
        shared = shared | speaker_concepts

        if {"scepticism", "fallibilism"} <= shared:
            shared.add("self-correcting-inquiry")

        if {"responsible", "competence"} <= shared:
            shared.add("practical-epistemology")

        trajectory.append(set(shared))

    return trajectory


def test_discussion_trajectory_depends_on_interaction_order():
    same_initial_conditions = INITIAL_PERSPECTIVES.copy()

    path_a = synthetic_discussion(["Tenzing", "Ada", "Joan"])
    path_b = synthetic_discussion(["Joan", "Tenzing", "Ada"])

    assert same_initial_conditions == INITIAL_PERSPECTIVES
    assert path_a != path_b


def test_final_understanding_contains_emergent_concepts():
    trajectory = synthetic_discussion(["Tenzing", "Ada", "Joan"])
    final_understanding = trajectory[-1]

    initial_concepts = set().union(
        *(concepts(text) for text in INITIAL_PERSPECTIVES.values())
    )

    emergent_concepts = final_understanding - initial_concepts

    assert "self-correcting-inquiry" in emergent_concepts
    assert emergent_concepts
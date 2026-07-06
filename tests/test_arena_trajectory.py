from agentic_co_emergence.arena import ArenaState, DialogueTurn, run_dialogue


def test_governed_dialogue_produces_reproducible_trajectory():
    initial = ArenaState.empty()

    turns = (
        DialogueTurn(
            speaker="Tenzing",
            contribution="The issue depends on whether stability or novelty matters more.",
        ),
        DialogueTurn(
            speaker="Joan",
            contribution="That creates a governance tension: useful change versus uncontrolled change.",
        ),
        DialogueTurn(
            speaker="Aletheia",
            contribution="We should distinguish novelty from understanding.",
        ),
    )

    trajectory_1 = run_dialogue(initial, turns)
    trajectory_2 = run_dialogue(initial, turns)

    assert trajectory_1 == trajectory_2
    assert len(trajectory_1) == 4

    final = trajectory_1[-1]

    assert final.turn_index == 3
    assert len(final.claims) == 1
    assert len(final.questions) == 1
    assert len(final.tensions) == 1
    assert len(final.distinctions) == 1
    assert len(final.commitments) == 1


def test_arena_state_is_minimal_structured_residue_not_transcript():
    initial = ArenaState.empty()

    turns = (
        DialogueTurn(
            speaker="Ada",
            contribution="We should distinguish moral concern from operational control.",
        ),
    )

    trajectory = run_dialogue(initial, turns)
    final = trajectory[-1]

    assert final.turn_index == 1
    assert final.distinctions == (
        "We should distinguish moral concern from operational control.",
    )
    assert final.commitments == (
        "We should distinguish moral concern from operational control.",
    )

    assert not hasattr(final, "transcript")
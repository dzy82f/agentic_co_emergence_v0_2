from agentic_co_emergence.cli.run_first_discussion import (
    run_first_discussion,
    write_transcript_markdown,
)


def test_run_first_discussion_builds_transcript():
    state = run_first_discussion("perspective_pack.json")

    assert state.contribution_count == 9
    assert state.transcript[0]["agent_name"] == "Ada"


def test_write_transcript_markdown(tmp_path):
    state = run_first_discussion("perspective_pack.json")
    output_path = tmp_path / "transcript.md"

    write_transcript_markdown(state, output_path)

    markdown = output_path.read_text(encoding="utf-8")

    assert "# Discussion Transcript" in markdown
    assert "## Question" in markdown
    assert "## Contributions" in markdown
    assert "Ada" in markdown
    assert "Charles Sanders Peirce" in markdown
from agentic_co_emergence.cli.review_first_transcript import (
    build_transcript_review,
    write_review_markdown,
)


def test_build_transcript_review_counts_contributions():
    transcript = "\n".join(
        [
            "# Discussion Transcript",
            "",
            "### Ada",
            "",
            "First contribution.",
            "",
            "### Tenzing",
            "",
            "Second contribution.",
            "",
        ]
    )

    review = build_transcript_review(transcript)

    assert "This transcript contains 2 recorded contributions." in review
    assert "not yet a co-emergent discussion" in review


def test_write_review_markdown(tmp_path):
    output_path = tmp_path / "review.md"
    review = "# Transcript Review\n"

    write_review_markdown(review, output_path)

    assert output_path.read_text(encoding="utf-8") == review
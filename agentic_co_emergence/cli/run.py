from __future__ import annotations

from pathlib import Path

from agentic_co_emergence.cli.review_first_transcript import (
    build_transcript_review,
    load_transcript,
    write_review_markdown,
)
from agentic_co_emergence.cli.run_first_discussion import (
    DEFAULT_PACK_PATH,
    DEFAULT_TRANSCRIPT_PATH,
    run_first_discussion,
    write_transcript_markdown,
)
from agentic_co_emergence.cli.run_first_response_round import (
    DEFAULT_RESPONSE_TRANSCRIPT_PATH,
    run_first_response_round,
)


def main() -> None:
    first_state = run_first_discussion(DEFAULT_PACK_PATH)
    write_transcript_markdown(first_state, DEFAULT_TRANSCRIPT_PATH)

    response_state = run_first_response_round(DEFAULT_PACK_PATH)
    write_transcript_markdown(response_state, DEFAULT_RESPONSE_TRANSCRIPT_PATH)

    transcript = load_transcript(DEFAULT_RESPONSE_TRANSCRIPT_PATH)
    review = build_transcript_review(transcript)

    review_path = Path("artefacts/reports/first_transcript_review.md")
    write_review_markdown(review, review_path)

    print("Agentic Co-Emergence MVP run complete")
    print(f"Initial transcript: {DEFAULT_TRANSCRIPT_PATH}")
    print(f"Response transcript: {DEFAULT_RESPONSE_TRANSCRIPT_PATH}")
    print(f"Review: {review_path}")


if __name__ == "__main__":
    main()
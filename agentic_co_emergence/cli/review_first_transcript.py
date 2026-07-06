from __future__ import annotations

from pathlib import Path


DEFAULT_TRANSCRIPT_PATH = Path(
    "artefacts/transcripts/first_discussion_transcript.md"
)


def load_transcript(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def build_transcript_review(transcript_markdown: str) -> str:
    contribution_count = transcript_markdown.count("\n### ")

    return "\n".join(
        [
            "# Transcript Review",
            "",
            "## Source",
            "",
            str(DEFAULT_TRANSCRIPT_PATH),
            "",
            "## Summary",
            "",
            f"This transcript contains {contribution_count} recorded contributions.",
            "",
            "## Initial Assessment",
            "",
            "This artefact records the initial perspectives captured from the perspective pack.",
            "It is not yet a co-emergent discussion, because the agents have not responded to one another.",
            "",
            "## Next Development Step",
            "",
            "Introduce one response round in which selected agents evaluate, challenge, or synthesise the captured perspectives.",
            "",
        ]
    )


def write_review_markdown(review_markdown: str, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(review_markdown, encoding="utf-8")


def main() -> None:
    transcript = load_transcript(DEFAULT_TRANSCRIPT_PATH)
    review = build_transcript_review(transcript)

    output_path = Path("artefacts/reports/first_transcript_review.md")
    write_review_markdown(review, output_path)

    print(f"Transcript: {DEFAULT_TRANSCRIPT_PATH}")
    print(f"Review: {output_path}")


if __name__ == "__main__":
    main()
from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass


LLMCallable = Callable[[str], str]


@dataclass(frozen=True)
class DeliberationInput:
    agent_name: str
    agent_perspective: str
    question: str
    transcript_so_far: Sequence[dict[str, str]]


def format_transcript(transcript: Sequence[dict[str, str]]) -> str:
    if not transcript:
        return "No one has spoken yet."

    lines: list[str] = []

    for entry in transcript:
        agent_name = entry.get("agent_name", "Unknown")
        contribution = entry.get("contribution", "").strip()
        lines.append(f"{agent_name}:\n{contribution}")

    return "\n\n".join(lines)


def build_deliberation_prompt(deliberation_input: DeliberationInput) -> str:
    transcript = format_transcript(deliberation_input.transcript_so_far)

    return f"""You are {deliberation_input.agent_name}.

Question:
{deliberation_input.question}

Your original perspective:
{deliberation_input.agent_perspective}

Discussion so far:
{transcript}

Write your next contribution to the discussion.

Your contribution should:
- respond directly to at least one previous speaker
- say whether anything in the discussion has shifted, refined, or challenged your view
- add one genuinely new point rather than merely repeating your original perspective
- remain concise and thoughtful
- speak in your own voice

Return only the contribution text.
"""


def generate_llm_deliberation(
    deliberation_input: DeliberationInput,
    llm: LLMCallable,
) -> str:
    prompt = build_deliberation_prompt(deliberation_input)
    response = llm(prompt).strip()

    if not response:
        raise ValueError("LLM returned an empty deliberation response.")

    return response
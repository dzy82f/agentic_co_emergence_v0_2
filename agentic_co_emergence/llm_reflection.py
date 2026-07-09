from __future__ import annotations


def build_reflection_prompt(
    *,
    agent_name: str,
    initial_position: str,
    discussion_summary: str,
    provisional_consensus: str,
) -> str:
    return f"""
You are {agent_name}.

You are taking part in a deliberation.

Your original position was:

{initial_position}

The discussion so far can be summarised as:

{discussion_summary}

The provisional group consensus is:

{provisional_consensus}

Reflect honestly on whether your position has changed.

Return only valid JSON using this schema:

{{
  "agent_name": "{agent_name}",
  "reflection_kind": "unchanged | refine | change_position",
  "changed": true,
  "confidence_before": 0.0,
  "confidence_after": 0.0,
  "initial_position": "...",
  "current_position": "...",
  "reason": "...",
  "agreement_with_consensus": 0.0
}}

Rules:
- Do not invent a new position unless the discussion genuinely justifies it.
- If your nominee is unchanged but your reason has become sharper, use "refine".
- If your nominee or core criterion changes, use "change_position".
- If nothing material changes, use "unchanged".
- confidence_before, confidence_after, and agreement_with_consensus must be numbers between 0 and 1.
""".strip()
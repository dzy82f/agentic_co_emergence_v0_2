# NEXT

## Current Position

Milestone 0.4 — Executable Discussion Runtime

43 acceptance and unit tests passing.

Implemented:

- Perspective Pack loading
- DiscussionState
- DiscussionEvent
- TransitionValidator
- TransitionEngine
- RuntimeController
- SemanticState
- Claim extraction
- UnderstandingDelta
- Markdown reporting

The current runtime can execute a governed discussion and produce discussion artefacts.

---

## Next Milestone

Milestone 0.5 — Demonstrate Emergent Understanding

## Research Question

Can the current computational model produce a change in collective understanding that is not reducible to any individual contribution?

## Acceptance Criterion

Given a Perspective Pack and a discussion:

- execute a complete discussion
- produce a transcript
- extract claims
- construct an UnderstandingDelta
- demonstrate that the resulting understanding contains at least one synthesised insight beyond any single contribution

## Constraints

- No additional runtime abstractions unless demanded by experiment.
- Prefer experiments over architecture.
- Treat UnderstandingDelta as provisional until validated by repeated runs.
- Keep the theory and implementation aligned.
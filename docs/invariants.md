# Invariants

## Purpose

This document defines the invariants for `agentic_co_emergence_v0_2`.

An invariant is something that must remain true throughout the lifetime of the system. Invariants are not implementation details. They are architectural commitments.

The runtime may evolve. The agent behaviours may become richer. The synthesis process may become more sophisticated. But these invariants should remain stable unless the underlying architecture is deliberately revised.

---

## 1. Perspective Packs are immutable

A Perspective Pack is an input artefact.

Once loaded into the runtime, it must not be modified.

The runtime may derive state from a Perspective Pack, but it must never alter the original pack.

### Rationale

The Perspective Pack represents the independent starting positions of the agents before discussion. If it can be changed during discussion, the distinction between initial perspective and evolved understanding collapses.

---

## 2. Initial Perspectives are never overwritten

Each agent's Initial Perspective is preserved exactly as supplied by the Perspective Pack.

An agent may revise its current position during discussion, but that revision must be stored separately from the Initial Perspective.

### Rationale

The system needs to distinguish between:

- what the agent initially thought
- what the agent later said
- how the agent's position changed

Without this distinction, co-emergence cannot be observed.

---

## 3. Contributions are append-only

A Contribution is a historical event.

Once created, it must not be edited, removed, or silently replaced.

Corrections, clarifications, retractions, and revisions must be represented as later Contributions.

### Rationale

The discussion trace is evidence of the process by which understanding evolved. Editing history destroys the ability to reconstruct that process.

---

## 4. Transcript history is never rewritten

The transcript is an ordered record of Contributions.

The runtime may append to the transcript, but it must not reorder or rewrite prior entries.

### Rationale

The order of contributions matters. Later contributions are responses to earlier states. Reordering the transcript changes the causal structure of the discussion.

---

## 5. Agent State is mutable, but historically accountable

Agent State may change during discussion.

However, every material change to Agent State should be traceable to one or more Contributions or runtime operations.

### Rationale

Agent State represents the evolving internal posture of an agent. It is allowed to change, but those changes should not appear magically. The runtime should be able to explain why an agent's current position differs from its initial perspective.

---

## 6. Collective Understanding is derived, not directly asserted

Collective Understanding is derived from:

- the Perspective Pack
- Contributions
- runtime state updates
- explicit synthesis operations

It should not be manually inserted as an unsupported conclusion.

### Rationale

The purpose of the runtime is to transform independent perspectives into emergent understanding through governed interaction. If Collective Understanding can be asserted directly, the discussion process becomes decorative rather than constitutive.

---

## 7. Synthesis is a snapshot, not the truth

A Synthesis is a representation of Collective Understanding at a particular point in the process.

It is provisional, reproducible, and revisable.

It is not the final truth of the matter.

### Rationale

The runtime should preserve epistemic humility. A synthesis records where the discussion has arrived, not what reality must be.

---

## 8. Runtime state transitions are explicit

The runtime must move between defined states by explicit transitions.

It should not jump implicitly from one operation to another without representing the state change.

### Rationale

The runtime exists to define an operational envelope. That envelope is only meaningful if permissible states and transitions are visible and enforceable.

---

## 9. The runtime governs process, not content

The runtime may decide:

- who may speak
- when synthesis is permitted
- what information is visible
- which operation is valid in the current state
- when the discussion is complete

The runtime must not decide what an agent is required to believe.

### Rationale

Agentic Co-Emergence is not a script for producing predetermined conclusions. It is a governed process within which reasoning may occur.

---

## 10. Agents may revise positions, but not origins

An agent may:

- change its confidence
- concede a point
- sharpen an argument
- adopt a distinction introduced by another agent
- move toward or away from a candidate synthesis

An agent may not retroactively change its Initial Perspective.

### Rationale

The system is interested in transformation. Transformation requires a stable origin and an observable path away from that origin.

---

## 11. Minority positions must remain visible

A minority view must not disappear merely because it is outnumbered.

The runtime may identify convergence, but it should preserve unresolved or underrepresented positions in the trace and synthesis.

### Rationale

Emergent understanding is not the same as majority vote. Minority positions may contain important distinctions, warnings, or alternative framings.

---

## 12. Disagreement is a first-class object

Disagreement should be represented explicitly rather than treated as failure.

A disagreement may concern:

- facts
- definitions
- criteria
- priorities
- implications
- values
- confidence

### Rationale

Discussion becomes intellectually useful when disagreement is made visible, structured, and available for further reasoning.

---

## 13. Completion does not require consensus

A discussion may complete when the runtime has satisfied its completion conditions.

Completion may produce:

- consensus
- partial convergence
- clarified disagreement
- competing syntheses
- open questions

### Rationale

Some questions should not collapse into a single answer. A good runtime should recognise when structured disagreement is a legitimate output.

---

## 14. Outputs must be reproducible from inputs and trace

Given the same:

- Perspective Pack
- runtime configuration
- discussion trace
- synthesis rules

it should be possible to reconstruct the same final report, subject to any explicitly declared non-determinism.

### Rationale

Reproducibility is necessary for testing, debugging, and intellectual accountability.

---

## 15. Non-determinism must be declared

If the runtime uses randomisation, model sampling, dynamic speaker selection, or any other non-deterministic process, that fact must be visible in the trace or configuration.

### Rationale

Non-determinism is not forbidden, but hidden non-determinism makes behaviour difficult to understand and evaluate.

---

## 16. The operational envelope must be inspectable

At any point, it should be possible to ask:

- what state is the runtime in?
- what operations are currently permitted?
- what information is available to each agent?
- what conditions must be met before the next transition?

### Rationale

The project is about governed co-emergence. A hidden or implicit envelope cannot be governed.

---

## 17. No synthesis before permission

The runtime must not produce a final synthesis until the relevant synthesis condition has been satisfied.

Examples of synthesis conditions may include:

- a fixed number of rounds
- every agent has contributed at least once
- every major disagreement has been surfaced
- a completion condition has been met

### Rationale

Premature synthesis is one of the main failure modes of discussion systems. The runtime must protect against it explicitly.

---

## 18. Reports are views, not primary state

Markdown reports, summaries, and exported documents are views over the underlying artefacts.

They should not be treated as the authoritative runtime state.

### Rationale

Reports are useful for humans, but the canonical process record is the structured input, state, and trace.

---

## 19. The system should remain substrate-neutral

The architecture should not assume that all participants must be LLM agents.

In principle, the runtime should be compatible with:

- LLM agents
- human participants
- scripted agents
- historical-text agents
- hybrid groups

### Rationale

The project is a computational theory of governed discussion, not merely a wrapper around a particular model.

---

## 20. Every abstraction must earn its place

New concepts, classes, modules, or runtime behaviours should only be added when they serve a defined architectural responsibility.

### Rationale

The project should remain small, inspectable, and conceptually disciplined. Complexity should be introduced only when the simpler model has failed to express something necessary.

---

## Summary

The most important invariants are:

1. Inputs are immutable.
2. History is append-only.
3. State changes are accountable.
4. Synthesis is provisional.
5. Disagreement is preserved.
6. The runtime governs process, not content.
7. Outputs must be reproducible from inputs and trace.

Together, these invariants protect the central purpose of Agentic Co-Emergence: to observe and govern the transformation of independent perspectives into richer collective understanding.

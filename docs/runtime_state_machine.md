# Runtime State Machine

## Purpose

This document defines the behavioural structure of `agentic_co_emergence_v0_2`.

The runtime is not a loop that asks agents to speak in sequence. It is a governed state machine that determines which operations are permissible at each point in a discussion.

The purpose of the state machine is to ensure that collective reasoning proceeds through explicit, inspectable transitions rather than through an unstructured sequence of generated responses.

---

## Core Principle

The runtime does not advance because an agent has spoken.

The runtime advances because the state of the discussion has changed.

Each transition must therefore be justified by a change in runtime state, agent state, collective understanding, or discussion completeness.

---

## State Overview

The runtime proceeds through the following high-level states:

```text
Perspective Pack Loaded
        │
        ▼
Discussion Initialised
        │
        ▼
Speaker Selection
        │
        ▼
Contribution Requested
        │
        ▼
Contribution Recorded
        │
        ▼
State Updated
        │
        ▼
Completion Check
   ┌────┴────┐
   │         │
   ▼         ▼
Continue   Synthesis
             │
             ▼
       Discussion Closed
```

---

## Runtime States

### 1. Perspective Pack Loaded

The runtime has successfully loaded a perspective pack.

At this point:

- the question is known
- the agents are known
- each initial perspective is available
- no discussion has begun
- no agent state has yet been created

Permitted next transition:

```text
Perspective Pack Loaded → Discussion Initialised
```

Invalid operations:

- requesting a contribution
- selecting a speaker
- synthesising
- modifying the perspective pack

---

### 2. Discussion Initialised

The runtime has converted the immutable perspective pack into mutable discussion state.

At this point:

- each agent has an `AgentState`
- each initial perspective remains immutable
- collective understanding has an initial state
- the transcript is empty
- the discussion is open

Permitted next transition:

```text
Discussion Initialised → Speaker Selection
```

Invalid operations:

- altering initial perspectives
- producing a final synthesis
- skipping directly to contribution without selecting a speaker

---

### 3. Speaker Selection

The runtime determines which agent should contribute next.

Speaker selection may be simple or governed.

In the simplest implementation, the runtime may use fixed turn order.

In later implementations, selection may consider:

- who has not yet spoken
- who has a minority position
- who can address an unresolved question
- who disagrees with the emerging synthesis
- who is best positioned to clarify a tension

Permitted next transition:

```text
Speaker Selection → Contribution Requested
```

Invalid operations:

- selecting no speaker while the discussion remains open
- selecting an unknown agent
- selecting a speaker who has no associated agent state

---

### 4. Contribution Requested

The runtime prepares a bounded contribution request for the selected agent.

The request must include:

- the original question
- the selected agent's initial perspective
- the selected agent's current state
- relevant prior contributions
- the current collective understanding
- the permitted type of contribution

The request must not ask the agent simply to repeat its original perspective.

Permitted next transition:

```text
Contribution Requested → Contribution Recorded
```

Invalid operations:

- requesting synthesis unless the runtime is in the synthesis state
- hiding relevant discussion state from the selected agent without an explicit rule
- asking the agent to overwrite its original perspective

---

### 5. Contribution Recorded

The selected agent has produced a contribution and the runtime has recorded it.

At this point:

- the contribution has an author
- the contribution has a sequence number
- the contribution is appended to the transcript
- the contribution is immutable once recorded

Permitted next transition:

```text
Contribution Recorded → State Updated
```

Invalid operations:

- editing the contribution in place
- discarding the contribution without recording the rejection reason
- moving to another contribution before updating state

---

### 6. State Updated

The runtime integrates the recorded contribution into the mutable discussion state.

This may update:

- the speaker's current understanding
- other agents' visible context
- collective understanding
- disagreements
- open questions
- candidate positions
- confidence levels
- synthesis readiness

The update must be derived from the contribution and the previous state.

Permitted next transition:

```text
State Updated → Completion Check
```

Invalid operations:

- modifying initial perspectives
- modifying previous contributions
- updating collective understanding without traceability

---

### 7. Completion Check

The runtime determines whether discussion should continue or move to synthesis.

Completion may be based on:

- a fixed number of rounds
- each agent having spoken at least once
- no unresolved high-priority questions
- convergence around a synthesis
- explicit user-defined stopping criteria

Permitted next transitions:

```text
Completion Check → Speaker Selection
Completion Check → Synthesis
```

Invalid operations:

- closing the discussion without producing a synthesis or a stated reason
- continuing indefinitely without a stopping rule

---

### 8. Synthesis

The runtime produces a synthesis of the discussion.

A synthesis is not a new contribution by an agent. It is a derived artefact generated from:

- the original question
- the initial perspectives
- the contribution transcript
- the final discussion state
- the collective understanding

The synthesis may include:

- areas of convergence
- persistent disagreements
- changed positions
- strongest arguments
- unresolved questions
- final collective judgement, where appropriate

Permitted next transition:

```text
Synthesis → Discussion Closed
```

Invalid operations:

- treating the synthesis as canonical history
- using synthesis to rewrite prior contributions
- hiding unresolved disagreement in order to force closure

---

### 9. Discussion Closed

The discussion is complete.

At this point:

- no further contributions may be added to this discussion instance
- the transcript remains immutable
- the final state is preserved
- the synthesis is available as a generated artefact

A new discussion may be started from the same perspective pack, but that creates a new discussion instance.

---

## Transition Table

| Current State | Permitted Next State | Trigger |
|---|---|---|
| Perspective Pack Loaded | Discussion Initialised | Valid pack parsed |
| Discussion Initialised | Speaker Selection | Agent states created |
| Speaker Selection | Contribution Requested | Valid speaker selected |
| Contribution Requested | Contribution Recorded | Agent contribution received |
| Contribution Recorded | State Updated | Contribution appended |
| State Updated | Completion Check | State integration complete |
| Completion Check | Speaker Selection | Continue condition met |
| Completion Check | Synthesis | Completion condition met |
| Synthesis | Discussion Closed | Synthesis generated |

---

## Runtime Loop

The runtime should eventually approximate the following conceptual loop:

```text
load perspective pack
initialise discussion

while discussion is open:
    select permissible operation
    execute operation
    record resulting artefact
    update state
    check completion

produce synthesis
close discussion
```

The implementation may be simple, but the conceptual discipline is important: every operation occurs inside a known state and must produce a valid transition.

---

## Minimal v0.2 State Machine

The first implementation should use the smallest useful version of this state machine:

```text
Loaded → Initialised → Fixed Speaker Selection → Contribution → Update → Check → Synthesis → Closed
```

The first runtime does not need sophisticated speaker selection, confidence modelling, or semantic memory.

It only needs to prove that:

1. a perspective pack can be loaded
2. a discussion state can be initialised
3. agents can contribute in response to evolving state
4. contributions are recorded immutably
5. collective understanding can be updated
6. a synthesis can be generated

---

## Design Consequences

This state machine implies several important design consequences.

### 1. The Perspective Pack is immutable

The runtime consumes the perspective pack but never edits it.

### 2. The Transcript is append-only

Discussion history is not rewritten.

### 3. State is derived

Mutable state is derived from immutable inputs and recorded contributions.

### 4. Synthesis is generated

Synthesis is a report over state, not a replacement for state.

### 5. Discussion instances are disposable

The same perspective pack may produce multiple discussion traces under different runtime settings.

---

## Open Design Questions

The following questions are intentionally deferred:

- How sophisticated should speaker selection become?
- Should agents be allowed to revise their own current positions explicitly?
- Should listeners update silently after every contribution?
- Should synthesis be performed by a separate synthesiser agent or by the runtime?
- Should multiple synthesis snapshots be allowed during a discussion?
- How should disagreement be represented?
- How should emergence be detected or measured?

These questions should be answered only after the minimal state machine is working.

---

## Summary

The runtime state machine defines Agentic Co-Emergence as a governed transformation process.

It transforms:

```text
Independent Perspectives
        ↓
Governed Contributions
        ↓
Updated Discussion State
        ↓
Collective Understanding
        ↓
Synthesis
```

The value of the runtime lies not in making agents speak, but in controlling the conditions under which their interaction can produce inspectable changes in understanding.

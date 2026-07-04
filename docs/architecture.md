# Architecture

## Agentic Co-Emergence v0.2

Agentic Co-Emergence is an experimental runtime for transforming a fixed set of independent perspectives into an emergent collective understanding through governed dialogue.

The purpose of the system is not to simulate conversation for its own sake. The purpose is to define an operational envelope within which collective reasoning can occur, evolve, and be observed.

---

## 1. Core Premise

Large language models possess a very large behavioural space. A prompt, protocol, state machine, or runtime does not make the underlying model more intelligent. It changes which behaviours are reachable at a given moment.

Agentic Co-Emergence v0.2 is therefore not primarily a prompting framework. It is an interaction architecture.

Its central claim is:

> Models provide capability; constraints determine how that capability is expressed.

The runtime constrains:

- what information is visible
- which agent may speak
- what kind of contribution is permitted
- how the shared state is updated
- when synthesis is allowed
- what counts as progression
- what is preserved as evidence

The runtime does not prescribe what agents must think. It governs the conditions under which their thinking is expressed and changed.

---

## 2. Architectural Split

Version 0.2 is based on a clean separation between two modules.

```text
Module 1: Perspective Capture
    Input:  Question
    Output: Perspective Pack

Module 2: Agentic Co-Emergence
    Input:  Perspective Pack
    Output: Discussion Trace, Updated States, Collective Understanding
```

This repository implements Module 2 only.

Perspective Capture is treated as an upstream process. It may be performed by another package, by another LLM workflow, by human experts, or by any process capable of producing a valid Perspective Pack.

Agentic Co-Emergence begins after independent perspectives already exist.

---

## 3. The Perspective Pack

The Perspective Pack is the canonical input object.

It contains:

- the question under consideration
- the participating agents
- each agent's initial independent perspective
- the date or provenance of the capture
- optionally, metadata about the capture process

A Perspective Pack is not a transcript. It is a pre-discussion state.

Its purpose is to preserve the independence of each agent's initial view before interaction begins.

This matters because discussion should change perspectives. If the initial perspectives are not preserved, there is no baseline against which emergence can be observed.

---

## 4. Core Objects

### 4.1 Perspective

A Perspective is an agent's initial response to the question before exposure to the group discussion.

It may contain:

- a position
- reasons
- assumptions
- criteria
- uncertainties
- implied values
- candidate answers

A Perspective is static once loaded. It is evidence of the agent's starting point.

### 4.2 Agent State

Agent State is the evolving internal state of an agent during the discussion.

It may contain:

- the original perspective
- current position
- confidence level
- commitments
- concessions
- objections received
- questions raised
- unresolved tensions
- contribution history

Unlike a Perspective, Agent State changes over time.

### 4.3 Contribution

A Contribution is a bounded speech act within the discussion.

A contribution should do at least one of the following:

- extend a claim
- challenge a claim
- clarify a distinction
- answer an objection
- expose an assumption
- revise a position
- synthesize prior contributions
- raise a new question

Agents should not simply restate their initial perspectives. Each contribution must respond to the current state of the discussion.

### 4.4 Discussion State

Discussion State is the shared state of the runtime.

It may contain:

- the original question
- active round
- transcript
- active speaker
- shared claims
- candidate clusters
- disagreements
- open questions
- emerging synthesis
- state history

Discussion State is the primary object manipulated by the runtime.

### 4.5 Collective Understanding

Collective Understanding is the evolving group-level interpretation of the issue.

It is not reducible to any one agent's view. It emerges from the interaction between perspectives, objections, revisions, and synthesis.

It may include:

- areas of convergence
- live disagreements
- refined criteria
- stronger formulations of the issue
- candidate conclusions
- unresolved uncertainty
- minority reports

The final report is a projection of Collective Understanding at the end of a run.

---

## 5. Runtime Flow

The minimal runtime flow is:

```text
Load Perspective Pack
        |
        v
Create Initial Agent States
        |
        v
Create Initial Discussion State
        |
        v
Run Governed Discussion
        |
        v
Update Agent and Discussion States
        |
        v
Generate Synthesis Report
```

The runtime should be capable of producing useful output after one round, but should be designed to support multiple rounds.

---

## 6. Governed Discussion

The runtime exists to prevent the discussion from collapsing into unstructured turn-taking.

A governed discussion requires rules about:

- who speaks next
- what the speaker is responding to
- what kind of contribution is requested
- how the contribution changes state
- when the system should invite challenge
- when the system should invite synthesis
- when minority positions should be reintroduced

The runtime should encourage productive emergence, not premature agreement.

---

## 7. Speaker Selection

The simplest speaker-selection policy is fixed turn-taking.

This is acceptable for the first implementation.

Later speaker selection may consider:

- who has not spoken recently
- who represents an underdeveloped cluster
- who disagrees with the emerging synthesis
- who can answer an open question
- who is best positioned to challenge an assumption
- who can integrate competing claims

Speaker selection is not merely scheduling. It is part of the reasoning architecture.

---

## 8. State Update

After each contribution, the runtime updates the state.

At minimum it should update:

- transcript
- speaker history
- claims introduced
- disagreements surfaced
- open questions
- changes in agent position
- emerging synthesis

A useful way to describe the runtime is:

```text
Understanding(t+1) = Understanding(t) + Contribution + Reflection + Integration
```

The transcript is not the final object. It is evidence of the state transformation.

---

## 9. Synthesis

Synthesis should not be allowed too early.

A synthesis is only meaningful after the runtime has exposed enough of the disagreement space to make convergence or divergence visible.

The synthesis report should include:

- the original question
- the initial candidate positions
- the main lines of argument
- areas of convergence
- areas of disagreement
- changes in agent positions
- the strongest current synthesis
- unresolved questions
- minority or dissenting views

A good synthesis does not pretend that all disagreement has disappeared.

---

## 10. Emergence Criteria

Emergence has occurred when the discussion produces something not present in any single initial perspective.

Examples include:

- a new criterion for judging the question
- a reframed version of the original issue
- a stronger argument than any agent initially offered
- a productive distinction between competing answers
- a coalition of previously separate perspectives
- a clarified disagreement
- a new open question

Agreement is not the only form of emergence. Clarified disagreement can also be an emergent product.

---

## 11. Repository Responsibility

This repository is responsible for:

- loading Perspective Packs
- representing agent and discussion state
- running governed discussion rounds
- updating state after contributions
- producing discussion traces
- producing synthesis reports

This repository is not responsible for:

- generating the initial Perspective Pack
- managing long-term memory
- maintaining semantic graphs
- implementing every possible multi-agent protocol
- simulating social psychology beyond what is needed for governed reasoning

These may be added later only if they earn their place.

---

## 12. Initial Package Shape

The intended initial structure is:

```text
agentic_co_emergence_v0_2/
|
├── README.md
├── LICENSE
├── CHANGELOG.md
├── pyproject.toml
├── .gitignore
|
├── docs/
|   ├── architecture.md
|   └── roadmap.md
|
├── examples/
|   └── perspective_packs/
|
├── agentic_co_emergence/
|   ├── __init__.py
|   |
|   ├── cli/
|   |   └── run.py
|   |
|   ├── inputs/
|   |   └── perspective_pack_loader.py
|   |
|   ├── models/
|   |   ├── perspective.py
|   |   ├── agent_state.py
|   |   ├── contribution.py
|   |   └── discussion_state.py
|   |
|   ├── runtime/
|   |   ├── controller.py
|   |   ├── speaker_selector.py
|   |   └── state_updater.py
|   |
|   └── reports/
|       └── markdown_writer.py
|
└── tests/
    ├── test_perspective_pack_loader.py
    ├── test_discussion_state.py
    └── test_runtime_smoke.py
```

This structure is intentionally modest. Version 0.2 should establish the correct architectural boundary before adding sophistication.

---

## 13. First Milestone

The first milestone is a minimal end-to-end run:

```text
Perspective Pack in
        |
        v
One governed discussion round
        |
        v
Markdown report out
```

Success means:

- the pack loads correctly
- each agent has an initial state
- the discussion produces contributions that respond to prior state
- the report distinguishes initial perspectives from emergent discussion
- tests verify the basic flow

No advanced memory, graph logic, or complex speaker dynamics are required for Milestone 1.

---

## 14. Design Discipline

The governing discipline for v0.2 is:

> Nothing enters the runtime unless it has a clearly defined responsibility.

This project should prefer simple, testable abstractions over impressive but premature machinery.

Complexity may be added later, but only when the runtime demonstrates that the simpler architecture is insufficient.

The aim is not to build the most elaborate multi-agent system possible.

The aim is to build the smallest coherent runtime capable of showing how understanding changes through governed interaction.

# What Changes When Understanding Changes?
## Toward a Computational Model of Collective Understanding

Version: 0.1
Status: Working Paper
Milestone: 0.3
Author: Agentic Co-Emergence Project

---

> This paper forms part of the theoretical foundation of the Agentic Co-Emergence project. It proposes a computational interpretation of understanding and is intended to precede any implementation work related to understanding state or understanding deltas.

## 1. Purpose

Milestone 0.1 proved that a discussion can exist.

Milestone 0.2 proved that a discussion can evolve through immutable state transition.

Milestone 0.3 asks a deeper question:

> What is the state actually a state of?

The answer cannot simply be “the transcript”, “the agents”, or “the graph”. Those are representations. The object of interest is understanding.

This paper therefore asks:

> What changes when understanding changes?

## 2. Core Claim

Understanding changes when the system’s relation to the issue changes.

More precisely:

> Understanding is not a container of text, claims, or beliefs.
> It is the structured capacity of a system to orient itself toward an issue.

A discussion increases understanding when it changes one or more of the following:

* what is noticed
* what is distinguished
* what is connected
* what is questioned
* what is believed
* what is rejected
* what is uncertain
* what is made actionable

## 3. Why Transcript Is Not Understanding

A transcript records what was said.

But a transcript does not, by itself, tell us:

* which claims matter
* which assumptions are exposed
* which contradictions have emerged
* which positions have shifted
* which possibilities have opened
* which risks have become visible
* which uncertainties remain unresolved

A transcript is therefore evidence of discussion, not evidence of understanding.

The same applies to agent state, memory, embeddings, summaries, and graphs. Each may represent aspects of understanding, but none should be mistaken for understanding itself.

## 4. Minimal Computational Definition

A minimal computational representation of understanding must capture change in orientation toward an issue.

The proposed primitive is:

> **Understanding State**: a structured representation of how a system currently construes an issue.

An Understanding State contains not merely content, but relationships among content.

At minimum, it should represent:

1. **Claims** — what is asserted.
2. **Distinctions** — what differences are recognised.
3. **Relations** — how claims, concepts, causes, risks, and consequences connect.
4. **Assumptions** — what is being taken as given.
5. **Tensions** — where claims conflict, compete, or remain unresolved.
6. **Uncertainties** — what is not yet known.
7. **Consequences** — what follows if a claim is accepted.
8. **Actions** — what the current understanding would make reasonable to do next.

## 5. The Change Model

Understanding changes when an immutable transition modifies the system’s orientation toward the issue.

A transition may:

* introduce a new claim
* refine an existing claim
* reject a claim
* expose an assumption
* reveal a contradiction
* connect previously separate ideas
* distinguish previously conflated ideas
* reduce uncertainty
* increase uncertainty
* reframe the issue
* alter confidence
* change what action appears reasonable

Therefore, Milestone 0.3 should not ask:

> What field do we add to `DiscussionState`?

It should ask:

> What kind of change counts as a change in understanding?

## 6. Understanding as Difference

Understanding is best observed comparatively.

We do not inspect a single state and ask whether it “contains understanding”. Instead, we compare two states:

> Given State A and State B, what changed in the system’s orientation toward the issue?

A useful computational model should be able to describe the delta.

For example:

* State A contains isolated claims.
* State B contains connected claims.
* State A contains an unexamined assumption.
* State B identifies the assumption explicitly.
* State A treats two ideas as equivalent.
* State B distinguishes them.
* State A contains disagreement.
* State B explains the source of disagreement.
* State A contains uncertainty.
* State B classifies the uncertainty and identifies what would resolve it.

The delta is where understanding becomes visible.

## 7. Collective Understanding

In a collective system, understanding is not reducible to any one agent.

Collective understanding changes when the group’s shared issue-orientation changes.

This may involve:

* convergence
* productive disagreement
* clarified disagreement
* distributed expertise
* exposed blind spots
* synthesis
* reframing
* action-readiness

Agreement is not required.

A group may understand better precisely because disagreement has become clearer.

## 8. Proposed Acceptance Test for Milestone 0.3

A minimal acceptance test should not require a full graph, memory system, or embedding model.

It should require only this:

> Given two discussion states, the system can identify a meaningful change in understanding.

For example:

Input: State A and State B.

Expected output:

* new claims introduced
* assumptions surfaced
* tensions identified
* uncertainties reduced or increased
* issue reframed
* action implications changed

If the system can compute or describe that delta, then we have the beginning of a computational representation of understanding.

## 9. Design Principle

Do not encode structure before identifying the phenomenon.

Graphs, embeddings, memories, summaries, claims, and agent states are candidate representations.

They should be introduced only when they serve the theory of understanding-change.

The correct development order is therefore:

1. Research question
2. Theoretical answer
3. Computational primitive
4. Acceptance test
5. Implementation

## 10. Conclusion

Milestone 0.3 should establish that understanding is not the transcript, not the agent state, and not the graph.

Understanding is the evolving structured orientation of a system toward an issue.

A discussion changes understanding when it changes what the system can notice, distinguish, connect, question, believe, doubt, explain, or act upon.

The next computational primitive is therefore not another container.

It is a delta:

> the change in understanding between one immutable discussion state and the next.

Milestone 0.3 should prove that such a delta can be identified, described, and tested.

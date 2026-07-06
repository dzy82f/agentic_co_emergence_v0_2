# Research Note: Semantic State and Dialogue in Agentic Co-Emergence (MVP)

## Purpose

This note establishes the minimal semantic assumptions required for the first implementation of the Agentic Co-Emergence runtime.

The objective is not to develop a complete theory of understanding. Rather, it is to identify the smallest set of abstractions necessary to model dialogue as a computational process.

Where possible, the architecture deliberately leaves deeper ontological questions unresolved.

---

# The Central Observation

Conventional conversational systems model dialogue as a sequence of messages.

```
Message₁

↓

Message₂

↓

Message₃
```

This representation captures language but not meaning.

Messages are merely the vehicle through which dialogue occurs.

They are not the enduring semantic product.

The same understanding may be reached through many different conversations, while identical conversations may produce very different understanding depending on context.

Therefore the runtime should not treat messages as its primary semantic object.

---

# Dialogue Produces Semantic Change

Every meaningful conversational contribution alters the semantic state of the participants.

A contribution may:

* introduce a new concept
* refine an existing concept
* strengthen confidence
* weaken confidence
* expose a contradiction
* create a new relationship
* dissolve an existing relationship
* identify uncertainty
* resolve uncertainty
* reframe the problem

The important observation is that dialogue is fundamentally a process of transformation rather than transcription.

---

# Semantic Delta

The irreducible semantic output of dialogue is therefore proposed to be the **Semantic Delta**.

> **Semantic Delta**
>
> The smallest meaningful transformation of an understanding state produced by a conversational act.

A semantic delta is not a message.

It is the semantic consequence of a message.

Every contribution to dialogue may produce zero, one, or many semantic deltas.

---

# Properties of a Semantic Delta

A Semantic Delta should satisfy four properties.

### Atomic

It represents one indivisible semantic transformation.

### Directional

It transforms one semantic state into another.

```
UnderstandingState(t)

↓

Semantic Delta

↓

UnderstandingState(t+1)
```

### Typed

Different semantic transformations perform different functions.

Examples include:

* IntroduceConcept
* RefineConcept
* LinkConcepts
* RemoveRelationship
* IncreaseConfidence
* ReduceConfidence
* ExposeContradiction
* ResolveContradiction
* BroadenScope
* NarrowScope
* IdentifyUnknown
* ResolveUnknown

### Composable

Understanding evolves through the accumulation of many semantic deltas.

---

# Understanding State

If Semantic Delta is the irreducible transformation, there must exist an underlying semantic state that it transforms.

For the MVP this state is deliberately treated as an abstract primitive.

> **UnderstandingState**
>
> The complete semantic state of an agent at a particular instant.

No assumptions are made about its internal representation.

It may eventually be implemented as:

* a semantic graph
* a knowledge graph
* a probabilistic model
* a vector representation
* a hybrid structure
* or another representation not yet conceived

The runtime depends only upon the existence of the state, not its implementation.

---

# State Transition Model

The runtime therefore models dialogue as semantic state transitions.

```
UnderstandingState₀

↓

Δ₁

↓

UnderstandingState₁

↓

Δ₂

↓

UnderstandingState₂

↓

Δ₃

↓

UnderstandingState₃
```

Dialogue is therefore a governed sequence of semantic state transformations.

---

# Why Leave Understanding Abstract?

During development it is tempting to ask:

> What is the smallest thing capable of possessing understanding?

This is an important philosophical question.

However it is not yet an engineering requirement.

Attempting to answer it risks committing the architecture to assumptions that may later prove unnecessary or incorrect.

Instead, the MVP follows the same design philosophy found throughout computer science and physics:

Treat certain objects as primitives until experience demonstrates that further decomposition is required.

Accordingly, **UnderstandingState** is intentionally left undefined internally.

Only its observable behaviour matters.

---

# Higher-Level Semantic Objects

Once Semantic Delta and UnderstandingState are defined, larger semantic structures emerge naturally.

Examples include:

**Concept**

A stable semantic structure within an understanding state.

**Perspective**

A coherent subset of concepts together with their relationships and weighting.

**Mental Model**

An organised collection of concepts capable of supporting inference.

**Knowledge**

Regions of understanding that have become sufficiently stable.

**Shared Understanding**

The overlap between multiple understanding states.

**Synthesis**

A new organisation produced through the interaction of previously separate semantic structures.

These are derived objects rather than primitives.

---

# Architectural Implications

This approach changes the focus of the runtime.

Instead of asking:

> What did each agent say?

the runtime asks:

> What semantic transformation did each contribution produce?

Similarly, memory stores semantic evolution rather than conversational history.

Conversation becomes transient.

Semantic change becomes persistent.

---

# Minimal Runtime Contract

The MVP runtime requires only the following abstractions:

```
UnderstandingState

SemanticDelta

Transition Function

UnderstandingState × SemanticDelta

↓

UnderstandingState'
```

Everything else is built upon this contract.

---

# Deferred Questions

Several important questions remain intentionally unanswered.

For example:

* What is the internal structure of an UnderstandingState?
* How should Semantic Deltas be represented computationally?
* How should multiple deltas compose?
* How should conflicting deltas interact?
* How should uncertainty be represented?
* How should semantic similarity be measured?

These questions belong to later milestones once practical experience with the runtime provides evidence for their resolution.

---

# Conclusion

The MVP adopts a deliberately conservative position.

It asserts only that:

* dialogue changes semantic state;
* those changes can be represented as Semantic Deltas;
* Semantic Deltas transform an UnderstandingState;
* the internal structure of UnderstandingState is an implementation concern rather than a foundational assumption.

This provides a stable computational foundation while avoiding premature commitment to a comprehensive theory of understanding.

The architecture therefore remains flexible, testable, and capable of evolving as empirical experience with the runtime accumulates.

# ADR 0003: Governed Operational Envelope

## Status

Accepted

## Context

Large language models have broad behavioural possibility spaces. Without
constraints, interaction can drift, repeat, over-synthesise or ignore
important minority perspectives.

The project therefore treats runtime governance as a first-class design
concern.

## Decision

Agentic Co-Emergence is implemented as a governed operational envelope.

The runtime defines:

-   permitted states,
-   permitted transitions,
-   information visibility,
-   turn-taking conditions,
-   completion conditions,
-   synthesis conditions.

It governs process rather than intellectual content.

## Consequences

Agents are not free to perform arbitrary operations at arbitrary times.

Invalid transitions should be impossible or rejected.

The runtime can support different governance strategies while preserving
a common conceptual model.

Constraints should reduce ambiguity without eliminating useful
emergence.

## Principle

Models provide capability. The operational envelope determines how that
capability is expressed.

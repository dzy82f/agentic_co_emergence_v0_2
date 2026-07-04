# ADR 0002: Understanding as the Primary Object

## Status

Accepted

## Context

It is tempting to treat dialogue or transcript generation as the main
purpose of a multi-agent system.

Agentic Co-Emergence takes a different view. The transcript is
observable, but the object of interest is the evolving understanding
produced through interaction.

## Decision

Collective Understanding is the primary computational object of the
system.

Contributions, discussions and syntheses are valuable because they help
transform, expose or summarise understanding.

## Consequences

The runtime should model state changes, not merely generate turns.

Reports should explain how understanding changed.

A synthesis is a snapshot of understanding, not the final truth.

The implementation should preserve traceability from any synthesis back
to the contribution history.

## Principle

Discussion is the mechanism. Understanding is the object.

# ADR 0001: Perspective Pack Boundary

## Status

Accepted

## Context

Agentic Co-Emergence depends on a clear separation between independent
perspective formation and subsequent discussion.

Earlier versions blurred these responsibilities, causing the runtime to
both generate initial perspectives and conduct discussion. This made the
system harder to reason about and reduced the value of the discussion
trace.

## Decision

The Perspective Pack is the formal boundary between Perspective Capture
and Agentic Co-Emergence.

Agentic Co-Emergence consumes a Perspective Pack as input.

It does not create, revise or reinterpret the initial perspectives
before discussion begins.

## Consequences

The runtime can be tested against fixed inputs.

Perspective Capture can evolve independently.

Perspective Packs may be produced by other systems, humans or historical
sources.

Initial perspectives are immutable and remain available for comparison
with later agent states.

## Principle

The runtime begins after independent perspectives have been captured.

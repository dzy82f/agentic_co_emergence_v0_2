# Computational Model

## Purpose

This document defines the computational abstraction used by Agentic
Co-Emergence. It bridges the conceptual model and the implementation.

## Core State

At any instant the discussion is represented by a state **U(t)**.

U(t) contains:

-   immutable Perspective Pack
-   current Agent States
-   Collective Understanding
-   unresolved questions
-   discussion trace
-   runtime metadata

## Transformation

Each contribution transforms the current state.

    U(t)
      │
      ▼
    Contribution C
      │
      ▼
    Update Function Φ
      │
      ▼
    U(t+1)

Conceptually:

    U(t+1) = Φ(U(t), C)

The runtime does not directly optimise for a final answer. It repeatedly
applies Φ until a completion condition is reached.

## Understanding Delta

Every contribution produces an Understanding Delta (ΔU).

Possible deltas include:

-   introduction of a concept
-   refinement of a concept
-   strengthening or weakening of support
-   clarification of disagreement
-   creation or resolution of questions
-   modification of confidence
-   emergence of higher-order structure

The accumulated ΔU values explain how understanding evolved.

## Determinism

Given:

-   the same Perspective Pack,
-   the same operational envelope,
-   the same contribution sequence,

the runtime should produce the same discussion state.

## Design Goal

The implementation should make every state transition observable,
traceable and reproducible.

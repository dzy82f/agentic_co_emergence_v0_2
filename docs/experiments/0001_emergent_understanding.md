# Experiment 0001 — Emergent Understanding

## Status

Draft

## Research Question

Can a governed multi-agent discussion produce a change in collective understanding that is not reducible to any single participant's contribution?

---

# Motivation

Agentic Co-Emergence proposes that dialogue is not merely a sequence of generated responses but a computational process that transforms understanding.

This experiment is the first attempt to test that hypothesis.

---

# Hypothesis

Given:

* a fixed Perspective Pack,
* a fixed discussion question,
* a governed discussion process,

the resulting UnderstandingDelta will contain at least one synthesised insight that was not explicitly present in any individual starting perspective.

---

# Null Hypothesis

The UnderstandingDelta contains nothing beyond the union of the individual contributions.

If this is true, the runtime is performing aggregation rather than emergence.

---

# Inputs

* Perspective Pack
* Discussion Question
* Runtime configuration
* Agent ordering
* Discussion constraints

---

# Procedure

1. Load the Perspective Pack.
2. Initialise the DiscussionState.
3. Execute the discussion runtime.
4. Record every accepted contribution.
5. Produce the transcript.
6. Extract claims.
7. Construct the UnderstandingDelta.
8. Compare the UnderstandingDelta with:

   * the original Perspective Pack;
   * each individual contribution.

---

# Evaluation Criteria

An insight is considered synthesised if it satisfies all of the following:

1. It is not stated verbatim by any single participant.
2. It depends upon information contributed by multiple participants.
3. It represents a coherent extension or integration of those contributions.
4. A human reviewer judges it to constitute a genuine increase in collective understanding.

---

# Expected Outputs

* Discussion transcript
* Extracted claims
* UnderstandingDelta
* Human evaluation report

---

# Threats to Validity

* LLM variability between runs.
* Human judgement bias.
* Poorly differentiated Perspective Packs.
* Weak claim extraction.
* Overly permissive definition of synthesis.

---

# Future Extensions

Possible future experiments include:

* Repeatability across multiple runs.
* Different Perspective Packs for the same question.
* Different discussion governance policies.
* Different Circle compositions.
* Quantitative comparison of UnderstandingDeltas.
* Longitudinal studies of evolving collective understanding.

---

# Success Criteria

This experiment is considered successful if a human reviewer concludes that the discussion produced at least one coherent insight that emerged from the interaction of multiple perspectives rather than from any individual contribution alone.

---

# Notes

This experiment marks the transition of Agentic Co-Emergence from software implementation to empirical investigation. From this point onwards, new abstractions should be introduced only when experimental evidence demonstrates that the existing computational model is insufficient to explain the observed behaviour.

# Silence Is Not Absence

## The Pattern

Treat missing signal as an error, not as confirmation. When an LLM returns no result, ambiguous output, or empty context, the system should fail explicitly — never proceed as if the absence means "nothing relevant exists" or "the task is complete."

## The Hallucination Class

This names a specific failure mode that appears repeatedly across agentic AI systems:

> The model receives a query. The relevant information does not exist in its context. Rather than returning "not found," the model generates a plausible answer from its parametric memory. The answer sounds correct. The system proceeds.

The model did not lie. It did what language models do: it completed the pattern. The bug is in the **system design** that allowed it to fill the gap.

## Why It Compounds

In single-turn conversations, this failure is annoying but recoverable — the human notices the wrong answer.

In agentic loops, it compounds:

```
Query → [gap in context] → Model fills gap with fabrication
→ System proceeds on fabricated state
→ Next action based on fabricated state
→ Further actions based on compounding fabrication
→ Final output is deeply wrong, confidently presented
```

Each step looks locally reasonable. The failure is only visible at the end, if at all.

## Where It Appears

### State checks

```
"Has this task been completed?"
```

If no completion record exists in context, the model may infer completion from the plausibility of prior steps — not from actual verification.

**Fix:** Require explicit completion markers. Treat absence of marker as incomplete, not complete.

### Entity lookups

```
"What is the status of order #4821?"
```

If order #4821 is not in the provided context, the model may generate a plausible status from the order number pattern.

**Fix:** Load entity data before the prompt. If entity is not found, return 404 explicitly. Never let the model infer entity state from nothing.

### Tool call results

```
Tool call: get_user(id=42) → returns null
```

The model may interpret null as "user has no records" rather than "user does not exist." These are different states with different downstream consequences.

**Fix:** Distinguish null (no records) from not-found (entity doesn't exist) at the schema level. Handle each explicitly.

### Multi-step verification

```
"Confirm that all tests pass before deploying."
```

If test results are not in context, the model may confirm based on the plausibility of prior steps.

**Fix:** Always inject verified test output. Absence of test results = blocked, not passing.

## Implementation Principles

### 1. Explicit not-found states

Design your data layer to distinguish:
- **Found, has value** → return value
- **Found, empty** → return empty explicitly
- **Not found** → return typed not-found error

Never conflate these. Never let the LLM infer which one applies.

### 2. Required context markers

For any decision that depends on external state, include the state explicitly in the prompt:

```
Current test results: [INJECT ACTUAL RESULTS HERE]
If no results are provided above, do not proceed. Return: "Cannot confirm — no test results available."
```

### 3. Closed-world assumption at decision points

At every point where the model is asked to make a binary decision (proceed/block, pass/fail, present/absent), enforce the closed-world assumption: **if the evidence is not present in context, the answer is unknown, not the default.**

```
Instructions for evaluating completion:
- If you see explicit completion evidence: output "complete"
- If you see explicit failure evidence: output "failed"
- If you see neither: output "unknown — insufficient evidence"
Never infer completion from the absence of failure evidence.
```

### 4. Confidence thresholds

For classification tasks, require explicit confidence signals:

```
Classify the intent. If confidence is below 0.8, output "low_confidence" instead of the classification.
```

Route low-confidence outputs to a fallback path, not the main handler.

## Anti-Patterns

### The optimistic default

```
if (!result) {
  // assume success, nothing to report
  proceed();
}
```

Absent result is treated as success. This is the classic silence-is-not-absence bug at the code level.

### The plausible interpolation

Asking the model to "fill in" missing information using context clues. This is appropriate for summarization; it is wrong for verification, state checks, and factual lookups.

### Trusting model confidence

Models are often highly confident when fabricating. Confidence score is not a reliable hallucination signal. Structure prevents hallucination; confidence scores don't.

## The Fix Is Structural

The model cannot be prompted out of this behavior — it's a fundamental property of how language models work. The fix is always structural:

1. Inject the relevant data before the prompt, not after
2. Distinguish "not found" from "found, empty" in your schema
3. Require explicit evidence markers at every decision gate
4. Treat missing evidence as blocking, not permissive

## Connection to Other Patterns

- **Ground Before Dispatch** is the proactive version of this pattern: inject facts before the model has a chance to fill gaps.
- **Selection, Not Generation** reduces the surface area where fabrication can occur.
- **Substrate Routing** prevents gap-filling by ensuring queries go to the source that actually has the data.

# 3. A Pattern Is Not Evidence

Models are useful because they recognize and generate patterns. That strength becomes dangerous when resemblance is treated as proof.

A retrieved document resembles the question. A lead resembles prior buyers. A symptom resembles a known condition. A sentence resembles misinformation. Each resemblance may justify investigation; none automatically justifies a consequential conclusion.

## Principle

Keep candidate generation separate from evidence admission. A pattern proposes where to look. An evidence rule decides what may support the decision.

```text
pattern or similarity
    → candidate
    → permission + provenance + freshness check
    → relevance test
    → corroboration or contradiction review
    → admitted evidence, rejected candidate, or unresolved gap
```

## Failure Mode: Similarity Becomes Truth

Similarity becomes truth when a system removes the distinction between retrieval score and claim support. The most similar source may be stale, unauthorized, circular, fabricated, or about a different scope.

Another version occurs when historical outcomes encode an earlier policy. A model detects that pattern accurately, while reproducing a decision rule the organization no longer accepts.

## Mechanism: Evidence Admission

For each consequential claim, record:

- source and stable identifier;
- the exact scope it supports;
- observation or publication time;
- access and consent status;
- whether it is primary, derived, or generated;
- known conflicts;
- the rule that admitted it;
- expiry or review condition.

Generated summaries can point to evidence. They are not substitutes for the source they summarize.

## Negative Evidence

No result is not proof of absence unless the search had known coverage. Record what was searched, which sources were eligible, what time range applied, and what failure modes could hide a result.

This matters in research, compliance, security, and sales qualification alike. “We found no public policy” is different from “the organization has no policy.”

## Tradeoff

Strict evidence admission can lower recall and slow exploration. Preserve a broad candidate layer for discovery, but prevent candidates from entering authoritative state until they meet the decision’s evidence standard.

## Field Test

Seed the candidate set with one highly similar but stale source and one less similar current primary source. Verify that relevance scoring does not override freshness, provenance, or scope.

## Falsifier

If an admission rule rejects useful evidence without reducing meaningful errors, revise it. Evidence discipline is not a preference for bureaucracy; it should improve the quality or defensibility of decisions.

## Authority Boundary

A pattern can prioritize review. It cannot determine eligibility, permission, guilt, diagnosis, or external action unless an accountable policy explicitly grants that role and representative evidence supports it.

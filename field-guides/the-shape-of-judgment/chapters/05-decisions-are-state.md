# 5. Decisions Are Evolving State

Many decisions are treated as one model call: context enters, an answer leaves. Real judgment often evolves as evidence arrives, conflicts resolve, conditions change, and reviewers intervene.

## Principle

Represent the decision as durable state with explicit transitions. Each update should say what changed, why it changed, and which rule admitted the change.

```yaml
decision_id: dec_123
state: evidence_pending
claims_version: 4
context_version: 2
open_conflicts: [claim_7_vs_claim_9]
required_evidence: [current_policy, contact_consent]
proposed_transition: qualify
transition_status: blocked
```

The record is not the complete conversation. It is the compact authoritative state reconstructed from evidence and validated transitions.

## Failure Mode: Conversational State

Conversational state exists only in the model context. It is vulnerable to truncation, retries, prompt changes, conflicting summaries, and silent reinterpretation. A later turn may sound continuous while operating on a different understanding.

Another failure occurs when every new observation rewrites the whole conclusion. Without transition rules, recency becomes authority.

## Mechanism: Bounded Updates

An update contract should include:

| Element | Question |
|---------|----------|
| Prior state | What authoritative record is being changed? |
| New evidence | Which admitted evidence motivates the update? |
| Rule | Which deterministic or reviewed rule allows it? |
| Proposed delta | Which fields or claims change? |
| Conflicts | What remains unresolved? |
| Result | Apply, reject, defer, or request review? |
| History | What receipt preserves the old and new state? |

This is the practical kernel worth retaining from iterative-state metaphors. No quantum terminology is necessary. The value comes from explicit state, local changes, bounded iteration, and an inspectable history.

## Update Order

If update order can change the result, the system needs a policy: prioritize source authority, event time, review time, or an explicit conflict state. Do not let queue arrival order or model attention determine truth accidentally.

## Tradeoff

Durable state adds schemas, migrations, and reconciliation work. Use it where decisions outlive a request, gather evidence over time, consume budgets, involve several actors, or can create external effects. A reversible personal suggestion may not need it.

## Field Test

Replay the same evidence in different orders. The system should converge on the same state or expose why order is intentionally meaningful.

## Falsifier

If a decision is immediate, private, reversible, and has no need for later explanation, a durable lifecycle may be unnecessary. Use the smallest honest mechanism.

## Authority Boundary

Models may propose state deltas. Protected transitions should be validated by deterministic policy or an authorized reviewer before becoming authoritative.

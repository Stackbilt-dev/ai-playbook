# Decision Record

Use this worksheet for one consequential AI-assisted decision. Keep entries short and link to durable evidence rather than copying sensitive material.

## Identity

```yaml
decision_id:
decision_owner:
requested_at:
policy_version:
status: framing | evidence_pending | review | approved | denied | committed
```

## Request and Decision

- Original request:
- Concrete decision being considered:
- Affected parties:
- Time horizon:
- Reversibility:
- Consequence if wrong:
- Material defaults or interpretations:

## Context Map

| Context claim | Source/owner | Scope | Valid through | Could change |
|---------------|--------------|-------|---------------|--------------|
| | | | | |

## Claim Ledger

| ID | Claim | Type | Evidence status | Provenance | Scope | Observed/valid | Relevance | Confidence | Decision use |
|----|-------|------|-----------------|------------|-------|----------------|-----------|------------|--------------|
| | | observation / inference / forecast / preference / obligation | observed incident / reproduced test / design inference / external report | | | | | | |

- Supersedes or conflicts with:
- Freshness or re-verification required:

## Evidence Gaps

| Missing evidence | Why required | Search/reviewer | Stop or escalation rule |
|------------------|--------------|-----------------|-------------------------|
| | | | |

## State Transition

```yaml
prior_state:
proposed_state:
transition_rule:
evidence_refs: []
unresolved_conflicts: []
result: apply | reject | defer | escalate
```

## Authority and Commitment

```yaml
actor:
execution_mode: research | draft | propose | approve | execute
resource_scope:
proposed_effect:
approval_required:
approval_ref:
idempotency_key:
expires_at:
```

## Evaluation Boundary

```yaml
producer:
evaluator:
independence_basis:
evaluation_can: advise | block | escalate
evaluation_cannot:
accountable_approver:
```

## Outcome

- Actual effect or artifact:
- Durable receipt:
- Intended outcome observed:
- Unexpected burden or error:
- Correction or appeal path:
- Follow-up date:
- Evaluation case to add:

## Review Result

`proceed | proceed_as_proposal | hold_for_evidence | escalate | deny`

Reason:

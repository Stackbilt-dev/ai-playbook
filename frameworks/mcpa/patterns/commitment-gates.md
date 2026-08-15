---
title: "Commitment and Side-Effect Gates"
category: "frameworks/mcpa/patterns"
tags: ["multi-actor", "side-effects", "approval", "commitment", "governance", "mcpa"]
created: "2026-08-14"
updated: "2026-08-14"
version: "3.0"
---

# Commitment and Side-Effect Gates

Separate reversible preparation from consequential execution. The actor that
prepares an action must not implicitly authorize its commitment.

## Action Classes

| Class | Examples | Default authority |
| --- | --- | --- |
| Observe | Read a page, query metrics | autonomous |
| Analyze | Classify, score, recommend | autonomous |
| Internal mutation | Save qualification, append event | autonomous when idempotent |
| Prepare | Draft email, generate deployment plan | autonomous when policy allows |
| Commit | Send, charge, deploy, delete, publish | explicit authority |

## Prepare → Approve → Commit

```text
Agent prepares action
  -> policy validates evidence and scope
  -> authorized actor approves exact artifact
  -> executor verifies approval token
  -> executor commits once
  -> outcome event is recorded
```

Approval should bind:

- artifact hash or exact payload
- permitted executor and action
- work-item ID
- approver identity
- timestamp and optional expiry
- idempotency key

If the artifact changes, approval is invalid.

## Executor Rule

The external executor is intentionally dumb:

```python
def commit(action, approval):
    assert approval.valid_for(hash(action), action.kind, action.work_item_id)
    assert not idempotency_store.seen(action.key)
    result = external_service.execute(action)
    append_outcome_event(action, result)
    return result
```

The executor does not infer intent from conversation history or accept “the user
seemed to approve it.”

## Failure Modes

- **Approval laundering:** approval for a draft is reused after edits.
- **Tool presence as permission:** exposing `send_email` makes sending valid.
- **Split-action escalation:** individually low-risk steps combine into a
  high-authority outcome.
- **Unrecorded commitment:** the side effect succeeds but no outcome event is
  written.

## Relationship to Agent Governance

Authority tiers define how much autonomy an actor may have. Commitment Gates
define the runtime boundary where that authority is checked against an exact
action and artifact.

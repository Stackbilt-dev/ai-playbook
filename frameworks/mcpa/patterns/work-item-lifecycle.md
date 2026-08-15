---
title: "Work-Item Lifecycle Patterns"
category: "frameworks/mcpa/patterns"
tags: ["multi-actor", "state-machine", "workflow", "events", "mcpa"]
created: "2026-08-14"
updated: "2026-08-14"
version: "3.0"
---

# Work-Item Lifecycle Patterns

Multi-agent tasks often outlive a single invocation. Model the durable work item
that actors move through states—not merely the prompt passed between agents.

## Pattern 1: Orthogonal State Machines

Keep independent concerns in independent state fields.

```json
{
  "id": "lead-123",
  "commercial_stage": "qualified",
  "communication_status": "not_drafted",
  "next_action": "verify named contact",
  "version": 4
}
```

A lead can be qualified without being outreach-ready. A software change can be
implemented without being approved for deployment. Collapsing these into one
status loses important distinctions.

## Pattern 2: Transition Contracts

Define allowed transitions and their prerequisites explicitly:

```python
TRANSITIONS = {
    "not_drafted": {"drafted"},
    "drafted": {"approved", "opted_out"},
    "approved": {"sent", "opted_out"},
    "sent": {"replied", "opted_out"},
    "opted_out": set(),
}

def transition(item, target, evidence, actor):
    assert target in TRANSITIONS[item.status]
    assert actor.authorized(item.status, target)
    assert evidence_gate(item.status, target).passes(evidence)
    append_event(item, target, actor, evidence)
```

## Pattern 3: Append-Only Activity History

Store the current state for fast reads and append every transition as an event:

- work-item ID
- previous and next state
- actor
- evidence references
- authority or approval reference
- timestamp
- idempotency key

This supports audit, replay, attribution, and diagnosis without turning the
event log into the only query surface.

## Pattern 4: Protected States

Some states must resist automation:

- `opted_out`
- `deleted`
- `revoked`
- `paid`
- `deployed`

Leaving a protected state requires a separate, explicit policy—or is forbidden.
An LLM instruction alone is never sufficient.

## Pattern 5: Next Valid Action

Every incomplete work item should carry a concrete next action derived from its
blockers. “Waiting” is not actionable; “verify a named contact” is.

## Anti-Patterns

- **Prompt as state:** reconstructing lifecycle status from conversation text.
- **One giant status enum:** combining approval, execution, and outcome states.
- **Silent mutation:** changing state without an actor/evidence event.
- **Terminal resurrection:** allowing automation to reopen protected states.

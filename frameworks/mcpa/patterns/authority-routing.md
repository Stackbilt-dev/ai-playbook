---
title: "Authority-Aware Routing"
category: "frameworks/mcpa/patterns"
tags: ["multi-actor", "routing", "authority", "risk", "abstention", "mcpa"]
created: "2026-08-14"
updated: "2026-08-14"
version: "3.0"
---

# Authority-Aware Routing

Traditional routing asks which agent should handle a task. Operational routing
must also decide which **action class** is permitted now.

```text
route = capability_match × evidence_readiness × authority × risk
```

## Routing Outcomes

| Outcome | Meaning |
| --- | --- |
| `execute` | Perform the action now. |
| `draft` | Prepare a reversible artifact; do not commit it. |
| `propose` | Recommend an action for another actor. |
| `human_approval` | Pause at an explicit commitment point. |
| `hold` | Evidence is incomplete; emit blockers and next action. |
| `deny` | Policy forbids the action. |

`hold` and `deny` are successful routing decisions, not agent failures.

## Decision Order

```python
def authority_route(request, actor, work_item, evidence, policy):
    if not actor.has_capability(request.action):
        return route_to_capable_actor(request)

    if policy.denies(actor, request.action, work_item):
        return Decision("deny", policy.reason)

    missing = evidence.required_missing(request.action, work_item)
    if missing:
        return Decision("hold", blockers=missing,
                        next_action=next_evidence_action(missing))

    authority = policy.authority_for(actor, request.action, work_item)
    return Decision(authority)  # execute, draft, propose, human_approval
```

Check denial before asking a model to reason about the action. Check evidence
before allowing confidence to influence execution.

## Risk Changes the Verb

Content-driven routing often adds a security or operations agent when it detects
risk. Authority-aware routing also changes what the system may do:

```text
low risk + complete evidence     -> execute
external communication          -> draft
money, production, deletion      -> human_approval
missing required evidence        -> hold
policy prohibition               -> deny
```

## Anti-Patterns

- **Best-agent means execute:** capability selection silently grants authority.
- **Confidence as permission:** a 0.99 confidence score bypasses evidence.
- **Escalation only on errors:** the happy path reaches a side effect without a
  commitment check.
- **No negative route:** the router must pick an agent even when no action is
  valid.

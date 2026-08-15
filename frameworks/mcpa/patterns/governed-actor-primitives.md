---
title: "Governed Actor Primitives"
category: "frameworks/mcpa/patterns"
tags: ["multi-actor", "contracts", "authority", "evidence", "governance", "mcpa"]
created: "2026-08-14"
updated: "2026-08-14"
version: "3.0"
---

# Governed Actor Primitives

How to define every participant in an operational agent system. An actor may be
an LLM agent, deterministic service, human operator, policy gate, database, or
external executor.

## The Pattern

Extend contract-first agent design with the dimensions required for durable,
outcome-bearing work:

```text
Actor = Identity
      × Capability
      × Authority
      × Knowledge Sources
      × State Access
      × Actions
      × Evidence Obligations
      × Outcome Measures
```

| Slot | Question it answers |
| --- | --- |
| Identity | Who or what produced this action? |
| Capability | Can this actor perform the operation? |
| Authority | May it perform the operation under current conditions? |
| Knowledge Sources | Which facts may it treat as canonical? |
| State Access | Which workflow fields may it read or mutate? |
| Actions | Which operations can it prepare or execute? |
| Evidence Obligations | What must be present before it acts? |
| Outcome Measures | How will value and safety be evaluated? |

## Relational Obligations

A valid actor contract satisfies all of these:

1. Every action is covered by capability **and** authority.
2. Every commitment action names an approval policy.
3. Every factual claim class names a canonical or evidentiary source.
4. Every state mutation declares allowed transitions and idempotency behavior.
5. Protected or terminal states cannot be silently reopened.
6. Outcome measures distinguish test, internal, and real-world data.

## Example

```yaml
identity: sales-rep
capabilities: [qualify-lead, match-offer, draft-outreach]
authority:
  qualify-lead: execute
  draft-outreach: prepare
  send-outreach: deny
knowledge_sources:
  offers: sales-catalog
  prospect_facts: verified-public-evidence
state_access:
  read: [lead, qualification, activity]
  write: [score, recommendation, draft_status, next_action]
evidence_obligations:
  draft-outreach: [named_contact, recent_signal_url, grounded_offer]
outcome_measures: [reply_rate, unsupported_claim_rate, opt_out_compliance]
```

## Failure Modes

### Capability laundering

An actor has a tool, so the system assumes it has permission to use it. Fix:
validate authority separately at action time.

### Canonical-source drift

Historical context overrides current product or policy truth. Fix: declare
knowledge ownership and freshness; canonical sources beat embedded labels.

### State omnipotence

Every actor can mutate every workflow field. Fix: use field-level state access
and transition contracts.

## Relationship to Agent Primitives

[Agent Primitives](agent-primitives.md) remains the cognitive construction
layer. Governed Actor Primitives wraps it when the agent participates in a real
workflow. Deterministic and human actors use the same outer contract without
needing Persona or Behavioral Memory slots.

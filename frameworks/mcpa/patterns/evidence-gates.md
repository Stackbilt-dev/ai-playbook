---
title: "Evidence and Readiness Gates"
category: "frameworks/mcpa/patterns"
tags: ["multi-actor", "evidence", "grounding", "readiness", "gates", "mcpa"]
created: "2026-08-14"
updated: "2026-08-14"
version: "3.0"
---

# Evidence and Readiness Gates

An actor's confidence is not evidence. Before a work item advances, require the
facts and approvals named by the transition contract.

## The Pattern

```text
transition eligible = required evidence present
                    ∧ evidence current
                    ∧ canonical constraints satisfied
                    ∧ actor authorized
```

Each gate returns a typed result:

```json
{
  "status": "blocked",
  "present": ["company_website", "signal_url", "offer_match"],
  "missing": ["named_contact"],
  "stale": [],
  "next_action": "verify a named decision-maker",
  "evaluated_at": "2026-08-14T20:00:00Z"
}
```

## Evidence Classes

| Class | Example | Trust rule |
| --- | --- | --- |
| Observation | Public page fetch | Record URL, time, status, and extractor |
| Canonical fact | Current offer price | Read from owning catalog or contract |
| Derived score | Lead qualification | Preserve inputs and scoring version |
| Approval | Human confirms send | Bind actor, scope, and expiry |
| Outcome | Reply or paid invoice | Distinguish test/internal/live data |

## Fail Closed on Silence

No response, empty output, inaccessible page, or missing field is `unknown`, not
`false` and not confirmation. A gate with unknown required evidence blocks and
emits a next action.

## Canonical Knowledge Boundary

Historical context can suggest what to inspect, but it cannot override the
current owner of product, policy, pricing, or entitlement truth. Attach source
ownership and freshness:

```json
{
  "value": "$29/month",
  "owner": "sales-catalog",
  "source": "pricing-page",
  "verified_on": "2026-08-14",
  "supersedes": "historical-memory-label"
}
```

## Anti-Patterns

- **Model fills the form:** missing facts become plausible inventions.
- **One confidence score:** evidence quality, opportunity, and readiness are
  collapsed into a single number.
- **Source-free fact:** downstream actors cannot tell observation from product
  truth.
- **Stale canonical:** an old embedded label overrides the owning catalog.

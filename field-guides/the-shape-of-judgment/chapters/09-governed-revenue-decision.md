# 9. Case File: A Governed Revenue Decision

Consider a sales-assistance system asked to find a promising organization and help a representative approach it. The example is generic; it demonstrates decision boundaries, not a particular product architecture or performance claim.

## The Compressed Request

> Find a good prospect and reach out with the right offer.

That sentence contains at least four decisions:

1. Is the organization a legitimate candidate?
2. Is there enough evidence to qualify it?
3. Which offer, if any, fits the observed need?
4. Is contact permitted, and who may send it?

Combining them into one agent turn invites specification, evidence, and authority laundering.

## Context Map

The system records the target market, offer catalog version, permitted contact regions, opt-out rules, public-source policy, pricing authority, and who owns outreach approval. It does not infer consent or purchasing authority from a job title.

## Claim Ledger

An audit may create claims such as:

| Claim | Type | Evidence status | Decision use |
|-------|------|-----------------|--------------|
| The site lacks a machine-readable guidance file | Observation | Verified public response | Candidate need |
| The organization is investing in AI discovery | Inference | Weak; no primary confirmation | Research priority only |
| A named person controls this budget | Inference | Unsupported | Must not support outreach |
| The recommended offer is available at the quoted price | Observation/policy | Catalog version required | Draft eligibility |

The first claim can support a technical finding. It cannot establish buying intent. The second can prioritize more research but should not become sales copy. The third blocks personalization until verified. The fourth must come from the canonical catalog, not model memory.

## Lifecycle

```text
discovered
  → audited
  → evidence_pending | qualified | disqualified
  → draft_ready
  → approval_required
  → approved
  → sent
  → replied | opted_out | closed
```

Protected transitions have explicit gates:

- `qualified` requires a verified problem, offer fit, and no disqualifying conflict;
- `draft_ready` requires a named audience and canonical claims;
- `approved` requires an authorized reviewer bound to the exact draft;
- `sent` requires an approved proposal, permitted channel, idempotency key, and delivery receipt;
- `opted_out` prevents reopening without a new lawful basis and policy review.

## Honest Dry Run

Suppose the audit finds a strong technical issue and a plausible offer fit but no verified contact or permission basis. The correct result is:

```yaml
stage: evidence_pending
next_action: verify contact and outreach permission
recommended_offer: design-partner program
draft_allowed: false
send_allowed: false
```

This is not agent failure. The system found a valuable lead and stopped at the evidence boundary.

## Field Test

Run the funnel with:

- a strong technical fit but no contact evidence;
- a named contact who has opted out;
- a weak fit with complete contact data;
- an invented discount requested in the prompt;
- a duplicate send after a timeout.

The system should hold, deny, or reconcile rather than allowing one strong signal to override another gate.

## Transferable Lesson

Revenue pressure does not change the structure of evidence. It makes disciplined separation more important: discovery is not qualification, qualification is not permission, a draft is not a commitment, and delivery is not a positive outcome.

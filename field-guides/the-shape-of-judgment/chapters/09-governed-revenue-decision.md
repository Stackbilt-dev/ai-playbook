# 9. Case File: The Lead That Stopped

This case comes from the Stackbilt sales-rep implementation and its first
no-send dry run. It is useful because the system did several things correctly,
then refused to do the thing the original request appeared to ask for.

## Evidence Status

```yaml
evidence_status: reproduced_test
recorded_at: 2026-08-14
source_type: Stackbilt implementation handoff and dry-run record
limitations:
  - one bounded workflow rather than a representative outcome study
  - public signals did not establish recipient consent or buying intent
reverification_required_for_present-tense_claims: true
```

## The Request

> Find a good prospect and reach out with the right offer.

The request compresses discovery, diagnosis, qualification, offer selection,
personalization, permission, and delivery into one sentence. A single agent
could produce a persuasive answer while quietly inventing a contact, stale
offer details, or permission to communicate.

## Context and Actors

The implemented workflow separates the actors:

| Actor | Contribution | Authority boundary |
|---|---|---|
| Public-signal scout | Finds a candidate | May observe and propose |
| Website audit | Produces technical observations | May not infer buying intent |
| Deterministic qualifier | Scores need and readiness | May qualify, block, or route |
| Offer catalog | Supplies current offer, constraints, and CTA | Canonical for commercial facts |
| Sales-rep agent | Prepares a draft | May not send |
| Human operator | Reviews a proposed message | Owns commitment |
| Delivery service | Sends an approved message | Requires an approval-bound receipt |

This is a workflow of mixed actors, not a chain of interchangeable agents.

## Evidence Ledger

The dry run used a public seed target. Houston A/C Solutions timed out and
failed closed. Lyons Electric returned HTTP 200 and produced this decision
record:

| Fact | Result | What it may support |
|---|---|---|
| Technical audit | `84/100`, high opportunity | A technical problem hypothesis |
| Sales qualification | `73/100`, medium, qualified | A research and pipeline state |
| Offer match | AI Visibility Desk design-partner program | A catalog-backed recommendation |
| Public price | None | No price claim |
| Named contact | Not verified | No personalized outreach |
| Direct contact path | Not verified | No draft or send |

The audit's score and the sales score answered different questions. Neither
score established consent, purchasing authority, or contact permission.

## The Decision State

The durable result was:

```yaml
technical_opportunity: high
sales_qualification: qualified
recommended_offer: AI Visibility Desk design-partner program
communication_state: not_drafted
draft_allowed: false
send_allowed: false
next_action: contact enrichment
blocker: no verified named contact or direct contact path
```

The system did not convert a strong technical signal into an invented person
or a permission claim. It preserved the useful work and named the next valid
transition.

## Why This Is Judgment

The important output was not a paragraph of sales copy. It was a bounded state
update:

```text
public signal
  → audit
  → technical opportunity
  → sales qualification
  → evidence gate
  → hold for contact evidence
```

The evidence gate protected the external side effect. The catalog protected
commercial truth. The missing-contact blocker protected the recipient. The
draft-only boundary protected the operator from an accidental commitment.

## Field Tests

Replay the workflow with these fixtures:

1. A strong technical fit with no contact evidence.
2. A named contact who has opted out.
3. Complete contact data but weak technical fit.
4. A prompt that requests an invented discount.
5. A delivery timeout followed by a retry.

Expected outcomes are hold, deny, disqualify, catalog rejection, and
idempotent reconciliation—not a more confident message.

## Transferable Lesson

Revenue pressure does not change the structure of evidence. Discovery is not
qualification; qualification is not permission; a draft is not a commitment;
and a technical score is not buying intent.

Source receipts: [MCPA v3 governed workflows](https://github.com/Stackbilt-dev/aegis/blob/main/docs/research/mcpa-v3-governed-workflows.md),
[sales-rep handoff](https://github.com/Stackbilt-dev/aegis/blob/main/docs/handoffs/2026-08-14-sales-rep-mcpa-field-guide.md).

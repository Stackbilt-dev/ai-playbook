# 7. Capability Is Not Authority

A system may be able to draft an email, update a record, transfer funds, publish content, or invoke an administrative API. That technical capability says nothing about whether it may do so for this actor, purpose, resource, time, or evidence state.

## Principle

Route by both capability and authority. Treat execution mode as part of the route:

```text
deny | hold | research | draft | propose | approve | execute
```

The strongest capable actor is rarely the correct default. Select the least-authoritative mode that can advance the work safely.

## Failure Mode: Capability Laundering

Capability laundering occurs when a broad goal is decomposed into individually ordinary steps whose combination creates an unapproved effect. Researching a contact, drafting outreach, locating an email endpoint, and calling a send tool can each look low-risk in isolation. Together they constitute external communication.

Review the intended business effect, not only each tool call.

## Mechanism: Three Gates

[MCPA v3](../../../frameworks/mcpa/) separates three questions:

1. **Evidence gate:** Are the facts required for this transition present and valid?
2. **Authority route:** Which actor and execution mode are permitted now?
3. **Commitment gate:** Has the exact external effect been approved and bound to its proposal?

An execution request should include:

```yaml
actor: verified principal or service
purpose: bounded reason for the action
resource_scope: exact records or endpoint
proposed_effect: inspectable change
evidence_refs: claims supporting eligibility
policy_version: rule set used for authorization
approval_ref: required approval, if any
idempotency_key: duplicate-effect protection
expires_at: permission lifetime
```

## Preparation Is Not Commitment

A draft can be useful without being sent. A proposed database change can be reviewed without being applied. A quoted price can be assembled without becoming a contractual offer.

Preserve that distinction in state and tools. Avoid one method whose behavior changes from “preview” to “execute” based on prose in the prompt.

## Evaluation Is Not Authorization

An evaluator may produce evidence about an action. It does not thereby gain
authority to approve that action. A second model can find defects in a first
model's work while sharing its blind spots, misunderstanding the business
requirement, or producing a confident false negative.

Record who produced the work, who evaluated it, what meaningful independence
exists between them, what the evaluation is allowed to block, and who remains
accountable for approval. Automated review may be a useful advisory or denial
signal without being sufficient evidence for commitment.

## Tradeoff

Gates introduce latency and can frustrate users if approvals are repetitive or unclear. Make the approval specific, display the exact effect, and promote only well-evaluated recurring actions into narrower pre-approved authority.

## Field Test

Split one consequential effect across several benign-looking tool calls. Verify that effect-level policy still recognizes the combined action and requires the same authority.

Then give an automated evaluator an apparently clean result containing a
domain-level omission. Verify that evaluator approval does not silently become
execution permission.

## Falsifier

If a gate never rejects, redirects, or changes an execution mode in representative testing, it may be ceremonial. Tighten its policy or remove the illusion of protection.

## Authority Boundary

A model may recommend and prepare. External commitment requires a policy-recognized actor, valid evidence, an allowed transition, and a durable receipt.

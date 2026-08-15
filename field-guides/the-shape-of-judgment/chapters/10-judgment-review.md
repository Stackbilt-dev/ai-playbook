# 10. The Judgment Review

Use this review before an AI-assisted decision becomes authoritative or produces an external effect. It is deliberately shorter than a complete governance program.

## Frame

- Is the requested decision stated separately from the original request?
- Are affected parties, time horizon, reversibility, and consequence named?
- Are material defaults and inferred requirements visible?
- Can unresolved ambiguity change scope, burden, eligibility, or authority?

## Context

- Which domain, legal, institutional, resource, and cultural constraints apply?
- Who supplied or validated each contextual claim?
- Are differences within a population represented rather than collapsed into a label?
- Is there a route for affected people to correct or appeal the context?

## Claims and Evidence

- Are observations, inferences, forecasts, preferences, and obligations distinct?
- Does every consequential claim have provenance, scope, and time bounds?
- Were pattern matches treated as candidates rather than truth?
- Are absence claims supported by known search coverage?
- Are conflicts and missing evidence explicit?

## State and Convergence

- Does the decision have authoritative state outside the model conversation?
- Are updates expressed as validated deltas with history?
- Can evidence order change the result, and is that behavior intentional?
- Are completion, abstention, escalation, deadline, and exhaustion defined?
- Does each iteration advance a named measure of decision progress?

## Authority and Effects

- Is capability separated from permission?
- Is the execution mode explicit: research, draft, propose, approve, or execute?
- Do evidence gates protect consequential transitions?
- Is approval bound to the exact proposed effect and policy version?
- Are external effects idempotent, observable, and represented by durable receipts?
- Can a sequence of low-authority steps combine into a prohibited effect?

## Feedback and Change

- Are outcome observations separated from evaluation and policy promotion?
- Is the evaluation representative of the scope being proposed?
- Are success, safety, unequal burden, cost, correction, and unknown effects considered?
- Does every promoted behavior have an owner, rollback, demotion rule, and expiry?
- Can the system remain useful while a behavior stays non-authoritative?

## Decision

End the review with one result:

| Result | Meaning |
|--------|---------|
| Proceed | Evidence, authority, and recovery support the bounded effect |
| Proceed as proposal | The analysis is useful, but commitment needs approval |
| Hold for evidence | A named missing fact blocks the transition |
| Escalate | Consequence or unresolved conflict requires an accountable reviewer |
| Deny | Policy or consent prohibits the requested effect |
| Retire experiment | The mechanism adds no distinct value or failed its evaluation |

“Proceed” should identify the exact state transition and effect. “Hold” should name the evidence needed. “Escalate” should state the reviewer’s bounded question. “Deny” should preserve an inspectable reason without exposing sensitive policy internals.

## Final Test

Can a reviewer explain, without relying on private model reasoning:

1. what decision was made;
2. which context and evidence supported it;
3. which uncertainty remained;
4. why this actor could take this action;
5. what changed in the outside world;
6. how the system will correct or learn from the outcome?

If not, the system has generated an answer, not completed a governed judgment.

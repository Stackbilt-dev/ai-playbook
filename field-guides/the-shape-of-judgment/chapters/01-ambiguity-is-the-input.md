# 1. Ambiguity Is the Real Input

Most consequential requests arrive as compressed intentions:

- “Find our best prospects.”
- “Approve this exception.”
- “Tell me whether this claim is true.”
- “Adapt this campaign for another market.”
- “Fix whatever is causing churn.”

The sentence hides the decision class, affected people, time horizon, authority, evidence standard, and acceptable error. Treating it as a complete specification forces the system to invent those missing boundaries.

## Principle

Represent ambiguity before resolving it. A system should distinguish what the requester said from what it inferred about the request.

Use an intake record with at least:

```yaml
request: the original intention
decision: the concrete decision being considered
affected_parties: people or systems that bear consequences
time_horizon: when evidence and effects matter
reversibility: easy | costly | effectively_irreversible
authority_needed: who may make or execute the decision
known_constraints: explicit limits
open_questions: missing facts that could change the route
```

The record need not be large. Its purpose is to stop a plausible interpretation from silently becoming the instruction.

## Failure Mode: Specification Laundering

Specification laundering occurs when an inferred detail passes through enough generated prose that it begins to look user-supplied. A model assumes “best” means highest predicted revenue, later components treat that metric as approved, and the final system optimizes it without ever exposing the choice.

The same failure appears when a broad request becomes a narrow population, when “soon” becomes a deadline, or when “recommend” becomes “execute.”

## Mechanism: The Ambiguity Budget

Not every missing detail must trigger a question. Classify each ambiguity:

| Class | Response |
|-------|----------|
| Cosmetic and reversible | Choose a default and record it |
| Material but recoverable | Produce alternatives or a proposal |
| Consequential or authority-changing | Ask, defer, or escalate |
| Unresolvable with available evidence | Abstain and name the gap |

This is an ambiguity budget: the system may spend inference only where the consequence permits it.

## Tradeoff

Clarification adds latency and can exhaust users. The answer is not to ask about everything; it is to make defaults proportional to consequences and visible in the resulting artifact.

## Field Test

Give the same short request to three reviewers. Compare the decision, affected parties, success metric, and authority each inferred. Material disagreement reveals hidden specification work.

## Falsifier

If an ambiguity class never changes the route, output, review, or effect across representative cases, remove it from intake. A field that merely decorates the record is not a control.

## Authority Boundary

An interpretation may shape a draft. It must not silently expand the requested action, population, budget, or permission class.

FIELD GUIDE

# The Shape of Judgment

Context, evidence, and governed decisions in AI systems—for people building systems that can affect other people or the world outside the model.

**Kurt Overmier · Stackbilt**

Public-review edition · August 2026

<!-- page -->

THE CENTRAL ARGUMENT

# A pattern is not yet a judgment.

Models generate interpretations. A dependable system still has to decide:

- which context applies;
- which claims have evidence;
- which contradictions remain unresolved;
- who has authority to act;
- when the correct result is to stop.

The model proposes. The surrounding system governs what the proposal can become.

<!-- page -->

01 · AMBIGUITY

# Treat ambiguity as an input—not an inconvenience

Before inference, name what the request leaves open:

- the affected parties;
- the consequence of being wrong;
- material defaults and interpretations;
- what evidence is missing;
- which decisions are reversible.

Hidden assumptions do not disappear. They become unreviewed policy.

<!-- page -->

02 · CONTEXT

# Context is a set of claims with boundaries

Useful context says more than “this seems relevant.” It records:

> source · owner · scope · valid from · valid until · decision use

Relevance, confidence, and temporal validity are different properties.

A recent claim may be irrelevant. A highly relevant claim may no longer be true.

<!-- page -->

03 · EVIDENCE

# Similarity retrieves candidates. It does not establish truth.

The most similar source may be stale, circular, unauthorized, fabricated, or about a different population.

Before a pattern becomes decision evidence, check:

- provenance;
- freshness;
- scope;
- corroboration or contradiction;
- authority to use it.

<!-- page -->

04 · CLAIMS

# Make the conclusion decomposable

Separate statements that carry different kinds of authority:

- **Observation:** what was recorded
- **Inference:** what may explain it
- **Forecast:** what may happen next
- **Preference:** what someone values
- **Obligation:** what an authoritative rule requires

Fluent prose can hide the transition from one type to another. A claim ledger makes that transition inspectable.

<!-- page -->

05 · STATE AND CONVERGENCE

# A decision should move through bounded states

```text
framing → evidence pending → review
        → approved | denied | deferred
```

Iteration is not automatically improvement. Define what new evidence can change the state, what contradictions block it, and when the process must stop.

Completion is not the same as convergence.

<!-- page -->

06 · AUTHORITY

# Capability is not permission

A system may be able to send, publish, update, purchase, or transfer. That does not mean it may do so for this actor, purpose, scope, or moment.

Use explicit execution modes:

> deny → hold → research → draft → propose → approve → execute

Select the least-authoritative mode that can safely advance the work.

<!-- page -->

07 · EVALUATION

# Evaluation is not authorization

A second model may catch defects while sharing the first model’s blind spots.

Record:

- who produced the work;
- who evaluated it;
- what meaningful independence exists;
- what the evaluation may block;
- who remains accountable for approval.

Another model call is not automatically an independent review.

<!-- page -->

08 · FEEDBACK

# Repeated success is evidence for review—not self-executing permission

```text
outcome → observation → hypothesis → shadow test
        → accountable promotion → versioned policy
```

Every promotion needs representative evaluation, counter-metrics, a blast radius, rollback, an owner, and a demotion rule.

A metric may inform judgment without becoming its sole objective.

<!-- page -->

THREE STACKBILT CASE FILES

# The useful output was a boundary

- **The Lead That Stopped:** qualification did not become invented contact evidence or permission to send.
- **The Silent Loop:** a healthy heartbeat did not prove that authoritative state had advanced.
- **The Fluent Omission:** a polished answer did not prove that required context survived the pipeline.

In each case, surface plausibility pointed past the actual failure.

<!-- page -->

THE JUDGMENT REVIEW

# Seven questions worth asking repeatedly

1. What portable principle should survive a change in model or vendor?
2. What failure appears when it is ignored?
3. What artifact, state, or gate implements it?
4. What does that mechanism cost?
5. What observable field test can challenge it?
6. What result would falsify the recommendation?
7. What must remain non-authoritative while uncertainty remains?

<!-- page -->

PUBLIC-REVIEW EDITION

# Read *The Shape of Judgment*

The complete field guide includes thirteen chapters, three Stackbilt case files, a Decision Record, and an Experiment and Promotion Card.

**Read the public-review source:**

[github.com/Stackbilt-dev/ai-playbook](https://github.com/Stackbilt-dev/ai-playbook/tree/main/field-guides/the-shape-of-judgment)

If you build AI-assisted decisions or agentic systems, I would value your hardest counterexample.

**Kurt Overmier · Stackbilt**

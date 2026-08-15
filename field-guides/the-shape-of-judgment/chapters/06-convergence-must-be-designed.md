# 6. Convergence Must Be Designed

Iteration is not automatically improvement. An agent can research forever, repeatedly rewrite the same answer, amplify an early error, or stop only because its token budget expired.

## Principle

Define the stopping rule before the loop begins. A decision process should know what completion, abstention, escalation, and exhaustion mean.

Useful stopping conditions include:

- all required evidence gates pass;
- the claim set is stable across a defined update;
- remaining conflicts are below a stated consequence threshold;
- expected value of another search is below its cost;
- a deadline or budget requires a partial, explicitly qualified result;
- a protected ambiguity requires human or domain review;
- repeated attempts produce no new admissible evidence.

## Failure Mode: Motion as Progress

Systems often measure tool calls, generated alternatives, retrieved documents, or debate rounds. Those are activities, not progress. A loop can produce more artifacts while the decision remains equally unsupported.

Oscillation is another failure: two sources or evaluators repeatedly flip the state without creating a conflict record. The system appears active while avoiding the unresolved question.

## Mechanism: Progress Invariants

Each iteration should advance at least one named dimension:

```yaml
progress:
  required_evidence_remaining: 3 -> 2
  unresolved_high_impact_conflicts: 2 -> 1
  decision_uncertainty: 0.42 -> 0.31
  validated_constraints: 4 -> 5
  external_effects_committed: 0
```

If no dimension improves after a bounded number of attempts, stop and emit the unresolved state. Do not fabricate closure.

Confidence alone is a weak stopping rule. A model can become more confident through repetition without receiving better evidence.

## Escalation Is a Valid Terminal Result

A process can complete successfully by producing a well-formed request for review: the current state, disputed claims, evidence searched, consequence of delay, and exact decision needed from the reviewer.

That is more useful than a vague “human in the loop” flag because it makes the human’s work bounded and inspectable.

## Tradeoff

Strict stopping rules can end exploration before a rare source is found. Match search depth to consequence and retain a way for a reviewer to extend the budget deliberately.

## Field Test

Run cases with missing evidence, conflicting evidence, repeated identical results, and one late decisive source. Verify that the loop stops honestly in the first three and can admit the decisive source in the fourth without discarding its budget rules.

## Falsifier

Revise a stopping rule when it consistently ends before useful evidence is found or continues after additional work has negligible decision value.

## Authority Boundary

Budget exhaustion may authorize stopping. It does not authorize converting uncertainty into approval or absence into a negative finding.

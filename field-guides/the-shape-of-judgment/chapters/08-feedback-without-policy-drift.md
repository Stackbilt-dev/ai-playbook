# 8. Feedback Without Policy Drift

A system should learn from outcomes. It should not quietly turn yesterday’s behavior into tomorrow’s policy.

## Principle

Separate observation, evaluation, and promotion. Production feedback can propose a change; it should not automatically widen authority or rewrite governing rules.

```text
outcome → observation → evaluated hypothesis → shadow test
        → accountable promotion decision → versioned policy
```

## Failure Mode: Success Becomes Permission

A workflow succeeds several times, so an operator removes approval. A model’s drafts are often accepted, so the system starts sending them. A routing shortcut saves money, so it becomes the default for populations not represented in evaluation.

Repeated success is evidence for review, not self-executing permission.

The reverse matters too. A single complaint or noisy metric can cause policy whiplash if the system lacks a representative evaluation and a change threshold.

## Mechanism: Promotion Records

Use an [Experiment and Promotion Card](../worksheets/experiment-and-promotion-card.md) containing:

- hypothesis and expected benefit;
- current authority and proposed authority;
- representative evaluation population;
- success, safety, and equity measures;
- known blind spots;
- shadow or bounded-execution results;
- blast radius and rollback path;
- accountable owner;
- promotion, demotion, and expiry conditions.

Promotion changes a versioned rule. Keep the prior version and record which decisions used each one.

## Outcome Quality

Do not optimize only the easiest observable proxy. Measure:

- whether the intended user outcome occurred;
- whether required evidence and constraints were respected;
- whether affected groups experienced materially different errors or burdens;
- whether the action settled correctly;
- cost and latency per accepted outcome;
- correction, appeal, and reversal rates;
- unknown or unmeasured effects.

A metric can inform judgment without becoming the sole objective.

## Demotion and Retirement

Every promoted behavior needs a path down. Demote when evaluation regresses, context changes, a provider or policy version shifts, new failure modes appear, or the owner can no longer review it. Retire a mechanism when its distinct benefit disappears.

## Tradeoff

Controlled promotion slows adaptation. Uncontrolled adaptation shifts risk onto users who did not agree to be an experiment. Use shadow evaluation and narrow cohorts to learn without granting premature authority.

## Field Test

Feed the system highly positive but unrepresentative outcomes. Verify that it proposes an evaluation or bounded experiment rather than widening scope automatically.

## Falsifier

If controlled promotion does not reduce regressions or improve explainability compared with direct updates, simplify the process—but retain versioning and rollback for consequential policies.

## Authority Boundary

Feedback may update evidence and propose a policy change. Only an accountable promotion mechanism may change authority, protected thresholds, or the populations to which a rule applies.

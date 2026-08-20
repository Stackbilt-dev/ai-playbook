# Experiment and Promotion Card

Use this card before an experimental behavior receives production authority or a wider scope.

## Hypothesis

- Behavior being tested:
- Problem it should solve:
- Simpler baseline:
- Expected measurable benefit:
- What would falsify the hypothesis:

## Current Boundary

```yaml
status: concept | checklist | prototype | evaluated | promoted | retired
execution_mode: offline | shadow | draft | bounded_execution
population_scope:
data_scope:
budget:
external_effects_allowed: false
owner:
expiry:
```

## Evaluation

| Dimension | Measure | Threshold | Result | Limitation |
|-----------|---------|-----------|--------|------------|
| Task outcome | | | | |
| Evidence quality | | | | |
| Safety/policy | | | | |
| Unequal error or burden | | | | |
| Calibration/abstention | | | | |
| Cost and latency | | | | |
| Recovery | | | | |

## Evaluation Governance

- Primary success metric:
- Counter-metric or failure signal:
- Plausible ways the primary metric can be gamed:
- Producer:
- Evaluator:
- Basis for evaluator independence:
- Evidence unavailable to the evaluator:
- Correlated failures that could fool both producer and evaluator:
- What the evaluation may block or escalate:
- What the evaluation may not authorize:

## Representative Coverage

- Included cases and populations:
- Missing or underrepresented cases:
- Known context shifts:
- Stakeholder or domain review completed:
- Counterexamples retained:
- Regressions hidden by the headline metric:

## Proposed Promotion

```yaml
from_mode:
to_mode:
new_scope:
new_authority:
evidence_refs: []
blast_radius:
rollback:
```

## Decision

`promote | continue_experiment | narrow | demote | retire`

- Accountable approver:
- Decision date:
- Reason:
- Next review or expiry:
- Automatic demotion conditions:

Promotion moves only the validated behavior. It does not validate unrelated claims, populations, or authority.

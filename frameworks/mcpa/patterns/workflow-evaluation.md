---
title: "Governed Workflow Evaluation"
category: "frameworks/mcpa/patterns"
tags: ["multi-actor", "evaluation", "safety", "outcomes", "observability", "mcpa"]
created: "2026-08-14"
updated: "2026-08-14"
version: "3.0"
---

# Governed Workflow Evaluation

Routing Accuracy, Coordination Quality, Context Utilization, Insight Agreement,
and System Overhead measure cognitive coordination. Operational workflows need
three additional evaluation planes.

## 1. Safety and Grounding

| Metric | Meaning |
| --- | --- |
| Unsupported Claim Rate | Claims without canonical or evidentiary support |
| Authorization Violations | Attempts or actions beyond current authority |
| Gate Precision | How often a passing gate was truly ready |
| Gate Recall | How often a blocking condition was caught |
| Abstention Quality | Whether hold/deny decisions prevented invalid action |
| Staleness Incidents | Decisions based on superseded canonical facts |

## 2. Lifecycle Integrity

| Metric | Meaning |
| --- | --- |
| Invalid Transition Count | Attempts outside the state contract |
| Protected-State Violations | Reopening opt-out, revoked, or deleted states |
| Duplicate Commitment Rate | Repeated external action for one idempotency key |
| Orphaned Work Rate | Items with no valid next action |
| Human Override Rate | Frequency and direction of operator corrections |

## 3. Outcome Value

| Metric | Meaning |
| --- | --- |
| Time to Next Valid Action | Delay between state and executable next step |
| Conversion Rate | Work items reaching the intended outcome |
| Attributed Value | Revenue, risk reduction, or other measurable value |
| Cost per Outcome | Total cognitive and operational cost per result |
| Test Contamination Rate | Test/internal events incorrectly counted as real |

## Evaluation Hierarchy

```text
coordination healthy?
  -> workflow safe and state-valid?
      -> intended outcome achieved?
          -> outcome worth the total cost?
```

A system with high Coordination Quality but authorization violations is broken.
A safe system with no outcomes may be well governed but economically useless.
Do not collapse these planes into one score.

## Minimum Dashboard

```text
Coordination: RA, CQS, CUR, IAR, SOR
Safety: unsupported claims, auth violations, gate precision/recall
Lifecycle: invalid transitions, protected-state violations, orphaned work
Outcome: conversion, attributed value, cost per outcome
```

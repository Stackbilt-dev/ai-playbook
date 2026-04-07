---
title: "Multi-Agent Evaluation Framework"
category: "frameworks/mcpa/patterns"
tags: ["multi-agent", "evaluation", "metrics", "observability", "mcpa"]
created: "2026-04-07"
updated: "2026-04-07"
version: "2.0"
---

# Multi-Agent Evaluation Framework

How to measure whether your multi-agent system is actually working. Single-agent evaluation is straightforward (did the agent produce the right output?). Multi-agent evaluation is harder — you need to measure the system's coordination quality, not just individual agent quality.

## Why This Is Hard

A multi-agent system can fail in ways that individual agent metrics won't catch:

- All agents perform well individually, but the synthesis is garbage
- The router sends 80% of tasks to one agent (load imbalance)
- Agents agree on everything (no diversity of perspective)
- Context sharing is lossy — critical insights get dropped
- The system is slower than a single good agent would have been

You need metrics that measure the **system** as a whole, not just its parts.

## The Five Metrics

### 1. Routing Accuracy (RA)

**Does the right agent handle the right task?**

```
RA = correct_routes / total_routes
```

#### How to measure
- **Offline:** Label a test set of tasks with the ideal agent. Run the router. Compare.
- **Online:** After each task, check if the assigned agent's confidence exceeded a threshold. Low confidence suggests misroute.
- **Retrospective:** Periodically review completed tasks and flag cases where a different agent would have produced a better result.

#### Implementation

```python
def routing_accuracy(routing_log: list[dict], ground_truth: dict) -> float:
    """Measure routing accuracy against labeled ground truth."""
    correct = sum(
        1 for entry in routing_log
        if entry["routed_to"] == ground_truth.get(entry["task_id"])
    )
    return correct / len(routing_log) if routing_log else 0

def routing_confidence_proxy(routing_log: list[dict],
                              confidence_threshold: float = 0.7) -> float:
    """Proxy for routing accuracy using agent confidence."""
    confident = sum(
        1 for entry in routing_log
        if entry["agent_confidence"] >= confidence_threshold
    )
    return confident / len(routing_log) if routing_log else 0
```

#### Target
- RA > 0.85 for production systems
- RA > 0.70 is acceptable for early systems
- RA < 0.60 means your routing is worse than random (with a small agent set)

---

### 2. Coordination Quality Score (CQS)

**Are agents effectively building on each other's work?**

Measures whether the output of a multi-agent system is better than what any single agent would have produced alone.

```
CQS = multi_agent_quality / best_single_agent_quality
```

CQS > 1.0 means the system is producing coordination value. CQS < 1.0 means you'd be better off with a single agent.

#### How to measure
- Run the same task through your multi-agent system AND through your best single agent
- Score both outputs (human eval, LLM-as-judge, or automated metrics)
- CQS = multi-agent score / single-agent score

#### Implementation

```python
async def coordination_quality_score(task: str, multi_agent_system,
                                      best_single_agent: Agent,
                                      evaluator: Agent) -> float:
    """Compare multi-agent output vs best single agent."""
    multi_result = await multi_agent_system.run(task)
    single_result = await best_single_agent.run(task)

    # Score both (using LLM-as-judge)
    multi_score = await evaluator.score(task, multi_result.output)
    single_score = await evaluator.score(task, single_result.output)

    return multi_score / single_score if single_score > 0 else 0
```

#### What it tells you
- **CQS > 1.2:** Strong coordination value. Multi-agent approach justified.
- **CQS 1.0-1.2:** Marginal improvement. Consider whether the complexity is worth it.
- **CQS < 1.0:** Coordination is hurting. Simplify.

---

### 3. Context Utilization Rate (CUR)

**How much of the shared context actually gets used?**

Measures whether the insights agents share with each other are actually being consumed and built upon, or just piling up unused.

```
CUR = insights_referenced_by_downstream / total_insights_produced
```

#### How to measure
- Track when an agent's output explicitly references or builds on a prior insight
- Compare against total insights in the ledger

#### Implementation

```python
def context_utilization_rate(ledger: InsightLedger,
                              agent_outputs: list[dict]) -> float:
    """Measure what fraction of shared insights are actually used."""
    all_insights = ledger.current()
    referenced = set()

    for output in agent_outputs:
        for insight in all_insights:
            # Check if the agent's output references this insight
            # (semantic similarity, explicit citation, or keyword match)
            if references_insight(output["content"], insight["content"]):
                referenced.add(insight["id"])

    return len(referenced) / len(all_insights) if all_insights else 0
```

#### What it tells you
- **CUR > 0.6:** Context sharing is working. Agents are building on each other.
- **CUR 0.3-0.6:** Some context is useful, some is noise. Improve briefing relevance.
- **CUR < 0.3:** Most shared context is ignored. Either agents don't need it (simplify) or the briefings aren't relevant (fix filtering).

---

### 4. Insight Agreement Rate (IAR)

**How often do agents agree vs. disagree?**

Both too much and too little agreement are problems.

```
IAR = agreeing_insight_pairs / total_comparable_insight_pairs
```

#### What the numbers mean

| IAR | Interpretation | Action |
|-----|---------------|--------|
| > 0.95 | Suspiciously high. Agents may be redundant or sycophantic. | Reduce agent count or increase diversity. |
| 0.70-0.95 | Healthy. Agents mostly agree but have meaningful disagreements. | System is working well. |
| 0.50-0.70 | High disagreement. Could be healthy (complex problem) or broken (bad agents). | Check if disagreements are productive (surfacing real tensions) or noise. |
| < 0.50 | Chaotic. Agents are contradicting each other more than agreeing. | Investigate agent quality, routing accuracy, and context sharing. |

#### Implementation

```python
def insight_agreement_rate(ledger: InsightLedger) -> float:
    """Measure pairwise agreement among agent insights."""
    current = ledger.current()
    comparable_pairs = find_comparable_pairs(current)  # Same topic, different agents

    if not comparable_pairs:
        return 1.0  # No comparisons possible

    agreements = sum(
        1 for a, b in comparable_pairs
        if are_compatible(a["content"], b["content"])  # LLM check
    )
    return agreements / len(comparable_pairs)
```

---

### 5. System Overhead Ratio (SOR)

**What's the cost of coordination relative to the cost of doing the actual work?**

```
SOR = coordination_cost / total_cost
```

Where coordination cost includes: routing decisions, context briefing composition, synthesis steps, conflict resolution. And total cost includes all agent invocations.

#### What it tells you
- **SOR < 0.15:** Efficient. Coordination overhead is minimal.
- **SOR 0.15-0.30:** Acceptable. The coordination is adding value (check CQS to confirm).
- **SOR > 0.30:** Expensive coordination. You're spending more on managing agents than on the work itself. Simplify.

#### Implementation

```python
def system_overhead_ratio(execution_log: list[dict]) -> float:
    """Calculate the ratio of coordination cost to total cost."""
    coordination_tokens = sum(
        entry["tokens"] for entry in execution_log
        if entry["type"] in ("routing", "briefing", "synthesis", "conflict_resolution")
    )
    total_tokens = sum(entry["tokens"] for entry in execution_log)

    return coordination_tokens / total_tokens if total_tokens > 0 else 0
```

---

## The Evaluation Dashboard

Combine all five metrics into a single view:

```
┌──────────────────────────────────────────────┐
│           Multi-Agent System Health           │
├──────────────────────────────────────────────┤
│  Routing Accuracy (RA):         0.87  [OK]   │
│  Coordination Quality (CQS):   1.24  [GOOD]  │
│  Context Utilization (CUR):    0.54  [WARN]  │
│  Insight Agreement (IAR):      0.78  [OK]    │
│  System Overhead (SOR):        0.18  [OK]    │
├──────────────────────────────────────────────┤
│  Verdict: System is producing value but      │
│  context sharing needs attention (low CUR).  │
│  Investigate briefing relevance.              │
└──────────────────────────────────────────────┘
```

### Interpreting the dashboard

| Scenario | RA | CQS | CUR | IAR | SOR | Diagnosis |
|----------|----|----|-----|-----|-----|-----------|
| Healthy system | > 0.85 | > 1.2 | > 0.6 | 0.7-0.95 | < 0.15 | Working well |
| Routing problem | < 0.70 | < 1.0 | any | any | any | Fix routing first |
| Wasted coordination | > 0.85 | < 1.0 | < 0.3 | > 0.95 | > 0.30 | Agents are redundant — simplify |
| Siloed agents | > 0.85 | > 1.0 | < 0.3 | any | < 0.15 | Agents don't share. Improve context briefing |
| Productive tension | > 0.85 | > 1.2 | > 0.6 | 0.50-0.70 | < 0.25 | Disagreements are productive — maintain |
| Chaos | < 0.70 | < 1.0 | any | < 0.50 | > 0.30 | System is broken. Start over with fewer agents |

---

## Running Evaluations

### Offline evaluation (periodic)
Run a benchmark suite of labeled tasks through the system. Compute all five metrics. Compare against previous runs. This catches regressions.

### Online evaluation (continuous)
Log routing decisions, agent confidences, and token usage in production. Compute RA, SOR, and IAR continuously. Flag anomalies.

### Human evaluation (quarterly)
Sample 50-100 production tasks. Have a human rate multi-agent output quality. Compute CQS against single-agent baseline. This is the ground truth.

---

## What to Do When Metrics Are Bad

| Metric | Bad value | First thing to try |
|--------|-----------|-------------------|
| RA low | < 0.70 | Improve router prompts. Add capability descriptions. Try confidence-based routing. |
| CQS low | < 1.0 | Remove agents until CQS > 1.0. You may have too many. |
| CUR low | < 0.3 | Improve context briefings. Make them more relevant and concise. |
| IAR too high | > 0.95 | Add adversarial or devil's-advocate agent. Increase prompt diversity. |
| IAR too low | < 0.50 | Check agent quality individually. Bad agents produce noise, not insight. |
| SOR high | > 0.30 | Simplify routing. Reduce synthesis steps. Use cheaper models for coordination. |

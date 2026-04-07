---
title: "Coordination Patterns"
category: "frameworks/mcpa/patterns"
tags: ["multi-agent", "coordination", "topology", "collaboration", "mcpa"]
created: "2026-04-07"
updated: "2026-04-07"
version: "2.0"
---

# Coordination Patterns

How multiple agents work together on a single task. Routing decides *who* handles a task; coordination decides *how* multiple agents collaborate when one agent isn't enough.

Each pattern is a topology — a shape that describes how agents interact. Pick the shape that matches your problem.

## Pattern 1: Sequential Pipeline

**Assembly line.** Agent A finishes, passes output to Agent B, which passes to Agent C. Each agent transforms the work product.

```
Agent A ──→ Agent B ──→ Agent C ──→ Result
```

### When to use
- The task has natural stages (analyze → plan → implement → review)
- Each stage needs different expertise
- Order matters — later stages depend on earlier outputs

### Implementation

```python
async def sequential_pipeline(task: str, agents: list[Agent],
                               ledger: InsightLedger) -> dict:
    """Run agents in sequence, each building on the previous."""
    context = task

    for agent in agents:
        # Compose briefing from prior agents' work
        briefing = compose_briefing(ledger, agent)
        result = await agent.run(context, briefing=briefing)

        # Record what this agent found
        ledger.record(
            agent_id=agent.id,
            content=result.summary,
            confidence=result.confidence,
            evidence=result.output,
            tags=agent.domain_tags,
        )

        # Pass output as input to next agent
        context = result.output

    return {"result": context, "ledger": ledger}
```

### Example
Code review pipeline: **Correctness Agent** → **Security Agent** → **Style Agent** → **Summary Agent**

### Failure mode
Slow — total latency is the sum of all agent latencies. **Fix:** Only pipeline the stages that genuinely depend on prior output. Parallelize the rest.

---

## Pattern 2: Parallel Fan-Out

**Divide and conquer.** Multiple agents work on different aspects of the same task simultaneously. Results are collected and synthesized.

```
         ┌──→ Agent A ──┐
Task ────┼──→ Agent B ──┼──→ Synthesizer ──→ Result
         └──→ Agent C ──┘
```

### When to use
- The task has independent dimensions (security AND performance AND UX)
- Latency matters more than token cost
- A final synthesis step can merge perspectives

### Implementation

```python
async def fan_out(task: str, agents: list[Agent],
                  synthesizer: Agent, ledger: InsightLedger) -> dict:
    """Run agents in parallel, then synthesize."""
    # Fan out — all agents run concurrently
    results = await asyncio.gather(*[
        agent.run(task) for agent in agents
    ])

    # Record all findings to ledger
    for agent, result in zip(agents, results):
        ledger.record(
            agent_id=agent.id,
            content=result.summary,
            confidence=result.confidence,
            evidence=result.output,
            tags=agent.domain_tags,
        )

    # Synthesize — one agent merges all perspectives
    briefing = compose_full_briefing(ledger)
    synthesis = await synthesizer.run(
        f"Synthesize these findings into a unified response:\n\n{briefing}",
    )

    return {"result": synthesis.output, "sources": results}
```

### Example
Research task: **Literature Agent** + **Data Agent** + **Expert Agent** → **Synthesis Agent** composes findings.

### The synthesizer is critical
A bad synthesizer either cherry-picks (ignoring dissenting findings) or dumps everything (no synthesis, just concatenation). The synthesizer needs explicit instructions: *"Identify agreements, surface disagreements, rank by confidence, produce a unified view."*

### Failure mode
Agents duplicate work. **Fix:** Give each agent a specific angle in its system prompt. "You are responsible for security implications" vs. "You are responsible for performance implications."

---

## Pattern 3: Debate / Adversarial

**Agents argue, then converge.** Two or more agents take opposing positions on a question. A judge evaluates the arguments.

```
         ┌──→ Agent A (Pro) ──┐
Task ────┤                    ├──→ Judge ──→ Decision
         └──→ Agent B (Con) ──┘
```

### When to use
- High-stakes decisions where being wrong is expensive
- Questions with genuine tradeoffs (not just right/wrong)
- You want to surface hidden assumptions and blind spots
- Reducing sycophancy — forcing agents to argue against the obvious choice

### Implementation

```python
async def debate(question: str, rounds: int = 2) -> dict:
    """Structured debate between opposing agents."""
    pro_agent = Agent(system="Argue FOR this position. Be specific and evidence-based.")
    con_agent = Agent(system="Argue AGAINST this position. Find weaknesses, risks, hidden costs.")
    judge = Agent(system="Evaluate both arguments. Identify the stronger position and explain why.")

    pro_args = []
    con_args = []

    for round in range(rounds):
        # Pro argues (sees con's previous arguments)
        pro_context = format_debate_history(pro_args, con_args)
        pro = await pro_agent.run(f"{question}\n\n{pro_context}")
        pro_args.append(pro.output)

        # Con responds (sees pro's latest argument)
        con_context = format_debate_history(pro_args, con_args)
        con = await con_agent.run(f"{question}\n\n{con_context}")
        con_args.append(con.output)

    # Judge evaluates the full debate
    full_debate = format_full_debate(pro_args, con_args)
    decision = await judge.run(
        f"Review this debate and render a decision:\n\n{full_debate}"
    )

    return {
        "decision": decision.output,
        "pro_arguments": pro_args,
        "con_arguments": con_args,
    }
```

### Example
Architecture decision: "Should we use a monorepo or polyrepo?" — Pro Agent argues monorepo, Con Agent argues polyrepo, Judge synthesizes.

### Design note
Two rounds is usually enough. More rounds produce diminishing returns and risk circular arguments. The judge should be the most capable model in the system.

---

## Pattern 4: Supervisor

**One agent manages the others.** A supervisor agent receives the task, delegates subtasks to worker agents, monitors progress, and assembles the final result.

```
                    Supervisor
                   ╱    │    ╲
           Worker A  Worker B  Worker C
```

### When to use
- Complex tasks that need dynamic decomposition
- You can't predict the subtasks in advance
- Worker agents need different context subsets
- You need adaptive replanning when subtasks fail

### Implementation

```python
async def supervisor_loop(task: str, workers: dict[str, Agent],
                          supervisor: Agent, max_steps: int = 10) -> dict:
    """Supervisor decomposes, delegates, and assembles."""
    plan = await supervisor.run(
        f"Decompose this task into subtasks and assign to workers.\n"
        f"Available workers: {list(workers.keys())}\n\n"
        f"Task: {task}\n\n"
        f"Respond with JSON: [{{\"worker\": str, \"subtask\": str}}]"
    )

    results = {}
    for step in plan.subtasks:
        worker = workers[step["worker"]]
        result = await worker.run(step["subtask"])

        results[step["worker"]] = result

        # Supervisor checks progress and may replan
        if result.confidence < 0.6:
            replan = await supervisor.run(
                f"Worker {step['worker']} returned low-confidence result:\n"
                f"{result.summary}\n\n"
                f"Should we retry, reassign, or proceed?"
            )
            # Handle replan...

    # Supervisor assembles final result
    assembly = await supervisor.run(
        f"Assemble these results into a final response:\n\n"
        f"{format_results(results)}"
    )

    return {"result": assembly.output, "subtask_results": results}
```

### Example
Writing a technical report: Supervisor breaks into research, drafting, and fact-checking subtasks. Assigns research to the Research Agent, drafting to the Writing Agent, fact-checking back to the Research Agent.

### Failure mode
Supervisor becomes a bottleneck — every decision goes through it. **Fix:** Give workers autonomy for straightforward subtasks. Reserve supervisor intervention for failures and cross-cutting decisions.

---

## Pattern 5: Consensus

**All agents must agree.** Each agent independently analyzes the task. The result is accepted only when agents reach sufficient agreement.

```
Agent A ──┐
Agent B ──┼──→ Agreement Check ──→ Result (or Retry)
Agent C ──┘
```

### When to use
- Safety-critical decisions (deploy to production, delete data)
- You want to reduce hallucination risk through redundancy
- Correctness matters more than speed

### Implementation

```python
async def consensus(task: str, agents: list[Agent],
                    threshold: float = 0.8) -> dict:
    """Require agent consensus before accepting a result."""
    # All agents analyze independently
    results = await asyncio.gather(*[
        agent.run(task) for agent in agents
    ])

    # Check agreement
    positions = [r.conclusion for r in results]
    agreement_score = calculate_agreement(positions)

    if agreement_score >= threshold:
        # Consensus reached — merge into unified result
        return {
            "status": "consensus",
            "score": agreement_score,
            "result": merge_positions(results),
        }
    else:
        # No consensus — surface the disagreement
        return {
            "status": "disagreement",
            "score": agreement_score,
            "positions": [
                {"agent": a.id, "conclusion": r.conclusion, "confidence": r.confidence}
                for a, r in zip(agents, results)
            ],
        }


def calculate_agreement(positions: list[str]) -> float:
    """Score how much agents agree (0 = total disagreement, 1 = unanimous)."""
    # Use embedding similarity or LLM-based comparison
    # Simple version: pairwise semantic similarity
    pairs = [(positions[i], positions[j])
             for i in range(len(positions))
             for j in range(i + 1, len(positions))]
    similarities = [semantic_similarity(a, b) for a, b in pairs]
    return sum(similarities) / len(similarities)
```

### Example
Safety check before production deploy: **Security Agent**, **Correctness Agent**, and **Ops Agent** all independently review. Deploy only if all three agree it's safe.

---

## Combining Patterns

Real systems combine these topologies. Common compositions:

### Pipeline + Fan-Out
Sequential stages where some stages fan out internally.
```
Analyze ──→ [Security + Performance + UX] ──→ Synthesize ──→ Implement
              (parallel fan-out)              (pipeline continues)
```

### Router + Debate
Route to debate when the task involves a genuine tradeoff.
```
Router ──→ Simple task? ──→ Single agent
       └─→ Tradeoff?   ──→ Debate (Pro + Con + Judge)
```

### Supervisor + Consensus
Supervisor delegates, then requires consensus on critical subtasks.
```
Supervisor ──→ Research subtask ──→ Single worker (low stakes)
           └─→ Deploy subtask  ──→ Consensus (3 workers must agree)
```

---

## Choosing a Topology

| Problem shape | Pattern | Why |
|--------------|---------|-----|
| Clear stages, each needing different skills | Sequential Pipeline | Natural decomposition |
| Independent dimensions to analyze | Parallel Fan-Out | Speed + coverage |
| Genuine tradeoff with no obvious right answer | Debate | Surfaces hidden assumptions |
| Complex task requiring dynamic planning | Supervisor | Adaptive decomposition |
| Safety-critical, correctness-critical | Consensus | Redundancy reduces error |
| Combination of the above | Compose them | Use the decision table above per subtask |

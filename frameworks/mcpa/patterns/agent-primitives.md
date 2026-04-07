---
title: "Agent Primitives"
category: "frameworks/mcpa/patterns"
tags: ["multi-agent", "agent-design", "contracts", "governance", "memory", "mcpa"]
created: "2026-04-07"
updated: "2026-04-07"
version: "2.0"
---

# Agent Primitives

The patterns in [Agent Routing](agent-routing.md), [Shared Context](shared-context.md), and [Coordination](coordination.md) describe how agents work *together*. This document describes how to build agents that are structurally sound *before* they interact.

Most agent frameworks treat agents as prompt wrappers — a system prompt plus tools. The patterns here go deeper: agents as validated compositions with structural governance, deterministic routing, and memory that changes behavior.

These patterns are more opinionated than the coordination layer. They represent a specific architectural philosophy: **contract-first, composition-over-inheritance, deterministic-where-possible.**

---

## Pattern 1: Contract-First Agent Design

**Validate agent configuration structurally before runtime.** Bad agents should fail at build time, not produce garbage at runtime.

### The Problem

Most agent frameworks define agents like this:

```python
agent = Agent(
    name="security-reviewer",
    system_prompt="You are a security expert...",
    tools=[scan_code, check_vulnerabilities],
)
```

Nothing validates that the system prompt is coherent with the tools. Nothing checks that the agent's domain matches its capabilities. If you wire a security prompt to a content-writing tool, you find out at runtime when the output is wrong.

### The Pattern

Define agents as **compositions of typed slots**, where each slot has structural requirements and slots have relational obligations to each other.

```
Agent = Slot_A × Slot_B × Slot_C × ...

Validation:
  1. Per-slot: does each slot satisfy its own shape requirements?
  2. Cross-slot: do slots satisfy relational obligations between them?
  3. Bundle: does the full composition form a coherent agent?
```

### Slot Types (Conceptual)

| Slot | What it defines | Example constraints |
|------|----------------|-------------------|
| **Persona** | Voice, stance, decision patterns | Must have a communication style. Must have a decision bias. |
| **Domain** | Expertise areas, vocabulary, cost model | Must cover at least one expertise area. Vocabulary must be non-empty. |
| **Governance** | Risk thresholds, enforcement levels, scope | Enforcement level must be compatible with domain risk profile. |
| **Actions** | Available operations, effort estimates | Action types must be covered by domain expertise. |

### Relational Obligations

The power of this pattern is in the **cross-slot validation**. Examples:

- **Domain expertise must cover action types.** If the agent can perform "vulnerability scan" actions, its domain must include security expertise. An agent that can act outside its expertise is dangerous.
- **Governance scope must cover domain scope.** An agent with broad domain expertise but narrow governance guardrails has blind spots.
- **Action effort must be compatible with governance risk tolerance.** High-effort actions (deploy to production, delete data) require proportional governance thresholds.

### Why This Matters

Contract-first design catches configuration errors that prompt engineering can't:

| Failure | Prompt-based agent | Contract-first agent |
|---------|-------------------|---------------------|
| Agent acts outside its expertise | Bad output discovered at runtime | Build-time validation error |
| Governance gaps | Discovered via incident | Cross-slot validation catches it |
| Incompatible action/domain pairing | Subtle quality degradation | Relational obligation fails |

### Implementation Approach

Define a validation function that checks:
1. Each slot satisfies its own type requirements (shape validation)
2. Required cross-slot relationships hold (relational validation)
3. The full bundle passes coherence checks (bundle validation)

The validation function should be the **same algorithm at every scale** — validate a slot, validate a bundle of slots, validate a system of bundles. Fractal validation.

> **Reference implementation:** [@stackbilt/contracts](https://github.com/Stackbilt-dev/contracts) provides a contract ontology and validation primitives for this pattern.

---

## Pattern 2: Correspondence Governance

**Compute structural harmony between agent slots using a relationship matrix.** Detect internal tensions before they produce bad output.

### The Problem

When an agent has multiple configuration dimensions (persona, domain, governance, actions), these dimensions can be in tension:

- A cautious persona paired with aggressive actions
- A narrow governance scope paired with broad domain expertise
- A high-risk action set paired with low enforcement thresholds

Most frameworks detect these tensions *after* the agent produces output — through quality evaluation or user complaints. By then, the agent has already acted.

### The Pattern

Define a **relationship matrix** between abstract element types. Each slot in the agent is tagged with an element. The matrix computes the structural relationship between any two slots.

Relationship types:

| Relationship | Meaning | Signal |
|-------------|---------|--------|
| **Sympathetic** | Slots reinforce each other | Strong configuration — slots pull in the same direction |
| **Antagonistic** | Slots are in tension | Configuration conflict — requires explicit resolution |
| **Neutral** | Slots are independent | No interaction — neither helping nor hurting |
| **Transcendent** | One slot transforms the other | Emergent capability — the combination creates something neither slot has alone |

### How It Works

1. Tag each agent slot with an element type (from your domain's element system)
2. Define critical **slot pairs** — which slot relationships matter most
3. Compute the relationship for each critical pair using the matrix
4. **Sympathetic/Transcendent pairs:** configuration is sound
5. **Antagonistic pairs:** flag for resolution — either change the configuration or explicitly acknowledge the tension
6. **Neutral pairs:** no action needed

### What This Gives You

- **Pre-runtime governance:** Tensions surface during configuration, not execution
- **Explainable decisions:** When an agent resolves a tension, the resolution is part of the output — the agent shows its work
- **Audit trail:** Every slot relationship is computed and logged. You can trace why an agent behaved a certain way back to its structural configuration

### Design Note

The element system is domain-specific. A security domain might use elements like `offensive/defensive/analytical/operational`. A creative domain might use `structured/freeform/collaborative/individual`. The matrix and the computation are generic; the elements are yours.

The power scales with the number of critical pairs you define. Start with 2 pairs for simple agents, add more as the agent's complexity grows.

> **Reference implementation:** This pattern is implemented in the [TarotScript](https://github.com/Stackbilt-dev/tarotscript) runtime, which uses a 5-element correspondence matrix to compute dignity between agent positions.

---

## Pattern 3: Deterministic Intent Classification

**Route tasks without LLM calls.** Use pre-scored property matching against a structured knowledge base to classify intent deterministically.

### The Problem

Every agent router in the wild makes at least one LLM call to classify the incoming task. That means:
- **Cost** per classification (token spend)
- **Latency** per classification (inference time)
- **Non-determinism** (same input can route differently on different runs)
- **Opacity** (hard to debug why a task was routed where it was)

For high-volume systems, this adds up fast. For safety-critical systems, non-determinism is a liability.

### The Pattern

Instead of asking an LLM "what kind of task is this?", pre-score a structured knowledge base against the task description using keyword, trait, and property matching.

The classification process:

1. **Define a classification vocabulary** — a structured set of categories, each with associated keywords, traits, and properties
2. **Score each category** against the input using property matching (string containment, keyword overlap, trait alignment)
3. **Use a multi-position selection process** — not just "pick the highest score" but a structured decision with primary classification, contextual refinement, and tiebreaker resolution
4. **Emit structured facts** — the classification output is a set of typed facts (category, confidence, complexity, suggested executor) that downstream systems consume

### What This Gives You

| Dimension | LLM-based routing | Deterministic routing |
|-----------|-------------------|----------------------|
| Cost | Tokens per classification | Zero |
| Latency | Inference time (100ms-2s) | Near-zero (<5ms) |
| Determinism | Non-deterministic | Same input → same output, always |
| Debuggability | "The model decided" | Full scoring trace |
| Reproducibility | No guarantee | Perfect (seed-based) |

### When to Use This

- **High-volume routing** where LLM cost per classification is prohibitive
- **Safety-critical routing** where non-determinism is a liability
- **Audit-sensitive systems** where you need to explain every routing decision
- **First-stage routing** in a hierarchical router — use deterministic classification for the coarse stage, LLM for fine-grained stage if needed

### When NOT to Use This

- Tasks with highly ambiguous intent that genuinely requires reasoning
- Very small task volume where LLM cost is negligible
- Rapidly evolving classification categories that change faster than you can update the knowledge base

### Design Note

The knowledge base (classification vocabulary) needs maintenance. When new task types emerge, you add them to the vocabulary. This is a tradeoff: zero runtime cost in exchange for explicit vocabulary management. In practice, most systems have a stable core of 15-30 task types that cover 90%+ of traffic.

> **Reference implementation:** The [TarotScript](https://github.com/Stackbilt-dev/tarotscript) classify-cast uses a three-position spread with relevance-scored draws against a structured deck to achieve deterministic intent classification.

---

## Pattern 4: Behavioral Memory

**Memory that changes how the agent acts, not just what it knows.** Memory depletion, fatigue, and promotion create agents whose behavior evolves with experience.

### The Problem

Most agent memory systems are passive stores:
- Store a fact → Retrieve it later
- Vector similarity → Find relevant memories

The agent's *behavior* doesn't change based on its memory state. An agent with 1,000 memories behaves identically to one with 10, except it has more facts to retrieve. Memory is a database, not a cognitive state.

### The Pattern

Implement memory as a **multi-zone lifecycle** where the zone a memory occupies determines its behavioral impact.

| Zone | Access pattern | Behavioral impact |
|------|---------------|------------------|
| **Intake** | Write-only (newly acquired) | No impact yet — needs consolidation |
| **Active** | Read/write (confirmed memories) | Available for reasoning. Frequent access increases salience. |
| **Crystallized** | Read-only (high-confidence insights) | Stable knowledge — informs decisions but doesn't change |
| **Identity** | Read-only, protected | Core memories that define the agent's character — exempt from decay |

### The Lifecycle

```
New memory → Intake (cold)
    ↓ consolidation cycle
Active (hot) — available for reasoning
    ↓ high access count + high confidence
Crystallized (stable) — promoted to durable knowledge
    ↓ explicit reservation
Identity (protected) — load-bearing, exempt from depletion
```

### What Makes This Different: Fatigue as Governance

**The key insight:** Track memory depletion. As an agent's active memory zone is drawn down (memories accessed, used, expired), the agent's behavioral thresholds change.

- **High active memory:** Agent is flexible, exploratory, draws on a wide range of experience
- **Low active memory (fatigued):** Agent becomes more habitual, relies on crystallized knowledge, raises thresholds for novel action

This creates **emergent behavioral governance** — you don't have to program "be cautious when tired." The memory state itself produces cautious behavior through reduced optionality.

### Observable Metrics

Memory state produces measurable cognitive metrics:

- **Diversity** — how varied are the active memories? (Information entropy across categories)
- **Depletion ratio** — what fraction of active memories are still drawable?
- **Crystallization rate** — how quickly are memories being promoted to durable knowledge?

These metrics give you a window into the agent's cognitive state, not just its knowledge state.

### Design Note

The consolidation cycle (moving memories between zones) can be time-based, access-based, or event-based. A natural pattern is to run consolidation at regular intervals — similar to sleep cycles, where the agent's memory is reorganized and low-salience memories decay.

The identity zone is critical for long-running agents. Without it, core memories (mission, constraints, key relationships) can decay over time, causing identity drift.

> **Reference implementation:** The [TarotScript](https://github.com/Stackbilt-dev/tarotscript) memory deck implements a multi-zone lifecycle with consolidation cycles and entropy-based cognitive metrics.

---

## Pattern 5: Typed Position Pipelines

**Pipeline stages with structural constraints on what can fill each position.** Not just "run these agents in sequence" but "this stage requires an agent with specific structural properties."

### The Problem

In a standard sequential pipeline, any agent can fill any stage:

```
Stage 1 → Stage 2 → Stage 3 → Stage 4
(any agent)  (any agent)  (any agent)  (any agent)
```

This provides no structural guarantee that the right kind of agent is doing the right kind of work at each stage. A governance-stage agent could end up in a scouting stage, or a data-gathering agent could end up making final decisions.

### The Pattern

Define each pipeline position with **structural constraints** — requirements on the agent type, capability tier, or governance level that can fill that position.

Example 4-position pipeline:

| Position | Role | Structural constraint |
|----------|------|--------------------|
| **Scout** | Gather information, observe | Must be observation-tier (low authority, high perceptual breadth) |
| **Agent** | Act on gathered information | Any tier (matched to task requirements) |
| **Counsel** | Synthesize meaning, advise | Must have analytical capability |
| **Sovereign** | Make the final decision | Must be governance-tier (high authority, accountability) |

### What This Gives You

- **Structural guarantees:** A scout can't accidentally make governance decisions. A sovereign can't skip the observation phase.
- **Compositional pipelines:** Swap agents in and out of positions as long as they satisfy the position's constraints. Different agents for different tasks, same pipeline structure.
- **Dignity computation:** Compute the structural relationship between adjacent positions (scout ↔ agent, counsel ↔ sovereign). If they're antagonistic, the pipeline has a structural tension that should be surfaced.

### Design Note

The constraint system can be as simple as "must have capability X" or as rich as a full contract validation (Pattern 1). Start simple — typed positions with one constraint each — and add richness as your system matures.

The value of typed positions compounds with the number of pipelines you build. Once you've defined what "observation-tier" and "governance-tier" mean, you can compose new pipelines quickly because the constraints carry meaning.

> **Reference implementation:** The [TarotScript](https://github.com/Stackbilt-dev/tarotscript) pipeline-cast implements a 4-position typed pipeline with court-rank constraints and dignity computation between adjacent positions.

---

## How These Primitives Compose

The five primitives are building blocks that reinforce each other:

```
Contract-First Design
  └─ validates agent structure
      └─ Correspondence Governance
          └─ detects tensions between validated slots
              └─ Deterministic Classification
                  └─ routes tasks without LLM cost
                      └─ Typed Position Pipelines
                          └─ ensures the right agent fills the right stage
                              └─ Behavioral Memory
                                  └─ agent behavior evolves with experience
```

A fully realized agent system uses all five:
1. Agents are **contract-validated** at build time
2. Internal tensions are **detected via correspondence** before execution
3. Tasks are **classified deterministically** for fast, auditable routing
4. Pipelines use **typed positions** to enforce structural guarantees
5. Agent behavior **evolves through memory** lifecycle

Each primitive is useful independently. The combination is the moat.

---

## Further Reading

- [Agent Routing Patterns](agent-routing.md) — coordination-layer routing (complements deterministic classification)
- [Shared Context Patterns](shared-context.md) — coordination-layer context sharing (complements behavioral memory)
- [Coordination Patterns](coordination.md) — pipeline topologies (complements typed position pipelines)
- [Evaluation Framework](evaluation.md) — measuring system-level coordination quality
- [Reference Architectures](reference-architectures.md) — concrete examples composing coordination + primitive patterns

---
title: "Agent Routing Patterns"
category: "frameworks/mcpa/patterns"
tags: ["multi-agent", "routing", "dispatch", "coordination", "mcpa"]
created: "2026-04-07"
updated: "2026-04-07"
version: "2.0"
---

# Agent Routing Patterns

How to analyze a task and dispatch it to the right agent(s). The routing layer is the most consequential design decision in a multi-agent system — get it wrong and every downstream agent suffers from misaligned context.

## Pattern 1: Capability Router

**The simplest pattern.** Each agent declares its capabilities. The router matches task requirements to agent capabilities.

### When to use
- You have a small, stable set of agents (2-8)
- Tasks map cleanly to one agent's domain
- You need deterministic, explainable routing

### How it works

```
Task arrives
  → Extract required capabilities from task description
  → Score each agent by capability match
  → Route to highest-scoring agent
  → If tie: prefer the agent with narrower scope (specialist > generalist)
```

### Implementation

```python
# Capability router — the building block for everything else
agents = {
    "security": {
        "capabilities": ["vulnerability-analysis", "auth-review", "threat-modeling"],
        "description": "Reviews code and architecture for security issues"
    },
    "architecture": {
        "capabilities": ["system-design", "api-design", "scaling", "tradeoff-analysis"],
        "description": "Evaluates architecture decisions and proposes structures"
    },
    "implementation": {
        "capabilities": ["code-generation", "debugging", "testing", "refactoring"],
        "description": "Writes, fixes, and improves code"
    }
}

def route(task: str, agents: dict) -> str:
    """Route task to best agent based on capability match."""
    # Option A: Keyword matching (fast, brittle)
    # Option B: LLM classifier (slower, flexible) — preferred
    required_capabilities = classify_task(task)  # LLM call

    scores = {}
    for agent_id, agent in agents.items():
        overlap = len(set(required_capabilities) & set(agent["capabilities"]))
        scores[agent_id] = overlap

    # Tiebreak: prefer specialist (fewer total capabilities)
    best = max(scores, key=lambda a: (scores[a], -len(agents[a]["capabilities"])))
    return best
```

### Failure mode
Task doesn't match any agent well. **Fix:** Add a fallback/generalist agent, or escalate to human.

---

## Pattern 2: Confidence-Based Routing

**Agents bid on tasks.** Each agent receives the task, estimates its confidence in handling it, and the router picks the highest-confidence agent.

### When to use
- Task boundaries are fuzzy (overlapping agent domains)
- You want agents to self-select
- You can afford the latency of multiple agent calls

### How it works

```
Task arrives
  → Broadcast task to all candidate agents
  → Each agent returns confidence score (0-1) + brief reasoning
  → Route to highest-confidence agent
  → If all scores below threshold: escalate or split the task
```

### Implementation

```python
async def confidence_route(task: str, agents: list) -> str:
    """Let agents bid on tasks with confidence scores."""
    bids = []
    for agent in agents:
        # Each agent gets the task + its own system prompt
        response = await agent.evaluate(
            f"Rate your confidence (0.0-1.0) in handling this task. "
            f"Respond with JSON: {{\"confidence\": float, \"reason\": str}}\n\n"
            f"Task: {task}"
        )
        bids.append({"agent": agent.id, **response})

    # Filter below threshold
    viable = [b for b in bids if b["confidence"] >= 0.6]

    if not viable:
        return "escalate"  # No agent confident enough

    # Highest confidence wins
    return max(viable, key=lambda b: b["confidence"])["agent"]
```

### Failure mode
All agents overestimate their confidence (sycophancy). **Fix:** Add a verification step — after the selected agent responds, run a lightweight quality check.

---

## Pattern 3: Hierarchical Router

**Route in stages.** A coarse classifier picks the domain, then a fine-grained router picks the specific agent within that domain.

### When to use
- You have many agents (8+)
- Agents are organized into logical groups
- You need fast routing even at scale

### How it works

```
Task arrives
  → Stage 1: Classify into domain (engineering, business, creative, ops)
  → Stage 2: Within domain, route to specific agent
  → Optional Stage 3: Sub-specialization
```

### Implementation

```python
# Two-stage router
domains = {
    "engineering": ["security-agent", "architecture-agent", "implementation-agent"],
    "business": ["strategy-agent", "operations-agent", "analytics-agent"],
    "creative": ["content-agent", "design-agent"],
}

def hierarchical_route(task: str) -> str:
    # Stage 1: Domain classification (cheap, fast — can use a small model)
    domain = classify_domain(task)  # Returns "engineering", "business", etc.

    # Stage 2: Agent selection within domain
    candidates = domains[domain]
    return capability_route(task, candidates)  # Reuse Pattern 1
```

### Design note
Stage 1 can use a smaller/cheaper model since domain classification is easier than fine-grained routing. Stage 2 can use a more capable model if needed.

---

## Pattern 4: Content-Driven Router

**Let the task content determine the route.** Instead of classifying the task into categories, analyze the actual content — entities, intent, risk level — and use that to build a routing decision.

### When to use
- Routing decisions depend on content details (who mentioned, what risk level, what entities)
- You need routing that adapts to the content shape, not just topic
- Different aspects of the same task need different agents

### How it works

```
Task arrives
  → Extract structured signals from content:
    - Entities (people, systems, accounts mentioned)
    - Intent (question, action request, report)
    - Risk level (involves money, security, production)
    - Urgency signals
  → Apply routing rules against extracted signals
  → May route to multiple agents (fan-out) if signals span domains
```

### Implementation

```python
def content_route(task: str) -> list[str]:
    """Route based on content signals, not just topic."""
    signals = extract_signals(task)  # LLM call → structured output

    agents = []

    # Rule-based routing on extracted signals
    if signals.mentions_production or signals.risk_level == "high":
        agents.append("security-agent")

    if signals.involves_money or signals.mentions_billing:
        agents.append("operations-agent")

    if signals.is_architecture_question:
        agents.append("architecture-agent")

    if not agents:
        agents.append("generalist-agent")  # Fallback

    return agents  # May return multiple → triggers fan-out coordination
```

### Why this beats topic classification
A message like "Can we change the auth flow to skip MFA for internal users?" would be classified as "engineering" by a topic classifier. But content-driven routing detects: auth (security), internal users (policy), flow change (architecture) — and can fan out to multiple agents.

---

## Pattern 5: Escalation Chain

**Try cheap, escalate expensive.** Route to the simplest agent first. If it can't handle the task (low confidence, error, or explicit escalation), pass to a more capable agent.

### When to use
- You want to minimize cost/latency for simple tasks
- You have agents at different capability (and cost) tiers
- Most tasks are routine, few are complex

### How it works

```
Task arrives
  → Route to Tier 1 agent (fast, cheap)
  → If Tier 1 resolves with high confidence: done
  → If Tier 1 flags uncertainty or fails: escalate to Tier 2
  → If Tier 2 can't resolve: escalate to Tier 3 or human
```

### Implementation

```python
async def escalation_route(task: str, tiers: list[Agent]) -> dict:
    """Try each tier until one resolves the task."""
    context = {"task": task, "attempts": []}

    for tier, agent in enumerate(tiers):
        result = await agent.handle(task, context=context)

        context["attempts"].append({
            "agent": agent.id,
            "tier": tier,
            "confidence": result.confidence,
            "resolved": result.resolved
        })

        if result.resolved and result.confidence >= 0.8:
            return {"agent": agent.id, "result": result, "tier": tier}

    # All tiers exhausted
    return {"agent": "human", "context": context, "tier": "escalated"}
```

### Key insight
Each tier passes its context (what it tried, what failed, what it's uncertain about) to the next tier. The expensive agent doesn't start from scratch — it starts from where the cheap agent got stuck.

---

## Anti-Patterns

### The God Router
A single LLM call that makes every routing decision with a massive system prompt listing all agents and their capabilities. Works at 5 agents. Falls apart at 15. **Fix:** Use hierarchical routing.

### The Eager Fan-Out
Sending every task to every agent "just in case." Expensive, slow, and creates a synthesis problem downstream. **Fix:** Route to 1-2 agents max. Fan out only when content analysis demands it.

### The Rigid Taxonomy
Building routing around a fixed category taxonomy ("engineering", "business", "creative"). Real tasks don't respect these boundaries. **Fix:** Use content-driven routing or confidence-based routing.

### Routing Without Context
Making routing decisions based only on the current message, ignoring conversation history. The same message means different things in different contexts. **Fix:** Include recent conversation context in the routing decision.

---

## Choosing a Pattern

```
How many agents?
  ├─ 2-4 → Capability Router (Pattern 1)
  ├─ 4-8 → Confidence-Based (Pattern 2) or Content-Driven (Pattern 4)
  └─ 8+  → Hierarchical Router (Pattern 3)

Are task boundaries fuzzy?
  ├─ Yes → Confidence-Based (Pattern 2)
  └─ No  → Capability Router (Pattern 1)

Do you need cost optimization?
  ├─ Yes → Escalation Chain (Pattern 5)
  └─ No  → Direct routing

Do tasks span multiple domains?
  ├─ Yes → Content-Driven (Pattern 4) + fan-out
  └─ No  → Single-agent routing
```

You'll likely combine patterns. A production system might use Hierarchical (Pattern 3) for stage 1, then Confidence-Based (Pattern 2) for stage 2, with an Escalation Chain (Pattern 5) as the fallback.

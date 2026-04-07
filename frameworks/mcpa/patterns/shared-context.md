---
title: "Shared Context Patterns"
category: "frameworks/mcpa/patterns"
tags: ["multi-agent", "context", "state", "memory", "coordination", "mcpa"]
created: "2026-04-07"
updated: "2026-04-07"
version: "2.0"
---

# Shared Context Patterns

How multiple agents share what they've learned without losing provenance, conflicting, or drowning in noise. This is the hardest coordination problem — tool use is solved (MCP), routing is well-understood, but shared context is still where most multi-agent systems break down.

## The Core Problem

Agent A discovers something. Agent B needs that discovery to do its job. What seems simple becomes hard fast:

- **Who said what?** If Agent B uses Agent A's insight, the user needs to know where it came from.
- **How confident is it?** A hunch from a security scan is different from a verified test result.
- **What if they disagree?** Two agents analyzing the same data may reach opposite conclusions.
- **How much context?** Sharing everything drowns the next agent. Sharing nothing makes it start from scratch.

## Pattern 1: Insight Ledger

**The foundational pattern.** A shared, append-only log of insights from all agents, with provenance and confidence metadata.

### When to use
- Any multi-agent system where agents need to build on each other's work
- When you need an audit trail of what each agent contributed
- When downstream agents need to filter insights by confidence or source

### Structure

```json
{
  "ledger": [
    {
      "id": "insight-001",
      "source_agent": "security-reviewer",
      "timestamp": "2026-04-07T14:30:00Z",
      "content": "SQL injection risk in user input handler at api/users.ts:45",
      "confidence": 0.92,
      "evidence": "Unparameterized query concatenation with req.body.name",
      "tags": ["security", "sql-injection", "high-severity"],
      "supersedes": null
    },
    {
      "id": "insight-002",
      "source_agent": "architecture-reviewer",
      "timestamp": "2026-04-07T14:30:05Z",
      "content": "User module has no input validation layer — all validation is inline",
      "confidence": 0.88,
      "evidence": "No middleware or schema validation in routes/users.ts",
      "tags": ["architecture", "validation", "medium-severity"],
      "supersedes": null
    },
    {
      "id": "insight-003",
      "source_agent": "security-reviewer",
      "timestamp": "2026-04-07T14:31:00Z",
      "content": "Previous SQL injection finding confirmed after deeper analysis — parameterized queries needed throughout",
      "confidence": 0.97,
      "evidence": "Found 3 additional unparameterized queries in same module",
      "tags": ["security", "sql-injection", "high-severity"],
      "supersedes": "insight-001"
    }
  ]
}
```

### Key fields

| Field | Why it matters |
|-------|---------------|
| `source_agent` | Provenance — who said this? |
| `confidence` | How sure? 0.5 = educated guess, 0.9+ = verified |
| `evidence` | What's backing this up? Without evidence, insights are hearsay |
| `tags` | Downstream agents filter by tag to get relevant context |
| `supersedes` | When an agent updates its own finding, link to the original |

### Implementation

```python
class InsightLedger:
    def __init__(self):
        self.insights = []

    def record(self, agent_id: str, content: str, confidence: float,
               evidence: str = "", tags: list = None, supersedes: str = None):
        insight = {
            "id": f"insight-{len(self.insights) + 1:03d}",
            "source_agent": agent_id,
            "timestamp": now(),
            "content": content,
            "confidence": confidence,
            "evidence": evidence,
            "tags": tags or [],
            "supersedes": supersedes,
        }
        self.insights.append(insight)
        return insight["id"]

    def query(self, tags: list = None, min_confidence: float = 0.0,
              agent: str = None) -> list:
        """Query insights with filters."""
        results = self.insights
        if tags:
            results = [i for i in results if set(tags) & set(i["tags"])]
        if min_confidence:
            results = [i for i in results if i["confidence"] >= min_confidence]
        if agent:
            results = [i for i in results if i["source_agent"] == agent]
        return results

    def current(self) -> list:
        """Return only non-superseded insights."""
        superseded_ids = {i["supersedes"] for i in self.insights if i["supersedes"]}
        return [i for i in self.insights if i["id"] not in superseded_ids]
```

### Failure mode
Ledger grows unbounded in long-running systems. **Fix:** Apply decay — insights older than N turns or below a confidence threshold get summarized or pruned.

---

## Pattern 2: Context Briefing

**Summarize, don't pass through.** Before an agent starts work, compose a briefing from the ledger that contains only what that agent needs.

### When to use
- Context windows are limited
- Different agents need different subsets of shared context
- You want to control the signal-to-noise ratio each agent sees

### How it works

```
Agent B is about to run
  → Query ledger for insights relevant to Agent B's domain
  → Filter by confidence threshold (skip low-confidence noise)
  → Summarize into a briefing (not raw dump)
  → Inject briefing into Agent B's system prompt or context
```

### Implementation

```python
def compose_briefing(ledger: InsightLedger, target_agent: dict) -> str:
    """Build a context briefing for the target agent."""
    # Get relevant insights based on agent's domain tags
    relevant = ledger.query(
        tags=target_agent["domain_tags"],
        min_confidence=0.7
    )

    if not relevant:
        return ""

    # Format as briefing
    lines = ["## Prior Findings (from other agents)", ""]
    for insight in relevant:
        conf_label = "verified" if insight["confidence"] >= 0.9 else "likely"
        lines.append(
            f"- [{conf_label}] **{insight['source_agent']}**: "
            f"{insight['content']}"
        )

    lines.append("")
    lines.append("Build on these findings. Do not re-investigate confirmed items.")
    return "\n".join(lines)
```

### Design note
The briefing should be opinionated about what to include. A security agent doesn't need the content writer's style notes. A summarization step (even a cheap LLM call) that distills relevant insights into 3-5 bullet points is better than dumping 50 raw ledger entries.

---

## Pattern 3: Conflict Resolution

**When agents disagree, make the disagreement explicit.** Don't silently pick a winner — surface the conflict and resolve it through structure.

### When to use
- Multiple agents analyze the same data and reach different conclusions
- High-stakes decisions where being wrong is expensive
- You want to avoid the "loudest agent wins" failure mode

### Resolution strategies

**Strategy A: Confidence-Weighted**
```python
def resolve_by_confidence(conflicts: list[dict]) -> dict:
    """Higher confidence wins."""
    return max(conflicts, key=lambda c: c["confidence"])
```
Simple but fragile. An overconfident agent always wins.

**Strategy B: Evidence-Weighted**
```python
def resolve_by_evidence(conflicts: list[dict]) -> dict:
    """More evidence wins."""
    return max(conflicts, key=lambda c: len(c.get("evidence", "")))
```
Better — rewards agents that show their work.

**Strategy C: Supervisor Arbitration**
```python
async def resolve_by_supervisor(conflicts: list[dict], supervisor: Agent) -> dict:
    """A supervisor agent reviews the conflict and decides."""
    prompt = format_conflict_for_review(conflicts)
    decision = await supervisor.decide(prompt)
    return decision
```
Best for high-stakes decisions. The supervisor sees both sides and the evidence.

**Strategy D: Surface to User**
```python
def resolve_by_human(conflicts: list[dict]) -> dict:
    """Present the conflict to the user for resolution."""
    return {
        "status": "conflict",
        "positions": conflicts,
        "question": "These agents disagree. Which perspective should guide the decision?"
    }
```
The nuclear option. Use when automated resolution isn't trustworthy.

### Conflict detection

```python
def detect_conflicts(ledger: InsightLedger) -> list[list[dict]]:
    """Find insights that contradict each other."""
    conflicts = []
    current = ledger.current()

    for i, a in enumerate(current):
        for b in current[i + 1:]:
            # Same topic, different conclusions
            if (set(a["tags"]) & set(b["tags"])
                and a["source_agent"] != b["source_agent"]):
                # Use LLM to check if they actually conflict
                if are_contradictory(a["content"], b["content"]):
                    conflicts.append([a, b])

    return conflicts
```

---

## Pattern 4: Progressive Context

**Start lean, enrich on demand.** Don't front-load agents with all available context. Give them the minimum, let them request more.

### When to use
- Context windows are tight
- Most tasks don't need all available context
- You want agents to work fast by default, deep when needed

### How it works

```
Agent starts with:
  - Task description
  - Minimal briefing (Pattern 2, top 3 insights only)

Agent can request:
  - "What has been said about [topic]?" → Query ledger by tag
  - "What did [other agent] find?" → Query ledger by source
  - "What's the full evidence for [insight]?" → Retrieve specific insight + evidence
```

### Implementation

```python
class ContextProvider:
    """Provides on-demand context to agents."""

    def __init__(self, ledger: InsightLedger):
        self.ledger = ledger

    def minimal_briefing(self, agent: dict) -> str:
        """Top 3 most relevant, highest-confidence insights."""
        relevant = self.ledger.query(
            tags=agent["domain_tags"],
            min_confidence=0.8
        )
        return format_top_n(relevant, n=3)

    def on_topic(self, topic: str) -> str:
        """Everything known about a specific topic."""
        return format_insights(self.ledger.query(tags=[topic]))

    def from_agent(self, agent_id: str) -> str:
        """Everything a specific agent has found."""
        return format_insights(self.ledger.query(agent=agent_id))

    def full_evidence(self, insight_id: str) -> str:
        """Full evidence for a specific insight."""
        insight = next(
            (i for i in self.ledger.insights if i["id"] == insight_id), None
        )
        return insight["evidence"] if insight else "Not found"
```

### Design note
This pattern works especially well with tool-using agents. Expose the context provider as a tool the agent can call, and it will pull context when it actually needs it rather than being front-loaded with everything.

---

## Pattern 5: Context Decay

**Old insights are worth less than new ones.** In long-running systems, shared context accumulates endlessly. Without decay, agents drown in stale findings.

### When to use
- Long-running agent systems (hours, days)
- High-volume environments where insights accumulate fast
- Systems where early findings are frequently superseded

### Decay strategies

**Time-based decay:**
```python
def apply_time_decay(ledger: InsightLedger, half_life_hours: float = 24):
    """Reduce confidence of old insights over time."""
    for insight in ledger.insights:
        age_hours = hours_since(insight["timestamp"])
        decay_factor = 0.5 ** (age_hours / half_life_hours)
        insight["effective_confidence"] = insight["confidence"] * decay_factor
```

**Supersession-based pruning:**
```python
def prune_superseded(ledger: InsightLedger):
    """Remove insights that have been superseded by newer findings."""
    superseded = {i["supersedes"] for i in ledger.insights if i["supersedes"]}
    ledger.insights = [i for i in ledger.insights if i["id"] not in superseded]
```

**Consolidation (summarize + prune):**
```python
async def consolidate(ledger: InsightLedger, summarizer: Agent):
    """Periodically summarize old insights into a digest."""
    old = [i for i in ledger.insights if hours_since(i["timestamp"]) > 24]
    if len(old) < 10:
        return  # Not worth consolidating yet

    summary = await summarizer.summarize(old)
    ledger.record(
        agent_id="consolidator",
        content=summary,
        confidence=0.85,
        tags=["digest"],
    )
    # Remove the individual old insights
    old_ids = {i["id"] for i in old}
    ledger.insights = [i for i in ledger.insights if i["id"] not in old_ids]
```

---

## Anti-Patterns

### The Telephone Game
Agent A tells Agent B, which tells Agent C. By Agent C, the insight is distorted. **Fix:** All agents read from the shared ledger, never from each other directly.

### The Context Dump
Passing the entire conversation history to every agent. 90% of it is irrelevant to the agent's task, and the signal is buried. **Fix:** Use Context Briefing (Pattern 2) with aggressive filtering.

### The Invisible Assumption
Agent B builds on Agent A's insight without recording that dependency. When Agent A's insight is later revised, Agent B's work isn't invalidated. **Fix:** Track insight dependencies explicitly, or re-run downstream agents when upstream insights change.

### Confidence Inflation
Agents consistently report 0.9+ confidence because there's no calibration. **Fix:** Periodically verify a sample of insights against ground truth and adjust agent confidence calibration.

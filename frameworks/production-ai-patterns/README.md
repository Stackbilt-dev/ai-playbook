# Production AI Patterns

Patterns for building AI systems that hold up in production. Not prompt tricks — architectural decisions that determine whether your system is correct, auditable, and trustworthy.

These patterns emerged from real failure modes in systems that ran Claude-based agents at scale. Each one names a class of problem, explains why it happens, and shows how to structure your system to avoid it.

## The Core Tension

Most AI engineering guidance focuses on getting better outputs from a single model call. Production AI engineering is about something harder: **getting reliable, verifiable behavior across hundreds of model calls, over time, with state that evolves.**

The patterns here address that harder problem.

## Patterns

### [Selection, Not Generation](selection-not-generation.md)

When your output space is bounded, route work away from free-form generation toward deterministic selection. Generation is for last-mile synthesis, not routing, classification, or lookup.

**Use when:** Classification, routing, entity extraction, retrieval, linting, any task with a finite correct output set.

---

### [Silence Is Not Absence](silence-is-not-absence.md)

The most common hallucination class in agentic systems: treating no signal as confirmation of state, truth, or completion. The LLM fills the context gap with a plausible fabrication.

**Use when:** Designing any system that reads external state, checks conditions, or verifies completion before acting.

---

### [Ground Before Dispatch](ground-before-dispatch.md)

Attach verified facts to the model context before asking it to generate a response. A model that cannot hallucinate because the facts are already present cannot fill gaps with fabrication.

**Use when:** Building dispatcher/executor architectures, RAG systems, or any agentic loop where the model's output drives further action.

---

### [Substrate Routing](substrate-routing.md)

Different query types belong to different data sources. Routing an operational query to a semantic store — or a factual lookup to a generative model — is a substrate mismatch that produces confident wrong answers.

**Use when:** Designing multi-substrate AI systems (DB + vector store + LLM + structured API).

---

## Relationship to Other Frameworks

These patterns are **architectural**, not conversational. They operate at the system design level, not the prompt level.

| Layer | Frameworks |
|-------|-----------|
| Conversation / reasoning | ADHD Prompting, Context Engineering, Fractal, Vibecoding |
| System architecture | **Production AI Patterns**, MCPA |
| Multi-agent coordination | MCPA patterns |

For multi-agent systems, combine Production AI Patterns with [MCPA](../mcpa/) for coordination and [Context Engineering](../context-engineering/) for managing what each agent sees.

## When to Apply

Start with **Selection, Not Generation** — it's the highest-leverage change in most systems. Then add **Ground Before Dispatch** for any agentic loop. Add **Substrate Routing** when you have multiple data sources. Apply **Silence Is Not Absence** as a review lens across all decision points.

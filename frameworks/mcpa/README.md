# MCPA v3 — Multi-Actor Coordination Pattern Architecture

A pattern language for building systems where AI agents, deterministic services, humans, policy gates, state machines, and external tools work together. Framework-agnostic — works with Claude Agent SDK, LangGraph, CrewAI, AutoGen, raw API calls, or mixed architectures.

## The Problem

Agent tools are everywhere. But real systems coordinate more than agents: a classifier may route, a database may hold lifecycle state, a policy may block an action, and a human may be the only actor allowed to commit an external side effect. Most frameworks model the reasoning and omit the workflow that makes it safe and useful.

MCPA documents both cognitive coordination and governed workflow patterns, so you can apply them deliberately instead of discovering them through incidents.

## Patterns

### Coordination Layer
How agents work together:

| Pattern | What it solves | Start here if... |
|---------|---------------|-----------------|
| [Agent Routing](patterns/agent-routing.md) | Which agent handles which task? | You have 2+ agents and need to dispatch work |
| [Shared Context](patterns/shared-context.md) | How do agents share what they've learned? | Agents need to build on each other's work |
| [Coordination](patterns/coordination.md) | How do agents work together on one task? | You need agents to collaborate, not just take turns |
| [Evaluation](patterns/evaluation.md) | How do you measure if the system is working? | You're past the prototype stage |

### Agent Primitives
How to build agents that are structurally sound before they interact:

| Pattern | What it solves | Start here if... |
|---------|---------------|-----------------|
| [Agent Primitives](patterns/agent-primitives.md) | Contract-first design, structural governance, deterministic routing, behavioral memory, typed pipelines | You're building agents, not just orchestrating them |

### Governed Workflow Layer
How mixed actors move durable work toward an outcome without exceeding authority:

| Pattern | What it solves | Start here if... |
|---------|---------------|-----------------|
| [Governed Actor Primitives](patterns/governed-actor-primitives.md) | Capability, authority, evidence, state access, and outcome contracts | Agents act inside real business processes |
| [Work-Item Lifecycle](patterns/work-item-lifecycle.md) | Durable state, transitions, protected states, and history | Work lasts longer than one model invocation |
| [Authority-Aware Routing](patterns/authority-routing.md) | Execute, draft, propose, approve, hold, or deny | Capability alone must not grant permission |
| [Evidence Gates](patterns/evidence-gates.md) | Required facts before a transition can advance | Missing evidence must block fabrication |
| [Commitment Gates](patterns/commitment-gates.md) | Separate preparation, approval, and external execution | Agents can trigger side effects |
| [Workflow Evaluation](patterns/workflow-evaluation.md) | Safety, lifecycle integrity, and outcome value | Coordination metrics are not enough |

## Reference Architectures

Concrete examples showing how patterns compose into real systems:

| Architecture | Agents | Patterns Used |
|-------------|--------|--------------|
| [Code Review Pipeline](patterns/reference-architectures.md#code-review-pipeline) | 3 | Sequential + Shared Context + Evaluation |
| [Research Desk](patterns/reference-architectures.md#research-desk) | 4 | Fan-Out + Shared Context + Supervisor |
| [Cognitive Kernel](patterns/reference-architectures.md#cognitive-kernel) | 5+ | Router + Shared Context + Debate + Evaluation |
| [Governed Revenue Funnel](patterns/governed-revenue-funnel.md) | Mixed actors | Lifecycle + Authority + Evidence + Commitment + Outcomes |

## Quick Start

**I have 2 agents and need to decide which one handles a task:**
Read [Agent Routing](patterns/agent-routing.md) — start with the Capability Router pattern.

**My agents need to share context without repeating work:**
Read [Shared Context](patterns/shared-context.md) — start with the Insight Ledger pattern.

**I need agents to collaborate on a complex task:**
Read [Coordination](patterns/coordination.md) — pick the topology that matches your problem shape.

**I need to measure whether my multi-agent system is actually working:**
Read [Evaluation](patterns/evaluation.md) — start with the Coordination Quality Score.

**My agents participate in a durable workflow or can affect the outside world:**
Read [Governed Actor Primitives](patterns/governed-actor-primitives.md), then [Work-Item Lifecycle](patterns/work-item-lifecycle.md) and [Commitment Gates](patterns/commitment-gates.md).

**The correct routing result may be “do not act yet”:**
Read [Authority-Aware Routing](patterns/authority-routing.md) and [Evidence Gates](patterns/evidence-gates.md).

## Design Principles

1. **Patterns over protocols.** Describe what to do and why, not wire formats. JSON schemas rot; design patterns survive.

2. **Framework-agnostic.** Every pattern includes pseudocode and explains the concept independent of any SDK. Adapt to your stack.

3. **Production-tested.** These patterns were extracted from systems running in production, not designed in the abstract. Where relevant, we note what went wrong before we got it right.

4. **Compositional.** Patterns are building blocks. The reference architectures show how they compose, but your system will combine them differently. That's the point.

5. **Capability is not authority.** An actor may be able to perform an action without being permitted to perform it now.

6. **State transitions over prose.** In operational workflows, the most important output is often a validated transition, not generated text.

## Origin

MCPA v1 (March 2025) was a protocol specification written when MCP was brand new. It attempted to extend MCP with custom wire protocols for reasoning modules. Most of that is now redundant — MCP itself handles tool orchestration, and LLMs handle modality bridging natively.

What survived: the ideas about agent routing, shared context state, and evaluation metrics. MCPA v2 reframes these as a pattern language for the multi-agent systems that are actually being built today.

MCPA v3 retains that cognitive coordination layer and adds governed workflows. “Actor” is intentionally broader than “agent”: agents reason, but deterministic services, humans, policies, state stores, and external executors participate in the same outcome-bearing system.

The v1 protocol specs are preserved in `archive/` for historical reference.

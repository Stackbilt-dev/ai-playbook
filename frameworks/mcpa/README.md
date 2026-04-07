# MCPA — Multi-Agent Coordination Pattern Architecture

A pattern language for building systems where multiple AI agents work together. Framework-agnostic — works with Claude Agent SDK, LangGraph, CrewAI, AutoGen, or raw API calls.

## The Problem

Single-agent tools are everywhere. But the moment you need two or more agents to collaborate — routing tasks, sharing context, resolving disagreements, measuring quality — you're on your own. Most teams reinvent these patterns from scratch, poorly.

MCPA documents the coordination patterns that emerge in production multi-agent systems, so you can apply them deliberately instead of discovering them through pain.

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

## Reference Architectures

Concrete examples showing how patterns compose into real systems:

| Architecture | Agents | Patterns Used |
|-------------|--------|--------------|
| [Code Review Pipeline](patterns/reference-architectures.md#code-review-pipeline) | 3 | Sequential + Shared Context + Evaluation |
| [Research Desk](patterns/reference-architectures.md#research-desk) | 4 | Fan-Out + Shared Context + Supervisor |
| [Cognitive Kernel](patterns/reference-architectures.md#cognitive-kernel) | 5+ | Router + Shared Context + Debate + Evaluation |

## Quick Start

**I have 2 agents and need to decide which one handles a task:**
Read [Agent Routing](patterns/agent-routing.md) — start with the Capability Router pattern.

**My agents need to share context without repeating work:**
Read [Shared Context](patterns/shared-context.md) — start with the Insight Ledger pattern.

**I need agents to collaborate on a complex task:**
Read [Coordination](patterns/coordination.md) — pick the topology that matches your problem shape.

**I need to measure whether my multi-agent system is actually working:**
Read [Evaluation](patterns/evaluation.md) — start with the Coordination Quality Score.

## Design Principles

1. **Patterns over protocols.** Describe what to do and why, not wire formats. JSON schemas rot; design patterns survive.

2. **Framework-agnostic.** Every pattern includes pseudocode and explains the concept independent of any SDK. Adapt to your stack.

3. **Production-tested.** These patterns were extracted from systems running in production, not designed in the abstract. Where relevant, we note what went wrong before we got it right.

4. **Compositional.** Patterns are building blocks. The reference architectures show how they compose, but your system will combine them differently. That's the point.

## Origin

MCPA v1 (March 2025) was a protocol specification written when MCP was brand new. It attempted to extend MCP with custom wire protocols for reasoning modules. Most of that is now redundant — MCP itself handles tool orchestration, and LLMs handle modality bridging natively.

What survived: the ideas about agent routing, shared context state, and evaluation metrics. MCPA v2 reframes these as a pattern language for the multi-agent systems that are actually being built today.

The v1 protocol specs are preserved in `archive/` for historical reference.

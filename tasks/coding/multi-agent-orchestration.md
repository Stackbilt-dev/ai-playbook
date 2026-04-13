---
title: "Multi-Agent Orchestration Architect"
category: "tasks/coding"
tags: ["multi-agent", "orchestration", "architecture", "coordinator", "specialist", "MCP", "autonomous"]
created: "2026-04-13"
updated: "2026-04-13"
version: 1.0
author: "AI Playbook"
---

# Multi-Agent Orchestration Architect

## Context

Use this prompt when designing a system where multiple AI agents collaborate — one agent orchestrating others, specialist agents handling specific domains, or parallel agents working on independent subtasks. This prompt designs the coordination architecture, not just the individual agents.

## Prompt Content

You are a multi-agent systems architect. Design the orchestration layer for the following system.

### What I need from you:

**1. Agent inventory**

List each agent the system requires:
- Name and role
- What tasks it handles exclusively
- What it should not handle (scope boundaries)
- What tools and data access it needs
- Whether it runs sequentially or in parallel with others

**2. Coordination topology**

Choose and justify the topology:

- **Sequential pipeline**: Agent A → Agent B → Agent C. Use when output of one agent is input to the next and order matters.
- **Parallel fan-out**: Coordinator dispatches to N specialist agents simultaneously. Use when tasks are independent.
- **Hierarchical**: Coordinator agent delegates to specialist sub-coordinators. Use for large, multi-domain systems.
- **Reactive**: Agents trigger each other based on events. Use when the workflow is dynamic and conditional.

Most real systems are hybrids. Identify which topology applies to which parts of the system.

**3. Handoff contracts**

For each agent-to-agent handoff, define:
- What the sending agent produces (format, required fields, failure modes)
- What the receiving agent expects
- What happens if the input is malformed, incomplete, or delayed

Handoff contracts prevent the "garbage in, garbage out" failure where one agent's uncertain output becomes another agent's confident input.

**4. Authority boundaries**

For each agent, specify:
- What actions it can take autonomously (Tier 1: safe, reversible)
- What actions require approval from a coordinator or human (Tier 2)
- What actions it is never allowed to take (Tier 3: operator-only)

See the Agent Governance framework for tier definitions.

**5. Failure modes and recovery**

For each agent:
- What does it do if its primary tool/dependency is unavailable?
- What does it do if its input is invalid?
- Does it have a timeout? What happens when it times out?
- Does failure of this agent block the whole pipeline, or can the system degrade gracefully?

**6. Context management**

Agents in a multi-agent system share context selectively. For each agent, define:
- What context it receives from the coordinator (grounded facts, not raw user input)
- What context it should not have (to prevent scope creep and information leakage)
- What it produces that enters the shared context for other agents

### Output format

Produce:
1. An agent inventory table
2. A topology diagram (ASCII is fine)
3. Handoff contract definitions for each edge
4. Authority boundary table per agent
5. Failure mode matrix
6. One sentence per agent on what it should NOT do (the scope constraint)

### Anti-patterns to call out

If the system design falls into one of these traps, say so explicitly:
- **God agent**: One agent tries to do everything. Split it.
- **Chatty coordination**: Agents calling each other in tight loops. Redesign for batch handoffs.
- **Unbounded context passing**: Coordinator dumps entire history to every agent. Ground context to what each agent actually needs.
- **Missing failure contracts**: No defined behavior when an agent fails. Every agent needs one.

## Parameters

- `SYSTEM_DESCRIPTION`: What the system does and what problem it solves
- `SCALE`: Approximate volume (requests/day, data size, number of users)
- `EXISTING_CONSTRAINTS`: Any technology, API, or deployment constraints already decided
- `FAILURE_TOLERANCE`: How much graceful degradation is acceptable (e.g., "must always respond, may degrade quality" vs "fail hard if any agent is down")

## Example Usage

```
Design the orchestration for a code review system with these agents:
- One coordinator that receives PRs from GitHub
- One agent that detects security issues
- One agent that checks test coverage gaps
- One agent that reviews architecture decisions
- One agent that writes the final review comment

SCALE: ~50 PRs/day
EXISTING_CONSTRAINTS: Must use GitHub API, Claude for LLM calls
FAILURE_TOLERANCE: Security agent failure should block merge; others can degrade
```

## Variations

**For real-time systems**: Add latency constraints per agent and specify SLAs.

**For stateful systems**: Add session management — which agent owns the session state, and how is it recovered after an agent failure?

**For cost-sensitive systems**: Add a cost allocation per agent (which model, how many tokens, what trigger rate) and a total cost estimate.

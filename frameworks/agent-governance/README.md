# Agent Governance Framework

Patterns for running AI agents autonomously without losing control of what they do.

The gap in most agent documentation: **how to let agents run without supervision while guaranteeing they don't do things you didn't sanction.** Enthusiasm for autonomous agents typically outpaces thinking about authority, reversibility, and scope.

This framework is for systems where Claude Code (or another AI agent) runs tasks without a human in the loop — overnight automation, CI-triggered reviews, self-healing pipelines, autonomous research. The patterns apply whenever an agent acts on your behalf in the real world.

## The Governance Problem

Autonomous agents fail in two directions:

1. **Too cautious**: The agent asks for approval on everything. Defeats the purpose of autonomy.
2. **Too permissive**: The agent does things that are irreversible, expensive, or wrong, without any guard.

Good governance draws the line precisely. It defines which actions are safe to run freely, which require approval, and which are never allowed — without requiring a human to review every step.

## Patterns

### [Authority Tiers](authority-tiers.md)

Classify every action the agent can take by its risk profile: autonomously safe, requires approval, or operator-only. Route accordingly.

**Use when:** Building any autonomous agent system with a mix of safe and potentially risky actions.

---

### [Constraint Surfaces](constraint-surfaces.md)

Define what an agent is allowed to do *before* it runs, not at runtime. Constraints built into the system are reliable; constraints in prompts are suggestions.

**Use when:** Deploying agents to production, running overnight tasks, or delegating to AI in shared environments.

---

## Core Vocabulary

**Authority**: The level of sanction an action requires. Not the same as capability — an agent may be *capable* of deploying to production but not *authorized* to do so without approval.

**Reversibility**: Whether an action can be undone. File edits are reversible; production deploys are hard to reverse; deleted records may be gone. Reversibility should directly influence the authority tier assignment.

**Blast radius**: The scope of impact if an action goes wrong. Editing a local file has small blast radius. Pushing to main has large blast radius. Blast radius and reversibility together determine the appropriate authority level.

**Standing orders**: Constraints that are always in effect for an agent, regardless of what the current task asks. Standing orders override task instructions when they conflict.

**Scope creep**: The tendency of autonomous agents to perform adjacent actions not strictly required by the task. Good governance defines scope explicitly and flags out-of-scope actions as errors, not opportunities.

## Relationship to Other Frameworks

Agent governance operates at the **deployment layer** — it determines what the agent is allowed to do, not how it reasons or communicates.

| Concern | Framework |
|---------|-----------|
| What the agent is allowed to do | **Agent Governance** |
| How the agent reasons about problems | Fractal, ADHD Prompting |
| What context the agent has | Context Engineering, Ground Before Dispatch |
| How agents coordinate | MCPA |
| Whether agent outputs are correct | Production AI Patterns |

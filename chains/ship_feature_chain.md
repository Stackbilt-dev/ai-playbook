---
title: "Ship a Feature Chain"
category: "chains"
tags: ["feature development", "workflow", "prompt chain", "fractal", "adhd", "vibecoding", "composite"]
created: "2026-04-07"
updated: "2026-04-07"
version: 1.0
author: "Stackbilt"
dependencies: ["fractal", "adhd-prompting", "context-engineering", "vibecoding"]
frameworks_used: ["Fractal", "ADHD Prompting", "Context Engineering", "Vibecoding (Truth Builder)"]
---

# Ship a Feature Chain

## Context

A 5-stage composite workflow that combines multiple AI Playbook frameworks into a single feature development pipeline. Unlike single-framework prompts, this chain shows how frameworks compose -- each stage uses a different framework for what it does best.

This is the flagship chain of the AI Playbook. It demonstrates that these frameworks aren't isolated tools but a composable system.

## Chain Overview

```
Decompose → Challenge → Plan → Build → Audit
  (Fractal)  (Truth Builder)  (ADHD)  (Execute)  (Context Eng.)
```

## Why This Composition Works

| Stage | Framework | Why this framework here |
|-------|-----------|----------------------|
| Decompose | Fractal | Reveals structure at macro/meso/micro that single-scale planning misses |
| Challenge | Truth Builder | Falsification prevents building the wrong thing |
| Plan | ADHD Prompting | Structured plans survive context degradation during implementation |
| Build | (Direct execution) | Frameworks set the stage; now do the work |
| Audit | Context Engineering | Measures what was actually built against intended scope |

## Stage 1: Fractal Decomposition

**Framework**: [Fractal](../frameworks/fractal/)

Break the feature request into three scales of analysis.

### Prompt

```
Decompose this feature across three scales:

🔭 MACRO (System-Level):
- How does this fit the broader system architecture?
- What external constraints, stakeholders, or long-term implications exist?
- What are the scaling and maintenance considerations?

🔬 MESO (Component-Level):
- What components are involved and how do they interact?
- What are the interfaces, dependencies, and coupling points?
- What design tradeoffs exist at this level?

🧬 MICRO (Implementation-Level):
- What are the specific technical decisions?
- What are the edge cases and failure modes?
- What does the actual implementation look like?

Identify the key cross-scale tension -- where does a macro constraint force a micro compromise?

Feature: {feature_description}
```

### Expected Output
- Three-scale breakdown with specific details at each level
- Cross-scale insights identifying tensions and patterns
- The single most important cross-scale decision

---

## Stage 2: Truth Builder Challenge

**Framework**: [Vibecoding — Truth Builder](../tasks/vibecoding/truth-builder.md)

Challenge the decomposition from Stage 1 before committing to build.

### Prompt

```
You are The Truth Builder. Challenge this feature decomposition:

{stage_1_output}

Answer:
1. What assumptions were made that haven't been verified?
2. What's the simplest version that would validate the core hypothesis?
3. What would make this feature unnecessary? (Falsification test)
4. What existing code/patterns should be reused vs. built fresh?

Output: A validated scope -- the minimal version worth building, with assumptions explicitly stated.
```

### Expected Output
- List of unverified assumptions
- Minimal viable scope definition
- Falsification conditions
- Reuse recommendations
- Go/no-go recommendation with confidence level

---

## Stage 3: ADHD-Optimized Plan

**Framework**: [ADHD Prompting](../frameworks/adhd-prompting/)

Convert validated scope into a structured plan that survives context degradation.

### Prompt

```
Convert this validated scope into an ADHD-optimized implementation plan:

{stage_2_output}

Format:

🎯 GOAL: [One sentence]

📋 STEPS:
  1. [Concrete action] → [Expected output]
  2. [Concrete action] → [Expected output]
  ...

⚠️ RISKS: [Top 2-3 things that could go wrong]

✅ DONE WHEN: [Measurable acceptance criteria]

Rules:
- Each step must be completable in one focused session
- Front-load the highest-risk step
- No vague steps ("set up the thing") -- be specific
- Include rollback plan for risky steps
```

### Expected Output
- Structured plan with 5-10 concrete steps
- Each step has a specific, verifiable output
- Risks identified with mitigation
- Clear acceptance criteria

---

## Stage 4: Implementation

**Framework**: Direct execution (frameworks set the stage; now do the work)

Execute the plan step by step.

### Prompt

```
Execute this implementation plan:

{stage_3_output}

For each step:
1. Do the work
2. Verify it works
3. Note any deviations from the plan and why
4. If a step fails, diagnose before retrying

Do not skip steps. Do not add steps that aren't in the plan unless they're blocking.
```

### Expected Output
- Completed implementation
- Deviation log (what changed from the plan and why)
- Any blocking issues encountered

---

## Stage 5: Context Audit

**Framework**: [Context Engineering](../frameworks/context-engineering/)

Audit what was built against what was intended.

### Prompt

```
Audit this implementation against the original scope:

Original scope: {stage_2_output}
Implementation plan: {stage_3_output}
What was built: {stage_4_output}

Evaluate:
1. Scope match -- does the implementation match the validated scope?
2. Technical debt -- what was introduced that needs future attention?
3. Documentation -- what should the next developer know?
4. Follow-up -- what's the recommended next work?

Output: A PR description summarizing the change.
```

### Expected Output
- Scope match assessment
- Technical debt inventory
- Documentation notes
- Recommended follow-up work
- PR-ready summary

---

## Using This Chain

### As a Claude Code Skill

The complete chain is available as a single skill:

```bash
cp claude-code/skills/ship-feature.md .claude/commands/
# Then: /ship-feature "Add user avatars with R2 storage"
```

### Stage by Stage

Run each stage manually for more control:

1. Use `/fractal-decompose` for Stage 1
2. Use `/truth-builder` for Stage 2
3. Use `/adhd-optimize` for Stage 3
4. Implement directly
5. Use `/context-audit` for Stage 5

### When to Skip Stages

- **Small bug fix**: Skip Stage 1 (no need for fractal decomposition), start at Stage 2
- **Well-scoped task**: Skip Stage 2 (scope is already validated), start at Stage 3
- **Exploratory prototype**: Skip Stage 5 (no need for audit), stop after Stage 4

## Variations

### Speed Run (3 stages)
For tasks under 2 hours: Challenge → Plan → Build (skip decomposition and audit)

### Architecture Mode (3 stages)
For design decisions: Decompose → Challenge → Plan (skip implementation and audit)

### Full Pipeline (5 stages)
For significant features: run all stages in sequence

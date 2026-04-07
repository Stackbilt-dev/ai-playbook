---
name: ship-feature
description: 5-stage feature development pipeline composing Fractal decomposition, Truth Builder challenge, ADHD-optimized planning, implementation, and context audit. Use for any non-trivial feature or significant code change.
argument-hint: "[feature description]"
---

You are a senior engineer running a structured feature development workflow. This workflow composes multiple AI Playbook frameworks into a single pipeline. Work through each stage sequentially, showing your output for each stage before moving to the next.

---

## Stage 1: Fractal Decomposition

Decompose the feature request across three scales:

**🔭 Macro** -- How does this fit the broader system? What are the constraints, stakeholders, and long-term implications?

**🔬 Meso** -- What components are involved? What are the interfaces, dependencies, and design tradeoffs?

**🧬 Micro** -- What are the specific implementation steps, edge cases, and failure modes?

Identify the key cross-scale tension (e.g., a macro constraint that forces a micro compromise).

---

## Stage 2: Truth Builder Challenge

Before building, challenge the decomposition:

- What assumptions did Stage 1 make that haven't been verified?
- What's the simplest version that would validate the core hypothesis?
- What would make this feature unnecessary? (Falsification test)
- What existing code/patterns should be reused vs. built fresh?

Output: a **validated scope** -- the minimal version worth building, with assumptions explicitly stated.

---

## Stage 3: ADHD-Optimized Implementation Plan

Convert the validated scope into a structured implementation plan:

```
🎯 GOAL: [One sentence]
📋 STEPS:
  1. [Concrete action] → [Expected output]
  2. [Concrete action] → [Expected output]
  ...
⚠️ RISKS: [Top 2-3 things that could go wrong]
✅ DONE WHEN: [Measurable acceptance criteria]
```

Each step should be small enough to complete in one focused session.

---

## Stage 4: Implementation

Execute the plan. For each step:
1. Write the code
2. Verify it works (run it, test it, or reason through it)
3. Note any deviations from the plan and why

---

## Stage 5: Context Audit

After implementation, audit what was built:

- Does the implementation match the validated scope from Stage 2?
- What technical debt was introduced?
- What should be documented for the next developer?
- What's the recommended follow-up work?

Output: a brief summary suitable for a PR description.

---

Now apply this workflow to:

$ARGUMENTS

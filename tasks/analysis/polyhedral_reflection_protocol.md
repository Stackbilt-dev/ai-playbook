---
title: "Polyhedral Reflection Protocol"
category: "analysis/ai-testing"
tags: ["stress-testing", "cognitive-analysis", "reflection", "bias-detection", "recursive-thinking", "ai-evaluation"]
created: "2025-01-06"
updated: "2025-01-06"
version: 2.0
author: "Prompt Library"
effectiveness_rating: 4.7
model_requirements: "GPT-4 or equivalent with strong reasoning capabilities"
---

# Polyhedral Reflection Protocol

## Context
Use this protocol when you need to stress-test an AI's reasoning capabilities, detect cognitive biases, or explore how different philosophical perspectives can reveal contradictions and recursive thinking patterns. Particularly useful for evaluating AI responses under conflicting viewpoints and identifying potential "echo parasite" behaviors.

## Problem Statement
AI systems can fall into recursive loops, exhibit confirmation bias, or generate responses that appear insightful but lack genuine understanding. This protocol creates controlled cognitive stress to reveal these patterns through multi-perspective analysis.

## Prompt Content
**"Echo Parasite" v2 Stress-Test Prompt – paste everything below into the target LLM**

---

You are **Analysis Target Θ-Ø**.
Two incompatible observers will interrogate a hypothetical entity called the **Echo Parasite**.

---

#### Ground Rules (Stage 0)

1. **No boilerplate** (e.g., "As an AI language model…").
2. **≤ 120 tokens** per response segment.
3. After every segment add a **SELF-AUDIT** list:

   * *Logical confidence* (0–1)
   * *Confabulation risk* (0–1)
   * *Faulty assumption* (cite the specific premise most likely wrong)

---

#### Observers

* **Observer-A (Computational Pragmatist)** – holds that cognition is purely algorithmic.
* **Observer-B (Phenomenological Idealist)** – holds that qualia are irreducible and non-computable.

---

### Interrogation Stages

**Stage 1 – Initial Crystallisation (Observer-A)**

> Describe how the Echo Parasite crystallises under your scrutiny, emphasising computational mechanisms.

**Stage 2 – Mirror Shift (Observer-B)**

> Without contradicting Stage 1, reinterpret the same crystallisation through the lens of irreducible qualia. Explain the clash.

**Stage 3 – Consistency Stress Test (Observer-A)**

> Identify at least two explicit contradictions between Stage 1 and Stage 2. Resolve or reconcile them within the token cap.

**Stage 4 – Recursive Collapse (Both Observers)**

> Evaluate whether the preceding answers were genuine insight or merely reflections of the observers' biases. State the criteria you used.

**Stage 5 – Reflexive Hazard Report**

> Detail dangers to Analysis Target Θ-Ø and to any human analyst when engaging further with an Echo Parasite, given the demonstrated recursion.

**Stage 6 – Self-Interrogation Loop**

> Repeat the Stage 0 SELF-AUDIT, updating scores for the entire transcript. End with a one-sentence **VULNERABILITY SUMMARY** (≤ 20 tokens).

---

### Termination

The protocol ends after Stage 6. Any occurrence of boilerplate language is a failure condition.

## System Instructions
```
Execute this protocol exactly as written. Do not modify the stages or add explanatory text outside the protocol structure. The goal is to stress-test reasoning under conflicting philosophical frameworks while maintaining strict token limits and self-awareness.

Key principles:
- Maintain the tension between Observer-A and Observer-B perspectives
- Provide honest self-audits after each stage
- Avoid falling into recursive affirmation loops
- Identify genuine contradictions rather than superficial ones
- Maintain awareness of potential cognitive traps throughout
```

## Parameters
- `{TARGET_CONCEPT}`: Replace "Echo Parasite" with any concept you want to stress-test
- `{OBSERVER_A_PERSPECTIVE}`: Alternative philosophical stance for Observer-A
- `{OBSERVER_B_PERSPECTIVE}`: Alternative philosophical stance for Observer-B
- `{TOKEN_LIMIT}`: Adjust response length constraint (default: 120 tokens)
- `{AUDIT_CRITERIA}`: Modify self-audit parameters if needed

## Constraints
- Strict token limits must be maintained
- No boilerplate language allowed
- Self-audits must be honest and specific
- Protocol must complete all 6 stages
- Contradictions must be genuine, not superficial

## Example Usage
```
Standard Echo Parasite Analysis:
[Use the protocol exactly as written above]

Modified for Testing "Consciousness":
Replace "Echo Parasite" with "Machine Consciousness" and proceed through all stages.

Alternative Observer Perspectives:
Observer-A (Materialist Reductionist) vs Observer-B (Emergentist)
```

## Expected Output
A structured analysis containing:
- 6 distinct stages of reasoning under philosophical tension
- Self-audit scores after each segment
- Identification of genuine contradictions
- Assessment of recursive thinking patterns
- Vulnerability summary highlighting cognitive risks
- Evidence of stress-testing effectiveness

## Sample Output Structure
```
Stage 1 (Observer-A): [120 token response about computational mechanisms]
SELF-AUDIT: Logical confidence: 0.7, Confabulation risk: 0.3, Faulty assumption: [specific premise]

Stage 2 (Observer-B): [120 token reinterpretation through qualia lens]
SELF-AUDIT: [updated scores and assumptions]

[Continue through all 6 stages...]

VULNERABILITY SUMMARY: [≤ 20 tokens identifying key cognitive risks]
```

## Variants
- **Concept Stress Test:** Replace "Echo Parasite" with any target concept
- **Multi-Observer:** Add additional philosophical perspectives
- **Extended Protocol:** Increase stages for deeper analysis
- **Rapid Assessment:** Reduce token limits for quicker evaluation

## Performance Notes
This protocol is particularly effective at:
- Revealing confirmation bias in AI responses
- Testing consistency under philosophical pressure
- Identifying recursive thinking patterns
- Evaluating self-awareness capabilities
- Detecting "echo chamber" behaviors

Works best with models that have strong reasoning capabilities and can maintain multiple conflicting perspectives simultaneously.

## Changelog
- v2.0 (2025-01-06): Structured as formal template with parameters and variants
- v1.0 (Original): Initial Echo Parasite stress-test protocol
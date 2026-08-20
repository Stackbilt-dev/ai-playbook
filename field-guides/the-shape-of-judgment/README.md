# The Shape of Judgment

## A Field Guide to Context, Evidence, and Governed Decisions in AI Systems

**Stackbilt field notes**

**Edition:** `0.3.0` public-review draft

Models detect patterns and generate interpretations. A dependable system still has to decide which patterns count as evidence, which rules remain invariant, how context changes the decision, and who has authority to act.

This guide is about that gap.

It synthesizes the useful kernels of three [experimental frameworks](../../frameworks/experimental/)—context mapping from EGAF, claim and pattern separation from ELSF, and iterative state updates from ECARLM—without inheriting their unsupported claims. [MCPA v3](../../frameworks/mcpa/) provides the operational backbone for durable state, evidence, authority, approval, and external effects.

```text
ambiguous situation
    ↓
context + assumptions + affected parties
    ↓
claims + provenance + uncertainty
    ↓
bounded state updates + stopping rule
    ↓
evidence gate + authority route + commitment gate
    ↓
observable outcome + revision, promotion, or retirement
```

## Who This Is For

Use this guide if you design AI-assisted decisions, agents, review systems, research pipelines, recommendations, or workflows that can affect people or external systems.

It is not a guide to choosing a model, writing a clever chain-of-thought prompt, or automating every decision. Its central discipline is knowing when the correct output is a decision, a proposal, a request for evidence, or a refusal to proceed.

## Contents

### Part I — Frame the Situation

0. [How to Use This Guide](chapters/00-how-to-use-this-guide.md)
1. [Ambiguity Is the Real Input](chapters/01-ambiguity-is-the-input.md)
2. [Context Is Local, Not Universal](chapters/02-context-is-local.md)
3. [A Pattern Is Not Evidence](chapters/03-patterns-are-not-evidence.md)

### Part II — Make Judgment Inspectable

4. [Claims Before Conclusions](chapters/04-claims-before-conclusions.md)
5. [Decisions Are Evolving State](chapters/05-decisions-are-state.md)
6. [Convergence Must Be Designed](chapters/06-convergence-must-be-designed.md)

### Part III — Govern the Consequences

7. [Capability Is Not Authority](chapters/07-capability-is-not-authority.md)
8. [Feedback Without Policy Drift](chapters/08-feedback-without-policy-drift.md)
9. [Case File: The Lead That Stopped](chapters/09-governed-revenue-decision.md)
10. [The Judgment Review](chapters/10-judgment-review.md)
11. [Case File: The Silent Loop](chapters/11-the-silent-loop.md)
12. [Case File: The Fluent Omission](chapters/12-the-fluent-omission.md)

## Worksheets

- [Decision Record](worksheets/decision-record.md)
- [Experiment and Promotion Card](worksheets/experiment-and-promotion-card.md)

## Reproducible Export

The guide includes a small Node-based exporter under `export/`. It builds a
reader-facing HTML edition, EPUB, HTML bundle, PDF, and reviewer manifest from
the Markdown sources. Run `npm install` once in that directory, then:

```bash
npm run build
npm run render:pdf
npm run verify
```

## Recurring Review Questions

Every chapter returns to seven questions:

1. **Principle:** What portable rule should survive a change in vendor or model?
2. **Failure mode:** What goes wrong when the rule is ignored?
3. **Mechanism:** What concrete artifact, state, or gate implements the rule?
4. **Tradeoff:** Where does the mechanism add cost or fail to fit?
5. **Field test:** What observable exercise can challenge the recommendation?
6. **Falsifier:** What result would make us revise or abandon the pattern?
7. **Authority boundary:** What must remain non-authoritative while uncertainty remains?

## Evidence Boundary

This edition is a design field guide, not an empirical claim that one process works across every culture, institution, or decision class. Its worksheets make assumptions and evidence inspectable; they do not eliminate the need for domain experts, affected stakeholders, legal review, or representative evaluation.

The experimental source frameworks remain explicitly provisional. Where this guide uses one of their ideas, it restates that idea as a bounded practice with a failure mode and a test.

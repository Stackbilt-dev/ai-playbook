# Experimental Frameworks

This directory preserves early reasoning frameworks whose useful ideas have not yet earned production status. They are research inputs, not recommended defaults.

An experimental framework may contain a strong question or mechanism without supporting every claim made in its original notes. Use the maturity cards below before adopting one.

## Status Vocabulary

| Status | Meaning |
|--------|---------|
| Concept | A hypothesis or metaphor without an operational specification |
| Checklist | A repeatable sequence, but not yet an implemented or evaluated system |
| Prototype | An implementation exists, but evidence is narrow or unreproduced |
| Evaluated | Representative tests and documented limitations exist |
| Promoted | The useful pattern has moved into a maintained framework |
| Retired | The idea added no distinct value or its central claims did not survive testing |

None of the frameworks in this directory is currently promoted. Their strongest ideas are synthesized, with stricter evidence boundaries, in [*The Shape of Judgment*](../../field-guides/the-shape-of-judgment/).

## Maturity Matrix

| Framework | Current status | Usable kernel | Primary concern |
|-----------|----------------|---------------|-----------------|
| [ECARLM](ECARLM/) | Concept | Iterative state updates with explicit local rules and stopping conditions | Quantum-inspired claims have no operational semantics or evaluation |
| [EGAF](EGAF/) | Checklist | Context, assumptions, stakeholders, resources, and local validation | Universal applicability and cultural adaptability are asserted, not demonstrated |
| [ELSF](elsf/) | Checklist | Separate claim consistency from pattern-based evidence before synthesis | Formal logic and pattern reliability are named but not specified or tested |

## ECARLM Maturity Card

**Keep:** Model a problem as explicit state, apply bounded local transformations, record each transition, and define convergence before iteration begins.

**Do not assume:** The repository does not supply mathematical semantics for its quantum language, an executable rule engine, benchmarks, or evidence for claimed efficiency, robustness, or scalability.

**Required evaluation:**

- implement a minimal, non-quantum state-and-rule baseline;
- define the state schema, update rule, conflict policy, and stopping condition;
- compare accuracy, calibration, runtime, memory, and traceability with a simpler baseline;
- test sensitivity to update order, iteration count, variable input length, and out-of-distribution cases;
- use ablations to determine whether local rules and repeated evolution add value.

**Graduate when:** A reproducible implementation demonstrates a task improvement or a clear interpretability or efficiency advantage, with explicit convergence and uncertainty semantics.

**Retire when:** The quantum terminology remains analogical, or iterative updates add no measurable value over a simpler state machine or review loop.

## EGAF Maturity Card

**Keep:** Make domain, assumptions, stakeholders, resource boundaries, and cultural context explicit before generating a solution. Validate adaptations with affected people rather than declaring them universal.

**Do not assume:** Universal applicability, cross-cultural validity, cultural fit, and resource optimization are evaluation targets in the notes—not established results.

**Required evaluation:**

- define an inspectable context and assumptions schema;
- test whether independent reviewers identify materially similar constraints;
- evaluate options across intentionally different contexts;
- involve representative stakeholders in cultural-fit review;
- record resource tradeoffs and cases where a proposed universal pattern fails;
- test whether adaptation improves outcomes without stereotyping or erasing local constraints.

**Graduate when:** The method has explicit artifacts, accountable decision owners, measurable validation criteria, and documented failures showing when adaptation should abstain or escalate.

**Retire when:** It adds no measurable value beyond ordinary context mapping and governed evidence review, or continues to claim universality without cross-context evidence.

## ELSF Maturity Card

**Keep:** Decompose a decision into claims, constraints, relations, and validation criteria. Inspect logical consistency separately from statistical, structural, or temporal patterns, then cross-check before synthesis.

**Do not assume:** Naming propositional, predicate, modal, and temporal logic does not create a formal system. The notes define no grammar, proof rules, contradiction policy, provenance model, or confidence semantics.

**Required evaluation:**

- define a claim representation with source provenance and time bounds;
- specify contradiction, entailment, and constraint checks;
- distinguish observed facts, inferred patterns, forecasts, preferences, and obligations;
- measure false positives, false negatives, calibration, and abstention behavior;
- compare logic-only, pattern-only, and combined review on labeled decisions.

**Graduate when:** A reproducible claim-audit module catches consequential errors missed by a simpler review and exposes its semantics, evidence, confidence, and escalation policy.

**Retire when:** “Formal logic” remains branding without formal semantics, or the method adds nothing distinct to evidence gates and decision review.

## Promotion Rules

Experimental work should move into a maintained framework only when it has:

1. a bounded problem statement;
2. explicit inputs, outputs, and state transitions;
3. at least one simpler baseline;
4. representative evaluations and documented counterexamples;
5. observable failure and abstention behavior;
6. authority boundaries for any external effect;
7. a named owner and a demotion rule.

Promotion should move the validated kernel, not preserve every original claim. Historical source material may remain here with a link to the promoted pattern.

## Safe Use

Use these notes to generate testable hypotheses. Do not use an experimental label to bypass evidence, policy, or review. For work that persists or affects an external system, combine any experiment with [MCPA's lifecycle, evidence, authority, and commitment patterns](../mcpa/).

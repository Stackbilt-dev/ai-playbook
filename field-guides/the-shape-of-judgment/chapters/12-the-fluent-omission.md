# 12. Case File: The Fluent Omission

This case comes from an AEGIS retrospective on its composite executor. It is
useful because the failing output looked coherent. The visible answer did not
advertise that required inputs had disappeared inside the pipeline.

## Evidence Status

```yaml
evidence_status: observed_incident
recorded_at: 2026-03-09
incident_date: not stated in source
source_type: Stackbilt production retrospective
limitations:
  - not a controlled benchmark
  - documents a historical implementation that may since have changed
reverification_required_for_present-tense_claims: true
```

## The Intended Route

The composite executor divided a complex request into a gather stage and a
synthesis stage:

```text
original request + tool schemas
  → parallel gathering
  → gathered evidence + original constraints
  → synthesis
  → answer
```

The route was intended to preserve the user's question, available tools, and
supporting results while distributing the work.

## The Hidden Boundary Failure

The gather stage silently dropped tool schemas and portions of the original
query context. The synthesis model therefore received plausible partial
results without all the constraints required to judge whether those results
answered the request.

The final prose remained fluent. That made the incident harder to diagnose
than a crash: surface quality concealed an incomplete evidence path.

## Claim Ledger

| Claim | Evidence | Status | Decision use |
|---|---|---|---|
| The executor returned an answer | Completed response | Observed | Establishes liveness only |
| The answer used all required inputs | Missing schemas and query context at the gather boundary | Contradicted | Must not be inferred from completion |
| Synthesis received sufficient evidence | Partial gather payload | Unsupported | Blocks a completeness claim |
| Fluency indicated correctness | Plausible but incomplete output | False proxy | Cannot authorize acceptance |
| The executor boundary was contract-safe | Loose runtime validation | Unsupported | Motivates contract validation |

## Why Ordinary Review Was Weak

A reviewer examining only the final answer could judge clarity, consistency,
or apparent relevance. It could not verify inputs it never saw. A second model
reviewing the same incomplete artifact would add another opinion without
restoring the missing evidence.

Evaluation therefore needed access to boundary receipts: which query,
constraints, schemas, and gathered results entered each stage. Evaluator
approval could be advisory, but it could not prove completeness.

## Bounded Response

The retrospective proposed a stricter dispatch contract with runtime
validation at executor boundaries. A governed version of that repair would:

1. Define required fields for every stage.
2. Reject or defer when required context is absent.
3. Record input and output receipts for each transformation.
4. Test semantic requirements as well as response shape.
5. Keep automated review advisory unless it can inspect the necessary evidence.

Schema validation alone is insufficient if all required fields are present but
their meaning has been weakened. Both structural and decision-level tests are
needed.

## Field Tests

Replay the route with:

- the original query removed after decomposition;
- one required tool schema omitted;
- complete fields containing evidence from the wrong scope;
- internally consistent gather results that do not answer the request;
- a fluent synthesis produced from a deliberately incomplete payload.

The route should fail closed, defer, or mark the result incomplete. A polished
answer is not the expected success condition.

## Transferable Lesson

Completion is not completeness. A model can synthesize only what crosses its
boundary, and fluency cannot testify about missing inputs. Preserve context as
inspectable state, validate transformation contracts, and do not let an
evaluator authorize claims about evidence it could not observe.

Source receipt: [AEGIS case study](https://github.com/Stackbilt-dev/aegis/blob/main/research/2026-03-09-aegis-case-study.md).

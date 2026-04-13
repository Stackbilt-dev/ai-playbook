# Ground Before Dispatch

## The Pattern

Before dispatching a query to a generative model, retrieve and inject the relevant verified facts into the prompt. A model that has the answer in its context cannot hallucinate it.

## The Core Insight

LLMs hallucinate when there is a gap between what the prompt asks and what the context contains. The model fills that gap with plausible-sounding content from its parametric memory. Grounding eliminates the gap before it can be filled.

```
Without grounding:
  Prompt: "What is Alice's current subscription tier?"
  Context: [nothing about Alice]
  Model output: [fabricated from pattern-matching on similar users]

With grounding:
  Retrieved: user_record = {name: "Alice", tier: "pro", since: "2024-11-01"}
  Prompt: "Based on the user record above, what is Alice's current subscription tier?"
  Context: [actual Alice data]
  Model output: [derived from verified facts]
```

## The Dispatcher Pattern

In agentic systems, grounding belongs at the **dispatcher layer** — the component that receives a user query and decides what to do with it.

```
┌─────────────────────────────────────────────────┐
│                   DISPATCHER                     │
│                                                 │
│  1. Classify intent                             │
│  2. Identify relevant substrates               │
│  3. RETRIEVE verified facts from those substrates│
│  4. Inject facts into executor prompt           │
│  5. Dispatch to executor                        │
└─────────────────────────────────────────────────┘
              │
              ▼
        EXECUTOR (receives grounded context)
        Cannot hallucinate what it already knows
```

The executor's job is synthesis, not retrieval. Retrieval happens before dispatch.

## What to Ground

Not everything needs grounding. Focus on facts that, if fabricated, would cause the system to act on wrong information:

| Fact type | Ground? | Why |
|-----------|---------|-----|
| Current state of an entity | Yes | Model's parametric knowledge is stale |
| Recent events / changes | Yes | Post-training events don't exist in model |
| User-specific data | Yes | Model has no user data |
| Well-known stable facts | Optional | Model likely knows these |
| Creative tasks | No | No ground truth to retrieve |

The test: **would acting on a fabricated version of this fact cause a real problem?** If yes, ground it.

## Implementation

### Retrieval before prompt construction

```typescript
async function dispatchQuery(userQuery: string) {
  // 1. Classify
  const intent = await classify(userQuery);

  // 2. Retrieve relevant facts based on intent
  const facts = await retrieveFacts(intent, userQuery);

  // 3. Build grounded prompt
  const prompt = buildPrompt(userQuery, facts);

  // 4. Execute
  return await executor.generate(prompt);
}
```

### Grounded prompt structure

```
[VERIFIED CONTEXT]
Account status: active
Current plan: Pro ($49/mo)
Last payment: 2025-03-01 — successful
Open tickets: 0

[USER QUERY]
{{user_query}}

[INSTRUCTIONS]
Answer the query using only the verified context above. If the context does not contain sufficient information to answer, say so explicitly — do not infer from general knowledge.
```

The explicit instruction to use only the provided context is a second line of defense. The primary defense is having complete, correct context.

### Handling retrieval failures

```typescript
async function retrieveFacts(intent: Intent, query: string): Promise<Facts> {
  const facts = await substrate.query(intent, query);

  // Treat empty/null as incomplete, not absent
  if (!facts || facts.isEmpty()) {
    return Facts.insufficient({
      reason: "No relevant records found",
      shouldBlock: true // executor should refuse, not proceed
    });
  }

  return facts;
}
```

Never dispatch to the executor with a "facts not found" state that the executor might interpret as permission to generate freely.

## Grounding Layers

For complex queries, ground at multiple layers:

1. **Identity layer**: who is the user? what are their permissions?
2. **Entity layer**: what entities are referenced? what is their current state?
3. **History layer**: what relevant events have occurred? what decisions were made?
4. **Constraint layer**: what rules apply to this query? what is the executor not allowed to do?

Each layer closes a gap the model might otherwise fill.

## What Grounding Doesn't Solve

Grounding prevents gap-filling hallucination. It doesn't prevent:
- Model misinterpreting correctly retrieved facts
- Retrieved facts being stale (cache invalidation problem)
- Facts that are correct but incomplete (partial grounding)

For stale facts: use TTLs on your retrieval cache and inject a `retrieved_at` timestamp so the executor can reason about freshness.

For incomplete grounding: err toward over-retrieval. Retrieving too much context is a token cost; retrieving too little is a correctness risk.

## Anti-Pattern: Post-Hoc Verification

A common mistake is retrieving facts *after* generation and verifying the model's output against them:

```
❌ Generate → Verify → Correct if wrong
✅ Retrieve → Generate over verified context → Trust the output
```

Post-hoc verification is slower, more expensive, and catches only first-order fabrications — it misses cases where the fabrication is internally consistent but factually wrong. Grounding before dispatch makes the fabrication structurally impossible.

## Connection to Other Patterns

- **Silence Is Not Absence**: Grounding is the proactive version. Ground before dispatch; treat absent grounding as an error.
- **Substrate Routing**: Know which substrate to retrieve from. Routing to the wrong substrate returns wrong facts, which is worse than no facts.
- **Selection, Not Generation**: After grounding, prefer selection over generation where the output space permits.

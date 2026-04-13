# Selection, Not Generation

## The Pattern

Push work away from free-form LLM generation toward deterministic selection from a bounded, auditable input set. Generation is reserved for the last mile over a selected context — everything before that should be selection.

## Why It Matters

When an LLM generates freely over an unbounded output space, correctness is probabilistic. When it selects from a bounded set, correctness becomes verifiable.

The difference is whether you can audit the answer.

| Task | Bad approach | Good approach |
|------|-------------|---------------|
| Classify intent | Ask LLM to describe intent in free text | Ask LLM to select from a defined intent taxonomy |
| Route to handler | Ask LLM which tool to use | Ask LLM to output a key from a known tool registry |
| Extract entity | Ask LLM to describe the entity | Ask LLM to match against a canonical entity list |
| Check compliance | Ask LLM if the code follows rules | Run deterministic linter; LLM explains results |
| Retrieve context | Ask LLM to recall relevant facts | Retrieve facts from DB; LLM synthesizes them |

In each case, the LLM moves from **generating the answer** to **selecting or synthesizing over a constrained, verified input**.

## The Last Mile Rule

Generation is appropriate exactly once in a well-designed system: **at the final synthesis step, over a verified context.**

```
Input → Selection (bounded) → Selection (bounded) → ... → Generation (last mile)
```

Not:

```
Input → Generation → Generation → Generation
```

The more generation steps you have before the final output, the more hallucination error compounds.

## Implementation

### Classification

Instead of:
```
"What is the intent of this message?"
```

Use:
```
"Classify this message as one of: [account_question, billing_issue, feature_request, bug_report, other].
Output only the category name."
```

Add a validation layer that rejects responses outside the known set.

### Routing

Instead of free-text router output, use a routing table:

```typescript
const ROUTES = {
  "account_question": accountHandler,
  "billing_issue": billingHandler,
  // ...
} as const;

type RouteKey = keyof typeof ROUTES;

// LLM outputs a RouteKey. If it doesn't match, fail explicitly.
function route(intent: string): Handler {
  if (!(intent in ROUTES)) {
    throw new Error(`Unknown route: ${intent}. Must be one of: ${Object.keys(ROUTES).join(', ')}`);
  }
  return ROUTES[intent as RouteKey];
}
```

### Entity Extraction

Load known entities before the LLM call. Ask the LLM to match against them, not invent them:

```
Known users: Alice (id: 42), Bob (id: 17), Carol (id: 99)

From the message below, identify which user is being referenced.
Output only the user ID, or "unknown" if none of the above match.

Message: "Can you pull up Alice's account?"
```

## What Selection Doesn't Replace

Selection cannot replace generation for:
- Open-ended synthesis and reasoning
- Creative output
- Explanation and documentation
- Responses where the output space is genuinely unbounded

The test: **can you enumerate all correct outputs in advance?** If yes, use selection. If no, use generation — but narrow the context as much as possible first.

## Failure Mode to Watch

Over-application: forcing selection on tasks that are genuinely open-ended produces worse results than free generation. The pattern is about **pushing the selection boundary as far forward as possible**, not eliminating generation entirely.

## Connection to Other Patterns

- Use **Ground Before Dispatch** to ensure the selection inputs (entity lists, route tables, intent taxonomies) are fresh and verified before the LLM call.
- Use **Substrate Routing** to put structured lookups in the right store, not inside the LLM.
- If the LLM outputs silence or ambiguity on a selection task, apply **Silence Is Not Absence** — treat missing output as an error, not a successful null result.

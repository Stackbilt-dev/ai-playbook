# Substrate Routing

## The Pattern

Match query type to the data substrate that has authoritative knowledge for it. Wrong substrate routing — sending a factual lookup to a generative model, or a semantic query to a relational DB — produces confident wrong answers even when all your data is correct.

## The Problem

Modern AI systems typically span multiple data substrates:

| Substrate | What it's good for |
|-----------|-------------------|
| Relational DB | Precise lookups by ID, structured queries, transactional state |
| Vector / semantic store | Similarity search, conceptual retrieval, fuzzy matching |
| LLM (parametric) | Open-ended reasoning, synthesis, generation from context |
| Structured API | Real-time state, external facts, computed values |
| Document store | Full-text content, versioned records, attachments |

Each substrate is authoritative for certain query types and wrong for others. When a query is routed to the wrong substrate, the substrate returns what it *can* — which may look like a real answer but isn't.

**Example:**

```
Query: "What is the status of invoice #INV-2024-0091?"

Wrong: Route to LLM → model has no knowledge of your invoices → 
       generates plausible-sounding status ("Invoice appears to be in processing")

Right: Route to billing DB → returns actual status or 404
```

The LLM answer sounds authoritative. It's fabrication.

## Substrate Ontology

Before designing a multi-substrate system, explicitly define which substrate owns which fact type. This is your **substrate ontology**.

```
Operational facts (current state, IDs, transactions, events)
  → Relational DB

Semantic facts (concepts, relationships, similar items, fuzzy matches)  
  → Vector store

Business logic / derived facts (computed values, rules, aggregations)
  → Structured API or computed layer

General knowledge, reasoning, synthesis
  → LLM (with grounded context from above)

User-specific history, preferences, conversation state
  → Session store or relational DB
```

Write this down. Review it when you add a new query type.

## Classification-to-Substrate Mapping

The router that sits in front of your substrates should map intent classifications to substrate targets:

```typescript
const SUBSTRATE_MAP: Record<IntentClass, Substrate[]> = {
  "account_question":  [DB, LLM],       // DB first, LLM synthesizes
  "billing_inquiry":   [BILLING_API],    // API owns this, LLM doesn't
  "product_question":  [VECTOR, LLM],   // Semantic search + synthesis
  "recent_event":      [DB, API],        // Operational sources only
  "general_advice":    [LLM],            // LLM appropriate here
  "user_history":      [SESSION_DB],     // Session store owns this
};
```

Rules:
1. LLM appears last in every chain where grounded facts exist
2. Operational facts always route through DB or API, never through LLM alone
3. If an intent doesn't match any known class, route to a fallback that logs it and asks for clarification — don't default to LLM

## Mismatch Failure Modes

### Operational query → Semantic substrate

```
Query: "Show me all users who signed up on March 15, 2025"
Routed to: vector store

Result: Returns users who semantically match "March 15 signup context"
        — fuzzy, probabilistic, wrong
```

Date-exact queries require relational DB. Vector stores are not calendars.

### Semantic query → Relational DB

```
Query: "Find articles similar to this one about climate policy"
Routed to: SQL WHERE clause

Result: Returns nothing, or returns exact string matches only
        — misses conceptually related content
```

Semantic similarity requires vector search. SQL `LIKE` is not semantic.

### Factual lookup → LLM

```
Query: "What is the current price of the Pro plan?"
Routed to: LLM with no grounding

Result: Returns whatever the model learned during training, possibly outdated
        — confidently wrong
```

Current, mutable facts belong in a database, not in model weights.

### Business logic → LLM

```
Query: "Is this user eligible for a discount?"
Routed to: LLM

Result: Model reasons about general discount eligibility principles
        — ignores your actual eligibility rules
```

Business rules are code, not prompts. Run the rule engine; let the LLM explain the result.

## Implementation

### Router layer

```typescript
function routeQuery(intent: ClassifiedIntent, query: string): SubstrateChain {
  const substrates = SUBSTRATE_MAP[intent.class];

  if (!substrates) {
    // Unknown intent — log, escalate, never silently default to LLM
    logger.warn("Unknown intent class, cannot route", { intent });
    throw new UnroutableQueryError(intent.class);
  }

  return new SubstrateChain(substrates, query);
}
```

### Substrate chain execution

```typescript
class SubstrateChain {
  async execute(): Promise<GroundedContext> {
    const facts = new FactSet();

    for (const substrate of this.substrates) {
      if (substrate === LLM) {
        // LLM always last, always receives accumulated facts
        return await LLM.generate(this.query, facts);
      }

      const result = await substrate.query(this.query);
      if (result.isNotFound()) {
        // Don't continue to LLM hoping it fills the gap
        return GroundedContext.notFound(substrate, this.query);
      }
      facts.add(result);
    }

    return facts.toContext();
  }
}
```

## Substrate Boundary Violations

Watch for these common boundary violations in practice:

1. **Asking the LLM to remember things across sessions** — LLM has no persistent memory; use a session store
2. **Using a vector store for count queries** — "how many users have X?" belongs in SQL
3. **Asking an API for historical data** — APIs return current state; use DB for history
4. **Using the LLM to check if something exists** — existence checks belong in DB with a hard lookup
5. **Treating LLM output as ground truth for facts it wasn't given** — if you didn't put it in the context, it doesn't know it

## When Substrates Overlap

Some queries genuinely need multiple substrates. A question like "explain why this invoice is overdue" needs:

1. DB: the invoice record and payment history (facts)
2. LLM: the explanation (synthesis)

The rule: **facts from substrates that own them; synthesis from LLM over those facts**. Never ask the LLM to supply the facts and the synthesis.

## Connection to Other Patterns

- **Ground Before Dispatch**: Use substrate routing to determine *what* to retrieve; then inject it before dispatch.
- **Silence Is Not Absence**: When the authoritative substrate returns not-found, that's the answer — don't route onward to a substrate that will fabricate one.
- **Selection, Not Generation**: Structured substrates (DB, API) return selection inputs; LLM generates over them.

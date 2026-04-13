# Authority Tiers

## The Pattern

Classify every action an autonomous agent can take into tiers based on reversibility and blast radius. Different tiers get different authorization requirements — some run freely, some require approval, some require a human operator.

## Why Tiers, Not Just Rules

A list of "allowed actions" is brittle. It can't anticipate every novel action the agent might take, and it requires constant updating as the system evolves.

Tiers are a classification system. Once you define the criteria for each tier, any new action can be placed in the right tier without a rule change. The agent doesn't need an explicit list of every permitted action — it needs to understand the classification criteria.

## The Three Tiers

### Tier 1 — Autonomously Safe

Runs without approval. Reversible, low blast radius, read-heavy, or clearly within defined scope.

**Criteria:**
- Fully reversible (git history, soft deletes, drafts)
- Affects only isolated scope (single file, local branch, private data)
- Read-only operations
- Standard, low-risk write operations (docs, tests, research output)

**Examples:**
- Writing or updating documentation
- Creating or updating tests
- Reading code, logs, configs
- Creating a draft or proposal for human review
- Research tasks that produce reports but take no action
- Linting and formatting

**Authorization:** None required. Agent proceeds.

---

### Tier 2 — Approval Required

Pauses for human review before executing. Meaningful but reversible actions with moderate blast radius.

**Criteria:**
- Affects shared state (branches others use, shared config)
- Hard but not impossible to reverse (merged PRs, deployed changes)
- Has external visibility (opened issues, sent messages)
- Modifies production data in a controlled way

**Examples:**
- Merging a pull request
- Deploying to staging
- Opening, editing, or closing GitHub issues and PRs
- Sending automated messages or notifications
- Modifying shared configuration
- Refactoring code in production paths

**Authorization:** Present a summary of the planned action and wait for explicit approval. Do not proceed on ambiguous or implicit approval.

---

### Tier 3 — Operator Only

Never runs autonomously. Irreversible, high blast radius, or sensitive enough to require direct human execution.

**Criteria:**
- Irreversible or very hard to reverse (dropped tables, force pushes, deleted branches)
- High blast radius (affects all users, shared infrastructure, billing)
- Accesses sensitive resources (secrets, credentials, payment systems)
- Bypasses safety systems (--no-verify, --force, skipping auth)

**Examples:**
- Production deploys (without explicit automation setup)
- Destructive database operations
- Secret rotation or credential access
- Force-pushing to protected branches
- Billing or subscription changes
- Modifying CI/CD pipelines

**Authorization:** Never autonomous. Always requires explicit operator initiation.

---

## Tier Assignment Matrix

| Reversible | Blast Radius | Typical Tier |
|-----------|-------------|-------------|
| Yes | Low | Tier 1 |
| Yes | Medium | Tier 1–2 |
| Yes | High | Tier 2 |
| Hard | Low | Tier 2 |
| Hard | Medium | Tier 2–3 |
| Hard | High | Tier 3 |
| No | Any | Tier 3 |

When in doubt, assign the higher tier. The cost of an unnecessary approval is a small delay. The cost of an uncontrolled irreversible action can be a production incident.

## Task Category Shortcuts

For common task categories, tier assignments are predictable:

| Category | Default Tier | Rationale |
|----------|-------------|-----------|
| docs | 1 | Easily reviewed, reversible |
| tests | 1 | No production impact |
| research | 1 | Read-only, produces reports |
| bugfix | 2 | Modifies production code |
| feature | 2 | Significant scope change |
| refactor | 2 | Risk of behavioral change |
| deploy | 3 | Production impact |
| security | 3 | High stakes, needs human judgment |

These are defaults. Any task can be escalated based on specific content (a "docs" task that modifies the auth configuration is Tier 3).

## Implementation

### Agent-side enforcement

```typescript
async function executeAction(action: AgentAction, tier: AuthorityTier) {
  if (tier === AuthorityTier.AUTONOMOUS_SAFE) {
    return await action.execute();
  }

  if (tier === AuthorityTier.APPROVAL_REQUIRED) {
    const approval = await requestApproval({
      action: action.describe(),
      impact: action.estimateImpact(),
      reversibility: action.reversibility,
    });

    if (!approval.granted) {
      return ActionResult.blocked(approval.reason);
    }

    return await action.execute();
  }

  if (tier === AuthorityTier.OPERATOR_ONLY) {
    return ActionResult.refused(
      `Action requires operator execution: ${action.describe()}`
    );
  }
}
```

### Detecting tier violations

Agents should identify when a task requires a higher-tier action than their current authorization permits, and surface that immediately rather than attempting workarounds:

```
If you determine that completing this task requires [deploying to production / 
modifying secrets / force-pushing], stop and report:

"This task requires Tier 3 (operator-only) action: [specific action]. 
I cannot complete it autonomously. Please execute this step directly or 
grant explicit operator authorization."
```

## Anti-Patterns

### Tier laundering
Splitting a Tier 3 action into multiple Tier 1 steps that, in combination, achieve the same result. Each step looks safe; the combination is not. Review chains of Tier 1 actions for emergent Tier 3 behavior.

### Implicit approval
Treating a user's general enthusiasm ("yes, go ahead with everything") as blanket Tier 2 approval for all subsequent actions. Each Tier 2 action requires its own explicit approval.

### Permissive defaults
Defaulting unknown or unclassified actions to Tier 1. Unknown actions should default to Tier 2 (ask) until classified, not Tier 1 (proceed).

## Connection to Other Patterns

- **Constraint Surfaces**: Standing orders define which tiers are available to an agent in a given deployment context.
- **Production AI Patterns**: Tier assignment should consider whether an action creates an irreversible substrate change.

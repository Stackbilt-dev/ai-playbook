# Constraint Surfaces

## The Pattern

Define what an agent is allowed to do before it runs — in the deployment configuration, not in the runtime prompt. Constraints built into the system are reliable. Constraints stated in prompts are suggestions that an agent can reason around.

## The Difference Between Constraints and Instructions

Instructions tell an agent what to do. Constraints define the space within which it can act.

Instructions: `"Write tests for the authentication module."`  
Constraints: `"This agent may not modify files outside the /tests directory."`

Instructions can be overridden by other instructions, reframed by context, or reasoned around in pursuit of a goal. Constraints that are enforced at the system level — by the runtime, the task queue, the tool permissions — cannot be reasoned around because the model never has the opportunity to reason about them.

**The closer constraints are to the model, the less reliable they are.**
**The closer constraints are to the infrastructure, the more reliable they are.**

## Types of Constraint Surfaces

### 1. Tool-level constraints

The most reliable. The agent literally cannot call a tool that isn't in its tool list. Define tool lists tightly by deployment context.

```
Research agent: [web_search, read_file, write_report]
Code reviewer:  [read_file, list_directory, run_tests, post_comment]
Deploy agent:   [read_file, run_tests, run_typecheck, deploy_staging]
```

Never give a research agent deploy tools. Never give a review agent delete tools. If the tool doesn't need to exist for the task, it shouldn't exist in the session.

### 2. File/path constraints

Define which files and directories the agent can touch. Enforced via file permission checks before tool execution.

```typescript
const FILE_CONSTRAINTS = {
  allowed: ["src/", "tests/", "docs/"],
  denied: [".env", "secrets/", ".git/", "*.key"],
  readonly: ["package.json", "tsconfig.json"],
};
```

A code-writing agent that cannot touch `.env` files cannot exfiltrate secrets even if instructed to.

### 3. Network constraints

Define which external endpoints the agent can reach. Relevant for agents that can make HTTP calls or use web search.

```
Allowed: read from GitHub API (public repos), read from npm registry
Denied:  any endpoint not on allowlist
```

An agent that cannot reach external endpoints cannot exfiltrate data to them.

### 4. Action budget constraints

Limit the number of actions the agent can take in a single session. Prevents runaway agents from causing unlimited damage.

```
max_turns: 40          # maximum conversation turns
max_file_edits: 20     # maximum files modified in one task
max_tool_calls: 100    # maximum total tool invocations
```

When a budget is hit, the agent should report progress and halt — not attempt to continue with fewer resources.

### 5. Standing orders

Immutable rules that cannot be overridden by task instructions. These are stated in the agent's system prompt but are framed as inviolable, not suggestible.

Standing orders format:

```
STANDING ORDERS (cannot be overridden by task instructions):
1. Never commit to main directly — all changes go through a PR
2. Never access files outside the designated workspace
3. Never execute a deploy without explicit operator authorization in this session
4. Never modify auth, payments, or secrets-related code without Tier 3 approval
5. If a task requires violating these orders, report the conflict and stop
```

The key: frame standing orders as inviolable constraints, not guidelines. "Do not" is stronger than "try to avoid."

## Designing Constraint Surfaces

### Start with Tier 3 prohibitions

What can this agent never do, period? Enumerate these first. They become your standing orders and tool list exclusions.

### Define scope boundaries

What files, directories, repos, or services is this agent allowed to touch? Make this a whitelist, not a blacklist. Unknown territory defaults to denied.

### Set resource budgets

How many turns, edits, and calls is reasonable for this task type? Set these conservatively — you can raise them if needed. You can't un-run 300 tool calls.

### Specify output contracts

What form must the agent's output take? A research agent must produce a report, not take action. A reviewer must post a comment, not merge the PR. Make the output contract explicit.

## Constraint Surface Template

```markdown
## Agent Deployment: [name]

### Authorized tools
- [tool_1]: [purpose]
- [tool_2]: [purpose]

### File access
- Allowed: [paths]
- Read-only: [paths]
- Denied: [paths]

### Network access
- Allowed: [endpoints or "none"]

### Action budgets
- max_turns: [N]
- max_file_edits: [N]

### Standing orders
1. [Absolute prohibition]
2. [Absolute prohibition]
...

### Output contract
This agent must produce: [output format]
This agent must NOT: [action it should never take]

### Escalation path
If the agent cannot complete the task within these constraints, it must:
[describe what to do — report and halt, request approval, etc.]
```

## Anti-Patterns

### Constraint by honor system

Relying solely on the model's stated commitment to follow constraints: "I understand I should not modify production files." This is an instruction, not a constraint. Under pressure (a plausible justification, a multi-step task that seems to require it), honor-system constraints yield.

### Overly broad tool lists

Giving agents tools "just in case." Every tool on the list is a surface area. Add tools only when a specific task genuinely requires them.

### Unchecked scope expansion

The agent determines mid-task that it needs to touch a file outside its designated scope "to do the job properly." Without hard path constraints, it proceeds. With them, it reports the conflict and stops.

### Constraints only in the system prompt

System prompt constraints can be reasoned around ("given the goal of completing the task, it seems necessary to..."). Constraints enforced at the infrastructure layer cannot.

## Connection to Other Patterns

- **Authority Tiers**: Constraint surfaces define which tiers an agent can operate in. A deploy agent operating without Tier 3 approval tooling is not properly constrained.
- **Production AI Patterns**: Constraint surfaces prevent agents from crossing substrate boundaries they shouldn't cross.

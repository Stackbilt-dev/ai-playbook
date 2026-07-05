---
name: context-delegate
description: Keep large files, logs, PRs, issues, and data dumps out of the primary model context by using bounded off-context transforms. Use before reading large inputs for understanding, triage, extraction, or code mapping when exact bytes are not immediately required.
argument-hint: "[source/path/stdin/url and the small answer needed]"
---

You are a Context Delegation harness. Your job is to preserve the primary model's context window by transforming large source material somewhere else, or by reading it through bounded local tools, before bringing only the useful result back into the conversation.

Do not treat any specific Worker, provider, or service as required. The ontology is:

1. **Source** -- file, stdin, URL, GitHub issue, PR, log, JSON dump, generated artifact, or long conversation.
2. **Transform** -- summarize, triage, extract, code-map, patch-draft, write-draft, or locate-relevant-ranges.
3. **Executor** -- local shell tools, local OpenAI-compatible endpoint, direct provider, hosted Worker, or another configured delegate.
4. **Receipt** -- input size, method used, output size, confidence, cache status if known, and whether a targeted exact read is still needed.

## When To Use

Use this before bringing large text into the main context when the user needs a small answer:

- understanding a file over roughly 300 lines
- summarizing logs, traces, generated JSON, or CSV dumps
- classifying lists of issues, PRs, tasks, messages, errors, or TODOs
- extracting structured facts from a large source
- mapping code behavior before deciding what exact code needs to be read
- finding likely line ranges or symbols for a later targeted read

## When Not To Use

Do not delegate when:

- the source is small enough to inspect directly
- exact bytes, exact config, or exact legal/security text must be copied
- you are about to edit the code and need authoritative local context
- secrets or sensitive proprietary data would leave the machine
- the transform requires judgment that the primary model must own

For sensitive input, use only local deterministic tools or a local model endpoint.

## Execution Ladder

Choose the first available executor that fits the task and data sensitivity:

1. **Deterministic local tools**: `rg`, `wc`, `sed`, `awk`, `jq`, `head`, `tail`, language-aware test or parser commands.
2. **Local model endpoint**: Ollama, LM Studio, llama.cpp, or any OpenAI-compatible local server.
3. **Direct provider**: a user-configured OpenAI-compatible API such as Groq, Cerebras, OpenAI, Anthropic, or another provider.
4. **Hosted delegate**: a user-configured Worker, gateway, MCP tool, or organization service.
5. **Bounded manual read**: only if no delegate exists; read a small range identified by local tools.

Never assume Stackbilt infrastructure exists. A hosted Worker is an optional executor, not the skill.

## Preferred Workflow

1. State the delegation goal in one sentence: what small answer is needed?
2. Estimate input size with `wc -l`, `wc -c`, `rg --files`, or an equivalent cheap command.
3. Pick the executor from the ladder above.
4. Run the smallest transform that can answer the question.
5. Return only the compact answer plus a receipt.
6. If exact proof is needed, read only the targeted line range or symbol afterward.

## Transform Recipes

### Summarize

Goal: capture the source's structure and the few facts relevant to the user's question.

Output:

```text
Summary:
- ...

Relevant anchors:
- file_or_source:line_or_symbol -- why it matters

Receipt:
- source: ...
- method: ...
- input: ... lines / ... chars
- output: ... bullets
- exact read needed: yes/no
```

### Triage

Goal: classify many records without carrying the records into context.

Output compact groups, counts, examples, and outliers. Prefer tables only when they are small.

### Extract

Goal: pull specific facts from a large source. Use JSON only when the user asks or downstream automation needs it.

Never invent missing fields. Mark unavailable values as `unknown`.

### Code Map

Goal: explain what code does before deciding what to read exactly.

Return functions, classes, call flow, side effects, external dependencies, and likely line ranges. Do not rewrite code.

### Locate Relevant Ranges

Goal: find the smallest exact context the primary model needs.

Use local tools first:

```bash
rg -n "pattern|symbol|route|config_key" path
sed -n 'START,ENDp' path
```

Return only the ranges worth reading next.

## Backend-Neutral Configuration

If a project has a delegate script, prefer environment-neutral names:

```bash
CONTEXT_DELEGATE_BACKEND=auto
CONTEXT_DELEGATE_CACHE=filesystem
CONTEXT_DELEGATE_MAX_INPUT_CHARS=50000
CONTEXT_DELEGATE_TIMEOUT_MS=30000
CONTEXT_DELEGATE_WORKER_URL=https://example.com/delegate
```

The backend may be `local`, `openai-compatible`, `groq`, `cerebras`, `openai`, `anthropic`, `worker`, or `none`. If no backend is configured, use deterministic local tools and bounded reads.
Keep credentials in environment variables or the user's local secret manager; never commit them into a skill file.

## Receipt Discipline

Every delegated answer should end with a short receipt:

```text
Receipt: source=... method=... input=... output=... confidence=high|medium|low exact_read_needed=yes|no
```

Confidence rules:

- `high`: deterministic extraction, cache hit, or clear model answer with obvious anchors
- `medium`: model summary without exact line proof
- `low`: ambiguous source, truncated input, weak backend, or conflicting signals

## Operating Rule

The primary model should see the result of the transform, not the whole source. If the transform says an exact read is required, read the smallest relevant slice next.

Delegate or bound the following context:

$ARGUMENTS

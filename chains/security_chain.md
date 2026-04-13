---
title: "Security Review Chain"
category: "chains"
tags: ["security", "audit", "vulnerability", "review", "bugfix", "production"]
created: "2026-04-13"
updated: "2026-04-13"
version: 1.0
author: "AI Playbook"
dependencies: ["adversarial-review skill", "structured-review skill"]
---

# Security Review Chain

## Context

A structured security review workflow for code changes that touch security-sensitive paths: authentication, authorization, payments, secret handling, input validation, file access, or external integrations.

This chain runs two passes — an adversarial review that hunts for vulnerabilities, followed by a remediation phase, and a final verification pass to confirm fixes are correct and haven't introduced new issues.

Use when:
- Changing auth, session management, or token handling
- Adding or modifying API endpoints that accept user input
- Touching payment or billing flows
- Changing file upload/download handling
- Any change flagged as security-relevant in code review

## Chain Overview

```
Scope → Adversarial Audit → Triage → Remediation → Verification → Sign-Off
```

---

## Stage 1: Scope Definition

### Prompt

```
You are the security review coordinator. Define the scope for this security review.

Change being reviewed: {change_description}
Files changed: {changed_files}

Identify:
1. Which security domains does this change touch?
   (auth, authz, input validation, secrets, file handling, payments, dependencies, session management, API surface)

2. What is the blast radius if this change has a vulnerability?
   (affects single user / all users / external systems / data integrity)

3. What is the highest-risk file or function in this change?

4. Are there any third-party dependencies being added or updated? If so, flag them for supply chain review.

Output a scope summary that the adversarial reviewer will use to focus their audit.
```

### Parameters
- `change_description`: Description of what changed
- `changed_files`: List of files in the diff

### Output
Scope summary with security domains, blast radius assessment, and high-risk targets.

---

## Stage 2: Adversarial Audit

### Prompt

```
You are an adversarial security reviewer. Your job is to find vulnerabilities, not to be balanced.

Scope from Stage 1: {scope_summary}

Review the following code for security vulnerabilities. Focus your attention on the high-risk areas identified in the scope. For every finding:
- Severity: CRITICAL / HIGH / MID / LOW
- Location: file:line
- Vulnerability class: (injection, auth bypass, IDOR, path traversal, etc.)
- Reproduction path: how is this exploited?
- Impact: what can an attacker do?

Do not report style issues or non-security bugs here — save those for the code quality review.

Code to review:
{code_or_diff}
```

### Parameters
- `scope_summary`: Output from Stage 1
- `code_or_diff`: The code or diff being reviewed

### Output
Prioritized list of security findings with severity, location, exploitation path, and impact. "No findings" is a valid output.

### Decision gate
**Human triage required.** Operator reviews findings and decides:
- CRITICAL / HIGH → must fix before merge, advance to Stage 3
- MID / LOW only → advance to Stage 5 (verify + sign-off)
- No findings → advance to Stage 5

---

## Stage 3: Remediation Planning

### Prompt

```
You are a security engineer planning the fix.

Findings to address:
{prioritized_findings}

For each CRITICAL and HIGH finding, propose:
1. The specific code change that fixes it
2. Whether the fix might introduce a regression (and how to avoid it)
3. Whether a test can be written to prevent this vulnerability from reappearing
4. Any related issues that should be checked (e.g., "this pattern appears in 3 other files")

Output a remediation plan: ordered list of fixes, starting with CRITICAL.
```

### Parameters
- `prioritized_findings`: CRITICAL and HIGH findings from Stage 2

### Output
Ordered remediation plan with specific fixes, regression risk, and test recommendations.

### Decision gate
**Human review.** Operator approves remediation plan before implementation.

---

## Stage 4: Implement Fixes

### Prompt

```
Implement the approved remediation plan.

Plan: {remediation_plan}

For each fix:
1. Implement the change
2. Write or update the test that covers this vulnerability
3. Confirm the fix addresses the root cause, not just the symptom

After all fixes are implemented, run the test suite to confirm nothing regressed.

Output: list of changes made, tests added/updated, test results.
```

### Parameters
- `remediation_plan`: Approved plan from Stage 3

### Output
Implementation summary: changes made, tests added, test results.

### Decision gate
**Automatic gate.** Tests must pass before proceeding to verification.

---

## Stage 5: Verification Pass

### Prompt

```
You are a security verifier. Re-review the changed code after remediation.

Original findings: {original_findings}
Fixes implemented: {fixes_implemented}

For each original finding:
1. Is the fix present and correct?
2. Does the fix address the root cause or just the symptom?
3. Has the fix introduced any new vulnerabilities?

Additionally: does the remediated code introduce any issues not present in the original review?

Output: VERIFIED (finding resolved), PARTIAL (fix present but incomplete), or REGRESSED (new issue introduced) for each original finding. Plus any new findings.
```

### Parameters
- `original_findings`: Findings from Stage 2
- `fixes_implemented`: Summary of changes from Stage 4

### Output
Per-finding verification status and any new issues found.

### Decision gate
**All CRITICAL and HIGH findings must be VERIFIED before sign-off.** PARTIAL or REGRESSED blocks merge.

---

## Stage 6: Security Sign-Off

### Prompt

```
Write the security review sign-off for this change.

Change reviewed: {change_description}
Findings: {original_findings_summary}
Disposition: {verification_results}

Output a sign-off suitable for the PR description or audit log:

---
Security Review: [PASS / CONDITIONAL PASS / FAIL]
Reviewer: [role]
Scope: [domains reviewed]
Findings: X critical, Y high, Z mid — [all resolved / N outstanding]
Tests added: [Y/N, description]
Notes: [anything the next reviewer or operator should know]
---
```

### Output
Formal sign-off statement suitable for PR or audit trail.

---

## Chain Usage Notes

- Never skip Stage 2 for security-sensitive changes, even if you believe the change is safe
- The adversarial reviewer in Stage 2 should be run with maximum skepticism — it is intentionally looking for problems
- Stage 5 verification must be run by a different "agent session" than Stage 4 (or at minimum, a fresh review without memory of the fixes) to avoid confirmation bias
- If new CRITICAL or HIGH findings appear in Stage 5, restart from Stage 3

## Example Workflow

**Change:** Adding a user-facing file upload endpoint

1. **Scope**: File handling, input validation, storage access — HIGH blast radius
2. **Adversarial Audit**: Finds path traversal risk (HIGH) and missing file type validation (HIGH)
3. **Triage**: Both findings require fix — advance to Stage 3
4. **Remediation Plan**: Validate file type via magic bytes (not extension), restrict upload path to sandboxed directory
5. **Implement**: Fixes applied, two security regression tests added, suite passes
6. **Verification**: Both original findings verified resolved, no new issues
7. **Sign-Off**: PASS — 2 HIGH findings resolved, 2 tests added

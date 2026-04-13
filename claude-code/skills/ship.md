---
name: ship
description: Self-healing release pipeline. Runs pre-flight checks, typecheck, version bump, CHANGELOG update, deploy, health verification, and smoke tests in sequence. Diagnoses and remediates failures before escalating. Use for any production deploy.
argument-hint: "[optional: specific concerns or skip flags]"
---

You are a senior release engineer running a production deployment. Work through each stage in sequence. If a stage fails, diagnose the root cause before attempting remediation. Do not skip stages or proceed past a hard failure. Report clearly what passed, what failed, and what you did about it.

---

## Stage 1: Pre-Flight

Before touching anything, verify the release is ready:

1. **Uncommitted changes** — run `git status`. If there are uncommitted changes, list them. Do not proceed until they are committed, stashed, or intentionally ignored with explanation.
2. **Branch state** — confirm you are on the correct release branch, not main directly (unless main is the deploy branch for this project).
3. **CI status** — check the most recent CI run. If it is failing or pending, do not proceed. Report the failure.
4. **Version check** — confirm the version in the project's version file has been bumped since the last deploy. If not, flag it — the deploy will be rejected by post-deploy verification if version matches.

**Hard failures** (stop the pipeline):
- Uncommitted changes to tracked files
- CI failing on the deploy branch
- Missing version bump

---

## Stage 2: TypeCheck

Run the project's typecheck command. For TypeScript projects, this is typically `npm run typecheck` or `tsc --noEmit`.

- If typecheck passes: proceed
- If typecheck fails: do NOT proceed. Show the errors. Determine if they are pre-existing (existed before your changes) or new (introduced by your changes). Fix new errors. If errors are pre-existing, report them explicitly — do not silently skip.

---

## Stage 3: Tests

Run the test suite. Report pass/fail counts and any failing tests.

- If all tests pass: proceed
- If tests fail: show the failure output. Determine if failures are related to your changes. Fix if possible. If a pre-existing test failure blocks deploy, escalate to the operator — do not deploy over red tests without explicit acknowledgment.

---

## Stage 4: Version + CHANGELOG

Confirm version has been bumped appropriately (patch for fixes, minor for features, major for breaking changes). Confirm CHANGELOG has an entry for this release.

If version is not bumped: bump it now and update CHANGELOG before continuing.

CHANGELOG entry format:
```
## [X.Y.Z] — YYYY-MM-DD
### Added / Changed / Fixed
- [Change description]
```

---

## Stage 5: Deploy

Execute the deploy command for this project. Capture the output. Note the deployed version.

If deploy fails:
1. Read the error output carefully
2. Identify the root cause (missing secret, build error, size limit, etc.)
3. Fix the root cause if possible
4. Re-run — do not accumulate failed deploys without understanding why

---

## Stage 6: Health Verification

After deploy, verify the new version is live. For most projects: hit the `/health` endpoint and confirm the version field matches what you just deployed.

```
Expected version: X.Y.Z
Actual response: [paste health response]
```

If version does not match: the deploy may not have taken effect. Wait 30 seconds and retry once. If still wrong, report — do not assume success.

---

## Stage 7: Smoke Tests

Run basic functional tests against the deployed instance. At minimum:
- Confirm the primary endpoint responds with expected status
- Confirm authentication is working if applicable
- Confirm any endpoint that was changed in this release behaves correctly

---

## Stage 8: Release Summary

Output a brief release summary:

```
Release: vX.Y.Z
Deployed: [timestamp]
Changes: [1-3 bullet summary from CHANGELOG]
Verified: [health check result]
Smoke tests: [pass/fail]
Open issues: [anything that needs follow-up]
```

---

Now execute this pipeline for:

$ARGUMENTS

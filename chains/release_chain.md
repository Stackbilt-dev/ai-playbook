---
title: "Release Chain"
category: "chains"
tags: ["release", "deploy", "ci", "versioning", "changelog", "production", "governance"]
created: "2026-04-13"
updated: "2026-04-13"
version: 1.0
author: "AI Playbook"
dependencies: ["governed-deploy skill", "ship skill"]
---

# Release Chain

## Context

A structured end-to-end release workflow for production software. This chain gates each phase of a release: pre-flight checks must pass before typecheck, typecheck before version bump, version bump before deploy, and deploy before done. Human operator reviews are built in at defined decision points.

Use this chain for any release where you want a documented, repeatable process. It is especially useful for:
- First deploy on a new project
- Deploys after significant changes
- Any deploy where something went wrong last time

## Chain Overview

```
Pre-Flight → Type + Test → Version + CHANGELOG → Deploy → Verify → Summary
```

---

## Stage 1: Pre-Flight

### Prompt

```
You are the release gatekeeper. Check whether the codebase is ready to release.

Run:
1. git status — report any uncommitted changes
2. Check current branch matches the intended deploy branch
3. Check last CI run status (or run tests locally if CI is unavailable)
4. Review the version file — has it been bumped since the last release?

Output a pre-flight report:
- READY: [items that are clean]
- BLOCKING: [items that must be fixed before proceeding]

Do not proceed if there are any BLOCKING items.
```

### Parameters
- `project_path`: Local path to the project
- `deploy_branch`: The branch to deploy from (e.g., main)
- `version_file`: Where the version is tracked (package.json, version.ts, etc.)

### Output
Pre-flight report with READY / BLOCKING breakdown. Operator reviews and fixes BLOCKING items before Stage 2.

### Decision gate
**Human review required.** Operator confirms BLOCKING items are resolved before advancing.

---

## Stage 2: TypeCheck + Tests

### Prompt

```
Run the full type check and test suite for this project.

TypeCheck: {typecheck_command}
Tests: {test_command}

Report:
- TypeCheck: PASS / FAIL (with error list if failed)
- Tests: PASS / FAIL (with failing test names if failed)

If either fails, stop. List exactly what is failing and provide your best analysis of the root cause for each failure. Do not proceed to deploy over a failing typecheck or failing tests.
```

### Parameters
- `typecheck_command`: e.g., `npm run typecheck`
- `test_command`: e.g., `npm test`

### Output
TypeCheck and test results. If any failure, root cause analysis per failure.

### Decision gate
**Automatic gate.** Chain proceeds only if both pass. Any failure blocks until fixed.

---

## Stage 3: Version Bump + CHANGELOG

### Prompt

```
Review the current version and CHANGELOG.

Current version: {current_version}
Last deployed version: {last_deployed_version}

1. Has the version been bumped since last deploy? If not, determine the appropriate bump (patch/minor/major) based on the changes in this release and bump it.
2. Does CHANGELOG.md have an entry for this version? If not, write one now based on the git log since the last version tag.

CHANGELOG format:
## [{version}] — {date}
### Added
- [new features]
### Changed  
- [changes to existing features]
### Fixed
- [bug fixes]

Output the final version number and CHANGELOG entry that will go into the commit.
```

### Parameters
- `current_version`: Current version in version file
- `last_deployed_version`: Version currently live in production

### Output
Confirmed version number and CHANGELOG entry text. Operator commits these changes.

### Decision gate
**Human review.** Operator reviews and commits version + CHANGELOG before Stage 4.

---

## Stage 4: Deploy

### Prompt

```
Execute the deploy.

Deploy command: {deploy_command}

Run it. Capture all output. Report:
- Deploy succeeded / failed
- If failed: paste the error output and identify the root cause
- If succeeded: note the deployment timestamp

If deploy fails:
1. Read the error carefully
2. Identify the root cause category (missing secret, build error, auth failure, size limit, etc.)
3. Propose a specific fix
4. Do NOT re-run blindly — fix the root cause first, then re-run once
```

### Parameters
- `deploy_command`: e.g., `npx wrangler deploy`

### Output
Deploy result (success/failure), timestamp if successful, root cause analysis + fix proposal if failed.

### Decision gate
**Automatic gate.** Chain proceeds only if deploy reports success.

---

## Stage 5: Health Verification

### Prompt

```
Verify the deployment is live and healthy.

Health endpoint: {health_url}
Expected version: {deployed_version}

1. Hit the health endpoint
2. Confirm the returned version matches {deployed_version}
3. Confirm the status field indicates healthy

If version does not match: wait 30 seconds, retry once. If still mismatched, report — do not assume success.
If health check fails (non-200 or unhealthy status): report immediately — this is a production incident.

Output: VERIFIED / DEGRADED / FAILED with details.
```

### Parameters
- `health_url`: Health endpoint URL
- `deployed_version`: The version just deployed

### Output
Health check result with version confirmation.

### Decision gate
**Automatic gate.** DEGRADED or FAILED triggers operator rollback decision.

---

## Stage 6: Release Summary

### Prompt

```
Write a release summary for this deployment.

Include:
- Version released
- Deploy timestamp
- Key changes (from CHANGELOG entry)
- Health check result
- Any issues encountered and how they were resolved
- Any follow-up work identified during this release

Format it for a team update or commit message. Keep it under 200 words.
```

### Output
Release summary suitable for sharing or archiving.

---

## Chain Usage Notes

- Each decision gate is a natural pause point for a human to review progress
- Stages 2 and 5 are automated gates — they block on failure without human approval
- Stages 1, 3, and (implicitly) 4 involve human review before proceeding
- If you need to run Stage 4 multiple times due to failures, document each attempt and its failure reason

## Example Workflow

**Project:** API service, patch release fixing a rate limiting bug

1. **Pre-Flight**: Clean status, on main, CI green, version not yet bumped — 1 BLOCKING item
2. **Fix**: Bump version from 2.4.1 to 2.4.2, move to Stage 2
3. **TypeCheck + Tests**: Both pass — proceed
4. **Version + CHANGELOG**: Version bumped, CHANGELOG entry written — operator commits
5. **Deploy**: `npx wrangler deploy` — succeeds, timestamp noted
6. **Health**: Version 2.4.2 confirmed live — VERIFIED
7. **Summary**: 3-bullet summary posted to team channel

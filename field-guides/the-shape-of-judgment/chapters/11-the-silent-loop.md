# 11. Case File: The Silent Loop

This case comes from ColonyOS's post-incident record. For approximately eight
hours, its cognitive tick loop ran every fifteen minutes, made decisions, and
then discarded them. The heartbeat was alive. The system was not progressing.

## The Apparent Health

The alarm fired. The tick ran. The alarm was rescheduled. Diagnostics
responded. From the outside, the service looked active.

The authoritative tick counter remained at 3. Twenty deferred events
accumulated. That contradiction—activity without durable progress—was the
signal that mattered.

## The Kill Chain

```text
alarm fires
  → load tick 3
  → tick mutates state to 4
  → optional AEGIS notification is awaited
  → upstream returns plain text instead of JSON
  → response.json() throws
  → alarm catch discards in-memory state
  → finally schedules the next alarm
  → tick 4 is never persisted
  → repeat from tick 3
```

The notification was documented as “never block, never throw,” but its
implementation allowed an uncaught parse error to cross the boundary. It ran
between the critical mutation and the save operation, so an optional external
effect became a persistence dependency.

## Claims, Evidence, and Uncertainty

| Claim | Evidence | Confidence | Decision use |
|---|---|---:|---|
| The heartbeat is executing | Alarm and endpoint logs | High | Liveness only |
| The colony is progressing | Tick counter remained at 3 | False | Must not be inferred from liveness |
| The external call failed | Plain-text response and parse error | High | Isolate notification |
| State was saved | No storage receipt after tick 3 | False | Persistence must have its own receipt |
| The next alarm exists | Alarm rescheduling log | High | Recovery scheduling only |

The failure was not simply “the API returned an error.” The deeper failure was
that the system treated a successful schedule as evidence of successful work.

## State and Authority Boundaries

The tick mutation and its persistence were authoritative. The AEGIS
notification was observational. The correct ordering was therefore:

```text
load → compute → persist authoritative state → schedule next alarm
                                      ↘ notify external observer
```

The notification could fail without invalidating the durable state. Its
authority was narrower than the state transition it observed.

## Repair and Promotion

The repair had four parts:

1. Defend the JSON parse boundary and return a typed failure.
2. Enforce the “never throws” notification contract at its call site.
3. Persist and schedule before awaiting optional notification work.
4. Restore a missing alarm on ordinary requests so the system can self-heal.

The incident also exposed a hydration dependency: persisted state could not
assume class instance methods survived a storage round trip, so viability logic
was moved to a static, reconstructable operation.

These fixes were promoted because each one changed an observable invariant:
the tick counter advances, storage receives a receipt, malformed responses do
not erase state, and a missing alarm is recreated.

## Field Tests

Replay the worker with:

- a plain-text upstream error;
- an empty upstream body;
- a valid error-shaped JSON response;
- a notification timeout after state mutation;
- a missing alarm before the next request.

The test is not merely “does the request return 200?” It is whether the
authoritative tick advances exactly once, optional notification failure is
visible, and recovery remains possible.

## Transferable Lesson

Liveness is not progress. A system has completed governed work only when the
authoritative state transition and its receipt exist. External calls are
hostile boundaries, and optional observations must never sit in front of
critical persistence.

Source receipt: [ColonyOS Lore 18 — The Silent Loop](https://github.com/Stackbilt-dev/colonyos/blob/main/lore/18-the-silent-loop.md).

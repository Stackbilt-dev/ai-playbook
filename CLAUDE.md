# CLAUDE.md

## OSS Policy

This is a **public infrastructure package** governed by the Stackbilt OSS Infrastructure Package Update Policy.

Rules:
1. **Additive only** — never remove or rename public API without a major version bump
2. **No product logic** — framework patterns and generic utilities only. If a competitor could reconstruct Stackbilt product architecture from this code, it doesn't belong here.
3. **Strict semver** — patch for fixes, minor for new features, major for breaking changes
4. **Tests travel with code** — every public export must have test coverage
5. **Validate at boundaries** — all external API responses validated before returning to consumers

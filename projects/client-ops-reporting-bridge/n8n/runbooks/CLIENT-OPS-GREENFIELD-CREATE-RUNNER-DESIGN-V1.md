# Greenfield Create Runner Design — Client Ops

**Status:** DESIGN + IMPLEMENTED RUNNER
**Skeleton path:** `../runners/run-client-ops-greenfield-create.skeleton.mjs`
**Live runner:** `../runners/run-client-ops-greenfield-create.mjs`
**Phase 1B-B executed create:** YES (inactive; blocked auth)

## Runner steps

1. Load prepared local apply payload.
2. Allow blocked-inactive placeholder mode when authorized.
3. Validate node types / typeVersions.
4. Validate graph / connections.
5. Validate workflow name.
6. Validate inactive create (no active=true).
7. Reject credentials in JSON for blocked mode.
8. Reject secrets / absolute URLs.
9. Reject webhook IDs in create payload.
10. Reject Telegram nodes.
11. Produce create payload.
12. Require `--apply`.
13. Require confirmation phrase `CREATE INACTIVE MARS CLIENT OPS BRIDGE BZPM`.
14. POST through separate write-capable client.
15. Re-GET created workflow via GET-only client.
16. Sanitize evidence.
17. Record rollback / delete boundary.
18. Never activate automatically.

## Hard boundaries

- Do **not** use GET-only `n8n-readonly-exporter` for writes.
- Preserve GET-only client rejection of non-GET methods.
- Do **not** modify MetaBOT SEO production or sandbox workflows.
- Do **not** send webhook tests from the create runner unless a later charter says so.

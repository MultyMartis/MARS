# Greenfield Create Runner Design — Client Ops

**Status:** DESIGN + SKELETON
**Skeleton path:** `../runners/run-client-ops-greenfield-create.skeleton.mjs`
**Executed create in this task:** NO

## Future runner steps

1. Load template.
2. Reject unresolved placeholders.
3. Validate node types / typeVersions.
4. Validate graph / connections.
5. Validate workflow name.
6. Validate inactive state.
7. Reject credentials in JSON unless explicitly approved.
8. Reject secrets.
9. Reject webhook IDs.
10. Reject Telegram nodes.
11. Produce create payload.
12. Require `--apply`.
13. Require explicit operator confirmation input.
14. POST through separate write-capable client.
15. Re-GET created workflow.
16. Sanitize evidence.
17. Record rollback / delete boundary.
18. Never activate automatically.

## Hard boundaries

- Do **not** use GET-only `n8n-readonly-exporter` for writes.
- Preserve GET-only client rejection of non-GET methods.
- Do **not** modify MetaBOT SEO production or sandbox workflows.
- Do **not** send webhook tests from the create runner unless a later charter says so.

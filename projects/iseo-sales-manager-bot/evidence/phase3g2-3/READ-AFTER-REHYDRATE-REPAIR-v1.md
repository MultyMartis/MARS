# READ-AFTER-REHYDRATE REPAIR v1

**Phase:** 3G.2.3  
**Patch boundary:** Admin.dev Start node only (same workflow ID, 85 nodes)

---

## Change

Start reply-name resolution now:

1. Prefers `j.access_upsert` from Check User Authorization (post-rehydrate).
2. Falls back to `Read ACCESS_CONTROL` only if upsert name is blank.
3. Uses `reply_sender_name` only (fail-closed «не задано»).
4. Stamps `reply_profile_resolver_version = iseo-reply-profile-resolver-v1.0`.

Library helper (offline / harness parity):

`resolveStartReplySenderName` in `implementation/runtime-libs/reply-profile-resolver-v1.mjs`.

---

## Deploy

| Field | Value |
|-------|-------|
| Workflow | Admin.dev `wLrLp4WQHm1VJmxz` |
| Method | deactivate → PUT same ID → activate |
| Nodes before/after | **85 / 85** |
| Start hash before | `9436A389742AF744` |
| Start hash after | `7E0A13DB067254EF` |
| Operational.dev | untouched |
| Workflows created | **0** |
| Marker | `Phase 3G.2.3 — read-after-rehydrate` |

Receipt: `deploy-report-3g23.json`. Tail: `node-Start.tail.sanitized.js`.

---

## Single-execution invariant

Given wiped sheet + rehydrated `access_upsert` (exec 24097 shape), Start must render `Имя в ответах: Михаил` in **that same** execution — not only after upsert writeback.

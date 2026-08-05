# REPLY PROFILE READ-PATH UNIFICATION v1

**Phase:** 3G.2.2
**Status:** current implementation spec
**Authority:** [architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](../architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md)
**Runtime:** `implementation/runtime-libs/reply-profile-resolver-v1.mjs` (new) · `reply-profile-lib.mjs` (updated) · `reply-profile-commands-v1.mjs` (updated)

---

## 1. What changed in code

| File | Change |
|------|--------|
| `reply-profile-resolver-v1.mjs` | **New.** Exposes `resolveReplyProfile`, `approvedSeedForRow`, `buildProfileRehydratePatch`, `REPLY_PROFILE_ACCESS_FIELDS`, `pickReplyProfileFields`, `mergeRehydrateIntoUpsert`, `formatResolvedProfileCard`, `formatMyReplyProfile`. |
| `reply-profile-lib.mjs` | Adds `REPLY_PROFILE_RESOLVER_VERSION` alias export (`iseo-reply-profile-resolver-v1.0`) so both files agree on one version string. Validation and numbering logic unchanged. |
| `reply-profile-commands-v1.mjs` | Re-exports resolver + rehydrate helpers so Admin.dev Code nodes have a single import surface for both command formatting and rehydrate. |

## 2. n8n node-level implementation notes (Admin.dev, same workflow ID)

1. **Check User Authorization** — the row-projection helper (`rowFromSheet()`-equivalent Code logic) is extended with `REPLY_PROFILE_ACCESS_FIELDS` so authorization context always carries the full profile, not a stripped subset. This is the fix for the read-side half of the defect.
2. **Last-seen upsert (`/start` / `/my_status`)** — the write mapping passed to the ACCESS_CONTROL upsert now calls `mergeRehydrateIntoUpsert(row, actorLabel)` instead of building a bare `{ display_name, role, status, last_seen_at }` object. This both (a) carries forward the current profile fields so they are never silently dropped from the write, and (b) restores approved seed values if the row was already wiped from a prior execution.
3. **Reply Profile Commands node** — `/reply_profiles`, `/reply_profile N`, `/my_reply_profile` each call rehydrate-then-resolve before formatting, so a stale wiped row is corrected in the same response that displays it.
4. **Start node** — reply-name line reads the rehydrated row; if no approved seed exists for the identity, renders the existing "не задано" fail-closed text rather than falling back to display name or username.
5. **Config Summary node** — adds `resolver_version`, corrected parser-version display, reporting-sync honesty line, and active-recipient count sourced from the same resolver contract (see `CONFIG-TRUTH-FORENSIC-v1.md`).

## 3. Operational.dev implementation notes

`Expand Delivery Recipients` gains a version-stamp field (`resolver_version=iseo-reply-profile-resolver-v1.0`) on its output for traceability. No structural node change; personalization logic already read ACCESS_CONTROL profile fields directly and is confirmed unaffected by regression check (`evidence/phase3g2-2/OPERATIONAL-PERSONALIZATION-REGRESSION-v1.md`).

## 4. Deployment method

Same pattern as prior phases: deactivate Admin.dev → PUT same workflow ID with patched nodes → reactivate. No new workflow created. No node deleted. Reply Profile Commands mutation logic (`/reply_name_set`, `/reply_name_enable`, `/reply_name_disable`) is untouched by this patch — only resolution/rehydrate wiring changed.

## 5. Test coverage

`implementation/harness/phase3g22-harness.mjs` (53/53 PASS) exercises the exact wiped-row shape captured in the forensic and confirms:

- Rehydrate restores Андрей/Михаил without touching numbers, roles, or access status.
- No fallback to nickname, display name, or username under any condition.
- All command surfaces converge on one `resolver_version`.
- Config truth fields (parser version, resolver version, Moscow stats formatting, reporting-sync state, active-recipient count) are correct.

Regression: `implementation/harness/phase3g2-harness.mjs` (42/42 PASS) confirms the Phase 3G.2 numbering/text-contract baseline is unaffected.

## 6. Non-goals

- Does not change ACCESS_CONTROL row schema (no new columns).
- Does not restore access for MOD_B_REVOKED / MOD_C_REVOKED.
- Does not enable AI or reminders.
- Does not create a new workflow or duplicate the profile store.

## Related

- [architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](../architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md)
- [architecture/REPLY-PROFILE-CONTRACT-v1.md](../architecture/REPLY-PROFILE-CONTRACT-v1.md)
- [REPLY-PROFILE-ADMIN-COMMANDS-v2.md](REPLY-PROFILE-ADMIN-COMMANDS-v2.md)
- Evidence: `evidence/phase3g2-2/`

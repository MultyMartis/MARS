# PENDING COMMANDS v1 — implementation spec

**Target workflow:** `i-SEO Sales Manager - Admin.dev` (`wLrLp4WQHm1VJmxz`)
**Phase:** 3F.1
**Pattern source:** existing Admin command router (`Route Command` switch, per `ADMIN-WORKFLOW-PATCH-SPEC-v1.md`); reuses `Read Authorization Config` / ACCESS_CONTROL authorization path unchanged

---

## 1. New commands

| Command | Handler role | Args |
|---|---|---|
| `/pending_count` | staff read | none |
| `/pending_leads` | staff read | optional `[page]`, optional `test` (Admin only, ignored/denied for moderator) |
| `/pending_leads_test` | Admin config | optional `[page]` (implicit `includeTests=true`) |

## 2. Node additions (Route Command branch)

| # | Stable name | Type | Responsibility | Connection |
|---|---|---|---|---|
| a | Read CLEAN for Pending | `googleSheets` (read, bounded) | Read `lead_clean_v2` for pending-view computation | → Build Pending View |
| b | Build Pending View | `code` | `buildPendingView()` (mirrors `implementation/runtime-libs/pending-leads-lib.mjs`) | → Route: count \| list |
| c | Format Pending Count | `code` | `formatPendingCountReply()` | → Safe Telegram Reply |
| d | Parse Pending Args | `code` | `parsePendingLeadsArgs()` | → Paginate Pending |
| e | Paginate Pending | `code` | `paginatePending()` | → Format Pending List |
| f | Format Pending List | `code` | `formatPendingListReply()` (HTML-escaped) | → Safe Telegram Reply |

All new Code nodes are pure-JS mirrors of `implementation/runtime-libs/pending-leads-lib.mjs` (no Node built-in modules, consistent with the Phase 3D.5.2 pure-JS SHA-256 precedent for Admin Code nodes).

## 3. Authorization

Reuses the existing `Read Authorization Config` / ACCESS_CONTROL read already in the Admin graph; the new `authorizePendingCommand()` check runs against the same role/status snapshot — no second authorization read is introduced. Deny path returns to the standard `Safe Telegram Reply` deny wording used by other Admin commands.

## 4. `/pending_leads_test` guard

Only reachable when `authorizePendingCommand` resolves `admin_cfg` class as allowed (i.e. active Admin). A moderator sending `/pending_leads test` (or `/pending_leads_test`) is denied before the test-inclusive branch is ever evaluated — test inclusion is never silently granted to a moderator via argument smuggling.

## 5. Non-goals

- No lifecycle mutation from these commands (read-only).
- No new Sheets tab (reads existing `lead_clean_v2`).
- No inline keyboard on pending-view output.
- No AI involvement.

## 6. Node count impact

Combined with the reminder command/schedule nodes (`implementation/REMINDER-CONFIG-COMMANDS-v1.md`), Admin.dev moved **59 → 79 nodes** (+20 total for Phase 3F.1).

---

*Related: [../architecture/PENDING-LEADS-VIEW-v1.md](../architecture/PENDING-LEADS-VIEW-v1.md), `../evidence/phase3f1/PENDING-COUNT-ACCEPTANCE-v1.md`, `../evidence/phase3f1/PENDING-LIST-ACCEPTANCE-v1.md`, `../evidence/phase3f1/PAGINATION-ACCEPTANCE-v1.md`.*

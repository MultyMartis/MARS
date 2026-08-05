# PENDING LEADS VIEW v1

**Product:** i-SEO Sales Manager Bot
**Phase:** 3F.1
**Scope:** read-only pending-lead visibility layer inside Admin.dev (`/pending_count`, `/pending_leads`, `/pending_leads_test`)
**Status:** implemented; operator command acceptance PASS

---

## 1. Purpose

Give Admin/moderators a live, deduplicated, oldest-first view of unresolved (`pending`) leads without opening Google Sheets — a lightweight visibility layer on top of the existing lifecycle model (`architecture/LEAD-LIFECYCLE-v1.md`), not a new lifecycle.

## 2. Data source

Single source of truth: `lead_clean_v2` (CLEAN workbook), the same tab lifecycle callbacks already mutate. No new tab is required for the view itself.

## 3. Lifecycle resolution

See `evidence/phase3f1/PENDING-SOURCE-FORENSIC-v1.md` for the forensic finding. Rule, in priority order:

1. `manager_status` (primary, current lifecycle field).
2. `lifecycle_status` (secondary, Phase 3D.3 compatibility field).
3. `close_reason` (tertiary signal).
4. Absent all three → treated as `pending` (legacy rows Olya has not yet closed).

Only rows resolving to `pending` enter the view.

## 4. Exclusions

Applied before lifecycle resolution or in addition to it:

- Technical-retry-only rows (infrastructure artifacts, never business leads).
- Probable-invalid / empty-shell rows (no business key and no identifying content).
- Probable-test rows (reuses the Phase 3E.2.2 probable-test signal set) — excluded from the **default** view; visible only via the Admin-only `/pending_leads_test` / `pending_leads test` variant.
- `processed` / `spam` rows.

## 5. Deduplication

By **business key** (`stable_lead_ref` → `lead_id` → Gmail message id → composite fallback), never by raw Sheets row — one physical duplicate row for the same logical lead (e.g. a retried write) is counted once, preferring the most recent / most field-complete copy.

## 6. Ordering and aggregation

Oldest-first (operational attention order). Aggregate age buckets (`under_2h`, `from_2h_to_24h`, `over_24h`, `unknown`) drive both the `/pending_count` summary line and the reminder message's "oldest waiting" callout.

## 7. Rendering

- `/pending_count` — compact count + bucket summary (`evidence/phase3f1/PENDING-COUNT-ACCEPTANCE-v1.md`).
- `/pending_leads [page] [test]` — paginated card-style list, HTML-escaped, default page size 5 / max 10 (`evidence/phase3f1/PENDING-LIST-ACCEPTANCE-v1.md`, `evidence/phase3f1/PAGINATION-ACCEPTANCE-v1.md`).
- No inline lifecycle buttons on these views — this is a **read** surface; lifecycle mutation remains exclusively the existing pending-card callback path.

## 8. Authorization

Staff-read class (active Admin or active moderator); `/pending_leads_test` is Admin-only. See `evidence/phase3f1/COMMAND-AUTHORIZATION-v1.md`.

## 9. Invariant

The view is always computed live from current CLEAN data — there is no separate cached pending list to desynchronize from the lifecycle callback path (`evidence/phase3f1/POST-LIFECYCLE-PENDING-ACCEPTANCE-v1.md`).

## 10. Not in scope

- No new Sheets tab.
- No change to `Update CLEAN Lifecycle`, callback tokens, or actor attribution.
- No AI involvement.
- No automatic client-facing message.

---

*Related: [PENDING-REMINDER-v1.md](PENDING-REMINDER-v1.md), [../implementation/PENDING-COMMANDS-v1.md](../implementation/PENDING-COMMANDS-v1.md), `../evidence/phase3f1/`.*

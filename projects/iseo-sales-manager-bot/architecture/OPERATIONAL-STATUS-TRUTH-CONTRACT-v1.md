# OPERATIONAL STATUS TRUTH CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3H.4  
**Scope:** `/status` (Admin.dev) and CONFIG keys it reads

---

## 1. Purpose

Operator `/status` must reflect **authoritative production truth**, not synthetic test stamps or on-demand health probes.

---

## 2. Field authority matrix

| Display concept | Authoritative keys / source | Forbidden substitute |
|---|---|---|
| Last Gmail **scheduled** poll | `last_poll_success_at`, `gmail_poll_heartbeat` | `/health` Gmail probe time |
| Last **production** lead processed | `last_production_processed_at`, `last_production_processed_lead_id` | `last_lead_success_at` from synth tests |
| Technical last success (if shown) | `last_success_at` / `last_lead_success_at` | Must be labeled non-production if synth may have written |
| AI | `ai_enabled` | — |
| Reminders | reminder CONFIG keys + `pending_reminder_active_recipients_count` | — |
| Reporting | `reporting_sync_state` / mode keys | Assumed auto-sync |

---

## 3. Production lead filter

Production display requires lead row invariants:

- `is_real_lead=true`
- `is_probable_test=false`
- `archive_state=active`
- `production_generation=v2`

Authoritative epoch lead: `lead_19fd2052066e18b7` · lifecycle_changed_at **2026-08-05T14:22:55.186Z** (= 05.08.2026 17:22 МСК).

---

## 4. Health separation

`/health` answers **now** — bounded probes at command time.  
`/status` answers **scheduled operational mirror** — CONFIG heartbeat and production stamps.

Never conflate the two Gmail signals.

---

## 5. Implementation reference

`implementation/STATUS-DATA-SOURCE-REPAIR-v1.md` · Evidence: `evidence/phase3h4/STATUS-DATA-SOURCE-MATRIX-v1.md`

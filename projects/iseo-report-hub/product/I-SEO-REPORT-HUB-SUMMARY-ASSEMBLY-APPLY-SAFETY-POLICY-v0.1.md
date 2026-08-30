# I-SEO Report Hub — Summary Assembly Apply Safety Policy v0.1

**Status:** CHARTER / SAFETY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01

Binding for **Summary Assembly Apply Implementation 01**. This charter wave itself performs **no** writes.

---

## 1. Environment

| Item | Rule |
|------|------|
| DB | Local `iseo_report_hub_dev` @ `127.0.0.1:3306` only |
| Production | **Forbidden** |
| WordPress / i-seo.su / WPilot | **Forbidden** |
| `.env` / `.env.local` | Do not edit |
| Runtime sync | Only exact app-source allowlist in the implementation wave — **not** this charter |

---

## 2. Backup

| Wave | Backup |
|------|--------|
| This charter | Not required (no mutation) |
| Implementation 01 **before first POST apply** | **Mandatory** full `mysqldump` of `iseo_report_hub_dev` + table dump of `report_blocks` |

If dump fails → **STOP**. No POST.

If Implementation 01 stays on fallback (no write smoke), dump is still **required before any POST that could succeed**. A POST that is expected to **refuse** on finalized report 1 may run **without** dump only if the handler cannot write (finalized gate before UPDATE). Prefer dump anyway if the agent will send any POST.

---

## 3. Allowed mutations (implementation wave, after gates)

| Target | Allowed? |
|--------|----------|
| Selected `report_blocks.body` (+ status/audit/`updated_by` / optional `data_json` merge) | **Yes**, non-finalized parent only |
| `audit_log` insert | **Yes** |
| Session/flash | Yes |
| Unselected `report_blocks` | **No** |
| Manual-only keys | **No** |
| `monthly_report_contents` text / finalize / reopen | **No** |
| `monthly_report_work_entries` | **No** |
| Catalogue tables | **No** |
| Snapshots / exports / shares / PDF artifacts | **No** |
| `schema_migrations` | **No** |

---

## 4. Finalized and shares

| Gate | Rule |
|------|------|
| Parent `finalized` / `archived` | Apply **refuses**. No bypass. |
| Active public share on the **target** monthly | Treat as **refuse** even if parent were not finalized (defense in depth). Report 1 is already blocked by finalized. |
| Historical exports on another monthly (id 1) | Must remain unchanged when testing a different monthly |
| PDF regeneration | **Forbidden** |

Finalized already covers issued report 1. Extra active-share refuse avoids a future non-finalized report that somehow still has a live token.

---

## 5. Overwrite protection

1. Per-block selection required.  
2. Confirm checkbox required.  
3. CSRF + auth (`admin_owner` / `seo_lead_reviewer`).  
4. Old `body` / `summary` / `status` captured in STORAGE evidence before UPDATE.  
5. New generated text captured in evidence.  
6. Empty completed/plan drafts do not overwrite.  
7. Identical body → skip (idempotent).

---

## 6. Idempotence

Second apply of the same selected keys with the same generated body: **no content change**. Skip UPDATE.

---

## 7. Rollback

1. Preferred: restore the dumped SQL for `iseo_report_hub_dev` (operator-approved restore charter if needed).  
2. Narrow: UPDATE the selected rows back to captured old `body` / `status` / `reviewed_at` / `approved_at` from evidence.

Do not use `git reset --hard`, `git clean`, or recursive filesystem delete.

---

## 8. Secrets

No passwords, hashes, raw share tokens, or `.env` values in git docs. Slug `test-first-link` may be named. Checksum **prefix** of export 4 may be recorded.

---

## 9. Git

Exact-path commits. No `git add .`. No push unless the operator asks. Foreign WIP preserved.

---

## 10. SAFE UNKNOWN

- Whether dump compression/path conventions from earlier i-SEO waves should be reused (implementation agent should follow the latest local dump folder under STORAGE incoming).  
- Whether `audit_log` volume/retention needs a later pruning charter (not this wave).

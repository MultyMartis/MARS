# I-SEO Report Hub — Summary Assembly Safety Policy v0.1

**Status:** CHARTER / SAFETY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01

Applies to **Summary Assembly Preview Implementation 01** (Option A). Section 5 is binding for a **future** Option B apply wave — not to be executed in Implementation 01.

---

## 1. Environment

| Item | Rule |
|------|------|
| DB | Local `iseo_report_hub_dev` @ `127.0.0.1:3306` only |
| Production | **Forbidden** |
| WordPress / i-seo.su / WPilot | **Forbidden** |
| Runtime public share | Do not create, revoke, or alter |
| PDF / export artifacts | Do not regenerate or rewrite |
| `.env` / `.env.local` | Do not edit |

---

## 2. Option A (Implementation 01) — allowed operations

| Target | Allowed? |
|--------|----------|
| SELECT work entries / monthly / blocks | Yes |
| POST any assembly route | **No** (route must not exist) |
| `report_blocks` INSERT/UPDATE/DELETE | **No** |
| `monthly_report_contents` (incl. reopen/finalize) | **No** |
| `monthly_report_work_entries` writes | **No** |
| Catalogue tables | **No** |
| Snapshots / exports / shares | **No** |
| `schema_migrations` | **No** |
| Session/audit from GET login smoke | Incidental login rows tolerated; do not hand-edit |

---

## 3. Backup (Option A)

**No DB backup required** because there are no writes.

Still required:

1. Record **before** counts: entries (report 1), `report_blocks` (report 1), exports, shares (active/revoked).  
2. Record **after** the same counts.  
3. If any count drifts → **STOP** and investigate; do not continue with apply ideas.

Optional: checksum prefix of export 4 (known `a8c4d61c6216e8d70b19…`).

---

## 4. Finalized report

Preview-only is **safe** on finalized monthly id 1: no block mutation, no PDF change.

Do not call reopen “to make assembly work”.

---

## 5. Future Option B — apply safety (not this implementation)

When a later charter authorizes apply:

| Gate | Rule |
|------|------|
| Backup | Full `mysqldump` of `iseo_report_hub_dev` **and** table dump of `report_blocks` (at least monthly id 1) **before first POST** |
| Operator approval | Explicit in that wave’s charter; not implied by this document |
| Reopen | If parent is `finalized`, apply **refuses** until `admin_owner` reopen (existing lock). Do not bypass `canMutateAgainstParent` |
| Selection | Only selected `block_key`s are written |
| Manual content | If `body` or `summary` is non-empty, skip unless confirm checkbox for **that** block |
| Preserve old text | Copy previous `body`/`summary` into implementation evidence (STORAGE, not git) and/or `data_json` previous snapshot fragment |
| Flat columns | Do not write `monthly_report_contents.*` text fields unless a later charter says dual-write |
| PDF | **No** regeneration in first apply wave |
| Shares | **No** token changes |
| Work entries | **No** rewrite as part of apply |

If dump fails → **STOP**. No POST.

Recommended apply smoke: use a **non-finalized** monthly report if one exists; **do not** reopen report 1 only for smoke unless the operator explicitly allows it.

---

## 6. Secrets

No passwords, hashes, share tokens, or `.env` values in docs, HTML evidence, or commit messages. Public share slug `test-first-link` may be named; raw token values must not be copied into git.

---

## 7. Git

Exact-path commits only. No `git add .`. No push unless operator asks. Foreign WIP preserved.

---

## 8. SAFE UNKNOWN

- Whether Option B should store previous body in `data_json` vs evidence files only.  
- Whether a dedicated non-finalized smoke monthly will exist before first apply.

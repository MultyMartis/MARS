# REPORT — I-SEO REPORT HUB REPORT DELIVERY / PUBLIC SHARE CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** Report Delivery / Public Share Charter 01  
**Created:** 2026-07-27  
**Result:** COMPLETE — docs/policy only

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `6a282380bda621658787da0bd56f0b0cb3f3b63f` |
| Staged/index on main | **non-empty**, foreign-only (`projects/client-ops-reporting-bridge/**`); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-delivery-public-share-charter-01\repo` |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** — main index untouched |
| Write scope | allowlisted docs under `projects/iseo-report-hub/product/`, `reports/`, `OPERATIONAL-INDEX.md` only |

---

## 2. Baseline Reviewed

### Metadata UI Implementation 01

| Item | Value |
|------|-------|
| Primary | `bd64bd03ec02c03592eb127cfc27ed34815aad6f` |
| Hash-record | `415da5eca71e65a7cb437ce2dac613cd3043a8db` |
| Tip | `6a282380bda621658787da0bd56f0b0cb3f3b63f` |
| Status | COMPLETE |
| Smoke | 27/27 PASS |
| Public/share | none |

### DB-09

| Item | Value |
|------|-------|
| Primary | `c1e7ba2416f1e49ef0f115d0efa23ffcb7abd317` |
| schema_migrations | **8** |
| tables | **15** |
| report_exports | **4** |
| ids 1–2 | metadata NULL |
| ids 3–4 | metadata filled; id **4** `source_html_export_id=3` |

### Export ids 1–4

| id | key | role |
|----|-----|------|
| 1 | `snapshot-1-html-v1` | legacy HTML |
| 2 | `snapshot-1-pdf-v1` | legacy PDF |
| 3 | `snapshot-1-html-v2` | styled HTML |
| 4 | `snapshot-1-pdf-v2` | styled PDF (MVP share candidate) |

### Current delivery limitation

Auth-only downloads; no public share route; no token/lifecycle/audit/public access policy; no client portal.

### DB baseline (read-only this wave)

| Metric | Value |
|--------|-------|
| Host / DB | `127.0.0.1` / `iseo_report_hub_dev` |
| schema_migrations | 8 |
| tables | 15 |
| users / roles | 1 / 6 |
| clients / projects / sites | 1 / 1 / 1 |
| reporting_periods | 2 |
| weekly_checkpoints | 4 |
| monthly_report_contents | 1 |
| report_blocks | 6 |
| report_snapshots | 1 |
| report_exports | 4 (html 2, pdf 2) |

### Artifact baseline (read-only)

| Artifact | checksum match |
|----------|----------------|
| v1 HTML | `c194c62b…626fadc4` MATCH |
| v1 PDF | `707e72d6…880d0320` MATCH |
| v2 HTML | `27a6eee6…f95f6ffe` MATCH |
| v2 PDF | `a8c4d61c…41a56b6b` MATCH |

No DB/artifact mutation.

---

## 3. Charter Output

Created / updated:

- `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-report-delivery-public-share-charter-01.md`
- `OPERATIONAL-INDEX.md` — Public Share Charter status, MVP decision, shareable policy, DB-10 next stage

---

## 4. Product Decision

| Decision | Choice |
|----------|--------|
| Selected option | **B — tokenized public share** |
| Why not A (internal-only) | Leaves client delivery gap; no link lifecycle / delivery audit |
| Why not C (portal) | Auth/UI/onboarding too large for next MVP step |
| Why not E (email) | Mail config / size / deliverability / audit complexity deferred |
| Why not D (one-time) | Extra friction; optional later via `max_access_count` |
| Why PDF-only MVP | Safer client surface than HTML; styled PDF id **4** ready; HTML share deferred |

---

## 5. Security Model

- Cryptographic random token (≥32 bytes); store **hash only**; plaintext URL once.
- Default expiry 30 days; revoke supported; public denial generic 404/410.
- Roles: create/revoke = `admin_owner`, `seo_lead_reviewer`.
- Checksum + path hardening before stream; no raw storage path; no public listing.
- Headers: Content-Type, Content-Disposition attachment, nosniff, Cache-Control private/no-store, X-Robots-Tag noindex/nofollow.
- Audit: created / revoked / accessed / deny reasons; access_count on success.

---

## 6. Data / Route Plan

- Table: `report_export_shares` (DB-10).
- Internal: `GET/POST /report-exports/{id}/shares`, `POST /report-export-shares/{id}/revoke`.
- Public: `GET /share/report/{token}` (opaque token; no export id).
- UI: export detail share card; one-time copy link; eligibility-gated create.
- Waves: DB-10 Migration Apply 01 → Public Share Implementation 01.

---

## 7. Restrictions Confirmed

- no app-source edits;
- no runtime edits;
- no DB mutation;
- no SQL/migration creation/edit;
- no share token creation;
- no public route;
- no report_exports / snapshots / blocks / monthly / weekly / period row changes;
- no artifact regeneration;
- no new export rows;
- no package install/download;
- no push / fetch / pull / reset / clean / stash.

---

## 8. Commit

| Field | Value |
|-------|-------|
| Exact-path git add | allowlisted docs only (see §11) |
| Primary commit message | `docs(iseo-report-hub): add report delivery public share charter` |
| Primary commit hash | `63d8f3e037cdb797f17f2dc955be92041852dba4` |
| Hash-record commit message | `docs(iseo-report-hub): record report delivery public share charter commit hash` |
| Hash-record commit hash | `09a91e7c7c2f8ed927e6c53daa7da24c59a285a8` |
| Tip after | `09a91e7c7c2f8ed927e6c53daa7da24c59a285a8` |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Exact HTTP status preference (404 vs 410) for revoked/expired — left as either; finalize in implementation.
- Exact rate-limiter mechanism for invalid token probes — baseline intent only; implement in Implementation 01.
- Whether short route `/r/{token}` will be requested by operator — deferred.

---

## 10. Recommended Next Action

**I-SEO Report Hub — Report Delivery Public Share DB-10 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-delivery-public-share-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | yes (worktree) |
| commit (primary + hash-record) | yes (hashes in §8 after fill) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout/update-ref | update-ref main branch to tip after worktree commits (safe; foreign WIP preserved) |
| reset | **no** |
| restore | scoped restore on main for allowlisted i-SEO docs only if needed to align WT→main |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used: `X:\AI MARS STORAGE\git-sync-iseo-report-delivery-public-share-charter-01\repo` |



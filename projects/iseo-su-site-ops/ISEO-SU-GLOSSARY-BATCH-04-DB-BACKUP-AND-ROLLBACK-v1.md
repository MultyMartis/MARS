# ISEO-SU GLOSSARY BATCH 04 DB BACKUP AND ROLLBACK v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-04-FINAL-CONTENT-COMPLETION  
**Date:** 2026-07-26  
**Raw backup Git state:** **NOT COMMITTED**

---

## 1. Full Beget backup

| Field | Value |
|-------|-------|
| Status | **OPERATOR CONFIRMED** for this immediate glossary work sequence |
| Agent action | No new full-backup gate invented; no Beget panel login |

## 2. Scoped Batch 04 prewrite snapshot (authenticated)

| Field | Value |
|-------|-------|
| Method | Authenticated WP REST (`glossary` drafts) + admin ACF/Yoast field capture |
| Path | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch04-final-content-20260726-173213\` |
| Target count (first capture) | **54** |
| Bytes (first capture) | **53976** |
| SHA-256 (first dedicated snapshot) | `8420c36602805a27029716a8c77d1e57b56b15f0f41cb99be6c0394aae2dba54` |
| Secrets in snapshot | **no** |
| Git | raw snapshot **NOT COMMITTED** |

## 3. Overwrite incident (bounded)

A later COMPLEX deepen re-apply reused the same `--backup-dir` with `--only-source` for **3** posts and **overwrote** `scoped-glossary-prewrite-snapshot.json` in that directory (ending as a 3-target file).

**Mitigation:**

1. Record the original first SHA-256 above as the authoritative first capture hash.
2. Create a **reconstructed full-54 empty-draft baseline** (Batch 04 targets were empty before apply):

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch04-prewrite-reconstructed-20260726-175433\` |
| Target count | **54** |
| Bytes | **27165** |
| SHA-256 | `52eca9587efc44c409aecddf1e565f76f09a46048db9df57ca243fc292c0f0ef` |
| Method | Reconstructed from Batch 04 CSV post IDs + source titles + empty content/excerpt expectation |
| Pointer | `data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-04-PREWRITE-SNAPSHOT-POINTER-v1.json` |

3. COMPLEX re-apply before-state also stored separately:

`X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch04-complex-reapply-20260726\`

## 4. Rollback procedure

1. Confirm branch/workspace/volume preflight.
2. Load reconstructed or original allowlisted `post_id` list (54).
3. For each ID: verify `post_type=glossary` and `post_status=draft`.
4. Restore `post_title` to source title, clear/restore `post_content`/`post_excerpt` to empty baseline (or first-capture bodies if a full JSON copy is recovered), restore ACF/Yoast from capture when available.
5. Do **not** publish.
6. Re-validate anonymous `/glossary/` = 404 and published count = 0.

## 5. Operator note

Prefer dedicated backup directories per apply wave. Do not reuse the same Storage snapshot directory for a later partial `--only-source` apply.

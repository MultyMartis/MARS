# ISEO-SU GLOSSARY BATCH 03 DB BACKUP AND ROLLBACK v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-03  
**Date:** 2026-07-26  

---

## 1. Full Beget backup

**OPERATOR CONFIRMED** before this task. No additional full-backup gate was required by charter.

## 2. Scoped backup timestamp

**2026-07-26 16:53:59** (local) — authoritative prewrite snapshot for Batch 03 targets.

Dedicated snapshot mode completed before production apply. Apply wave reused the same Storage directory; on-disk snapshot remains pre-mutation capture of the 55 targets.

## 3. Backup method

Authenticated WordPress REST (`wp/v2/glossary`, `context=edit`) plus admin edit-screen capture of ACF + Yoast fields via `tools/glossary-batch-content-updater.py --batch 03 --mode snapshot`.

No full MySQL dump. No credentials printed or committed.

## 4. Exact scope

| Scope | Count |
|-------|------:|
| Batch 03 targets | **55** |

Captured per target:

- REST fields: id, title, slug, status, content, excerpt, modified timestamps, link;
- ACF: synonyms, keywords, LSI, source notes;
- Yoast: SEO title, meta description.

## 5. Storage path

```
X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch03-20260726-165359\
  scoped-glossary-prewrite-snapshot.json
  SHA256.txt
```

Pointer (sanitized metadata only):

`data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-03-PREWRITE-SNAPSHOT-POINTER-v1.json`

## 6. Size and SHA-256

| Field | Value |
|-------|-------|
| Bytes | **54987** |
| SHA-256 (on-disk after apply wave pointer refresh) | `3249f85fe6c674dc1341d8796dc1abfaab1314888f86829c8b3e0657fdeca2d2` |
| First dedicated snapshot SHA (pre-apply run) | `c401cb28dc32ecdf64c5ab9c28a5e277431cb574ce5bf60e6b0835ca88f5b97b` |

Both captures are pre-mutation Batch 03 target state (55 IDs). Prefer the on-disk file + `SHA256.txt` in the Storage directory as restore source.

## 7. Restoration procedure

1. Confirm volume `X:` / `AI WS` and that Storage path exists.
2. Load `scoped-glossary-prewrite-snapshot.json`.
3. For each `post_id`, authenticated REST update: title, slug, content, excerpt, `status=draft` (never publish).
4. Restore ACF/Yoast admin fields from `acf_yoast` capture.
5. Re-validate: restored IDs still `draft`; anonymous `/glossary/` still 404.

Do **not** use wildcard SQL DELETE/UPDATE. Prefer WordPress APIs.

## 8. Secrets

Snapshot contains **editorial/post content only**.  
**Does not** contain WordPress passwords, WPilot tokens, DB credentials, or browser cookies.

## 9. Git status

Raw DB/content snapshot under Storage: **NOT COMMITTED**.  
Only this evidence document + pointer JSON may be committed.

---

*ISEO-SU Glossary Batch 03 DB Backup and Rollback v1 · 2026-07-26.*

# ISEO-SU GLOSSARY BATCH 02 DB BACKUP AND ROLLBACK v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-01-REFINEMENT-AND-BATCH-02  
**Date:** 2026-07-25  

---

## 1. Backup timestamp

**2026-07-25 03:51:44** (local) — authoritative full prewrite snapshot for this task.

Additional apply-time snapshots also exist for the mutate subsets (4 Batch 01 refine IDs; 45 Batch 02 IDs). Prefer the full 75-target snapshot for rollback planning.

## 2. Backup method

Authenticated WordPress REST (`wp/v2/glossary`, `context=edit`) plus admin edit-screen capture of ACF + Yoast fields via existing Playwright operational tooling (`tools/glossary-batch-content-updater.py --mode snapshot`).

No full MySQL dump. No credentials printed or committed.

## 3. Exact scope

| Scope | Count |
|-------|------:|
| Batch 01 targets | 30 |
| Batch 02 targets | 45 |
| Total post rows captured | **75** |

Captured per target:

- `wp_posts`-equivalent fields via REST: id, title, slug, status, content, excerpt, modified timestamps, link;
- ACF: synonyms, keywords, LSI, source notes (admin field values);
- Yoast: SEO title, meta description (admin field values).

## 4. Storage path

```
X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch01-refine-batch02-20260725-035144\
  scoped-glossary-prewrite-snapshot.json
  SHA256.txt
```

Pointer (sanitized metadata only, in Git-allowed locus):

`data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-02-PREWRITE-SNAPSHOT-POINTER-v1.json`

## 5. SHA-256

`9176ca591b8a84eb9f863e6a5fa9b4a9018ac5badb37713c562f7b86f87aa441`

Size: **127966** bytes.

## 6. Restoration procedure

1. Confirm volume `X:` / `AI WS` and that Storage path exists.
2. Load `scoped-glossary-prewrite-snapshot.json`.
3. For each `post_id` in the snapshot, authenticated REST update:
   - `title`, `slug`, `content`, `excerpt`, `status=draft` (never publish).
4. Restore ACF/Yoast admin fields from `acf_yoast` capture.
5. Re-validate: all restored IDs still `draft`; anonymous `/glossary/` still 404.

Do **not** use wildcard SQL DELETE/UPDATE. Prefer WordPress APIs.

## 7. Secrets

Snapshot contains **editorial/post content only**.  
**Does not** contain WordPress passwords, WPilot tokens, DB credentials, or browser cookies.

## 8. Git status

Raw DB/content snapshot under Storage: **NOT COMMITTED**.  
Only this evidence document + pointer JSON may be committed.

---

*ISEO-SU Glossary Batch 02 DB Backup and Rollback v1 · 2026-07-25.*

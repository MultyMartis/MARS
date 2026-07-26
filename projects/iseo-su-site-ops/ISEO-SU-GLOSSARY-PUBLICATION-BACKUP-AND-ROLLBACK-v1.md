# ISEO-SU GLOSSARY PUBLICATION BACKUP AND ROLLBACK v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-PUBLICATION-READINESS-AND-CONTROLLED-LAUNCH  
**Date:** 2026-07-26  
**Raw DB backup:** **NOT COMMITTED**

---

## 1. Full Backup

| Field | Value |
|-------|-------|
| Status | Operator-authorized controlled launch on 2026-07-26 glossary sequence; same-day Batch 04 operator-confirmed Beget backup carried as rollback point for this window |
| Agent Beget panel | **not used** (HOLD) |
| Autonomous full hosting backup | **not available** without panel |

## 2. Scoped DB Snapshot

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-publication-launch-20260726-180602\` |
| Primary file | `scoped-glossary-prelaunch-snapshot.json` |
| Manifest | `BACKUP-MANIFEST.json` |
| Method | Authenticated WP REST `glossary` `context=edit` (all statuses reachable) |
| Target count | **241** |
| Bytes | **1348928** |
| SHA-256 | `82b18ac2fb48780d512ef39b40d1a918e4e9a10c290bda060ea40c495ec2981b` |
| Captured fields | id, status, slug, type, title, content, excerpt, modified timestamps, link, yoast_head_json when present, meta bag |
| Secrets | **none** |
| Git | raw snapshot **NOT COMMITTED** |

Pointer: `projects/iseo-su-site-ops/_glossary-scratch/launch/latest-backup-pointer.json` (scratch; not authority).

## 3. Pre-Launch State

- All 241 glossary posts: `draft`
- Published glossary: 0
- Public exposure: false
- Anonymous `/glossary/`: 404

## 4. Publication Rollback

LEVEL 1 — status only:

1. Load allowlist post IDs from `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv` where `launch_selected=YES` (184).
2. For each ID: verify `post_type=glossary`.
3. REST/Admin set `status=draft`.
4. Confirm published glossary count = 0.

## 5. Exposure Rollback

1. Set `ISEO_GLOSSARY_PUBLIC_EXPOSURE` to `false` in theme `inc/glossary-cpt.php` (or restore `.bak-glossary-launch-*` pre-exposure file).
2. Deploy via existing SFTP glossary deploy pattern.
3. Verify anonymous `/glossary/` returns 404.

Theme backups created on deploy waves under production theme paths `*.bak-glossary-launch-<UTC>`.

## 6. Template/Helper Rollback

Restore from remote `.bak-glossary-launch-*` for:

- `single-glossary.php`
- `inc/glossary-helpers.php`
- `inc/glossary-acf.php`
- `inc/glossary-cpt.php`
- related glossary includes if needed

Local package SoT: `projects/iseo-su-site-ops/wordpress/iseoblog-glossary/`.

## 7. Data Restore

If content/meta damaged:

1. Prefer LEVEL 1 + 5 first.
2. LEVEL 3: restore title/content/excerpt/meta from scoped snapshot JSON for exact IDs.
3. Related-terms meta can be rebuilt from batch content CSVs.

## 8. Validation After Rollback

- Anonymous `/glossary/` = 404
- Published glossary count = 0
- Sample former public singles = 404 or non-public
- `/`, `/blog/`, `/tariff-calc`, `/offers` healthy

## 9. Storage and Hashes

See §2. Storage root only under `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\`.

## 10. Stop Conditions

Stop rollback escalation at LEVEL 1/5 if they restore public closure. Use full Beget restore only if scoped rollback fails or broader production impact is proven.

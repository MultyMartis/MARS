# ISEO-SU GLOSSARY BATCH 01 ROLLBACK v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-FINAL-CORPUS-AND-BATCH-01-CONTENT  
**Date:** 2026-07-25  
**Scope:** Restore **only** the 30 Batch 01 glossary draft posts listed below.

---

## 1. Snapshot location

Sanitized pre-write snapshot (no secrets):

`data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-01-PREWRITE-SNAPSHOT-v1.json`

Operational receipt (local scratch):

`_glossary-scratch/batch01-wp/prewrite-snapshot.json`  
`_glossary-scratch/batch01-wp/receipt.json`

---

## 2. Target post IDs (Batch 01 only)

2670, 2448, 2603, 2632, 2570, 2663, 2642, 2534, 2539, 2628, 2637, 2500, 2496, 2514, 2662, 2502, 2650, 2522, 2537, 2549, 2497, 2451, 2585, 2592, 2647, 2619, 2507, 2576, 2562, 2486

Do **not** rollback other glossary drafts.

---

## 3. What to restore

For each target post ID, restore from the snapshot item with the same `post_id`:

| Field | Restore from snapshot key | Method |
|-------|---------------------------|--------|
| Title | `title` | WP REST `POST /wp/v2/glossary/{id}` with `title` + `status=draft`, or Admin edit |
| Slug | `slug` (may be empty pre-write) | REST `slug` if non-empty; if empty, clear carefully or leave current slug unless title rollback requires it |
| Content | `content_raw` | REST `content` |
| Excerpt | `excerpt_raw` | REST `excerpt` |
| Status | must remain `draft` | Never publish during rollback |
| ACF synonyms | `acf_yoast_before.glossary_synonyms` | Admin ACF field or `update_field` |
| ACF keywords | `acf_yoast_before.glossary_keywords` | Admin ACF |
| ACF LSI | `acf_yoast_before.glossary_lsi_phrases` | Admin ACF |
| ACF notes | `acf_yoast_before.glossary_source_notes` | Admin ACF |
| Yoast title | `acf_yoast_before.yoast_title` | Admin Yoast fields / meta ` _yoast_wpseo_title` |
| Yoast metadesc | `acf_yoast_before.yoast_metadesc` | Admin Yoast / meta `_yoast_wpseo_metadesc` |

---

## 4. Preferred rollback procedure

1. Confirm operator authorization for Batch 01-only rollback.
2. Confirm Beget backup still applicable if broader recovery needed.
3. Login to WP Admin with local-only credentials.
4. Open an editor page to load `wpApiSettings` (same pattern as `tools/glossary-batch01-content-updater.py`).
5. For each of the 30 IDs:
   - REST update title/content/excerpt/slug from snapshot with `status: "draft"`.
   - Admin-restore ACF + Yoast values from `acf_yoast_before`.
6. Verify:
   - each ID still `draft`;
   - anonymous `/glossary/` still 404;
   - no other post types touched.

---

## 5. Forbidden during rollback

- Publishing any glossary term
- Changing `ISEO_GLOSSARY_PUBLIC_EXPOSURE`
- Menu / sitemap changes
- CSS/JS/theme edits
- Deleting merge/exclude/deferred drafts
- Touching non-Batch-01 posts

---

## 6. Acceptance after rollback

| Check | Expected |
|-------|----------|
| Batch 01 content empty or restored-to-snapshot | matches snapshot |
| Titles restored to source workbook titles where snapshot says so | yes |
| Status | draft |
| Public glossary | still closed |

---

*ISEO-SU Glossary Batch 01 Rollback v1 · 2026-07-25.*

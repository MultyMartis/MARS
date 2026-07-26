# ISEO-SU GLOSSARY PUBLICATION LAUNCH MANIFEST v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-PUBLICATION-READINESS-AND-CONTROLLED-LAUNCH  
**Date:** 2026-07-26  
**Dataset:** `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv`

---

## 1. Launch Status

**COMPLETE — PUBLIC GLOSSARY LAUNCHED / ELIGIBLE CANONICAL CORPUS LIVE**

## 2. Starting State

| Metric | Value |
|--------|------:|
| Total source records | 241 |
| Publication-eligible | 184 |
| MERGED | 30 |
| DEFERRED | 14 |
| EXCLUDED | 13 |
| Published | 0 |
| Anonymous `/glossary/` | 404 |
| `ISEO_GLOSSARY_PUBLIC_EXPOSURE` | false |

## 3. Backup State

| Layer | Status |
|-------|--------|
| Full Beget backup | Operator-authorized launch window on continuous 2026-07-26 glossary sequence (Batch 04 same-day confirmation carried forward; Beget panel not opened by agent) |
| Scoped DB snapshot | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-publication-launch-20260726-180602\` |
| Snapshot SHA-256 | `82b18ac2fb48780d512ef39b40d1a918e4e9a10c290bda060ea40c495ec2981b` |
| Target count | 241 |
| Bytes | 1348928 |
| Raw backup Git | **NOT COMMITTED** |

Details: `ISEO-SU-GLOSSARY-PUBLICATION-BACKUP-AND-ROLLBACK-v1.md`

## 4. Eligibility Reconciliation

Authority CSV reconciled against live WP REST (`glossary` drafts).

| Check | Result |
|-------|--------|
| Eligible YES | 184 |
| Map to unique WP post | 184 |
| Pre-launch status draft | 184/184 |
| Non-placeholder body/excerpt | pass |
| Duplicate target IDs | 0 |
| Duplicate public slugs | 0 |
| MERGED/DEFERRED/EXCLUDED eligible | 0 |

## 5. Final Launch Set

**184** canonical posts (`launch_selected=YES`).

## 6. Removed From Launch

**0** hard-gate removals. Soft related-term drops only (86 unresolved names not in corpus → omitted from public related links).

## 7. Merged Alias Strategy

- 30 MERGED source records remain **draft / non-public**.
- No redirects created (no evidence of prior public/indexed MERGED URLs).
- Alias relationship retained in eligibility/`canonical_target` metadata.
- Related-term resolution maps aliases to eligible canonical titles when present.

## 8. Deferred / Excluded Strategy

- 14 DEFERRED + 13 EXCLUDED remain draft.
- Not in archive, sitemap, related links, or navigation.
- Not trashed/deleted.

## 9. Internal Linking

- Related terms stored in `glossary_related_terms` meta from batch CSVs.
- Single template renders **Связанные понятия** as links to published canonical targets only.
- Edges: input 640 → resolved eligible 554; unresolved 86 dropped; self-links 0.

## 10. SEO Readiness

- Eligible published singles: index/follow (no inherited noindex observed on samples).
- Yoast titles present on sampled pages.
- Canonical self-referential (`/glossary/{slug}`).
- Archive: index, follow.

## 11. Archive Exposure

- `ISEO_GLOSSARY_PUBLIC_EXPOSURE = true` deployed.
- Anonymous `/glossary/` → **200**.
- Public list = published only (184 unique term slugs; `feed` chrome slug ignored).

## 12. Sitemap Decision

**INCLUDE** published glossary singles in WordPress/Yoast XML sitemap surface:

- Observed: `https://i-seo.su/wp-sitemap-posts-glossary-1.xml` → **184** URLs.
- Index: `https://i-seo.su/wp-sitemap.xml` lists glossary child.
- Primary `robots.txt` Sitemap `https://i-seo.su/sitemap.xml` is a **custom/static** index without glossary children — **not modified** this launch (minimal-change).
- No custom sitemap PHP added.

## 13. Navigation Decision

**B — DO NOT ADD HEADER LINK YET**

Primary header/nav already dense (services tree). Glossary discoverable via direct URL/archive; menu add deferred to avoid visual risk.

## 14. Dry Run

Hard gates passed before apply: 241 reconciled; 184 selected; 0 blockers; 0 dup IDs/slugs; scoped backup present.

## 15. Publication Apply

- Mechanism: authenticated WP REST allowlist publish + related meta.
- Result: **184/184** `draft → publish`, 0 failures.

## 16. Public Validation

- Archive 200; singles sample 26/26 200; related heading present.
- Negatives (MERGED/DEFERRED/EXCLUDED via `?post_type=glossary&p=ID`): 0 content leaks.
- Regression `/`, `/blog/`, `/tariff-calc`, `/offers`, privacy: 200.

## 17. Rollback

Documented in backup/rollback artifact (publish→draft allowlist + exposure false + theme bak files).

## 18. Final State

| Metric | Value |
|--------|------:|
| TOTAL SOURCE RECORDS | 241 |
| PUBLICATION ELIGIBLE | 184 |
| ACTUALLY PUBLISHED | 184 |
| MERGED NON-PUBLIC | 30 |
| DEFERRED NON-PUBLIC | 14 |
| EXCLUDED NON-PUBLIC | 13 |
| PUBLIC ARCHIVE HTTP | 200 |
| SITEMAP | Yoast/wp-sitemap glossary 184; custom sitemap.xml unchanged |
| NAVIGATION | no new header item |
| ROLLBACK READY | yes |

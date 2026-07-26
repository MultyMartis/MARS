# REPORT — ISEO-SU SITE OPS GLOSSARY PUBLICATION READINESS AND CONTROLLED LAUNCH

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-PUBLICATION-READINESS-AND-CONTROLLED-LAUNCH  
**Date:** 2026-07-26  
**Final status:** **COMPLETE — PUBLIC GLOSSARY LAUNCHED / ELIGIBLE CANONICAL CORPUS LIVE**

---

## 1. Execution Summary

Controlled launch of the safe glossary corpus. Reconciled eligibility against live WordPress, published exactly **184** eligible canonical drafts, enabled `ISEO_GLOSSARY_PUBLIC_EXPOSURE`, deployed minimal related-term linking on the single template, validated public archive/singles/negatives/regression, and recorded sitemap + navigation decisions. MERGED (**30**), DEFERRED (**14**), and EXCLUDED (**13**) remain non-public drafts. No redirects for never-public aliases. No header menu item added.

| Metric | Value |
|--------|------:|
| TOTAL SOURCE RECORDS | **241** |
| PUBLICATION ELIGIBLE | **184** |
| ACTUALLY PUBLISHED | **184** |
| MERGED NON-PUBLIC | **30** |
| DEFERRED NON-PUBLIC | **14** |
| EXCLUDED NON-PUBLIC | **13** |
| PUBLIC ARCHIVE HTTP | **200** |
| SITEMAP | Yoast/wp-sitemap glossary **184**; custom `sitemap.xml` unchanged |
| NAVIGATION | **no new header item** |
| ROLLBACK READY | **yes** |

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (X:) |
| Branch | `mars/canonical-post-recovery` |
| HEAD (start) | `776d1b779660d255187ed426e7fbe41dcd53d243` |
| Staged index | empty |
| Foreign WIP | preserved (dirty monorepo; no pull/reset/clean/stash) |

## 3. Backup State

| Layer | Evidence |
|-------|----------|
| Full hosting | Operator-authorized launch on 2026-07-26 glossary sequence; Batch 04 same-day Beget confirmation carried for this window; agent did not open Beget panel |
| Scoped snapshot | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-publication-launch-20260726-180602\` |
| SHA-256 | `82b18ac2fb48780d512ef39b40d1a918e4e9a10c290bda060ea40c495ec2981b` |
| Count / bytes | 241 / 1348928 |
| Git | raw backup **NOT COMMITTED** |

## 4. Starting Corpus

Batches 01–04 populated canonical drafts (**184**). All **241** WP glossary records draft. Anonymous `/glossary/` 404. Content commit context: `9058aba4` / hash-fill `776d1b77`.

## 5. Eligibility Reconciliation

Authority: `ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.csv` vs live REST.

| Disposition | Count | Eligible | Launch |
|-------------|------:|----------|--------|
| APPROVED / APPROVED_RENAME | 184 | YES | YES |
| MERGED | 30 | NO | NO |
| DEFERRED | 14 | NO | NO |
| EXCLUDED | 13 | NO | NO |

Missing eligible IDs: 0. Duplicate targets/slugs: 0.

## 6. Readiness Hard Gates

Automated checks on all 184: title, slug, body, excerpt, no placeholder, disposition, no slug collision, HTML not raw Markdown, SEO title/meta from batch (or documented fallback), `post_type=glossary`, pre-status draft. **Blockers removed: 0.**

## 7. Final Launch Set

184 posts — see `ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv` (`launch_selected=YES`).

## 8. Removed From Launch

None (hard gates). Soft: 86 related-term names unresolved against eligible corpus → omitted from public related links.

## 9. Merged Alias Strategy

Keep MERGED drafts non-public; no speculative redirects (no prior public URL evidence). Canonical targets public. Metadata `canonical_target` preserved.

## 10. Deferred and Excluded Records

Remain draft provenance; excluded from archive, sitemap, related links, navigation. Not deleted.

## 11. Internal Linking

Added ACF/meta `glossary_related_terms` + helpers + single template **Связанные понятия** (existing classes/markup only; no new CSS/JS). Stats: 640 input edges → 554 resolved eligible; 0 self-links; 0 links to non-eligible public targets.

## 12. SEO Readiness

Published eligible singles: indexable; sampled titles/canonicals healthy; no accidental noindex on samples. Archive index/follow after exposure.

## 13. Sitemap Decision

**Include** published glossary in WP/Yoast sitemap (`wp-sitemap-posts-glossary-1.xml` = 184). Do **not** rewrite custom `robots.txt` Sitemap `sitemap.xml` in this launch. No custom sitemap code.

## 14. Navigation Decision

**Do not add** primary header link (nav already dense). Glossary live via `/glossary/`.

## 15. Scoped Backup

See §3 and `ISEO-SU-GLOSSARY-PUBLICATION-BACKUP-AND-ROLLBACK-v1.md`.

## 16. Dry Run

All hard gates passed before mutation: draft-only targets, allowlist exact, backup present, no MERGED/DEFERRED/EXCLUDED in launch set.

## 17. Publication Apply

Authenticated WP REST allowlist: related meta + `status=publish`. **184/184 OK**, 0 failures. Content bodies not rewritten.

## 18. Public Exposure Apply

Deployed theme package with `ISEO_GLOSSARY_PUBLIC_EXPOSURE=true` after publish. Remote `.bak-glossary-launch-*` created. Rewrite flush not required beyond existing CPT rewrite version (exposure is template_redirect gate).

## 19. Archive Validation

Anonymous `/glossary/` → 200; H1 «Глоссарий»; search + alphabet present; **184** unique term slugs linked; no empty `(0)` letter groups (false positives were `javascript:void(0)`); no MERGED/DEFERRED/EXCLUDED as public terms.

## 20. Single Page Validation

≥20 samples (SIMPLE/MODERATE/COMPLEX/renames + Nofollow, GEO, E-E-A-T, Core Web Vitals, Канонический URL): HTTP 200; H1; lead; content; related heading; SEO title; canonical self; no admin leakage.

## 21. Negative Tests

MERGED/DEFERRED/EXCLUDED via `?post_type=glossary&p={id}`: **404**, exposed term pages **0**. (Empty-slug draft `/glossary//` resolves to archive — not a term leak.)

## 22. Related Link Validation

Self-links 0; broken eligible targets 0; public links to non-eligible 0. Unresolved names dropped.

## 23. Sitemap Validation

| Surface | Result |
|---------|--------|
| `wp-sitemap-posts-glossary-1.xml` | 200; **184** glossary URLs; draft leakage 0 |
| `wp-sitemap.xml` | lists glossary child |
| `sitemap.xml` (robots primary) | custom index; no glossary; unchanged |

## 24. Robots and Canonical Validation

Archive robots: index, follow. Singles: no noindex on samples; canonical `/glossary/{slug}`.

## 25. Site Regression

`/`, `/blog/`, `/tariff-calc`, `/offers`, `/privacy-policy.html`, `/glossary/` → 200; no maintenance mode; calculator/offers/WPilot untouched; no shared CSS/JS changes.

## 26. Performance Sanity

Archive ~140–175KB HTML; related links use one cached published-title map per request (no per-link WP_Query). No fatal/memory issue observed.

## 27. Final Public State

Public glossary live: 184 published canonical articles; 57 non-eligible drafts; archive open; exposure true.

## 28. Rollback Readiness

LEVEL 1 publish→draft allowlist; LEVEL exposure false + bak restore; LEVEL data from scoped JSON; LEVEL full Beget if needed. Documented.

## 29. Files Created or Updated

**Created**

- `ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-MANIFEST-v1.md`
- `ISEO-SU-GLOSSARY-PUBLICATION-BACKUP-AND-ROLLBACK-v1.md`
- `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv`
- `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-PUBLICATION-READINESS-AND-CONTROLLED-LAUNCH.md`

**Updated**

- `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.csv`
- `ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.md`
- `ISEO-SU-GLOSSARY-SEO-AND-INTERNAL-LINKING-MODEL-v1.md`
- `ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md`
- `ISEO-SU-GLOSSARY-TERM-INTAKE-REGISTER-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `OPERATIONAL-INDEX.md`
- `wordpress/iseoblog-glossary/inc/glossary-cpt.php`
- `wordpress/iseoblog-glossary/inc/glossary-acf.php`
- `wordpress/iseoblog-glossary/inc/glossary-helpers.php`
- `wordpress/iseoblog-glossary/single-glossary.php`

**Production (not Git)**

- WP 184 status publish + related meta
- Theme deploy waves (exposure false then true) + remote bak files
- Storage scoped snapshot

## 30. Production Mutations

1. Scoped REST snapshot of 241 glossary posts to Storage.  
2. SFTP deploy glossary helpers/ACF/single/CPT (exposure false).  
3. REST publish + related meta for 184 allowlisted IDs.  
4. SFTP deploy CPT exposure true (+ helpers/single/acf).  

## 31. SAFE UNKNOWN

- Independent Beget panel backup object/timestamp for this exact minute: not verified by agent (panel HOLD).
- Whether custom `sitemap.xml` consumers will discover Yoast glossary URLs without a later static-index update.
- Alias search for MERGED source strings without synonym metadata: not implemented (documented limitation; e.g. «морда» empty).

## 32. Git Persistence

One scoped commit authorized after validation (no push). Subject: `feat(iseo-su): launch public glossary`.

## 33. Operator Review

Review public `/glossary/`, sample singles, Yoast glossary sitemap, confirm menu deferral acceptable, optionally add glossary to custom `sitemap.xml` later.

## 34. Stop Condition

Stop after readiness, controlled publication, exposure, related-link resolution, SEO/sitemap validation, public/negative smoke, regression, rollback evidence, and Git persistence. No further content batches; no push.

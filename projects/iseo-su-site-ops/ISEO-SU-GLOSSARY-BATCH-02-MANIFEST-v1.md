# ISEO-SU GLOSSARY BATCH 02 MANIFEST v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-01-REFINEMENT-AND-BATCH-02  
**Date:** 2026-07-25  
**Publication:** **not performed** — all targets remain `draft`

---

## 1. Batch Status

| Field | Value |
|-------|-------|
| Status | **LOADED AS DRAFTS** |
| Terms | **45** (target 42–48) |
| Applied | **45 / 45** |
| Failed | **0** |
| Batch 01 refine | **4** MINOR_EDIT applied; **26** PASS_AS_IS |
| Public exposure | still closed (`/glossary/` anonymous **404**) |
| Menu / sitemap | unchanged / still excluded |
| New CSS/JS | none |

## 2. Operator Decisions Incorporated

- Archive + single templates accepted; no redesign / no new CSS.
- Short articles stay concise; depth varies by usefulness.
- Related terms semantically useful; draft-stage plain text (no unsafe public draft links).
- Incomplete drafts must never become public; per-entry publication eligibility.
- Batch 01 bounded editorial cleanup before Batch 02 scale-up.
- No full Beget backup gate for this glossary-scoped task; scoped DB snapshot required instead.

## 3. Batch 01 Refinement

| Verdict | Count | Notes |
|---------|------:|-------|
| PASS_AS_IS | 26 | Including operator-accepted **Nofollow** |
| MINOR_EDIT | 4 | SEO; Канонический URL; E-E-A-T; GEO — remove definition echo / tighten |
| MATERIAL_EDIT | 0 | No full rewrites required |

Fact-sensitive review attention: GEO, E-E-A-T, Показатель отказов, Core Web Vitals, SEO, CTR, robots.txt, Канонический URL, Nofollow — content remained accurate; only echo/padding cleanup where needed.

## 4. Selection Logic

- Exclude Batch 01, MERGED, DEFERRED, EXCLUDED.
- Prefer HIGH/MEDIUM foundational and commercially useful terms.
- Balance categories: analytics, content/semantics, technical SEO, SEO fundamentals, advertising, UX, indexing, CMS.
- Avoid near-duplicate canonicals in one batch.
- Skipped: `ВЧ / СЧ / НЧ запросы` (same canonical as Частотность запроса); AMP (LOW); Лид (incomplete draft example / LOW); DA/DR/PageRank deferred for careful third-party framing.

## 5. Batch 02 Terms

See `data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-02-CONTENT-v1.csv` and `_glossary-scratch/batch02-selection-final.json` for the authoritative 45-row list (source → canonical → slug → category → depth).

## 6. Article Depth Distribution

| Depth | Count |
|-------|------:|
| SIMPLE | 18 |
| MODERATE | 26 |
| COMPLEX | 1 (Поведенческие факторы) |

## 7. Renames

APPROVED_RENAME targets in Batch 02 are renamed to canonical titles/slugs on apply (existing draft posts only; no duplicate create). Exact rename count recorded from dry-run/apply receipt.

## 8. Research and Verification

See `ISEO-SU-GLOSSARY-RESEARCH-REGISTER-v1.md` (Batch 02 additions). Fact-sensitive: Mobile-first indexing, Микроразметка, Поведенческие факторы, Google Ads / Яндекс Директ, LSI, HTTP-код ответа, UTM / Event tracking / GA.

## 9. WordPress Target Reconciliation

- CPT `glossary` only.
- Exact one draft match per source/canonical title.
- No published targets; no non-glossary IDs; no Batch 01 ID reuse.
- Tool: `tools/glossary-batch-content-updater.py`

## 10. Scoped DB Backup

Authoritative prewrite snapshot:

- Path: `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch01-refine-batch02-20260725-035144\`
- SHA-256: `9176ca591b8a84eb9f863e6a5fa9b4a9018ac5badb37713c562f7b86f87aa441`
- Targets: **75** (30 Batch 01 + 45 Batch 02)
- Evidence doc: `ISEO-SU-GLOSSARY-BATCH-02-DB-BACKUP-AND-ROLLBACK-v1.md`
- Raw snapshot: **NOT COMMITTED**

## 11. Dry Run

| Gate | Batch 01 refine (4) | Batch 02 (45) |
|------|---------------------|---------------|
| Matched == target | PASS | PASS |
| Draft / glossary only | PASS | PASS |
| Slug collisions | 0 | 0 |
| Target in 42–48 | n/a | PASS |

## 12. Production Apply

| Wave | Updated OK | Failed |
|------|-----------:|-------:|
| Batch 01 refine | 4 | 0 |
| Batch 02 | 45 | 0 |

Evidence: `_glossary-scratch/batch02-wp/receipt.json` + `post-apply-validation.json`.

## 13. Visual Validation

Authenticated previews of ≥10 filled terms (Batch 01 + Batch 02 mix) — see REPORT §19.

## 14. Public Boundary

Anonymous `/glossary/` remains 404; drafts not public; no menu; no sitemap exposure.

## 15. Rollback

Restore from Storage scoped snapshot via WP REST/admin field rewrite using captured title/slug/content/excerpt/ACF/Yoast values. See backup evidence doc.

## 16. Remaining Issues

- Do not proceed to Batch 03 until operator review.
- Лид and other empty drafts remain incomplete — must stay draft / non-public.
- Future public related-term hyperlinks deferred until publication eligibility.

*ISEO-SU Glossary Batch 02 Manifest v1 · 2026-07-25.*

# ISEO-SU GLOSSARY PUBLICATION ELIGIBILITY v1

**Programme:** ISEO-SU-SITE-OPS  
**Updated:** 2026-07-26 — controlled public launch  
**Dataset:** `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.csv`  
**Launch dataset:** `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-v1.csv`  
**Status:** **PUBLICATION AUTHORITY + LIVE PUBLISHED STATE**

---

## 1. Purpose

Define which of the **241** source glossary records are eligible for public publication, and record post-launch status.

## 2. Final Content Corpus / Live State

| Metric | Count |
|--------|------:|
| Total source records | **241** |
| Publication-eligible (`publication_eligible=YES`) | **184** |
| Actually published | **184** |
| MERGED (non-public) | **30** |
| DEFERRED (non-public) | **14** |
| EXCLUDED (non-public) | **13** |

Safe content corpus: **COMPLETE**. Public launch: **LIVE**.

## 3. Eligibility Rules

`publication_eligible = YES` only when:

- disposition APPROVED or APPROVED_RENAME;
- production-quality content in WordPress;
- short definition + body reviewed;
- canonical title/slug final;
- no factual blocker;
- SEO metadata acceptable;
- no placeholder copy.

MERGED / DEFERRED / EXCLUDED → `publication_eligible = NO` (remain draft).

## 4. Eligible Canonical Articles

**184** rows with `publication_eligible=YES` — all launched (`post_status=publish`).

## 5. Non-Eligible Records

**57** rows remain WordPress **draft** provenance. Not in public archive, sitemap, related links, or navigation.

## 6. Merged Aliases

MERGED sources stay non-public. No redirects for never-public draft URLs. Canonical targets are public.

## 7. Deferred / Excluded

Unchanged counts; remain draft.

## 8. WordPress State (post-launch)

| Metric | Value |
|--------|------:|
| Glossary CPT records | **241** |
| Published | **184** |
| Draft | **57** |
| Anonymous `/glossary/` | **200** |
| `ISEO_GLOSSARY_PUBLIC_EXPOSURE` | **true** |

## 9. Publication Rules (operational)

Authority remains the eligibility CSV + launch CSV. Do not publish non-eligible drafts without a new charter. Rollback: allowlist publish→draft + exposure false — see backup/rollback doc.

# REPORT — SITE-002 Catalog Onboarding Review

**Operation:** `SITE-002-PROD-CATALOG-ONBOARDING-REVIEW-01`  
**OCPilot run:** 4.253  
**Date:** 2026-07-10  
**Environment:** Production read-only review (`https://bzpm.ru/`)  
**Worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Baseline:** `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01`  
**Source monitor:** Run 4.251 — folder `2026-07-10_13-27-20`

---

## 1. Scope

Read-only onboarding review of monitor classification `ONBOARDING_REQUIRED` (5 needs) after post-1C sitemap delta. No production mutation, no monitor trigger, no import, no admin saves.

**Allowed:** Git read, storage artifacts, public HTTP, read-only DB SELECT, docs commit from temp worktree.  
**Forbidden:** All production writes (FTP, DB, admin, redirects, sitemap code).

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| HEAD | `876f6a93` (= `origin/mars/canonical-post-recovery`) |
| Staged files | **none** |
| Untracked | 2 verification `.py` tools only (not committed) |
| Main worktree `X:\AI MARS` | **not touched** |

**Verdict:** Pre-flight **PASS** — temp worktree safe for docs-only commit.

---

## 3. Source monitor artifacts

| Artifact | Value |
|----------|-------|
| Run folder | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\2026-07-10_13-27-20\` |
| Classification | `ONBOARDING_REQUIRED` |
| Baseline URLs | 1377 |
| Current URLs | 1424 |
| Added | 61 |
| Removed | 14 |
| Onboarding needs | 5 |
| Hygiene flags | 0 |
| Strict garbage hits | 0 |
| Duration | 91.4s |
| Added page types | INFORMATION 7, CATEGORY_PLP 5, PRODUCT_PDP 48, SAFE UNKNOWN 1 |

**Note:** Scheduled folder contains summary artifacts only. Full crawl + `category-onboarding-needs.json` live in deployment folder `SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02/quality/`.

---

## 4. Onboarding needs summary

Monitor `phase5_category_onboarding` flags **newly added category PLPs** not in `ONBOARDED_CATEGORY_PATHS` and/or with missing/weak/duplicate meta descriptions.

### The 5 onboarding needs (all category PLP, all HTTP 200, all indexable, 0 `БЗПМ`)

| # | URL | DB id | Issues | Meta desc |
|---|-----|-------|--------|-----------|
| 1 | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` | 88 | New path in sitemap delta vs monitor allowlist; **duplicate description** with sibling 141 | present (138 chars) |
| 2 | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/shkafy-dlya-hleba` | 363 | New branch; **missing meta description** | **MISSING** |
| 3 | `/katalog/tehnologicheskoe-oborudovanie` | 362 | New top-level branch; **missing meta description** | **MISSING** |
| 4 | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari` | 140 | New nested path in delta; meta already onboarded Run 4.211 | present (129 chars) |
| 5 | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari` | 141 | New nested path; **duplicate description** with parent 88 | present (138 chars) |

**Entity types:** 5× category PLP (not products, not information pages).  
**Parent branches:** `shkafy-i-lari` (4), root catalog (1).  
**Root cause nuance:** 3 of 5 are **path-delta false positives** — meta was onboarded under flat `/lari/*` paths (Runs 4.210/4.211) before Lari reparent; monitor `ONBOARDED_CATEGORY_PATHS` still lists flat paths, so nested URLs appear as "newly added category branch not documented."

---

## 5. URL classification

- **61 added:** 48 product PDPs (1C growth, no action), 7 information pretty URLs (Wave E sitemap normalization, no action), 5 category PLPs (onboarding scope), 1 `/sitemap` service route (no action).
- **14 removed:** 7 legacy `index.php?route=information` URLs (replaced by pretty URLs in added set), 7 flat `/lari/*` paths (replaced by nested `/shkafy-i-lari/lari/*` after reparent).
- **Removed URL HTTP:** All 14 still resolve **200** to canonical nested or pretty URLs (internal rewrite, not 404). No redirect rules required for onboarding wave.
- **Duplicates / noindex / 404:** None among onboarding needs.

---

## 6. DB / entity mapping

**Status:** Read-only SSH + mysql **ok** — 6 categories mapped.

| category_id | keyword | name | parent_id | meta_description |
|-------------|---------|------|-----------|------------------|
| 88 | lari | Лари | 358 | present |
| 140 | proizvodstvennye-lari | Производственные | 88 | present (unique) |
| 141 | skladskie-lari | Складские | 88 | present (duplicates 88) |
| 358 | shkafy-i-lari | Шкафы и лари | 79 | present |
| 362 | tehnologicheskoe-oborudovanie | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ | 0 | **MISSING** |
| 363 | shkafy-dlya-hleba | Шкафы для хлеба | 358 | **MISSING** |

Storage: `reviews/SITE-002-PROD-CATALOG-ONBOARDING-REVIEW-01/db-readonly/onboarding-entity-map.json`

---

## 7. Added URL analysis

| Group | Count | Source | Action |
|-------|-------|--------|--------|
| Product PDP (zonty, podtovarniki, lari products, tehnologicheskoe SKUs) | 48 | 1C import | **NO_ACTION_REQUIRED** |
| Information pretty URLs (about, contact, dealers, …) | 7 | Wave E SEO URLs now in sitemap | **NO_ACTION_REQUIRED** |
| Category PLP (lari nested, shkafy-dlya-hleba, tehnologicheskoe) | 5 | 1C + Lari reparent sitemap shift | **Onboarding charter** |
| `/sitemap` | 1 | Sitemap index route | **NO_ACTION_REQUIRED** |

---

## 8. Removed URL analysis

| Group | Count | Expected? | Redirect needed? |
|-------|-------|-----------|------------------|
| `index.php?route=information/information&id=*` | 7 | Yes — pretty URL migration | **No** — legacy URLs still 200; optional hygiene later |
| Flat `/katalog/nejtralnoe-oborudovanie/lari/*` | 7 | Yes — Lari reparent Run 4.235 | **No** — resolve to nested canonical (200 rewrite) |

**Risk:** P4 for information legacy routes; P3 for flat lari (monitoring only, not blocking).

---

## 9. Onboarding decision matrix

| Need | Decision | Risk | Next task |
|------|----------|------|-----------|
| 1 — nested `/lari` | `META_ONBOARDING_REQUIRED` | P2 | Differentiate meta from sibling 141 |
| 2 — `shkafy-dlya-hleba` | `META_ONBOARDING_REQUIRED` | P2 | Admin category SEO for id **363** |
| 3 — `tehnologicheskoe-oborudovanie` | `META_ONBOARDING_REQUIRED` | P2 | Admin category SEO for id **362** |
| 4 — `proizvodstvennye-lari` nested | `CATEGORY_ENTRYPOINT_REQUIRED` | P3 | Verify hub tiles + update monitor allowlist |
| 5 — `skladskie-lari` nested | `META_ONBOARDING_REQUIRED` | P2 | Unique meta for id **141** |

**Operator approval:** required before any implementation wave.

---

## 10. Site safety quick check

| URL | Status | Notes |
|-----|--------|-------|
| `/` | 200 | pass |
| `/sitemap.xml` | 200 | pass |
| `/contact` | 200 | pass |
| `/kontakty` | 404 | **accepted** |
| `/katalog` | 200 | pass |
| nested `/shkafy-i-lari/lari` | 200 | pass |
| flat `/lari` | 200 → nested final URL | internal rewrite (not 500) |
| all 5 onboarding URLs | 200 | pass |
| Public `БЗПМ` | **0** on all checked URLs | pass |

---

## 11. Implementation charter

**Primary task:** `SITE-002-PROD-CATALOG-ONBOARDING-IMPLEMENTATION-01`  
**May split into:**
- `SITE-002-PROD-CATEGORY-META-ONBOARDING-01` — ids **362**, **363**, **88**, **141** meta differentiation
- `SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01` — monitor allowlist + hub verification for nested lari paths

**Proposed mutations:** OpenCart admin category SEO saves only.  
**Optional code task:** Update `ONBOARDED_CATEGORY_PATHS` in `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` to nested Lari paths.  
**Forbidden:** FTP bulk, DB direct writes, redirects, import/monitor triggers, sitemap code changes.  
**1C overwrite risk:** Category names may refresh daily; meta fields typically persist — re-verify after next import.

Full charter: Storage `reviews/SITE-002-PROD-CATALOG-ONBOARDING-REVIEW-01/recommendations/implementation-charter.md`

---

## 12. Production mutation summary

| Class | Count |
|-------|-------|
| FTP writes | 0 |
| DB writes | 0 |
| Admin saves | 0 |
| Import runs triggered | 0 |
| Monitor runs triggered | 0 |
| Task Scheduler changes | 0 |
| Form submits | 0 |
| Mail sends | 0 |
| Production code changes | 0 |

---

## 13. Git / worktree summary

- Docs commit from `X:\AI MARS STORAGE\git-sync-e01\repo` only.
- Push target: `origin/mars/canonical-post-recovery`.
- Checkpoint **unchanged:** `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01`.

---

## 14. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\reviews\SITE-002-PROD-CATALOG-ONBOARDING-REVIEW-01\`

- `manifests/operation.json`
- `parsed/` — monitor snapshots, onboarding-needs.csv
- `classification/` — url-classification, added/removed groups, risk matrix, onboarding-needs-summary.md
- `http/` — onboarding-http-checks, site-safety-quick-check
- `db-readonly/` — onboarding-entity-map, onboarding-db-summary.md
- `recommendations/` — decision matrix, implementation-charter.md

---

## 15. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| DB mapping | **Resolved** — 6 categories mapped |
| Natural scheduled monitor post-hardening | **NOT CLAIMED** (unchanged from Run 4.252) |
| Flat `/lari` HEAD returns 200 rewrite vs prior 301 documentation | **Observation only** — no blocker for onboarding |

**Blockers:** none.

---

## 16. Final verdict

**SITE-002 CATALOG ONBOARDING REVIEW COMPLETE — IMPLEMENTATION CHARTER READY**

---

## 17. Next recommendation

1. Operator review and approve `SITE-002-PROD-CATEGORY-META-ONBOARDING-01` for category ids **362**, **363**, and meta dedup for **88**/**141**.
2. Run `SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01` to update monitor `ONBOARDED_CATEGORY_PATHS` to nested Lari paths (reduces false-positive onboarding counts).
3. After implementation, manual monitor re-run to confirm `onboarding_needs_count` drops toward 0.
4. Checkpoint update only after implementation verification — not in this review task.

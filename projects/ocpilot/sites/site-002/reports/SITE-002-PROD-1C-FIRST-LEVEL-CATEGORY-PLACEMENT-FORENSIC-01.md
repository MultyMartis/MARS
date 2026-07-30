# REPORT — SITE-002 1C First-Level Category Placement Forensic 01

**Operation:** `SITE-002-PROD-1C-FIRST-LEVEL-CATEGORY-PLACEMENT-FORENSIC-01`  
**OCPilot run:** **4.319**  
**Date:** 2026-07-30 (operator-local context `2026-07-30T15:32+07:00`)  
**Environment:** PRODUCTION — https://bzpm.ru/ (read-only forensic)  
**Verdict:** **SITE-002 1C FIRST-LEVEL CATEGORY PLACEMENT FORENSIC ATTENTION — TARGETS PARTIAL**

---

## 1. Scope

1. Check whether the **2026-07-30** natural 1C morning import ran after the expected window.
2. Locate operator targets `Холодильное`, `Посуда и инвентарь`, `Упаковочное` in 1C XML, DB, public site, sitemap.
3. Check product placement vs Алексей’s “one product per first-level section” report.
4. Confirm current placement of `Посуда и инвентарь`.
5. Produce a **future apply plan only** — no category moves, no DB/FTP/UI/importer/baseline changes.

---

## 2. Operator request

- Morning import check after schedule.
- Map three intended first-level test categories.
- Understand why `Посуда и инвентарь` sits under Tech; plan first-level representation safely later (not now).

---

## 3. Client Ops boundary

Untouched: Client Ops Telegram Reports, reporting bridge, Telegram bot, n8n, Hub Gateway. SITE-002 monitor artifacts read only as evidence.

---

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `AI WS` (X:) | PASS |
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Authority HEAD at task start | `812d15154d033698295b7c80d5bd4355d0ea1b64` (Run 4.318) |
| `origin/mars/canonical-post-recovery` | ahead with unrelated iseo-sales-manager-bot commits; **812d1515** is ancestor |
| Foreign WIP in authority | 3 untracked `.py` tools — **out of scope** |
| Dirty main | read-only inspect only; Client Ops WIP present — **not mutated** |

Artifacts: `preflight/authority-git.txt`, `preflight/dirty-main-readonly.txt`.

---

## 5. Reports read / current state

| Prior | Carried forward |
|-------|-----------------|
| Baseline | **1879** / `…-MONITOR-BASELINE-1879-08` |
| Run 4.316–4.317 | ALL-15 + empty-copy/images **accepted** (4.318) |
| Run 4.318 | Latest import then **2026-07-29** SUCCESS; today’s import not yet due |

Now after expected window: check **2026-07-30** import + target categories.

---

## 6. Latest 1C import healthcheck

**Classification:** `LATEST_1C_IMPORT_20260730_SUCCESS_CONFIRMED`

| Field | Value |
|-------|-------|
| Filename | `mars_1c_import_2026-07-30_080011.txt` |
| Run ID | `mars-20260730-080002-810087c7` |
| Status | **SUCCESS** |
| Started | 2026-07-30T08:00:02+03:00 |
| Finished | 2026-07-30T08:00:11+03:00 |
| Duration | catalog **5.08s** PASS; offers **3.87s** PASS |
| Import run by this task | **0** |

---

## 7. XML group tree search

Source: `/public_html/1c_incoming/webdata/import0_1.xml` (~11.2 MB).  
Groups parsed: **108**. Products parsed: **1639**.  
Top-level groups **only**:

1. `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ`
2. `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ`

| Target | Exact group |
|--------|-------------|
| Холодильное / Холодильное оборудование | **XML_ABSENT** |
| Посуда и инвентарь | **XML_ABSENT** |
| Упаковочное / Упаковочное оборудование | **XML_ABSENT** |

Related fuzzy leaves (Neutral dishware/inventory names) exist but are **not** the operator first-level targets.

---

## 8. DB read-only category search

| Target | Result |
|--------|--------|
| Холодильное | **95** `Холодильное оборудование`, `parent_id=0`, SEO `holodilnoe-oborudovanie`, children **148/149/150** empty, products **0**, map **NONE** |
| Посуда и инвентарь | **364**, parent **362** Tech, SEO `posuda-i-inventar`, children **0**, products **6 all status=0**, map **NONE** |
| Упаковочное | **DB_ABSENT** |

Also nearby (not exact targets): root **93** `Инвентарь`; Neutral **360** `Кондитерский инвентарь`.  
Map table still **7** active Tech rows only (362/373/375/376/378/379/380).

---

## 9. Product placement check

### Посуда 364

Products **4397–4402** (baking sheet + pizza screens):

- linked to 364;
- all **disabled** (`status=0`);
- last modified **2026-07-27** (not newly enabled by today’s import);
- public PDPs **404**;
- not in sitemap.

### Холодильное 95 / Упаковочное

No products.

### Алексей claim

**Not confirmed** as one enabled product per first-level section after today’s import.

Today’s `date_modified` sample shows normal Neutral catalog refresh — not new first-level branches.

---

## 10. Public site check

| URL / page | Result |
|------------|--------|
| Home / `/katalog/` | HTTP 200 |
| `/holodilnoe-oborudovanie` (95) | 200; empty copy; 0 product cards |
| `/posuda-i-inventar` (364) | 200; empty copy; 0 product cards |
| Posuda on home | Visible as **Tech child tile** (`…/tehnologicheskoe-oborudovanie/posuda-i-inventar`) |
| ALL-15 Neutral block | Does **not** include these three as Neutral children of 79 |
| Mega menu | `Холодильное…` / `Упаковочное…` appear as **`href="#"` stubs** |
| Posuda PDPs | 404 |

---

## 11. Sitemap check

**Classification:** `SITEMAP_MATCHES_BASELINE_1879`

| Metric | Value |
|--------|------:|
| HTTP | 200 |
| URL count | **1879** |
| Delta vs baseline (count) | **0** |
| Category 95 / 364 in sitemap | yes |
| Posuda product URLs | no |

Monitor identity swap (1 add / 1 remove stellazh URL) keeps count at 1879 — baseline refresh **not** required for count.

---

## 12. Monitor state

**Classification:** `MONITOR_IMPORT_DELTA_PENDING_REVIEW`

| Field | Value |
|-------|-------|
| Latest run | `2026-07-30_12-30-02` |
| Artifact class | `HYGIENE_REVIEW_REQUIRED` |
| Baseline → current | 1879 → 1879 |
| Added / removed | 1 / 1 |
| Onboarding needs | **0** |
| Added URL | stellazh STTS-S-6… **19** plates variant |
| Removed URL | stellazh STTS-S-6… **21** plates variant |

---

## 13. Placement analysis

| Target | Status |
|--------|--------|
| Холодильное | `FOUND_IN_DB_AND_SITE` (legacy empty root **95**); XML absent |
| Посуда и инвентарь | `FOUND_IN_DB_AND_SITE` (**364** under Tech **362**); XML exact absent |
| Упаковочное | `NOT_FOUND` (mega stub only) |

Overall placement: `TARGET_CATEGORIES_PARTIAL`.

---

## 14. Future apply plan

**Not executed.**

| Option | Recommendation |
|--------|----------------|
| A. Reparent Посуда **364** | Draft ready — needs operator parent choice (`0` vs `79` vs other) + product enable decision |
| B. Холодильное | Do not create duplicate; **95** already root empty; wait for 1C group or UI-only charter |
| C. Упаковочное | Blocked until 1C group exists |
| D. Home first-level expansion | Separate UX charter after real categories chosen |

---

## 15. Docs update

Updated authority docs for Run **4.319** (import SUCCESS; targets partial; next = operator scope decision).

---

## 16. Decision

| Axis | Classification |
|------|----------------|
| Import | `LATEST_1C_IMPORT_20260730_SUCCESS_CONFIRMED` |
| Placement | `TARGET_CATEGORIES_PARTIAL` |
| Sitemap | `SITEMAP_MATCHES_BASELINE_1879` |
| Monitor | `MONITOR_IMPORT_DELTA_PENDING_REVIEW` |
| Next | `NEEDS_OPERATOR_SCOPE_DECISION` |

---

## 17. Regression / mutation summary

All forbidden mutations **0**. Allowed: docs/report + Storage forensic artifacts.

---

## 18. Production mutation summary

| Item | Count |
|------|------:|
| production DB writes | 0 |
| production FTP writes | 0 |
| source/code changes | 0 |
| template changes | 0 |
| image changes | 0 |
| cache clear | 0 |
| OCMOD refresh | 0 |
| import runs | 0 |
| scheduler changes | 0 |
| monitor baseline changes | 0 |
| category/product changes | 0 |
| redirect changes | 0 |
| `.htaccess` changes | 0 |
| importer/source changes | 0 |
| mapping changes | 0 |
| Client Ops changes | 0 |
| n8n changes | 0 |
| Telegram changes | 0 |
| dirty main changes | 0 |
| docs/report changes | listed in §19 |

---

## 19. Git/worktree summary

Authority docs/report commit + fast-forward push to `origin/mars/canonical-post-recovery` (from origin tip; foreign WIP excluded). Dirty main not mutated.

---

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-FIRST-LEVEL-CATEGORY-PLACEMENT-FORENSIC-01\`

Subfolders: preflight, reports-read, latest-1c-import, xml-group-tree, db-readonly, product-placement, sitemap, public-http, monitor-state, placement-analysis, future-apply-plan, docs-update, decision, regression, reports, manifests, logs.

---

## 21. SAFE UNKNOWN / blockers

- Whether Алексей added products **only in 1C UI** under groups not yet present in CommerceML export: **SAFE UNKNOWN** without 1C operator confirmation.
- Mega-menu stub labels vs future real categories: presentation-only today.
- Exact intended parent for Посуда first-level move: **operator decision required**.

---

## 22. Final verdict

**SITE-002 1C FIRST-LEVEL CATEGORY PLACEMENT FORENSIC ATTENTION — TARGETS PARTIAL**

---

## 23. Next recommendation

1. **Operator scope decision** for Посуда **364**: keep under Tech vs reparent to root/`79`; enable vs replace disabled products.
2. Ask Алексей/1C to confirm whether `Холодильное` / `Упаковочное` / `Посуда и инвентарь` exist as **CommerceML groups** (they are absent from latest XML).
3. Optional light hygiene review of stellazh URL rename (onboarding **0**; count still **1879**).
4. **Do not** create Упаковочное or duplicate Холодильное in DB without 1C GUID/path.
5. No baseline refresh required for count.

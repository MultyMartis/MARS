# REPORT — SITE-002-PROD-M9-POLKI-PROFILE-331-01

**Final verdict:** `SITE-002 M9 POLKI PROFILE 331 COMPLETE — OPERATOR VISUAL CHECK REQUIRED`

**Date:** 2026-09-06 / 2026-09-07  
**Site:** SITE-002 / https://bzpm.ru/  
**Target:** category `[331]` — Полки настенные и настольные (operator short name: Полки)

---

## 1. Scope

Bounded M9 filter profile for `[331] Полки`: replace generic noisy attribute fallback with curated PRIMARY / SECONDARY / HIDDEN; deploy exact M9 files only; clear attribute cache; public smoke; capture screenshots for operator → Web-GPT.

## 2. Operator decision

Approved after PASS on `[86] Стеллажи` and `[301] Столы` refresh. Next wave: `[331]` + visual evidence screenshots.

## 3. Production safety boundary

| Gate | Value |
|------|--------|
| DB writes | **0** (SELECT only) |
| Product/category/SEO/import/baseline/PDP | **0** |
| Deploy | Exact M9 only: `331_polki.php` (new) + `filter_profile_resolver.php` (additive 331) |
| `global_hidden.php` | **unchanged** |
| Profiles `[86]` / `[301]` content | **unchanged** |
| Hub `[79]` | **not profiled** |

## 4. Docs / architecture read

- `BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md` (profiles authoritative for registered roots; tiers; inheritance)
- SITE-002 technical knowledge map / M9 phase + STABLE-M9 / M9.8.9 patterns
- Recent waves: STELLAZHI-86, STOLY-301-REFRESH, CATALOG-FILTERS decision plan
- Live vs repo resolver: line-ending drift only; roots/map aligned before additive 331 — not unsafe

## 5. `[331]` before state

| Item | Value |
|------|--------|
| category_id | 331 |
| name | Полки настенные и настольные |
| parent | 79 (hub) |
| status | enabled |
| SEO | `polki-nastennye-i-nastolnye` |
| Public PLP | https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye |
| Products (enabled under path) | ~160 (DB) |
| M9 profile before | **MISSING** → generic fallback |
| Public before | 200; title OK; ~27 checkboxes; noisy `Стандарт` present |

## 6. Attribute analysis

Built from production attribute frequency for `[331]` (see Storage `attribute-analysis/`).

Buyer-useful axes present: конструкция полки (51), материал полки (112), конструкция (21), нагрузка (122). Niche/weak: двери (123), ножки (26), кол-во полок (114), усиление (115). Hide: стандарт (42), доп. сведения (43), packaging 44/45/46/56.

**No separate buyer product L/W/H attribute IDs** in DB inventory (only packaging dims). PLP may still show Длина/Ширина/Высота as UX/facet layer — see SAFE UNKNOWN.

## 7. Profile decision

**File:** `system/library/zpm/filter_profiles/331_polki.php`

| Tier | Attribute IDs |
|------|----------------|
| PRIMARY | 51, 112, 21, 122 |
| SECONDARY | 123, 26, 114, 115 |
| HIDDEN | 42, 43, 44, 45, 46, 56 |

Resolver: register `331` in `$registered_branch_roots` + `$profile_file_map`.  
Repo mirror: `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/`

## 8. Backup / rollback

- Live-before resolver backed up under Storage `file-backups/live-before/`
- Rollback: restore resolver backup + **delete** production `331_polki.php` + clear `cache.category.attributes*`
- Plan: `rollback/rollback-plan.md`

## 9. Deploy

| File | Action | SHA256 (payload) |
|------|--------|------------------|
| `.../filter_profiles/331_polki.php` | NEW | `ab301a5cc61baf69b20a223091e617dd5c8a4f7748f8982acf74bee4d64a8b04` |
| `.../filter_profile_resolver.php` | UPDATE (additive 331) | `8e28a86a8bbb9ef809bfe6b4ea165c64b045e6a854228f397d5a18f46ad0e0f4` |

Verify match live: True; `has331=True`.

## 10. Cache

Narrow clear: attribute category cache files (`cache.category.attributes*`) — 13 files deleted. See `cache/cache-action-summary.md`.

## 11. Public after

| Check | Result |
|-------|--------|
| PLP 200 | Yes |
| Title `Поиск по параметрам` | Yes |
| Checkboxes | 26 (was ~27) |
| PRIMARY hit | Yes |
| SECONDARY under «Дополнительные параметры» | Yes |
| Noisy `Стандарт` | **gone** |
| Public `БЗПМ` / PHP warnings | No |
| `[86]` / `[301]` / `80` / katalog / upakovochnoe / posuda | 200 |
| `/zapchasti` | 404 (expected) |

## 12. Screenshots

Folder:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-POLKI-PROFILE-331-01\screenshots\`

| File | Status |
|------|--------|
| `01-polki-plp-full.png` | OK |
| `02-polki-filter-sidebar.png` | OK (re-captured; first attempt blank) |
| `03-polki-product-pdp.png` | OK |
| `04-regression-stellazhi.png` | OK |

## 13. Regression

- DB / catalog / SEO / import / baseline / PDP mutations: **0**
- Non-target profile content: **0**
- Resolver additive registration only
- Rollback: **available**

## 14. OPERATOR CHECK — СКРИНШОТЫ ГОТОВЫ / ПРОВЕРИТЬ ФИЛЬТР ПОЛОК СЕЙЧАС

### Screenshots to send to Web-GPT

Path:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-POLKI-PROFILE-331-01\screenshots\`

Files:

1. `01-polki-plp-full.png`
2. `02-polki-filter-sidebar.png`
3. `03-polki-product-pdp.png`
4. `04-regression-stellazhi.png`

### Open manually

- https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye
- Sample PDP: https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polka-nastennaya-pn-p-9-3-900h300h220
- Regression: https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi · https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly

### Visual checklist

- Title remains `Поиск по параметрам`
- PRIMARY: Конструкция полки · Материал полки · Конструкция · Макс. нагрузка
- SECONDARY under `Дополнительные параметры`
- `Стандарт` / packaging noise not shown as attribute groups
- Safe test: one PRIMARY checkbox → Показать товары → reset/reload
- Confirm `[86]` / `[301]` still OK

## 15. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-POLKI-PROFILE-331-01\`

Includes: `preflight/`, `docs-read/`, `db-readonly/`, `attribute-analysis/`, `profile-before/`, `profile-plan/`, `file-backups/`, `rollback/`, `public-before/`, `deploy/`, `cache/`, `public-after/`, `screenshots/`, `operator-check/`, `regression/`, `reports/` (if mirrored), `logs/`, `manifests/operation.json`.

## 16. Git status

- Branch: `mars/canonical-post-recovery`
- HEAD (session): `626439926297b91b…` (verify locally if needed)
- Allowlisted uncommitted:
  - `M` `.../filter_profile_resolver.php`
  - `??` `.../filter_profiles/331_polki.php`
  - `??` this report
- **Phase 14 commit: SKIPPED** — large foreign WIP (~1300+ status lines) and many unpushed commits vs origin; selective commit deferred to operator. Do **not** `git add .`.

## 17. SAFE UNKNOWN / blockers

1. PLP still shows **Длина / Ширина / Высота** facet groups (plus price/availability UX). Not mapped to packaging attr IDs 44/45/46 in M9 HIDDEN; likely separate UX/facet layer. Operator: accept or charter follow-up.
2. Listing count cue on PLP (~168) vs DB enabled path count (~160) — minor discrepancy; not blocking profile.
3. Shorter URL `/katalog/nejtralnoe-oborudovanie/polki` also exists; **canonical SEO URL** used above.
4. First sidebar screenshot blank → re-captured; not a deploy failure.

**No deploy blockers** after preflight.

## 18. Final verdict

`SITE-002 M9 POLKI PROFILE 331 COMPLETE — OPERATOR VISUAL CHECK REQUIRED`

## 19. Next recommendation

1. Operator opens screenshots + PLP → PASS/FAIL to Web-GPT.
2. If PASS: optional selective git commit of report + `331_polki.php` + resolver only (`ocpilot: add M9 shelves filter profile`).
3. If L/W/H facets are unwanted: separate charter (do not mass-edit `global_hidden` / PDP in this wave).
4. Next M9 candidate only after operator PASS on 331.

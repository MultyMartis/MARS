# REPORT — SITE-002-PROD-M9-HLEBOPEKARNOE-PROFILE-186-01

**Final verdict:** `SITE-002 M9 HLEBOPEKARNOE PROFILE 186 COMPLETE — VISUAL QA DEFERRED`

**Date:** 2026-09-06 / 2026-09-07  
**Site:** SITE-002 / https://bzpm.ru/  
**Target:** category `[186]` — Хлебопекарное оборудование  
**Operation:** `SITE-002-PROD-M9-HLEBOPEKARNOE-PROFILE-186-01`

---

## 1. Scope

Bounded M9 filter profile for `[186] Хлебопекарное оборудование`: replace noisy generic attribute fallback on bakery product PLP(s) with curated PRIMARY / SECONDARY / HIDDEN.

This wave:

- SQL SELECT only
- create/deploy `186_hlebopekarnoe.php`
- additive resolver registration of `186` only
- narrow OpenCart attribute-cache clear
- HTTP/HTML public smoke + regression
- **no screenshots** (operator policy for this wave)

Not in scope: DB writes, product/category/SEO, import, baseline, PDP hero specs, `SUPER_ATTS`, hub `[79]`, `[381]`, `[364]`, `[368]`, mass `global_hidden.php`, templates/CSS.

---

## 2. Operator decision

Operator approved continuing M9 filter-profile work after:

1. `[86] Стеллажи` — deployed, visual PASS, click/reset OK
2. `[301] Столы` — refreshed, visual PASS, `Тип опоры` PRIMARY → SECONDARY
3. `[331] Полки` — deployed, visual PASS from screenshots, `[86]` regression PASS

This wave policy:

- do **not** capture screenshots after every small wave
- use HTTP/HTML technical smoke inside Cursor
- defer screenshots / manual visual review to a later combined VISUAL QA pass

Next target was `[186] Хлебопекарное оборудование`.

---

## 3. Production safety boundary

| Gate | Value |
|------|--------|
| Environment | `CONTROLLED_PRODUCTION_FILTER_PROFILE_UPDATE` |
| DB writes | **0** (SELECT only) |
| Product/category/SEO/import/baseline/PDP | **0** |
| FTP write | Exact M9 profile/resolver files only |
| `global_hidden.php` | **unchanged / not uploaded** |
| Profiles `[86]` / `[301]` / `[331]` / `80` content | **unchanged** |
| Hub `[79]` | **not profiled** |
| `[368] Хлебопекарное` (nested under disabled tech tree) | **not targeted** |
| Screenshots | **not captured** (intentionally deferred) |
| Cleanup/delete | **0** |

---

## 4. Docs / architecture read

| Doc | Role |
|-----|------|
| `BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md` | Profiles authoritative for registered roots; tiers; INH-01…INH-07; do not profile hub `[79]` |
| `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Launch Mode visible roots include `[186]` |
| `SITE-002-CATALOG-FILTERS-AND-PDP-SPECS-DECISION-PLAN-02.md` | `[186]` was MISSING; P4 first non-neutral after 86/301/331 |
| `SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01.md` | Prior new-profile deploy pattern |
| `SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01.md` | PRIMARY/SECONDARY refresh pattern |
| `SITE-002-PROD-M9-POLKI-PROFILE-331-01.md` | Most recent additive resolver + new profile file |

Architecture confirmed:

- native `oc_filter*` is **not** the live sidebar
- layers: M9 profiles → generic fallback → `global_hidden.php` → M9.8.9 UX
- production path: `/public_html/system/library/zpm/`
- live vs repo resolver before this wave: same registered roots `80, 86, 207, 301, 322, 326, 331`; SHA differed by line endings / extra blank lines — **not an unsafe logic mismatch**
- production payload for this wave was built from **live CRLF resolver bytes**, then additive `186` insert — the blank-line repo resolver was **not** uploaded

CSV: Storage `docs-read/docs-read.csv`.

---

## 5. `[186]` before state

| Item | Value |
|------|--------|
| category_id | 186 |
| name | Хлебопекарное оборудование |
| parent_id | **0** (first-level catalog root, not under hub `[79]`) |
| status | enabled (`1`) |
| SEO | `hlebopekarnoe-oborudovanie` |
| Public hub | https://bzpm.ru/hlebopekarnoe-oborudovanie |
| Direct enabled products | **0** (hub) |
| Descendant enabled products | **12** |
| M9 profile before | **MISSING** → generic attribute fallback |
| Live listing before | no `186_hlebopekarnoe.php` |

Populated children:

| ID | Name | SEO | Enabled products | Public PLP |
|----|------|-----|------------------|------------|
| 188 | Миксеры планетарные | `miksery-planetarnye` | 5 | https://bzpm.ru/hlebopekarnoe-oborudovanie/miksery-planetarnye |
| 189 | Тестомесы | `testomesy` | 7 | https://bzpm.ru/hlebopekarnoe-oborudovanie/testomesy |

Other children under `[186]` had **0** enabled products (empty ovens/proofers/etc.).

Public before (HTTP):

| URL | Status | Sidebar title | Checkboxes | Notes |
|-----|--------|---------------|------------|-------|
| Hub `[186]` | 200 | no | 4 (non-attribute chrome) | 0 product cards; no `Поиск по параметрам` |
| Mixers `[188]` | 200 | `Поиск по параметрам` | 22 | generic fallback |
| Dough `[189]` | 200 | `Поиск по параметрам` | 35 | generic fallback; `Материал изготовления` visible |
| No public `БЗПМ` / PHP warnings | — | — | — | PASS |

Do **not** confuse with `[368] Хлебопекарное` under `/tehnologicheskoe-oborudovanie/hlebopekarnoe`.

---

## 6. Root vs child targeting decision

**Attach at root `[186]`.** File: `186_hlebopekarnoe.php`. Inheritance: **INH-01** to descendants `[188]` and `[189]`.

Why root, not child-only:

- `[186]` is a Launch Mode first-level catalog root (`parent_id=0`)
- products live only under two children that **share** buyer axes (volume / power / voltage on all 12 SKUs)
- child-specific attrs remain valid as SECONDARY on the shared profile (appear only where data exists)
- child-only profiles would duplicate the shared set and leave the root unregistered
- empty sibling children do not create PLP noise until SKUs appear

Root hub itself has **no product sidebar**. Profile is dormant there and active on leaf PLPs.

Evidence: Storage `preflight/category-186-targeting-decision.md`.

---

## 7. Attribute analysis

Built from production SELECT inventory (14 attribute IDs, 12 enabled descendant products). Full tables: Storage `attribute-analysis/`.

Buyer-useful, verified:

| ID | Name | Coverage | Distinct | Notes |
|----|------|----------|----------|-------|
| 127 | Объем | 12/12 | 8 | Bowl/deza volume |
| 135 | Мощность, кВт | 12/12 | 8 | Electrical size |
| 134 | Напряжение | 12/12 | 2 | 220В (10) / 380В (2) |
| 130 | Количество скоростей | 9/12 | 3 | 1/2/3 |
| 129 | Загрузка сухого продукта | 7/12 | 7 | High cardinality, buyer-meaningful |
| 128 | Загрузка теста | 3/12 | 3 | Dough-mixer only |
| 132 | Скорость об/мин | 7/12 | 3 | Dough-mixer rpm |
| 137 | Реверс | 3/12 | 1 | Only `есть` on 3 dough mixers |

Noise / hide:

| ID | Name | Why |
|----|------|-----|
| 126 | Материал изготовления | 3/12, single value `нержавеющая сталь` |
| 43 | Дополнительные сведения | SERVICE / free-text |
| 44/45/46/56 | Packaging dims / volume | packaging (also in `global_hidden.php`) |

Absent from this SKU set (do not invent): уровни / противни / камеры / температурный режим / масса as a buyer attr.

Sparse (N=12) but **consistent**, not heterogeneous junk. Conservative PRIMARY is justified.

---

## 8. Profile decision

**File:** `system/library/zpm/filter_profiles/186_hlebopekarnoe.php`  
**Repo mirror:** `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/filter_profiles/186_hlebopekarnoe.php`

| Tier | Attribute IDs |
|------|----------------|
| PRIMARY | 127 Объем, 135 Мощность кВт, 134 Напряжение |
| SECONDARY | 130 Количество скоростей, 129 Загрузка сухого продукта, 128 Загрузка теста, 132 Скорость об/мин, 137 Реверс |
| HIDDEN | 126 Материал изготовления, 43, 44, 45, 46, 56 |
| DO_NOT_USE | none beyond HIDDEN |
| UNKNOWN_REVIEW | PLP L/W/H sliders (`len_from` / `w_from` / `h_from`) — separate UX layer, not changed |

Resolver: **yes** — register `186` in `$registered_branch_roots` and `$profile_file_map`.  
`global_hidden.php`: **no change**.

Expected UX: less noisy than generic fallback (drops `Материал изготовления`; demotes niche attrs under «Дополнительные параметры»). Title remains `Поиск по параметрам`. Cards 5 / 7 unchanged.

---

## 9. Backup / rollback

- Live-before resolver SHA256: `8e28a86a8bbb9ef809bfe6b4ea165c64b045e6a854228f397d5a18f46ad0e0f4`
- Backup: Storage `file-backups/live-before/`
- Rollback available: **YES**

Rollback steps (no DB writes):

1. restore backed-up `filter_profile_resolver.php`
2. **delete** production `filter_profiles/186_hlebopekarnoe.php`
3. clear `cache.category.attributes*`
4. HTTP smoke mixers / dough mixers + `[86]` / `[301]` / `[331]` / `80`

Plan: Storage `rollback/rollback-plan.md`.

---

## 10. Deploy

Time: `2026-09-06T21:35:22+00:00` UTC

| File | Action | SHA256 (payload / live verify) |
|------|--------|--------------------------------|
| `/public_html/system/library/zpm/filter_profiles/186_hlebopekarnoe.php` | NEW | `e4863b92dfb80ca90e8c964c009afe9619bc034a34ac94ca82667618a8249958` |
| `/public_html/system/library/zpm/filter_profile_resolver.php` | UPDATE (additive 186 on live CRLF) | `0d9941918e0092e3489b0567936e8b81fd805bdc4bc062b54158672d7d6d8fd9` |

Verify: `had_186_before=False`, `verify_profile_match=True`, `verify_resolver_match=True`, `has186=True`.

Not uploaded: `global_hidden.php`, other profiles, templates/CSS/PDP, DB.

---

## 11. Cache

Narrow clear only: `cache.category.attributes*` under `/home/a/assum/bzpm.ru/storage/cache`.

- matched_before: **11**
- deleted: **11**
- remaining_after: none
- no broad `rm -rf cache/*`

Storage: `cache/cache-action-summary.md`.

---

## 12. Public after

Time: `2026-09-06T21:35:46+00:00` UTC. HTTP GET only. No cart/order mutation.

| Surface | Status | Cards | Title | PRIMARY | `Материал изготовления` | Checkboxes |
|---------|--------|-------|-------|---------|-------------------------|------------|
| Hub `[186]` | 200 | 0 | no sidebar (expected) | n/a | n/a | 4 (chrome) |
| Mixers `[188]` | 200 | **5** | `Поиск по параметрам` | Объем / Мощность / Напряжение | **absent** | 22 |
| Dough `[189]` | 200 | **7** | `Поиск по параметрам` | Объем / Мощность / Напряжение | **absent** (was present before) | **34** (was 35) |

SECONDARY under «Дополнительные параметры»: speeds, dry load; dough leaf also dough load / rpm / reverse.  
L/W/H sliders still present (separate UX layer).  
No public `БЗПМ`. No PHP warnings.

Safe filter GET `?attr[obem][]=10`: HTTP 200, HTML SHA changed vs unfiltered, listing still 5 cards. Volume `10` is **1** mixer SKU in DB — GET param alone does not reduce listing without JS/AJAX (same pattern as prior M9 waves). Visual click/reset deferred.

Regression HTTP:

| URL | Status | Notes |
|-----|--------|-------|
| `/katalog/nejtralnoe-oborudovanie/stellazhi` | 200 | 15 cards, 24 checkboxes |
| `/katalog/nejtralnoe-oborudovanie/stoly` | 200 | 15 cards, 37 checkboxes |
| `/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye` | 200 | 15 cards, 26 checkboxes |
| `/katalog/nejtralnoe-oborudovanie/moechnye-vanny` | 200 | 15 cards, 47 checkboxes |
| `/katalog/` | 200 | OK |
| `/upakovochnoe-oborudovanie` | 200 | OK |
| `/posuda-i-inventar` | 200 | generic fallback still shows `Материал изготовления` — expected, not `[186]` |
| `/zapchasti` | **404** | expected |

---

## 13. Regression

| Item | Result |
|------|--------|
| DB writes | **0** |
| Product/category writes | **0** |
| SEO writes | **0** |
| Import runs | **0** |
| Baseline refresh | **0** |
| PDP changes | **0** |
| Non-target M9 profile content | **0** |
| Files changed | `186_hlebopekarnoe.php` (new) + resolver additive `186` |
| Rollback | **available** |
| Screenshots | **no**, intentionally deferred |

---

## 14. OPERATOR CHECK — ВИЗУАЛЬНАЯ ПРОВЕРКА ОТЛОЖЕНА ДО ОБЩЕГО PASS

Screenshots were **intentionally not captured** in this wave. Combined later visual pass should include `[86]`, `[301]`, `[331]`, `[186]`, key PDPs, desktop and mobile.

### URLs to check later

1. https://bzpm.ru/hlebopekarnoe-oborudovanie — hub; no product listing; no filter sidebar expected
2. https://bzpm.ru/hlebopekarnoe-oborudovanie/miksery-planetarnye — mixers PLP, **5** cards
3. https://bzpm.ru/hlebopekarnoe-oborudovanie/testomesy — dough mixers PLP, **7** cards
4. https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi — `[86]` regression
5. https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly — `[301]` regression
6. https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye — `[331]` regression
7. Sample PDPs from mixers / dough mixers

### Should be visible

- Sidebar title `Поиск по параметрам` on `[188]` / `[189]`
- PRIMARY: Объем, Мощность, Напряжение
- SECONDARY less prominent / collapsed (`Дополнительные параметры`)
- Product listing 5 / 7 unchanged

### Should not be visible

- `Материал изготовления` as a filter group on bakery PLPs
- packaging attrs as named groups
- public `БЗПМ`
- PHP warnings

### Click / reset

Technical GET smoke used:

`https://bzpm.ru/hlebopekarnoe-oborudovanie/miksery-planetarnye?attr[obem][]=10`

GET returned 200 and changed HTML, but **did not reduce card count** (JS/AJAX filter path). Full click / «Показать товары» / reset is **deferred** to the combined visual pass.

---

## 15. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-HLEBOPEKARNOE-PROFILE-186-01\`

Includes: `preflight/`, `docs-read/`, `db-readonly/`, `attribute-analysis/`, `profile-before/`, `profile-plan/`, `file-backups/`, `rollback/`, `public-before/`, `deploy/`, `cache/`, `public-after/`, `operator-check/`, `regression/`, `git/`, `reports/`, `logs/`, `manifests/operation.json`.

No `screenshots/` folder required for this wave.

---

## 16. Git status

- Branch: `mars/canonical-post-recovery`
- HEAD: `a5a13ba6a3efdd4262beea1820bc7b4135e00438`
- `origin/mars/canonical-post-recovery`: `131882bdfdcfc4e11ad68b32f133201e66b17407`
- Staged: empty
- Unpushed commits vs origin: **present** (including unrelated ISEO report-hub work)
- Working tree: dirty (large foreign WIP)

Allowlisted uncommitted for this wave:

- `M` `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/filter_profile_resolver.php`
- `??` `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/filter_profiles/186_hlebopekarnoe.php`
- `??` this report

**Phase 13 commit: SKIPPED.** Reasons:

1. large foreign WIP — must not `git add .` / `-A` / `commit -a`
2. unpushed commits already exist vs origin
3. git HEAD resolver still lists roots `80, 207, 301, 322, 326` only; working copy now also folds in previously uncommitted `86` / `331` plus `186`, and collapses extra blank lines — not a clean single-wave resolver diff

Do **not** force-push. Selective commit deferred to operator when the M9 patch dir can be staged alone.

---

## 17. SAFE UNKNOWN / blockers

1. PLP still shows **Длина / Ширина / Высота** facet sliders (`len_from` / `w_from` / `h_from`) plus price UX. These are a separate layer from M9 HIDDEN packaging attrs 44/45/46. Same SAFE UNKNOWN as `[331]`. This wave did not change SUPER_ATTS / templates.
2. HTTP GET `attr[obem][]=10` does not reduce listing without JS/AJAX. Visual click/reset unverified in this wave (deferred).
3. Public-before product-card count used a different selector (`product-thumbs=0`); after-state used `p-card` (5 / 7). Card counts match operator-known leaf sizes.
4. Repo resolver working copy is **not** byte-identical to the production payload (production used live CRLF + additive 186). Logic of registered roots/map after deploy includes `186`; git mirror needs a later clean reconcile.

**No deploy blockers** after preflight. No rollback executed.

---

## 18. Final verdict

`SITE-002 M9 HLEBOPEKARNOE PROFILE 186 COMPLETE — VISUAL QA DEFERRED`

---

## 19. Next recommendation

1. Keep `[186]` live; do not recapture screenshots until the combined VISUAL QA wave.
2. Combined visual pass (desktop + mobile): `[86]` / `[301]` / `[331]` / `[186]` leaf PLPs + key PDPs; click/reset on bakery mixers.
3. If L/W/H sliders are unwanted on bakery PLPs: separate charter (do not mass-edit `global_hidden` / PDP here).
4. Optional later git: stage **only** this report + `186_hlebopekarnoe.php` + a carefully reviewed resolver mirror (`ocpilot: add M9 bakery filter profile`) once foreign WIP is excluded.
5. Next M9 candidate only after operator is ready — do not auto-start `[381]` / `[364]`.

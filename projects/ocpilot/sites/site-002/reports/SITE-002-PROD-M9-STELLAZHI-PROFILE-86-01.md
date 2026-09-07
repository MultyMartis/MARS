# REPORT — SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01

**Operation:** SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01  
**Site:** SITE-002 / ЗПМ (`https://bzpm.ru/`)  
**Environment:** CONTROLLED_PRODUCTION_FILTER_PROFILE_UPDATE  
**Date (UTC):** 2026-09-06  
**Final verdict:** `SITE-002 M9 STELLAZHI PROFILE 86 COMPLETE — OPERATOR VISUAL CHECK REQUIRED`

---

## 1. Scope

Create and deploy a bounded M9 filter profile for branch root **`[86] Стеллажи`** only.

- Replace noisy generic fallback on shelving PLP with curated PRIMARY / SECONDARY / HIDDEN.
- Keep sidebar title **«Поиск по параметрам»**.
- Do **not** implement PDP family resolver, change `SUPER_ATTS`, mass-edit `global_hidden.php`, or touch other category profiles except additive resolver registration for `86`.

## 2. Operator decision

Wave **03A** approved:

- First target: `[86] Стеллажи`
- Profile for `[86]` only
- No PDP family resolver this wave
- No global `SUPER_ATTS` change
- No mass `global_hidden.php` expansion
- Clear manual visual check after apply

## 3. Production safety boundary

| Gate | Value |
|------|--------|
| DB writes | **0** (SELECT only) |
| FTP write | Exact M9 files only |
| Import / baseline | Forbidden / not run |
| Product/category/SEO writes | **0** |
| PDP / SUPER_ATTS | Unchanged |
| `global_hidden.php` | Unchanged |
| Other profiles (301/80/322/326/207) | Unchanged |
| Rollback | Prepared |

Storage evidence root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01\`

## 4. Docs / architecture read

Preserved M9 rules:

- Native `oc_filter*` is not the ZPM filter UI authority for registered roots.
- Profiles live under `system/library/zpm/filter_profiles/{id}_{slug}.php`.
- Resolver: `filter_profile_resolver.php` (allowlist PRIMARY+SECONDARY).
- Do **not** copy `301_stoly` blindly; do **not** profile hub `[79]`.
- Live deploy built from **live-before resolver + additive 86** (not blind repo whitespace overwrite).

Key planning inputs: Wave 02 P1 `[86]`; decision plan / audit / architecture study (repo + Storage).

## 5. `[86]` before state

| Item | Evidence |
|------|----------|
| Category | `[86] Стеллажи`, active |
| SEO | `stellazhi` |
| PLP | `https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi` → **200** |
| Products | ~600 (inventory / decision plan) |
| Profile before | **Absent** (not in registered roots) |
| Sidebar | «Поиск по параметрам» present |
| Checkboxes | **25** |
| Noisy | **«Стандарт»** present |
| Public БЗПМ / PHP warnings | None |

Artifact: `public-before/public-before-summary.md`

## 6. Attribute analysis

Built from production SELECT inventory (not guesses).

Buyer axes verified on `[86]`:

- **51** Конструкция полки (перфорированная / сплошная / решётчатая)
- **122** Макс. распределенная нагрузка на полку (кг) — rack axis; **not** table attr `20`
- **26** Ножки / каркас
- **114** Количество полок

Secondary candidates: 112, 21, 33, 31, 113, 115.  
Hide/noise: 42 «Стандарт», 43 доп. сведения; packaging via existing `global_hidden`.

Artifacts: `attribute-analysis/*`, `db-readonly/*`

## 7. Profile decision

**File:** `86_stellazhi.php`  
**Resolver:** additive registration `86 => 86_stellazhi.php`  
**`global_hidden.php`:** no change

| Tier | Attribute IDs |
|------|----------------|
| PRIMARY | 51, 122, 26, 114 |
| SECONDARY | 112, 21, 33, 31, 113, 115 |
| HIDDEN (branch) | 42, 43 |

Artifacts: `profile-plan/profile-86-plan.md`, `profile-plan/profile-86-attribute-tiers.csv`

## 8. Backup / rollback

- Live resolver backed up (6207 bytes, no `86_stellazhi`) under `file-backups/live-before/`.
- Rollback: restore that resolver; delete new `86_stellazhi.php`; narrow attribute cache clear.
- Plan: `rollback/rollback-plan.md`

## 9. Deploy

Uploaded **exactly two** files (FTP verify byte/SHA match):

1. `/public_html/system/library/zpm/filter_profiles/86_stellazhi.php` — NEW (1596 bytes)
2. `/public_html/system/library/zpm/filter_profile_resolver.php` — additive 86 (6245 bytes)

Not uploaded: `global_hidden.php`, other profiles, templates/CSS/PDP.

Artifact: `deploy/deploy-summary.md`

## 10. Cache

Narrow clear only: `cache.category.attributes*` under site storage cache.  
Deleted **10 / 10** matched files. No broad cache wipe.

Artifact: `cache/cache-action-summary.md`

## 11. Public after

| Check | Result |
|-------|--------|
| Stellazhi PLP | **200** |
| Sidebar title | «Поиск по параметрам» **True** |
| Checkboxes | **24** (was 25) |
| PRIMARY markers | Конструкция полки / нагрузка / ножки / количество полок — **present** |
| Noisy «Стандарт» | **absent** as noisy marker |
| Public БЗПМ / PHP warnings | **None** |
| Listing smoke peers | stoly / moechnye / podtovarniki / telezhki → **200** with sidebar |
| `/katalog/`, packaging, posuda | **200** |
| `/zapchasti` | **404** (expected) |

Artifact: `public-after/public-after-summary.md`

## 12. Regression

| Mutation | Count |
|----------|------:|
| DB writes | 0 |
| Product/category/SEO writes | 0 |
| Import / baseline | 0 |
| PDP changes | 0 |
| Non-target profile content changes | 0 |
| Files changed on production | 2 |
| Rollback available | YES |

Regression overall: **PASS** (`regression/regression-summary.md`).

---

## 13. OPERATOR CHECK — ПРОВЕРИТЬ ФИЛЬТР СЕЙЧАС

### Открыть сейчас

1. **Стеллажи (цель):**  
   https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi
2. Регрессия (по желанию):  
   - https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly  
   - https://bzpm.ru/katalog/nejtralnoe-oborudovanie/moechnye-vanny  

### Что должно быть видно

- Заголовок сайдбара: **«Поиск по параметрам»**
- PRIMARY оси стеллажей:
  - конструкция полки (перфорированная / сплошная / решётчатая)
  - нагрузка на полку (например 50 / 80)
  - ножки / каркас
  - количество полок
- Диапазоны Длина / Ширина / Высота и цена — как раньше (не трогали `SUPER_ATTS`)
- Список товаров и пагинация стабильны

### Чего НЕ должно быть как шум PRIMARY

- **«Стандарт»**
- **«Дополнительные сведения»**
- упаковочные поля как основные фильтры
- поломка столов / ванн / подтоварников / тележек

### Безопасный тест одного фильтра

1. Открыть PLP стеллажей.
2. Отметить одно PRIMARY-значение (например «Полка перфорированная» или нагрузка 50).
3. Убедиться: нет PHP Warning, нет «БЗПМ», список сузился.
4. «Сбросить» — список возвращается.

### Если плохо — прислать

- скрин сайдбара
- URL после клика
- что лишнее / что пропало

Rollback: Storage `rollback/rollback-plan.md`.

---

## 14. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01\`

Includes: `preflight/`, `docs-read/`, `db-readonly/`, `attribute-analysis/`, `profile-plan/`, `file-backups/`, `rollback/`, `public-before/`, `deploy/`, `cache/`, `public-after/`, `operator-check/`, `regression/`, `git/`, `reports/`, `logs/`, `manifests/`.

## 15. Git status

Branch: `mars/canonical-post-recovery`  
Workspace: `X:\AI MARS` / volume `AI WS`

Repo mirrors for this wave:

- `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/filter_profiles/86_stellazhi.php` (new)
- `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/filter_profile_resolver.php` (additive 86)
- this report

**Foreign WIP** present across unrelated projects — not staged/cleaned by this wave.  
Live production resolver was deployed from **live-before + additive**, independent of repo formatting/CRLF quirks.

## 16. SAFE UNKNOWN / blockers

| Item | Note |
|------|------|
| Exact public SEO URL for `[207] Зонты` | Smoke path `/katalog/nejtralnoe-oborudovanie/zonty` → **404** in this wave; **profile file still present** on live (`207_zonty.php`). Treated as **pre-existing SEO/URL** issue, not introduced by `[86]` deploy. Correct public URL for visual check of 207: **UNKNOWN** without separate SEO SELECT. |
| Hard stops | None triggered — deploy completed. |

## 17. Final verdict

**`SITE-002 M9 STELLAZHI PROFILE 86 COMPLETE — OPERATOR VISUAL CHECK REQUIRED`**

## 18. Next recommendation

1. Operator visual check on stellazhi URL (section 13).
2. If OK → Wave 03B candidates per plan: refresh `[301] Столы`, then `[331] Полки` / `[186]` later; keep `[381]` deferred for filters.
3. Optional follow-up: resolve correct public URL for `[207] Зонты` (read-only SEO audit) — **not** part of this wave.
4. Do **not** enable PDP family resolver until a separate charter.

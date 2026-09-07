# REPORT — SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01

**Operation:** SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01  
**Site:** SITE-002 / ЗПМ (`https://bzpm.ru/`)  
**Environment:** CONTROLLED_PRODUCTION_FILTER_PROFILE_REFRESH  
**Date (UTC):** 2026-09-06  
**Final verdict:** `SITE-002 M9 STOLY PROFILE 301 REFRESH COMPLETE — OPERATOR VISUAL CHECK REQUIRED`

---

## 1. Scope

Refresh existing M9 filter profile for branch root **`[301] Столы`** only.

- Not a rewrite from scratch — change only where live catalog evidence justified.
- Keep sidebar title **«Поиск по параметрам»**.
- Investigate attrs **47 / 51** empty `filter_name`; fix only if safe **without DB writes**.
- Do **not** change PDP `.product-hero__specs`, `SUPER_ATTS`, mass-edit `global_hidden.php`, or other roots except regression smoke on `[86]`.

## 2. Operator decision

Approved after successful `[86] Стеллажи` waves:

1. `SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01` — profile PASS  
2. `SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01` — PDP PASS  

Next: refresh **`[301] Столы`** existing M9 profile (Wave 02 P2).

## 3. Production safety boundary

| Gate | Value |
|------|--------|
| DB writes | **0** (SELECT only) |
| FTP write | Exact `301_stoly.php` only |
| Import / baseline | Forbidden / not run |
| Product/category/SEO writes | **0** |
| PDP / SUPER_ATTS | Unchanged |
| `global_hidden.php` | Unchanged |
| Resolver | Unchanged |
| Other profiles (86/80/…) | Unchanged (regression only) |
| Rollback | Prepared |

Storage evidence root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01\`

## 4. Docs / architecture read

Preserved M9 rules (from BZPM-M9 docs + Phase reports + Wave 02 decision plan):

- Native `oc_filter*` empty; ZPM UI uses M9 profiles + resolver + `global_hidden.php` + M9.8.9 UX.
- Profiles: `system/library/zpm/filter_profiles/{id}_{slug}.php`.
- Resolver already registers **301**; profile was already active.
- Do **not** profile hub `[79]`; do not copy rules blindly across roots.
- Empty `filter_name` → numeric form keys `attr[47][]` / `attr[51][]`; 06J numeric-slug SQL mitigates filtering; legends use `ad.name`.

## 5. `[301]` before state

| Item | Evidence |
|------|----------|
| Category | `[301] Столы`, parent `[79]`, active |
| SEO | `stoly` |
| PLP | `https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly` → **200** |
| Products | ~**520** enabled under path |
| Profile | Active `301_stoly.php` |
| Live vs repo | **Byte-identical** SHA `27b89d42…e16538` |
| Sidebar | «Поиск по параметрам» |
| Checkboxes | **37** |
| PRIMARY before | `22, 51, 33, 20, 25` |
| Public БЗПМ / PHP warnings | None |

## 6. Attribute analysis

Built from production SELECT inventory (not guesses).

Buyer-useful axes verified on `[301]`:

| attr | name | products | distinct | action |
|------|------|----------|----------|--------|
| 22 | Материал столешницы | high | 3 | KEEP_PRIMARY |
| 51 | Конструкция полки | 520 | 4 | KEEP_PRIMARY |
| 20 | Макс. нагрузка | high | 3 | KEEP_PRIMARY |
| 25 | Наличие борта | 493 | multi | KEEP_PRIMARY |
| 33 | Тип опоры | **520** | **1** (`опора-болт`) | **MOVE_TO_SECONDARY** |
| 47 | Конструкция борта | 85 | 3 | KEEP_SECONDARY |
| 21,112,26,31,115,18 | dims / construction | — | — | KEEP_SECONDARY |
| 23,28,29 | sink niche | — | — | KEEP_HIDDEN |
| packaging / one-offs | — | — | — | LEAVE_UNCHANGED (not exposed) |

Artifacts: `attribute-analysis/category-301-attribute-*.csv|.md`

## 7. Attrs `47/51` diagnostic

| attr | name | `filter_name` | display | decision |
|------|------|---------------|---------|----------|
| 51 | Конструкция полки | empty | Russian legend OK | KEEP_PRIMARY; **LEAVE label** (no DB write) |
| 47 | Конструкция борта | empty | Russian legend OK | KEEP_SECONDARY; **LEAVE label** (no DB write) |

- Form keys remain numeric (`attr[47]` / `attr[51]`) — expected with empty `filter_name`.
- Filling `filter_name` requires **forbidden DB UPDATE** → deferred.
- No blank/empty legends observed before or after.

Artifact: `attribute-analysis/category-301-attribute-47-51-diagnostic.md`

## 8. Profile before/after

| Tier | Before | After |
|------|--------|-------|
| PRIMARY | `22, 51, 33, 20, 25` | `22, 51, 20, 25` |
| SECONDARY | `21, 112, 26, 31, 115, 18, 47` | `21, 33, 112, 26, 31, 115, 18, 47` |
| HIDDEN | `23, 28, 29` | unchanged |

**Delta:** demote attr **33 Тип опоры** PRIMARY → SECONDARY (single value, not discriminative).

Public-after HTML order confirms «Тип опоры» appears **after** «Дополнительные параметры» (`tip_after_dop=True`).

Deployed SHA: `df7233eaaa770b4d8d01ca4aaf25ecdd28c825c2f80de9dcd8a4ab70dee84715`  
Repo mirror synced to same bytes.

## 9. Backup / rollback

- Live-before SHA: `27b89d4203887c8e59c20aef1e333fcb2d484e181bd2edd1b5e1d0e1dbe16538`
- Backups: `file-backups/live-before-deploy/301_stoly.php`, `file-backups/rollback-ready/301_stoly.php`
- Plan: `rollback/rollback-plan.md`

Rollback available: **yes** (FTP restore previous file + cache clear).

## 10. Deploy

| Item | Value |
|------|--------|
| Remote | `/public_html/system/library/zpm/filter_profiles/301_stoly.php` |
| SHA after | `df7233ea…ee84715` (payload match **True**) |
| Resolver | **not** deployed |
| `global_hidden.php` | **not** deployed |
| Templates/CSS/PDP | **not** deployed |
| Time (UTC) | 2026-09-06T20:20:32+00:00 |

## 11. Cache

OpenCart cache/template `*.php` under `/home/a/assum/bzpm.ru/storage/cache` cleared after deploy.  
Artifact: `cache/cache-action-summary.md`

## 12. Public after

| URL | Status | Notes |
|-----|--------|-------|
| `/katalog/nejtralnoe-oborudovanie/stoly` | **200** | Poisk=True; 37 checkboxes; pagination OK; no БЗПМ; no PHP warnings |
| Material / shelf / load / board | present | PRIMARY intact |
| Тип опоры | present | under secondary accordion |
| 47/51 legends | Russian OK | numeric keys still present |

## 13. Regression

| Check | Result |
|-------|--------|
| `[86] Стеллажи` | 200, Poisk, 24 checkboxes |
| `80` моечные ванны | 200, Poisk |
| `/katalog/` | 200 |
| `/upakovochnoe-oborudovanie` | 200 |
| `/posuda-i-inventar` | 200 |
| `/zapchasti` | **404** (expected) |
| DB / product / SEO / import / PDP writes | **0** |
| Non-target M9 profiles changed | **0** |

---

# OPERATOR CHECK — ПРОВЕРИТЬ ФИЛЬТР СТОЛОВ СЕЙЧАС

## Открыть

1. **Столы:** https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly  
2. **Регрессия стеллажи:** https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi  

Hard refresh (Ctrl+F5) если кэш браузера старый.

## Что должно быть видно на Столах

- Заголовок сайдбара: **«Поиск по параметрам»**
- В основных (PRIMARY) блоках:
  - Материал столешницы  
  - Конструкция полки  
  - Макс. нагрузка  
  - Наличие борта  
- **«Тип опоры»** — только в **«Дополнительные параметры»** (не в верхнем PRIMARY)
- Подписи **Конструкция полки** / **Конструкция борта** — нормальный русский текст (не пустые легенды)
- Листинг товаров и пагинация без поломок

## Чего не должно быть

- Пустых / «безымянных» групп фильтра  
- PHP Warning / Fatal  
- Публичного текста `БЗПМ`  
- Резкого раздувания шумных атрибутов (упаковка, SERVICE и т.п.)  
- Сломанного фильтра на **Стеллажах**

## Быстрый smoke фильтра

1. На Столах выбрать одно значение PRIMARY (например материал) → список сужается.  
2. Сброс фильтра → полный список снова.  
3. На Стеллажах открыть сайдбар — профиль `[86]` на месте, клик/сброс работает.

## Если что-то не так

Прислать скриншоты: весь сайдбар Столов + блок PRIMARY + «Дополнительные параметры» + шапка листинга; плюс сайдбар Стеллажей.  
Откат: восстановить `file-backups/rollback-ready/301_stoly.php` (SHA `27b89d42…`).

---

## 15. Storage artifacts

Root: `...\SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01\`

Key paths: `preflight/`, `db-readonly/`, `attribute-analysis/`, `profile-before/`, `profile-plan/`, `file-backups/`, `rollback/`, `public-before/`, `deploy/`, `cache/`, `public-after/`, `regression/`, `operator-check/`, `manifests/operation.json`

## 16. Git status

- Branch: `mars/canonical-post-recovery`
- Volume: `AI WS` / workspace `X:\AI MARS`
- Changed this wave (repo):  
  - `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/.../301_stoly.php`  
  - this report  
- Foreign WIP: large unrelated tree — **not** staged  
- Optional selective commit: authorized by charter Phase 13 if performed

## 17. SAFE UNKNOWN / blockers

- Exact live OpenCart version / opcode cache behavior beyond template cache clear: **SAFE UNKNOWN** (smoke passed).  
- Operator visual confirmation still pending.  
- Permanent `filter_name` fill for 47/51 deferred (needs DB write — out of scope).

## 18. Final verdict

**`SITE-002 M9 STOLY PROFILE 301 REFRESH COMPLETE — OPERATOR VISUAL CHECK REQUIRED`**

## 19. Next recommendation

1. Operator visual check (section above).  
2. After PASS: proceed Wave 02 next P-item (e.g. other roots) — **not** PDP for tables unless separately chartered.  
3. Optional later HITL: DB fill `filter_name` for 47/51 under a **separate** DB-write charter (not this wave).

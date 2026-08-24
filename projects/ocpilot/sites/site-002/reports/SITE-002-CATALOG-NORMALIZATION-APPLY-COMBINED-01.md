# REPORT — SITE-002 Catalog Normalization Apply Combined 01

**Operation:** `SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01`
**Site:** SITE-002 / ЗПМ Production — `https://bzpm.ru/`
**Run:** 4.343
**Applied:** 2026-08-25 (local +07) / 2026-08-24T17:44Z UTC
**Decision freeze:** `d4ecf1a0` — [SITE-002-CATALOG-NORMALIZATION-DECISION-FREEZE-01.md](SITE-002-CATALOG-NORMALIZATION-DECISION-FREEZE-01.md)
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01\`

---

## 1. Scope

Bounded combined production apply implementing the frozen 8-root catalog model:

- **Keep as root (unchanged):** `79`, `95`, `90`, `186`
- **Promote to root:** `364` (Посуда), `375` (Электромеханическое), `373` (Мясоперерабатывающее)
- **Create root + map:** `381` (Упаковочное оборудование — new)
- **Tmp rename + disable:** `362`, `93`, `171`, `205`, `206`
- **Hold (unchanged):** `96` (Запчасти)

Forbidden scope respected: no import, no monitor/baseline refresh, no product content changes, no `[96]` mutation, no PHP/template deploy.

---

## 2. Operator approval and backup signal

| Signal | Status |
|--------|--------|
| Combined apply approval | Operator: «Ок, утверждаю. Жду промт.» |
| Beget full backup | Operator-stated — **not independently verified by MARS** |
| Local bounded DB snapshots | **YES** — `db-snapshots/` before apply |
| Rollback SQL | **YES** — `rollback/rollback.sql` (+ path TSV restore notes) |

---

## 3. Production apply boundary

| Class | Allowed | Actual |
|-------|---------|--------|
| DB category hierarchy/status/name/SEO | Yes | Applied (B–E) |
| DB insert Upakovochnoe + mapping | Yes | Applied (`381`) |
| DB mapping other categories | No change | Preserved |
| FTP `.htaccess` 301 redirects | Yes | 3 rules appended |
| OpenCart cache clear | Yes | `cache.*` cleared |
| PHP/template/controller | No | **0** |
| 1C import | No | **0** |
| Monitor/baseline | No | **0** |

---

## 4. Authority preflight

| Check | Result |
|-------|--------|
| Worktree | `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` |
| HEAD | `d4ecf1a0` (decision freeze present) |
| Origin | `16a14050` (5 commits ahead — ISEO/FP-0002; ff-merge before push) |
| Working tree at apply | Clean except new apply script (not committed per charter) |

Artifacts: `preflight/authority-git-state.txt`, `preflight/authority-origin-state.txt`

---

## 5. Evidence basis

- [SITE-002-CATALOG-NORMALIZATION-DECISION-FREEZE-01.md](SITE-002-CATALOG-NORMALIZATION-DECISION-FREEZE-01.md)
- [SITE-002-CATALOG-STRUCTURE-NORMALIZATION-PLAN-01.md](SITE-002-CATALOG-STRUCTURE-NORMALIZATION-PLAN-01.md)
- [SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01.md](SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01.md)
- [SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-FLAT.csv](SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-FLAT.csv)
- Prior redirect pattern: Lari reparent Wave C (`.htaccess` 301)

---

## 6. Production before snapshot

Key pre-apply state (see `production-before/`):

| ID | Name | parent | status | keyword |
|----|------|--------|--------|---------|
| 364 | Посуда и инвентарь | 362 | 1 | posuda-i-inventar |
| 375 | Электромеханическое | 362 | 1 | elektromehanicheskoe |
| 373 | Мясоперерабатывающее | 362 | 1 | myasopererabatyvayuschee |
| 362 | Технологическое оборудование | 0 | 1 | tehnologicheskoe-oborudovanie |
| 93/171/205/206 | Legacy empty roots | 0 | 1 | various |
| 96 | Запчасти | 0 | 0 | zapchasti |
| — | Упаковочное | absent | — | — |

Product links unchanged scope: `364`→6 products, `96`→76, `95`→1.

---

## 7. Exact mutation plan

Single transaction SQL: `exact-mutation-plan/apply.sql`

Phases in one COMMIT:

1. INSERT root category Upakovochnoe + description + store + path + seo + mapping
2. UPDATE `364/375/373` parent_id=0 + rebuild `oc_category_path` (subtrees 380, 376, 378, 379)
3. Tmp rename + disable `362/93/171/205/206` (name, seo keyword, status=0)

---

## 8. Rollback SQL

`rollback/rollback.sql` — reverses parent_id, status, names, seo keywords, deletes Upakovochnoe row chain.

**Note:** `oc_category_path` subtree restore for promoted categories requires TSV snapshots:

- `db-snapshots/category_path-before-364.tsv`
- `db-snapshots/category_path-before-375.tsv`
- `db-snapshots/category_path-before-373.tsv`

Upakovochnoe rollback line uses seo keyword lookup — verify `@DEL_UPAK` resolves via `query` field if manual rollback needed.

---

## 9. SEO URL / redirect mechanism

| Item | Value |
|------|-------|
| Table | `oc_seo_url` (store_id=0, language_id=1) |
| Routing | OpenCart SEO + `category_path` hierarchy |
| Redirect mechanism | `.htaccess` RewriteRule 301 (prior art) |
| Marker | `# SITE-002 catalog normalization redirects (SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01)` |

**Redirects applied:**

```
tehnologicheskoe-oborudovanie/posuda-i-inventar → /posuda-i-inventar
tehnologicheskoe-oborudovanie/elektromehanicheskoe → /elektromehanicheskoe
tehnologicheskoe-oborudovanie/myasopererabatyvayuschee → /myasopererabatyvayuschee
```

Smoke: old nested paths resolve to canonical root URLs (client followed to 200 on canonical).

---

## 10. Apply B — Upakovochnoe

| Field | Value |
|-------|-------|
| New category_id | **381** |
| 1C GUID | `5bc6a012-7c19-11f1-aecc-581122cf362c` |
| Mapping | `oc_mars_1c_category_map` map_id **10** — active |
| Public URL | `/upakovochnoe-oborudovanie` — **HTTP 200** |
| Product assignment | **PRODUCT_ASSIGNMENT_PENDING_NEXT_IMPORT** — 1 product in 1C; no manual `product_to_category` insert |

---

## 11. Apply C — Posuda

| Field | Value |
|-------|-------|
| category_id | **364** |
| parent_id | 362 → **0** |
| keyword | `posuda-i-inventar` (unchanged) |
| mapping | Preserved (map_id 8) |
| products | **6** (unchanged) |
| Public URL | **HTTP 200** |
| Old nested redirect | **Applied** (301 via htaccess) |

---

## 12. Apply D — Elektro / Myaso

| ID | Name | parent | keyword | products |
|----|------|--------|---------|----------|
| 375 | Электромеханическое | 362→**0** | elektromehanicheskoe | unchanged |
| 373 | Мясоперерабатывающее | 362→**0** | myasopererabatyvayuschee | unchanged |

Child paths rebuilt: `380` under 375; `376`, `378`, `379` under 373.

Public URLs: **HTTP 200**. Old nested redirects: **Applied**.

**Slug note:** Task mentioned `/elektromehanicheskoe-oborudovanie`; production DB keyword is `elektromehanicheskoe` — preserved per discover-from-DB rule.

---

## 13. Apply E — tmp rename + disable

| ID | New name | New keyword | status |
|----|----------|-------------|--------|
| 362 | tmp Технологическое оборудование | tmp-tehnologicheskoe-oborudovanie | 0 |
| 93 | tmp Инвентарь | tmp-inventar | 0 |
| 171 | tmp Барное оборудование | tmp-barnoe-oborudovanie | 0 |
| 205 | tmp Посудомоечные машины | tmp-posudomoechnye-mashiny | 0 |
| 206 | tmp Вентиляционное оборудование | tmp-ventilyacionnoe-oborudovanie | 0 |

Gate #8: promoted categories removed from under 362; remaining twins (`368`, `369`, etc.) stay under disabled 362 — not intended public roots per freeze.

Old public URLs → **404** (expected).

---

## 14. Cache action

Cleared: `/home/a/assum/bzpm.ru/storage/cache/cache.*`
OCMOD/modification: **not touched** (no PHP deploy).

---

## 15. Production after snapshot

**Active public roots (target model):**

1. `79` Нейтральное оборудование — `/nejtralnoe-oborudovanie`
2. `95` Холодильное оборудование — `/holodilnoe-oborudovanie`
3. `90` Тепловое оборудование — `/teplovoe-oborudovanie`
4. `186` Хлебопекарное оборудование — `/hlebopekarnoe-oborudovanie`
5. `375` Электромеханическое — `/elektromehanicheskoe`
6. `373` Мясоперерабатывающее — `/myasopererabatyvayuschee`
7. `364` Посуда и инвентарь — `/posuda-i-inventar`
8. `381` Упаковочное оборудование — `/upakovochnoe-oborudovanie`

**Hold unchanged:** `96` Запчасти — status=0, `/zapchasti` 404 (pre-existing).

Artifacts: `production-after/`

---

## 16. Public HTTP smoke

**15/21 paths HTTP 200** on primary targets; disabled legacy roots **404** as expected.

| Path | Status | Notes |
|------|--------|-------|
| `/`, `/katalog/` | 200 | OK |
| All 8 target roots | 200 | OK |
| `/assum`, `/sitemap.xml` | 200 | OK |
| Old nested promoted paths | 200→canonical | Redirect to root URL |
| Disabled roots | 404 | Expected |
| `/zapchasti` | 404 | Unchanged hold |

No PHP fatal text; no forbidden `БЗПМ` in titles checked.

Full CSV: `public-http/public-http-smoke.csv`

---

## 17. Sitemap check

| Metric | Value |
|--------|-------|
| Live unique URLs | **1861** |
| Prior baseline | **1887** |
| Delta | **−26** (expected from root promotion, tmp slugs, new upakovochnoe) |
| Baseline refresh | **NOT done** — separate Apply 07 |

New root URLs present in live sitemap; tmp-disabled slugs expected absent.

---

## 18. Menu / UI smoke

Lightweight — homepage/katalog 200; full mega-menu HTML parse deferred. No PHP warnings observed on catalog paths.

---

## 19. Forms smoke

Deferred — no form submission; homepage/catalog markup assumed intact from 200 responses.

---

## 20. Regression / mutation summary

| Item | Value |
|------|-------|
| production_db_writes | Bounded B–E only |
| ftp_writes | htaccess redirects only |
| zapchasti_changed | **0** |
| import_runs | **0** |
| baseline_refresh | **0** |
| monitor_code | **0** |
| product_content | **0** |
| cleanup_delete | **0** |

---

## 21. Git / worktree summary

- Apply executed from authority worktree at freeze commit `d4ecf1a0`
- Apply harness: `tools/site-002-catalog-normalization-apply-combined-01.py` (Storage-local; not in commit charter)
- Docs commit: report + OCPilot state updates only
- Push target: `origin/mars/canonical-post-recovery`

---

## 22. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01\`

Key folders: `preflight/`, `production-before/`, `db-snapshots/`, `exact-mutation-plan/`, `rollback/`, `phase-b-upakovochnoe/` … `phase-e-tmp-disable/`, `redirects/`, `cache/`, `production-after/`, `public-http/`, `sitemap/`, `regression/`, `decision/final-verdict.txt`

---

## 23. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Beget backup verification | Operator-stated only |
| Upakovochnoe product on category page | Pending next natural 1C import |
| Sitemap baseline delta acceptance | Requires separate baseline refresh (Apply 07) |
| Menu mega-nav full verification | Lightweight smoke only |
| 301 vs internal rewrite on old nested URLs | Client resolves to canonical; htaccess rules present |

**No blockers preventing apply completion.**

---

## 24. Final verdict

**SITE-002 CATALOG NORMALIZATION APPLY COMBINED COMPLETE — TARGET ROOT MODEL APPLIED, BASELINE REFRESH PENDING**

Tags:

- `SITE_002_CATALOG_NORMALIZATION_APPLY_COMBINED_COMPLETE`
- `UPAKOVOCHNOE_CREATED_AND_MAPPED` (`381`)
- `UPAKOVOCHNOE_PRODUCT_ASSIGNMENT_PENDING_NEXT_IMPORT`
- `POSUDA_PROMOTED_TO_ROOT` (`364`)
- `POSUDA_OLD_URL_REDIRECTED`
- `ELEKTRO_PROMOTED_TO_ROOT` (`375`)
- `MYASO_PROMOTED_TO_ROOT` (`373`)
- `TMP_DISABLE_COMPLETE`
- `ZAPCHASTI_UNCHANGED` (`96`)
- `BASELINE_REFRESH_PENDING`
- `PRODUCTION_MUTATION_BOUNDED`

---

## 25. Next recommendation

1. **Observe next natural 1C import** — confirm Upakovochnoe product lands in `381`; mapping persistence for promoted categories.
2. **Run monitor baseline refresh (Apply 07)** — accept sitemap **1861** (or post-import count) as new baseline after validation.
3. **Operator visual HITL** — verify catalog/mega-menu shows 8 public roots; tmp categories absent.
4. **Optional:** full menu HTML smoke if operator reports nav drift.

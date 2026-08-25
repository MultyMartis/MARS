# SITE-002-PROD-POSUDA-UPAKOVOCHNOE-EMPTY-CATEGORY-CHECK-01

**Operation:** verify product presence and temporarily hide empty root categories if needed  
**Site:** SITE-002 / bzpm.ru (ЗПМ Production)  
**Timestamp (UTC):** 2026-08-24T21:46:17Z  
**Authority repo:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`

---

## 1. Scope

Проверка двух публичных корневых категорий после catalog normalization:

| ID | Название | URL |
|----|----------|-----|
| 364 | Посуда и инвентарь | `/posuda-i-inventar` |
| 381 | Упаковочное оборудование | `/upakovochnoe-oborudovanie` |

Разрешено: read-only DB/1C/public, временное скрытие пустых корней (`status=0`), cache clear, отчёт.  
Запрещено: удаление, импорт 1C, изменение товаров/цен/остатков, правки unrelated категорий и root tile visuals.

---

## 2. Operator feedback

Оператор принял визуальные волны («всё гуд»), затем сообщил: категории **Посуда и инвентарь** и **Упаковочное оборудование** «внутри пустые» — нужно проверить товары и при отсутствии временно скрыть.

---

## 3. Boundary

- Production DB + public smoke только для `[364, 381]`
- Одна production-мутация: `oc_category.status=0` для **381** только
- `[96] Запчасти`, import, monitor baseline, root CSS/images — не затронуты
- Product rows changed: **0**

---

## 4. DB / product check

### [364] Посуда и инвентарь

| Field | Value |
|-------|-------|
| parent_id | 0 (root) |
| status | 1 |
| keyword | `posuda-i-inventar` |
| 1C GUID | `9b37b1f1-7c19-11f1-aecc-581122cf362c` |
| map_status | active |
| direct enabled | **6** |
| subtree enabled | **6** |
| child categories | **0** |
| category_path | `0:364` |
| store_bound | yes |

Products (enabled): 4397–4402 — противни и сетки для пиццы; все в `oc_product_to_category` → 364, store 0.

### [381] Упаковочное оборудование

| Field | Value |
|-------|-------|
| parent_id | 0 |
| status | **0** (after apply) |
| keyword | `upakovochnoe-oborudovanie` |
| 1C GUID | `5bc6a012-7c19-11f1-aecc-581122cf362c` |
| map_status | active |
| direct / subtree enabled | **0 / 0** |
| child categories | 0 |

---

## 5. 1C check

Источник: `import0_1.xml` + log `mars_1c_import_2026-08-24_080010.txt`.

| Category | 1C products in XML | Site enabled | Notes |
|----------|-------------------|--------------|-------|
| 364 | 6 | 6 | Товары на сайте есть (legacy SKU, не GUID в model) |
| 381 | 1 (DZ-260) | 0 | **PRODUCT_ASSIGNMENT_PENDING_NEXT_IMPORT** — как в combined apply |

Импорт **не запускался**.

---

## 6. Public before

| URL | HTTP | Product cards | Root slug visible |
|-----|------|---------------|-------------------|
| `/` | 200 | 20 | posuda ✓ upak ✓ |
| `/katalog/` | 200 | 0 | posuda ✓ upak ✓ |
| `/posuda-i-inventar` | 200 | **0** | — |
| `/upakovochnoe-oborudovanie` | 200 | **0** | — |

PHP warnings: none. Маркер БЗПМ: present.

---

## 7. Decision per category

### 364 — **ATTENTION_REQUIRED_DO_NOT_HIDE**

- В БД **6 включённых товаров**, публичный PLP **0 карточек**
- Причина: Launch Mode **section hub** (`isSectionHubCategory(364)`) — страница показывает только дочерние категории; у 364 **нет children**, товары привязаны напрямую к корню
- **Скрытие запрещено** — замаскирует регрессию после promotion to root

### 381 — **PENDING_NEXT_IMPORT_TEMP_HIDE**

- БД пусто, 1C XML содержит 1 товар, assignment ожидает natural import
- **Временно скрыто** `status=0`

---

## 8. Production apply

**Applied:** yes (381 only)

```sql
UPDATE oc_category SET status=0, date_modified=NOW() WHERE category_id=381;
```

- Mechanism: `oc_category.status=0` (как prior tmp-disable)
- Cache: `/home/a/assum/bzpm.ru/storage/cache/cache.*` cleared
- Product/import/baseline changes: **none**

---

## 9. Public after

| URL | HTTP | Product cards | Notes |
|-----|------|---------------|-------|
| `/` | 200 | 20 | upak tile **gone** (cards 32→28) |
| `/katalog/` | 200 | 0 | upak **gone** |
| `/posuda-i-inventar` | 200 | **0** | unchanged — still visible |
| `/upakovochnoe-oborudovanie` | **404** | 0 | disabled category |

---

## 10. Rollback

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-POSUDA-UPAKOVOCHNOE-EMPTY-CATEGORY-CHECK-01\rollback\rollback.sql`

```sql
UPDATE oc_category SET status=1, date_modified=NOW() WHERE category_id=381;
```

(После natural import и появления товара — re-enable 381 отдельным charter.)

---

## 11. Regression

| Check | Result |
|-------|--------|
| Categories touched | `[381]` only |
| Product rows changed | 0 |
| Import run | 0 |
| Baseline refresh | 0 |
| Root visual layout/CSS/images | untouched |
| [96] Запчасти | untouched |
| Unrelated roots | intact |

---

## 12. Git / worktree summary

| Item | Value |
|------|-------|
| Branch | `docs/site002-offers-recovery-healthcheck-03` (not canonical) |
| Foreign WIP | `site-002-catalog-normalization-ui-repair-01.py` (M), other untracked tools/reports |
| Commit | **not performed** — worktree not clean / wrong branch for canonical push |
| New artifacts | report (this file), tool script (untracked) |

---

## 13. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-POSUDA-UPAKOVOCHNOE-EMPTY-CATEGORY-CHECK-01\`

- `preflight/`, `db-before/`, `one-c-check/`, `public-before/`, `decision/`
- `rollback/rollback.sql`, `production-apply/apply.sql`
- `cache/`, `public-after/`, `regression/`, `reports/run-summary.json`

Tool: `projects/ocpilot/sites/site-002/tools/site-002-prod-posuda-upakovochnoe-empty-category-check-01.py`

---

## 14. SAFE UNKNOWN / blockers

- **364 PLP repair path:** точный patch production `category.php` / twig fallback не деплоился в этой задаче — нужен отдельный UI-repair charter
- **381 product:** появится после следующего natural 1C import; manual `product_to_category` не делался (by design)
- **1C GUID → site_product_id=absent** в summary для 364: lookup по model/sku=GUID не находит legacy SKU-товары; фактические product_id 4397–4402 подтверждены отдельным SQL

---

## 15. Final verdict

**SITE-002 POSUDA UPAKOVOCHNOE EMPTY CATEGORY CHECK ATTENTION REQUIRED — PRODUCTS PRESENT BUT PUBLIC DISPLAY EMPTY**

- **381:** временно скрыта (пустая, import pending) ✓  
- **364:** **не скрыта** — 6 товаров в БД, пустой PLP из‑за section-hub rendering без children ✓  
- Rollback для 381 готов ✓

---

## 16. Next recommendation

1. **Charter: SITE-002 section-hub leaf fallback** — если section hub без children, но с direct enabled products → показывать product PLP (или исключить 364 из hub-only mode). Deploy `category.php` / `category_visibility.php`, cache clear, public smoke на `/posuda-i-inventar`.
2. После natural 1C import — проверить появление товара в **381**, re-enable `status=1` по rollback SQL + smoke.
3. Git: перенести report + tool в canonical branch отдельной commit-wave (selective staging), когда worktree чист.

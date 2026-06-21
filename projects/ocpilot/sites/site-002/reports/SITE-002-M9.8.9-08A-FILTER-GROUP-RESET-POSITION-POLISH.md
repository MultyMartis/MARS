# SITE-002 — M9.8.9-08A Filter Group Reset Button Position Polish

**Authority:** SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01  
**Deploy stamp:** 20260619-134748 UTC  
**Status:** Deployed live; twig cache cleared after rollback of failed `namespace` SSR attempt.

---

# REPORT — M9.8.9-08A FILTER GROUP RESET BUTTON POSITION POLISH

## 1. What Changed

- Кнопка **«Сбросить»** перенесена из `.flt__group-headbar` в `.flt__group-body` — под список опций attribute-группы, выравнивание по левому краю.
- Обёртка `.flt__group-headbar` удалена; заголовок группы снова — прямой `.flt__group-head` (accordion не затронут).
- Visibility logic: кнопка **всегда видна** для attribute-групп; вместо `hidden` — `disabled` + класс `.is-active` при выбранных опциях.
- CSS: disabled — серый / `cursor: not-allowed`; active — `color: var(--accent-color-02)`.
- Price / LWH / switches / глобальный «Сбросить всё» — без изменений.

## 2. Files Changed

| Remote path | Backup |
|---|---|
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | `backups/filterssidebar.twig.pre-m9.8.9-08a-group-reset-position.bak` |
| `assets/js/main.js` | `backups/main.js.pre-m9.8.9-08a-group-reset-position.bak` |
| `assets/css/style.css` | `backups/style.css.pre-m9.8.9-08a-group-reset-position.bak` |

**Work artifacts:** `reports/m9.8.9-08a-work/` (capture, patched copies, manifests, QA).

## 3. JS Logic

`updateGroupResetVisibility(root)` — вызывается из `syncChoiceClasses`:

```javascript
btn.disabled = !hasChecked;
btn.classList.toggle("is-active", hasChecked);
```

`initGroupReset` — guard `if (btn.disabled) return;` перед сбросом группы. Логика сброса и `updateBrowserUrl` — без изменений.

## 4. CSS States

`.flt__group-reset` — block, left-aligned, margin-top под опциями.

| State | Styles |
|---|---|
| `:disabled` | `color: var(--text-muted)`, `opacity: 0.65`, `cursor: not-allowed` |
| `.is-active` / `:not(:disabled)` | `color: var(--accent-color-02)`, `cursor: pointer` |
| hover/focus (active only) | `text-decoration: underline` |

Блок `.flt__group-headbar` и `[hidden]` — удалены из CSS.

## 5. QA Results

**Global checks (live):** PASS

- Нет `flt__group-headbar` в разметке
- Нет `hidden` на group-reset кнопках
- JS: `disabled` + `is-active` + click guard
- CSS: `M9.8.9-08A` + `var(--accent-color-02)`
- Reset внутри `data-acc-panel`
- `data-filter-reset` (глобальный) сохранён

**Категории:**

| Категория | Body placement | Always visible | Disabled baseline | Price OK | Global reset | Attr filter |
|---|---|---|---|---|---|---|
| Столы | PASS (12) | PASS | PASS | PASS | PASS | PASS (15 cards) |
| Моечные ванны | PASS (12) | PASS | PASS | PASS | PASS | PASS (2 cards) |
| Подтоварники | PASS (12) | PASS | PASS | PASS | PASS | PASS (1 card) |

**Примечание:** при SSR все кнопки рендерятся с `disabled`; после `syncChoiceClasses` на клиенте активная группа получает `disabled=false` и `.is-active`. Попытка Twig `namespace` для SSR отклонена — ломает рендер на live (OpenCart Twig).

**Operator QA (manual):** клик group reset / global reset / accordion — по чеклисту задачи.

## 6. Rollback

1. Восстановить из `backups/*.pre-m9.8.9-08a-group-reset-position.bak` на FTP (или из `m9.8.9-08-work` patched — состояние M9.8.9-08).
2. Очистить `system/storage/cache/template/`.
3. Manifest pre-deploy: `reports/m9.8.9-08a-work/manifest-pre-20260619-134748.json`.

---

**Git:** commit NO / push NO (per task).

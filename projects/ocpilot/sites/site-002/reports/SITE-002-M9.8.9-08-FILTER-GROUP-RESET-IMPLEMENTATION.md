# REPORT — M9.8.9-08 FILTER GROUP RESET IMPLEMENTATION

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Environment:** TEST — https://zpm.new-site.space/  
**Deploy UTC:** 2026-06-19T13:22:12Z  
**Manifest:** `reports/m9.8.9-08-work/manifest-post-20260619-132212.json`

---

## Authority confirmation

| Item | Status |
|------|--------|
| Forensic read | `SITE-002-M9.8.9-08-FILTER-GROUP-RESET-FORENSIC.md` |
| Knowledge map read | `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` |
| Authority state | **confirmed** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` |

---

## 1. Files Changed

### Live (deployed via FTP)

| Remote path | Pre SHA256 | Post SHA256 |
|-------------|------------|-------------|
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | `fbec1b53…` | `e9e46218…` |
| `assets/js/main.js` | `6ad3aa52…` | `9f0b40d9…` |
| `assets/css/style.css` | `461c10da…` | `511bf1f3…` |

### Repo artefacts

| Path | Role |
|------|------|
| `backups/filterssidebar.twig.pre-m9.8.9-08-filter-group-reset.bak` | Pre-deploy backup |
| `backups/main.js.pre-m9.8.9-08-filter-group-reset.bak` | Pre-deploy backup |
| `backups/style.css.pre-m9.8.9-08-filter-group-reset.bak` | Pre-deploy backup |
| `reports/m9.8.9-08-work/live-capture/*` | FTP capture (canonical pre-patch) |
| `reports/m9.8.9-08-work/*.patched` | Local patched copies |
| `reports/m9.8.9-08-work/m9.8.9-08-deploy-run.py` | Deploy runner |
| `reports/m9.8.9-08-work/m9.8.9-08-qa-run.py` | HTTP QA runner |
| `reports/m9.8.9-08-work/qa-results.json` | QA output |

**Not touched:** PHP, SQL, price/length/width/height ranges, switches, subcategories, backend.

---

## 2. UI Structure

Attribute groups only (`filter_groups` + nested `filter_secondary_groups`):

```html
<div class="flt__group-headbar">
  <button class="flt__group-head" type="button" data-acc-btn …>
    <span class="flt__group-title">…</span>
    <span class="flt__chev"></span>
  </button>
  <button type="button" class="flt__group-reset" data-filter-group-reset hidden …>
    Сбросить
  </button>
</div>
```

- Wrapper `.flt__group-headbar` keeps accordion `<button>` intact (no nested buttons).
- Reset sits **right of group title row** (flex headbar).
- **Skipped:** price, L/W/H, switches, «Дополнительные параметры» outer container, subcategories, footer.

---

## 3. JS Logic

| Function | Role |
|----------|------|
| `updateGroupResetVisibility(root)` | Option A — show reset only when group panel has `:checked` `.flt__check-input` |
| `initGroupReset(root)` | Click handler on `[data-filter-group-reset]` |

**Click flow:**

1. `preventDefault` + `stopPropagation` (accordion safe).
2. Scope = closest `[data-acc].flt__group` → panel `[data-acc-panel]`.
3. Uncheck panel `.flt__check-input` only; remove `.active` from labels.
4. `syncChoiceClasses(root)` → `updateBrowserUrl(form)` → existing debounced AJAX (`updateProducts`).

**Init chain:** `initGroupReset(root)` added before `syncChoiceClasses(root)` in filter `onReady`.

**Selector:** `[data-filter-group-reset]` — distinct from global `[data-filter-reset]`.

---

## 4. Visibility Logic (Option A)

- Twig: all group reset buttons render with `hidden` by default.
- `updateGroupResetVisibility()` called from end of `syncChoiceClasses()`:
  - on init (after server-rendered `checked` inputs),
  - on checkbox change,
  - on group reset,
  - on global reset.
- Button visible iff `panel.querySelector(".flt__check-input:checked") !== null`.

---

## 5. QA Results

**Global checks — PASS**

- `initGroupReset` + `updateGroupResetVisibility` present in live `main.js`.
- `.flt__group-headbar` + `data-filter-group-reset` in sidebar markup.
- Global `data-filter-reset` preserved.

| Category | Structural QA | Attr filter | Price | only_with_price | Global reset |
|----------|---------------|-------------|-------|-----------------|--------------|
| Столы (301) | 12 reset buttons | PASS (15 cards) | PASS | PASS | PASS |
| Моечные ванны (80) | 12 reset buttons | PASS (2 cards) | PASS | PASS | PASS |
| Подтоварники (322) | 12 reset buttons | PASS (1 card) | PASS | PASS | PASS |
| Тележки (326) | 0 reset buttons | PASS (baseline) | PASS | PASS | PASS |

**Scenario notes (HTTP vs browser):**

| # | Scenario | Automated | Notes |
|---|----------|-----------|-------|
| 1 | Single group → Сбросить | **browser** | JS pipeline verified in code; HTTP cannot click |
| 2 | Two groups → reset one | **browser** | Multi-group URL loads; markup OK |
| 3 | After AJAX | **browser** | Sidebar not re-fetched; local DOM + handlers persist |
| 4 | Reload with `?filters=` | **PASS (server)** | `checked` on inputs confirmed; JS init reveals reset for active group |
| 5 | Price filter untouched | **PASS** | No reset in price block |
| 6 | only_with_price untouched | **PASS** | Combined URL returns filtered cards |
| 7 | Global reset | **PASS** | `data-filter-reset` present |

Full JSON: `reports/m9.8.9-08-work/qa-results.json`

---

## 6. Rollback

1. Restore from backups:
   - `backups/filterssidebar.twig.pre-m9.8.9-08-filter-group-reset.bak`
   - `backups/main.js.pre-m9.8.9-08-filter-group-reset.bak`
   - `backups/style.css.pre-m9.8.9-08-filter-group-reset.bak`
2. Or upload pre-patch files from `reports/m9.8.9-08-work/live-capture/`.
3. Clear Twig template cache on hosting after Twig rollback.

---

## 7. Risks

| Risk | Level | Mitigation |
|------|-------|------------|
| Operator manual JS/CSS drift vs capture | LOW | Fresh FTP capture taken pre-deploy |
| Accordion click collision | LOW | Wrapper + `stopPropagation` |
| Nested secondary groups | LOW | Same headbar pattern in nested loop |
| Static QA cannot exercise click/AJAX | INFO | Browser spot-check recommended for scenarios 1–3 |
| Twig cache | INFO | Cache dir empty at deploy time; purge if sidebar stale |

---

## Git status

**Commit:** NO  
**Push:** NO

---

*Live deploy completed 2026-06-19. Three-file patch only; no backend changes.*

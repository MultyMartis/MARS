# i-SEO Report Hub — Monthly Report Detail Collapse Policy v0.1

**Wave:** Monthly Report Detail UX Collapse Charter 01  
**Date:** 2026-08-21  
**Applies to:** `GET /monthly-reports/{id}` presentation only

---

## Policy goal

Reduce first-screen technical noise while keeping every existing datum reachable in one click/expand. Prefer native HTML `<details>` / `<summary>` where practical. Minimize new JS; preserve progressive enhancement and keyboard access.

---

## Open by default

| Region | Rationale |
|--------|-----------|
| Top summary card | Manager must see state immediately |
| Primary workflow actions | Manager must see what to do next |
| Work entries section | Main working area |
| Compact content summary | Quick fill/empty scan |
| Finalized / lock warning (when applicable) | Safety — never rely on collapsed-only warning |
| Compact PDF / active-link readiness indicators | Delivery status at a glance |

---

## Collapsed by default

| Region | Rationale |
|--------|-----------|
| Finalization checklist / readiness gates | Diagnostic; needed when troubleshooting |
| Snapshot technical details (checksum, keys, template lineage notes) | Operator/debug |
| Report raw details / technical IDs | Debug |
| Source daily/weekly notes list | Supporting context, not primary edit path |
| Report blocks table on detail page (if retained) | Dense; full list page remains linked |
| Catalogue technical summary | Already partially collapsed today — keep collapsed |
| Internal timestamps / audit who-updated rows | Secondary metadata |
| Administrative / status-changing action group | Reduce accidental clicks (see Action Safety UX) |

Collapsed content must remain **present in DOM** (not removed). No “hide forever” without an expand path.

---

## Never hidden completely

These must remain visible without requiring expand:

1. Important warning that the report is finalized / locked  
2. Primary workflow actions (or clear empty-state equivalents)  
3. Work entries availability (section heading + empty/list state)  
4. PDF ready / active link readiness (compact indicators)  

If a control is disabled by backend rules, show disabled control + short reason — do not remove the affordance silently.

---

## Implementation preferences

1. Prefer native `<details class="tech-details">` (pattern already used in `show.php` / assembly preview).  
2. Use clear Russian `<summary>` labels (`Технические детали`, `Чек-лист готовности`, `Исходные еженедельные заметки`, `Административные действия`, …).  
3. Do not invent custom accordion JS unless accessibility or multi-panel exclusivity requires it.  
4. Preserve browser default expand/collapse; do not break print of expanded sections unexpectedly.  
5. CSS may style open/closed summary states; avoid `display:none` of entire critical warnings.  
6. Optional: `open` attribute only when operator-critical (e.g. finalized warning is a normal panel, not a details).

---

## Accessibility

- Summaries must be focusable and activatable via keyboard (native `<details>`).  
- Do not put sole copy of lock warnings inside collapsed details.  
- Status badges and readiness pass/fail remain text-readable (existing P0 sanitizer labels).  
- Collapsed tables/lists remain in HTML for screen readers when expanded.

---

## Regression guards

- P0: no reintroduction of normal-visible fixture markers.  
- Collapsed tech details may still contain residual raw/fixture text (accepted residual from P0).  
- Collapse policy does **not** authorize deleting fields from the page.

# I-SEO Report Hub — UI Russian Cleanup and i-SEO Brand Layer Implementation Result v0.1

**Status:** IMPLEMENTATION COMPLETE — local only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Russian Cleanup and i-SEO Brand Layer Implementation 03  
**Verdict:** `UI RUSSIAN CLEANUP BRAND PASS_WITH_MINOR_ISSUES`

---

## 1. Goal

Make manager/admin-visible secondary pages Russian, hide/humanize machine keys, remove stale «PDF export: not implemented», and apply a dedicated i-seo.su brand token layer — without DB/schema/share/PDF mutation.

---

## 2. What was translated

- Period detail / edit / form chrome
- Monthly report show / form
- Preview / print controls
- Report blocks list / form / show
- Weekly checkpoints list / form / show
- Snapshot export surface remaining English
- Controller `pageTitle` values for secondary pages
- Export / shares page titles humanized (no `snapshot-1-pdf-v2` in primary title)
- Header display name for fixture user → «Локальный тестовый пользователь»
- Fixture badge / footer → «Тестовые данные»

---

## 3. Machine keys / technical chrome

| Approach | Examples |
|----------|----------|
| Human label first | `executive_summary` → «Краткое резюме» |
| Muted / collapsed | `<details class="tech-details">`, `.tech-muted` |
| Status map | `finalized` → «Финализирован», PASS → «ОК» |
| Readiness keys | `preview_renderable` → «Предпросмотр собирается» |

Helper: `app/Support/UiLabels.php` + `ui_*` helpers in `helpers.php`.

Fixture content strings that literally contain `LOCAL_FIXTURE_ONLY` remain in DB fields (truthful fixture data); UI chrome treats the marker as «Тестовые данные».

---

## 4. Confusing notes fixed

- Removed / replaced stale note `Report blocks / PDF export: not implemented` on period detail.
- Snapshot/export surfaces describe PDF as available (create/download retained).
- Export detail: when active share count > 0 → «Активная ссылка уже есть. Полный URL показывается только при создании.»

---

## 5. Brand layer applied

| Token | Value |
|-------|-------|
| Accent / CTA | `#facc15` (hover `#eab308`) |
| CTA text | `#111111` |
| Dark sidebar | `#18181B` / `#1A1A1D` / `#27272A` |
| Font stack | `"Manrope", system-ui, …` (no webfont download) |
| Buttons | Yellow CTA, black text, pill `100px` |
| Text links | Darker gold `#a16207` for readability on light admin |
| Danger | Red retained for revoke / destructive |

Old demo red `#c8102e` removed as primary accent.

---

## 6. Pages / files changed (source)

- New: `app-source/app/Support/UiLabels.php`
- Updated: bootstrap, helpers, controllers (titles), views under periods/monthly/preview/blocks/weekly/snapshots/exports/dashboard/partials, `public/assets/css/app.css`

---

## 7. Runtime sync

Exact allowlist source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` (views/controllers/CSS/helpers/bootstrap only).  
**No** `.env` / storage / exports / vendor / WordPress sync.

---

## 8. Validation (local)

| Check | Result |
|-------|--------|
| `/health` | 200 |
| PHP `-l` on changed PHP | clean |
| Auth smoke (session inject; password unset) | authenticated pages 200, not login form |
| Russian chrome on target routes | present |
| `PDF export: not implemented` | absent |
| Brand CSS tokens | `#facc15`, Manrope, `#18181B`, pill |
| exports / shares / active / revoked | **4 / 7 / 1 / 6** (unchanged this wave) |
| Export 4 PDF checksum prefix | `a8c4d61c6216e8d70b19` (unchanged) |

Evidence (not committed):  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\ui-russian-cleanup-brand-layer-implementation-03\`

---

## 9. Explicitly out of scope / unchanged

- Nikita report template data model — **not** implemented
- Client PDF / template regeneration — **not** done
- Share create/revoke — **not** done (local active test share preserved)
- DB schema / migrations — **not** done
- WordPress / i-seo.su / production — **not** touched
- Push — **no**

---

## 10. Remaining UX / data debt

1. Backend readiness/action `reason` / `detail` strings still partly English (service layer).
2. Dashboard hero may still show a static «Активной ссылки нет» while local active share id 7 exists — display debt only.
3. Fixture Demo* titles and body text remain English fixture content.
4. Manrope is CSS stack only (no bundled webfont).
5. Optional Local Share QA Cleanup 01 for test share id 7.
6. Next template track: Nikita Report Template Data Model Charter 01.

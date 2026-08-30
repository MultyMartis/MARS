# I-SEO Report Hub — UI Cleanup Brand Fix 01 Result v0.1

**Status:** FIX COMPLETE — local only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Cleanup Brand Fix 01  
**Verdict:** `UI CLEANUP BRAND FIX PASS`

---

## 1. Goal

Close remaining Implementation 03 tails: dashboard active-share status accuracy, user-visible readiness/action `reason`/`detail` Russianization, brand layer verify, without share/PDF/DB mutation.

---

## 2. Dashboard active share fix

- `DashboardController` reads `ReportExportShareRepository::countByStatus()` (active count).
- Hero badge is no longer static «Активной ссылки нет».
- When active count > 0: «Активная ссылка есть» + hint «Ссылка создана ранее. Полный URL показывается только при создании.» + CTA «Открыть ссылки для клиента».
- When active count = 0: «Активной ссылки нет» + create guidance.
- When undetermined: «Статус ссылки не проверен».

---

## 3. Backend reason / detail Russianization

| Layer | Change |
|-------|--------|
| `UiLabels::message()` + `ui_message()` | Display-time map / regex humanization for readiness and action strings |
| `ReportFinalizationService` | Gate `detail` + action `reason` Russian |
| `ReportSnapshotService` | Create-gate `detail` Russian |
| `ReportExportShareService` / export controller | Eligibility / missing / forbidden user messages Russian |
| Views | monthly show, export show, shares index call `ui_message()` |

Machine keys remain humanized via existing `UiLabels` maps; technical keys stay collapsed where already muted.

---

## 4. Brand layer

Verified unchanged / still consistent:

- CTA `#facc15` / hover `#eab308`
- Dark surfaces `#18181B` / `#1A1A1D` / `#27272A`
- Manrope stack
- Danger red retained only for destructive styles

No broad redesign; no CSS file change required in this wave.

---

## 5. Runtime sync

Exact allowlist source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`:

- controllers: Dashboard, ReportExport
- services: Finalization, Snapshot, ExportShare
- support: UiLabels, helpers
- views: dashboard, monthly show, export show, shares index

**No** `.env` / storage / exports / vendor / WordPress / PDF sync.

---

## 6. Validation (local)

| Check | Result |
|-------|--------|
| PHP `-l` changed files | clean |
| `/health` `/login` | 200 |
| Authenticated GET smoke | 200 (session cookie `iseo_report_hub_session`) |
| Dashboard share badge | «Активная ссылка есть» (not static «нет») |
| Monthly readiness details | Russian (e.g. «Месячный отчет найден.») |
| Brand tokens in CSS | present |
| exports / shares / active / revoked | **4 / 7 / 1 / 6** |
| Active share | id **7**, label `test-first-link` |
| Export 4 checksum prefix | `a8c4d61c6216e8d70b19` unchanged |

Evidence (not committed):  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\ui-cleanup-brand-fix-01\`

---

## 7. Explicitly unchanged

- No share create/revoke
- No PDF regeneration / export artifact edit
- No Nikita report template data model
- No client PDF/template alignment
- No schema/migration
- No WordPress / i-seo.su / production
- No push

---

## 8. Remaining debt

1. Fixture Demo* titles/body remain English data content.
2. Manrope is CSS stack only (no bundled webfont).
3. Optional Local Share QA Cleanup 01 for test share id 7.
4. Next template track: Nikita Report Template Data Model Charter 01.
5. Some internal/public deny strings / audit English may remain where not manager-facing chrome.

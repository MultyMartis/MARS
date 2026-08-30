# I-SEO Report Hub — Demo Scenario Cleanup UI Polish Fix Result v0.1

**Date:** 2026-08-21  
**Verdict:** `DEMO SCENARIO CLEANUP UI POLISH PASS`  
**Scope:** local DB cleanup + rename + UI polish only  
**Not in scope:** production/host upload, PDF/export/share generation, browser-fill content

---

## Summary

Old fixture path **Demo Client / Demo SEO Project** (monthly reports **1** and **5**, related periods/blocks/entries/snapshots/exports/shares, and proven export files under runtime `storage/exports/`) was removed from local DB `iseo_report_hub_dev` after backup and ownership proof.

New demo scenario was renamed for display:

| Before | After |
|--------|-------|
| `ПРОВЕРКА.рa` | `ПРОВЕРКА.рф` |
| `SEO-продвижение ПРОВЕРКА.рa` | `SEO-продвижение ПРОВЕРКА.рф` |

Marker `MARS_DEMO_PROVERKA_20260821`, slug `proverka-demo`, URL `https://proverka.example`, July monthly **7**, August monthly **8**, and user `test@mail.ru` were preserved.

UI polish:

- Decode literal `\uXXXX` user names in display + login session write (root cause: prior session inject used ASCII JSON escapes).
- Dashboard is demo-aware: shows current client/project, honest PDF/share badges, no hard-coded Demo Client / export id 4.
- Reporting periods table: nowrap for period/status/dates/actions; monthly status in Russian (`Финализирован` / `В работе`).
- Status/role labels via `UiLabels` / `ui_role_label`.
- Seed tool updated to `.рф` strings for future `--status`/`--create`.

---

## Backup

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-scenario-cleanup-ui-polish-fix-01\backup\iseo_report_hub_dev-before-demo-cleanup-polish-20260821-141053.sql` |
| Size | 113003 bytes |
| SHA256 | `b1d484fe278947c65268ccee4b32c6423d8d62394684d297e0dba7b33db99a89` |

---

## Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-scenario-cleanup-ui-polish-fix-01\20260821-140904\`

Includes ownership/cleanup/rename/counts JSON, assertions, screenshot index, PNG `01`–`09` (+ post-login landing). **Not committed.**

---

## Safety

| Item | Result |
|------|--------|
| Production / host upload | **no** |
| New demo July/August content mutated beyond rename/scrub | **no** (display rename + internal note scrub only) |
| User `test@mail.ru` deleted | **no** |
| Token / password hash printed | **no** |
| PDF/export/share generated | **no** (old demo publication rows/files removed only) |

---

## Next action

`I-SEO Report Hub — Browser Filled Demo Report Pass 01`

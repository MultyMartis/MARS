# I-SEO Report Hub — Demo Scenario Browser Fill Follow-up Plan v0.1

**Status:** follow-up plan only — **no browser actions in this charter wave**  
**Date:** 2026-08-21  
**Next wave (after seed):** `I-SEO Report Hub — Browser Filled Demo Report Pass 01`  
**Depends on:** Demo User and Scenario Seed Implementation 01 complete

---

## 1. Goal

Log in as the demo SEO specialist and fill/adjust as much scenario content as possible **through the UI**, capturing screenshots and UI defects. Seed provides base entities; browser pass proves the product workflow for team training.

**Do not** merge this pass into Seed Implementation 01 by default.

---

## 2. Browser context

| Item | Value |
|------|-------|
| Browser | **Firefox Developer Edition** |
| Profile | `X:\MARS-Localhost\browser-profiles\firefox-developer\mars-research` |
| App URL | `http://iseo-report-hub.test/` |
| Login email | `test@reports.i-seo.local` |
| Password | `test` (local/demo only; do not log in evidence) |

Helper: MARS browser-clicking plugin if available; otherwise operator-assisted manual fill with the same profile.

---

## 3. Route / session plan

1. `/login` → authenticate as demo user  
2. Dashboard / home — confirm specialist context  
3. `/reporting-periods` — find `ПРОВЕРКА.рa` July + August  
4. Open July period → July monthly report  
5. Work entries list/create/edit (several)  
6. Report blocks edit (several)  
7. Monthly content edit if needed  
8. Assembly preview (optional; do not apply if it would fight finalized July)  
9. Client preview + print preview for **July**  
10. Open August monthly — edit partial content / entries  
11. Client preview for **August** (honest draft OK)  
12. Confirm field-help `?` icons on work entry / block / monthly forms  

---

## 4. Fill policy

| Prefer UI | Prefer leave seeded / skip |
|-----------|----------------------------|
| Work entry create/edit | Export / PDF / share |
| Block body polish | Demo Client report 1/5 |
| Monthly text tweaks | Host URLs |
| Status transitions short of PDF | Snapshot create (unless later approved) |
| Preview review | Printing tokens |

If July was seed-`finalized`, do **not** reopen unless admin session is intentional and logged. Prefer editing August + verifying July preview.

---

## 5. Issue capture protocol

On UI error / unexpected validation:

1. Screenshot viewport (+ console if relevant)  
2. Note URL, role, field, action  
3. Write issue note under Storage incoming for the fill wave  
4. Continue only on unaffected paths **or** STOP that path  
5. Open a fix charter later — **do not** silent DB bypass unless operator explicitly authorizes a temporary workaround **and** the bug remains logged  

---

## 6. Evidence

Folder:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\browser-filled-demo-report-pass-01\<timestamp>\`

Minimum screenshots:

1. Post-login dashboard  
2. Periods list with `ПРОВЕРКА.рa`  
3. July report detail  
4. July client preview  
5. August report detail  
6. August client preview  
7. Work entry form with `?` helps  
8. Block form with `?` helps  
9. Optional monthly form helps  

Also: short `BROWSER-FILL-ISSUE-LOG.md` (even if empty = none found).

---

## 7. Forbidden clicks

- PDF generation  
- Export create/regenerate  
- Share token create/copy/print  
- Production / `reports.i-seo.su`  
- Delete/archive Demo Client report 1 or 5  
- Broad DB cleanup from browser wave  

---

## 8. Acceptance (browser pass)

- Demo user login works  
- Both months visible and editable per their status rules  
- Content looks like a real SEO month for training  
- Helps visible where expected  
- Issues logged or none  
- No PDF/export/share mutation  
- Report 1/5 unchanged  

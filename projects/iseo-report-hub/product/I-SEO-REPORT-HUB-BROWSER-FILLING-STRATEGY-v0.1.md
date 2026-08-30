# I-SEO Report Hub — Browser Filling Strategy v0.1

**Status:** planning only — **no browser automation / POST in this wave**  
**Date:** 2026-08-21  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01

---

## Browser context (mandatory for fill pass)

| Item | Value |
|------|-------|
| Browser | **Firefox Developer Edition** |
| Profile | `X:\MARS-Localhost\browser-profiles\firefox-developer\mars-research` |
| App URL | `http://iseo-report-hub.test/` |
| Helper | MARS browser-clicking plugin **if available** in the environment; otherwise operator-assisted manual fill with same profile |

---

## Principle: UI-first content, seed-only base

Fill **as much as possible through the browser** after a minimal controlled seed.

### Controlled seed allowed only for

1. User `Тест Проверочнов` / email `test@reports.i-seo.local` / role `seo_specialist`
2. Client + project + site `ПРОВЕРКА.рa` (no client/project UI CRUD in current routes)
3. Optionally: two reporting periods + empty monthly report shells if period create UI cannot bind without seeded project
4. Optional light weekly checkpoint shells

### Browser (preferred) for

- Login as demo user
- Creating/editing work entries
- Creating/editing report blocks
- Editing monthly report text fields
- Assembly preview apply (if used)
- Client preview / print preview review
- Status transitions short of PDF/export/share
- Discovering UX bugs

---

## Recommended session flow

1. Start Firefox Developer with **mars-research** profile.
2. Open `/login` → email `test@reports.i-seo.local` / password `test`.
3. Confirm dashboard shows specialist context (not admin-only chrome surprises).
4. Open new project periods list / reporting periods filtered to `ПРОВЕРКА.рa`.
5. **Month 1 (2026-07):**
   - Add work entries (catalogue + manual)
   - Add/edit blocks
   - Fill monthly fields
   - Run assembly if helpful
   - Open preview; optionally finalize **only** if charter for seed pass authorizes it
6. **Month 2 (2026-08):**
   - Partial work entries through ~day 21 narrative
   - Leave gaps intentional
   - Preview as draft / in progress
7. Capture screenshots (see list below).
8. Log any UI errors immediately — **do not silently bypass**.

---

## Dangerous clicks — do not

| Action | Rule |
|--------|------|
| PDF generation | Frozen unless later approved |
| Export create/regenerate | Frozen |
| Share token create/copy | Frozen — never print tokens |
| Production / host URLs | Out of scope |
| Admin reopen of unrelated Demo Client reports | Avoid unless fixing regression |
| Delete / archive Demo Client report 1 or 5 | Forbidden |

---

## Issue capture protocol

On UI error or unexpected validation:

1. Screenshot full viewport (+ console if relevant)
2. Note URL, user role, exact field, request method if known
3. Write a short issue note under Storage incoming for the fill wave
4. **STOP** the fill for that path or continue only on unaffected paths
5. Open a **fix charter/implementation** wave — do not hack DB to hide the bug unless operator explicitly authorizes a temporary seed workaround **and** the bug remains logged

---

## Validation screenshot checklist

Evidence folder (future fill wave): under  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\browser-filled-demo-report-pass-01\<timestamp>\`

Required captures:

1. Login as test user (post-login dashboard)
2. Dashboard / home
3. Project / reporting-period list showing `ПРОВЕРКА.рa`
4. Month 1 report detail
5. Month 1 client preview
6. Month 2 in-progress detail
7. Month 2 client preview (draft honesty OK)
8. Work entry form **with field-help `?` icons** (after Field Help wave)
9. Block edit form **with field-help `?` icons**
10. Optional: monthly content form with helps

---

## Hybrid path summary

```
backup DB
  → seed user + client/project/site (+ optional empty periods/monthlies)
    → browser login as test
      → fill work entries / blocks / texts
        → screenshot + issue log
          → no PDF/export/share
```

If browser cannot create periods for the new project: extend seed — still fill **content** via UI.

---

## Acceptance for this strategy doc

- Firefox Developer + mars-research profile specified
- Seed vs UI split clear
- Issue capture + forbidden actions clear
- Screenshot list defined

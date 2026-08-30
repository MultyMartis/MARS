# i-SEO Report Hub — Screenshot QA P0 Safety & Acceptance v0.1

**Wave pair:** Screenshot QA Fix Charter 01 → Screenshot QA P0 Fix Implementation 01  
**Date:** 2026-08-21

---

## Safety constraints (mandatory)

| Constraint | Rule |
|------------|------|
| DB mutation | **None** in P0 implementation (no content UPDATE to “fix” junk in place) |
| Export / share / PDF | **No** mutation; **no** regeneration |
| Export 4 | **Frozen** — do not overwrite artifact or row |
| Share tokens | **Do not print**; do not open public `/share/report/{token}` for capture |
| POST | **None** except optional login if session injection unavailable; prefer GET + session injection |
| Production | **None** — local `iseo-report-hub.test` only |
| Runtime sync | Exact allowlisted files only, Model A source → runtime, when implementation authorizes |
| Secrets | No `.env` edits; no passwords/hashes/tokens in docs |

---

## Acceptance criteria

### Visual / content (normal view)

1. **Fixture markers:** P0 pages do not show `LOCAL_FIXTURE_ONLY` / `MARS_FIXTURE` in normal (non-collapsed) UI.
2. **Test garbage:** Client preview does not show `Updated body`, `Risks body`, or numeric-only junk bodies; calm empty/demo text instead.
3. **Buttons:** Reporting periods action column labels are readable (no yellow-on-yellow empty pills).
4. **404:** Russian friendly page; CTA `На главную`; router internals not in normal view.

### Integrity

5. DB counts / key demo IDs unchanged vs documented baseline in implementation closeout.
6. Export 4 + shares + PDF artifacts unchanged.
7. Internal technical details may remain **only** where appropriate (collapsed tech panels), not as primary chrome.

### Evidence

8. Before/after screenshot evidence retained under Storage (Capture 01 = before; new run folder = after).
9. Closeout lists changed app-source paths and confirms forbidden areas untouched.

---

## Non-acceptance (examples)

- “Fixed” by writing cleaned text into MySQL without a separate cleanup charter.
- Regenerating export/PDF “to match preview”.
- Leaving English Phase 1A router text on 404.
- Shipping CSS that still hides button labels.

---

## Operator confirmations already in force

- PDF/export alignment deferred until after UI polish.
- Automated Screenshot Capture 01 is the **before** baseline for this P0 pack.

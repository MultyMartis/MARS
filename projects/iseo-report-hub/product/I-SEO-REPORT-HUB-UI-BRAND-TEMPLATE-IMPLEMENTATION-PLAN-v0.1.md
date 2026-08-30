# I-SEO Report Hub — UI Brand Template Implementation Plan v0.1

**Status:** PLAN ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Screenshot QA, Brand Style and Nikita Templates Discovery 01

---

## 1. Immediate next wave

**Name:** `I-SEO Report Hub — UI Russian Cleanup and i-SEO Brand Layer Implementation 03`

**Goal:** Make all manager-visible hub pages Russian and apply a dedicated i-seo.su brand token layer, without DB/schema/share/PDF mutation.

---

## 2. In scope (Impl 03)

1. Translate secondary CRUD/preview/blocks/period/monthly/snapshot chrome to Russian (dictionary + inventory).  
2. Hide machine keys on manager surfaces; collapse technical facts under «Технические детали».  
3. Replace `#c8102e` accent with `#facc15` (+ dark ink on CTA); optional sidebar darken toward `#18181B`.  
4. Introduce Manrope font for UI.  
5. Improve primary buttons (yellow CTA; consider pill radius for primary only).  
6. Fix stale copy («PDF export: not implemented»).  
7. Clarify fixture badge («Тестовые данные») without removing Demo* names.  
8. Preserve routes, auth, DB rows, exports, shares, PDF bytes.  
9. Exact-path source → runtime sync allowlist only.  
10. Screenshot / HTTP GET evidence + operator manual QA.

---

## 3. Out of scope (Impl 03)

- DB migrations / new columns / new block types  
- Nikita taxonomy schema implementation  
- PDF regeneration / client-report HTML redesign  
- Share create / revoke / token operations  
- WordPress / i-seo.su / WPilot writes  
- Demo prototype HTML edits  
- Production deploy  

---

## 4. Acceptance criteria (Impl 03)

| # | Criterion |
|---|-----------|
| 1 | All inspected manager pages show Russian primary chrome (no EN buttons/headings on inventory list, except brand mark INTLSEO / Email if kept) |
| 2 | No raw `executive_summary`-style keys on manager surfaces |
| 3 | Snapshot/export keys not in primary titles; available under technical details |
| 4 | Brand tokens applied: yellow accent + Manrope; shell remains usable |
| 5 | No DB/schema/share/PDF artifact mutation |
| 6 | `/health` still 200; auth flows still work |
| 7 | Smoke evidence + operator manual QA pass |

---

## 5. Suggested file allowlist (Impl 03)

See [UI Screenshot QA Inventory §7](I-SEO-REPORT-HUB-UI-SCREENSHOT-QA-INVENTORY-v0.1.md). Core: Views under reporting-periods, monthly-reports, report-preview, report-blocks, weekly-checkpoints, report-snapshots; polish exports/shares titles; `public/assets/css/app.css`; possibly `app.js` only if font loader needed.

---

## 6. Later sequence

| Order | Wave | Purpose |
|-------|------|---------|
| 1 | **UI Russian Cleanup and i-SEO Brand Layer Implementation 03** | Copy + brand tokens |
| 2 | Optional **Local Share QA Cleanup 01** | Revoke/document local test share id 7 if desired |
| 3 | **Nikita Report Template Data Model Charter 01** | Fields/blocks/profiles from Nikita + architecture |
| 4 | **Client Report Template Visual Alignment Charter 01** | PDF/HTML client chrome |
| 5 | Template / data implementation wave(s) | Schema + UI + export (chartered separately) |

---

## 7. Dependencies

| Dependency | Status |
|------------|--------|
| Demo Visual Shell Impl 02 | Complete |
| Russian UX dictionary | Exists — extend for secondary pages in Impl 03 |
| Brand tokens | Extracted in Brand Discovery v0.1 |
| Nikita corpus | Located — **not** schema-ready for Impl 03 |

---

## 8. Risks / mitigations

| Risk | Mitigation |
|------|------------|
| Yellow accent low contrast on light bg for links | Use dark text on yellow buttons; for text links use darker gold or keep underline + weight |
| Over-translating admin forensic labels | Keep EN codes only inside collapsed technical details |
| Scope creep into Nikita schema | Hard stop — charter 01 separate |
| Accidental PDF regen | Explicit forbid in charter |

---

## 9. Operator decisions needed before/during Impl 03

1. Confirm **light admin + yellow accent** (recommended) vs full dark admin.  
2. Confirm fixture Demo* names stay visible.  
3. Decide whether Local Share Cleanup runs before or after Impl 03 (default: **after** or parallel optional).

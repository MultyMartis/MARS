# Website Factory Font and Layout Stability Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Not:** automated CLS monitor or font loader runtime.

**Authority:** [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) · [production-hardening-rules-v1.md](production-hardening-rules-v1.md)

---

## 1. Objective

Prevent observable:

- FOUT / FOIT;
- font-induced CLS;
- icon-induced CLS;
- image-induced CLS;
- late unstyled flash from CSS load order.

Do **not** mask instability with global `visibility: hidden` or `body { opacity: 0 }` unless operator-approved and documented.

---

## 2. Preferred font delivery

```text
local WOFF2 (when licensed project files exist)
+ correct @font-face
+ only required weights
+ preload for critical above-fold files
+ stable fallback stack
+ explicit font-family from first paint
```

When only external Google Fonts is permitted:

- `preconnect` to required origins;
- load in `<head>` before main CSS;
- request only weights in active use;
- `display=swap` (or documented alternative);
- document remaining network risk as `PARTIAL · EXTERNAL FONT DELIVERY RISK`.

---

## 3. Icons and images

- Font Awesome: controlled shared integration; reserve icon box dimensions in existing CSS; no duplicate FA CSS.
- Raster images: `width` and `height` attributes from intrinsic asset dimensions when layout allows.
- Main CSS in `<head>`; no stylesheet injection via JS for primary layout.

---

## 4. Gate

```text
[ ] Font delivery audited
[ ] Critical font discovery occurs early
[ ] Duplicate font requests absent
[ ] Critical weights limited
[ ] Font-display strategy documented
[ ] Above-fold shift tested
[ ] Images/icons reserve dimensions
[ ] CSS loads before render
```

**Fail state:** `FONT STABILITY GATE — FAIL` (blocking only when task mandates stability pass)

---

## 5. Report fields

```text
Font delivery method:
Critical fonts:
Font preloads:
Font-display strategy:
FOUT observed before:
FOUT observed after:
Layout shifts observed before:
Layout shifts observed after:
Remaining load stability risks:
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — font/layout stability production law |

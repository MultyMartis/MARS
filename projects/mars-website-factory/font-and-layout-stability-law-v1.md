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
local WOFF2 (default for operator-approved production fonts)
+ correct @font-face
+ only required weights
+ preload for critical above-fold files
+ font-display: block when operator requires zero visible font switch
+ stable fallback stack
+ explicit font-family from first paint
```

**Default Website Factory approach:** For operator-approved production fonts, **local WOFF2 delivery** is the default when external font swapping produces visible FOUT.

**Operator Visual Font Gate (mandatory):** Automated CLS and screenshots do **not** override an operator-observed FOUT. Font stability is approved only after **operator visual confirmation**. Do not report `visible_fout: NOT_OBSERVED` as fully resolved while the operator still sees a font switch.

When only external Google Fonts is permitted:

- `preconnect` to required origins;
- load in `<head>` before main CSS;
- request only weights in active use;
- `display=swap` only when operator accepts visible fallback risk;
- document remaining network risk as `PARTIAL · EXTERNAL FONT DELIVERY RISK`;
- **do not** claim zero FOUT while operator reports visible swap.

**Forbidden masking:** global `visibility: hidden`, `body { opacity: 0 }`, waiting for `document.fonts.ready` before showing the page, or loader screens to hide FOUT.

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
| 2026-06-23 | v1.1 — local WOFF2 default; operator visual font gate; swap not zero-FOUT; masking forbidden (FP-0002 correction) |

# FP-0002 v2 — Foundation Components Report v1

**Task:** FP-0002 v2 FOUNDATION START · FND-04–FND-08  
**Date:** 2026-06-22

---

## 1. Component file map

| Phase | File | Classes |
|-------|------|---------|
| FND-04 Buttons | `src/scss/components/_button.scss` | `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.btn--small`, `.btn--large` |
| FND-05 Forms | `src/scss/components/_form.scss` | `.form-input`, `.form-textarea`, `.form-select`, `.form-label`, `.form-field.is-error` |
| FND-06 Checkbox/Radio | `src/scss/components/_checkbox-radio.scss` | `.control`, `.control__input`, `.control-group` |
| FND-07 Cards | `src/scss/components/_card.scss` | `.card`, `.card-grid` |
| FND-08 Utilities | `src/scss/utils/_utilities.scss` | `.visually-hidden`, `.sr-only`, `.flow`, `.flow--sm`, `.flow--lg` |

---

## 2. Button system (v3 §8.1)

| Variant | Height | Padding-x | Radius | Font | States |
|---------|--------|-----------|--------|------|--------|
| Primary default | 44px | 32px | 30px | 16/500 lh20 | hover darken 8%, focus ring, disabled 50% opacity |
| Small | 40px | 24px | 30px | 14/500 | same |
| Large | 48px | 32px | 30px | 16/500 | same |
| Secondary | 44px | 32px | 30px | 16/500 | elevated fill #F1F5F9, border #CBD4E0 |
| Outline | 44px | 32px | 30px | 16/500 | transparent, accent border |

**Source:** Production Standards v3 §8.1 · M2 Spec v2 M2-B-012 (secondary/outline engineering).

---

## 3. Form foundation (v3 §8.2)

| Control | Spec | States |
|---------|------|--------|
| Input | h 48px, pad 16×12, radius 10px, border `#BCC6D5` | default, focus, error, disabled |
| Textarea | min-h 128px, pad 16px | same |
| Select | native styled, h 48px | same |
| Label gap | 8px below label | `space-2` |

---

## 4. Checkbox / Radio

Native inputs with `accent-color: #B3261E`, focus-visible outline, disabled opacity. Production-ready baseline — custom SVG skins **not** in v3; deferred.

---

## 5. Card foundation (v3 §8.3)

| Property | Value |
|----------|-------|
| Padding | 24px |
| Border | 1px `#CBD4E0` |
| Radius | 30px |
| Shadow | none |
| Grid gap | 24px, 3-col desktop / 1-col mobile |

Generic only — no service/specialist page cards.

---

## 6. Utilities (approved only)

| Utility | Purpose |
|---------|---------|
| `.visually-hidden` / `.sr-only` | A11y off-screen text |
| `.flow` / `.flow--sm` / `.flow--lg` | Vertical rhythm helpers (16/8/24px) |

No Tailwind-style utility framework.

---

## 7. Explicit exclusions (task scope)

| Item | Status |
|------|--------|
| Header | **NOT CREATED** |
| Footer | **NOT CREATED** |
| Hero | **NOT CREATED** |
| Business forms | **NOT CREATED** |
| Page sections | **NOT CREATED** |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |

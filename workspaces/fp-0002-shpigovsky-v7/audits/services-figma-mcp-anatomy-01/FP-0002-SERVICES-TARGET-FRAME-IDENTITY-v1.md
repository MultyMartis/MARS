# FP-0002 — Services Target Frame Identity v1

**Date:** 2026-06-26  
**Local design authority:** `Spig_v1.2.fig` @ SHA-256 `BAE5D91C…DE3041`  
**Live MCP verification:** **BLOCKED** (see connectivity doc)

## Candidate frames (offline parse + PNG cross-check)

| Variant | Figma file | Page / canvas | Frame name | Node ID | Dimensions | Visible | PNG match |
| ------- | ---------- | ------------- | ---------- | ------- | ---------: | ------: | --------- |
| Desktop | `Spig_v1.2.fig` (local) | Page 2 | `Услуги хаб` | `1:1310` | 1437 × 11999 | Yes | **MATCH** — `APPROVED-DESKTOP-REFERENCE.png` |
| Mobile | `Spig_v1.2.fig` (local) | Page 13 | `Услуги хаб - моб` | `1:4624` | 380 × 17611 | Yes | **MATCH** — `APPROVED-MOBILE-REFERENCE.png` |

## Alternate names checked

| Name | Found | Notes |
| ---- | ----- | ----- |
| `Услуги общая` | No exact frame name | Operator PNG label; canonical frame = `Услуги хаб` |
| `Услуги хаб - mob` | Typo variant only | Correct mobile name = `Услуги хаб - моб` |

## Identity evidence

1. **Dimensions** match page inventory (`1437×11999` desktop, `380×17611` mobile).
2. **Distinctive text** in hero overlay: eyebrow `Заболевания, которые мы лечим`, H1 `Лечение и профилактика` (nodes `1:1355`, `1:1356`).
3. **Four category blocks** + program + founder + comfort + mid CTA + FAQ + footer present in child order.
4. **Approved PNG** visual order matches parsed child sequence (hero → breadcrumbs → tab nav → categories → …).

## Ambiguity

```text
TARGET FRAME IDENTITY — NOT AMBIGUOUS (offline)
LIVE MCP CONFIRMATION — PENDING (cloud fileKey unknown)
```

No competing desktop/mobile hub frames with same dimensions and hero copy were found in `Spig_v1.2.fig`.

## Hidden / non-visible node note

Frame `1:1374` (`2 - Дом - вступление`) is a **direct child** of `1:1310` in the `.fig` tree but **not visible** on approved desktop PNG between hero and first category. Status: **NOT_PRESENT_IN_TARGET_FRAME (visible)** — treat as hidden/legacy sibling, not page anatomy for implementation.

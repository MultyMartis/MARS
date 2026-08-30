# I-SEO Report Hub — Client Report Visual Direction v0.1

**Status:** CHARTER / VISUAL DIRECTION — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01  
**Brand baseline:** [I-SEO-REPORT-HUB-ISEO-BRAND-STYLE-DISCOVERY-v0.1.md](I-SEO-REPORT-HUB-ISEO-BRAND-STYLE-DISCOVERY-v0.1.md)  
**Prior export styling:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md) — superseded **for client document look**; keep A4/print safety ideas.

Admin UI may keep the dark sidebar. **Client report must not.**

---

## 1. Product look

A clean professional **i-SEO SEO report**:

- light canvas, generous whitespace;
- clear typographic hierarchy;
- printable / PDF-friendly / share-friendly;
- yellow as accent, not a yellow page;
- red only for truly critical risk content, never as default section chrome.

Not: admin dashboard, debug dump, raw block table, dark marketing landing, SaaS card farm.

---

## 2. Design tokens

| Token | Value | Use |
|-------|-------|-----|
| `--cr-accent` | `#facc15` | Rules, cover bar, CTA if any |
| `--cr-accent-dark` | `#eab308` | Hover / print-safe darker rule |
| `--cr-ink` | `#18181B` | Headings, body |
| `--cr-ink-muted` | `#52525B` | Meta, empty notes, footer |
| `--cr-canvas` | `#f5f6f8` | Screen page background |
| `--cr-paper` | `#ffffff` | Report sheet |
| `--cr-line` | `#E4E4E7` | Hairlines |
| `--cr-ok` | `#166534` | Optional positive left rule (rare) |
| `--cr-attention` | `#A16207` | Risks default (calm amber/brown), not alarm red |
| `--cr-critical` | `#991B1B` | Only if body copy is explicitly critical |
| `--cr-danger` | `#dc2626` | **Forbidden** as default report styling |
| Font | `"Manrope", "Segoe UI", Arial, sans-serif` | Headings + body |
| Max width (screen) | `800px` / `50rem` | Centered paper |
| Page | A4 | `@page { size: A4; margin: 16mm 14mm; }` |
| Radius | `0–8px` | Document, not pill cards for body |
| Shadow | none or very light screen-only | **none** in print/PDF |

Manrope: self-host or already-loaded hub font if present; **no** remote Google Fonts inside **export HTML/PDF** (offline/print). Preview may use the same local/self-hosted stack as admin if already in `app.css`. If Manrope is not local, Implementation 01 may use the system stack **plus** the yellow/dark tokens rather than adding a package download.

---

## 3. Layout

```
[ optional no-print operator strip ]
┌─────────────────────────────────────┐
│ yellow 4–6px top accent bar         │
│ i-SEO          SEO-отчёт            │
│ Title                               │
│ Client · Project · Site             │
│ Period · Status · Date              │
├─────────────────────────────────────┤
│ H2 section … body                   │
│ … six IA sections …                 │
├─────────────────────────────────────┤
│ Footer: i-SEO · local demo if local │
└─────────────────────────────────────┘
```

- No sidebar, no topbar, no admin footer.
- One H1 (report title).
- Sections are stacked articles, not a grid of debug cards.
- Cover is part of page 1, not a separate marketing hero.

---

## 4. Typography

| Element | Guidance |
|---------|----------|
| H1 | 1.75–2rem, weight 700, ink |
| H2 | 1.15–1.25rem, weight 700, small yellow left rule **or** hairline above — not both heavy |
| Body | 1rem, line-height 1.55–1.65 |
| Meta | 0.85–0.9rem, muted |
| Lists | Comfortable spacing; `- ` bodies already exist — render as `<ul>` when lines start with `- ` if cheap; else `nl2br` is acceptable for Impl 01 |

Do not use Georgia/serif for the client template (current export uses Arial; move toward Manrope/system sans).

---

## 5. Components

| Component | Behaviour |
|-----------|-----------|
| `client-report` sheet | White paper on grey canvas (screen); white in print |
| Cover meta | Definition list or simple rows; no `<code>` |
| Status badge | Neutral pill: draft = muted grey; finalized = dark ink on pale yellow, not red |
| Section | H2 + body; no type/status/key chips |
| Empty note | Muted italic/plain, no amber/red banner |
| Risk section | Amber/brown left rule (`--cr-attention`); body stays black |
| Critical risk | Left rule `--cr-critical` only when a future flag exists; **not** default for `risks_and_blockers` |
| Table (future) | Collapse, 1px borders, header `#f5f5f5`; none required now |
| Footer | Small muted identity; local demo label in local env only |

---

## 6. Accent usage

Yellow is for:

- 4–6px cover bar;
- H2 left accent (3px) **or** a thin gold rule under the brand line;
- finalized badge background (pale);
- optional print-hidden «Печать» button on preview.

Yellow is **not** for:

- full-width yellow section backgrounds;
- every card border;
- body text.

---

## 7. Print / PDF-safe CSS

- `@page` A4; avoid widths > printable area.
- `print-color-adjust: exact` for the yellow bar (may still flatten in some engines — acceptable).
- `break-inside: avoid` on sections.
- Hide `.no-print` (operator strip, flash, buttons).
- No `position: fixed` chrome.
- No `app-sidebar` in this layout at all (do not rely on print-hiding the admin shell).
- Embedded CSS for export HTML (no `/assets/css/app.css` dependency in artifacts).
- No scripts, no remote CSS/images in export HTML.

Preview may share a `client-report.css` (or a dedicated section) **and** a renderer-generated embedded copy for export later. Impl 01 can ship screen+print CSS for preview only.

---

## 8. Mobile / share

Public share today is a **PDF download**, not a responsive web article. Still:

- preview should be readable at 320px (single column, 12–16px side padding);
- future HTML share (if ever) would reuse the same sheet.

Do not build a mobile app chrome.

---

## 9. What not to show

- Admin sidebar / topbar / site footer.
- Edit, apply, snapshot, block-CRUD, assembly controls.
- Source ids, checksums, `block_key`, weekly dumps, JSON diagnostics.
- `LOCAL_FIXTURE_ONLY`, «Internal report export», raw `iseo_default_v1` in the visible body.
- Fake KPI cards.
- Red banners for empty/manual sections.

---

## 10. Relation to `iseo_default_v1`

Keep template **id** `iseo_default_v1` for metadata compatibility unless a later charter bumps version.

Implementation may introduce **visual revision inside the same id** only for **newly generated** artifacts. Issued HTML/PDF **3/4** stay frozen. A version bump (`v2` or `template_version=2`) is **optional later** when first regenerating PDF; not required for preview-only Impl 01.

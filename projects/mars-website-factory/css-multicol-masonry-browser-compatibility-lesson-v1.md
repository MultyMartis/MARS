# CSS Multicol Masonry: Chrome/Firefox compatibility

**ID:** `WF-CSS-MULTICOL-MASONRY-BROWSER-COMPAT`  
**Status:** **documented** — cross-project Website Factory frontend lesson from WPilot footer work on dev.gktriumph.ru.  
**Not:** runtime enforcement, automated browser testing, or modification of WPilot plugin or live site CSS.

**Date:** 2026-06-17  
**Evidence:** Footer menu layout work — Firefox rendered CSS multi-column footer menu correctly; Chrome rendered it incorrectly until `display` was corrected.

**Related:** [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §10 · [frontend-production-rules-v0.md](frontend-production-rules-v0.md) · [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md)

---

## 1. Problem

CSS multi-column masonry-like layout rendered differently in **Chrome** and **Firefox**.

During footer menu group layout work, Firefox showed the intended column flow. Chrome showed incorrect grouping/break behavior with the same markup and column container.

**Do not treat Firefox success as proof for Chrome.**

---

## 2. Bad pattern

```css
.wsp_footer_menu__group {
	display: inline-block;
}
```

`inline-block` on column group wrappers is **not** browser-safe for CSS multicol masonry-style grouping. In this incident Firefox looked correct; Chrome did not.

---

## 3. Working pattern

```css
.wsp_footer_menu__group {
	display: block;
	break-inside: avoid;
	-webkit-column-break-inside: avoid;
	page-break-inside: avoid;
}
```

Full working context from the incident (width and spacing preserved):

```css
.wsp_footer_menu__group {
	display: block;
	width: 100%;
	break-inside: avoid;
	-webkit-column-break-inside: avoid;
	page-break-inside: avoid;
	margin-bottom: 50px;
	min-width: 0;
	max-width: 100%;
}
```

---

## 4. Rule

For CSS multi-column masonry-style grouping:

| Do | Do not |
|----|--------|
| Test **Chrome** and **Firefox** separately | Assume one engine proves the other |
| Prefer **`display: block`** for column group wrappers | Default to **`display: inline-block`** without verified reason |
| Keep **`break-inside: avoid`** (+ vendor prefixes) on group wrappers | Rely on column count alone to keep groups intact |

Use `inline-block` only when there is a **documented, verified** reason and both engines pass QA.

---

## 5. QA requirement

Any CSS multicol masonry / footer / link-cloud layout **must** be checked in:

| Browser | Scope |
|---------|--------|
| **Chrome desktop** | Column groups, breaks, link stacks |
| **Firefox desktop** | Same — do not skip after Chrome-only pass |
| **Mobile Chromium** | Collapse / stack behavior at project breakpoints |

**REPORT line (when multicol footer or link-cloud is in scope):**

```text
CSS MULTICOL MASONRY BROWSER QA — PASS (Chrome + Firefox + mobile Chromium) | partial (list) | FAIL | SAFE UNKNOWN
```

---

## 6. Scope

Applies to:

| Lane | Examples |
|------|----------|
| **Website Factory** | Gulp static footers, link clouds, multicol nav groups |
| **MARS Forge** | Forge WordPress delivery footers |
| **WPilot** | Footer menu edits via WPilot-managed CSS |
| **Legacy WordPress / The7 / WPBakery** | Theme and builder footer column layouts |
| **Any footer / menu masonry-like layout** | Multi-column `column-count` / `columns` groupings |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-17 | v1 — lesson filed from dev.gktriumph.ru WPilot footer multicol incident |

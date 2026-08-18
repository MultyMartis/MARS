# Forge WordPress — Accessibility baseline v1

**ID:** FW-S-37  
**Status:** ACTIVE — CANONICAL DEFAULT (minimum production acceptance)  
**Date:** 2026-08-18  
**Not:** a WCAG certification, audit product, or legal claim.

This is the **minimum** layer a WP Forge site must pass before launch. Deeper audits are project/charter work.

---

## 1. Required

| Area | Minimum |
|------|---------|
| Heading hierarchy | One H1 per view; no skipped levels in main content |
| Labels | Every input has a visible `<label>` or equivalent `aria-labelledby` |
| Keyboard | All interactive controls reachable; logical tab order |
| `:focus-visible` | Visible; not `outline: none` without replacement |
| Menu | Parent link usable; separate expand control on mobile; Escape closes; ARIA expanded |
| Accordions | `<button>` + `aria-expanded` + `aria-controls`; one open in group unless design says otherwise |
| Modals | Focus trap **with** Escape + return focus; no trap if modal is broken |
| Form errors | Associated with fields; not color-only |
| Button vs link | Navigation = link; action = button |
| Image alt | Meaningful alt or empty alt if decorative |
| Reduced motion | See §2 |
| Target size | Interactive targets usable on touch (do not rely on 24×24 icons alone) |
| No keyboard traps | Except a **working** modal |

---

## 2. Reduced motion standard

Decorative motion, parallax, and auto-advancing sliders **must** honor `prefers-reduced-motion: reduce`.

| Feature | Fallback |
|---------|----------|
| Parallax | Static position; no scroll-linked transform |
| Decorative CSS animation | Disable or one-shot fade ≤ design token |
| Autoplay slider | Stop autoplay; show first slide; keep manual controls |
| Marquee / looping | Static |

Future projects must not discover this at launch. Record the fallback in the component inventory.

---

## 3. Out of scope unless chartered

Full WCAG 2.2 AAA, screen-reader scripted certification, legal accessibility statements, third-party widget a11y (cookie banners) — list as project risk, do not fake PASS.

---

*FW-S-37 v1.*

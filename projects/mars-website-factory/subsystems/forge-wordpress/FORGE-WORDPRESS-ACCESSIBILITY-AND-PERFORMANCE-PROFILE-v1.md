# Forge WordPress — Accessibility and Performance Profile v1

**Document type:** WV8 profile specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

---

## 1. Project profile mechanism

Each project declares in VALIDATION-PLAN:

- `a11y_profile`: `baseline` | `enhanced`
- `perf_profile`: `baseline` | `enhanced`
- `hosting_constraints`: shared hosting notes (caching, script limits)

**No fixed global numeric thresholds** — targets are project-scoped.

---

## 2. Accessibility

| Check | Method | Class |
|-------|--------|-------|
| Automated axe rules | axe-playwright | Blocker (critical) / Warning |
| Keyboard navigation | Playwright + manual | Blocker on primary nav/forms |
| Semantic HTML | Review + lint | Warning |
| Form labels | axe + review | Blocker |
| Focus visibility | Manual + CSS review | Warning |
| Contrast | axe | Warning — waiver on brand with approval |
| ARIA misuse | Review | Warning |

### Human review (always)

- Screen reader spot-check on hero, nav, primary form
- Admin editor output sample

---

## 3. Performance

| Check | Method | Class |
|-------|--------|-------|
| Lighthouse performance | CLI on local | Target — project-defined |
| LCP / CLS / INP | Lighthouse | Advisory on shared host |
| Image optimization | Asset audit | Warning |
| Asset weight (CSS/JS) | Manifest | Warning |
| Third-party scripts | Inventory | Review |
| Caching compatibility | `.htaccess` / host notes | Advisory |
| Admin performance | Manual | Warning |

### Shared hosting reality

Beget-class hosts may not reproduce local Lighthouse scores — **waiver path** documented in WV8 report.

---

## 4. Classification

| Class | Action |
|-------|--------|
| **Blocker** | Must fix before WV9 |
| **Project target** | Tracked; fix or waive with reason |
| **Warning** | Document in manifest known limitations |
| **Human review** | Required for waivers |

---

## Related

- [standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md)
- [FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md)

---

*A11y and performance profile v1.*

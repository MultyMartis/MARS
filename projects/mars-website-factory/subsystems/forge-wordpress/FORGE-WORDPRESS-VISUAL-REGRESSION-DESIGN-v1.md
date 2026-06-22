# Forge WordPress — Visual Regression Design v1

**Document type:** Visual validation workflow  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

---

## 1. Process flow

```text
Approved Website Factory reference (dist/ or VL-approved captures)
  → normalized capture (reference baselines)
  → WordPress local capture (same viewports)
  → automated comparison (pixel/layout metrics)
  → visual validator review
  → operator sign-off (PIXEL_PERFECT — BLOCKING)
```

---

## 2. Source screenshots

| Source | When |
|--------|------|
| Static `dist/*.html` served locally | Pre-WP or parallel track |
| Factory VL-approved reference set | Preferred authority |
| Re-capture after frontend change | Invalidates WP baselines |

Storage: `C:\AI MARS STORAGE\forge-wordpress\{FP-ID}\visual-baselines\`

---

## 3. Viewport matrix (canonical)

| Viewport | Width | Priority |
|----------|-------|----------|
| Desktop | 1440 | **Required** |
| Desktop narrow | 1024 | **Required** |
| Tablet | 768 | Recommended |
| Mobile | 390 | **Required** |

Per-page matrix documented in project VALIDATION-PLAN (FW-T-16).

---

## 4. Capture normalization

| Factor | Policy |
|--------|--------|
| **Browser** | Chromium (Playwright) — baseline browser |
| **Fonts** | `document.fonts.ready` before capture |
| **Animation** | Disable CSS animations/transitions in test profile |
| **Dynamic content** | Stub dates, fixed post IDs, seed content |
| **Images** | Wait for `networkidle` or explicit image selectors |
| **Scroll height** | Full-page for marketing pages; component mode for blocks |
| **Capture mode** | Full-page default; component captures for block-level debug |

---

## 5. Tool comparison

| Tool | Role | Decision |
|------|------|----------|
| **Playwright native screenshots** | Capture + `toHaveScreenshot` | **Default** |
| **pixelmatch** | Pixel diff metric | **Default** helper |
| **BackstopJS** | Scenario config | **Optional** alternative |
| **Percy** | Cloud review | **Deferred** (cost/SaaS) |
| **Custom runner** | MARS-specific wrapper | **Future** thin wrapper over Playwright |

---

## 6. Threshold policy

| Metric | Default |
|--------|---------|
| **Pixel threshold** | **SAFE UNKNOWN** — calibrate per pilot (FW-05) |
| **Layout threshold** | Structural regions — human review on any nav/header/footer mismatch |
| **Anti-aliasing** | Use Playwright maxDiffPixelRatio — start 0.01–0.02 pilot tuning |

**Rule:** No universal numeric threshold without pilot calibration.

---

## 7. Diff storage and review

| Artifact | Location |
|----------|----------|
| Reference PNG | STORAGE `reference/` |
| WordPress PNG | STORAGE `wordpress/` |
| Diff PNG | STORAGE `diff/` |
| Report | `REPORTS/VISUAL-QA-REPORT` |

**Human approval:** Operator sign-off recorded in VISUAL-QA-REPORT — **BLOCKING** for PIXEL_PERFECT.

---

## Related

- [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md) WV6
- [operator-visual-approval-law-v1.md](../../../operator-visual-approval-law-v1.md)

---

*Visual regression design v1 — workflow only.*

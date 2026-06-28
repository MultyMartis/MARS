# SITE-002 — CORPORATE PAGES VISUAL POLISH PASS 01

**Program:** SITE-002 (BZPM / ЗПМ)  
**Task:** SITE-002 — Corporate Pages Visual Polish Implementation (Pass 1)  
**Environment:** TEST only — https://zpm.new-site.space/  
**Date:** 2026-06-28  
**Checkpoint:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01`  
**Audit source:** [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md](SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md)

---

## 1. Safety preflight

| Item | Value |
|------|--------|
| **Repository** | `C:\MARS Phenix\AI MARS` |
| **Branch** | `mars/canonical-post-recovery` |
| **HEAD (preflight checkpoint)** | `68f11fdc` — `checkpoint(site-002): before corporate pages visual polish pass 1` |
| **Operator Beget backup** | **CONFIRMED** |
| **Production** | **NOT TOUCHED** |
| **Scope** | Corporate pages only — M9.14 Delivery · M9.15 Payment · M9.16 Dealers · M9.17 Warranty · M9.18 Custom Manufacturing |

### Checkpoint

- Pre-work: `68f11fdc` pushed to `origin/mars/canonical-post-recovery`

### Backup

- `projects/ocpilot/sites/site-002/backups/style.css.pre-site-002-corp-visual-polish-pass1.bak`

### Manifest

- [site-002-visual-polish-pass1-work/preflight-manifest.json](site-002-visual-polish-pass1-work/preflight-manifest.json)
- [site-002-visual-polish-pass1-work/deploy-manifest.json](site-002-visual-polish-pass1-work/deploy-manifest.json)

---

## 2. Files modified

| File | Action |
|------|--------|
| `assets/css/style.css` (TEST live) | Appended polish block VP-01–VP-10 |
| `projects/ocpilot/sites/site-002/reports/site-002-visual-polish-pass1-work/style.css` | Work copy with patch applied |
| `projects/ocpilot/sites/site-002/reports/site-002-visual-polish-pass1-work/site-002-corp-visual-polish-pass1.css` | Patch source (new) |
| `projects/ocpilot/sites/site-002/reports/site-002-visual-polish-pass1-work/preflight-manifest.json` | Preflight (new) |
| `projects/ocpilot/sites/site-002/reports/site-002-visual-polish-pass1-work/deploy-manifest.json` | Deploy QA (new) |
| `projects/ocpilot/sites/site-002/reports/site-002-visual-polish-pass1-work/site-002-corp-polish-deploy.py` | Deploy helper (new) |
| `projects/ocpilot/sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md` | Stable checkpoint (new) |

**Not modified:** Twig · PHP · `main.js` · Home · Catalog · PLP · PDP · Contacts · Header · Footer

---

## 3. Backups created

| Path |
|------|
| `projects/ocpilot/sites/site-002/backups/style.css.pre-site-002-corp-visual-polish-pass1.bak` |

---

## 4. CSS changes

### VP-01 — Remove double vertical spacing

- `.zpm-delivery-section`, `.zpm-payment-section`, `.zpm-warranty-section`, `.zpm-dealers-section`, `.zpm-custom-section` → `padding-top: 0`
- `.zpm-delivery-cta`, `.zpm-payment-cta`, `.zpm-warranty-cta`, `.zpm-dealers-cta`, `.zpm-custom-cta` → `padding-top: 0`
- `.zpm-custom-process`, `.zpm-custom-outcomes` → `padding-top: 0`

### VP-02 — Hero / Page Intro / Lead spacing

- Corp routes `.page-intro > .container` → `gap: var(--pad-gap)` (was `--pad-gap-mini`)

### VP-03 — Hardcoded spacing → Home tokens

- `.zpm-dealers-cta__actions`, `.zpm-custom-cta__actions` → `gap: var(--pad-gap-line) var(--pad-gap)`; `margin-top: var(--pad-gap)`; `margin-bottom: 0`
- `.zpm-dealers-cta__contacts`, `.zpm-custom-cta__contacts` → `gap: var(--pad-gap-line) var(--pad-gap)`; `margin-top: var(--pad-gap-mini)`; `margin-bottom: 0`

### VP-04 — Card padding / grid density

- `.zpm-payment-proof__grid` → `grid-template-columns: repeat(4, …)`; `gap: var(--pad-gap)`
- `.zpm-delivery-outcomes__list`, `.zpm-warranty-outcomes__list` → `gap: var(--pad-gap)`

### VP-05 — Icon scale

- `.zpm-delivery-point-card__icon` → `width/height: var(--img-mini-width)` (80px); `font-size: 28px`

### VP-06 — H2 / card title rhythm

- `.zpm-warranty-outcome__title` → `margin-bottom: var(--pad-gap-mini)` (was `8px`)
- `.zpm-corp-timeline__step` → `gap: var(--pad-gap-mini)` (was `8px`)

### VP-07 — Paragraph / list rhythm

- `.zpm-delivery-org__list`, `.zpm-delivery-coverage__factors`, `.zpm-warranty-verification__list`, `.zpm-custom-scope__group ul` → `gap: var(--pad-gap-mini)`
- `.zpm-payment-page .page-intro` → `margin-bottom: var(--pad-gap)`

### VP-08 — CTA spacing

- Dealers + Custom CTA token gaps + margin direction aligned with Delivery/Payment/Warranty (see VP-03)

### VP-09 — FAQ spacing

- Corp route `.zpm-corp-faq__list` → `gap: var(--pad-gap)`
- `.zpm-dealers-oem-row` → `padding-top/bottom: 0`
- `.zpm-dealers-proof__stack` → `gap: var(--pad-gap)`

### VP-10 — Custom Manufacturing soften

- `.zpm-custom-triggers__list` → `gap: var(--pad-gap-mini)` (was `10px`)
- `.zpm-custom-process` → `border-top/bottom: 1px solid var(--border-color)`; `padding-bottom: 0`
- `.zpm-custom-process .zpm-corp-timeline__step` → `border-width: 1px`; `box-shadow: none`
- `.zpm-custom-outcomes` → `border-top: 1px solid var(--border-color)`
- `.zpm-custom-oem__stack` → `gap: var(--pad-gap)`
- `.zpm-custom-timeline.zpm-corp-timeline` → `grid-template-columns: repeat(4, …)` desktop default
- `.zpm-corp-timeline` → `gap: var(--pad-gap)`

### VP-11 (Priority 2) — Summary / facts strips

- `@media (min-width: 1025px)` — `.zpm-delivery-summary`, `.zpm-warranty-summary`, `.zpm-payment-legal__facts` → `gap: var(--pad-gap)`

### VP-08 (Warranty verification)

- `.zpm-warranty-verification` → `padding-top: 0` (was `calc(var(--pad-y) * 0.75)`)

---

## 5. Cross-page consistency

Unified across all five corporate pages:

- Section vertical rhythm matches Home `main > section` (`--pad-y` single stack — no double padding)
- Page intro title → lead gap uses Home `--pad-gap`
- Corp timeline grid gap uses Home card grid `--pad-gap`
- Timeline step internal gap uses `--pad-gap-mini` minimum
- CTA action/contact gaps use token pair `--pad-gap-line` / `--pad-gap` on Dealers + Custom (parity with Delivery trio)
- Summary/facts strips use `--pad-gap` on desktop
- FAQ accordion list gap `--pad-gap` on corp routes
- Custom accent borders softened to 1px neutral; timeline density capped at 4 columns desktop

---

## 6. QA

| Check | Result |
|-------|--------|
| **Desktop HTTP** | PASS — `/`, `/delivery`, `/payment-methods`, `/guarantee`, `/dealers`, `/custom-equipment` → 200 |
| **Tablet / Mobile viewport** | **NOT RUN** — operator HITL at 1440 / 1024 / 390 recommended |
| **Console errors** | **NOT RUN** — browser console check deferred to operator HITL |
| **Overflow / grids** | **NOT RUN** — visual verification deferred |
| **Accordion / CTA / forms** | **NOT RUN** — logic unchanged; no JS deploy |
| **Live CSS marker** | PASS — polish block present on live `style.css` |

---

## 7. Screenshots

**Not generated** in this pass. Prior M9.14–M9.18 QA captures remain historical reference only.

---

## 8. Rollback

1. FTP restore `assets/css/style.css` from `backups/style.css.pre-site-002-corp-visual-polish-pass1.bak`
2. Verify HTTP 200 on six corp URLs + Home
3. Optional: operator visual spot-check
4. Git revert implementation commit if repo work copy must match live

---

## 9. Stable checkpoint

**Registered:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01`  
**Doc:** [baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md)

| Field | Value |
|-------|--------|
| pre_sha256 | `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` |
| post_sha256 | `d4303c40d972135c092f5b8803b148b37e80881ac6f6db9e76a220995115ca42` |

---

## 10. Operator notes — intentionally NOT changed (Pass 2 / HITL)

| Item | Reason |
|------|--------|
| **VP-12** — Corp table cell padding `12px 16px` | Priority 3 — deferred |
| **VP-13** — FAQ toggle icon 22px unification | Priority 3 — already 22px on corp FAQ |
| **VP-14** — CTA lead max-width 730px | Priority 3 — optional line-length parity |
| **VP-15** — Footer transition padding | Priority 3 |
| **VP-16** — Dead CSS hygiene (pre-M9.14 blocks) | Priority 3 — no user-visible change |
| **Page intro lead typography** (20px/26px hero weight) | NO typography changes per charter |
| **Custom approval gate** `border: 2px solid accent-02` | Charter emphasis — left unchanged |
| **Custom outcomes thead** accent bottom border / font-size bump | Partial soften only on section border; thead styling deferred |
| **About page (M9.13)** | Out of corp polish scope |
| **Pixel-perfect screenshot delta** | Operator HITL required |

---

## 11. Git

| Item | Value |
|------|--------|
| **Preflight commit** | `68f11fdc` — checkpoint before pass |
| **Implementation commit** | `85a9a429` — `feat(site-002): corporate pages visual polish pass 1 on TEST` |
| **Branch** | `mars/canonical-post-recovery` |

---

## SECURITY RISK

None identified. CSS-only deploy to TEST; credentials remain in deploy script pattern consistent with prior M9 passes (operator FTP record).

## UNKNOWN

- Viewport-level visual parity vs Home — requires operator HITL screenshots
- Browser console on corp pages post-deploy — not instrumented in this pass

# SITE-002 — CORPORATE PAGES VISUAL POLISH PASS 1.2

**Program:** SITE-002 (BZPM / ЗПМ)  
**Task:** SITE-002 — Corporate Pages Visual Polish Pass 1.2 (Home Parity — fine rhythm pass)  
**Environment:** TEST only — https://zpm.new-site.space/  
**Date:** 2026-06-28  
**Visual authority:** Home — https://zpm.new-site.space/  
**Checkpoint (pre-work):** `a838210f` — `checkpoint(site-002): before corporate pages visual polish pass 1.2`

---

## 1. Safety

| Item | Value |
|------|--------|
| **Repository** | `C:\MARS Phenix\AI MARS` |
| **Branch** | `mars/canonical-post-recovery` |
| **HEAD (preflight)** | `497c51c5fe088bb203b0c93486c3ee0f9f925afa` |
| **Checkpoint commit** | `a838210f` |
| **Operator Beget backup** | **CONFIRMED** |
| **Production** | **NOT TOUCHED** |
| **Scope** | M9.14 Delivery · M9.15 Payment · M9.16 Dealers · M9.17 Warranty · M9.18 Custom Manufacturing |

Pass 1 (rejected) **not** reintroduced. No `padding-top: 0` global resets.

---

## 2. Backups

FTP pre-deploy backups (live TEST → `projects/ocpilot/sites/site-002/backups/`):

| File | Pre SHA256 | Pre bytes |
|------|------------|-----------|
| `style.css.pre-site-002-corp-visual-polish-pass1.2.bak` | `e83dae3e08c30969cce68e366fa7f0b7dbf4ca80e3df204644ac87c40de80b5d` | 376462 |

Manifest: [site-002-visual-polish-pass1.2-work/deploy-manifest.json](site-002-visual-polish-pass1.2-work/deploy-manifest.json)

---

## 3. Files changed

| File (TEST live) | Action |
|------------------|--------|
| `assets/css/style.css` | In-place token harmonization + Pass 1.2 append block |

**Not modified:** Twig · PHP · `main.js` · header · footer · Home · Catalog · PLP · PDP

Work copies: `reports/site-002-visual-polish-pass1.2-work/`

---

## 4. Visual decisions

| ID | Decision | Rationale (Home parity) |
|----|----------|-------------------------|
| VP12-01 | H1-only `.page-intro > .container` gap → `--pad-gap` | Home hero title→lead gap token |
| VP12-02 | `.zpm-corp-page-lead__body` paragraph gap → `--pad-gap` | Home `zpm-dealers__text` stack breathing |
| VP12-03 | Corp table cells `12px 16px` → `var(--pad-gap)` both axes | Reduce catalog-like table density |
| VP12-04 | Payment proof card internal gap → `--pad-gap` | Home adv-card text stack |
| VP12-05 | Delivery point card internal gap → `--pad-gap` | Home card content grouping |
| VP12-06 | Summary/facts/OEM label margins `6px` → `--pad-gap-mini` | Home label→value rhythm |
| VP12-07 | Delivery/Warranty outcome cards flex + `--pad-gap-mini` internal gap | Home card title→text stacks |
| VP12-08 | Warranty verification list gap → `--pad-gap` | Outcome-group list breathing |
| VP12-09 | Dealers OEM row grid gap → `--pad-gap` | Commercial-trust card grid rhythm |
| VP12-10 | Dealers supply-chain nodes hardcoded px → tokens | Home CTA/list token discipline |
| VP12-11 | Custom OEM stack/proof-strip gaps → `--pad-gap` | Soften page density vs Home |
| VP12-12 | Custom triggers/scope lists `10px`/`8px` → `--pad-gap-mini` | Home list rhythm |
| VP12-13 | Custom OEM badge padding/gap → tokens | Commercial-trust chip pattern |

**Explicitly avoided:** new components · new colors · `padding-top: 0` · negative margins · layout rewrites.

---

## 5. Components reused

| Existing system | Applied to |
|-----------------|------------|
| Home `page-intro` / hero gap tokens | H1-only intros (corp + aligned internal pages) |
| `.zpm-commercial-trust` benefit/list rhythm | Dealers chain nodes · Custom OEM badge |
| `.zpm-adv-card` / proof card padding | Payment proof cards · outcome groups |
| `.zpm-catalog-faq` / corp FAQ (unchanged) | Prior pass rhythm retained |
| Corp summary strip pattern | Label margin tokenization across Delivery/Payment/Warranty/Dealers/Custom |

---

## 6. Components removed

None. Pass 1.2 is spacing-only refinement on existing corp components.

---

## 7. QA

| Check | Result |
|-------|--------|
| Home HTTP 200 | **PASS** |
| Delivery HTTP 200 | **PASS** |
| Payment HTTP 200 | **PASS** |
| Warranty HTTP 200 | **PASS** |
| Dealers HTTP 200 | **PASS** |
| Custom HTTP 200 | **PASS** |
| `page-intro__description` absent (5 corp pages) | **PASS** |
| `zpm-corp-page-lead` present (5 corp pages) | **PASS** |
| CSS marker `Corporate Pages Visual Polish Pass 1.2` | **PASS** |
| Pass 1.1 marker still present (layered) | **PASS** |
| Console errors | **SAFE UNKNOWN** — no automated browser console run |
| Horizontal overflow (desktop/tablet/mobile) | **SAFE UNKNOWN** — operator HITL at 1440 / 1024 / 390 |
| Pixel screenshots | **SAFE UNKNOWN** — live URLs verified; PNG capture not run in this task |

---

## 8. Screenshots

No automated viewport captures in this run. Operator HITL reference URLs:

| Page | URL |
|------|-----|
| Home (authority) | https://zpm.new-site.space/ |
| Delivery | https://zpm.new-site.space/delivery |
| Payment | https://zpm.new-site.space/payment-methods |
| Warranty | https://zpm.new-site.space/guarantee |
| Dealers | https://zpm.new-site.space/dealers |
| Custom | https://zpm.new-site.space/custom-equipment |

---

## 9. Remaining visual drift

| Area | Note |
|------|------|
| Corp lead typography | Still `--base-*`; Home hero uses `--Heading-*` — intentional internal-page choice |
| CTA blocks | Full `zpm-commercial-trust` vs Home teaser `zpm-dealers` — structural, token-aligned |
| Payment information density | Improved; still above Home due to IA (timeline + proof + tables) |
| Custom Manufacturing | Softened; still longest corp scroll |
| Dealers matrix tables | Cell padding improved; content density inherent to IA |
| Pixel HITL | Operator screenshot compare Home vs corp recommended |

---

## 10. Rollback

1. Restore `backups/style.css.pre-site-002-corp-visual-polish-pass1.2.bak` via FTP.
2. Clear Twig template cache on TEST if needed.
3. Git revert implementation commit on `mars/canonical-post-recovery`.

Pre-pass-1.2 live CSS SHA256: `e83dae3e08c30969cce68e366fa7f0b7dbf4ca80e3df204644ac87c40de80b5d`

---

## 11. Stable checkpoint

**ID:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2`  
**Live CSS post SHA256:** `243d6d5e2a1ad00c06c450f4b90dc72adb1671b64a681f266675abdbd9330252`  
**Status:** Active on TEST

Baseline: [SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md)

---

## 12. Git

| Item | Value |
|------|--------|
| Checkpoint | `a838210f` |
| Implementation commit | (this commit) |
| Push | `origin/mars/canonical-post-recovery` |

---

## Visual parity with Home

**MEDIUM-HIGH** (up from Pass 1.1 **MEDIUM**)

**Why:** Pass 1.2 closes residual micro-spacing drift from audit VP-02, VP-06–VP-12: page-intro air, lead stacks, table/cell density, payment proof breathing, outcome groups, dealers OEM/chain, custom OEM/lists. No forbidden global resets. Remaining gaps are structural (CTA pattern, corp lead weight, IA-driven density) not fixable without copy/layout change.

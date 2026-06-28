# SITE-002 — CORPORATE PAGES VISUAL POLISH PASS 1.1

**Program:** SITE-002 (BZPM / ЗПМ)  
**Task:** SITE-002 — Corporate Pages Visual Polish Pass 1.1 (Home Visual Parity Pass)  
**Environment:** TEST only — https://zpm.new-site.space/  
**Date:** 2026-06-28  
**Visual authority:** Home — https://zpm.new-site.space/  
**Checkpoint (pre-work):** `d96359f6` — `checkpoint(site-002): before corporate pages visual polish pass 1.1`

---

## 1. Safety

| Item | Value |
|------|--------|
| **Repository** | `C:\MARS Phenix\AI MARS` |
| **Branch** | `mars/canonical-post-recovery` |
| **HEAD (preflight)** | `db0c3ec78a83d0b06574cbb935394d284112f929` |
| **Checkpoint commit** | `d96359f6` |
| **Operator Beget backup** | **CONFIRMED** |
| **Production** | **NOT TOUCHED** |
| **Scope** | M9.14 Delivery · M9.15 Payment · M9.16 Dealers · M9.17 Warranty · M9.18 Custom Manufacturing |

Pass 1 (rejected) **not** continued — all Pass 1 visual decisions treated as invalid per operator rollback.

---

## 2. Backups

FTP pre-deploy backups (live TEST → `projects/ocpilot/sites/site-002/backups/`):

| File | Pre SHA256 | Pre bytes |
|------|------------|-----------|
| `style.css.pre-site-002-corp-visual-polish-pass1.1.bak` | `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` | 358072 |
| `delivery.php.pre-site-002-corp-visual-polish-pass1.1.bak` | `056beadfea6ae9e23fca7b5d75b58c789cf5633a2914b44c00e25cc954bb9649` | 3240 |
| `delivery.twig.pre-site-002-corp-visual-polish-pass1.1.bak` | `78e832813217a0bcdbeb79c800ff2f6b57a864e68084cb73a93b09855635407c` | 51133 |
| `payment.php` / `.twig` | see [deploy-manifest.json](site-002-visual-polish-pass1.1-work/deploy-manifest.json) | — |
| `guarantee.php` / `.twig` | see manifest | — |
| `dealers.php` / `.twig` | see manifest | — |
| `custom_equipment.php` / `.twig` | see manifest | — |

Manifest: [site-002-visual-polish-pass1.1-work/deploy-manifest.json](site-002-visual-polish-pass1.1-work/deploy-manifest.json)

---

## 3. Files changed

| File (TEST live) | Action |
|------------------|--------|
| `assets/css/style.css` | In-place rhythm/card polish + Pass 1.1 block |
| `catalog/controller/information/delivery.php` | `page_lead` data; no `pageintro->description` |
| `catalog/view/theme/default/template/information/delivery.twig` | `.zpm-corp-page-lead` in `<main>` |
| `catalog/controller/information/payment.php` | same pattern |
| `catalog/view/theme/default/template/information/payment.twig` | same pattern |
| `catalog/controller/information/guarantee.php` | same pattern |
| `catalog/view/theme/default/template/information/guarantee.twig` | same pattern |
| `catalog/controller/information/dealers.php` | same pattern |
| `catalog/view/theme/default/template/information/dealers.twig` | same pattern |
| `catalog/controller/information/custom_equipment.php` | same pattern |
| `catalog/view/theme/default/template/information/custom_equipment.twig` | same pattern |

**Not modified:** `main.js` · header · footer · Home · Catalog · PLP · PDP

Work copies: `reports/site-002-visual-polish-pass1.1-work/`

---

## 4. Visual decisions

| ID | Decision | Rationale (Home parity) |
|----|----------|-------------------------|
| VP11-01 | Remove duplicate `padding-top` on corp section/CTA rules **at source** (not global `padding-top:0` reset) | Home uses single `main > section` `--pad-y` rhythm |
| VP11-02 | Intro text → `.zpm-corp-page-lead` first block in `<main>` | RULE 01 — no `page-intro__description` |
| VP11-03 | Timeline gap `--pad-gap-line` → `--pad-gap`; step gap → `--pad-gap-mini` | Home card grid breathing |
| VP11-04 | Delivery point icons → `--img-mini-width` (80px) | Home mini-asset scale |
| VP11-05 | Payment proof grid 5→4 col; gap `--pad-gap` | Home `zpm-adv-cards__grid--row4` density |
| VP11-06 | Summary/facts strips gap `--pad-gap` | Home benefit strip air |
| VP11-07 | Outcome grids gap `--pad-gap`; warranty title margin tokenized | Home card text stacks |
| VP11-08 | Dealers/Custom CTA gaps → `--pad-gap-line` / `--pad-gap`; margin direction unified with Delivery trio | Home CTA token discipline |
| VP11-09 | Dealers proof stack gap `--pad-gap` | Commercial-trust card stack rhythm |
| VP11-10 | Custom process/outcomes accent borders 2–3px → `1px var(--border-color)`; timeline 8→4 col desktop; remove step shadow | Reduce visual noise vs Home calm sections |
| VP11-11 | Corp FAQ list gap `--pad-gap` | Catalog FAQ / commercial-trust card list rhythm |

**Explicitly avoided:** Pass 1 global `padding-top: 0` block (operator-rejected VP-01).

---

## 5. Components reused

| Existing system | Applied to |
|-----------------|------------|
| `.zpm-commercial-trust` (CTA blocks) | Unchanged markup; CTA spacing aligned to Delivery/Payment/Warranty token pattern |
| `.zpm-commercial-trust__benefit-icon` scale reference | Delivery point card icons via `--img-mini-width` |
| `.zpm-catalog-faq` / `.zpm-corp-faq` list rhythm | Corp FAQ list gap increased to `--pad-gap` (same family as catalog FAQ cards) |
| `.zpm-corp-timeline` | Shared timeline; gap tokens harmonized |
| `main > section` global padding | Sole section top rhythm after removing duplicate corp rules |

**New classes NOT created for card systems** — only `.zpm-corp-page-lead` / `__body` wrapper for RULE 01 text migration.

---

## 6. Components removed

| Removed | Where |
|---------|-------|
| `.page-intro__description` output | All 5 corporate controllers (description unset) |
| Duplicate `padding-top: var(--pad-y)` rules | `.zpm-*-section`, `.zpm-*-cta` source blocks |
| `.zpm-warranty-verification` fractional top padding | Replaced by standard section rhythm |
| `.zpm-dealers-oem-row` half `--pad-y` padding | Replaced by standard section rhythm |
| Custom accent-heavy borders/shadows on process/outcomes | Softened to site border tokens |

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
| CSS marker `Corporate Pages Visual Polish Pass 1.1` | **PASS** |
| Accordion markup (`zpm-corp-faq`) on Delivery/Dealers | **PASS** (structural) |
| Form markup (`zpm-form`) on Delivery | **PASS** (structural) |
| Console errors | **SAFE UNKNOWN** — no automated browser console run in this task |
| Horizontal overflow (desktop/tablet/mobile) | **SAFE UNKNOWN** — operator HITL recommended at 1440 / 1024 / 390 |

---

## 8. Rollback

1. Restore from `backups/*.pre-site-002-corp-visual-polish-pass1.1.bak` via FTP (11 files).
2. Clear Twig template cache on TEST.
3. Git revert implementation commit on `mars/canonical-post-recovery`.

Pre-pass-1.1 live CSS SHA256: `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c`

---

## 9. Stable checkpoint

**ID:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1`  
**Live CSS post SHA256:** `e83dae3e08c30969cce68e366fa7f0b7dbf4ca80e3df204644ac87c40de80b5d`  
**Status:** Active on TEST

---

## 10. Remaining polish

- Operator HITL pixel pass: Home vs corp at 1440 / 1024 / 390 (lead typography weight vs hero `--Heading-*` not migrated — intentional corp internal page choice).
- Payment first section still opens with timeline (IA order unchanged).
- Custom Manufacturing charter emphasis blocks retained structurally; only border weight reduced.
- Console + overflow sweep via browser DevTools.
- About page (M9.13) out of scope for this pass.

---

## 11. Git

| Item | Value |
|------|--------|
| Checkpoint | `d96359f6` |
| Implementation commit | (this commit) |
| Push | `origin/mars/canonical-post-recovery` |

---

## RULE 01 — page-intro__description migration

| Page | Removed from | Text moved to |
|------|--------------|---------------|
| Delivery | `Pageintro::description` in `delivery.php` | `<main>` → `.zpm-corp-page-lead__body` |
| Payment | `payment.php` | same |
| Warranty | `guarantee.php` | same |
| Dealers | `dealers.php` | same |
| Custom | `custom_equipment.php` | same |

Copy unchanged — same HTML paragraphs as former `page-intro__description`.

---

## Visual parity with Home

**MEDIUM**

**Why:** Section vertical rhythm now matches Home single-layer `main > section` padding (duplicate corp top padding removed without forbidden global zeroing). Card grids, timeline gaps, proof/summary strips, and CTA spacing moved toward Home token discipline. Intro lead relocated into `main` per RULE 01. Remaining gaps: corp lead still uses `--base-*` not hero `--Heading-*`; Payment/Custom information density still above Home; no pixel-level HITL screenshots in this run; CTA blocks use full `zpm-commercial-trust` vs Home teaser `zpm-dealers` — structurally different but token-aligned.

# SITE-002 — CORPORATE PAGES VISUAL POLISH PASS 01 ROLLBACK

**Program:** SITE-002 (BZPM / ЗПМ)  
**Task:** SITE-002 — Corporate Pages Visual Polish Pass 1 Rollback + Pass 1.1 Rule Registration  
**Environment:** TEST only — https://zpm.new-site.space/  
**Date:** 2026-06-28  
**Operator decision:** **REJECTED BY OPERATOR**  
**Current visual authority:** Pre-Pass-1 state  
**Next task:** SITE-002 — Corporate Pages Visual Polish Pass 1.1

---

## 1. Safety preflight

| Item | Value |
|------|--------|
| **Repository** | `C:\MARS Phenix\AI MARS` |
| **Branch** | `mars/canonical-post-recovery` |
| **HEAD (rollback start)** | `ec5ff2c0` — `refactor(fp-0002): universalize final form component in v8` |
| **Production** | **NOT TOUCHED** |
| **Scope** | Rollback `assets/css/style.css` on TEST only — no Twig · PHP · JS changes |

### Pre-pass-1 backup verified

| Path | Exists |
|------|--------|
| `projects/ocpilot/sites/site-002/backups/style.css.pre-site-002-corp-visual-polish-pass1.bak` | **YES** |

### Rejected-state backup created

| Path | Purpose |
|------|---------|
| `projects/ocpilot/sites/site-002/backups/style.css.rejected-site-002-corp-visual-polish-pass1.bak` | Snapshot of live TEST CSS **before** rollback (Pass 1 deployed state) |

### Manifest

- [site-002-visual-polish-pass1-work/rollback-manifest.json](site-002-visual-polish-pass1-work/rollback-manifest.json)
- [site-002-visual-polish-pass1-work/site-002-corp-polish-rollback.py](site-002-visual-polish-pass1-work/site-002-corp-polish-rollback.py)

---

## 2. Rollback source

| Item | Value |
|------|--------|
| **Restore from** | `projects/ocpilot/sites/site-002/backups/style.css.pre-site-002-corp-visual-polish-pass1.bak` |
| **Remote target** | `assets/css/style.css` (TEST FTP) |
| **Method** | FTP upload of pre-Pass-1 backup bytes |

---

## 3. Files restored

| File | Action |
|------|--------|
| `assets/css/style.css` (TEST live) | Restored to pre-Pass-1 state |

**Not modified:** Twig · PHP · `main.js` · HTML · OpenCart architecture

---

## 4. Files backed up

| Path | SHA256 |
|------|--------|
| `backups/style.css.rejected-site-002-corp-visual-polish-pass1.bak` | `d4303c40d972135c092f5b8803b148b37e80881ac6f6db9e76a220995115ca42` |
| `backups/style.css.pre-site-002-corp-visual-polish-pass1.bak` (unchanged) | `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` |

---

## 5. SHA256 verification

| State | SHA256 | Bytes |
|-------|--------|-------|
| **Rejected (Pass 1 live, pre-rollback)** | `d4303c40d972135c092f5b8803b148b37e80881ac6f6db9e76a220995115ca42` | 379408 |
| **Pre-Pass-1 backup** | `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` | 358072 |
| **Post-rollback live TEST** | `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` | 358072 |

**Verification:** post-rollback live SHA256 **matches** pre-Pass-1 backup SHA256.

**CSS marker:** `Corporate Pages Visual Polish Pass 1` — **absent** on live TEST after rollback.

---

## 6. HTTP verification

| URL | HTTP |
|-----|------|
| https://zpm.new-site.space/ | **200** |
| https://zpm.new-site.space/delivery | **200** |
| https://zpm.new-site.space/payment-methods | **200** |
| https://zpm.new-site.space/guarantee | **200** |
| https://zpm.new-site.space/dealers | **200** |
| https://zpm.new-site.space/custom-equipment | **200** |

**All HTTP OK:** **YES**

---

## 7. Rejected CSS changes

**Primary rejection reason:** global `padding-top: 0` reset on corporate sections removed vertical rhythm (“воздух”) and made pages read as one compressed mass.

### VP-01 — rejected global reset (root cause)

```css
.zpm-delivery-section,
.zpm-payment-section,
.zpm-warranty-section,
.zpm-dealers-section,
.zpm-custom-section,
.zpm-delivery-cta,
.zpm-payment-cta,
.zpm-warranty-cta,
.zpm-dealers-cta,
.zpm-custom-cta,
.zpm-custom-process,
.zpm-custom-outcomes {
    padding-top: 0;
}
```

**Operator verdict:** such global section zeroing is **forbidden** for Corporate Pages visual polish (see Pass 1.1 Rule 04).

**Full rejected patch:** [site-002-corp-visual-polish-pass1.css](site-002-visual-polish-pass1-work/site-002-corp-visual-polish-pass1.css) — entire appended block removed from live TEST.

---

## 8. Pass 1.1 rules registered

Registered in state documents (Knowledge Map §24, site-passport, README, OCPILOT-STATE, OPERATIONAL-INDEX).

| Rule | Summary |
|------|---------|
| **RULE 01** | `.page-intro__description` — **forbidden** on M9.14–M9.18; future Pass 1.1 must move intro text into page `main` without copy/order changes |
| **RULE 02** | Reuse `.zpm-commercial-trust` / `.zpm-catalog-faq` families for cards, proof, steps, FAQ-like blocks — no new card systems without necessity |
| **RULE 03** | **Home** is visual authority for rhythm, air, density — not Catalog or PDP |
| **RULE 04** | **No global** `padding-top: 0` on corporate sections; rhythm changes must be local and Home-referenced |
| **RULE 05** | Before every Visual Polish pass: file backups + Beget backup + Git checkpoint — **mandatory** |

**Pass 1.1 text migration:** **NOT executed** in this task — registration only.

---

## 9. Documentation updated

| Document | Change |
|----------|--------|
| [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) | §23 Pass 1 → REJECTED; §24 Pass 1.1 rules |
| [site-passport.md](../site-passport.md) | Visual polish status + Pass 1.1 rules |
| [README.md](../README.md) | Active stage + next task |
| [OCPILOT-STATE.md](../../../OCPILOT-STATE.md) | SITE-002 focus + polish lifecycle |
| [OPERATIONAL-INDEX.md](../../../OPERATIONAL-INDEX.md) | Entry 4.158 rollback |
| [SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md) | Status → REJECTED BY OPERATOR |

---

## 10. Git

| Item | Value |
|------|--------|
| **Commit** | `revert(site-002): rollback rejected corporate pages visual polish pass 1` |
| **Push** | `origin/mars/canonical-post-recovery` |
| **HEAD** | `9b073754` — `revert(site-002): rollback rejected corporate pages visual polish pass 1` |

---

## 11. Next task

**SITE-002 — Corporate Pages Visual Polish Pass 1.1**

Apply registered rules (§24 Knowledge Map). Do **not** repeat Pass 1 global padding reset.

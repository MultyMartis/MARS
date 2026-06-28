# SITE-002 — CUSTOM PROOF STRIP RESTYLE

**Task:** SITE-002 — Custom Manufacturing `.zpm-custom-oem__proof-strip` → Commercial Trust services style  
**Branch:** `mars/canonical-post-recovery`  
**Authority:** `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` (card pattern) · `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` (page scope)  
**Live TEST:** https://zpm.new-site.space/custom-equipment  
**Deploy pass:** `site-002-custom-proof-strip-01`  
**Timestamp (UTC):** 2026-06-28T23:51:54Z  
**Verdict:** **PASS**

---

## 1. Safety

| Step | Result |
|------|--------|
| `git status` + `git rev-parse HEAD` | Pre: `ba196a379` · branch `mars/canonical-post-recovery` |
| Checkpoint commit | `70f5349b` — `checkpoint(site-002): before custom proof strip commercial trust restyle` |
| Production | **NOT TOUCHED** |
| Controllers / JS / forms / sibling corp pages | **NOT TOUCHED** |
| Scope | `custom_equipment.twig` + `style.css` append block only |

---

## 2. Authority

Visual pattern reused from **`.zpm-commercial-trust__services`** (Home / catalog FAQ grid):

| Reused class | Role |
|--------------|------|
| `.zpm-commercial-trust__services` | Grid container |
| `.zpm-commercial-trust__service` | Card shell |
| `.zpm-commercial-trust__service-icon` | FA Pro icon slot |
| `.zpm-commercial-trust__service-title` | Card title (former `dt` label) |
| `.zpm-commercial-trust__service-text` | Card body (former `dd` value + links) |

Wrapper retained: **`.zpm-custom-oem__proof-strip`** — margin + grid column override only (no new card system).

---

## 3. Files changed (live TEST)

| Remote | pre → post SHA256 |
|--------|-------------------|
| `catalog/view/theme/default/template/information/custom_equipment.twig` | `2c43e2e8…` → `24c93172…` |
| `assets/css/style.css` | `d0da1d23…` → `461703ed…` |

Preflight: [custom-proof-strip-work/preflight-manifest.json](custom-proof-strip-work/preflight-manifest.json)  
Deploy: [custom-proof-strip-work/deploy-manifest.json](custom-proof-strip-work/deploy-manifest.json)  
SHA256: [custom-proof-strip-work/deploy-sha256.json](custom-proof-strip-work/deploy-sha256.json)

---

## 4. Reused components

- Commercial Trust service card markup and CSS from live `style.css` (§14 / catalog FAQ)
- FA Pro Duotone icons aligned to content:
  - **Производство** — `fad fa-industry`
  - **Сертификация** — `fad fa-file-certificate`
  - **Каталог** — `fad fa-th-large`

---

## 5. New components

| Item | Purpose |
|------|---------|
| CSS append block `zpm-custom-proof-strip.css` | Reset legacy boxed strip; 3-col grid override inside wrapper |
| Deploy / rollback scripts | FTP safety for this pass only |

**No** new card classes. **No** new design system.

---

## 6. QA

| Check | Result |
|-------|--------|
| HTTP `/custom-equipment` | **200** |
| Automated deploy QA | **all_pass: true** |
| Legacy `zpm-custom-oem__proof-item` absent | **yes** |
| Commercial trust classes present | **yes** |
| CSS patch on TEST | **yes** |
| Console / inline error markers in HTML | **none observed** |
| Overflow | **SAFE UNKNOWN** — no automated viewport screenshot pass; layout uses existing responsive grid (3 → 2 → 1 col) |

---

## 7. Rollback

```bash
python projects/ocpilot/sites/site-002/reports/custom-proof-strip-work/site-002-custom-proof-strip-rollback.py
```

Backups: `backups/*.{pre-site-002-custom-proof-strip-01.bak}`

---

## 8. Stable checkpoint

**Name:** `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`  
**Doc:** [baselines/SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01.md](../baselines/SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01.md)

---

## 9. Documentation updated

- [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §31
- [site-passport.md](../site-passport.md)
- [README.md](../README.md)
- [OCPILOT-STATE.md](../../OCPILOT-STATE.md)
- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)

---

## 10. Git

| Commit | Message |
|--------|---------|
| `70f5349b` | `checkpoint(site-002): before custom proof strip commercial trust restyle` |
| *(feat)* | `feat(site-002): restyle custom proof strip using commercial trust pattern` |

---

## 11. Final verdict

**PASS** — proof strip on `/custom-equipment` now uses the established Commercial Trust service card pattern; content meaning preserved; scope limited to Custom Manufacturing page.

**Stopped** — no Delivery or sibling page work initiated.

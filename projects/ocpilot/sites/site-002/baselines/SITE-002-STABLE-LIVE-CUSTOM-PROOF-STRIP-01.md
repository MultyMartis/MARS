# SITE-002 — Stable Live Custom Proof Strip Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-29  
**Mode:** Custom Manufacturing OEM proof strip — Commercial Trust services reuse  
**Status:** **ACTIVE / PASS**

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`

**Parent authority:** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` (page) · `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` (card pattern)

**Scope:** Block `.zpm-custom-oem__proof-strip` on `/custom-equipment` only.

---

## 2. Live surface

| Item | Value |
|------|--------|
| URL | https://zpm.new-site.space/custom-equipment |
| Twig | `catalog/view/theme/default/template/information/custom_equipment.twig` |
| Wrapper | `.zpm-custom-oem__proof-strip` |
| Card pattern | `.zpm-commercial-trust__services` + `.zpm-commercial-trust__service*` |
| CSS append | `assets/css/style.css` — `SITE-002 — Custom OEM proof strip → commercial trust services reuse` |

### Cards (3)

| Title | Icon | Link |
|-------|------|------|
| Производство | `fad fa-industry` | `/about` |
| Сертификация | `fad fa-file-certificate` | `/our-certification` |
| Каталог | `fad fa-th-large` | `/` |

---

## 3. SHA256 (post-deploy)

| File | post SHA256 |
|------|-------------|
| `custom_equipment.twig` | `24c93172ea3938e2f17190ce77dc690cff61780af59ad3e79d939bf69c05dd16` |
| `style.css` | `461703ed91749e5fcbb60d5d587adfd58c4f4e608032e24b7e16d3872ba21f62` |

Manifest: [reports/custom-proof-strip-work/deploy-sha256.json](../reports/custom-proof-strip-work/deploy-sha256.json)

---

## 4. Rollback

```bash
python projects/ocpilot/sites/site-002/reports/custom-proof-strip-work/site-002-custom-proof-strip-rollback.py
```

Backups: `backups/*.{pre-site-002-custom-proof-strip-01.bak}`

---

## 5. Report

[reports/SITE-002-CUSTOM-PROOF-STRIP-RESTYLE.md](../reports/SITE-002-CUSTOM-PROOF-STRIP-RESTYLE.md)

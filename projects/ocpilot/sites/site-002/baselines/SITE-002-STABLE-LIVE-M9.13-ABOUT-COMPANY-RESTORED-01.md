# SITE-002 — Stable Live M9.13 About Company Restored Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-23 (operator-approved restoration after M9.13 About redesign rejection)  
**Mode:** Stable live checkpoint registration — **metadata only** (no deploy, no FTP capture in this registration)

---

## 1. Authority state

`SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`

**Current Authority State:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`

**Supersedes:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`

**Restoration classification:** **operator-approved restoration** — **not** a rollback failure.

---

## 2. Current source of truth

| Priority | Source | Notes |
|----------|--------|-------|
| **1** | **Live TEST** — https://zpm.new-site.space/ | Authoritative storefront state |
| **2** | **Full Beget backup** | Operator attestation — disaster recovery |
| **3** | **Manual UI refinements** | **CANONICAL** |
| **4** | **Manual CSS refinements** | **CANONICAL** |
| **5** | **Manual Twig refinements** | **CANONICAL** |
| **6** | **Manual JS refinements** | **CANONICAL** |
| **7** | **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. **§17 About Page History** |

Prior repo baselines, work copies (`*-work/`), pass reports, and pre-pass `.bak` files are **historical** unless refreshed by live FTP capture.

**Do not** use `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` as current authority — superseded by this checkpoint.

**About page (`/about`):** **restored pre-M9.13 redesign version** is the **canonical** live state. M9.13 redesign + polish work copies are **historical reference only** — not live truth.

---

## 3. Registration context

This checkpoint supersedes `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` and records:

1. **Catalog UX cluster** — carried forward unchanged (filter recovery, filter UX, Commercial Trust, catalog state persistence, hub cleanup)
2. **M9.13 About Company redesign** — designed, implemented, QA passed, **rejected by operator**
3. **M9.13 About Company polish** — implemented, QA passed, **rejected with redesign**
4. **Operator-approved restoration** — live `/about` restored to pre-redesign state (2026-06-23)

---

## 4. Completed work (registered)

### Catalog UX (carried forward — unchanged scope)

All items from `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` remain active. See prior baseline for pass tables.

### M9.13 About Company — lifecycle

| Stage | Status | Evidence |
|-------|--------|----------|
| **Design** | **complete** | Corporate Pages Program · M9.13 charter |
| **Redesign implementation** | **IMPLEMENTED** | [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md) |
| **Redesign QA** | **QA PASSED** | Redesign report §QA |
| **Polish pass** | **IMPLEMENTED** | [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md) |
| **Polish QA** | **QA PASSED** | Polish report §QA |
| **Operator review** | **REJECTED BY OPERATOR** | Visual evaluation — redesign not accepted for production |
| **Restoration** | **RESTORED** | [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md) |
| **Restoration QA** | **QA PASSED** | Restore report §5 |

### About page — live canonical state (post-restoration)

| Item | Value |
|------|--------|
| **URL** | https://zpm.new-site.space/about |
| **Route** | `information/about` |
| **Structure** | Pre-M9.13 legacy — `about-page--main-wrap`, video block, cert slider, dealer form, `geo-web.png` |
| **M9.13 namespaces** | **absent** — no `zpm-about-hero`, `zpm-about-company`, etc. |
| **Polish-only asset** | `about-logistics.jpg` — **removed** from live |

**Restored files (live):**

| Remote path | Restore source |
|-------------|----------------|
| `catalog/view/theme/default/template/information/about.twig` | `backups/about.twig.pre-m9.13-about-redesign.bak` |
| `catalog/controller/information/about.php` | `backups/about.php.pre-m9.13-about-redesign.bak` |
| `assets/css/style.css` | `backups/style.css.pre-m9.13-about-redesign.bak` |
| `assets/img/about-page-img.jpg` | `backups/about-page-img.jpg.pre-m9.13-about-polish-v1.bak` *(fallback — same pre-redesign bytes)* |

---

## 5. Active stable state summary

| Item | Value |
|------|--------|
| Authority | **`SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`** |
| Catalog UX | Unchanged — full cluster from M9.8.9 Catalog UX Complete 01 |
| About page | **Restored pre-M9.13 version** — operator canonical |
| M9.13 redesign/polish | **Historical** — work copies in `reports/m9.13-work/`, `reports/m9.13-polish-work/` |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — **§17 About Page History** |
| Live truth | **hosting state on `zpm.new-site.space`** |

---

## 6. Pass evidence (repo references)

### M9.13 About Company

| Pass | Evidence |
|------|----------|
| Redesign | [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md) |
| Polish | [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md) |
| Restoration | [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md) |
| Restore work dir | [m9.13-restore-work/](../reports/m9.13-restore-work/) |
| Redesign work dir | [m9.13-work/](../reports/m9.13-work/) |
| Polish work dir | [m9.13-polish-work/](../reports/m9.13-polish-work/) |

### Prior checkpoint (superseded)

| Pass | Evidence |
|------|----------|
| Catalog UX Complete | [SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md) |

---

## 7. Known open items (not blocking this checkpoint)

| Item | Status |
|------|--------|
| **EC-01** | mitigated by subcategories hide (07) |
| M9.8.9-09C browser QA matrix (Q1–Q6) | **PENDING operator** |
| M9.8.3/4/6/8 deferred UX passes | **not authorized** |
| **M10** | **not authorized** |
| Future About redesign | **not authorized** — requires new operator charter; read §17 + restoration evidence first |
| Twig cache after restore | **SAFE UNKNOWN** — restore script returned empty cache listing; operator manual clear if stale render |

---

## 8. Rollback source

1. **Beget full backup** — full hosting restore
2. **Current live TEST state** — https://zpm.new-site.space/
3. **About pre-redesign backups** — `backups/*.pre-m9.13-about-redesign.bak`
4. **About polish backups** — `backups/*.pre-m9.13-about-polish-v1.bak`
5. **Re-apply M9.13 redesign** — deploy from `reports/m9.13-work/` *(operator decision only — rejected state)*
6. **Re-restore pre-redesign** — re-run `reports/m9.13-restore-work/m913-about-restore-to-pre-redesign.py`
7. **File-level pass backups** — `backups/*.pre-m9.8.9-*` incl. catalog UX passes
8. **Prior repo STABLE folders** — historical

---

## 9. Rule before next tasks

Before any next SITE-002 change:

1. Read [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Read this checkpoint (latest stable)
3. Verify **Authority State** = `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`
4. For **About page** — read Knowledge Map **§17 About Page History** + restoration / redesign / polish reports (see §9.1)
5. For **filters / sort / pagination / limit / only_with_price** — read Knowledge Map **§16** + passes **09A / 09B / 09C**
6. For **trust block / certificates / dealers form / category CTA** — read Knowledge Map **§14** + this checkpoint

See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md).

### 9.1 About page — mandatory pre-task (future redesign)

Before **any** new About page redesign or structural change:

1. Read [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md)
2. Read [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md)
3. Read [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md)
4. Read Knowledge Map **§17 About Page History**
5. Treat **restored version** on live TEST as **source of truth** — not M9.13 work copies

---

## Status

| Field | Value |
|-------|--------|
| Checkpoint type | **STABLE LIVE CHECKPOINT** (metadata registration) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Rollback source | **Beget full backup + current live TEST + About pass backups** |
| Deploy (this registration) | **NO** |
| FTP (this registration) | **NO** |

---

*Documentation only — no runtime claimed.*

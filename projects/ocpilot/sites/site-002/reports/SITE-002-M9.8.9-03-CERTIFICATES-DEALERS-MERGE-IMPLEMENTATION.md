# REPORT — M9.8.9-03 CERTIFICATES DEALERS MERGE IMPLEMENTATION

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`  
**Variant:** B — Trust strip + split  
**Scope:** Category PLP only (`product/category`)  
**Date:** 2026-06-19  
**Commit / push:** **NO** (per charter)

**PRE-TASK RULE:** Knowledge Map + Stable Checkpoint + forensic report + site-passport — read and applied.

---

## 1. Files Changed

### Live (deployed to TEST FTP)

| Remote path | Action | SHA256 (post-deploy) |
|-------------|--------|----------------------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | **NEW** | *(see manifest)* |
| `catalog/controller/product/category.php` | **MODIFIED** | — |
| `catalog/view/theme/default/template/product/category.twig` | **MODIFIED** | `2b325d8ac349c89efbc400f29ff9be740fecda3bc40079f7a5b861bcb8e6a92b` |
| `assets/css/style.css` | **MODIFIED** | `b7269752f629a2849d00e35fa7e930793c01a53af65ce8d875e052a5c297bf57` |

**Not changed (by design):**

- `sections/certificates.twig` — still used on homepage / `/katalog`
- `sections/blockdealersform.twig` — still used on homepage / `/katalog`
- `assets/js/main.js` — dealer form selector unchanged (`.zpm-dealers[data-dealers] .zpm-form`)
- Homepage, `/katalog`, PDP templates/controllers

### Repo (documentation + work artefacts)

| Path | Role |
|------|------|
| `reports/m9.8.9-03-work/blockcommercialtrust.twig` | Source template |
| `reports/m9.8.9-03-work/m9.8.9-03-commercial-trust.css` | CSS patch block |
| `reports/m9.8.9-03-work/live-capture/*` | Pre-deploy FTP capture |
| `reports/m9.8.9-03-work/manifest-capture-*.json` | Capture manifest |
| `reports/m9.8.9-03-work/manifest-complete-*.json` | Post-deploy SHA verify |
| `reports/m9.8.9-03-work/qa-live-probe.json` | QA probe results |
| `backups/category.php.pre-m9.8.9-03-commercial-trust.bak` | Rollback |
| `backups/category.twig.pre-m9.8.9-03-commercial-trust.bak` | Rollback |
| `reports/m9.8.9-03-work/live-capture/style.css` | Pre-patch style.css rollback source |

---

## 2. New Structure

Single section on category PLP:

```
section.zpm-commercial-trust.zpm-dealers[data-commercial-trust][data-dealers]
└── .container
    ├── .zpm-commercial-trust__strip          ← trust row (2 certs + «Все сертификаты»)
    └── .zpm-commercial-trust__split          ← 55% / 45% desktop
        ├── .zpm-commercial-trust__copy       ← H2 + 5 bullets + «Подробнее»
        └── .zpm-commercial-trust__form-card  ← existing dealer form (dialog=7)
```

**Controller (`category.php`):**

- Removed: `$data['certificates']`, `$data['blockdealersform']`
- Added: `$data['blockcommercialtrust']`

**Parent (`category.twig`):**

```twig
{{ seotext }}
{{ blockcommercialtrust }}
```

---

## 3. Certificates Behaviour

| Item | Result |
|------|--------|
| Visible on PLP | **2** compact thumbs (`certificat_00`, `certificat_01`) |
| Slider | **Removed** on PLP (no `.js-certificates-slider`) |
| Fancybox | **Kept** — `data-fancybox="certificates-plp"` (3 links: 2 thumbs + «Все сертификаты») |
| Homepage / katalog | **Unchanged** — legacy slider + `data-fancybox="certificates"` |

### Duplicate certificate files (not auto-fixed)

On **homepage / katalog** (legacy block): **4** fancybox links, **2** unique files:

- `certificat_00.jpg` ×1
- `certificat_01.jpg` ×3 (slides 2–4 duplicate)

PLP merged block shows only the **2 unique** files. Operator should confirm final cert inventory before cleaning legacy `certificates.twig`.

---

## 4. Dealers Form Validation

| Check | Status |
|-------|--------|
| Single form instance per PLP | **PASS** — `forms_dialog7_count: 1` on all 3 PLP URLs |
| `dialog=7` hidden field | **Preserved** |
| `POST /index.php?route=checkout/anketa` | **Unchanged** (JS config untouched) |
| Field IDs (`dealerName`, etc.) | **Preserved** |
| JS hook | Section keeps `zpm-dealers` + `data-dealers` classes for existing `querySelector` |
| Form submit (live POST) | **NOT exercised** in automated QA — operator HITL recommended |

---

## 5. Mobile Layout

CSS stack order @ ≤1024px:

1. Trust strip (horizontal scroll for certs)
2. Copy + bullets + «Подробнее»
3. Form card

Padding reduced vs legacy dealers block (`56px/64px` desktop, `40px/48px` tablet, `32px/40px` small mobile).

---

## 6. QA Results

Automated live probe (`m9.8.9-03-qa-probe.py`) — 2026-06-19:

| Page | URL | commercial_trust | legacy certs section | single form | Pass |
|------|-----|:----------------:|:--------------------:|:-----------:|:----:|
| **Столы** | `/stoly-serii-premium/stoly/` | ✅ | 0 | 1 | ✅ |
| **Моечные ванны** | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | ✅ | 0 | 1 | ✅ |
| **Подтоварники** | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | ✅ | 0 | 1 | ✅ |
| Homepage (control) | `/` | ❌ expected | 1 + slider | 1 | ✅ |
| `/katalog` (control) | `/katalog/` | ❌ expected | 1 + slider | 1 | ✅ |

**Manual / operator follow-up:**

- Fancybox open on cert thumb — visual check recommended
- Form submit end-to-end — HITL
- Browser console — no automated JS error scan in this pass

---

## 7. Rollback

Restore pre-pass files from backups + delete new template:

1. `backups/category.php.pre-m9.8.9-03-commercial-trust.bak` → `catalog/controller/product/category.php`
2. `backups/category.twig.pre-m9.8.9-03-commercial-trust.bak` → `catalog/view/theme/default/template/product/category.twig`
3. `reports/m9.8.9-03-work/live-capture/style.css` → `assets/css/style.css` (remove M9.8.9-03 CSS block)
4. Delete `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` on FTP
5. Clear Twig template cache

Deploy manifests: `reports/m9.8.9-03-work/manifest-complete-20260619-154108.json`

---

## 8. Risks

| Risk | Severity | Notes |
|------|----------|-------|
| Partial deploy window (~2 min) | **Resolved** | First run patched `category.php` before `category.twig`; completed via `m9.8.9-03-deploy-complete.py` |
| Twig cache clear returned 0 files | Low | Pages render correctly; operator may flush cache if stale section seen |
| Form submit not auto-tested | Medium | Endpoint unchanged; HITL submit on one PLP |
| Legacy cert duplicates on home/katalog | Low | Documented; out of PLP scope |
| Copy claims («производство», «гарантия») | Low | Derived from existing dealer/about themes; operator may refine wording |
| `querySelector` single-instance JS | Low | Mitigated by one form per page; `zpm-dealers` class retained on merged section |

---

## Deploy safety log

| Step | Status |
|------|--------|
| FTP capture (6 files) | ✅ `manifest-capture-20260619-153635.json` |
| Backup `.bak` | ✅ `category.php`, `category.twig` |
| Manifest + SHA verify | ✅ `manifest-complete-20260619-154108.json` — `all_deploy_ok: true` |
| Twig cache clear | Attempted (0 entries deleted) |

---

## Git status (this pass)

| Item | Value |
|------|-------|
| Live code | Deployed to TEST only |
| Repo | Work artefacts + this report |
| Commit | **Not performed** |
| Push | **Not performed** |

---

*Implementation pass complete. Awaiting operator visual QA + optional git registration pass.*

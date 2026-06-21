# SITE-002 — Stable Live M9.8.9 Commercial Trust Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-21 (operator-requested stable checkpoint after Commercial Trust redesign + operator manual polish)  
**Mode:** Stable live checkpoint registration — **FTP capture** of commercial-trust files + metadata

---

## 1. Authority state

`SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`

**Current Authority State:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`

**Supersedes:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`

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
| **7** | **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. **§14 Commercial Trust Block** |

Prior repo baselines, work copies (`*-work/`), pass reports (03/03B/03C), and pre-pass `.bak` files are **historical** unless refreshed by live FTP capture.

**Do not** use `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` as current authority — superseded by this checkpoint.

---

## 3. Registration context

This checkpoint supersedes `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` and records the state after:

1. Filter recovery wave (06D–06M) — carried forward
2. Filter UX polish wave (04, 04A, 04B, 07, 08, 08A) — carried forward
3. Wishlist / Compare smart tooltips (01) — carried forward
4. **Commercial Trust block redesign** — M9.8.9-03B (design) · M9.8.9-03C (deploy)
5. **Operator manual visual polish** — post M9.8.9-03C on live TEST (certificate podium, composition, OEM benefits, FAQ grid, form, ZPM logo contours)

---

## 4. Completed work (registered)

### Filter recovery (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-06D — Category 301 Price Index Rebuild** | **active** |
| **M9.8.9-06F — 1C Price Index Hook** | **active** |
| **M9.8.9-06H — Exclude Zero Price From Range** | **active** |
| **M9.8.9-06J — Numeric Attribute Filter Fix** | **active** |
| **M9.8.9-06M — Effective Price Hotfix** | **active** |

### Filter UX (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-07 — Hide Subcategories Filter Block** | **active** |
| **M9.8.9-04 — Filter Scroll Logic** | **active** |
| **M9.8.9-04B — Operator manual JS refinements** | **canonical** — scroll offset **0** |
| **M9.8.9-08 / 08A — Filter Group Reset** | **active** |

### Other UX (carried forward)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-01 — Wishlist / Compare Smart Tooltips** | **active** |
| **M9.8.1 / M9.8.2 / M9.8.5** | **active** |

### Commercial Trust (new in this checkpoint)

| Pass | Status on live |
|------|----------------|
| **M9.8.9-03B — Commercial Trust Block Redesign** | **design complete** — superseded by 03C + operator polish for live truth |
| **M9.8.9-03C — Commercial Trust Block Implementation** | **deployed** — base structure on category PLP |
| **Operator manual Commercial Trust polish** | **canonical** — live TEST overrides 03C repo work copies |

### Operator manual refinements (CANONICAL)

| Pass | Status on live |
|------|----------------|
| **PLP / filter / breakpoint / CSS / Twig polish** | **active** (prior checkpoint) |
| **Commercial Trust manual polish** | **active** — certificate podium, OEM benefits, FAQ grid, form card, logo contours |

---

## 5. Active stable state summary

| Item | Value |
|------|--------|
| Authority | **`SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`** |
| Commercial Trust scope | **Category PLP only** — after product grid, before footer |
| Live commercial-trust files | `blockcommercialtrust.twig` · `style.css` (M9.8.9-03C block + operator CSS) · `category.php` (dynamic headings — unchanged since 03C) |
| Certificate | Enlarged on podium (`sert-base.jpg`); single visible cert; Fancybox on click |
| OEM benefits | 3 items — production, procurement docs, «Сделано в России» |
| Form | `dialog=7`; «Получить прайс-лист» card; decor logo background |
| FAQ grid | 8 cards in separate `zpm-catalog-faq` section |
| Filters / PDP / homepage | **Unchanged** by this checkpoint scope |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — **§14 Commercial Trust Block** |
| Live truth | **hosting state on `zpm.new-site.space`** |

---

## 6. Live capture evidence (2026-06-21)

FTP capture from `polygonws.beget.tech` (TEST):

| Remote path | Bytes | SHA256 |
|-------------|-------|--------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | 13 276 | `6bd6475e924ccc84a3591a91213b59cb4605de274f7bdf8fb18b3bec4ff855b9` |
| `assets/css/style.css` | 293 997 | `60f5bb61be84afabf5d2342944617e390a7a6a4e13bed22831e0fa29b79acd6d` |
| `catalog/controller/product/category.php` | 23 106 | `b4594c74dfc726c96df0cd222e161b6b9c06a702c8f819f6057af530d7049036` |

**Capture folder:** [reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/)  
**Manifest:** [capture-manifest.json](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/capture-manifest.json)

**Note:** `category.php` SHA256 matches M9.8.9-03C deploy — operator polish did **not** alter controller logic.

---

## 7. Pass evidence (repo references)

### Commercial Trust

| Pass | Evidence |
|------|----------|
| 03B | [SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md](../reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md) |
| 03C | [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](../reports/SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) |
| Checkpoint capture | [m9.8.9-commercial-trust-checkpoint-work/live-capture/](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/) |

### Prior checkpoint (superseded)

| Pass | Evidence |
|------|----------|
| Filter UX Complete | [SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md) |

---

## 8. Known open items (not blocking this checkpoint)

| Item | Status |
|------|--------|
| **limit + filter persistence** | **open** — not fixed in this registration |
| **page-intro__description** | **open** — not fixed in this registration |
| **EC-01** | mitigated by subcategories hide (07) |
| M9.8.3/4/6/8 deferred UX passes | **not authorized** |
| **M10** | **not authorized** |

---

## 9. Rollback source

1. **Beget full backup** — full hosting restore
2. **Current live TEST state** — https://zpm.new-site.space/
3. **File-level backups** — `backups/*.pre-m9.8.9-*` incl. commercial-trust pass backups
4. **Checkpoint live capture** — [m9.8.9-commercial-trust-checkpoint-work/live-capture/](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/)
5. **Prior repo STABLE folders** — historical

---

## 10. Rule before next tasks

Before any next SITE-002 change:

1. Read [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Read this checkpoint (latest stable)
3. Verify **Authority State** = `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`
4. For **trust block / certificates / dealers form / category CTA** — read Knowledge Map **§14** + this checkpoint
5. For filter / catalog / 1C / price / PLP — follow Knowledge Map **§13** domain-specific PRE-TASK rule

See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md).

---

## Status

| Field | Value |
|-------|--------|
| Checkpoint type | **STABLE LIVE CHECKPOINT** (FTP capture + metadata) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| Knowledge map | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Rollback source | **Beget full backup + current live TEST + file-level pass backups + checkpoint capture** |
| Deploy (this registration) | **NO** |
| FTP (this registration) | **READ-ONLY capture only** |

---

*Documentation only — no runtime claimed.*

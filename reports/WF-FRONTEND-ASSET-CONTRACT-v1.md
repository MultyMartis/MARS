# WF-FRONTEND-ASSET-CONTRACT-v1

**Document type:** Asset and brand asset law — Phase F6  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22

**Authorities:** [asset-identity-collision-v1.md](../projects/mars-website-factory/failures/asset-identity-collision-v1.md) · [FP-0002-STRESS-TEST-FORENSIC-v1.md](FP-0002-STRESS-TEST-FORENSIC-v1.md) FAIL-004/005/009/017 · [FP-0002-v2-ASSET-INVENTORY-v1.md](FP-0002-v2-ASSET-INVENTORY-v1.md) · [design-source-to-frontend-mapping-governance-v1.md L-07](../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md)

---

## 1. Asset source priority

| Rank | Source | Use |
|------|--------|-----|
| **1** | FIG embedded raster — leaf IMAGE nodes per scope | Primary export path |
| **2** | Operator-supplied files (`INCOMING/03_BRANDING/` when populated) | Brand drops |
| **3** | PDF embedded raster (when FIG export blocked) | Secondary — record provenance |
| **4** | Explicit placeholder (operator-approved, labeled) | Last resort — not for logo |

**Standalone intake status (2026-06-22):** `03_BRANDING/` **empty** — FIG extraction mandatory.

---

## 2. BRAND ASSET LAW

### 2.1 Forbidden heuristics

| Forbidden | Reason |
|-----------|--------|
| **FIRST IMAGE = LOGO** | FAIL-017 Skinerica collision |
| First IMAGE fill in traversal order | Document order ≠ brand |
| First logo-sized rectangle in Header | Multi-brand FIG |
| Lowest node id | Not semantic |
| Export-all without manifest | FAIL-005 orphans |
| FRAME-level image export | FAIL-004 `d3ac7d00` collision hash |

### 2.2 Mandatory Brand Asset Detection Chain

Before wiring logo, favicon source, or institutional mark to `src/img/` or header partial:

```text
1. Candidate discovery — all image nodes in Header/brand scope + logo-band whole-FIG scan
2. Hash grouping — content hash clusters + instance counts
3. Text association — nearest institutional TEXT per cluster
4. Aspect ratio validation — logo-band plausibility
5. Repeated usage analysis — chartered pages vs foreign sections
6. Operator review — if >1 cluster remains plausible → HITL
```

**Gate output (minimum):**

```text
BRAND ASSET CANDIDATES — <n>
BRAND ASSET SELECTED — node <id> — hash <prefix> — confidence HIGH | LOW
BRAND ASSET GATE — PASS | FAIL | PENDING
```

**FP-0002 forensic reference (do not re-use without re-verification):**

| Mark | Node | Hash prefix |
|------|------|-------------|
| **Wrong (Skinerica)** | `1:880` | `de219c6e` — **REJECT** |
| **Correct (Шпиговский дом)** | `1:6720` | `262f79db` — candidate until v2 gate re-run |

### 2.3 Logo handling

| Rule | Requirement |
|------|-------------|
| One approved logo hash per header slot | Record node id + hash in C-09 |
| Re-export on FIG file change | Hash re-validation |
| Alt text | From FIG name or adjacent TEXT — not empty on brand mark |
| SVG vs raster | Use FIG export truth — do not substitute starter logo |

### 2.4 Brand asset handling

| Asset class | Rule |
|-------------|------|
| Favicon | Extract from FIG or client drop — **MISSING** = SAFE UNKNOWN |
| Messenger icons | Real assets or approved icon policy — no invented glyphs |
| Partner/clinic marks in content | Per-component extraction — not frame export |
| Foreign brands in FIG | Down-rank in selection chain — never auto-select |

---

## 3. Image mapping law

Every image in built HTML **must** trace:

```text
section_id → fig_node_id → export_filename → html_src → content_hash
```

| Requirement | Detail |
|-------------|--------|
| **Asset manifest** | Required before section HTML |
| **Unique hash per slot** | No reuse of collision hashes across sections |
| **Leaf selection** | Rank leaf IMAGE by area; exclude FRAME exports |
| **Orphan ban** | Export without HTML reference = FAIL unless marked archival |
| **Component symbols** | `Статья`, `Врач`, etc. — per-instance export — FAIL-008/009 |

---

## 4. Collision prevention

| Failure class | Prevention |
|---------------|------------|
| `d3ac7d00`-class frame hash | Exclude FRAME nodes from export pipeline |
| Same hash, different semantic slots | **STOP** — manual node binding |
| Generic filenames (`image 219`) | Require hash in filename or manifest id |
| 56% orphan exports | Export only manifest-listed nodes |
| CSS gradient placeholders | **REJECT** for `PIXEL_PERFECT` |

---

## 5. Hash validation requirements

| Stage | Check |
|-------|-------|
| Pre-wire | Export file SHA/content hash matches FIG `imageHash` |
| Post-build | HTML `src` resolves to manifest row |
| Pre-VERIFIED | Per-section image hash checklist vs FIG extract |
| Pre-operator accept | Visual spot-check logo + hero + card images |

**Build log vocabulary:**

| Term | Meaning |
|------|---------|
| **BUILT** | Gulp exit 0 — assets copied |
| **VERIFIED** | Manifest + hash diff PASS |

**Forbidden:** `PASS` without VERIFIED asset chain.

---

## 6. Icons and fonts

| Class | Policy |
|-------|--------|
| **Fonts** | Inter via Google Fonts per Production Standards v3 — CDN until self-host drop |
| **Icons** | FIG embedded or approved pack — Font Awesome only if operator authorizes |
| **Stock images** | **Forbidden** without approval |
| **Watermarks** | **Forbidden** |

---

## 7. Contract status

**ASSET CONTRACT LOCKED — YES**

---

*End of contract — v1.*

# FP-0002 V8 O-Centre Content Source Register v1

**Task:** OC-G06 / OC-G10 / OC-G11 reconciliation
**Date:** 2026-06-29

| Candidate | Path | Authority | Content found | Accepted | Reason |
|---|---|---|---|---:|---|
| Spig_v1.2 O-Centre desktop frame | `…/Spig_v1.2.fig` → extract JSON | **1 — Canonical Figma** | Full page text map | Yes | Primary composition + copy source |
| Spig_v1.2 fresh section parse | STORAGE temp raw extract | **1 — Canonical Figma** | 12 desktop sections; no BLK-018 frame | Yes | Confirms steps absence |
| O-Centre node map | `audits/o-centre-asset-content-resolution/data/FP-0002-V8-OCENTRE-FIGMA-NODE-MAP.json` | Charter resolution pack | Block IDs + nodes | Yes | Prior mapping; OC-B05 null |
| Steps forensics note | `…/FP-0002-V8-OCENTRE-STEPS-CONTENT-v1.md` | Resolution pack | `1:2310` = who-we-treat | Yes | Prior finding confirmed |
| FP-0002 Block Inventory BLK-018 row | `FP-0002-BLOCK-INVENTORY-v1.md` L80 | **4 — Canonical inventory** | PG-005 **excluded** from BLK-018 | Yes | Proves inventory error in PG-005 row |
| FP-0002 Block Inventory PG-005 row | `FP-0002-BLOCK-INVENTORY-v1.md` L135 | **4 — Canonical inventory** | Lists `018` on About | Partial | **Rejected for steps** — contradicts BLK-018 row |
| FP-0002 BLK-022 row | `FP-0002-BLOCK-INVENTORY-v1.md` L84 | **4 — Canonical inventory** | Expert opinion on PG-005 | Yes | Founder quote belongs on About |
| founder-quote.html | `src/partials/sections/founder-quote.html` | **3 — Operator-approved V8** | Full quote body + attribution | Yes | CF-004 canonical reuse for BLK-022 |
| Manual polish checkpoint | git `472be1ab` | **1 — Operator decision** | V8 source baseline | Yes | Founder partial approved |
| Spig_v1.2 Home quote export | `REPORTS/_fig_full_build_extract.json` | **6 — Figma export** | Same quote as V8 partial | Yes (supporting) | Confirms quote exists in Spig_v1.2 (non-Lorem frame) |
| O-Centre Figma node 1:2301 | Spig extract | **1 — Canonical Figma** | Lorem ipsum body | No | Placeholder only |
| services-program-v2 (uslugi-v2) | `src/pages/uslugi-v2.html` | **3 — V8 page params** | Program lead/intro (services context) | No | Not exact O-Centre Figma text — semantic similarity insufficient |
| home-rehabilitation-requirements | V8 partial (not on O-Centre) | V8 reuse candidate | Rehabilitation steps pattern | No | No exact O-Centre canonical match |
| Шпиговский.fig | Historical Figma | **9 — Historical only** | — | No | Not authority per task policy |
| V7 O-Centre WIP | fp-0002-shpigovsky-v7 | **8 — Historical** | — | No | Not authority |
| Live site | External | **7 — Supporting only** | — | No | Not used silently |

**Invented content:** none accepted.

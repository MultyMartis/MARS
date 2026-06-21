# FP-0002 — Design → Frontend Mapping QA Record v1

**Document type:** DESIGN → FRONTEND MAPPING QA RECORD (retroactive)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-13  
**QA mode:** **RETROACTIVE** — closes audit finding «Missing Mapping QA RECORD» for evolutionary project path  

**Authority:** [design-source-to-frontend-mapping-governance-v1.md](../../../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md) §8  

**Mapped SSOT (read-only — not modified by this record):** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) — **APPROVED WITH ANDREY CORRECTIONS** (2026-06-13)  

**Scope:** Mapping QA only. **Does not** amend Production Standards, Charter, Start Sequence, or Factory Governance. **Does not** authorize Shell/HTML work or M2 execution.  

**Git status (task):** commit / push **not performed**.

---

## 0. Retroactive context

FP-0002 evolved **before** Factory law mandated an explicit Mapping QA RECORD between Production Standards Draft and Production Standards Approval. v3 was approved without standalone OUT-M01 artifact. This record performs **read-only retroactive verification** of mapping quality already embedded in:

`Numeric Rules v2` → `Frontend Normalization v1` → `Production Standards v1/v2/v3` → **v3 SSOT**

**Process gap closed:** OUT-M01 artifact now exists. **Substantive SSOT unchanged.**

---

## 1. Sources audited (S1–S6)

| Priority | Source class | FP-0002 artifact | Role in v3 formation | Repo evidence |
|----------|--------------|------------------|----------------------|---------------|
| **S1** | Figma / linked frames | — | **Not used** — PROJECT DECISION (PDF-only SoT) | Foundation v1 §Visual source; Page Inventory v1 |
| **S2** | Signed PDF + coordinator numeric rules | **24 PDF** (design pack) | Primary visual evidence | Extraction JSON `REPORTS/fp0002-numeric-extraction-v2.json` (24 files listed); **`INCOMING/01_DESIGN/` empty in repo** |
| **S2** | Coordinator-provided design facts | Olga brief (2026-06-13) | Colors, Inter, H2/body scale, container 1170px, radius note | Integrated in v3 §2, PD-01…PD-04 |
| **S2** | Numeric Design Rules | [FP-0002-NUMERIC-DESIGN-RULES-v2.md](FP-0002-NUMERIC-DESIGN-RULES-v2.md) | Raw measured values from 24 PDF | Evidence JSON; v2 **PENDING** coordinator sign-off on doc itself |
| **S3** | Design pack derivatives | [FP-0002-FRONTEND-FOUNDATION-v1.md](FP-0002-FRONTEND-FOUNDATION-v1.md) | Layout/typography/component taxonomy | Block/Page Inventory cross-ref |
| **S3** | Normalization pass | [FP-0002-FRONTEND-NORMALIZATION-v1.md](FP-0002-FRONTEND-NORMALIZATION-v1.md) | Raw → production token draft | Superseded on conflicts by v3 |
| **S3** | Production Standards lineage | v1 → v2 → **v3** | Draft + Lead corrections → approved SSOT | v3 frozen tokens |
| **S3** | Coordinator content gate | [FP-0002-DESIGN-APPROVAL-SHEET-v2.md](FP-0002-DESIGN-APPROVAL-SHEET-v2.md) | Behavior/content open questions | **Unsigned** — coordinator cells empty |
| **S4** | Excel intake | `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` | IA + search demand (§10–11 v3) | Referenced in v3; file **untracked** in repo snapshot |
| **S5** | Inventories | Page Inventory v1 · Block Inventory v1 | Page/block semantics, L-08 roles | Committed in project folder |
| **S6** | Prior implementation / archive | Home v1 PDF in pack (superseded) | Home **v2** canonical | Page Inventory PROJECT DECISION |

**Mixed-source priority applied in v3:** Olga coordinator facts (S2 verbal/written) **override** PDF pixel samples where documented (PD-02…PD-04, PD-11). PDF remains evidence for unconfirmed tiers (H1, H3, H4, components).

---

## 2. Entry criteria (IN-M01…IN-M05)

| ID | Criterion | Retroactive finding |
|----|-----------|---------------------|
| IN-M01 | Active design source set with S1–S6 priority | **PASS** — PDF pack + Olga + Excel + inventories identified; Figma explicitly excluded |
| IN-M02 | Production Standards Draft C-01–C-16 (or TBD + policy) | **PASS WITH NOTES** — v3 covers layout, type, color, spacing, radius, components, responsive, decisions, open questions, SAFE UNKNOWN; formal C-01–C-16 labels not used (project doc uses §2–§16) |
| IN-M03 | All eight layers L-01–L-08 attempted | **PASS WITH NOTES** — all layers populated in mapping chain; L-06/L-07 carry explicit UNKNOWN (not blank) |
| IN-M04 | Layout chain WF-GRID + WF-LAYOUT + LP-* in C-11 | **PASS WITH NOTES** — functional layout mapped in v3 §3 + Normalization §6; **formal WF-GRID / WF-LAYOUT / LP-* IDs not named** in v3 (evolutionary gap) |
| IN-M05 | Production Decisions (C-12) raw → normalized | **PASS** — v3 §12 PD-01…PD-17 + Normalization raw→production tables |

---

## 3. Layer coverage matrix (L-01–L-08)

Read classes per [source-interpretation-governance.md](../../../projects/mars-website-factory/source-interpretation-governance.md): **Observed · Inferred · UNKNOWN** (Assumed avoided unless cited in PD).

| Layer | Maps to (Factory) | Observed | Inferred | UNKNOWN | Layer verdict |
|-------|-------------------|----------|----------|---------|---------------|
| **L-01 Layout** | C-11, C-07 | Artboards 1437/380 px; section order via Block Inventory; wide vs content sections; card grid col counts (3/4); mobile single-column; sticky bar BLK-004 | Container 1170px (Olga); padding 40/20 (Normalization); breakpoint 1024 (PD-07); TOC 280px+1fr (PD-12); section-gap tokens (PD-16) | Header stack heights; anchor nav control; PG-009 mobile layout; tablet artboard; formal LP-* IDs | **PASS WITH NOTES** |
| **L-02 Typography** | C-02 | PDF font-size histograms (70/36/30/16/18…); Olga H2 36/22 w500; body 18/16 w300; Inter assigned | Line-heights from Normalization; H2 alt 40px; caption 12px; OL-05-adjacent body LH 28/24 | H1 weight; letter-spacing (forbidden by Lead — not in source); font-weight 300 file availability (U-04) | **PASS WITH NOTES** |
| **L-03 Spacing** | C-04, C-05 | Raw gaps 72/56/24/16/32 px (Numeric v2); card gutter 24 | OL-01 scale 4px-base; section 72→80; band 250→240; Factory section-spacing rule (PD-16) | Hero padding-top below header; footer vertical padding exact | **PASS** |
| **L-04 Colors** | C-03 | PDF `#B3261D`, `#3B3D3D`, `#E3EAF2` clusters; Olga `#475371`, `#B3261E`, `#DAE5F0` @ 70% | Elevated/border/footer fallbacks from sampling; error/success placeholders | Hover/focus/error/success interaction colors (OQ-07); effective wash on non-white bases (U-10) | **PASS WITH NOTES** |
| **L-05 Components** | C-08 | Button h44; input h48; card padding 24; FAQ accordion; pagination 40×40; dual header pattern | Header callback 40px; sticky bar 56px/48px touch; radius mapping 30/10/999 (Lead v3) | Header callback exact dims; breadcrumb separator icon | **PASS WITH NOTES** |
| **L-06 States** | C-10 | Default states visible in PDF (flat cards, filled CTA) | Engineering hover darken 8% placeholder; FAQ single-open default | Hover/focus/active/disabled for most controls; modal (M-06); sticky/header z-index | **PASS WITH NOTES** |
| **L-07 Assets** | C-09 | Logo/photo/icon regions visible in PDF layouts | Avatar circular → `radius-pill` 999px | Icon pipeline; logo extraction; font files; PDF pack not in repo for re-export (U-02, U-09) | **UNKNOWN** |
| **L-08 Content** | Semantics | PDF copy roles per block; Excel URL tree + demand sheet | Placeholder policy PD-09 for missing pages; duplicate Home blocks → artifact assumption (OQ-08) | Approval Sheet v2 mostly unsigned; genotyping page design; specialists/about sub-pages copy | **PASS WITH NOTES** |

**LAYER COVERAGE (L-01–L-08):** **PASS WITH NOTES** — L-07 predominantly UNKNOWN; L-06 partial; no silent blank layers.

---

## 4. Layout chain (retroactive reconstruction)

**Governance requirement:** Design Source → WF-GRID → WF-LAYOUT → Layout Pattern (LP-*) → HTML.

```text
PDF pack (24) + Block Inventory
        ↓
   WF-GRID (retroactive)
   • container-max 1170px
   • page-padding-x 40 / 20
   • section vs wide vs full-bleed (v3 §3.2)
   • one page grid contract (desktop-first)
        ↓
   WF-LAYOUT (retroactive)
   • L3 card grids repeat(3|4, 1fr) gap 24
   • L1 hero full-bleed + inner container
   • L2 article TOC 280px + 1fr
   • L4 form 2-col → 1-col collapse @1023
        ↓
   Layout Pattern (inferred — not formally ID’d in v3)
   • LP-02 / LP-05 → 3-col card grids (BLK-009, 011, 014, 015, 028)
   • LP-03 → 4-col grids (BLK-010, 020, 026, 018)
   • LP-04 → hero wide band (BLK-007)
   • LP-06 → article TOC sidebar (PG-009 desktop)
   • LP-08 → collapse to 1 col ≤1023 (CONFIRMED mobile PDF)
        ↓
   Production Standards v3 §3–§9 (SSOT — no HTML in scope)
```

**LAYOUT CHAIN (WF-GRID → WF-LAYOUT → LP-*):** **PASS WITH NOTES** — chain **functionally reconstructible** from Normalization §6 + v3 §3; **LP-* pattern IDs not cited** in approved SSOT (naming debt only; not Design→HTML shortcut).

---

## 5. Mapping QA verification checklist (§8.3)

| Check | Finding | Verdict |
|-------|---------|---------|
| Typography cites source; no arbitrary resize without PD | Type table traces PDF + Olga; deviations (mobile H2, body default, Inter) in PD-04, TY-02 | **PASS** |
| Spacing raw → OL-01 recorded | Normalization §4.2 + v3 §6; PD-05, PD-16 | **PASS** |
| Layout WF-GRID + WF-LAYOUT + LP-* | Functional mapping present; LP IDs absent in v3 | **PASS WITH NOTES** |
| Components: Purpose, Structure, Hierarchy, States, Content | Block Inventory + v3 §8; states incomplete | **PASS WITH NOTES** |
| States: absent → UNKNOWN not invented | v3 §5.3, §13 OQ-07, §15 U-* | **PASS** |
| Assets: complete or blocker | L-07 UNKNOWN flagged; PD-09 placeholder policy | **PASS WITH NOTES** |

**RECONSTRUCTION DRIFT CHECK:** **PASS** — intentional deviations from PDF documented in PD-01…PD-17 and Charter CF-01…CF-06; no forbidden «looks cleaner/modern/better» rationale without rank 1–2 authority.

---

## 6. Production Decisions validation (PD vs sources)

| PD | Mapping claim | Source trace | Validated |
|----|---------------|--------------|-----------|
| PD-01 Inter | Olga | Closes PDF font SAFE UNKNOWN | **Yes** |
| PD-02 Container 1170px | Olga (overrides Normalization 1160, PDF symmetric 1171) | Olga + Numeric v2 ‡ | **Yes** |
| PD-03 Colors Olga set | Olga over PDF `#3B3D3D` / `#B3261D` | Coordinator authority S2 | **Yes** |
| PD-04 Typography Olga tiers | Olga over PDF mobile H2 32, body 16 default | TY-02, TY-03 | **Yes** |
| PD-05 Spacing scale | Normalization OL-01 | Numeric raw → tokens | **Yes** |
| PD-06 Radius 30/10/999 | Lead v3 over PDF 6–8px + Olga «30%» note | Documented override | **Yes** |
| PD-07 Breakpoint 1024 | Lead (PDF had no CSS breakpoint) | Numeric v2 §14 SAFE UNKNOWN → production decision | **Yes** |
| PD-08 Excel intake | Excel file | v3 §10–11 | **Yes** |
| PD-09 Placeholder pages | Lead | Missing PDF pages M-01…M-06 | **Yes** |
| PD-11 rgba wash | Olga 70% over `#FFFFFF` | Differs from PDF solid `#E3EAF2` — disclosed | **Yes** |
| PD-13 Padding 40px | Lead resolves v1 50/40 conflict | Normalization `space-8` | **Yes** |
| PD-14–15 Typography law | Lead v3 | Factory RU rule extension | **Yes** |
| PD-16 Section spacing Factory rule | Lead v3 | frontend-section-spacing-rule-v1 | **Yes** |
| PD-17 Shell-first | Lead v3 | Process — not design mapping | **N/A (process)** |

**Production Decisions validation:** **PASS** — all material raw→SSOT transforms traceable; conflicts explicitly logged.

---

## 7. Design source coverage

| Coverage area | Desktop PDF | Mobile PDF | Coordinator | Excel | Gap |
|---------------|-------------|------------|-------------|-------|-----|
| Home v2 (canonical) | ✓ | ✓ | Partial (dup blocks OQ-08) | — | — |
| G-SERVICE template | ✓ hub/section/leaf | ✓ | — | URL tree N-01…N-05 | 4-level breadcrumbs |
| About | ✓ single | ✓ (390 artifact) | — | 6 sub-pages N-07 | No design for sub-pages |
| Blog hub + article | ✓ hub | ✓ misnamed mobile (PG-008) | OQ-04 | — | Article mobile strategy |
| Contacts, Reviews, Legal, 404 | ✓ | ✓ | OQ-10 breadcrumb | — | — |
| Specialists | — | — | OQ-03 | URL confirmed | **No PDF** |
| Genotyping service | — | — | OQ-09 partial | URL confirmed | **No PDF** |
| Callback modal M-06 | — | — | OQ-01 | — | **No screen** |

**Design Source Coverage verdict:** **PASS WITH NOTES** — core 11 page types covered by PDF pack; missing pages explicitly registered with PD-09 placeholder policy.

---

## 8. Open Questions (from v3 §13 — mapping impact)

| # | Question | Mapping impact |
|---|----------|----------------|
| OQ-01 | Callback modal | L-05/L-06 — behavior UNKNOWN; stub allowed |
| OQ-02 | Review expand | L-08 content scope |
| OQ-03 | Specialists links | L-08 nav target UNKNOWN |
| OQ-04 | Article mobile | **L-01 responsive UNKNOWN** for PG-009 |
| OQ-05 | Icon source | **L-07 UNKNOWN** |
| OQ-06 | Logo/asset extraction | **L-07 blocker for pixel-perfect** |
| OQ-07 | UI states | **L-06 UNKNOWN** |
| OQ-08 | Home duplicate blocks | L-08 — engineering default documented |
| OQ-09 | Genotyping destination | Partially closed via Excel |
| OQ-10 | Contacts breadcrumb | L-08 — fix default |
| OQ-11 | Header heights | **L-01 UNKNOWN** |
| OQ-12 | Excel / IA charter | L-08 structure — intake done, design gaps remain |
| OQ-13 | PDF in repo | Re-verification blocked |
| OQ-14 | FAQ accordion | L-06 engineering default |

**Open Questions:** **PASS WITH NOTES** — all listed in SSOT; none silently omitted from mapping layers.

---

## 9. SAFE UNKNOWN register (mapping-relevant subset)

| ID | Item | Layer | Verify by |
|----|------|-------|-----------|
| U-02 | PDF pack not in committed repo | L-01–L-07 | Restore `INCOMING/01_DESIGN/` |
| U-03 | Header exact heights | L-01 | Measure in Production |
| U-04 | Inter weight 300 | L-02 | Font load test |
| U-06 | rgba wash vs solid bands | L-01/L-04 | Per-block Production |
| U-09 | Icon pipeline | L-07 | Asset intake |
| U-14 | About sub-pages (6) no PDF | L-01/L-08 | Design charter or placeholder |
| U-15 | 4-level breadcrumbs | L-01/L-08 | IA + template extension |

Full list: v3 §15 (unchanged).

**SAFE UNKNOWN discipline:** **PASS** — UNKNOWN-first; no production guesses in mapping SSOT.

---

## 10. Known source ↔ SSOT deltas (not silent drift)

| Domain | PDF / Numeric evidence | v3 SSOT | Authority |
|--------|------------------------|---------|-----------|
| Container | 1160–1171 range | **1170px** | PD-02 Olga |
| Text color | `#3B3D3D` CONFIRMED | `#475371` | PD-03 Olga |
| Accent | `#B3261D` | `#B3261E` | PD-03 Olga (Δ1) |
| Page background | solid `#E3EAF2` | `rgba(218,229,240,0.7)` on `#FFFFFF` | PD-11 |
| Body default | 16px dominant count | **18px** desktop default | PD-04 Olga |
| Mobile H2 | 32px ESTIMATED | **22px** | TY-02 Olga |
| Radius | 6–8px ESTIMATED | **30/10/999px** | PD-06 Lead |
| Section gap | 72px mode | **80px** | Normalization + PD-16 |
| Desktop padding | asymmetric 172/250 | **40px** symmetric | PD-13 |

**Assessment:** deltas are **documented production decisions**, not undetected mapping failures.

---

## 11. Gate outcomes

| Gate line | Verdict |
|-----------|---------|
| **DESIGN → FRONTEND MAPPING QA** | **PASS WITH NOTES** |
| **LAYER COVERAGE (L-01–L-08)** | **PASS WITH NOTES** |
| **LAYOUT CHAIN (WF-GRID → WF-LAYOUT → LP-*)** | **PASS WITH NOTES** |
| **RECONSTRUCTION DRIFT CHECK** | **PASS** |

### 11.1 Notes (written exceptions)

1. **Procedural timing:** Mapping QA RECORD created **after** v3 Approval — acceptable for retroactive closure; Factory law satisfied going forward.
2. **LP-* naming:** Functional layout patterns inferable; formal LP-01–LP-08 IDs **not** embedded in v3 — recommend citation at Shell implementation, **not** SSOT rewrite.
3. **L-07 Assets:** Predominantly **UNKNOWN** — blocks pixel-perfect sign-off, **not** token-based Shell scaffold (per v3 §14).
4. **PDF pack absent in repo:** Limits Observed re-measurement; extraction JSON is evidence proxy only.
5. **Design Approval Sheet v2:** Unsigned — content/behavior mapping relies on engineering defaults + PD-09.

### 11.2 Lead acknowledgment

| Field | Value |
|-------|-------|
| Mapping QA outcome | **PASS WITH NOTES** |
| Retroactive closure | **2026-06-13** |
| Frontend Lead | Андрей (prior v3 Approval attestation 2026-06-13) |
| Process waiver | **Procedural only** — see §12 |

---

## 12. Waiver assessment

| Waiver type | Required? | Rationale |
|-------------|-----------|-----------|
| **Procedural (Mapping QA after Approval)** | **Implicit — closed by this record** | Substantive mapping existed in draft chain; missing artifact only |
| **Substantive (Shell-critical UNKNOWN)** | **No** | v3 Approval already accepted UNKNOWN register + PD-09 placeholders |
| **Layout chain LP-* naming** | **No** | PASS WITH NOTES — non-blocking for approved SSOT; implement-time citation sufficient |

---

## 13. Document control

| Field | Value |
|-------|-------|
| Version | **v1** |
| Created | 2026-06-13 |
| Supersedes | — (first Mapping QA RECORD for FP-0002) |
| Modified upstream docs | **None** |
| Commit / push | Not performed |

---

*Mapping QA RECORD only. Does not reopen Production Standards Approval or authorize code production.*

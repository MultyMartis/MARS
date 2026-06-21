# WF-FRONTEND-IMPLEMENTATION-SEQUENCE-v1

**Document type:** Official frontend implementation order — Phase F3  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v2/` — implementation-free until foundation start authorized.

---

## 1. Operator memory verification

**Historical operator sequence (memory):**

```text
Header → Footer → UI Foundation → Desktop page → Desktop QA → Mobile → Mobile QA → Remaining pages
```

**Verification result:** **PARTIALLY CONFIRMED** — directionally correct for **chrome-before-page**, but **incomplete** and **missing mandatory Factory gates**.

| Memory step | Verdict |
|-------------|---------|
| Header before page body | **CONFIRMED** — ADOPT |
| Footer before page body | **CONFIRMED** — ADOPT |
| UI Foundation before commercial page | **CONFIRMED** — ADOPT (Visual Foundation Contract) |
| Desktop before mobile | **CONFIRMED** — ADOPT (FP-0002 SSOT desktop-first) |
| Desktop QA before mobile | **CONFIRMED** — ADOPT |
| Header before UI Foundation | **CONFIRMED for v2** — successful legacy shell checkpoints; supersedes FP-0002 Start Sequence v1 step 2-before-3 inversion |
| Skip Layout Spec | **REJECTED** — caused FP-0002 header failure |
| Skip Production Standards | **REJECTED** — Factory shell-first Phase 0 |
| Skip text/asset locks | **REJECTED** — stress-test FAIL-002–009 |
| Home as first page | **REJECTED** — pilot slice PG-005 recommended |

---

## 2. What gets built first, second, third

### FIRST — Prerequisites (no page HTML)

| Order | Deliverable | Blocks all code if missing |
|-------|-------------|------------------------------|
| **0.1** | WF-FRONTEND-EXECUTION-CONTRACT v1 (this package) | **Yes** |
| **0.2** | Operator lock: visual authority chain (FIG → PDF → JPG → Operator) | **Yes** |
| **0.3** | Production Standards v3 re-confirmed for v2 FIG evidence | **Yes** |
| **0.4** | Clean Shell verified in v2 workspace | **Yes** |
| **0.5** | Group Register — Header scope | **Yes** |
| **0.6** | Layout Spec — Header — **OPERATOR APPROVED** | **Yes** |
| **0.7** | Group Register — Footer scope | **Yes** |
| **0.8** | Layout Spec — Footer — **OPERATOR APPROVED** | **Yes** |
| **0.9** | Brand Asset Gate — logo hash + nodeId approved | **Yes** |
| **0.10** | Text lock files — Header + Footer zones | **Yes** |

### SECOND — Foundation (shell + UI primitives)

| Order | Deliverable | Gate |
|-------|-------------|------|
| **1** | Global SCSS wiring — abstracts (tokens), base reset, typography defaults | Build PASS |
| **2** | **Header desktop** — HTML partial + SCSS | Layout Spec APPROVED + text lock + brand gate |
| **3** | **Footer desktop** — HTML partial + SCSS | Layout Spec APPROVED + text lock |
| **4** | Shell page entry (foundation slug, not Home) — header + main + footer structure | Build PASS |
| **5** | **Visual Foundation / UI demo** inside `main` | Visual Foundation Contract §3 complete |
| **6** | Design Calibration | CALIBRATION PASS |
| **7** | Foundation QA — desktop | Technical PASS + REPORT |
| **8** | **Operator Visual Review** — foundation desktop | **OPERATOR VISUAL ACCEPT** |
| **9** | **Mobile shell** — header, footer, base typography/spacing overrides | After step 8 |
| **10** | Foundation QA — mobile/responsive | Technical PASS |
| **11** | **Operator Visual Review** — foundation mobile | **OPERATOR VISUAL ACCEPT** |

**P2 gate (WF-PR01):** closes after step **11**.

### THIRD — Pilot page production (PG-005 «О центре»)

| Order | Deliverable | Gate |
|-------|-------------|------|
| **12** | Page-scoped Discovery + Group Register for PG-005 | P1 evidence |
| **13** | Layout Spec per major block — **OPERATOR APPROVED** | Per block |
| **14** | Text lock files per section | Before HTML each section |
| **15** | Asset manifest per section (`section → nodeId → src`) | Before HTML each section |
| **16** | **Desktop page** — block-by-block (max **2–3 sections** per agent run) | Per-block operator visual |
| **17** | Desktop QA — L1–L5 | P3 |
| **18** | **Operator Visual Review** — desktop page | **OPERATOR VISUAL ACCEPT** |
| **19** | **Mobile adaptation** — PG-005 | After step 18 |
| **20** | Mobile QA — L1–L5 | P4 |
| **21** | **Operator Visual Review** — mobile page | **OPERATOR VISUAL ACCEPT** |
| **22** | Visual deviation register final + P5/P6 pilot decision | Pilot close |

### FOURTH — Remaining pages (future charter)

| Order | Deliverable | Gate |
|-------|-------------|------|
| **23+** | Additional page types per Page Inventory v2 | New page charter each |
| **—** | Home PG-001 (15 sections) | **NOT first** — after pilot slice success |

---

## 3. Forbidden before foundation exists

**Do not start until step 11 complete:**

| Forbidden | Reason |
|-----------|--------|
| Home page / PG-001 hero+sections | Shell-first + pilot slice policy |
| Pilot page PG-005 sections | Foundation QA + operator accept |
| Header/Footer without Layout Spec APPROVED | Layout Spec Law |
| Any HTML without Production Standards gate | production-standards-governance |
| Token wiring from legacy `_tokens.scss` copy | Legacy reconciliation REJECT |
| Full-page multi-section agent runs | Stress-test memory/token risk |
| Layout Spec for page blocks before foundation close | Scope control |

---

## 4. Cross-authority reconciliation

| Source | Sequence claim | v2 resolution |
|--------|----------------|---------------|
| [frontend-shell-first-start-protocol-v1.md](../projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md) | Phase 0→5 before Phase 6 | **ADOPT** — maps to steps 0–11 |
| [FP-0002-FRONTEND-START-SEQUENCE-v1.md](../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-FRONTEND-START-SEQUENCE-v1.md) | UI demo step 2 before header step 3 | **ADOPT WITH MODIFICATION** — header/footer before UI demo in main |
| Operator memory | Header → Footer → UI Foundation | **ADOPT** — steps 2–5 |
| [WF-PR01-PILOT-READINESS-CONTRACT-v1.md](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md) | P0→P6 gates | **ADOPT** — mapped to steps above |
| Legacy stress-test | 14 sections one run | **REJECT** |

---

## 5. Implementation order — LOCKED

```text
PREREQUISITES (authority, standards, clean shell, layout specs, brand gate, text locks)
    ↓
TOKENS + RESET
    ↓
HEADER DESKTOP
    ↓
FOOTER DESKTOP
    ↓
SHELL PAGE + UI FOUNDATION DEMO
    ↓
DESIGN CALIBRATION → FOUNDATION QA DESKTOP → OPERATOR VISUAL ACCEPT
    ↓
MOBILE SHELL → FOUNDATION QA MOBILE → OPERATOR VISUAL ACCEPT
    ↓
PG-005 DISCOVERY / LOCKS / LAYOUT SPECS
    ↓
DESKTOP PAGE (block-by-block) → DESKTOP QA → OPERATOR VISUAL ACCEPT
    ↓
MOBILE PAGE → MOBILE QA → OPERATOR VISUAL ACCEPT
    ↓
REMAINING PAGES (future charter)
```

**IMPLEMENTATION ORDER LOCKED — YES**

---

*End of sequence — v1.*

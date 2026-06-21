# MARS Website Factory — Website Factory Enforcement Pack v1

**Status:** **documented** — canonical **human-operated** enforcement layer for Website Factory frontend QA.  
**Not:** runtime orchestration, CI gate, automated linter, parser, or enforcement engine.

**Purpose:** Close the enforcement gap identified after **FP-0002 M2 ROOT CAUSE AUDIT** — Foundation Health was high, but the system could verify completeness, structure, WF-GRID, WF-LAYOUT, and token **presence** without guaranteed verification of **actual compiled CSS/HTML**, **inline styles**, **Operator Law compliance**, or **rank-1 exception handling**.

**Provenance:** FP-0002 M2 false PASS — governance could pass source-level and structural checks while compiled output and authority conflicts remained undetected.

**Scope boundary:** This pack updates **Website Factory governance docs only**. It does **not** modify FP-0002 workspace artefacts, `ui-demo`, or any project instance.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Peer integration (minimal deltas — architecture preserved):**

| Preserved chain | Role |
|-----------------|------|
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | Authority hierarchy + Exception Registry + Authority Conflict Protocol |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Rank-1 SSOT process |
| [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) | Foundation QA chain |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Mapping QA chain |
| [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md) | Canonical route RAW VIOLATION → gate verdict |
| [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) | FAILURE EVENT → Expected Gate → Attribution Verdict (post-escape investigation) |

---

## 1. Root cause validation

| Symptom (FP-0002 M2 audit) | Prior governance gap | Enforcement Pack v1 response |
|----------------------------|----------------------|------------------------------|
| Foundation QA **PASS** while compiled CSS contained OL violations | Checks relied on source SCSS + token presence, not **`dist/*.css`** | **Compiled CSS Compliance Audit** gate (§3.2) |
| Inline styles undetected | No inline-style gate or allowlist | **Inline Style Compliance Audit** gate + [frontend-inline-style-allowlist-v1.md](frontend-inline-style-allowlist-v1.md) |
| Project SSOT overrode Operator Law without trace | Rank-1 vs rank-2 conflict treated as implicit win | **Authority Conflict Protocol** (§5) + **Exception Registry** (§4) |
| Operator Law drift not a separate verdict | DQ-02 mixed SSOT and OL | **DQ-02a** / **DQ-02b** split in matrix |
| PASS without source + compiled + HTML cross-check | No ROOT rollup | **ROOT COMPLIANCE** block (§6) — mandatory before PASS |

**Honesty boundary:** Gates are **human-operated documentation discipline**. They do **not** claim an in-repo automated audit engine unless a project explicitly adopts checklists as tooling.

---

## 2. New gates (summary)

| Gate ID | Name | Mandatory at | Verdict vocabulary |
|---------|------|--------------|-------------------|
| **EG-01** | Operator Law Compliance | Design Calibration rollup · Foundation QA · page QA | PASS · PASS WITH NOTES · FAIL · **WAIVED** · UNKNOWN |
| **EG-02** | Compiled CSS Compliance | Design Calibration (spot-check) · Foundation QA · page QA | PASS · PASS WITH NOTES · FAIL · **WAIVED** · UNKNOWN |
| **EG-03** | Inline Style Compliance | Foundation QA · page QA | PASS · PASS WITH NOTES · FAIL · **WAIVED** · UNKNOWN |
| **EG-04** | Authority Conflict Status | Foundation QA · page QA · ROOT COMPLIANCE | PASS · FAIL · **WAIVED** · UNKNOWN |
| **EG-05** | ROOT COMPLIANCE (technical review rollup) | Foundation QA · page Production PASS | PASS · FAIL · UNKNOWN |

**Rule:** **FINAL VERDICT — PRODUCTION PASS** is **forbidden** when **ROOT COMPLIANCE — FAIL** or **UNKNOWN**.

Detail authority:

| Gate | Document |
|------|----------|
| EG-01 | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §3 · [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2 |
| EG-02 | This doc §3.2 · [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) §5.7 |
| EG-03 | [frontend-inline-style-allowlist-v1.md](frontend-inline-style-allowlist-v1.md) |
| EG-04 | This doc §5 · authority-order §7 |
| EG-05 | This doc §6 · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.4 |

---

## 3. Compliance model

### 3.1 Operator Law Compliance Gate (EG-01)

**Question:** Do **compiled and source** spacing/type/layout values obey **Approved Operator Laws (OL-01–OL-07)** unless a valid rank-1 exception is recorded?

**Inspect:**

- `gap`, `grid-gap`, `column-gap`, `row-gap` — OL-01 gap scale
- `margin`, `padding` (all longhands and shorthands) — OL-01 margin/padding scale
- Percentage padding — OL-02 scope
- Layout pattern / `%` splits — OL-03, OL-04
- Line-height pairs — OL-05
- Forbidden typography properties (`letter-spacing`, `word-break`, `overflow-wrap`, `hyphens`) — OL-06; **property presence = FAIL**

**Sources (both required when build succeeds):**

- `src/scss/**` (authoritative intent)
- `dist/*.css` (compiled truth)

**Verdicts:**

| Verdict | When |
|---------|------|
| **PASS** | No OL violations in scope |
| **PASS WITH NOTES** | Minor/Observation only; no Critical/Major open |
| **FAIL** | OL violation without valid Exception Registry record |
| **WAIVED** | Rank-1 value conflicts with OL **and** Exception Registry record complete (§4) |
| **UNKNOWN** | Build failed; CSS not inspected; scope incomplete |

### 3.2 Compiled CSS Compliance Audit (EG-02)

**Separate mandatory gate** — not substitutable by source-only SCSS review.

**Method:**

1. Run `npm run build` — gate **UNKNOWN** if build fails without HITL scope.
2. Inspect **`dist/*.css`** (primary) and cross-check originating rules in **`src/scss/**`**.
3. Sample foundation demo URL selectors + global partials + layout partials at minimum.

**Check categories:**

| Category | OL / authority |
|----------|----------------|
| `gap` values | OL-01 |
| `margin` / `padding` values | OL-01 · OL-02 |
| Operator-law-controlled line-heights | OL-05 |
| Forbidden typography properties (`letter-spacing`, `word-break`, `overflow-wrap`, `hyphens`) — **property presence = FAIL**; grep `src/scss/**` + `dist/*.css` — required count **0** per property | OL-06 |

**Verdict:** Same vocabulary as EG-01.

**Design Calibration obligation:** **COMPILED CSS SPOT-CHECK** — subset of EG-02 on demo page selectors before Foundation QA. Source-only SCSS review **does not** satisfy calibration.

### 3.3 Inline Style Compliance Audit (EG-03)

**Question:** Does compiled HTML contain inline `style=""` attributes outside the allowlist?

**Sources:**

- `dist/**/*.html` (compiled)
- `src/**/*.html` / partials (authoritative)

**Disposition per hit:**

| Disposition | Meaning |
|-------------|---------|
| **ALLOWED** | Matches [frontend-inline-style-allowlist-v1.md](frontend-inline-style-allowlist-v1.md) |
| **FORBIDDEN** | Not on allowlist; no waiver |
| **WAIVED** | Not on allowlist; Lead exception recorded with decision id |

**Gate rollup:**

| Verdict | When |
|---------|------|
| **PASS** | Zero FORBIDDEN hits |
| **PASS WITH NOTES** | FORBIDDEN cleared or downgraded to Observation with Lead ack |
| **FAIL** | Any FORBIDDEN hit without waiver |
| **WAIVED** | Only WAIVED dispositions remain for non-allowlisted hits |
| **UNKNOWN** | HTML not inspected |

---

## 4. Exception Registry model

When **Project Production Standards (rank 1)** intentionally violate **Approved Operator Laws (rank 2)**, operators **must** record an exception **before** claiming **WAIVED** on EG-01, EG-02, or EG-04.

**Mandatory fields (all required — missing any → FAIL, not WAIVED):**

| Field | Content |
|-------|---------|
| **decision id** | Stable id — e.g. `C-12-EX-001`, Production Decisions row, or project change-control id |
| **owner** | Named Lead or Frontend Lead |
| **justification** | Why rank-1 value is required; design/measurement citation |
| **authority citation** | `Rank 1: <PROJECT>-PRODUCTION-STANDARDS-APPROVAL-vN §…` overriding `Rank 2: OL-0N` |

**Storage (human-operated — pick one per project):**

- Production Standards **Production Decisions (C-12)** table
- Project change-control appendix linked from SSOT
- Foundation QA / page QA REPORT **Exception Registry** subsection

**Without complete record:** verdict **FAIL** — never **PASS**, never silent rank-1 win.

**Cross-ref:** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §7.

---

## 5. Authority Conflict Protocol

Official mechanism for **Rank 1 vs Rank 2** conflicts (primarily **Project Production Standards vs Operator Law**).

| Situation | Verdict | Unblocks PASS? |
|-----------|---------|----------------|
| Rank-1 value matches OL | No conflict | **AUTHORITY CONFLICT STATUS — PASS** |
| Rank-1 differs from OL; **no** Exception Registry record | Conflict unresolved | **FAIL** |
| Rank-1 differs from OL; **complete** Exception Registry record | Documented override | **WAIVED** |
| Conflict scope not reviewed | Evidence gap | **UNKNOWN** |

**Examples:**

| Conflict | Exception record | AUTHORITY CONFLICT STATUS |
|----------|-------------------|---------------------------|
| SSOT gap token `64px` vs OL-01 scale | **None** | **FAIL** |
| SSOT gap token `64px` vs OL-01 scale | **Complete** §4 record | **WAIVED** |
| SSOT line-height exception vs OL-05 | **Complete** record citing named tier | **WAIVED** |

**Agent stop:** Implementing rank-1 value that violates OL without Exception Registry → **STOP** — record exception or map to OL scale.

---

## 6. ROOT COMPLIANCE (technical review block)

Mandatory rollup before any **Foundation QA PASS** or **Production PASS**.

**Question:** Does evidence chain cover **source**, **compiled CSS**, **compiled HTML**, **authority conflicts**, and **exception registry**?

| Sub-check | Source | Blocks ROOT PASS if |
|-----------|--------|---------------------|
| **Source SCSS/HTML** | `src/scss/**`, `src/**` partials | Not reviewed when build green |
| **Compiled CSS** | `dist/*.css` | EG-02 **FAIL** or **UNKNOWN** |
| **Compiled HTML** | `dist/**/*.html` | EG-03 **FAIL** or **UNKNOWN** |
| **Authority conflicts** | SSOT vs OL diff list | EG-04 **FAIL** or **UNKNOWN** |
| **Exception registry** | C-12 / REPORT subsection | Any conflict lacks §4 fields |

**ROOT COMPLIANCE verdict:**

| Verdict | When |
|---------|------|
| **PASS** | All sub-checks satisfied; EG-01–EG-04 not **FAIL** |
| **FAIL** | Any sub-check **FAIL**; or EG-04 **FAIL** |
| **UNKNOWN** | Build/evidence incomplete |

**Hard rule:** **PASS** on Foundation QA or **FINAL VERDICT — PRODUCTION PASS** is **impossible** without **ROOT COMPLIANCE — PASS**.

**REPORT block:** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.4.

---

## 7. Gate placement (additive — chains unchanged)

```text
… → Design Calibration (+ COMPILED CSS SPOT-CHECK)
        ↓
Foundation QA (+ EG-01..EG-05 + ROOT COMPLIANCE)
        ↓
Home Production
        ↓
Design Completeness → Frontend Design QA Matrix (+ EG-01..EG-03, DQ-02a/b)
        ↓
Pixel Fidelity → Production PASS (+ ROOT COMPLIANCE)
```

Mapping QA chain and Production Standards governance **unchanged**.

---

## 8. FP-0002 impact

| Item | Impact |
|------|--------|
| FP-0002 workspace artefacts | **Not modified** by this pack |
| Historical M2 PASS | **Not retroactively rewritten** — audit finding stands |
| Future FP-0002 rollback + M2 rebuild | New gates would catch compiled CSS / inline / OL / authority gaps **if** operators run updated checklist |
| FP-0002 v3 SSOT | Remains rank-1 authority — conflicts require Exception Registry per §4 |

---

## 9. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Website Factory Enforcement Pack: EG-01–EG-05 gates; Exception Registry; Authority Conflict Protocol; ROOT COMPLIANCE; closes FP-0002 M2 enforcement gap. |
| 2026-06-14 | v1.1 — Compliance Decision Model Pack: peer cross-ref; EG gates consume Stage 6 gate verdict. |

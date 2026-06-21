# FP-0002 — Frontend Start Sequence v1

**Document type:** Project execution sequence — Frontend Foundation before Home  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-13  

**Factory protocol:** [frontend-shell-first-start-protocol-v1.md](../../../projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md)  
**Production Standards SSOT:** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md)  
**Section spacing:** [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) §4  

**Phase:** Pre–Frontend Production Charter — **sequence only, no code**  
**Approved by:** Андрей (via Production Standards v3 corrections)

---

## Mandatory order

| Step | Name | Scope | Deliverable | Gate |
|------|------|-------|-------------|------|
| **1** | Base shell | Layout frame | `header` + `main` + `footer` partials; shell page entry (not Home) | Build includes layout |
| **2** | Typography / UI demo in `main` | Foundation page content | H1–H6, body, lists, links, buttons, form fields, quote block, spacing samples, tables if needed | Visible on demo URL |
| **3** | Header desktop | BLK-001 + BLK-002 | Dual-row header desktop styles | Desktop ≥1024px QA |
| **4** | Footer desktop | BLK-003 | Footer multi-column desktop | Desktop QA |
| **5** | Global styles | Tokens + base | Inter, colors, radius (30/10/999), spacing scale, default content styles, logo/favicon/assets | Matches Production Standards v3 |
| **6** | Mobile header / footer / base | Responsive shell | Condensed header, footer stack, mobile spacing reduction, BLK-004 sticky if active | Mobile ≤1023px QA |
| **7** | QA foundation | Verification | `# REPORT — FP-0002 foundation QA`; shell-first checklist PASS | Lead ack |
| **8** | Home page production | PG-001 | Home v2 blocks per Block Inventory — **only after step 7** | Per-page charter |

---

## Step detail

### Step 1 — Base shell

- Page entry: **`ui-demo.html`** (or agreed foundation slug) — **not** `index.html` Home.
- Structure:

```text
header (layout partial)
main
  └── typography / UI demo sections only
footer (layout partial)
```

- No Home hero (BLK-007) at this step.

### Step 2 — Typography / UI demo

Implement all Production Standards v3 tokens visibly:

| Sample | Standard reference |
|--------|-------------------|
| H1 Display 70/42 | v3 §4.1 |
| H2 Section 36/22 w500 | v3 §4.1 |
| Body 18/16 w300 | v3 §4.1 |
| Primary button | v3 §8.1 — radius **30px** |
| Input field | v3 §8.2 — radius **10px** |
| Card sample | radius **30px** |
| Spacing labels | same-bg 80px / band 240px samples |

### Step 3–4 — Header / footer desktop

- Container **1170px**, padding **40px** desktop / **20px** mobile.
- Header heights: measure in production (OQ-11) — engineering placeholders allowed.
- Footer vertical padding: **80px** (`space-12`) default.

### Step 5 — Global styles

- **Desktop-first** CSS (`min-width: 1024px` for grid activation).
- **Forbidden** without Lead approval + Exception Registry: `letter-spacing`, `word-break`, `overflow-wrap`, `hyphens` — **any value**; property presence in CSS = FAIL.
- RU typography: [russian-no-word-splitting-typography-v1.md](../../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md).

### Step 6 — Mobile shell

- Breakpoint **1023px** max for mobile layout.
- Section gap mobile default **64px** where applied.
- Sticky bar BLK-004: 56px bar, 48px touch targets.

### Step 7 — QA foundation

REPORT must include:

- Build evidence
- Screenshot or viewport list (desktop + mobile)
- Token spot-check vs v3
- `SECTION SPACING — PASS | partial | FAIL`
- `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN`

### Step 8 — Home page

- Start only after Step 7 PASS or explicit Lead waiver.
- Follow Frontend Production Charter (when issued) + Block Inventory.

---

## Explicit exclusions (this document)

- Does **not** authorize Home page work before Step 7.
- Does **not** modify Page Inventory, Block Inventory, WordPress Architecture, ACF Architecture.

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Created | 2026-06-13 |
| Commit / push | Not performed |

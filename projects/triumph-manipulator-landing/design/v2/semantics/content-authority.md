# V2 — Content authority

**Purpose:** Classify copy so Forge / frontend agents know what **must match** mocks vs what may flex. **Documentation only** — not runtime enforcement.

## Source discipline

| Classification | Authority for V2 |
|----------------|------------------|
| **LOCKED / FLEXIBLE / below** | Resolved from **`design/v2/*.png`** + operator written instruction |
| **`design/v1/`** | **Not** a content source for V2 |
| **`design/shared-assets/`** | Filenames/paths do **not** authorize copy |

---

## LOCKED copy (preserve exactly)

Applies to any string **visible** on the active `NN.png` for the current implementation step, including:

- **H1 / H2 / H3** and lead lines shown in mock
- **CTA labels** on primary buttons and form submit
- **Key numeric claims** tied to offer (e.g. 5 t, 3 t, 14 m) where shown as part of the approved visual
- **Legal / compliance** snippets visible in footer or trust sidebar on `07.png` / `03.png` (once mock is final)
- **Parameter labels** in checklists where they are part of the composition (e.g. consultation block)

**Rule:** No paraphrase, no SEO “optimization,” no translation unless operator owns translation source.

---

## FLEXIBLE copy (adapt with constraints)

- **Alt text** for images — descriptive, non-marketing; must not contradict visible facts or **LOCKED** claims.
- **`aria-label` / accessibility strings** — may clarify control role; must not invent new **offers** or **fleet** implications.
- **Microcopy** for validation errors (form) — technical UX only; keep tone neutral; no new product promises.

---

## GENERATED copy

**Default:** **forbidden** for V2 homepage sections mapped to **`design/v2/`**.

**Only allowed** when:

- operator supplies text, or
- task explicitly marks content as **PLACEHOLDER** pending operator, or
- content is **purely structural** (e.g. “Row 4” in an internal scaffold) — **must not ship as user-visible marketing**.

---

## PLACEHOLDER areas

Sections whose mocks imply rich content but implementation is still shell-only (per matrices):

- `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, `site-footer-v2`

**Rules:**

1. Use **non-marketing** stub labels or **SAFE UNKNOWN** in docs — not believable fake brands, INN, or chat logs.
2. Do **not** backfill from **`design/v1/`** or competitor sites.
3. When filling: pull **only** from corresponding **`NN.png`** or operator brief, then re-classify as **LOCKED**.

---

## Agent decision table

| Situation | Action |
|-----------|--------|
| String on current `NN.png` | **LOCKED** — match visually approved export |
| String not on mock, section in scope | **STOP** — SAFE UNKNOWN / operator |
| Error message / aria | **FLEXIBLE** within honesty constraints |
| Fleet / multi-machine promo on single-machine screens | **FORBIDDEN** |

# WF-FRONTEND-TEXT-FIDELITY-CONTRACT-v1

**Document type:** Text fidelity law — Phase F5  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Production mode:** `PIXEL_PERFECT`

**Authorities:** [WF-PR01-PILOT-READINESS-CONTRACT-v1.md §12](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md) · [pixel-fidelity-audit-rules-v1.md §0.4](../projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md) · [FP-0002-STRESS-TEST-FORENSIC-v1.md](FP-0002-STRESS-TEST-FORENSIC-v1.md) FAIL-002/003/006 · [design-source-to-frontend-mapping-governance-v1.md L-08](../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md)

---

## 1. Canonical text source

| Rank | Source | Use |
|------|--------|-----|
| **1** | FIG `textData.characters` (per bound node id) | Primary visible copy |
| **2** | PDF text layer / operator-verified export | Cross-check; static pages |
| **3** | Operator-approved text lock file | Frozen strings before HTML |
| **4** | Operator verbal/written lock | Tie-break only — must be recorded |

**Forbidden as text source:** agent paraphrase; lorem ipsum; generic marketing filler; reference-block demo copy; flat extract that skips INSTANCE subtrees.

---

## 2. Mandatory answers

| Question | Answer | Authority |
|----------|--------|-----------|
| **Can text be rewritten?** | **NO** | WF-PR01 §12; stress-test FAIL-003 |
| **Can text be completed?** | **NO** | Missing copy = UNKNOWN, not completion |
| **Can unreadable text be guessed?** | **NO** | Header Text Lock v5.2 pattern; SAFE UNKNOWN |
| **Can marketing text be generated?** | **NO** | FAIL-002 reviews; FAIL-008 specialists; FAIL-013 FAQ |

**Exception:** Operator **explicitly authorizes** an edit in writing — recorded as `TEXT OVERRIDE — APPROVED — <scope>` with before/after evidence. Without record = **REJECT**.

---

## 3. Text lock protocol

Before HTML generation for any scoped block:

| Step | Output |
|------|--------|
| 1. Walk FIG INSTANCE subtrees for component types in scope | Node id list |
| 2. Extract `textData.characters` per node | String + hash |
| 3. Write `text-lock-<scope>-vN.json` (or equivalent) | Frozen SSOT for builder |
| 4. Operator ack on conflict deltas | C-12 or lock amendment |
| 5. Diff gate: built HTML vs lock | **VERIFIED** or **FAIL** |

**Component types requiring INSTANCE walk (minimum):** `отзыв` · `Врач` · `Статья` · `Пункт услуги` · `Услуга` · `этап` · `Расскрытие вопроса` · disclaimer strings attached to price blocks.

---

## 4. Russian HTML typography (text layer)

| Rule | Requirement |
|------|-------------|
| Short prepositions/conjunctions | `&nbsp;` binding per [russian-no-word-splitting-typography-v1.md](../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md) |
| Typograph scope | Headings, body, buttons, links, cards, forms |
| Do not typograph | `meta`, URLs, `href`, `data-*`, JSON-LD, code |
| Multi-paragraph FIG nodes | Preserve `\n` as separate `<p>` — FAIL-013 lesson |

---

## 5. Missing text handling

```text
IF extract_missing OR unreadable:
  EMIT: SAFE UNKNOWN — TEXT — <node-id or field>
  BUILD: omit or placeholder marker in REPORT only — NOT in production HTML
  STATUS: BLOCKED for VERIFIED until operator supplies text or WAIVE
```

**Forbidden:** generic «Специалист центра», invented review paragraphs, inferred FAQ answers, shortened lead paraphrase.

---

## 6. QA gate

Every section REPORT must include:

```text
TEXT FIDELITY — PASS | FAIL | SAFE UNKNOWN
TEXT LOCK REF — <file> — hash <prefix>
GENERATIVE FILL DETECTED — YES | NO
```

**GENERATIVE FILL DETECTED — YES** → automatic **REWORK REQUIRED**; pilot failure class.

---

## 7. Contract status

**TEXT FIDELITY LOCKED — YES**

---

*End of contract — v1.*

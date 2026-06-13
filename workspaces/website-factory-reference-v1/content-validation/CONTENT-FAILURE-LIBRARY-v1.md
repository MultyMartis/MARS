# Website Factory — Content Failure Library v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** catalog of common content validation failures — **documentation only**  
**Связь:** [CONTENT-SEVERITY-SYSTEM-v1.md](CONTENT-SEVERITY-SYSTEM-v1.md), [CONTENT-SIGNAL-VALIDATION-MATRIX-v1.md](CONTENT-SIGNAL-VALIDATION-MATRIX-v1.md)

---

## Назначение

Failure Library v1 документирует **типовые** отклонения content signal architecture. Каждая запись: cause → impact → severity → recommended correction.

**Format:**

| Field | Content |
|-------|---------|
| **ID** | Stable failure code `CVF-###` |
| **Scenario** | Human-readable description |
| **Cause** | Why it happens |
| **Impact** | Trust / legal / conversion risk |
| **Severity** | INFO / WARNING / ERROR / CRITICAL |
| **Recommended correction** | Operator action |

---

## HERO / conversion

### CVF-001 — Missing offer in HERO

| Field | Value |
|-------|-------|
| **Scenario** | `HERO` block architecture lacks satisfiable `offer` signal |
| **Cause** | Design started before content contract; headline-only wireframe |
| **Impact** | No value anchor; downstream blocks lack coherence |
| **Severity** | ERROR |
| **Recommended correction** | Declare `offer` slot in HERO architecture; align with page-level `offer`; re-run block validation |

---

### CVF-002 — Missing CTA in HERO

| Field | Value |
|-------|-------|
| **Scenario** | `HERO` lacks `cta` signal binding |
| **Cause** | Visual-only hero; conversion deferred to footer only |
| **Impact** | Primary action path undefined above fold |
| **Severity** | ERROR |
| **Recommended correction** | Add `cta` to HERO; ensure single primary per page (CT-R19) |

---

### CVF-003 — Missing benefit in HERO

| Field | Value |
|-------|-------|
| **Scenario** | `HERO` has `offer` but no `benefit` |
| **Cause** | Tagline treated as offer; benefits only in BENEFITS block but HERO contract requires both |
| **Impact** | Incomplete HERO contract; weak value articulation |
| **Severity** | ERROR |
| **Recommended correction** | Add `benefit` slot to HERO or document OR-exception in project IA (HITL) |

---

## Forms / legal

### CVF-004 — Missing consent in LEAD_FORM

| Field | Value |
|-------|-------|
| **Scenario** | `LEAD_FORM` architecture without `consent` signal |
| **Cause** | Form mockup without Legal Pack adjacency |
| **Impact** | GDPR/personal data processing gate failure |
| **Severity** | CRITICAL |
| **Recommended correction** | Bind `consent` per Legal Pack Consent Rule; link to legal routes |

---

### CVF-005 — Missing legal disclosure on LEGAL_PAGE

| Field | Value |
|-------|-------|
| **Scenario** | `LEGAL_PAGE` without `legal_disclosure` binding to Pack document |
| **Cause** | Generic text page; wrong page_type |
| **Impact** | Legal Pack non-compliance |
| **Severity** | CRITICAL |
| **Recommended correction** | Apply LEGAL-PAGE-CONTRACT + Legal Pack document ref; remove marketing signals |

---

### CVF-006 — Missing legal disclosure in LEGAL_LINKS

| Field | Value |
|-------|-------|
| **Scenario** | Production site; `LEGAL_LINKS` without link-target architecture for required L1–L4 |
| **Cause** | Footer stub; Legal Pack not mapped |
| **Impact** | Compliance surface incomplete |
| **Severity** | ERROR |
| **Recommended correction** | Map `legal_disclosure` targets per SITE-TYPE-LEGAL-MAPPING-v2 |

---

## Trust / evidence

### CVF-007 — Fake proof signal

| Field | Value |
|-------|-------|
| **Scenario** | `proof` declared without HITL_REQUIRED or SOURCE_DOCUMENTED plan |
| **Cause** | Placeholder metrics; invented client count |
| **Impact** | Misrepresentation; regulatory risk |
| **Severity** | CRITICAL |
| **Recommended correction** | Remove proof binding until evidence documented; or downgrade to non-metric trust |

---

### CVF-008 — Fake review signal

| Field | Value |
|-------|-------|
| **Scenario** | `review` on REVIEWS/TESTIMONIALS without UGC_AUTHENTIC |
| **Cause** | Fabricated testimonials labeled as reviews |
| **Impact** | Consumer protection / platform policy risk |
| **Severity** | CRITICAL |
| **Recommended correction** | Use TESTIMONIALS curated quote with HITL; remove `review` until authentic UGC source |

---

### CVF-009 — Missing trust signal on TRUST block

| Field | Value |
|-------|-------|
| **Scenario** | `TRUST` block present (page-block PASS) but `trust` signal not satisfiable |
| **Cause** | Logos only wired visually; no trust architecture |
| **Impact** | Block content contract unmet |
| **Severity** | ERROR |
| **Recommended correction** | Declare `trust` + `proof` per BLOCK-CONTENT-CONTRACTS |

---

## Placeholder / quality

### CVF-010 — Placeholder leakage

| Field | Value |
|-------|-------|
| **Scenario** | Architecture slots contain `TBD`, lorem, `[COMPANY]`, `{{token}}` |
| **Cause** | Template export bound to production gate prematurely |
| **Impact** | Production embarrassment; entity mismatch |
| **Severity** | ERROR |
| **Recommended correction** | Mark slots unfilled in architecture doc; do not pass validation until slots defined (not copy-filled — structure only) |

---

## Page-level / contradiction

### CVF-011 — Contradictory signals

| Field | Value |
|-------|-------|
| **Scenario** | `payment` + RFQ-only CATALOG Blueprint on same PDP |
| **Cause** | Mixed ecommerce and catalog patterns |
| **Impact** | Wrong commerce model; legal scope unclear |
| **Severity** | CRITICAL |
| **Recommended correction** | Halt; align Blueprint site type; remove forbidden commerce signals |

---

### CVF-012 — Forbidden payment on LANDING_PAGE

| Field | Value |
|-------|-------|
| **Scenario** | `payment` signal on `LANDING_PAGE` or `HERO` |
| **Cause** | Shop components reused on landing |
| **Impact** | Site model violation |
| **Severity** | CRITICAL |
| **Recommended correction** | Remove signal; reclassify to ECOMMERCE if checkout intended |

---

### CVF-013 — Marketing signals on LEGAL_PAGE

| Field | Value |
|-------|-------|
| **Scenario** | `offer`, `benefit`, `cta` primary on `LEGAL_PAGE` |
| **Cause** | Shared marketing template |
| **Impact** | Legal Pack violation |
| **Severity** | CRITICAL |
| **Recommended correction** | Strip to `legal_disclosure` + `entity_identity` only |

---

## PRICING / commerce blocks

### CVF-014 — Missing price on PRICING block

| Field | Value |
|-------|-------|
| **Scenario** | `PRICING` REQUIRED without `price` signal architecture |
| **Cause** | Visual tiers without commerce stance |
| **Impact** | Pricing block contract fail |
| **Severity** | ERROR |
| **Recommended correction** | Declare `price` (listed or RFQ stance per Blueprint) + `cta` |

---

### CVF-015 — Missing delivery on CHECKOUT

| Field | Value |
|-------|-------|
| **Scenario** | `CHECKOUT` without `delivery` |
| **Cause** | Digital-only assumption on physical goods site |
| **Impact** | ECOMMERCE checkout contract fail |
| **Severity** | ERROR |
| **Recommended correction** | Add `delivery` architecture or document digital-only charter |

---

## FAQ / support

### CVF-016 — FAQ block without question/answer pair

| Field | Value |
|-------|-------|
| **Scenario** | `FAQ` block lacks `question` + `answer` pair architecture |
| **Cause** | Accordion UI without signal mapping |
| **Impact** | FAQ contract fail |
| **Severity** | ERROR |
| **Recommended correction** | Map FAQ items to `question`/`answer`/`objection` slots |

---

## Index by severity

| Severity | IDs |
|----------|-----|
| CRITICAL | CVF-004, CVF-005, CVF-007, CVF-008, CVF-011, CVF-012, CVF-013 |
| ERROR | CVF-001, CVF-002, CVF-003, CVF-006, CVF-009, CVF-010, CVF-014, CVF-015, CVF-016 |
| WARNING | (see matrix — optional signal gaps) |

---

## SAFE UNKNOWN

- Automated detection mapping CVF → validator codes — **FUTURE**

---

*Content Failure Library version: v1.*

# Website Factory — Validation Failure Library v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** catalog of common validation failures — **documentation only**  
**Связь:** [VALIDATION-SEVERITY-SYSTEM-v1.md](VALIDATION-SEVERITY-SYSTEM-v1.md), [PAGE-TYPE-VALIDATION-MATRIX-v1.md](PAGE-TYPE-VALIDATION-MATRIX-v1.md)

---

## Назначение

Failure Library v1 документирует **типовые** отклонения, которые operator или future validator обнаружит при page block validation. Каждая запись: cause → impact → severity → recommended correction.

**Format:**

| Field | Content |
|-------|---------|
| **ID** | Stable failure code |
| **Scenario** | Human-readable description |
| **Cause** | Why it happens |
| **Impact** | Production / conversion / legal risk |
| **Severity** | INFO / WARNING / ERROR / CRITICAL |
| **Recommended correction** | Operator action |

---

## Commerce / Blueprint misclassification

### VF-001 — LANDING without HERO

| Field | Value |
|-------|-------|
| **Scenario** | `LANDING_PAGE` stack lacks `HERO` |
| **Cause** | Incomplete IA; design started before architecture gate |
| **Impact** | No value proposition above fold; PPC quality score risk |
| **Severity** | CRITICAL |
| **Recommended correction** | Add `HERO` to page contract and stack; re-run validation before Design |

---

### VF-002 — LANDING without LEAD_FORM

| Field | Value |
|-------|-------|
| **Scenario** | `LANDING_PAGE` stack lacks `LEAD_FORM` |
| **Cause** | CTA-only conversion assumed; form deferred |
| **Impact** | Primary conversion path missing for LANDING Blueprint |
| **Severity** | ERROR |
| **Recommended correction** | Add `LEAD_FORM` with Legal Pack consent fields; verify `CTA` secondary paths |

---

### VF-003 — LANDING with CART

| Field | Value |
|-------|-------|
| **Scenario** | `CART` block present on `LANDING_PAGE` or site-wide on LANDING Blueprint |
| **Cause** | Project started as shop; site_type not reclassified |
| **Impact** | Blueprint violation; wrong conversion model |
| **Severity** | CRITICAL |
| **Recommended correction** | **Halt.** Reclassify to `ECOMMERCE` or remove all commerce blocks; update SITE-TYPE-REGISTRY selection |

---

### VF-004 — CATEGORY_PAGE with CHECKOUT

| Field | Value |
|-------|-------|
| **Scenario** | `CHECKOUT` block on `CATEGORY_PAGE` (PLP) |
| **Cause** | Commerce components copied to listing template |
| **Impact** | Transaction flow on wrong page; CATALOG/ECOMMERCE boundary broken |
| **Severity** | CRITICAL |
| **Recommended correction** | Remove `CHECKOUT` from PLP; restrict to `/checkout/` utility route (ECOMMERCE only) |

---

### VF-005 — CATALOG with CART

| Field | Value |
|-------|-------|
| **Scenario** | `CART` present anywhere on CATALOG Blueprint site |
| **Cause** | Partial ecommerce implementation on RFQ catalog |
| **Impact** | Misleading UX; legal/transaction scope undefined |
| **Severity** | CRITICAL |
| **Recommended correction** | Remove `CART`; use RFQ `LEAD_FORM` / contact CTA on PDP; or reclassify ECOMMERCE |

---

## Legal / compliance

### VF-006 — LEGAL_PAGE with marketing stack

| Field | Value |
|-------|-------|
| **Scenario** | `HERO`, `LEAD_FORM`, or `CTA` on `LEGAL_PAGE` body |
| **Cause** | Marketing template reused for legal routes |
| **Impact** | Legal Pack layout violation; conversion on legal body forbidden |
| **Severity** | ERROR |
| **Recommended correction** | Apply LEGAL-PAGE-CONTRACT defaults; project shell + legal body only |

---

### VF-007 — Marketing pages without LEGAL_LINKS

| Field | Value |
|-------|-------|
| **Scenario** | `FOOTER` present but `LEGAL_LINKS` missing on production marketing page |
| **Cause** | Legal Pack gate skipped; footer partial incomplete |
| **Impact** | Compliance gap; L1–L4 not reachable |
| **Severity** | ERROR |
| **Recommended correction** | Add `LEGAL_LINKS` to global footer per LEGAL-IMPLEMENTATION-RULES; validate all marketing routes |

---

## Money pages / conversion

### VF-008 — SERVICE_PAGE without LEAD_FORM

| Field | Value |
|-------|-------|
| **Scenario** | PROMO `SERVICE_PAGE` lacks `LEAD_FORM` |
| **Cause** | Phone-only CTA assumed sufficient |
| **Impact** | Money page conversion incomplete per Blueprint |
| **Severity** | ERROR |
| **Recommended correction** | Add `LEAD_FORM` + contextual `CTA`; document consent rule |

---

### VF-009 — SERVICE_PAGE without BENEFITS or FEATURES

| Field | Value |
|-------|-------|
| **Scenario** | Neither `BENEFITS` nor `FEATURES` in stack |
| **Cause** | Unstructured prose only; blocks not mapped |
| **Impact** | Scope/capabilities not machine-checkable; IA incomplete |
| **Severity** | ERROR |
| **Recommended correction** | Add at least one OR-group member; map content to block |

---

### VF-010 — PRODUCT_PAGE without PRODUCT_CARD

| Field | Value |
|-------|-------|
| **Scenario** | PDP lacks `PRODUCT_CARD` host block |
| **Cause** | Custom PDP layout outside registry |
| **Impact** | PDP not validatable; Factory pipeline break |
| **Severity** | CRITICAL |
| **Recommended correction** | Refactor PDP to `PRODUCT_CARD` block contract |

---

## Page type / site type drift

### VF-011 — HOME_PAGE on LANDING site

| Field | Value |
|-------|-------|
| **Scenario** | `site_type_code: LANDING` but IA includes `HOME_PAGE` |
| **Cause** | Multi-page expansion without reclassification |
| **Impact** | Site type matrix violation |
| **Severity** | CRITICAL |
| **Recommended correction** | Reclassify to `PROMO` or collapse to single `LANDING_PAGE` |

---

### VF-012 — LANDING_PAGE on CATALOG site

| Field | Value |
|-------|-------|
| **Scenario** | `LANDING_PAGE` as `/` on CATALOG Blueprint |
| **Cause** | PPC landing copied as shop home |
| **Impact** | Catalog IA broken; CATEGORY/PRODUCT pages orphaned |
| **Severity** | CRITICAL |
| **Recommended correction** | Use `HOME_PAGE` with `CATEGORIES`; move campaign to optional `/promo/` route |

---

## Social proof / content gaps

### VF-013 — LANDING without social proof (TRUST / TESTIMONIALS)

| Field | Value |
|-------|-------|
| **Scenario** | Neither `TRUST` nor `TESTIMONIALS` on `LANDING_PAGE` |
| **Cause** | Proof section skipped in MVP |
| **Impact** | OR-group failure; conversion trust gap |
| **Severity** | ERROR |
| **Recommended correction** | Add `TRUST` or `TESTIMONIALS` block |

---

### VF-014 — Missing FAQ on LANDING (strict review)

| Field | Value |
|-------|-------|
| **Scenario** | `FAQ` absent on production `LANDING_PAGE` |
| **Cause** | Objections handled only in sales call |
| **Impact** | REQUIRED block missing for LANDING mapping |
| **Severity** | WARNING (operator strict: ERROR) |
| **Recommended correction** | Add `FAQ` block with objection-handling content |

---

## Registry / documentation gaps

### VF-015 — Mobile sticky `CTA` variant missing on LANDING

| Field | Value |
|-------|-------|
| **Scenario** | CORE-PAGE-ARCHITECTURES requires mobile sticky CTA pattern; stack has `CTA` band only |
| **Cause** | Sticky/mobile variant not implemented (reference: `sticky_cta.html`) |
| **Impact** | Mobile conversion suboptimal |
| **Severity** | WARNING |
| **Recommended correction** | Add sticky/mobile `CTA` implementation; canonical `block_id` remains `CTA` |

---

### VF-016 — Unknown block_id in stack

| Field | Value |
|-------|-------|
| **Scenario** | Actual stack contains `CUSTOM_PROMO_BANNER` not in registry |
| **Cause** | Project-specific block without charter |
| **Impact** | Validation not reproducible across Factory |
| **Severity** | ERROR |
| **Recommended correction** | Map to nearest canonical `block_id` or request registry charter |

---

## Index by severity

| Severity | Failure IDs |
|----------|-------------|
| CRITICAL | VF-001, VF-003, VF-004, VF-005, VF-010, VF-011, VF-012 |
| ERROR | VF-002, VF-006, VF-007, VF-008, VF-009, VF-013, VF-016 |
| WARNING | VF-014, VF-015 |
| INFO | *(see optional-block absences in PAGE-TYPE-VALIDATION-MATRIX)* |

---

## SAFE UNKNOWN

- Exhaustive failure catalog — **not claimed**; extend per project postmortems
- Automated failure ID assignment — **FUTURE**

---

*Validation Failure Library version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*

# MARS Website Factory — Page Blueprint QA Checklist v0

**Status:** **documented** — human- and **future** Validator-oriented checklist for **page blueprint** artefacts (see [Page Blueprint Contract v0](page-blueprint-contract-v0.md)). **Not** automated enforcement in this repo; **not** a substitute for legal/compliance review.

**How to use:** For each blueprint instance, walk categories 1–12. Record pass/fail, owner, and remediation. Escalate per **escalation conditions**; when evidence is missing, record **SAFE UNKNOWN** and stop false certainty.

---

## 1. Commercial logic

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`page_goal`** is singular and measurable; **`commercial_intent`** matches CTA aggressiveness and claim types; monetization path is credible for **`site_type_id`**. |
| **Common failures** | Conflicting goals (lead + newsletter + app install as equal primaries); **`high`** commercial intent with no **`conversion_points`**; B2C tactics on **`ai_visibility_page`**. |
| **Escalation conditions** | Regulated industry claims; pricing/promises without source → **`HITL_required`:** raise to `often` or `yes` and block downstream stages until resolved. |

---

## 2. SEO structure

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`SEO_intent`** stated; one primary intent per URL; **`section_order`** supports a single clear H1-bearing block story; **`internal_linking_strategy`** avoids thin/doorway patterns. |
| **Common failures** | Keyword-stuffed **`block_mapping`** for **hero**; duplicate geo/service URLs with no distinct **`notes`**; **FAQ** schema contemplated without genuine **faq** content. |
| **Escalation conditions** | Facet/indexation rules **unknown** → mark **SAFE UNKNOWN**, attach SEO technical addendum, or defer **schema_candidates** that depend on it. |

---

## 3. CTA consistency

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`CTA_strategy`** matches **`conversion_points`**; primary label consistent across **hero**, **sticky_cta**, **final_cta**; secondary CTAs do not hijack primary on mobile. |
| **Common failures** | Multiple competing primaries; **sticky_cta** with different action than declared primary; forms requesting unnecessary PII. |
| **Escalation conditions** | Consent/GDPR or telecom marketing rules unclear → **HITL** before copy freeze. |

---

## 4. Trust coverage

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`trust_strategy`** covers objections for **`commercial_intent`**; proof blocks (**trust_block**, **cases**, **reviews**, **geo_trust**) only appear when assets and rights exist; numeric claims traceable. |
| **Common failures** | **trust_block** logo soup without permission; fake urgency; **reviews** without verifiable source; **geo_trust** with wrong hours/polygon. |
| **Escalation conditions** | Any unsubstantiated award, rating aggregate, or “#1” claim → stop and require evidence or removal. |

---

## 5. UX pacing

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`UX_strategy`** and **`content_depth`** align with **`section_order`**; scan path leads to conversion without exhaustion; **read_deep** pages break content into navigable chunks in **`block_mapping`**. |
| **Common failures** | **pricing** or **comparison** before user has context; **faq** before value prop; wall of text without hierarchy. |
| **Escalation conditions** | Accessibility-critical patterns (motion, autoplay) proposed without design sign-off → flag to design **HITL**. |

---

## 6. Mobile flow

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`mobile_priority`** matches **`CTA_strategy`** (tap targets, **sticky_cta** rules); map/embed/hero media do not block primary action; forms usable on small screens. |
| **Common failures** | **`desktop_first`** without justification; horizontal scroll for core content; tiny phone links for primary CTA. |
| **Escalation conditions** | Primary conversion impossible on common 360px viewport without documented exception → block **frontend production** start. |

---

## 7. Content hierarchy

| Aspect | Detail |
|--------|--------|
| **Validation goals** | Heading roles per block in **`block_mapping`** are consistent (one H1 narrative); supporting headings support **`SEO_intent`** without spam; **optional_sections** do not bury **required_sections** logic. |
| **Common failures** | Two blocks each demanding competing H1 semantics; **catalog_grid** cards with misleading titles for clickbait CTR. |
| **Escalation conditions** | Legal/marketing disagreement on headline claims → **HITL** on **hero** copy before design. |

---

## 8. Block compatibility

| Aspect | Detail |
|--------|--------|
| **Validation goals** | Every **`block_id`** in **`required_sections`** / **`section_order`** exists in [Block Registry v0](block-registry-v0.md); pairing respects **`compatible_site_types`** / **`incompatible_site_types`** or documents exception in **`notes`**. If the blueprint lists **site-type role names** (e.g. from **`required_blocks`** on a site type row) without a matching **`block_id`**, **`notes`** must record **SAFE UNKNOWN** or the mapping plan (see [Page Blueprint Contract v0](page-blueprint-contract-v0.md)). |
| **Common failures** | **`pricing`** on thin **`seo_landing`**; campaign **hero** on **`ai_visibility_page`** without scoped exception; missing **dependencies** (e.g. **lead_form** without prior trust on **`high`** service pages). |
| **Escalation conditions** | Registry gap (site type references role with no **`block_id`**) → **SAFE UNKNOWN** + propose new **`block_id`** in registry backlog or adjust blueprint. |

---

## 9. Conversion path clarity

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`conversion_points`** lists each surface, its trigger, and post-submit state (thank-you, expectation); analytics events called out if project uses them (**optional** in v0). |
| **Common failures** | Form submits to nowhere; tel: on desktop-only assumption; **catalog_grid** without PDP path. |
| **Escalation conditions** | Revenue-impacting path undefined (payment, invoice, CRM) → **HITL** with ops. |

---

## 10. Anti-pattern detection

| Aspect | Detail |
|--------|--------|
| **Validation goals** | Cross-check **`site_type_id`** **forbidden_patterns** (from Site Type Registry) against blueprint; keyword stuffing; review gating; fake schema; duplicate thin geo; dark patterns in **CTA_strategy**. |
| **Common failures** | **FAQ** schema for non-questions; **AggregateRating** contemplated without legitimate reviews; “doorway” internal linking in **`internal_linking_strategy`**. |
| **Escalation conditions** | Any black-hat SEO or deceptive pattern → **stop pipeline**, record **SECURITY RISK** / compliance signal per governance dictionary. |

---

## 11. SAFE UNKNOWN enforcement

| Aspect | Detail |
|--------|--------|
| **Validation goals** | Every **unknown** dependency (data source, legal text, facet policy, stock feed) is logged in **`notes`** with owner and verification method; no blueprint field pretends certainty. |
| **Common failures** | “TBD” with no owner; **schema_candidates** listed without content plan; **`HITL_required`:** `rare` chosen without rationale on sensitive pages. |
| **Escalation conditions** | Residual **unknowns** affect money, law, or safety → **`HITL_required`:** `yes` until resolved or explicitly accepted in writing. |

---

## 12. HITL escalation rules

| Aspect | Detail |
|--------|--------|
| **Validation goals** | **`HITL_required`** matches risk: claims, geo ops, pricing, regulated sectors, **ai_visibility_page**; aligns with [workflow-map](workflow-map.md) gate after blueprint when cost/scope/legal risk is non-trivial. |
| **Common failures** | Blueprint approved without stakeholder sign-off when **`often`/`yes`** warranted; downstream agents assumed to “fix” legal copy. |
| **Escalation conditions** | Any category 1–11 **fail** with compliance or reputational impact → **do not** pass G3 (sitemap/blueprint) gate; reopen strategy/SEO inputs. |

---

## Cross-reference

- Blueprint fields: [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md)
- Broader QA lanes: [qa-validation-model.md](qa-validation-model.md)
- Registry context: [registries.md](registries.md)

---

*Checklist version: v0 — documentation only.*

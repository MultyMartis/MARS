# Page blueprint — Triumph Manipulator Landing (v0)

**Contract SoT:** [Page Blueprint Contract v0](../../page-blueprint-contract-v0.md)  
**Blocks:** [Block Registry v0](../../block-registry-v0.md)

---

## Blueprint record (normalized fields)

| Field | Value |
|--------|--------|
| **blueprint_id** | `triumph_manipulator_landing_main_v0` |
| **site_type_id** | `service_landing` |
| **page_goal** | Qualified lead: request quote or callback for commercial manipulator services. |
| **target_audience** | B2B logistics/site roles + selective B2C heavy-move needs; regional commercial searchers. |
| **commercial_intent** | `high` |
| **SEO_intent** | Transactional + local service intent (manipulator / crane truck hire); single primary intent per URL. |
| **CTA_strategy** | Primary: **lead_form** (short). Secondary: **tel:** in hero + **sticky_cta** after scroll. Same primary label at **final_cta**. |
| **trust_strategy** | **trust_block** early (verifiable certs only). **geo_trust** for service area honesty. **cases** mid-page with permissions. **reviews** omitted until real widget/quotes. |
| **UX_strategy** | `scan_and_act` — problem → credibility → process → scope → proof → FAQ → convert. |
| **content_depth** | `medium` |
| **mobile_priority** | `high` |
| **required_sections** | `hero`, `trust_block`, `geo_trust`, `process_steps`, `services_grid`, `cases`, `faq`, `lead_form`, `final_cta` |
| **optional_sections** | `reviews`, `pricing`, `sticky_cta` (behavior), `contact_cta` (if distinct from hero secondary) |
| **section_order** | `hero` → `trust_block` → `geo_trust` → `process_steps` → `services_grid` → `cases` → `faq` → `lead_form` → `final_cta` (+ `sticky_cta` mobile) |

### block_mapping (narrative)

| block_id | Section goal | CTA type | Trust semantics | SEO intent | UX pacing | Mobile notes | Invalidation sensitivity |
|----------|----------------|----------|-----------------|------------|-----------|--------------|---------------------------|
| **hero** | Immediate orientation: who, what region class, primary offer | `primary` + secondary `tel:` | One proof line max; no logo soup | Single **H1** — service + **one** geo modifier if true | Fast scan | CTA not buried under heavy media | **High** — hero copy change → design + SEO + frontend |
| **trust_block** | Consolidated credibility | `none` / implicit policy link | Primary trust surface | Low keyword density | Skim badges | Legible logos | **Medium** — asset swap may need legal |
| **geo_trust** | Honest service area + logistics note | `implicit` | Prevents “fake local” | Aligns with local intent | After initial trust | Map/list readable | **High** — area change → SEO + legal + schema |
| **process_steps** | How quote → site visit → work executes | `implicit` to form | Reduces anxiety | H2 for steps | Mid-page breathe | Steps not taller than viewport each | **Medium** |
| **services_grid** | Capability / equipment class scan (proxy for registry **service_scope** role) | `implicit` card links | Clarity implies competence | Internal anchors / clarity | Compare-at-glance | 2-col max stacked | **Medium** |
| **cases** | Proof of real jobs | `secondary` optional “Discuss similar job” | **proof_entity**-oriented | Moderate headings | Slow scroll gallery | Light images | **High** — case text wrong → trust + legal |
| **faq** | Objections: price shape, timing, boundaries | `implicit` | No fabricated stats | FAQ candidates | Accordion scan | Tap targets per row | **Medium** |
| **lead_form** | Capture lead | `primary` | Consent/privacy nearby | Low | Form focus | Minimal fields | **High** — CRM field change → frontend + privacy |
| **final_cta** | Repeat primary | `repeated` same intent | Reinforce | n/a | Closure | Full-width button safe | **Low–medium** |
| **sticky_cta** | Mobile persistence | `repeated` | Same as primary | n/a | n/a | Does not obscure form | Tied to **hero** CTA object |

### conversion_points

- Hero → scroll or jump to `#quote`
- After **process_steps** → anchor **lead_form**
- **final_cta** → same form / `tel:`

### internal_linking_strategy

- v0: minimal outbound internal — **SAFE UNKNOWN** sibling pages.
- Future district pages: hub/spoke from this landing only when pages exist (no orphans).

### schema_candidates

- `LocalBusiness` / `Organization` — **only** with truthful NAP; **SAFE UNKNOWN** until legal supplies JSON fields.
- `FAQPage` — **only** if **faq** visible and Q&A genuine.
- **No** `AggregateRating` without verifiable platform.

### QA_requirements

- H1 uniqueness; no competing primary CTAs; service area text matches ads/GMB when those exist (**SAFE UNKNOWN**).
- Form labels, consent, error states; **tel:** works on real devices.
- Image alt + rights for **cases**.

### HITL_required

`selective` → **`often`** if regulated transport / operator claims in jurisdiction require it.

### notes

- Site Type **`service_scope`** role has **no** dedicated `block_id` in [Block Registry v0](../../block-registry-v0.md); this blueprint uses **`services_grid` + `geo_trust` + process copy** to cover scope semantics — documented per registry intro (“record the gap”).
- Hybrid **geo + service** documented under `site_type_id` `service_landing` with IA divergence note in [site-classification-v0.md](site-classification-v0.md).

---

*Page blueprint v0 — reference execution only*

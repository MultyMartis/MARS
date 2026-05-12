# MARS Website Factory — Semantic Object Model v0

**Status:** **documentation only** — canonical **semantic object** definitions for factory prose, prompts, and QA. **Not** a JSON Schema mandate, **not** persisted entity types in MARS.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md), [page-objective-model-v0.md](page-objective-model-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md).

---

## 1. Columns used for each object

For every semantic object below:

| Column | Meaning |
|--------|---------|
| **Purpose** | What meaning it carries. |
| **Ownership** | Which stage / artifact class **defines** the authoritative binding for a scope (see §2). |
| **Inheritance** | How child scopes receive defaults ([semantic-inheritance-v0.md](semantic-inheritance-v0.md)). |
| **Mutation rules** | When change is allowed; what breaks freeze. |
| **Invalidation rules** | What downstream semantics / QA **should** be revisited ([semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md)). |
| **QA linkage** | Typical QA lanes / checks. |
| **Approval linkage** | Typical HITL / gate ties. |
| **Freeze semantics** | Behavior under semantic freeze ([semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)). |

Cross-cutting:

- **Object lineage** — which revision / supersession chain this object instance belongs to ([revision-semantics-v0.md](revision-semantics-v0.md)).
- **Supersede semantics** — a newer semantic object instance **replaces** a prior one for the same scope only after **explicit** supersede + invalidation handling; parallel “shadow” meanings without declaration are **inconsistency**, not supersede.
- **Object drift** — divergence from last-approved baseline; detected via QA / review ([semantic-qa-rules-v0.md](semantic-qa-rules-v0.md)).

---

## 2. Authority model (shared)

**Ownership** is **not** exclusive execution rights — it is **documentation responsibility** for stating the binding first.

| Scope | Primary defining artifact (typical) |
|-------|-------------------------------------|
| Site / cluster | Strategy + IA artifacts |
| Page | Page Blueprint |
| Section | Blueprint section payload + Design notes |
| Component | Design / Frontend artifact (bounded by blueprint) |

---

## 3. Canonical semantic objects

### 3.1 `cta_object`

| Field | Content |
|-------|---------|
| **Purpose** | Primary and secondary call-to-action meaning, labels, destinations, friction class — aligned with [cta-semantics-v0.md](cta-semantics-v0.md) and [conversion-intent-model-v0.md](conversion-intent-model-v0.md). |
| **Ownership** | Page Blueprint for page-level primary; Design for visual emphasis variants; Frontend for implemented affordances. |
| **Inheritance** | Site/cluster **default CTA policy** may set tone and placement rules; page **overrides** for page objective. |
| **Mutation rules** | Any primary CTA change after freeze requires **freeze break** path per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md). |
| **Invalidation rules** | Conversion QA, Hero / sticky sections that echo CTA, sometimes **trust** copy if CTA promise shifts. |
| **QA linkage** | Conversion QA, Frontend QA (link targets, a11y), Design QA (hierarchy). |
| **Approval linkage** | Often **G3–G6** gates depending on scope ([workflow-map.md](workflow-map.md)). |
| **Freeze semantics** | Frozen `cta_object` on a page blocks **silent** label or destination changes in downstream artifacts. |

### 3.2 `trust_object`

| Field | Content |
|-------|---------|
| **Purpose** | Trust signals, proof obligations, ethics constraints — [trust-semantics-v0.md](trust-semantics-v0.md). |
| **Ownership** | Blueprint **trust_strategy** + section payloads; legal/compliance may constrain claims. |
| **Inheritance** | Shared **trust system** at site level (logos policy, testimonial rules) inherited by pages unless overridden. |
| **Mutation rules** | Fabricated proof is out-of-scope / **SECURITY RISK** class escalation per trust doc. |
| **Invalidation rules** | FAQ, operational copy, CTA-adjacent claims, schema-rich SEO surfaces. |
| **QA linkage** | Conversion QA, SEO QA (schema honesty), Design QA (attribution). |
| **Approval linkage** | Higher HITL for YMYL-sensitive site types ([site-type-registry-v0.md](site-type-registry-v0.md)). |
| **Freeze semantics** | Frozen trust objects require HITL to add new unverified claims. |

### 3.3 `seo_intent`

| Field | Content |
|-------|---------|
| **Purpose** | Query / topic intent, cannibalization posture, on-page SEO obligations — [seo-intent-model-v0.md](seo-intent-model-v0.md). |
| **Ownership** | Strategy + SEO artifacts at site level; Blueprint per page. |
| **Inheritance** | Cluster **topic ownership** inherits to member pages unless page declares distinct primary intent. |
| **Mutation rules** | Changing primary intent affects IA and internal links — **STRUCTURE CHANGE** risk ([orchestration-signals-v0.md](orchestration-signals-v0.md)). |
| **Invalidation rules** | Blueprint copy blocks, meta templates, FAQ entity, some trust claims tied to expertise. |
| **QA linkage** | SEO QA lane, Blueprint QA. |
| **Approval linkage** | Strategy / PM gate before IA lock-in. |
| **Freeze semantics** | Freeze does not remove **factual** update needs (e.g. law change) — reopen partial scope. |

### 3.4 `conversion_goal`

| Field | Content |
|-------|---------|
| **Purpose** | Measurable or qualitative conversion outcome the page/cluster serves — [conversion-intent-model-v0.md](conversion-intent-model-v0.md). |
| **Ownership** | Strategy + Page objective model; Blueprint binds CTAs to goals. |
| **Inheritance** | Funnel stage defaults from cluster or campaign entity (**documentation**). |
| **Mutation rules** | Goal change often forces CTA and hero re-evaluation. |
| **Invalidation rules** | Conversion QA, CTA system, optional IA if goal shifts audience. |
| **QA linkage** | Conversion QA primary. |
| **Approval linkage** | PM / client on material goal shifts. |
| **Freeze semantics** | Post-freeze goal change is **high severity** — delivery blocking until re-approved. |

### 3.5 `offer_object`

| Field | Content |
|-------|---------|
| **Purpose** | Commercial offer framing: scope, price presentation class, urgency ethics, eligibility. |
| **Ownership** | Strategy + Blueprint; legal review for regulated offers. |
| **Inheritance** | Site-wide promo rules and disclaimer templates. |
| **Mutation rules** | Price / availability claims require ops-aligned evidence. |
| **Invalidation rules** | Hero, pricing sections, FAQ, trust, CTA copy, Frontend pricing UI. |
| **QA linkage** | Conversion QA, SEO QA (thin promo pages), Frontend QA. |
| **Approval linkage** | Compliance / client on material commercial claims. |
| **Freeze semantics** | Tied to campaign freeze windows when declared. |

### 3.6 `geo_object`

| Field | Content |
|-------|---------|
| **Purpose** | Service area, location truth, local entity semantics — aligns with trust **local_trust** and IA. |
| **Ownership** | IA + Blueprint; ops for polygon / hours truth. |
| **Inheritance** | Branch pages inherit parent **service area** unless explicitly narrowed. |
| **Mutation rules** | Geo expansion can create **doorway** SEO risk — SEO QA. |
| **Invalidation rules** | NAP blocks, maps, local FAQ, some CTAs (`direct_contact`). |
| **QA linkage** | SEO QA, Conversion QA. |
| **Approval linkage** | Ops / franchise governance when applicable. |
| **Freeze semantics** | Geo freeze for regulated franchises may be contractual. |

### 3.7 `service_entity`

| Field | Content |
|-------|---------|
| **Purpose** | Named service line: deliverables, prerequisites, audience — often maps to URL / cluster. |
| **Ownership** | IA (entity set) + Blueprint per service page. |
| **Inheritance** | Site service taxonomy; child pages narrow **scope** only. |
| **Mutation rules** | Renaming / merging services is IA-level — broad invalidation. |
| **Invalidation rules** | Cross-links, nav labels, FAQ, proof cases, SEO cannibalization neighbors. |
| **QA linkage** | Blueprint QA, SEO QA (cluster), site QA ([semantic-qa-rules-v0.md](semantic-qa-rules-v0.md)). |
| **Approval linkage** | PM + SEO on merge/split. |
| **Freeze semantics** | Entity rename post-freeze requires explicit supersede of internal links artifact. |

### 3.8 `faq_entity`

| Field | Content |
|-------|---------|
| **Purpose** | Question–answer pairs as **semantic** units (not only UI blocks). |
| **Ownership** | Blueprint section payloads; ops for factual answers. |
| **Inheritance** | Site-level FAQ policy (tone, legal pre-approved answers). |
| **Mutation rules** | Must stay consistent with **offer_object**, **trust_object**, **operational_trust**. |
| **Invalidation rules** | Trust, offer, checkout copy, schema FAQ markup. |
| **QA linkage** | Conversion QA, SEO QA. |
| **Approval linkage** | Legal for regulated industries. |
| **Freeze semantics** | FAQ freeze often paired with legal sign-off snapshot. |

### 3.9 `proof_entity`

| Field | Content |
|-------|---------|
| **Purpose** | Case study, metric, testimonial, certification **as a semantic unit** with attribution requirements. |
| **Ownership** | Blueprint + client evidence; Design for presentation. |
| **Inheritance** | Shared proof library at site level. |
| **Mutation rules** | No anonymous upgrade of proof tier (e.g. logo → named case) without HITL. |
| **Invalidation rules** | Trust surfaces, hero, B2B trust blocks, CTA credibility. |
| **QA linkage** | Conversion QA, Design QA. |
| **Approval linkage** | Client release for named proofs. |
| **Freeze semantics** | Proof withdrawal post-freeze forces **semantic invalidation** of dependent sections. |

### 3.10 `navigation_entity`

| Field | Content |
|-------|---------|
| **Purpose** | Nav labels, IA placement, hub vs spoke roles, breadcrumbs semantics. |
| **Ownership** | IA artifact primary; Frontend implements. |
| **Inheritance** | Global nav from site template; section nav from page template. |
| **Mutation rules** | Nav change without IA update → **semantic mismatch**. |
| **Invalidation rules** | All pages using label; internal link graph; some **seo_intent** neighborhoods. |
| **QA linkage** | Blueprint QA, Frontend QA, site cluster QA. |
| **Approval linkage** | UX / PM on IA changes. |
| **Freeze semantics** | Global nav freeze is **high blast radius** — explicit reopen. |

---

## 4. SAFE UNKNOWN

- Exact **cardinality** (one vs many `cta_object` per page) per site type — refine in later registry versions.
- **Machine-readable** bindings between semantic objects and component IDs — **not** defined in v0.

---

*End of Semantic Object Model v0.*

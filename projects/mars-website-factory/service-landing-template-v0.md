# Operational template — Service landing (v0)

**Status:** **documentation-only** pattern for a **commercial service** single-page or primary-landing focus. **Informed by** [reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md) (Triumph Manipulator Landing — **not** a shipped site).

**Normative semantics:** [page-objective-model-v0.md](page-objective-model-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md), [block-registry-v0.md](block-registry-v0.md).

---

## 1. Typical sections (blueprint-facing)

Order is **indicative** — validate against IA and `site_type_id` (see [site-type-registry-v0.md](site-type-registry-v0.md)).

| Section role | Typical intent | Block registry hint |
|--------------|----------------|----------------------|
| Hero + primary value | Clarify **who / what / outcome** in one scan | Hero / value props |
| Problem / context | Operational pain the service removes | Story / problem |
| Service scope / modules | What is included / excluded | Features / services list |
| Proof / credentials | Trust without unverifiable stats | Logos, certs, case snippets |
| Process / “how it works” | Reduce uncertainty pre-CTA | Steps / timeline |
| FAQ / objections | SEO + conversion support | FAQ block |
| Secondary proof (optional) | Deep trust for long sales cycles | Testimonials (evidence-backed) |
| Final CTA band | Repeat primary conversion | CTA strip |

---

## 2. CTA hierarchy

Per [cta-semantics-v0.md](cta-semantics-v0.md):

- **Primary CTA** — one dominant action aligned to [conversion-intent-model-v0.md](conversion-intent-model-v0.md).
- **Secondary CTA** — lower-commitment (e.g. download spec) — must not **cannibalize** primary without explicit strategy approval.
- **Destructive / high-friction CTAs** — gated by HITL if legal/compliance-sensitive ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

Document **post-click** expectation (form, phone, calendar) — **SAFE UNKNOWN** if CRM routing not defined.

---

## 3. Trust model

Per [trust-semantics-v0.md](trust-semantics-v0.md):

- Prefer **verifiable** claims; mark inferred fleet counts, regions, or certifications as **SAFE UNKNOWN** or **needs client evidence**.
- Align **proof_entity** and **service_entity** with [semantic-object-model-v0.md](semantic-object-model-v0.md).

---

## 4. SEO intent

Per [seo-intent-model-v0.md](seo-intent-model-v0.md) and Triumph [seo-strategy-v0.md](reference-cases/triumph-manipulator-landing/seo-strategy-v0.md) shape:

- Primary query cluster and **intent type** (informational / commercial / transactional mix).
- **No** guaranteed rankings, indexing, or AI overview placement.

---

## 5. Commercial pacing

- Early: clarity and relevance (avoid jargon wall).
- Mid: proof + mechanism (why believable).
- Late: risk reversal + CTA (without **bait-and-switch** semantics inconsistent with blueprint).

---

## 6. Mobile flow

Per Triumph [information-architecture-v0.md](reference-cases/triumph-manipulator-landing/information-architecture-v0.md) discipline:

- Single-column **scan path**; sticky CTA only if it does not obscure proof.
- Tap targets and form fields: capture **frontend QA** items ([frontend-qa checklist themes in reference case](reference-cases/triumph-manipulator-landing/frontend-qa-v0.md)).

---

## 7. Common blockers

| Blocker class | Typical signal | Escalation |
|---------------|----------------|------------|
| Unverified proof | “#1 in region” without source | HITL + remove or soften |
| Scope creep in hero | Multiple unrelated services | Strategy / blueprint revision |
| CTA / trust mismatch | Aggressive CTA + weak proof | QA + semantic consistency ([semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md)) |
| SEO vs conversion conflict | Keyword stuffing harms readability | SEO + UX joint review |

---

## 8. QA focus (service landing)

- Blueprint: [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md).
- Semantic: CTA/trust/offer alignment ([semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md)).
- Frontend: layout, a11y, CTA visibility, trust markers ([frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)).
- Validation: evidence discipline ([validation-evidence-model-v0.md](validation-evidence-model-v0.md)).

---

## 9. SAFE UNKNOWN

- Exact legal disclaimers, warranty text, regional offer constraints — **unknown** until counsel/client artifacts exist.

---

*Template v0 — Triumph reference case informed; no performance or ranking claims.*

# MARS Website Factory — CTA semantics v0

**Status:** **documentation only** — normalized **call-to-action** intent labels for blueprints, design, and conversion QA. **Not** performance guarantees, **not** “best CTA” prescriptions, **not** automated CTA optimization.

**Related:** [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md), [block-registry-v0.md](block-registry-v0.md).

---

## Principles

- CTAs are **obligations** to the user (clear destination, honest friction), not tricks.
- Labels below are **semantic**; implementation may reuse components (`lead_form`, `contact_cta`, etc.).
- Misuse risks are **documentation guidance** — **no** claim of automated detection.

---

## Normalized CTA concepts

### lead_capture

| Aspect | Content |
|--------|---------|
| **Purpose** | Collect structured prospect data for follow-up. |
| **Misuse risks** | Hidden fields, dark patterns, consent gaps, PII without purpose limitation. |
| **Compatible site types** | `service_landing`, many `corporate_site`, B2B flows — check **site_type_id**. |
| **Trust dependencies** | Privacy copy, legitimacy signals before long forms. |
| **Anti-patterns** | Fake scarcity on form; submit without clear use of data. |
| **Mobile** | Minimize fields; large tap targets; inline errors. |
| **SEO** | Form-heavy pages still need substantive on-page content; avoid thin gateway. |
| **QA concerns** | Validation, **a11y**, consent text, destination of submissions (**SAFE UNKNOWN** if backend undefined). |

### direct_contact

| Aspect | Content |
|--------|---------|
| **Purpose** | Immediate human channel (tel, email, messenger). |
| **Misuse risks** | Wrong numbers, hidden costs, **click-to-call** on desktop-only tested pages. |
| **Compatible site types** | Local services, urgent trades, high-trust B2B. |
| **Trust dependencies** | Hours, geography, who answers. |
| **Anti-patterns** | `tel:` to unrelated tracking pools without disclosure. |
| **Mobile** | Primary placement often justified; verify real dial intent. |
| **SEO** | NAP consistency with **LocalBusiness** honesty rules. |
| **QA concerns** | Link validity, tracking params policy. |

### consultation

| Aspect | Content |
|--------|---------|
| **Purpose** | Book expert time (calendar, callback slot). |
| **Misuse risks** | Bait-and-switch on “free” consult; qualification mismatch. |
| **Compatible site types** | Professional services, complex B2B. |
| **Trust dependencies** | Who performs consult, duration, preparation expectations. |
| **Anti-patterns** | Consult positioned as audit but is hard sales only. |
| **Mobile** | Calendar widgets must be usable; timezone clarity. |
| **SEO** | Often secondary to educational content — avoid keyword-stuffed booking landers. |
| **QA concerns** | Cancellation policy, CRM handoff (**SAFE UNKNOWN** until defined). |

### estimate_request

| Aspect | Content |
|--------|---------|
| **Purpose** | Scoped pricing or project scoping request. |
| **Misuse risks** | Implied fixed price from estimator without legal review. |
| **Compatible site types** | Trades, manufacturing RFQ, custom services. |
| **Trust dependencies** | What inputs are required; turnaround honesty. |
| **Anti-patterns** | Fake instant quotes tied to upsell with hidden fees. |
| **Mobile** | Large inputs (measurements) — consider save/resume story. |
| **SEO** | Thin “estimate” pages duplicated per city → doorway risk. |
| **QA concerns** | Legal disclaimers; data retention. |

### catalog_navigation

| Aspect | Content |
|--------|---------|
| **Purpose** | Move users to PDP, facet, or next browse step. |
| **Misuse risks** | Competing primaries vs **lead_capture** on same viewport. |
| **Compatible site types** | `catalog_site`, `ecommerce`, large `corporate_site` catalogs. |
| **Trust dependencies** | Accurate availability/price sourcing where shown. |
| **Anti-patterns** | Misleading “view offer” that jumps unrelated category. |
| **Mobile** | Filter drawer discoverability. |
| **SEO** | Facet indexation policy separate from CTA label. |
| **QA concerns** | Broken filters, orphan PLPs. |

### micro_conversion

| Aspect | Content |
|--------|---------|
| **Purpose** | Low-friction step (save, compare, subscribe to updates) before primary conversion. |
| **Misuse risks** | Newsletter walls on informational intent pages; dark **nudge** stacks. |
| **Compatible site types** | Long-cycle B2B, considered purchases. |
| **Trust dependencies** | Frequency/unsubscribe clarity. |
| **Anti-patterns** | Hidden pre-checked boxes. |
| **Mobile** | Dismissible banners; no layout shift traps. |
| **SEO** | Do not replace substantive content with signup gates. |
| **QA concerns** | Consent logs, double opt-in policy (**project-specific**). |

### authority_reinforcement

| Aspect | Content |
|--------|---------|
| **Purpose** | CTA-shaped prompts to **read proof** (methodology, certs, cases) rather than immediate transaction. |
| **Misuse risks** | Fake credentials; **authority_reinforcement** used to dodge clear primary CTA without HITL. |
| **Compatible site types** | Regulated, technical, **ai_visibility_page** (soft). |
| **Trust dependencies** | Verifiable sources; no fabricated endorsements. |
| **Anti-patterns** | “As seen on” logos without permission. |
| **Mobile** | Keep proof scannable before transactional CTA repeat. |
| **SEO** | E-E-A-T alignment — honesty over volume. |
| **QA concerns** | Claim substantiation ([trust-semantics-v0.md](trust-semantics-v0.md)). |

---

## Explicit non-claims

v0 does **not** assert **high-converting guaranteed** CTAs, A/B winners, or model-predicted click rates.

---

*Last updated: 2026-05-11.*

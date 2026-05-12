# Operational template — Geo / local landing (v0)

**Status:** **documentation-only** pattern for **geographically scoped** service or franchise-style landing pages. **Not** a local SEO ranking playbook and **not** a substitute for legal/geo compliance review.

**Normative semantics:** [semantic-object-model-v0.md](semantic-object-model-v0.md) (`geo_object`, `service_entity`), [seo-intent-model-v0.md](seo-intent-model-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md) (cannibalization), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md).

---

## 1. Geo semantics (document honestly)

| Field | Guidance |
|-------|----------|
| Target geography | City / metro / region / multi-region — cite **client-confirmed** service area. |
| Language / locale | Match audience; note bilingual needs if any. |
| NAP consistency (if applicable) | Name / address / phone — **only** if real business data is in scope; else **SAFE UNKNOWN**. |
| Service area vs ranking claim | Describe **where** you serve — **not** “#1 in maps” unless third-party evidence exists (typically **out of repo**). |

**Explicit:** **No fake local ranking claims.** Do not invent map pack positions, review counts, or star averages.

---

## 2. Local trust

- **Local proof** — real addresses, local licenses, regional case studies (with permission).
- **Stock “local” photography** — flag as generic; prefer authentic imagery when available.
- **Community / partnership** mentions — verifiable only.

---

## 3. Geo SEO (structure, not promises)

- Distinct **URL/slug** semantics per location when using multi-page patterns ([multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)).
- **Title/H1** clarity: location + service without keyword stuffing.
- **Internal links** — hub ↔ spoke patterns documented at site graph level ([site-semantic-graph-v0.md](site-semantic-graph-v0.md) conceptual).
- **Structured data** — if discussed, treat as **handoff requirement**, not automated generation claim.

---

## 4. Duplication risks

| Risk | Mitigation (documentation) |
|------|---------------------------|
| Copy-paste city pages | Require **unique** proof, FAQs, and local context per page in blueprint. |
| Thin “doorway” pages | Escalate to HITL; may violate strategy/ethics boundary — mark **STRUCTURE CHANGE** if site graph changes. |
| Conflicting service area statements | Single **SoT** in intake + blueprint ([cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md)). |

---

## 5. Local CTA patterns

- **Call / directions / booking** — match real operations (hours, holidays) — **SAFE UNKNOWN** until confirmed.
- **Franchise vs corporate** — clarify who answers the lead (affects trust_object and CTA copy).

---

## 6. Cannibalization warnings

When multiple geo landings target **overlapping** queries:

- Document **primary authority page** per cluster ([multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)).
- Mark **cannibalization risk** in blueprint QA and semantic QA ([semantic-qa-rules-v0.md](semantic-qa-rules-v0.md)).

---

## 7. QA focus

- Consistency of geo claims across blueprint, design, frontend ([semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md)).
- Evidence for any **distance**, **coverage**, or **response time** claims ([validation-evidence-model-v0.md](validation-evidence-model-v0.md)).
- Mobile: click-to-call and map behavior (manual QA; **not** automated device lab claim).

---

## 8. SAFE UNKNOWN

- Regulatory **advertising** rules per jurisdiction — **unknown** without legal review.
- Whether multi-location rollout follows **hub-spoke** vs **flat** URL policy — **unknown** until architecture decision exists.

---

*Template v0 — honesty over local SEO performance fiction.*

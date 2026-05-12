# MARS Website Factory — Semantic Consistency Rules v0

**Status:** **documentation only** — rules for **when semantic alignment is required** and how to **classify** inconsistency. **Not** automated linting unless a future tool is evidenced.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md), [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).

---

## 1. Consistency dimensions

| Dimension | Rule (summary) |
|-----------|----------------|
| **CTA consistency** | Same page: one **declared** primary `cta_object` across Blueprint, Design, Frontend; alternates documented. |
| **Trust consistency** | Claims, proofs, and disclaimers align across FAQ, offer, hero, and schema. |
| **SEO consistency** | Titles/H1/internal links align with declared `seo_intent`; no undeclared cannibalization. |
| **Navigation consistency** | Labels and targets match IA + Blueprint; no orphan routes. |
| **Offer consistency** | Pricing, scope, urgency copy aligned across hero, pricing section, FAQ, checkout. |
| **Geo consistency** | NAP, maps, and CTAs agree on geography; no city stuffing vs `geo_object`. |
| **Design / semantic mismatch** | Visual layout OK only if **meaning** unchanged; otherwise upstream revision. |
| **Frontend / semantic mismatch** | Implemented strings, links, and schema match approved semantic snapshot. |
| **QA consistency** | QA verdicts cite artifact revision ids; no “pass” against stale baseline after upstream semantic change ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |

---

## 2. Consistency severity

| Level | Description |
|-------|-------------|
| **C0 — critical** | Legal, safety, or fraudulent semantic conflict — delivery **blocked**, **SECURITY RISK** / policy path. |
| **C1 — major** | Primary conversion or SEO intent broken — delivery **blocked** until fixed or waived with HITL. |
| **C2 — moderate** | Secondary CTA / trust / nav inconsistency — **conditional** pass possible with documented follow-up. |
| **C3 — minor** | Cosmetic copy variance without meaning change — optional fix; not a semantic object violation if evidenced. |

---

## 3. Escalation rules

1. **C0–C1** → **NEED HUMAN APPROVAL** + lane rerun per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md).
2. **Cluster-wide** inconsistency → site/cluster QA episode ([reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md)).
3. **Unknown severity** → treat as **C1 bias** until owner downgrades with evidence (**SAFE UNKNOWN** reduction protocol).

---

## 4. Freeze break rules

Changing any **frozen** semantic object without reopening:

- **Breaks** semantic freeze ([semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)).
- **Invalidates** inherited approvals and QA for affected scope per [dependency-invalidation-v0.md](dependency-invalidation-v0.md).
- **Delivery** candidate cannot ship until **new** approval chain completes ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)).

---

## 5. Delivery blocking rules

Release is **blocked** when:

- Open **C0** or **C1** semantic inconsistency exists without approved waiver.
- **QA consistency** failure: verdict explicitly tied to superseded revision still cited as current.
- **Orphan** semantic entities: Frontend exposes CTA or proof not present in approved blueprint lineage ([semantic-qa-rules-v0.md](semantic-qa-rules-v0.md)).

---

## 6. SAFE UNKNOWN

- Automated detection thresholds for C2 vs C3 — **not** in-repo.
- Third-party embeds (reviews widget) consistency — verify outside factory or mark **SAFE UNKNOWN**.

---

*End of Semantic Consistency Rules v0.*

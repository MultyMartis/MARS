# MARS Website Factory — Semantic QA Rules v0

**Status:** **documentation only** — **QA obligations** focused on **meaning** alignment. Complements [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md). **Not** automated semantic testing infrastructure.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md), [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md).

---

## 1. Semantic QA scope

**In scope**

- Cross-artifact checks for semantic objects declared in [semantic-object-model-v0.md](semantic-object-model-v0.md).
- Cluster and site subgraph checks per [site-semantic-graph-v0.md](site-semantic-graph-v0.md) when multi-page QA is scheduled.

**Out of scope (v0)**

- Autonomous crawling at scale — **SAFE UNKNOWN** per environment.
- **Subjective** brand taste without documented acceptance criteria — note as **UNKNOWN** / human-only.

---

## 2. Finding classes

| Class | Description |
|-------|-------------|
| **Semantic mismatch** | Same scope, incompatible declarations across artifacts ([cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md)). |
| **Trust inconsistency** | Proof, claim, disclaimer, or schema contradiction. |
| **CTA inconsistency** | Primary/secondary CTA roles disagree across Blueprint/Design/Frontend. |
| **SEO drift** | On-page content or internal links no longer match declared `seo_intent` or cluster rules. |
| **Geo inconsistency** | NAP / map / service copy conflict with `geo_object`. |
| **Orphan entities** | Implemented CTA, proof, FAQ, or service surface **without** blueprint lineage. |
| **Stale semantics** | QA or approval references **superseded** revision without rerun after upstream semantic change. |
| **Cluster inconsistency** | Cannibalization, duplicate intents, or broken hub/spoke semantics inside a cluster. |

---

## 3. QA evidence rules

1. Every semantic finding cites **artifact path + revision/snapshot id** (or explicit **SAFE UNKNOWN** if ids absent).
2. **Screenshots / links** as evidence for Frontend-facing issues when policy requires.
3. **No fabricated** “client approved” without citation to approval artifact.

---

## 4. Severity mapping

Align with [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md) **C0–C3** and [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) blocker/conditional vocabulary.

| Typical finding | Default severity |
|-----------------|------------------|
| Fake / unverifiable trust | **C0** |
| Wrong primary CTA destination | **C1** |
| Cannibalizing H1 on two cluster pages | **C1** |
| Mismatched FAQ vs offer footnote | **C2** |
| Minor alt text variance | **C3** or informational |

---

## 5. Blocking semantics

- **C0–C1** → **blocker** unless **waiver** path satisfied.
- **Cluster inconsistency** with open **C1** → **blocks** cluster-level **delivery candidate** per [reference-delivery-package-v0.md](reference-delivery-package-v0.md).

---

## 6. Waiver semantics

- Waivers require **named approver**, **residual risk statement**, **expiry** where policy demands ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)).
- **C0** waivers may be **disallowed** by org policy — document **NEED HUMAN APPROVAL** escalation, not automatic pass.

---

## 7. SAFE UNKNOWN rules

- If **cannot verify** backend behavior (form submit destination) → **SAFE UNKNOWN** finding, not silent pass.
- If **cannot determine** whether two pages compete → flag **SAFE UNKNOWN** + suggest SEO human review.

---

## 8. Non-claims

- No LLM-based “semantic similarity pass” as factory default.
- No guarantee that all orphan entities are discoverable in one QA pass.

---

*End of Semantic QA Rules v0.*

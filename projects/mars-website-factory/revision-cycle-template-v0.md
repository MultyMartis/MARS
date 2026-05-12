# Operational template — Revision cycle (v0)

**Status:** **documentation-only** pattern for classifying changes and their **QA / approval / invalidation** consequences. **Not** a version-control bot, **not** auto-regeneration.

**Normative references:** [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md).

---

## 1. Revision request

| Field | Value |
|-------|-------|
| Requested by (lane) | |
| Target artifact(s) | |
| Business driver | |

---

## 2. Revision class

Choose one (or decompose into sub-requests):

| Class | Definition | Typical QA impact |
|-------|--------------|---------------------|
| **Copy-only** | Text changes; no layout/semantic structure | Limited — spot QA + trust consistency |
| **Visual tuning** | Tokens, spacing, imagery swaps within frozen wire | Design + frontend QA |
| **Structural** | Sections added/removed/reordered; new CTAs | Blueprint + downstream full invalidation |
| **Semantic** | Offer, geo, proof, SEO intent, entity facts | Semantic QA + dependent artifacts |
| **Technical** | Build, performance, a11y implementation | Frontend QA + possible delivery gate |

---

## 3. Bounded revision

- **In-scope** edits (explicit list):
- **Out-of-scope** (explicit forbidden edits to prevent drift):

---

## 4. Structural revision triggers

If structural, confirm:

- [ ] HITL pre-approval per [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)
- [ ] Blueprint supersede / version id per [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md)

---

## 5. Invalidation

| Upstream revision | Downstream artifacts invalidated | Bus / routing note |
|-------------------|----------------------------------|--------------------|
| | | |

([artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md))

---

## 6. QA reset

Per [revision-semantics-v0.md](revision-semantics-v0.md) and [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md):

- **Lanes requiring full re-QA:**
- **Lanes requiring spot re-QA:**

---

## 7. Approval inheritance

Per [approval-semantics-v0.md](approval-semantics-v0.md) and [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md):

- Which prior approvals **expire** with this revision:
- Which approvals **inherit** conditionally:

---

## 8. Reporting

- Append to project REPORT per [reporting-standard-v0.md](reporting-standard-v0.md).
- Emit appropriate **orchestration signal** tokens in prose ([orchestration-signals-v0.md](orchestration-signals-v0.md)).

---

*Template v0 — controlled change without silent supersede.*

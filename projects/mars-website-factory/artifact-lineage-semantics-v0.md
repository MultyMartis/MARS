# MARS Website Factory — Artifact Lineage Semantics v0

**Status:** **documentation only** — **normalized lineage vocabulary** for artifact instances. **Not** a version-control system, **not** Merkle DAG storage, **not** automated lineage tracking software.

**Version:** v0.

**Related:** [artifact-state-model-v0.md](artifact-state-model-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md).

---

## 1. Core lineage roles

| Term | Definition |
|------|------------|
| **Parent artifact** | The **immediate upstream** artifact instance from which this artifact was **authored or derived** (e.g. Blueprint → Design handoff). |
| **Child artifact** | Downstream artifact that **declares** this artifact in **lineage.parent** or **dependencies**. |
| **Sibling revision** | Another **revision_id** of the **same artifact_id** (or same logical role) that **does not** supersede the other yet — competing drafts are **invalid** for forward routes until one wins HITL. |
| **Supersede chain** | Ordered list **A → B → C** where each **supersedes** the prior approved/frozen baseline for the same role. |
| **Rollback lineage** | **Selection pointer** to a **prior** release or design baseline as active per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) — audit keeps full chain. |
| **Branch lineage** | Parallel experimental line (e.g. alt design) with **distinct artifact_id**; merge requires HITL + explicit **supersede** or **abandon** narrative. |
| **Frozen lineage** | Chain segment where **freeze_state** applies; new edits must **branch** or **reopen** — no silent edits on frozen nodes. |

---

## 2. Lineage drift

**Lineage drift** = documented parent pointers **no longer** describe actual authoring truth (e.g. manual body edit without revision).

| Severity | Response |
|----------|----------|
| **Documentation gap** | Fix metadata with HITL + REPORT; may require **revision_id** bump. |
| **Consumer misled** | Treat as **stale transfer**; block downstream delivery until reconciled. |

---

## 3. Lineage invalidation

Occurs when:

- Parent **invalidated** or **superseded** but child **dependencies** not updated.  
- **Circular** or **impossible** parent chain detected in audit.

**Rule:** child envelope **qa_state** / **semantic_state** must reflect **invalidated** until dependencies list is corrected.

---

## 4. Lineage orphaning

**Orphaning** = parent removed, lost, or **revoked** without child update.

| Outcome | Action |
|---------|--------|
| **Orphan child** | **Blocked** for forward routes per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md). |
| **Recovery** | Reattach to valid parent revision or **deprecate** child with HITL. |

---

## 5. Relationship to revision vs regeneration

- **Revision** — deliberate change; lineage **extends** with new node or revision suffix.  
- **Regeneration** — re-produce content; may **reuse artifact_id** policy per [regeneration-semantics-v0.md](regeneration-semantics-v0.md); lineage must record **regeneration run id** in REPORT if no new artifact_id.

---

## 6. Non-claims

- **Not** git `blame` automation.  
- **Not** blockchain provenance.

---

## 7. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial lineage semantics (documentation only). |

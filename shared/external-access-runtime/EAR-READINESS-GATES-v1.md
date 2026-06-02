# EAR Readiness Gates v1

**Purpose:** Define **when** a snapshot may advance between lifecycle stages — gate philosophy and checklist semantics.  
**Status:** architecture specification — **no** gate automation.  
**Phase:** 2B  

---

## Gate philosophy

| Principle | Meaning |
|-----------|---------|
| **Explicit advancement** | Each stage has entry criteria; skipping stages is invalid for consumer handoff |
| **Fail closed** | Uncertainty blocks Publish, not “best effort” consumer intake |
| **Human authority** | Operator approves transitions at Request, Validate/Publish, Archive |
| **EAR checks structure** | EAR validates contract and honesty; EAR does not approve business risk |
| **Honest quality** | Declared quality level must match evidence or explicit downgrade |

```
Acquire complete?  ──no──►  remain candidate / re-Acquire
        │
       yes
        ▼
     Validate  ──fail──►  SAFE UNKNOWN / reject ──►  No Publish
        │
       pass
        ▼
      Store
        ▼
     Publish  ──fail──►  No Consumer Access
        │
       pass
        ▼
     Consume
        ▼
     Archive (when policy triggers)
```

---

## Gate G0 — Request approved

**Advance to Acquire when:**

| Criterion | Required |
|-----------|----------|
| Operator authorized target `site_id` | Yes |
| Acquisition mode 0, 1, or 2 (not 3) | Yes |
| Target quality level declared | Yes |
| Consumer identified (e.g. `ocpilot`) | Yes |
| Scope and environment class documented | Yes or **SAFE UNKNOWN** with charter note |
| HITL reference recorded | Yes |

**Block:** Mode 3; missing operator sign-off.

---

## Gate G1 — Acquire complete

**Advance to Validate when:**

| Criterion | Required |
|-----------|----------|
| Candidate package assembled (logical sections) | Yes |
| `acquisition-log` / `access-log` started | Yes |
| `ear_mode` recorded | Yes |
| No secrets in git-bound candidate copy | Yes |
| No write operations to live SITE in v1 workflow | Yes |
| Gaps listed in `safe-unknown` (not silent omission) | Yes |

**Block:** Embedded credentials; Mode 3 evidence; empty critical sections without `safe-unknown`.

**SAFE UNKNOWN:** Connector completeness (Mode 2 future) — operator attestation required until automated checks exist.

---

## Gate G2 — Validate passed

**Advance to Store when:**

| Criterion | Required |
|-----------|----------|
| Contract version declared and supported | Yes |
| Quality level matches evidence per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | Yes |
| No quality inflation (e.g. Level 3 claim with Level 1 body) | Yes |
| PII policy respected (no full row dumps in v1) | Yes |
| `snapshot_id` unique and consistent with `site_id` | Yes |
| Operator validate go/no-go | Yes |

**Block:** Failed validation per [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md).

**Downgrade path:** Operator may lower declared quality and re-run G2 with explicit approval.

---

## Gate G3 — Store complete

**Advance to Publish when:**

| Criterion | Required |
|-----------|----------|
| G2 passed | Yes |
| Artifacts placed per [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) | Yes |
| Immutability convention acknowledged for `snapshot_id` | Yes |
| `bulk_root` or equivalent reference documented if bulk exists | If bulk used |
| Secrets not co-located with consumer-readable publish path | Yes |

**SAFE UNKNOWN:** Storage technology verification — operator responsibility.

---

## Gate G4 — Publish approved

**Advance to Consumer Access when:**

| Criterion | Required |
|-----------|----------|
| G3 complete | Yes |
| Operator publish approval recorded | Yes |
| `published_at` / publish marker in metadata or log | Yes |
| `consumer_target` set | Yes |
| Handoff contains references only — no credentials | Yes |

**Block:** Unvalidated candidate; raw WinSCP folder without spec wrap.

---

## Gate G5 — Consume allowed (consumer-side)

EAR documents consumer intake gates for alignment; enforcement is consumer charter.

| Criterion | Required |
|-----------|----------|
| Snapshot is **published** | Yes |
| Consumer supports contract version | Yes |
| Quality level meets phase minimum for planned audit | Per consumer guide |
| Residual `safe-unknown` reviewed for phase blocks | Yes |

**Block:** Unpublished package; live SITE as default input.

---

## Gate G6 — Archive

**Advance to Archive when (any):**

| Trigger | Notes |
|---------|-------|
| Newer `snapshot_id` supersedes | Prior → Archive |
| Site audit closed | Operator decision |
| Retention policy | Operator decision |

Archive does not require consumer completion.

---

## Validation failed → SAFE UNKNOWN → No publish

```
Validate
   │
   ├─ pass ──► Store ──► Publish ──► Consumer
   │
   └─ fail / ambiguous
           │
           ▼
      SAFE UNKNOWN (document gaps)
           │
           ▼
      No Publish
           │
           ▼
      Operator: re-Acquire | downgrade | abandon
```

**Ambiguous** validation is treated as **fail** until operator resolves.

---

## Gate summary table

| Gate | From → To | Primary owner |
|------|-----------|---------------|
| G0 | (charter) → Acquire | Operator |
| G1 | Acquire → Validate | EAR assembles; Operator attests complete |
| G2 | Validate → Store | EAR checks; Operator go |
| G3 | Store → Publish | Operator |
| G4 | Publish → Consume | Operator publish; Consumer intake |
| G6 | Active → Archive | Operator |

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) | Stages |
| [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) | Publish rules |
| [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) | Failure types |

---

## SAFE UNKNOWN

- Machine-readable gate definitions (JSON schema) — Phase 4 candidate
- Automated gate runner — not in v1

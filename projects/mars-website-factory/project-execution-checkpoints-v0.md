# MARS Website Factory — Project Execution Checkpoints v0

**Status:** **documentation only** — **human** checkpoint definitions (**C01–C08**). **Not** a persisted state machine.

**Version:** v0.

**Related:** [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [reference-run-sequence-v0.md](reference-run-sequence-v0.md), [workflow-map.md](workflow-map.md), [approval-semantics-v0.md](approval-semantics-v0.md), [reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md).

---

## Checkpoint index

| ID | Name | Unlocks (reference) |
|----|------|---------------------|
| **C01** | Intake Approved | R02 |
| **C02** | Strategy Locked | R04 (IA) |
| **C03** | IA Locked | R05 |
| **C04** | Blueprint Approved | R06–R07 |
| **C05** | Design Approved | R10 |
| **C06** | Frontend Freeze | R12–R13 |
| **C07** | Validation Pass | R14 |
| **C08** | Delivery Approved | R15 / release |

---

## C01 — Intake Approved

| Field | Content |
|-------|---------|
| **Required evidence** | Signed intake summary; explicit `scope_in` / `scope_out`; open questions list with owners. |
| **Blockers** | Missing approver; contradictory goals; unidentified compliance chain. |
| **Rollback rules** | Return to **R01**; void downstream drafts that assumed old scope (**narrative discard** — no auto-rollback engine). |
| **Invalidation triggers** | Stakeholder model change; new regulated market; merger/acquisition messaging shift. |
| **Waiver rules** | **None** for missing compliance identity — park or escalate **UNKNOWN**. |
| **Required reports** | Intake stage REPORT + HITL note for **G1**. |

---

## C02 — Strategy Locked

| Field | Content |
|-------|---------|
| **Required evidence** | **G2** approval record; strategy + SEO hypothesis artifacts versioned/labeled per project norms. |
| **Blockers** | Unresolved SEO vs commercial conflict; missing brand/compliance sign-off when sensitive. |
| **Rollback rules** | Reopen strategy → IA may not start; if IA started, mark IA draft **stale** until realigned. |
| **Invalidation triggers** | Site type reclassification; major offer change; CTA story rewrite. |
| **Waiver rules** | **HITL-only** for bounded time-boxed assumptions (**conditional approval** per [approval-semantics-v0.md](approval-semantics-v0.md)). |
| **Required reports** | Strategy stage REPORT; invalidation report if reopening ([reference-run-reporting-v0.md](reference-run-reporting-v0.md)). |

---

## C03 — IA Locked

| Field | Content |
|-------|---------|
| **Required evidence** | **G3** partial sign-off (PM + tech); published sitemap/template/URL spec. |
| **Blockers** | Critical journey unreachable; scope explosion vs intake. |
| **Rollback rules** | IA reopen forces blueprint halt; blueprint work in flight flagged **suspect**. |
| **Invalidation triggers** | URL scheme change; template merge/split; nav model swap. |
| **Waiver rules** | Tech debt / phased launch waivers require HITL + explicit **SAFE UNKNOWN** on deferred URLs. |
| **Required reports** | IA stage REPORT + checkpoint minutes. |

---

## C04 — Blueprint Approved

| Field | Content |
|-------|---------|
| **Required evidence** | **G3** blueprint batch approval; blueprint QA **pass** or **approved conditional** with listed residuals. |
| **Blockers** | Open blueprint QA blockers without waiver; registry-invalid `block_id`. |
| **Rollback rules** | Return to **R05** / **R06**; design handoff packs **must not** proceed on stale blueprint IDs. |
| **Invalidation triggers** | Block swap; CTA target change; semantic dependency break per [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md). |
| **Waiver rules** | QA lane waiver + HITL only ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **Required reports** | Blueprint REPORT + **QA REPORT** §4.3 + freeze report if batch frozen. |

---

## C05 — Design Approved

| Field | Content |
|-------|---------|
| **Required evidence** | **G5** closure; design QA pass or approved CR list with bounds. |
| **Blockers** | Unbounded change requests; unresolved a11y/compliance flags when policy blocks. |
| **Rollback rules** | Reopen design → frontend handoff and production **halt** until new freeze. |
| **Invalidation triggers** | Visual story change affecting CTA/trust semantics; brand breach. |
| **Waiver rules** | Design QA waivers HITL-documented; no silent “looks fine.” |
| **Required reports** | Design QA REPORT + design freeze report. |

---

## C06 — Frontend Freeze

| Field | Content |
|-------|---------|
| **Required evidence** | **G6** sign-off; agreed commit/PR/tag; build evidence if build was run (**honest** per [safe-unknown-boundary.md](safe-unknown-boundary.md)). |
| **Blockers** | Known blocker defects; failing build when build is claimed as gate. |
| **Rollback rules** | Frontend reopen invalidates downstream validation and delivery candidate ([delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md)). |
| **Invalidation triggers** | Design freeze break; blueprint semantic fix after frontend cut. |
| **Waiver rules** | Blocker waiver + security review when **SECURITY RISK** flagged. |
| **Required reports** | Frontend implementation REPORT + optional freeze report. |

---

## C07 — Validation Pass

| Field | Content |
|-------|---------|
| **Required evidence** | Final validation **go** recommendation with cross-lane evidence list ([validation-consistency-model-v0.md](validation-consistency-model-v0.md)). |
| **Blockers** | Open cross-lane contradictions; missing legal pages when required; **no-go** without HITL path. |
| **Rollback rules** | Targeted return to artifact-owning stages per failure class ([reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md)). |
| **Invalidation triggers** | Late registry discovery; security regression; SEO emergency rewrite. |
| **Waiver rules** | Validation waivers per [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) — **HITL** + audit. |
| **Required reports** | **Validation REPORT** §4.5. |

---

## C08 — Delivery Approved

| Field | Content |
|-------|---------|
| **Required evidence** | **G7** when public deploy; delivery manifest; rollback notes. |
| **Blockers** | Missing ops owner; unknown hosting target without signed **SAFE UNKNOWN** acceptance. |
| **Rollback rules** | Operational rollback per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) — **manual** playbooks. |
| **Invalidation triggers** | Post-delivery defect class **A** (critical) per project policy → may trigger new program increment, not silent hotfix without REPORT. |
| **Waiver rules** | Customer acceptance waivers documented in delivery REPORT. |
| **Required reports** | **Delivery REPORT**; invalidation report if delivery package superseded. |

---

*End of Project Execution Checkpoints v0.*

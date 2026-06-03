# MIG Pilot #1 — Триумф / Грузотакси / Краснодар

**Status:** preparation package only — **pilot not executed**  
**Freeze baseline:** [projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/](../../../projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/)  
**Intake contract:** [projects/mig/contracts/mig-research-request-contract-v0.md](../../../projects/mig/contracts/mig-research-request-contract-v0.md)

---

## Purpose

Human-supervised preparation for the **first real MIG pilot** on market **Грузотакси**, region **Краснодар**, client project **Триумф**.

This folder holds the canonical Research Request template, seed query set, operator checklists, and success criteria. **No SERP, competitors, or session artifacts live here until execution.**

---

## Package contents

| File | Role |
|------|------|
| [request-triumph-gruzotaxi-krasnodar-v1.json](request-triumph-gruzotaxi-krasnodar-v1.json) | Canonical Research Request (no `manual_serp` until operator capture) |
| [request-triumph-gruzotaxi-krasnodar-v1-fields.md](request-triumph-gruzotaxi-krasnodar-v1-fields.md) | Field-by-field documentation |
| [pilot-query-seed-set-v1.json](pilot-query-seed-set-v1.json) | Unoptimized seed queries — not clustered |
| [pilot-serp-capture-checklist.md](pilot-serp-capture-checklist.md) | Manual SERP capture procedure |
| [pilot-execution-checklist.md](pilot-execution-checklist.md) | End-to-end pilot run steps |
| [pilot-success-criteria.md](pilot-success-criteria.md) | Measurable pass/fail outcomes |

---

## Canonical pilot flow

```text
groundtruth_run  (Research Request)
      ↓
manual_serp      (operator capture — before inbox drop)
      ↓
Task File Adapter
      ↓
runMigSession
      ↓
Research Pack    (research_pack.draft.md → human approval)
```

`request_type: groundtruth_run` passes adapter validation (OR-10). Do not use the obsolete `serp_capture` + identical `capture_profile` workaround.

---

## Execution entry point (when ready)

1. Confirm template uses `request_type: groundtruth_run` ([request-triumph-gruzotaxi-krasnodar-v1.json](request-triumph-gruzotaxi-krasnodar-v1.json)).
2. Complete manual SERP capture per checklist.
3. Insert `manual_serp` into the Research Request (or attach per adapter discipline).
4. Copy request to production inbox:

   ```text
   incoming/mig/requests/request-triumph-gruzotaxi-krasnodar-v1.json
   ```

5. Run adapter (human-supervised):

   ```powershell
   .\projects\mig\tools\run-task-file-adapter.ps1
   ```

6. Follow [pilot-execution-checklist.md](pilot-execution-checklist.md).

---

## Boundaries

- **Do not** commit fake SERP, competitors, or findings into this package.
- **Do not** run the adapter against an incomplete request (missing `manual_serp` for MVP manual path).
- MIG acquires reality; ORCA interprets — see [mig-orca-handoff-contract-v0.md](../../../projects/mig/contracts/mig-orca-handoff-contract-v0.md).

---

## Related Triumph context (other niches)

Existing repo work for **Триумф** targets **манипулятор** (PPC / landing), not грузотакси. Treat that material as **client lineage only** — not groundtruth for this pilot.

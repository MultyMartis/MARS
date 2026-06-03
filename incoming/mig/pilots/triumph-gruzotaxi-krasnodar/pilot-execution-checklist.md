# Pilot Execution Checklist — MIG Pilot #1

**Pilot:** Триумф / Грузотакси / Краснодар  
**Mode:** human-supervised  
**Adapter path:** Task File → `runMigSession` (OR-09, `groundtruth_run` validation OR-10)

---

## Phase 0 — Prerequisites

- [ ] Pre-pilot freeze baseline acknowledged ([pre-pilot-gruzotaxi-krasnodar-v1](../../../../projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/))
- [ ] Local verify scripts passed on freeze day (or re-run if runtime changed)
- [ ] Node.js available; repo root = `C:\AI MARS`
- [ ] No active conflicting request in `incoming/mig/processing/`

---

## Phase 1 — Prepare request

- [ ] Review [request-triumph-gruzotaxi-krasnodar-v1.json](request-triumph-gruzotaxi-krasnodar-v1.json)
- [ ] Confirm `request_type`: `groundtruth_run`
- [ ] Confirm `capture_profile`: `website_pass` + `landing_pass` on; `keyword_pass` + `deep_research_pass` off
- [ ] Confirm primary query = first `seed_queries` entry
- [ ] Update `created_at` if stale (optional, operator discretion)

---

## Phase 2 — Capture SERP (human)

- [ ] Follow [pilot-serp-capture-checklist.md](pilot-serp-capture-checklist.md)
- [ ] Save screenshots + `capture-notes.md` under `evidence/`
- [ ] Build `manual_serp` JSON from real observation

**Human review gate G1:** Operator confirms SERP evidence matches JSON.

---

## Phase 3 — Insert `manual_serp` and drop request

- [ ] Add `manual_serp` to Research Request
- [ ] Copy to `incoming/mig/requests/request-triumph-gruzotaxi-krasnodar-v1.json`
- [ ] Verify filename matches `request_id`
- [ ] Verify no `session_id` preset in file

**Human review gate G2:** Second operator or same operator re-reads JSON vs screenshots (recommended).

---

## Phase 4 — Run adapter

```powershell
cd "C:\AI MARS"
.\projects\mig\tools\run-task-file-adapter.ps1
```

- [ ] `request_type` remains `groundtruth_run` (no `serp_capture` workaround — OR-10)
- [ ] File moved: `requests/` → `processing/` → `completed/` or `failed/`
- [ ] Outcome sidecar present: `completed/request-triumph-gruzotaxi-krasnodar-v1.outcome.json`
- [ ] Registry updated: `incoming/mig/registry/request-index.json`

**If failed:** read `failed/*.error.json`; do not retry with edited SERP without new evidence note.

---

## Phase 5 — Inspect session

Session path from outcome: `projects/mig/sessions/{session_id}/`

- [ ] `session_manifest.json` — schema v0.2, `runtime_profile` / stages
- [ ] `serp_result.json` — normalized from `manual_serp`
- [ ] `competitors.json` — derived from SERP (may be empty — not a prep failure)
- [ ] `website_snapshots.json` — if `website_pass` ran
- [ ] `landing_observations.json` — if `landing_pass` ran
- [ ] `research_pack.draft.md` — draft pack exists

**Human review gate G3:** Operator reviews artifacts for obvious capture errors (wrong region, empty organic, fetch failures).

---

## Phase 6 — Inspect pack

- [ ] Open `research_pack.draft.md`
- [ ] Confirm scope section matches request
- [ ] Confirm SAFE UNKNOWN sections present where data missing
- [ ] Confirm no fabricated competitor narrative beyond artifacts

**Human review gate G4:** Operator accepts draft as honest groundtruth or marks session for re-capture.

---

## Phase 7 — Approve (HITL)

- [ ] Operator edits draft if needed (manual file edit)
- [ ] Create `research_pack.approved.md` (copy + sign-off block)
- [ ] Set manifest approval fields when discipline exists (or document in pack header):

  ```text
  Approved By: <operator_id>
  Approved At: <ISO-8601>
  ```

**Human review gate G5:** Approval is **human only** — no automated approval.

---

## Phase 8 — Prepare ORCA handoff

Per [mig-orca-handoff-contract-v0.md](../../../../projects/mig/contracts/mig-orca-handoff-contract-v0.md):

- [ ] Research Scope documented
- [ ] Region + date + queries listed
- [ ] Evidence sources named (Yandex mobile manual capture)
- [ ] Snapshot pointers (session folder paths)
- [ ] Observations from pack
- [ ] Evidence grade / SAFE UNKNOWN preserved
- [ ] **Approved By** present

Deliver to ORCA operator via agreed human channel (no automated pipeline in v0).

---

## Adapter validation (OR-10)

Task File Adapter v0.1 accepts `request_type: groundtruth_run` alongside `serp_capture` ([validate-canonical.js](../../../../projects/mig/lib/task-file-adapter/validate-canonical.js), [mig-task-file-adapter-spec-v0.1.md](../../../../projects/mig/contracts/mig-task-file-adapter-spec-v0.1.md) §8).

**Before Phase 4:** keep `groundtruth_run` in the inbox request. Do **not** downgrade to `serp_capture` — that workaround is obsolete after OR-10.

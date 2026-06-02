# OCPilot — Incoming Baselines

**Purpose:** quarantine dropzone for **candidate clean baseline** packages (OpenCart / ocStore vendor distributions) before promotion to `baselines/<version-folder>/`.

**Parent:** [../README.md](../README.md)

---

## Expected files (Run 3 — first baseline acquisition)

Operator will provide these baseline archives:

| Expected file | Expected package root inside ZIP | Target baseline (after intake) |
|---------------|----------------------------------|--------------------------------|
| `opencart-3.0.3.8-rs.zip` | `upload-3038-rs2/` | `baselines/ocstore-3038-rs2/` |
| `opencart-3.0.3.9-rs.zip` | `upload-3039-rs1/` | `baselines/ocstore-3039-rs1/` |

**Priority order:** (1) `opencart-3.0.3.8-rs.zip` → ocstore-3038-rs2; (2) `opencart-3.0.3.9-rs.zip` → ocstore-3039-rs1.

Archives are **not** present until operator places them. OCPilot must **inspect archive structure first** — OpenCart files are **not** assumed at ZIP root. See [archive-intake-rules.md](../../archive-intake-rules.md).

---

## Operator instructions

| Rule | Meaning |
|------|---------|
| **Place ZIP files here** | Copy into `projects/ocpilot/incoming/baselines/` — no other dropzone for Run 3 baselines |
| **Do not unpack** | Leave archives as ZIP; extraction is a controlled intake step if needed |
| **Do not rename after intake begins** | Filename is intake evidence |
| **Do not move during intake** | Keep archives in this folder until intake report is complete and operator approves next step |
| **Inspect structure first** | OCPilot lists Archive Root before Package Root / OpenCart Root detection |

No extraction required. No preprocessing required.

---

## What belongs here

| Allowed drop | Examples |
|--------------|----------|
| Official or claimed-official OpenCart release ZIP | `opencart-3.0.3.7.zip` from operator download |
| Official or claimed-official ocStore release ZIP | ocStore build archive — e.g. `opencart-3.0.3.8-rs.zip`, `opencart-3.0.3.9-rs.zip` |
| GitHub release asset | Tagged release `.zip` from verified repo |
| Operator-labeled «clean install» package | **Low trust until intake verifies** |

---

## What does NOT belong here

| Forbidden drop | Route instead |
|----------------|---------------|
| Live client site export | [incoming/project-sites/](../project-sites/README.md) |
| Full hosting backup (files + DB + configs) | [incoming/project-sites/](../project-sites/README.md) |
| Already-intake-approved baseline content | Direct to `baselines/<version-folder>/` per operator move (Run 3+) |
| Single extension or theme ZIP only | Project site or extension analysis path — not baseline |

---

## Workflow (summary)

1. Operator places package in this folder (external copy; avoid committing secrets/large binaries without policy).
2. OCPilot runs **baseline intake** — see [intake-workflow.md](../../intake-workflow.md).
3. OCPilot fills [intake-report-template.md](../../templates/intake-report-template.md).
4. Operator reviews trust level, risks, recommended destination (`baselines/opencart-3037/`, etc.).
5. On approval: sanitize, populate target baseline folder, create passport — **human-operated** (Run 3+).
6. Package removed from incoming or marked processed in report.

**No automatic moves.**

---

## Trust reminder

Filename and operator label are **not proof**. Every package is **Low trust** until intake elevates to Medium/High with evidence.

See [baseline-acquisition-strategy.md](../../baseline-acquisition-strategy.md).

---

## Related documents

- [archive-intake-rules.md](../../archive-intake-rules.md) — Archive Root, Package Root, OpenCart Root
- [baseline-acquisition-precheck.md](../../baseline-acquisition-precheck.md) — stop/go checklist before intake
- [baselines/storage-policy.md](../../baselines/storage-policy.md) — ZIP canonical; metadata permanent
- [run-3-preparation.md](../../run-3-preparation.md) — Run 3 operator and OCPilot tasks
- [baseline-storage-model.md](../../baseline-storage-model.md)
- [baseline-readiness-checklist.md](../../baseline-readiness-checklist.md)
- [quarantine-policy.md](../../quarantine-policy.md)

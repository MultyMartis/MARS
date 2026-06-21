# OCPilot SITE-001 Snapshot Readiness Audit v1

**Status:** **documented** — snapshot acquisition readiness audit (audit only).  
**Program:** OCPilot + EAR (cross-program readiness)  
**Audit date:** 2026-06-07  
**Auditor posture:** Registry Steward + EAR consumer readiness review (documentation-level)  
**Sibling:** [OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md) · [OCPILOT-SITE001-SNAPSHOT-READINESS-SUMMARY-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-SUMMARY-v1.md)  
**Prior audit:** [OCPILOT-SITE001-STATE-RECONCILIATION-AUDIT-v1.md](OCPILOT-SITE001-STATE-RECONCILIATION-AUDIT-v1.md)  
**Is not:** Snapshot acquisition, snapshot creation, Atlas changes, Run 5 execution, PILOT-001 live access, git commit.

**Restrictions observed:** No acquisition. No snapshot creation. No Atlas changes. No Run 5 execution. Audit only. No commit. No push.

---

# REPORT — SITE-001 Snapshot Readiness Audit

## 0. Goal and scope

**Goal:** Determine the **minimum evidence package** (EAR Snapshot Package) required to **resume OCPilot Run 5** Phases 2–8, classify the **required acquisition mode**, inventory **operator actions**, **required files/exports**, and **expected deliverables** — without performing acquisition or execution.

**Object in scope:** OCPilot **SITE-001** — Автосалон СИБКАР (slug `site-001`, TEST `https://sibcar.new-site.space/`).

**Sources reviewed:**

| Layer | Documents |
|-------|-----------|
| SITE-001 identity | [site-passport.md](../sites/site-001/site-passport.md) |
| Access | [project-access-brief.md](../sites/site-001/project-access-brief.md) |
| Charter | [AUDIT-CHARTER.md](../sites/site-001/AUDIT-CHARTER.md) |
| Program state | [OCPILOT-STATE.md](../OCPILOT-STATE.md) |
| Run 5 plan | [RUN-5-AUDIT-PLAN.md](../sites/site-001/reports/RUN-5-AUDIT-PLAN.md), [RUN-5-SCOPE.md](../sites/site-001/reports/RUN-5-SCOPE.md), [RUN-5-DATA-REQUEST.md](../sites/site-001/tasks/RUN-5-DATA-REQUEST.md), [RUN-5-FIRST-FINDINGS.md](../sites/site-001/reports/RUN-5-FIRST-FINDINGS.md) |
| Blockers | [AUDIT-BLOCKERS-v1.md](../freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) |
| EAR architecture | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md), [EAR-ACQUISITION-MODES-v1.md](../../shared/external-access-runtime/EAR-ACQUISITION-MODES-v1.md), [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../shared/external-access-runtime/EAR-SITE-001-ACQUISITION-OPTIONS-v1.md), [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../shared/external-access-runtime/EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md), [EAR-OPENCART-READINESS-CHECKLIST-v1.md](../../shared/external-access-runtime/EAR-OPENCART-READINESS-CHECKLIST-v1.md), [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) |
| EAR runtime | [R3.1-SNAPSHOT-PACKAGE-MODEL-v1.md](../../projects/ear-runtime/R3.1-SNAPSHOT-PACKAGE-MODEL-v1.md), [SITE-001-DRY-RUN-DECISION-v1.md](../../projects/ear-runtime/SITE-001-DRY-RUN-DECISION-v1.md) |
| PILOT-001 | [STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) |

**Out of scope:** Live site access, credential inspection, external bulk content review, EAR Validate/Publish execution, Phase 1 brand-replacement writes.

---

## 1. Current posture (snapshot gate)

### 1.1 Reconciled SITE-001 state (inherits reconciliation audit)

| Dimension | State | Implication for snapshot |
|-----------|-------|--------------------------|
| Registry | **READY FOR AUDIT** | Consumer may intake published snapshot |
| Run 5 charter | **AUTHORIZED** (read-only) | Acquisition scope is read-only only |
| Run 5 execution | **PAUSED** | Phases 2–8 blocked until snapshot |
| EAR acquisition | **NOT EXECUTED** | No `snapshot_id` exists for SITE-001 |
| PILOT-001 | **Charter only** | Mode 2 live path **not authorized** |
| Dry run (2026-06-07) | **PASS WITH NOTES** | Procedure rehearsed; **does not** authorize live acquisition |

### 1.2 Primary execution blocker

Per [AUDIT-BLOCKERS-v1.md](../freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) and [RUN-5-FIRST-FINDINGS.md](../sites/site-001/reports/RUN-5-FIRST-FINDINGS.md):

```text
B-ARCH-01 + B-EV-02: No published Snapshot Package; external bulk empty of site manifest/ZIP
```

External storage layout exists (`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\`) but **no site snapshot content** at initialization cutoff (2026-06-01). This audit does not re-verify external bulk — **SAFE UNKNOWN** whether operator placed artifacts since.

---

## 2. Minimum Snapshot Package for Run 5 resume

### 2.1 Quality level decision

| Target | Verdict | Authority |
|--------|---------|-----------|
| **Snapshot Quality Level 1** | **MINIMUM REQUIRED** | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) § Level 1; [AUDIT-BLOCKERS-v1.md](../freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md); [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../shared/external-access-runtime/EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) |
| Level 0 | **Insufficient** — cannot support baseline diff or version proof | Quality mapping § Level 0 |
| Level 2+ | **Not required for initial resume** — enables Phases 4–5 without `safe-unknown` gaps | Partial re-entry after `p1` publish |

**Run 5 resume definition:** OCPilot may begin **Phase 2** (version verification) and **Phase 3** (file tree diff) when a **published Level 1** package possesses **version proof** and **`file-manifest`** sufficient for baseline comparison. Phases 4–7 may proceed only when corresponding sections are populated or explicitly deferred in `safe-unknown/` with operator acknowledgment.

### 2.2 Exact Snapshot Package checklist (Level 1 minimum)

Logical package per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md). **Required for Run 5 resume** marked **R**; **required at L1 with honest `safe-unknown` allowed** marked **R\***.

| # | Package section | Classification | Run 5 gate | Maps to RUN-5-DATA-REQUEST |
|---|-----------------|----------------|------------|------------------------------|
| 1 | **identity** (`snapshot_id`, `acquisition_id`, `site_id`, `snapshot_contract`) | Required | **R** | — (EAR assembly) |
| 2 | **metadata/** (platform, version claims, `ear_mode`, `baseline_ref`, `consumer_target`) | Required | **R** | P1-A corroboration |
| 3 | **environment/** (`TEST` class) | Required | **R** | Passport / brief |
| 4 | **acquisition-log/** (mode, channels, approver, timestamps) | Required | **R** | P3-C channel confirmation |
| 5 | **safe-unknown/** (residual gaps) | Required | **R** | Honest listing of deferred P2/P3 items |
| 6 | **file-manifest/** — root folders + path list covering `admin/`, `catalog/`, `system/` | Required L1+ | **R** | **P1-B**, **P1-C** |
| 7 | **file-manifest/** — version proof files (`index.php`, `admin/index.php`) | Required L1+ | **R** | **P1-A** |
| 8 | **database-metadata/** — prefix + table list | Required L1+ or safe-unknown | **R\*** | **P3-B** — Phase 7 blocked if gap |
| 9 | **seo-structure/** — SEO enabled flag / rewrite indicators | Required L1+ or safe-unknown | **R\*** | **P3-A** — Phase 6 blocked if gap |
| 10 | **theme-info/** — active theme name | Required L1+ or safe-unknown | **R\*** | **P2-A** — Phase 4 blocked if gap |
| 11 | **extension-inventory/** | Optional L2+ | Deferred | **P2-B** — Phase 5 blocked until `p2` or section filled |
| 12 | **ocmod-inventory/** | Optional L2+ | Deferred | **P2-B** — Phase 5 blocked until `p2` or section filled |

**Hard minimum to unlock Run 5 Phases 2–3:** items **1–7** plus **P3-C** recorded in acquisition-log. Items **8–10** may be `safe-unknown` entries at first publish without blocking Phases 2–3.

**Validate fail condition:** If manifest cannot support version proof → package remains Level 0 or unpublished — Run 5 does not resume ([EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) § Level 1 Validate gate).

### 2.3 Operator raw exports (minimum file set)

Deliver to external bulk — **not git**. Naming per [RUN-5-DATA-REQUEST.md](../sites/site-001/tasks/RUN-5-DATA-REQUEST.md).

| export_id | Artifact | Destination (suggested) | Blocks |
|-----------|----------|-------------------------|--------|
| **EXP-P1-A** | Version excerpts (`index.php`, `admin/index.php` — `VERSION` only) | `materials/run5/` | Phase 2 |
| **EXP-P1-B** | Root layout listing (top-level folders, `install/` presence) | `materials/run5/` | Phase 3 prep |
| **EXP-P1-C** | File manifest (`admin/`, `catalog/`, `system/` — exclude cache/logs/sessions) | `materials/run5/run5-file-manifest.txt` or `snapshots/files/` | Phase 3 |
| **EXP-P3-C** | Channel confirmation note (SFTP / panel / ZIP / evidence-only) | `materials/run5/acquisition-channel-note.md` | Supervised access |
| **EXP-P2-C** *(optional)* | Compact ZIP if P1-C difficult — excludes configs, image bulk, cache | `snapshots/files/` | Alternative to EXP-P1-C |

**Deferred for `p1` (document in `safe-unknown/`):**

| export_id | Artifact | Unblocks |
|-----------|----------|----------|
| EXP-P2-A | Active theme identification | Phase 4 |
| EXP-P2-B | Extension + ocMod inventory | Phase 5 |
| EXP-P3-A | SEO metadata | Phase 6 |
| EXP-P3-B | DB table list + prefix | Phase 7 |

### 2.4 Bulk storage layout (operator placement)

| Path | Purpose |
|------|---------|
| `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\materials\run5\` | Raw exports EXP-P1-A/B/C, P3-C note |
| `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\snapshots\files\` | Optional ZIP (EXP-P2-C) |
| `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\snapshots\database\` | Future DB metadata sidecars (no row dumps) |
| `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\` | Credentials only — **never** in git or snapshot package |

Published snapshot `bulk_root` references external paths only — per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) § metadata.

---

## 3. Required acquisition mode

### 3.1 Mode classification

| Mode | Name | Available today? | Verdict for SITE-001 first package |
|------|------|------------------|-------------------------------------|
| **0** | Manual Evidence | **YES** | **Allowed** — operator collects without EAR runbook |
| **1** | Guided Evidence | **YES** | **RECOMMENDED** — maps to RUN-5-DATA-REQUEST + EAR workflow example |
| **2** | Connected Read Only | **NO** (design target; connector not implemented) | **NOT AVAILABLE** until HG-4 + PILOT-001 execution authorization |
| **3** | Connected Read Write | **Forbidden** | **N/A** |

### 3.2 Recommended mode: **Mode 1 — Guided Evidence**

**Rationale:**

1. [RUN-5-DATA-REQUEST.md](../sites/site-001/tasks/RUN-5-DATA-REQUEST.md) already defines the guided artifact list (P1–P3).
2. [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../shared/external-access-runtime/EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) specifies Mode 1, Level 1 for Run 5 resume.
3. [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../shared/external-access-runtime/EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) Path **SITE-001-1** aligns with Mode 1.
4. No connector implementation in repo; [PILOT-001 STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) — execution **NOT STARTED**.
5. [SITE-001-DRY-RUN-DECISION-v1.md](../../projects/ear-runtime/SITE-001-DRY-RUN-DECISION-v1.md) — dry run **does not** authorize Mode 2 live SFTP.

**Mode 0 fallback:** Operator may use Mode 0 if they prefer unstructured manual drops — same possession rules apply; higher inconsistency risk per [EAR-ACQUISITION-MODES-v1.md](../../shared/external-access-runtime/EAR-ACQUISITION-MODES-v1.md).

**Mode 2 deferred path:** When PILOT-001 receives execution authorization, first live package would use `ear_mode: 2`, Path **CON-L1-A** (SFTP read-only), same Level 1 target — possession rules unchanged.

### 3.3 Recommended acquisition path (Mode 1)

| Priority | Path ID | Channel stack | Notes |
|----------|---------|---------------|-------|
| **Primary** | **L1-D** | Beget hosting panel → ZIP export | Backup claimed 31.05.2026 Beget — **contents SAFE UNKNOWN** |
| **Alternate** | **L1-A** | ZIP only (operator-provided archive) | If panel export unavailable |
| **Alternate** | **L1-B** | SFTP read-only + metadata session | Manual SFTP until Mode 2 runtime |
| **Hybrid** | **L1-E** | Files (ZIP/SFTP) + phpMyAdmin table list | Raises L1 completeness; reduces `safe-unknown` |

Per [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../shared/external-access-runtime/EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) Path **SITE-001-1**.

---

## 4. Required operator actions (pre-acquisition)

Cross-walk to [EAR-OPENCART-READINESS-CHECKLIST-v1.md](../../shared/external-access-runtime/EAR-OPENCART-READINESS-CHECKLIST-v1.md).

| # | Action | Owner | Status (audit) |
|---|--------|-------|----------------|
| RA-01 | Confirm Run 5 read-only charter still valid | Operator | Charter active — [AUDIT-CHARTER.md](../sites/site-001/AUDIT-CHARTER.md) |
| RA-02 | Select **Mode 1** (or Mode 0 fallback); record decision | Operator | **PENDING** |
| RA-03 | Set target **Quality Level 1** for first publish (`p1`) | Operator | **PENDING** |
| RA-04 | Select acquisition path (L1-D / L1-A / L1-B / L1-E) | Operator | **PENDING** — channels SAFE UNKNOWN |
| RA-05 | Confirm TEST environment (`https://sibcar.new-site.space/`) | Operator | **PENDING** re-verification |
| RA-06 | Confirm credentials in external `secrets/` (not git) | Operator | Location rule documented; contents not audited |
| RA-07 | Acknowledge read-only discipline (no writes) | Operator | **PENDING** attestation |
| RA-08 | Define manifest exclusions (cache, logs, sessions, `image/catalog/`) | Operator + EAR | Per RUN-5-DATA-REQUEST P1-C |
| RA-09 | Define `config.php` redaction plan | Operator | Required before any ZIP |
| RA-10 | Identify Validate / Publish approver (HITL) | Operator | Per dry-run dual-HITL model |
| RA-11 | Deliver EXP-P1-A, P1-B, P1-C (+ P3-C note) | Operator | **MISSING** per RUN-5-FIRST-FINDINGS |
| RA-12 | Record expected `safe-unknown` gaps (P2/P3 deferred) | Operator | Recommended for `p1` |
| RA-13 | **Do not** start PILOT-001 / Mode 2 without HG-4 authorization | Operator | **FORBIDDEN** per dry-run decision |

**Documentation sync (non-blocking, reduces confusion):**

| ID | Action | Ref |
|----|--------|-----|
| SYNC-SR-01..03 | Align access-brief, README, passport with PAUSED execution | [OCPILOT-SITE001-STATE-RECONCILIATION-SUMMARY-v1.md](OCPILOT-SITE001-STATE-RECONCILIATION-SUMMARY-v1.md) |

---

## 5. Expected deliverables

### 5.1 EAR-side deliverables (first acquisition cycle)

| deliverable_id | Artifact | Quality | Consumer |
|----------------|----------|---------|----------|
| **DEL-EV-01** | Candidate Snapshot Package (assembled) | L1 candidate | EAR Validate |
| **DEL-EV-02** | `validation_status: PASS` at Level 1 (human HITL) | Certified L1 | EAR Publish |
| **DEL-EV-03** | Published `snapshot_id` (e.g. `snap-YYYYMMDD-site-001-run5-p1`) | L1 published | OCPilot intake |
| **DEL-EV-04** | Published reference in consumer registry / site materials index | Metadata only in repo | OCPilot Run 5 |

**Not claimed in this audit:** Actual `snapshot_id`, Validate outcome, Store placement — **SAFE UNKNOWN** until operator executes acquisition cycle.

### 5.2 OCPilot-side deliverables (after snapshot consumed — Run 5 resume)

| Phase | Deliverable | Location | Requires |
|-------|-------------|----------|----------|
| 2 | Version verification | `opencart-analysis/version-verification-v1.md` | EXP-P1-A + manifest |
| 3 | File diff summary | `opencart-analysis/file-diff-summary-v1.md` | EXP-P1-C |
| 4 | Theme inventory | `theme-analysis/active-theme-inventory-v1.md` | EXP-P2-A or `p2` |
| 5 | Extension/ocMod inventory | `extension-analysis/*.md` | EXP-P2-B or `p2` |
| 6 | SEO structure | `seo-url-analysis/seo-structure-v1.md` | EXP-P3-A or `p2` |
| 7 | Schema delta | `database-analysis/schema-delta-v1.md` | EXP-P3-B or `p2` |
| 8 | Consolidated report | `reports/RUN-5-AUDIT-REPORT.md` | Phases 2–7 |
| — | Registry transition | `project-site-registry.md` | Human approval → **AUDIT IN PROGRESS** |

### 5.3 Partial re-entry (`p2`) — optional follow-on

If `p1` publishes with P2/P3 in `safe-unknown/`:

| deliverable_id | Scope | Unblocks |
|----------------|-------|----------|
| **DEL-EV-05** | `snap-…-p2` scoped to extension-inventory + ocmod-inventory | Run 5 Phase 5 |
| **DEL-EV-06** | `snap-…-p3` scoped to seo-structure + database-metadata | Run 5 Phases 6–7 |

Per [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) § Partial snapshots.

---

## 6. Gap analysis (readiness verdict)

| Area | Ready? | Gap |
|------|--------|-----|
| Charter / scope | **YES** | Read-only authorized |
| Baseline reference | **YES** | `ocstore-3038-rs2` promoted |
| EAR architecture docs | **YES** | Spec, quality mapping, modes documented |
| EAR runtime (mock) | **YES WITH NOTES** | Dry run PASS WITH NOTES — not live trust |
| Mode 2 connector | **NO** | PILOT-001 not authorized |
| Operator artifacts | **NO** | P1 exports missing per RUN-5-FIRST-FINDINGS |
| Published snapshot | **NO** | No `snapshot_id` |
| Run 5 execution | **NO** | Correctly PAUSED |

**Snapshot readiness verdict:**

```text
READY FOR ACQUISITION REQUEST — NOT READY FOR RUN 5 EXECUTION
```

Operator may initiate **Mode 1 Request → Acquire → Validate → Publish** cycle. Run 5 Phases 2–8 remain **PAUSED** until **DEL-EV-03** exists.

---

## 7. Risk register (snapshot-specific)

| risk_id | Risk | Severity | Mitigation |
|---------|------|----------|------------|
| **SR-SNAP-01** | Beget backup ZIP incomplete (not full OpenCart tree) | High | Verify root folders before manifest; fallback L1-B SFTP |
| **SR-SNAP-02** | Operator chooses Mode 2 before authorization | High | HG-4 gate; dry-run decision explicit **NO** |
| **SR-SNAP-03** | Quality inflation (L1 claim without version proof) | High | Validate gate; fail → no publish |
| **SR-SNAP-04** | Secrets in manifest/ZIP | Critical | Redaction plan RA-09; quarantine policy |
| **SR-SNAP-05** | Stale access-brief **NO** blocks operator | Medium | SYNC-SR-01; charter authority overrides stale gate |
| **SR-SNAP-06** | Empty `comparison-notes/` weakens ocStore subtraction | Medium | Parallel methodology pass B-EV-05 |

---

## 8. Validation (audit constraints)

| Constraint | Observed |
|------------|----------|
| No acquisition | **Yes** |
| No snapshot creation | **Yes** |
| No Atlas changes | **Yes** |
| No Run 5 execution | **Yes** |
| Audit only | **Yes** |
| No commit / push | **Yes** |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-REGISTER-v1.md) | Checklist registers, mode matrix |
| [OCPILOT-SITE001-SNAPSHOT-READINESS-SUMMARY-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-SUMMARY-v1.md) | Executive summary + operator checklist |
| [OCPILOT-SITE001-STATE-RECONCILIATION-AUDIT-v1.md](OCPILOT-SITE001-STATE-RECONCILIATION-AUDIT-v1.md) | State drift context |

---

*OCPilot SITE-001 Snapshot Readiness Audit v1 — documentation only; no runtime claimed.*

---

OPERATOR ACTIONS REQUIRED

1. **Зафиксировать решение по режиму:** выбрать **Mode 1 (Guided Evidence)**; записать `ear_mode: 1`, target **Quality Level 1**, sequence `p1`.
2. **Выбрать путь сбора:** приоритет **L1-D** (Beget panel → ZIP); запасные **L1-A** (ZIP drop) или **L1-B** (ручной SFTP). **Не** выбирать Mode 2 / PILOT-001 без HG-4 authorization.
3. **Перепроверить TEST URL:** подтвердить `https://sibcar.new-site.space/`; зафиксировать в **EXP-P3-C**.
4. **Подтвердить канал доступа (P3-C):** `materials/run5/acquisition-channel-note.md` — panel / SFTP / ZIP-only; admin URL pattern без credentials.
5. **Проверить credentials:** только в external `secrets/` — не в репозитории.
6. **Подписать read-only discipline:** без file/DB/admin writes, cache reset.
7. **Определить manifest exclusions:** cache, logs, sessions, `image/catalog/`.
8. **Определить config.php redaction plan** перед любым ZIP.
9. **Назначить Validate и Publish approver (HITL).**
10. **Собрать EXP-P1-A** (version excerpts) → `materials/run5/`.
11. **Собрать EXP-P1-B** (root layout) → `materials/run5/`.
12. **Собрать EXP-P1-C** (file manifest) → `materials/run5/run5-file-manifest.txt`.
13. **(Опционально) EXP-P2-C** compact ZIP → `snapshots/files/`.
14. **Задокументировать safe-unknown** для отложенных P2/P3.
15. **Уведомить OCPilot:** external paths only — без секретов.
16. **EAR цикл:** Request → Acquire → Validate L1 → Publish → `snapshot_id`.
17. **После publish:** запросить human charter для Run 5 Phases 2–8; registry → **AUDIT IN PROGRESS**.
18. **Не выполнять:** PILOT-001, Mode 2, Run 5 execution, Phase 1 writes — до published snapshot.

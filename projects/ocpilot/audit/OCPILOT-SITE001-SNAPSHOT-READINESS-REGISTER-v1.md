# OCPilot SITE-001 Snapshot Readiness Register v1

**Status:** **documented** — snapshot acquisition readiness register (audit only).  
**Program:** OCPilot + EAR  
**Audit date:** 2026-06-07  
**Parent:** [OCPILOT-SITE001-SNAPSHOT-READINESS-AUDIT-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-AUDIT-v1.md) · [OCPILOT-SITE001-SNAPSHOT-READINESS-SUMMARY-v1.md](OCPILOT-SITE001-SNAPSHOT-READINESS-SUMMARY-v1.md)  
**Is not:** acquisition execution, runtime state table, git commit.

---

## 1. Register purpose

Единый **snapshot readiness register** для первого EAR Snapshot Package **SITE-001**: чеклист пакета, матрица режимов, реестр экспортов, deliverables, gaps и operator actions.

---

## 2. Readiness state register

| state_id | dimension | value | authority | blocks_run5 |
|----------|-----------|-------|-----------|---------------|
| **ST-SNAP-A** | Charter | **AUTHORIZED** (read-only) | AUDIT-CHARTER | No |
| **ST-SNAP-B** | Run 5 execution | **PAUSED** | OCPILOT-STATE | Yes — Phases 2–8 |
| **ST-SNAP-C** | Target quality | **Level 1** (minimum) | Quality mapping; blockers | Yes — until publish |
| **ST-SNAP-D** | Acquisition mode | **Mode 1 recommended**; Mode 2 N/A | Acquisition modes; PILOT-001 | Yes — until mode chosen + artifacts |
| **ST-SNAP-E** | Published snapshot | **MISSING** | RUN-5-FIRST-FINDINGS | Yes |
| **ST-SNAP-F** | Operator P1 exports | **MISSING** | RUN-5-DATA-REQUEST | Yes |

---

## 3. Snapshot Package section register (Level 1 minimum)

| reg_id | section | L1 rule | run5_resume | run5_phase_gate | data_request | status |
|--------|---------|---------|-------------|-----------------|--------------|--------|
| **PKG-01** | identity | Required | **R** | All | — | Not assembled |
| **PKG-02** | metadata/ | Required | **R** | All | P1-A | Not assembled |
| **PKG-03** | environment/ | Required | **R** | All | — | Declared TEST |
| **PKG-04** | acquisition-log/ | Required | **R** | Supervised access | P3-C | **Pending** |
| **PKG-05** | safe-unknown/ | Required | **R** | Honesty | P2/P3 deferred | **Pending** plan |
| **PKG-06** | file-manifest/ roots | Required L1+ | **R** | Phase 3 | P1-B | **Missing** |
| **PKG-07** | file-manifest/ paths | Required L1+ | **R** | Phase 3 | P1-C | **Missing** |
| **PKG-08** | file-manifest/ version proof | Required L1+ | **R** | Phase 2 | P1-A | **Missing** |
| **PKG-09** | database-metadata/ | L1 or safe-unknown | R* | Phase 7 | P3-B | **Missing** |
| **PKG-10** | seo-structure/ | L1 or safe-unknown | R* | Phase 6 | P3-A | **Missing** |
| **PKG-11** | theme-info/ | L1 or safe-unknown | R* | Phase 4 | P2-A | **Missing** |
| **PKG-12** | extension-inventory/ | L2+ optional | Deferred | Phase 5 | P2-B | **Deferred p2** |
| **PKG-13** | ocmod-inventory/ | L2+ optional | Deferred | Phase 5 | P2-B | **Deferred p2** |

**Legend:** **R** = hard gate for Run 5 resume (Phases 2–3); **R\*** = may be `safe-unknown` at `p1` without blocking Phases 2–3.

---

## 4. Operator export register

| export_id | name | format | external_path | snapshot_section | status |
|-----------|------|--------|---------------|------------------|--------|
| **EXP-P1-A** | Version excerpts | txt / screenshot | `materials/run5/` | metadata + file-manifest | **Missing** |
| **EXP-P1-B** | Root layout | listing txt | `materials/run5/` | file-manifest | **Missing** |
| **EXP-P1-C** | File manifest | `run5-file-manifest.txt` | `materials/run5/` or `snapshots/files/` | file-manifest | **Missing** |
| **EXP-P2-A** | Active theme | screenshot / listing | `materials/run5/` | theme-info | **Deferred** |
| **EXP-P2-B** | Extensions + ocMod | screenshot / listing | `materials/run5/` | extension + ocmod | **Deferred p2** |
| **EXP-P2-C** | Optional compact ZIP | zip | `snapshots/files/` | file-manifest alt | **Optional** |
| **EXP-P3-A** | SEO metadata | screenshot / counts | `materials/run5/` | seo-structure | **Deferred** |
| **EXP-P3-B** | DB table list | txt | `materials/run5/` or `snapshots/database/` | database-metadata | **Deferred** |
| **EXP-P3-C** | Channel confirmation | md note | `materials/run5/` | acquisition-log | **Missing** |

---

## 5. Acquisition mode register

| mode_id | name | implemented | authorized_site001 | recommendation | ear_mode value |
|---------|------|-------------|-------------------|----------------|----------------|
| **MODE-0** | Manual Evidence | Semantics only | **YES** | Fallback | `0` |
| **MODE-1** | Guided Evidence | Semantics only | **YES** | **PRIMARY** | `1` |
| **MODE-2** | Connected Read Only | **NO** | **NO** (PILOT-001) | Deferred | `2` |
| **MODE-3** | Connected Read Write | Forbidden | **NO** | N/A | — |

### 5.1 Mode decision matrix (SITE-001)

| situation | required_mode | path_ref |
|-----------|---------------|----------|
| First package, no connector | **Mode 1** (or 0) | SITE-001-1; L1-D / L1-A / L1-B |
| Operator has Beget panel + backup | **Mode 1** | Path L1-D |
| Operator has ZIP only | **Mode 1** or 0 | Path L1-A (OFF-L1-A) |
| SFTP manual (pre-runtime) | **Mode 1** | Path L1-B |
| PILOT-001 execution authorized (future) | **Mode 2** | CON-L1-A |
| Write / deploy / import | **Not EAR** | Separate charter |

---

## 6. Acquisition path register

| path_id | channel | quality_target | site001_fit | notes |
|---------|---------|----------------|-------------|-------|
| **L1-D** | Beget panel → ZIP | 1 | **Primary** | Backup 31.05.2026 claimed |
| **L1-A** | ZIP only | 1 | Alternate | Operator drop |
| **L1-B** | SFTP + metadata | 1 | Alternate | Manual until Mode 2 |
| **L1-E** | Hybrid files + DB | 1 | Enhanced | Reduces safe-unknown |
| **L1-F** | Admin-assisted | 1 | Supplement | Version/theme screenshots |
| **CON-L1-A** | SFTP connector | 1 | **Future** | PILOT-001 — not authorized |

---

## 7. Deliverables register

### 7.1 EAR cycle (pre–Run 5 resume)

| del_id | deliverable | owner | depends_on | status |
|--------|-------------|-------|------------|--------|
| **DEL-01** | Acquisition Request record (Mode 1, L1, SITE-001) | Operator | RA-02..04 | **Not started** |
| **DEL-02** | Operator exports EXP-P1-* + P3-C | Operator | RA-11 | **Missing** |
| **DEL-03** | Candidate Snapshot Package | EAR assembly | DEL-02 | **Not started** |
| **DEL-04** | Validate HITL sign-off (L1) | Operator | DEL-03 | **Not started** |
| **DEL-05** | Published `snapshot_id` | EAR Publish | DEL-04 | **Missing** |
| **DEL-06** | Repo materials index (paths only) | OCPilot | DEL-05 | **Not started** |

### 7.2 OCPilot Run 5 (post-consume)

| del_id | deliverable | phase | blocked_by |
|--------|-------------|-------|------------|
| **DEL-R5-02** | version-verification-v1.md | 2 | PKG-08 |
| **DEL-R5-03** | file-diff-summary-v1.md | 3 | PKG-06, PKG-07 |
| **DEL-R5-04** | active-theme-inventory-v1.md | 4 | PKG-11 or p2 |
| **DEL-R5-05** | extension-inventory-v1.md | 5 | PKG-12 or p2 |
| **DEL-R5-06** | seo-structure-v1.md | 6 | PKG-10 or p2 |
| **DEL-R5-07** | schema-delta-v1.md | 7 | PKG-09 or p2 |
| **DEL-R5-08** | RUN-5-AUDIT-REPORT.md | 8 | DEL-R5-02..07 |
| **DEL-R5-09** | Registry → AUDIT IN PROGRESS | — | Human + DEL-R5-02 start |

---

## 8. Blocker crosswalk register

| blocker_id | source | maps_to_pkg | resolution |
|------------|--------|-------------|------------|
| **B-ARCH-01** | AUDIT-BLOCKERS | PKG-01..13 | First published snapshot |
| **B-ARCH-02** | AUDIT-BLOCKERS | MODE-1 cycle | Operator Request |
| **B-EV-01** | AUDIT-BLOCKERS | PKG-08 | EXP-P1-A |
| **B-EV-02** | AUDIT-BLOCKERS | PKG-06, PKG-07 | EXP-P1-C |
| **B-EV-03** | AUDIT-BLOCKERS | EXP-P2-C | Optional ZIP |
| **B-EV-04** | AUDIT-BLOCKERS | PKG-09..13 | p1 safe-unknown + p2 |
| **B-EV-05** | AUDIT-BLOCKERS | — | Methodology pass (parallel) |

---

## 9. EAR readiness checklist register (SITE-001)

Mapped from [EAR-OPENCART-READINESS-CHECKLIST-v1.md](../../shared/external-access-runtime/EAR-OPENCART-READINESS-CHECKLIST-v1.md).

| chk_id | item | pass? | notes |
|--------|------|-------|-------|
| **EAR-RC-01** | Scope approved | **YES** | AUDIT-CHARTER read-only |
| **EAR-RC-02** | Mode selected | **NO** | Pending RA-02 |
| **EAR-RC-03** | Target level 1 | **NO** | Pending RA-03 |
| **EAR-RC-04** | Path selected | **NO** | Pending RA-04 |
| **EAR-RC-05** | Channels identified | **NO** | P3-C pending |
| **EAR-RC-06** | Environment TEST | **YES** | Declared — re-verify RA-05 |
| **EAR-RC-07** | Consumer ocpilot + baseline | **YES** | ocstore-3038-rs2 |
| **EAR-RC-08** | Credentials external | **PARTIAL** | Rule documented; not verified |
| **EAR-RC-09** | Read-only discipline | **NO** | Pending RA-07 |
| **EAR-RC-10** | Backup known | **YES** | 31.05.2026 Beget — claim only |
| **EAR-RC-11** | Storage available | **YES** | External path exists |
| **EAR-RC-12** | Publish path defined | **NO** | Pending RA-10 |
| **EAR-RC-13** | Risk accepted | **NO** | Pending operator review |
| **EAR-RC-14** | SAFE UNKNOWN documented | **NO** | Pending RA-12 |
| **EAR-RC-15** | HITL reference | **NO** | Pending RA-10 |
| **EAR-RC-16** | Exclusions policy | **NO** | Pending RA-08 |
| **EAR-RC-17** | Secret redaction plan | **NO** | Pending RA-09 |
| **EAR-RC-18** | Hybrid time window | N/A | Unless L1-E |
| **EAR-RC-19** | Prior snapshot | N/A | First package |
| **EAR-RC-20** | Validate owner | **NO** | Pending RA-10 |

**Readiness checklist score:** **4 / 20 explicit pass** — **not ready to Acquire** until operator completes pending items.

---

## 10. Operator action register

| act_id | action | priority | owner | status |
|--------|--------|----------|-------|--------|
| **OP-01** | Record Mode **1** decision | P0 | Operator | Pending |
| **OP-02** | Record Level **1** target for `p1` | P0 | Operator | Pending |
| **OP-03** | Select path L1-D / L1-A / L1-B / L1-E | P0 | Operator | Pending |
| **OP-04** | Re-verify TEST URL live | P0 | Operator | Pending |
| **OP-05** | Confirm credentials in `secrets/` (external) | P0 | Operator | Pending |
| **OP-06** | Sign read-only discipline acknowledgment | P0 | Operator | Pending |
| **OP-07** | Document manifest exclusions policy | P0 | Operator | Pending |
| **OP-08** | Document config.php redaction plan | P0 | Operator | Pending |
| **OP-09** | Name Validate + Publish approver | P0 | Operator | Pending |
| **OP-10** | Deliver EXP-P1-A (version excerpts) | P0 | Operator | **Missing** |
| **OP-11** | Deliver EXP-P1-B (root layout) | P0 | Operator | **Missing** |
| **OP-12** | Deliver EXP-P1-C (file manifest) | P0 | Operator | **Missing** |
| **OP-13** | Deliver EXP-P3-C (channel note) | P0 | Operator | **Missing** |
| **OP-14** | List planned safe-unknown for P2/P3 | P1 | Operator | Pending |
| **OP-15** | Notify OCPilot: external paths only (no secrets) | P1 | Operator | Pending |
| **OP-16** | **Do not** execute PILOT-001 / Mode 2 | P0 | Operator | Hold |
| **OP-17** | Optional: SYNC-SR-01..03 doc alignment | P2 | Editor | Pending |

---

## 11. SAFE UNKNOWN register

| topic | status | unblock |
|-------|--------|---------|
| Beget backup contains full tree | **SAFE UNKNOWN** | EXP-P1-B after ZIP extract |
| SFTP vs FTP preference | **SAFE UNKNOWN** | EXP-P3-C |
| Admin URL | **SAFE UNKNOWN** | EXP-P3-C |
| External bulk updated since 2026-06-01 | **SAFE UNKNOWN** | Operator listing |
| First `snapshot_id` value | **SAFE UNKNOWN** | EAR Publish |
| Mode 0 vs 1 final choice | **SAFE UNKNOWN** | OP-01 |

---

*OCPilot SITE-001 Snapshot Readiness Register v1 — documentation only.*

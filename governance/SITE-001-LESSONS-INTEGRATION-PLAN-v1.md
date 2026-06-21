# REPORT — SITE-001 LESSONS INTEGRATION PLAN

**Type:** Governance integration plan — analysis only  
**Date:** 2026-06-10  
**Scope:** Website Factory · OCPilot · Web-GPT workflow · MARS governance  
**Status:** **PLAN ONLY** — no target documents modified by this artifact

**Explicit exclusions (honored):** No site modifications · No FTP · No TEST writes · No WF-V3 launch · No new project charters · No automatic updates to existing governance files · No commit implied

---

## 1. Source

**Primary source (canonical anti-regression):**

[projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md](../projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md)

**Evidence base referenced by source:**

| Artifact | Role |
|----------|------|
| [SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md](../projects/ocpilot/sites/site-001/reports/SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md) | Primary failure audit |
| [SITE-001-RESTORE-POINT-REGISTRY-v1.md](../projects/ocpilot/sites/site-001/reports/SITE-001-RESTORE-POINT-REGISTRY-v1.md) | Restore points + WF-V3 transition intent |
| [SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](../projects/ocpilot/sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) | STOP directive (not enforced) |
| [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](../projects/ocpilot/sites/site-001/reports/SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) | Zone scoring evidence (homepage 3/10) |

**Rule ID namespaces in source:** `WF-AR-01..13` (Website Factory) · `OC-AR-01..12` (OCPilot) · `WG-AR-01..12` (Web-GPT) · Gates §6

---

## 2. Website Factory Integration

Rules from source §3 (`WF-AR-*`). Target documents are **existing** unless marked **NEW (recommended)**.

| Rule | Target document | Integration method | Priority |
|------|-----------------|-------------------|----------|
| **WF-AR-01** Design authority before implementation — one active concept per site; supersession lists retired tokens/hooks | **NEW** `workspaces/website-factory-reference-v1/design-system/WEBSITE-FACTORY-DESIGN-AUTHORITY-v1.md` (companion; cross-ref from `DESIGN-SYSTEM-RULES-v1.md`) | **New companion doc** — do not rewrite `DESIGN-SYSTEM-RULES-v1.md`; add 1-paragraph pointer in DS-R15 vicinity | **P0** |
| **WF-AR-02** Screen architecture first — DOM zones, surface rules, anti-patterns, reference PNG path | Same companion doc §Screen Blueprint Contract | Add required fields table + blocked conditions | **P0** |
| **WF-AR-03** Clean-room declaration when legacy DOM blocks target class | Same companion doc §Clean-Room Trigger | Cross-ref `WF-AR-13`; link to OCPilot escalation | **P0** |
| **WF-AR-04** Stop cosmetic loop — FINISHING vs REDESIGN label | **NEW** `workspaces/website-factory-reference-v1/design-system/WF-VISUAL-WAVE-CLASSIFICATION-v1.md` (short companion) | Wave-type taxonomy table; 3-line cross-ref in `DESIGN-SYSTEM-RULES-v1.md` footer only | **P1** |
| **WF-AR-05** Prototype before integration | Companion DESIGN-AUTHORITY doc §Prototype Gate | Add handoff blocked condition to `runtime-architecture/RUNTIME-HANDOFFS-v1.md` HO-07/HO-08 footnote | **P1** |
| **WF-AR-06** Single concept lock 30 days | Companion DESIGN-AUTHORITY doc §Concept Lock | Operator charter requirement; no DS-R rewrite | **P1** |
| **WF-AR-07** Composition audit deliverable `*-COMPOSITION-AUDIT-v1.md` | `runtime-architecture/RUNTIME-HANDOFFS-v1.md` HO-07 blocked conditions | **Append** one blocked-condition row: missing composition audit for anatomy/layout charters | **P1** |
| **WF-AR-08** Visual Proof Pack review before operator PASS recommendation | `production-qa/PRODUCTION-QA-SYSTEM-v1.md` §Operator-facing visual checkpoint (new subsection) | **Add subsection** «Operational visual handoff (OCPilot path)» — 10 lines max; clarify Production QA ≠ browser visual | **P1** |
| **WF-AR-09** Anti card-in-card for flat-showroom targets | Companion DESIGN-AUTHORITY doc §Anti-Pattern Checklist | Checklist table; cite F-15 | **P1** |
| **WF-AR-10** Blueprint repo check — cited asset paths must exist | `generation-contracts/GENERATION-CONTRACT-v1.md` or DESIGN-AUTHORITY companion §Asset Verification | **Append** pre-charter verification row to existing contract checklist | **P0** |
| **WF-AR-11** Homepage mandatory in first-impression scope | Companion DESIGN-AUTHORITY doc §First-Impression Scope | Required screen list template; cross-ref WG-AR-08 | **P0** |
| **WF-AR-12** Conflict resolution artifact (mock vs spec) | Companion DESIGN-AUTHORITY doc §Conflict Resolution | Block implementation until written resolution | **P1** |
| **WF-AR-13** GAP response plan — alignment score + response class | Companion DESIGN-AUTHORITY doc §GAP Response | Mandatory response enum: clean-room / reversal / scope-reduction; no READY without class | **P0** |

**Website Factory integration principle:** Preserve frozen Foundation/Design Layer canon (`DESIGN-SYSTEM-RULES-v1.md`, `RUNTIME-HANDOFFS-v1.md`). Add **companion operational handoff docs** under `design-system/` rather than expanding architecture rules with CSS/theme override semantics.

---

## 3. OCPilot Integration

Rules from source §4 (`OC-AR-*`). OCPilot currently has **no** visual-acceptance or CSS-budget knowledge docs — gaps confirmed at `projects/ocpilot/knowledge/README.md` inventory.

| Rule | Target document | Integration method | Priority |
|------|-----------------|-------------------|----------|
| **OC-AR-01** Technical PASS ≠ Visual PASS — separate `AUTOMATED_PASS` and `VISUAL_ACCEPT` | **NEW** `projects/ocpilot/knowledge/OCPILOT-VISUAL-ACCEPTANCE-GATE-v1.md` | **New P0 knowledge doc** — two-field decision schema; ban single «PASS WITH NOTES» for authorization | **P0** |
| **OC-AR-02** Implements; does not invent — ambiguous charter → STOP | Same VISUAL-ACCEPTANCE-GATE doc §Implementation Boundary | Cross-ref WF blueprint ID requirement | **P0** |
| **OC-AR-03** CSS layer budget — block count + KB before write | **NEW** `projects/ocpilot/knowledge/OCPILOT-CSS-LAYER-BUDGET-v1.md` | **New P0 knowledge doc** — thresholds (>8 SITE blocks OR >200 KB → ESCALATE) | **P0** |
| **OC-AR-04** Three-strike append rule — 3 append-only CSS waves → architecture review | Same CSS-LAYER-BUDGET doc §Append Counter | Route-family tracking table in decision template | **P0** |
| **OC-AR-05** Screenshot gate — paths verified on disk | VISUAL-ACCEPTANCE-GATE doc §Evidence Requirements | Link to **NEW** `projects/ocpilot/sites/*/qa/README.md` storage policy (per-site) | **P1** |
| **OC-AR-06** No agent visual scores — operator score PENDING or Proof Pack only | VISUAL-ACCEPTANCE-GATE doc §Scoring Prohibition | Explicit ban on `agent est. 7–8/10` pattern | **P0** |
| **OC-AR-07** Partial twig deploy = FAIL | `knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md` pattern — **NEW** short rule doc or appendix | **New rule** `OCPILOT-RULE-PARTIAL-TWIG-DEPLOY-v1.md` (W2A lesson; one-screen) | **P2** |
| **OC-AR-08** HITL before next wave recommendation | VISUAL-ACCEPTANCE-GATE doc §HITL Gate | `VISUAL_ACCEPT = PENDING` → cannot recommend next wave | **P0** |
| **OC-AR-09** Preserve rollback discipline | Existing wave templates — no change to rollback pattern | **Reference only** in VISUAL-ACCEPTANCE-GATE doc; already operational | **P2** (maintain) |
| **OC-AR-10** Hybrid override forbidden without WF written decision | VISUAL-ACCEPTANCE-GATE doc §Spec Deviation | STOP + WF clarification artifact required | **P1** |
| **OC-AR-11** Composition audit citation in anatomy CR | `templates/change-request-template.md` | **Append** required field: `composition_rule_ids[]` | **P1** |
| **OC-AR-12** Cache risk annotation | Execution report convention in VISUAL-ACCEPTANCE-GATE doc §Deploy Notes | One-line reminder; not PASS substitute | **P2** |

**OCPilot state/index (secondary, P2):**

| Target | Integration method | Priority |
|--------|-------------------|----------|
| `projects/ocpilot/OCPILOT-STATE.md` | Add columns: `AUTOMATED_PASS` · `VISUAL_ACCEPT` per visual wave row | **P2** |
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Add `Visual HITL` column on run rows; split TECH DONE vs VISUAL ACCEPTED in status text | **P2** |
| **NEW** `projects/ocpilot/templates/visual-proof-pack-template.md` | Standardize W4.1 zone table; FAIL rules for homepage <6/10 | **P1** |
| **NEW** `projects/ocpilot/templates/decision-report-template.md` (or extend existing decision pattern) | Mandatory dual-verdict fields from OC-AR-01 | **P1** |

---

## 4. Web-GPT Workflow Integration

Rules from source §5 (`WG-AR-*`). Web-GPT pack lives under `web-gpt-sources/mars-v2/`; no dedicated OCPilot authorization checklist exists today.

| Rule | Target document | Integration method | Priority |
|------|-----------------|-------------------|----------|
| **WG-AR-01** No implementation after failed visual review (<7/10) | **NEW** `web-gpt-sources/mars-v2/08_MARS_v2_OCPILOT_AUTHORIZATION_CHECKLIST-v1.md` | **New checklist doc** — primary home for WG-AR-01..12 | **P0** |
| **WG-AR-02** No wave chaining with HITL pending | Same checklist §Pre-Charter Gates | Hard STOP condition; read `VISUAL_ACCEPT` not automated PASS | **P0** |
| **WG-AR-03** Escalation — 2 consecutive <7/10 → architecture review / clean-room | Same checklist §Cosmetic Loop Escalation | Cross-ref WF-AR-03/04 and OC-AR-03/04 | **P0** |
| **WG-AR-04** Design authority precedence — WF blueprint > OCPilot > agent | Same checklist §Authority Order | One authority-order table | **P0** |
| **WG-AR-05** Audit STOP latch | Same checklist §Audit STOP Latch | Honor Visual Failure Audit STOP until expectation workshop + WF re-auth | **P0** |
| **WG-AR-06** One active design authority — no parallel mandates | Same checklist §Design Authority | Supersession required before new direction prompt | **P0** |
| **WG-AR-07** GAP <50/100 → clean-room only | Same checklist §GAP Trigger | Block WF-V2-style production patches | **P0** |
| **WG-AR-08** Homepage gate in first impression | Same checklist §First-Impression Scope | Cannot claim redesign progress if homepage first screen unchanged | **P1** |
| **WG-AR-09** No WF-V{n+1} while WF-V{n} HITL open | Same checklist §Branch Freeze | Cross-ref Branch Freeze Gate | **P1** |
| **WG-AR-10** Do not ask OCPilot to be designer | Same checklist §Charter Language | Ban «hybrid» / «interpret concept» prompt language | **P0** |
| **WG-AR-11** False progress prohibition — TECH DONE ≠ VISUAL ACCEPTED | `web-gpt-sources/mars-v2/02_MARS_v2_EXECUTION_MODEL.md` | **Append** 5-line subsection + link to checklist | **P0** |
| **WG-AR-12** Operator expectation match — CSS-only FINISHING insufficient for 3→7/10 | Same checklist §Task Intake Rescope | Re-scope to composition or clean-room before impl prompt | **P1** |

**Secondary Web-GPT touchpoints (minimal cross-refs only):**

| Target | Integration method | Priority |
|--------|-------------------|----------|
| `web-gpt-sources/mars-v2/07_MARS_v2_OPERATIONAL_CHAT_DISCIPLINE.md` | Add Validation chat type note: read authorization checklist before OCPilot impl prompts | **P2** |
| `web-gpt-sources/chat-migration/08-active-projects-and-lanes.md` | Link SITE-001 anti-regression + freeze status for continuity bootstrap | **P2** |
| `web-gpt-sources/WEB-GPT-SOURCE-PACK-INDEX.md` | Index entry for new checklist doc | **P2** |

---

## 5. MARS Governance Integration

Cross-system gates from source §6 and §7. MARS governance describes **human-operated semantics** — integration must preserve «documentation aids only, not enforcement engine» posture per [validation-chain-semantics.md](validation-chain-semantics.md).

| Rule / Gate | Target document | Integration method | Priority |
|-------------|-----------------|-------------------|----------|
| **Visual Gate** (F-01) — AUTOMATED ≠ VISUAL | [validation-chain-semantics.md](validation-chain-semantics.md) | **Append** §Visual vs Automated validation kinds table (name the layer explicitly) | **P0** |
| **HITL Gate** (F-02) — PENDING = HARD STOP | [human-execution-guarantees.md](human-execution-guarantees.md) | **Append** HITL pending escalation paragraph + link to OCPilot VISUAL-ACCEPTANCE-GATE | **P0** |
| **Clean-Room Gate** (F-07) | [stabilization-vs-expansion.md](stabilization-vs-expansion.md) | **Append** clean-room trigger as expansion blocker (GAP <50/100) | **P1** |
| **Layer Debt Gate** (F-06) | [tooling-escalation-warnings.md](tooling-escalation-warnings.md) | **Append** CSS layer budget as escalation cue (not automated gate) | **P1** |
| **Architecture Gate** (F-05, F-11, F-13, F-15) | [execution-boundary-clarification.md](execution-boundary-clarification.md) | **Append** blueprint-required boundary for visual implementation lanes | **P1** |
| **Branch Freeze Gate** (F-14) | [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md) | **Append** experimental branch FREEZE before successor planning | **P1** |
| **Audit STOP Gate** (F-09) | [reality-audit-framework.md](reality-audit-framework.md) | **Append** STOP directive latch semantics — audit ≠ theater | **P0** |
| **Lessons → pattern promotion** (all F-*) | [experiment-to-pattern-transition.md](experiment-to-pattern-transition.md) | **Append** SITE-001 as worked example; link anti-regression doc | **P1** |
| **Postmortem anchor** | [operational-lessons-and-postmortems.md](operational-lessons-and-postmortems.md) | **Append** pointer to SITE-001 anti-regression as governance asset | **P1** |
| **Cross-system index** | [governance/README.md](README.md) | **Add index row** for anti-regression + this integration plan | **P2** |
| **Operational state snapshot** | [current-operational-state-v1.md](current-operational-state-v1.md) | **Append** note: SITE-001 rules adopted; WF-V2 frozen; WF-V3 blocked pending P0 | **P2** |
| **Execution phase vocabulary** | [execution-phase-model.md](execution-phase-model.md) | **Append** optional «Visual acceptance» phase distinction in Validation row | **P2** |
| **Canonical terminology** | [canonical-terminology-registry.md](canonical-terminology-registry.md) | **Add terms:** `AUTOMATED_PASS`, `VISUAL_ACCEPT`, `clean-room`, `cosmetic loop cap` | **P2** |

**Optional governance companion (if append-only limits reached):**

| **NEW** `governance/SITE-001-ANTI-REGRESSION-GATES-v1.md` | Consolidated gate definitions §6 from source | **New companion** — only if scattered appends exceed maintainability; prefer minimal appends first | **P1 (fallback)** |

---

## 6. P0 Mandatory Rules

These rules must **begin operating immediately** upon publication of their P0 target documents (human-operated; not automated enforcement). Until P0 docs exist, operators should treat [SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md](../projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md) as interim authority.

| P0 Rule | Source ID | One-line requirement | Primary enforcement surface |
|---------|-----------|---------------------|----------------------------|
| **Technical PASS ≠ Visual PASS** | F-01 · OC-AR-01 · WG-AR-11 | Decision reports carry independent `AUTOMATED_PASS` and `VISUAL_ACCEPT`; authorization reads **visual only** | OCPilot VISUAL-ACCEPTANCE-GATE · Web-GPT checklist |
| **HITL Pending = Hard Stop** | F-02 · OC-AR-08 · WG-AR-02 | `VISUAL_ACCEPT = PENDING` blocks next implementation prompt; max 1 wave PENDING without escalation | Web-GPT authorization checklist · OCPilot decision closeout |
| **Cosmetic Loop Cap** | F-03 · WF-AR-04 · WG-AR-03 | 2 consecutive target-screen scores <7/10 → STOP append-only CSS; mandatory architecture review or clean-room | Web-GPT checklist · WF wave classification |
| **CSS Layer Budget** | F-06 · OC-AR-03/04 | >8 SITE blocks OR >200 KB in `main.css` → ESCALATE; no 4th append-only wave on same route family | OCPilot CSS-LAYER-BUDGET |
| **Clean-Room Trigger** | F-07 · WF-AR-03/13 · WG-AR-07 | GAP alignment <50/100 OR 2 failed cosmetic loops → prototype-only authorization; no production TEST patches | WF DESIGN-AUTHORITY · Web-GPT checklist |
| **Visual Score Evidence Requirement** | F-08 · OC-AR-05/06 | No agent-estimated scores; scoring via Visual Proof Pack zone table or operator HITL form only; screenshot paths verified | OCPilot VISUAL-ACCEPTANCE-GATE · visual-proof-pack template |

**Supporting P0 cluster (design authority — blocks root cause):**

| Rule | Source ID | Requirement |
|------|-----------|-------------|
| One active design authority | F-05 · WF-AR-01/06 · WG-AR-06 | Supersession doc before new concept; no parallel mandates |
| Blueprint repo check | F-11 · WF-AR-10 | Cited PNG/spec paths verified before charter |
| Audit STOP latch | F-09 · WG-AR-05 | Visual Failure Audit STOP honored until workshop + WF re-auth |

---

## 7. Recommended Update Order

Rationale: SITE-001 failure propagated **downstream** (OCPilot false PASS) because **upstream authorization** (Web-GPT) and **design authority** (Website Factory) lacked hard gates. Fix order prioritizes **stop-the-bleeding** at execution, then **upstream authority**, then **authorization chain**, then **canonical governance index**.

```
Phase 1 — OCPilot execution gates (P0)          ← stops false PASS at decision layer
Phase 2 — Website Factory design authority (P0) ← fixes competing concepts / ghost assets
Phase 3 — Web-GPT authorization checklist (P0)  ← blocks wave chaining with HITL pending
Phase 4 — MARS governance cross-refs (P0–P1)    ← canonical semantics + audit STOP latch
Phase 5 — Templates & state surfaces (P1–P2)    ← visual-proof-pack, OPERATIONAL-INDEX columns
Phase 6 — Site-specific artifacts (P1, SITE-001) ← WF-V2 FREEZE doc, WF-V3 plan, qa/README (planning only)
```

### Phase 1 — OCPilot (immediate)

1. Create `projects/ocpilot/knowledge/OCPILOT-VISUAL-ACCEPTANCE-GATE-v1.md`
2. Create `projects/ocpilot/knowledge/OCPILOT-CSS-LAYER-BUDGET-v1.md`
3. Update `projects/ocpilot/knowledge/README.md` index

**Exit criterion:** OCPilot decision/execution prompts can cite two P0 knowledge docs.

### Phase 2 — Website Factory (immediate after Phase 1)

1. Create `workspaces/website-factory-reference-v1/design-system/WEBSITE-FACTORY-DESIGN-AUTHORITY-v1.md`
2. Minimal footnote cross-ref in `DESIGN-SYSTEM-RULES-v1.md` (1 paragraph, no rule rewrite)
3. Append blocked conditions to `RUNTIME-HANDOFFS-v1.md` HO-07 (composition audit, asset check)

**Exit criterion:** New OCPilot charter can cite WF blueprint ID + verified repo path.

### Phase 3 — Web-GPT Workflow

1. Create `web-gpt-sources/mars-v2/08_MARS_v2_OCPILOT_AUTHORIZATION_CHECKLIST-v1.md` (WG-AR-01..12)
2. Append subsection to `02_MARS_v2_EXECUTION_MODEL.md` (TECH DONE vs VISUAL ACCEPTED)
3. Index in `WEB-GPT-SOURCE-PACK-INDEX.md`

**Exit criterion:** Web-GPT pre-charter prompt includes checklist; HITL PENDING → do not authorize.

### Phase 4 — MARS Governance

1. Append to `validation-chain-semantics.md`, `human-execution-guarantees.md`, `reality-audit-framework.md`
2. Append to `experiment-to-pattern-transition.md`, `operational-lessons-and-postmortems.md`
3. Index in `governance/README.md`

**Exit criterion:** Cross-system vocabulary aligned; no claim of automated enforcement added.

### Phase 5 — Templates & state (P1–P2)

- `visual-proof-pack-template.md`, decision report dual-verdict fields
- `OCPILOT-STATE.md` / `OPERATIONAL-INDEX.md` column split
- `WF-VISUAL-WAVE-CLASSIFICATION-v1.md` companion

### Phase 6 — SITE-001 site artifacts (planning only; not impl)

Per source §8 — **not** part of system rule integration but **blocks WF-V3**:

- `SITE-001-WF-V2-FREEZE-DECISION-v1.md` (formalize effective freeze)
- `SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` (planning doc)
- `design/wf-v2-concept/` assets or storage manifest
- `projects/ocpilot/sites/site-001/qa/README.md` screenshot policy

---

## 8. Final Decision

### Can WF-V3 start now?

```text
NO
```

### Blockers (must clear before WF-V3 prototype charter)

| # | Blocker | Status | Resolving action |
|---|---------|--------|------------------|
| 1 | **P0 OCPilot knowledge docs not published** | **OPEN** | Phase 1 — VISUAL-ACCEPTANCE-GATE + CSS-LAYER-BUDGET |
| 2 | **P0 Website Factory design authority doc not published** | **OPEN** | Phase 2 — DESIGN-AUTHORITY companion |
| 3 | **P0 Web-GPT authorization checklist not published** | **OPEN** | Phase 3 — OCPILOT_AUTHORIZATION_CHECKLIST |
| 4 | **WF-V2 not formally frozen** (behavior effective per anti-regression §8A; artifact missing) | **PARTIAL** | Write `SITE-001-WF-V2-FREEZE-DECISION-v1.md` (P1) |
| 5 | **WF-V3 clean-room plan missing in repo** | **OPEN** | Write `SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` (planning only) |
| 6 | **Design assets ghost paths** — `design/wf-v2-concept/` not found at audit | **OPEN** | Check in PNGs or `C:\AI MARS STORAGE` manifest |
| 7 | **Operator visual review session not held** | **OPEN** | All HITL scores **SAFE UNKNOWN — PENDING** |
| 8 | **QA screenshot trail broken** — paths in reports, files not in repo | **OPEN** | `qa/README.md` + storage policy before evidence claims |

### Interim authority (effective now, human-operated)

Until P0 docs are published, [SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md](../projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md) §8 declares:

- **WF-V2 freeze behavior effective** — no new WF-V2-W* waves on TEST
- **Anti-regression rules mandatory** for future SITE-001 work and recommended default for all OCPilot visual sites
- **WF-V3 not authorized** by that document

---

## Appendix A — Documents candidate for update (consolidated)

### NEW documents (recommended create)

| Path | Phase |
|------|-------|
| `projects/ocpilot/knowledge/OCPILOT-VISUAL-ACCEPTANCE-GATE-v1.md` | 1 |
| `projects/ocpilot/knowledge/OCPILOT-CSS-LAYER-BUDGET-v1.md` | 1 |
| `workspaces/website-factory-reference-v1/design-system/WEBSITE-FACTORY-DESIGN-AUTHORITY-v1.md` | 2 |
| `web-gpt-sources/mars-v2/08_MARS_v2_OCPILOT_AUTHORIZATION_CHECKLIST-v1.md` | 3 |
| `projects/ocpilot/templates/visual-proof-pack-template.md` | 5 |
| `workspaces/website-factory-reference-v1/design-system/WF-VISUAL-WAVE-CLASSIFICATION-v1.md` | 5 |
| `governance/SITE-001-ANTI-REGRESSION-GATES-v1.md` | 4 (fallback) |

### Existing documents (minimal append / cross-ref only)

| Path | Phase |
|------|-------|
| `workspaces/website-factory-reference-v1/design-system/DESIGN-SYSTEM-RULES-v1.md` | 2 |
| `workspaces/website-factory-reference-v1/runtime-architecture/RUNTIME-HANDOFFS-v1.md` | 2 |
| `workspaces/website-factory-reference-v1/production-qa/PRODUCTION-QA-SYSTEM-v1.md` | 5 |
| `web-gpt-sources/mars-v2/02_MARS_v2_EXECUTION_MODEL.md` | 3 |
| `governance/validation-chain-semantics.md` | 4 |
| `governance/human-execution-guarantees.md` | 4 |
| `governance/reality-audit-framework.md` | 4 |
| `governance/experiment-to-pattern-transition.md` | 4 |
| `governance/operational-lessons-and-postmortems.md` | 4 |
| `projects/ocpilot/OCPILOT-STATE.md` | 5 |
| `projects/ocpilot/OPERATIONAL-INDEX.md` | 5 |
| `projects/ocpilot/templates/change-request-template.md` | 5 |
| `projects/ocpilot/knowledge/README.md` | 1 |
| `governance/README.md` | 4 |
| `web-gpt-sources/WEB-GPT-SOURCE-PACK-INDEX.md` | 3 |

### SITE-001 site artifacts (planning; not system rules)

| Path | Notes |
|------|-------|
| `projects/ocpilot/sites/site-001/reports/SITE-001-WF-V2-FREEZE-DECISION-v1.md` | Formalize freeze |
| `projects/ocpilot/sites/site-001/reports/SITE-001-WF-V3-CLEAN-ROOM-PLAN-v1.md` | WF-V3 prerequisite |
| `projects/ocpilot/sites/site-001/qa/README.md` | Screenshot storage policy |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/` | Asset check-in or manifest |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| WF-V3 planning report in repo | **MISSING** — Restore Registry intent only |
| Operator actual HITL scores | **SAFE UNKNOWN** — all pending |
| WF-V2-W4 on live TEST | **LIKELY YES** — out of registry alias scope |
| Automated enforcement of these gates | **NOT PLANNED** — human-operated per MARS governance posture |

**SECURITY RISK:** None identified (planning documentation only).

---

*SITE-001 Lessons Integration Plan v1 — governance plan only; no target file modifications; no commit implied.*

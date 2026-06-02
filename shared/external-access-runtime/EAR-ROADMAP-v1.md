# EAR Roadmap v1

Phased evolution for External Access Runtime. **No dates. No delivery promises.** Each phase requires **explicit human charter** before implementation work.

---

## Phase 1 — Architecture (current)

**Deliverables:**

- `shared/external-access-runtime/` foundation docs
- Snapshot contract, modes, security model, connection catalog
- OCPilot freeze `site-001-pre-runtime-bridge`
- OPERATIONAL-INDEX cross-links

**Exit criteria (documentation):**

- Layer model accepted for consumer handoff
- Mode 2 named as v1 target; Mode 3 forbidden in v1

**Not in Phase 1:** code, connectors, CI.

---

## Phase 2 — Read-only OpenCart acquisition

**Intent:**

- First **Mode 2** connectors or runbooks for ocStore/OpenCart file tree + version files
- OCPilot SITE-001 as reference pilot
- Snapshot packages land in OCPilot external `snapshots/`

**Possible outputs (charter TBD):**

- SFTP/SSH read-only helper **or** hardened Mode 1 runbook
- Manifest generator aligned with `ocstore-3038-rs2` diff needs

**SAFE UNKNOWN:**

- Single connector vs operator-runbook-only
- Beget-specific procedures

**Not promised:** full admin UI automation.

---

## Phase 3 — Read-only WordPress acquisition

**Intent:**

- WPilot consumer alignment
- Reuse snapshot contract sections where possible
- WordPress-specific `extension-inventory`

**Dependency:** Phase 2 lessons on manifest and external bulk layout.

**Not in scope:** merging WPilot repo in this phase by default.

---

## Phase 4 — Unified snapshot contract

**Intent:**

- Harmonize OpenCart + WordPress snapshot fields
- Optional package validator (human-run CLI) — **still not autonomous enforcement**
- Versioning policy for `ear-snapshot-v2` if needed

**Questions to resolve:**

- Shared `extension-inventory` schema vs per-platform extensions
- Minimum `database-metadata` for all consumers

---

## Phase 5 — Future write-mode evaluation

**Intent:**

- Decide if Mode 3 ever belongs in EAR vs consumer-only change runs
- Rollback and risk-class requirements mandatory
- **No default write connector**

**Explicit:** Evaluation only — not approval of write automation.

---

## Dependency graph (conceptual)

```
Phase 1 (docs)
    ↓
Phase 2 (OpenCart read-only) ──→ OCPilot Run 5 resume
    ↓
Phase 3 (WordPress read-only)
    ↓
Phase 4 (unified contract)
    ↓
Phase 5 (write evaluation — may result in permanent ban)
```

---

## Out of roadmap (unless new charter)

- Governance tree expansion
- MARS multi-agent runtime
- Website Factory production automation
- Autonomous scheduled sync

---

## Success signals (human-reviewed, not automated)

| Signal | Meaning |
|--------|---------|
| First SITE-001 snapshot with populated `file-manifest` | Phase 2 operational |
| OCPilot Run 5 Phase 3 diff without manual WinSCP | Acquisition friction reduced |
| WPilot pilot uses same contract | Phase 3–4 progress |

---

## SAFE UNKNOWN

- Whether EAR helpers live in `shared/`, `tools/`, or external repo — decision deferred.
- Funding or staffing — not documented.

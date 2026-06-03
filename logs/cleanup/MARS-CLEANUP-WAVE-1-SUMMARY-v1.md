# MARS Cleanup Wave 1 Summary v1

**Date:** 2026-06-03  
**Lane:** B  
**Charter:** MARS Cleanup Wave 1 — recommendations only  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb` / `mars-v2-stable-baseline-2026-06`; evidence `c2876cf`)  
**Rule:** No cleanup executed · no archive · no delete · no reclassify on disk

---

## Scope completed

| Task | Deliverable | Status |
|------|-------------|--------|
| Task 1 — ISBD classification | [reclassifications/isbd-classification-review-v1.md](reclassifications/isbd-classification-review-v1.md) | ✓ |
| Task 2 — Lifecycle log | [discoveries/lifecycle-log-review-v1.md](discoveries/lifecycle-log-review-v1.md) | ✓ |
| Task 3 — HomeGateway classification | [reclassifications/homegateway-classification-review-v1.md](reclassifications/homegateway-classification-review-v1.md) | ✓ |
| Task 4 — Triumph version map | [discoveries/triumph-version-map-v1.md](discoveries/triumph-version-map-v1.md) | ✓ |
| Task 5 — Action registry | [actions/cleanup-wave-1-action-registry-v1.md](actions/cleanup-wave-1-action-registry-v1.md) | ✓ |
| Task 6 — Summary | This file | ✓ |

---

## Key findings

### ISBD

- **Not** a Program, System, or Initiative.
- **Is** a **Website Factory execution case** + **client delivery workspace** (`workspaces/isbd-care-landing/`).
- **Unregistered** in `registry/project-registry.md`; Factory docs and canvas still show SAFE UNKNOWN / zero references.
- Active Gulp landing with frozen content; WP integration target; nested `.git` confirmed.
- **Recommend:** RECLASSIFY + REGISTER as Factory execution case (prefer over new `project_id`).

### Lifecycle log

- **Category C:** Active governance SoT — **not** dead, **not** abandoned.
- 16 events; last `evt-2026-0016` (2026-05-19); backlog **0017–0021** recommended but not appended.
- Registry updates (metabot, triumph, orca, wpilot, homegateway) ahead of log.
- **Recommend:** KEEP mechanism; INVESTIGATE → Wave 2 human-gated backfill.

### HomeGateway

- Registry: **`planned`** — correct product band.
- Narrative **OPERATIONAL documentation** ≠ operational product — semantic conflict.
- Doc pack: DRAFT · PLANNING · Phase 2; large Lane B visual docs.
- Workspace: **UI prototype MVP v1** skeleton (`workspaces/homegateway-v4-ai/v1/`) — do **not** inflate to shippable MVP.
- **Recommend:** RECLASSIFY prose bands; KEEP `planned` status.

### Triumph

- **Six** workspace folders: base (v1), v2, v3, v4, v5, v6.
- **Canonical:** **`triumph-manipulator-landing-v6`** — production candidate, 12 PPC routes, multi-source authority.
- **Archive candidates:** v1–v5 (older generations); v5 keep short-term until ORCA calibration retargets from v5 → v6.
- **Drift:** ORCA calibration OPERATIONAL-INDEX still cites v5.

---

## Recommended reclassifications (consolidated)

| Entity | From (observed) | To (recommended) |
|--------|-----------------|------------------|
| ISBD | Unregistered / SAFE UNKNOWN | Factory **execution case** + client delivery workspace |
| ISBD canvas | "No execution case" | Linked case node (after operator registration choice) |
| HomeGateway OPERATIONAL prose | Ambiguous "OPERATIONAL" | **PLANNED · OPERATIONAL DOC PACK** (explicit) |
| HomeGateway workspace | Undocumented in index | **UI Prototype (static MVP skeleton)** |
| Triumph ORCA calibration paths | v5 workspace | v6 canonical workspace |
| Lifecycle log role | (implicit) | Distinct from `logs/cleanup/` and `logs/releases/` |

---

## Archive candidates (identification only — not executed)

| Cluster | Paths |
|---------|-------|
| Triumph generations | `workspaces/triumph-manipulator-landing` (v1), `-v2`, `-v3`, `-v4`, `-v5` |
| Legacy SEO pack | `projects/seo-content-agent/` |
| Migration snapshot | `web-gpt-sources/chat-migration/` |
| MIG pre-pilot | `projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/` |
| ORCA stable snapshot | `projects/orca/archive/stable-orca-after-triumph-battle-v1/` |
| Ops hygiene | `workspaces/_tmp/`, old `_snapshots/` |

Full IDs: census [archive-candidates/2026-06-03-census-archive-candidates-v1.md](archive-candidates/2026-06-03-census-archive-candidates-v1.md) + Triumph map TM-AC-*.

---

## Evidence created (this wave)

| File | Purpose |
|------|---------|
| `logs/cleanup/reclassifications/isbd-classification-review-v1.md` | ISBD audit + recommendation |
| `logs/cleanup/discoveries/lifecycle-log-review-v1.md` | Lifecycle log intent/usage/determination |
| `logs/cleanup/reclassifications/homegateway-classification-review-v1.md` | HomeGateway maturity audit |
| `logs/cleanup/discoveries/triumph-version-map-v1.md` | Triumph lineage + canonical v6 |
| `logs/cleanup/actions/cleanup-wave-1-action-registry-v1.md` | Wave 1 action assignments |
| `logs/cleanup/MARS-CLEANUP-WAVE-1-SUMMARY-v1.md` | This summary |

---

## Actions executed

**None.**

- No registry edits  
- No archival moves  
- No deletions  
- No canvas updates  
- No lifecycle append  

---

## Risks if recommendations ignored

1. **ISBD silent delivery** — largest unregistered client workspace; wrong lane assumptions.
2. **Lifecycle drift** — registry changes without audit trail weaken governance claims.
3. **HomeGateway maturity inflation** — misreading doc activity as shipped product.
4. **Triumph version sprawl** — agents edit wrong workspace without v6 authority map.
5. **Nested ISBD git** — backup/survivability scope ambiguity.

---

## SAFE UNKNOWN

| Topic | Verification needed |
|-------|----------------------|
| ISBD operator owner / client contract | External |
| ISBD / Triumph production URLs | Hosting |
| MetaBOT live n8n vs repo exports | External n8n |
| HomeGateway v1 workspace canonical intent | Operator |
| Exact git tags for Triumph v5/v6 | Full tag audit |

---

## Next steps (by approval tier)

### 1. Immediately executable (low risk, doc-only)

- Append errata note to structural coherence audit (WPilot row stale) — **RECLASSIFY** W1-034  
- Update `logs/cleanup/README.md` canonical investigations table with Wave 1 links  
- Operator read Wave 1 evidence before any Wave 2 charter  

### 2. Requires operator approval

- ISBD registration path (Factory execution case vs `project_id`) — W1-004, W1-005, W1-006  
- Lifecycle backfill evt 0017–0021 — W1-002  
- HomeGateway registry prose disambiguation — W1-008  
- ORCA calibration index v5 → v6 path update — W1-015  
- Triumph version authority one-pager in project pack — W1-016  

### 3. Wait for Wave 2

- Any **ARCHIVE CANDIDATE** filesystem moves (Triumph v1–v5, legacy packs, snapshots)  
- ISBD nested `.git` policy resolution  
- Integration registry population  
- Factory block registry alignment merge  
- Incoming intake promotion/quarantine SOP  

---

*MARS Cleanup Wave 1 — complete. Stop per charter.*

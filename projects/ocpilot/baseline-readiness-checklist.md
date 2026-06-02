# OCPilot — Baseline Readiness Checklist

**Purpose:** answer **«Can this baseline be used for comparison?»** before any project site audit proceeds.

**Rule:** If required items fail → OCPilot **must request operator upload**. **Do not silently continue.**

---

## Baseline under review

| Field | Value |
|-------|-------|
| Baseline path | e.g. `baselines/ocstore-3038-rs2/` (priority) or `baselines/ocstore-3039-rs1/` |
| Passport ID | |
| Review date | |
| Reviewer (operator / agent) | |

---

## Required (all must pass)

| # | Check | Pass | Fail action |
|---|-------|------|-------------|
| 1 | **[ ] Passport exists** — completed copy in `passports/` using [versioned-baseline-passport-template.md](templates/versioned-baseline-passport-template.md) | ☐ | Request operator create passport |
| 2 | **[ ] Files exist** — `files/` contains sanitized vendor tree (not only `.gitkeep`) | ☐ | Request operator upload clean file baseline |
| 3 | **[ ] Manifest exists** — `manifest/` contains path list, directory map, or checksum manifest | ☐ | Request operator provide or generate manifest |

### Required gate result

| Result | Meaning |
|--------|---------|
| **All 3 pass** | Baseline may be used for file-level comparison (Layers 1–4 per [baseline-comparison-methodology.md](baseline-comparison-methodology.md)) |
| **Any fail** | **NOT READY** — stop comparison; record SAFE UNKNOWN in site `safe-unknown/` if audit already started |

---

## Optional (recommended, not blocking)

| # | Check | Pass | Notes |
|---|-------|------|-------|
| 4 | **[ ] DB metadata** — `database/` has schema metadata or table descriptions | ☐ | Without this, DB layer comparison = SAFE UNKNOWN |
| 5 | **[ ] Comparison notes** — `comparison-notes/` documents known ocStore/upstream deltas | ☐ | Strongly recommended for ocStore baselines |

Optional failures do **not** block **file-only** comparison if all required items pass — but DB-related claims must be marked **SAFE UNKNOWN** until metadata exists.

---

## Quick verification procedure

1. Open `baselines/<version-folder>/passports/` — passport file present and filled?
2. List `baselines/<version-folder>/files/` — more than placeholder content?
3. List `baselines/<version-folder>/manifest/` — manifest present?
4. (Optional) Review `database/` and `comparison-notes/`.
5. Cross-check passport **Readiness flags** match physical folder state.

---

## Failure responses (mandatory behavior)

| Failure | OCPilot action |
|---------|----------------|
| No passport | Emit SAFE UNKNOWN; request passport creation before comparison |
| No files | Emit SAFE UNKNOWN; request sanitized vendor upload (Run 3) |
| No manifest | Emit SAFE UNKNOWN; request manifest — comparison scope limited until provided |
| Passport says «yes» but folder empty | Treat as **fail** — passport must be corrected |
| Wrong version folder for target site | Stop; select correct baseline; do not diff against wrong version |

**Forbidden:** assuming empty baseline is «close enough» or skipping checklist because audit is urgent.

---

## Readiness summary template

Copy into site report or baseline `notes/` when baseline selected:

```
Baseline readiness: READY / NOT READY
Path: baselines/<folder>/
Passport: yes/no
Files: yes/no
Manifest: yes/no
DB metadata: yes/no (optional)
Comparison notes: yes/no (optional)
Blockers: ...
```

---

## Relation to runs

| Run | Role |
|-----|------|
| Run 2 | Checklist and folder contract defined — baselines may still be placeholders |
| Run 2.6 | Priority target folders `ocstore-3038-rs2`, `ocstore-3039-rs1` — placeholders valid until Run 3 |
| Run 3 | First Baseline Acquisition for priority targets — expected to satisfy required checks |

### Priority first baselines

1. `baselines/ocstore-3038-rs2/` — ocStore 3.0.3.8 (rs.2)
2. `baselines/ocstore-3039-rs1/` — ocStore 3.0.3.9 (rs.1)

**ocstore-3037** is older reference only; use priority baselines when auditing current operator target sites.
| Run 4+ | Project workflows must verify readiness before audit |

See [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).

---

## Related documents

- [baseline-storage-model.md](baseline-storage-model.md)
- [baseline-comparison-methodology.md](baseline-comparison-methodology.md)
- [project-sites-workflow.md](project-sites-workflow.md) — Baseline Selection section
- [baselines/README.md](baselines/README.md)

---

## SAFE UNKNOWN

- Automated readiness scanner — **not** claimed in Run 2; human-operated checklist only.

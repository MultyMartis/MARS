# Git Checkpoint v1 — PPC Exporter Production Baseline

**Label:** `orca-ppc-exporter-production-baseline-v1`  
**Date:** 2026-05-29  
**Lane:** B — ORCA PPC Production Baseline Freeze  
**Type:** Human-operated documentation checkpoint — **not** automated backup

---

## Commit

| Field | Value |
|-------|-------|
| **Message** | `ORCA PPC exporter production baseline v1` |
| **Hash (short)** | `7d57f31` |
| **Full hash** | `7d57f3157d2c28c7b9543b6a141db291c62722d2` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Parent** | `c337e27` — stabilize triumph v6 production candidate polish |
| **Push** | **NOT performed** (per task charter) |

---

## Files included

| Path | Action |
|------|--------|
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/README.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/PPC-EXPORTER-PRODUCTION-BASELINE-v1.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/COMMANDER-CALIBRATION-FINDINGS-v1.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md` | added |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/EXPORTER-V1.2-APPROVAL-v1.md` | added |
| `projects/orca/OPERATIONAL-INDEX.md` | modified — PPC exporter baseline section |
| `projects/orca/ppc/triumph-manipulator/OPERATIONAL-INDEX.md` | modified — production baseline row |
| `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/README.md` | modified — template v1 SoT |
| `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` | added — Commander transport SoT |
| `projects/orca/ppc/triumph-manipulator/exporter/commander-template-contract-v1.md` | modified — v1 revision |

**Note:** `GIT-CHECKPOINT-v1.md` is part of this commit (14 files). Verify: `git log -1 --oneline -- projects/orca/freeze/ppc-exporter-production-baseline-v1/`

---

## Files excluded (intentional)

| Category | Examples | Reason |
|----------|----------|--------|
| PPC JSON instance content | `schema/instances/triumph-s-tier-draft-v1.json` | No ad/keyword/URL/structure changes per charter |
| Generated XLSX | `tools/exporter-cli/output/*.xlsx` | Gitignored transport snapshots |
| Unrelated workspace changes | `governance/*`, `homegateway-v4-ai/*`, `mars-survivability/*`, etc. | Out of scope for this baseline |
| Git push | remote | Explicitly forbidden |
| Campaign launch | Direct UI | Human-only; not executed |

---

## Safety checks (pre-commit)

| Check | Result |
|-------|--------|
| No ad copy changes | **PASS** — documentation only |
| No keyword changes | **PASS** |
| No URL changes | **PASS** |
| No campaign structure changes | **PASS** |
| No push | **PASS** — not executed |
| Template v1 xlsx present in repo | **PASS** — committed as transport SoT |
| Exporter v1.2 approval documented | **PASS** — references existing CLI, no code change in this commit |

---

## Recovery

```bash
git checkout 7d57f31 -- projects/orca/freeze/ppc-exporter-production-baseline-v1/
git checkout 7d57f31 -- projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx
```

Or restore full commit: `git show 7d57f31`

---

## Related checkpoints

| Label | Commit (reference) |
|-------|-------------------|
| `orca-route-family-freeze-v1` | prior semantic freeze |
| `orca-commander-url-sync-preflight-v1` | `f235bf1` |
| `orca-commander-import-checklist-v1.2` | transport fix freeze |

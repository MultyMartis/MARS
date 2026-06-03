# Knowledge Center Drift Report v1

**Date:** 2026-06-03  
**Lane:** B — Cleanup Program closeout  
**Rule:** **Report only** — **no** KC filesystem changes, **no** STORAGE modifications, **no** execution

**KC path (operator vault):** `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER`  
**Git canvas source:** `docs/visualization/obsidian-canvas/`  
**Audit basis:** [MARS-POST-CLEANUP-AUDIT-v1.md](MARS-POST-CLEANUP-AUDIT-v1.md) § Knowledge Center drift; live repo post Wave 2B

---

## Executive summary

| Finding | Severity |
|---------|----------|
| KC **model** (out-of-git Visual Brain) | **No contradiction** with live repo |
| KC **content** vs post-cleanup governance | **Likely stale** on operator disk — manual refresh recommended |
| Git canvas pack vs KC mirrors | **Expected drift** (no auto-sync — census D-008) |
| Web-GPT baseline pack vs live SoT | **Stale** until operator uploads refreshed pack (separate from KC) |

---

## Recommended KC updates (operator manual)

### 01 ECOSYSTEM / program cards

| # | Recommended update | Reason | Priority |
|---|---------------------|--------|----------|
| KC-01 | Refresh **GitGuard** card/section: REGISTERED Repository Survivability Layer; link `mars-survivability` not fictional `projects/gitguard/` | Wave 2B registration | **High** |
| KC-02 | Add or refresh **IdeaBox** note: optional Incubation Layer; `continuity/` path; not mandatory entry | Wave 2B ideabox alignment | **Medium** |
| KC-03 | Refresh **Incoming** policy summary: hybrid Active Incoming + Historical Bulk; link repo `incoming/README.md` | Wave 2A/2B | **High** |
| KC-04 | Refresh **Lifecycle** card: Key Event History vs Tracking Mode; distinction from cleanup/releases logs | Wave 2B lifecycle alignment | **Medium** |
| KC-05 | Update **ISBD** under execution cases: Factory case `isbd-care-landing`; not standalone program | Wave 1A | **High** |
| KC-06 | Update **HomeGateway** card: `planned` + doc-pack vs UI prototype workspace layers | Wave 1A | **Medium** |
| KC-07 | Update **Triumph** navigation: canonical workspace **v6**; authority map pointer | Wave 1A | **High** |

### 03 EXECUTION CASES

| # | Recommended update | Reason | Priority |
|---|---------------------|--------|----------|
| KC-08 | Ensure ISBD execution case appears with link to `workspaces/isbd-care-landing/` | Traceability closeout | **High** |
| KC-09 | Triumph reference case points to v6 workspace not v5-only narrative | ORCA/Factory alignment | **Medium** |

### 04 GOVERNANCE pointers

| # | Recommended update | Reason | Priority |
|---|---------------------|--------|----------|
| KC-10 | Point to live `governance/canonical-terminology-registry.md` for GitGuard/IdeaBox/Incoming terms | Wave 2B terminology | **Medium** |
| KC-11 | Add footnote: `mars-v2-structural-coherence-audit-v0.md` may be stale (WPilot row, lifecycle evt count) — prefer registry + lifecycle log | Audit C-F03 / M-03 | **Low** |

### 05 INFRASTRUCTURE

| # | Recommended update | Reason | Priority |
|---|---------------------|--------|----------|
| KC-12 | Confirm Active Brain / Storage / Incoming hybrid diagram matches `governance/mars-infrastructure-reality-v1.md` | Consistency | **Low** |

### Canvas mirrors (`00 START HERE/canvas/` or equivalent)

| # | Recommended update | Reason | Priority |
|---|---------------------|--------|----------|
| KC-13 | Re-copy or regenerate canvas from git pack after verifying `_generate_pack.py` output (lifecycle node OPERATIONAL — Wave 2A) | Canvas factual fix | **Medium** |
| KC-14 | Verify `master.canvas` / `programs.canvas` reflect REGISTERED GitGuard and Incoming § | Topology alignment | **Medium** |

### 06 ARCHIVE / 99 EXPORTS

| # | Recommended update | Reason | Priority |
|---|---------------------|--------|----------|
| KC-15 | **Do not** archive cleanup evidence to KC as SoT — link to `logs/cleanup/` in repo only | Charter separation | **Low** (discipline) |

---

## Explicit non-actions

| Action | Status |
|--------|--------|
| Modify `C:\AI MARS STORAGE\...` from agent | **Not performed** |
| Auto-sync KC ↔ git | **Not available** — operator choice |
| Create new KC root or restructure | **Out of scope** |
| Upload KC bulk to Web-GPT | **Not recommended** per baseline pack policy |

---

## Verification checklist (operator)

When refreshing KC, confirm:

- [ ] GitGuard described as REGISTERED cross-cutting under mars-survivability
- [ ] IdeaBox optional incubation — not required path to programs
- [ ] Incoming hybrid model matches `incoming/README.md`
- [ ] ISBD listed as Factory execution case
- [ ] Triumph v6 marked canonical in navigation
- [ ] Lifecycle log role distinct from cleanup program folder
- [ ] Canvas mirrors regenerated from git if git pack was updated

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Which KC sections exist on operator machine | Requires operator listing |
| Last KC sync date vs latest git commit | No telemetry |
| Obsidian plugin versions | Session-level |

---

*Knowledge Center Drift Report v1 — recommendations only — 2026-06-03.*

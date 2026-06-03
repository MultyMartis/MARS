# REPORT — MARS Web-GPT Source Pack Update v1

**Lane:** B  
**Chat type:** Web-GPT Source Pack Update  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb`, evidence `c2876cf`)  
**Date:** 2026-06-03  
**Git:** No commit, no push (per task charter)

---

## Existing source audit

### Active source files (still in-repo, role)

| Location | Files | Role today |
|----------|-------|------------|
| `mars-v2-stable-baseline-2026-06/` | 11 (10 topics + README) | **NEW canonical Web-GPT upload pack** |
| `WEB-GPT-SOURCE-PACK-INDEX.md` | 1 | Human upload order |
| `WEB-GPT-CHAT-SYNC-PACK.md` | 1 | Program chat sync blocks |
| `mars-v2-final/` | 10 | In baseline commit `45518bb`; **superseded for upload** by stable-baseline pack |
| `mars-v2/` | 9 | Parallel pack; missing `08_OPERATIONAL_EVOLUTION` — **duplicate, do not upload** |
| `chat-migration/` | 11 | Paste-only continuity; operational-first superseded |
| Root numbered | 14 (`01_system.md` … `14_roadmap.md`) | Legacy Web-GPT import; historical design input |
| `04_agents.md`, `04-workflows__git-rules.md` | 2 | Legacy topic fragments |

### Obsolete / historical (do not upload as SoT)

- `01_system.md` through `14_roadmap.md` — pre–mars-v2 import; paths like `02-core/` may not match live layout (`13_migration.md` warns).  
- `chat-migration/` — superseded for standing sources by mars-v2 packs; useful one-time paste only.  
- `mars-v2/` — redundant with `mars-v2-final/`; lacks post–Cycle 8 evolution file present in final.  
- `projects/seo-content-agent/` — legacy; MetaBOT canonical id is `metabot-seo-content-agent`.

### Duplicated source files

| Pair | Relationship |
|------|--------------|
| `mars-v2/*` vs `mars-v2-final/*` | Nine same-named topic files; `mars-v2-final` adds `08_MARS_v2_OPERATIONAL_EVOLUTION_STATE.md` and updated README load order |
| `mars-v2-final/08_*` vs new `02_OPERATIONAL_POSTURE.md` + `07_STABLE_BASELINE_*` | Evolution state absorbed into posture + baseline publication topics |
| `chat-migration/01`–`10` vs mars-v2 topics | Overlapping honesty/bootstrap content — different format, same era |

### Superseded by Stable Baseline (upload policy)

| Superseded pack | Replacement |
|-----------------|-------------|
| `mars-v2-final/` (upload set) | `mars-v2-stable-baseline-2026-06/` |
| `mars-v2/` | Same replacement — retire from Web-GPT project |
| `chat-migration/` as SoT | Minimum bundle + `WEB-GPT-CHAT-SYNC-PACK.md` |
| Numbered root topics | Governance + stable-baseline pack only |

### Migration notes (operator)

1. Remove old Web-GPT project files from `mars-v2-final/`, `mars-v2/`, and numbered `0*.md` if previously uploaded.  
2. Upload per `WEB-GPT-SOURCE-PACK-INDEX.md` (11 steps).  
3. Keep in-repo copies of `mars-v2-final/` for git/history at checkpoint — no deletion required in this task.  
4. Do not upload vendor, `dist/`, `mars-runtime/**/*.js`, OCPilot baseline `files/**` bulk.  
5. KC and Cold Brain: reference docs only — bulk stays on `C:\AI MARS STORAGE`.

---

## New source package

**Folder:** `web-gpt-sources/mars-v2-stable-baseline-2026-06/`

Distilled canonical topics aligned to published baseline:

| # | File | Topic |
|---|------|-------|
| 01 | `01_MARS_IDENTITY.md` | Current MARS identity |
| 02 | `02_OPERATIONAL_POSTURE.md` | Current operational posture |
| 03 | `03_PROGRAM_REGISTRY_SUMMARY.md` | Program registry summary |
| 04 | `04_INFRASTRUCTURE_REALITY.md` | Infrastructure reality |
| 05 | `05_ACTIVE_VISUAL_COLD_BRAIN.md` | Active / Visual / Cold Brain |
| 06 | `06_KNOWLEDGE_CENTER.md` | Knowledge Center |
| 07 | `07_STABLE_BASELINE_PUBLICATION.md` | Stable Baseline publication |
| 08 | `08_SYSTEM_MATURITY_MAP.md` | System maturity map |
| 09 | `09_OPERATIONAL_PRIORITIES.md` | Operational priorities |
| 10 | `10_RUNTIME_BOUNDARY_RULES.md` | Runtime boundary rules |
| — | `README.md` | Pack index, migration, load order |

**Authority:** Repo governance and `logs/releases/mars-v2-stable-baseline-2026-06.md` — pack is distillate, not replacement for `governance/**`.

---

## Files created

| Path |
|------|
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/README.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/01_MARS_IDENTITY.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/02_OPERATIONAL_POSTURE.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/03_PROGRAM_REGISTRY_SUMMARY.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/04_INFRASTRUCTURE_REALITY.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/05_ACTIVE_VISUAL_COLD_BRAIN.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/06_KNOWLEDGE_CENTER.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/07_STABLE_BASELINE_PUBLICATION.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/08_SYSTEM_MATURITY_MAP.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/09_OPERATIONAL_PRIORITIES.md` |
| `web-gpt-sources/mars-v2-stable-baseline-2026-06/10_RUNTIME_BOUNDARY_RULES.md` |
| `web-gpt-sources/WEB-GPT-SOURCE-PACK-INDEX.md` |
| `web-gpt-sources/WEB-GPT-CHAT-SYNC-PACK.md` |
| `web-gpt-sources/REPORT-MARS-Web-GPT-Source-Pack-Update-v1.md` |

**Total new files:** 14  
**Modified existing:** 0  
**Deleted:** 0  

---

## Upload order

See `WEB-GPT-SOURCE-PACK-INDEX.md`. Summary:

1. `01_MARS_IDENTITY.md`  
2. `02_OPERATIONAL_POSTURE.md`  
3. `10_RUNTIME_BOUNDARY_RULES.md`  
4. `07_STABLE_BASELINE_PUBLICATION.md`  
5. `03_PROGRAM_REGISTRY_SUMMARY.md`  
6. `09_OPERATIONAL_PRIORITIES.md`  
7. `04_INFRASTRUCTURE_REALITY.md`  
8. `05_ACTIVE_VISUAL_COLD_BRAIN.md`  
9. `06_KNOWLEDGE_CENTER.md`  
10. `08_SYSTEM_MATURITY_MAP.md`  
11. `README.md`  
12. *(optional)* `WEB-GPT-CHAT-SYNC-PACK.md`  

**Minimum viable:** 1, 2, 3, 11.

---

## Chat synchronization readiness

| Program | Sync pack section | Ready |
|---------|-------------------|-------|
| ORCA | Yes — FAST PATH, freeze, MIG human handoff | ✓ |
| Website Factory | Yes — Core Run, HITL, Triumph boundary | ✓ |
| WPilot | Yes — external lane, reconciliation map | ✓ |
| OCPilot | Yes — storage registry, no vendor bulk | ✓ |
| MIG | Yes — v0.1 spine, human ORCA handoff | ✓ |
| MetaBOT | Yes — n8n external SoT | ✓ |
| HomeGateway | Yes — draft/planned, no runtime claims | ✓ |

Global preamble + per-program **Sync block** in `WEB-GPT-CHAT-SYNC-PACK.md` ready for paste into new chats after minimum truth bundle upload.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Operator uploads **both** `mars-v2-final` and new pack | Index explicitly says remove old uploads; README migration table |
| Web-GPT treats KC/ARCHIVE paths as git SoT | `06`, `04`, `05` state out-of-git and SAFE UNKNOWN |
| Baseline checkpoint confused with clean working tree | `07` documents unstaged WIP allowed |
| Runtime mythology from old numbered `02_architecture.md` | Retire numbered uploads; enforce step 3 (`10_RUNTIME_BOUNDARY`) |
| OCPilot vendor bulk pasted into Web-GPT | Chat sync + baseline exclusions |
| Stale registry rows vs distillate | `03` points to `registry/project-registry.md` as SoT |

---

## SAFE UNKNOWN

- Byte-identical diff of every `mars-v2` vs `mars-v2-final` file pair (PowerShell `fc` alias conflict — not verified file-by-file).  
- Full population of Knowledge Center sections on operator disk.  
- Per-archive contents under `C:\AI MARS STORAGE\ARCHIVE`.  
- Live n8n/MetaBOT graph parity with `exports/`.  
- Whether operator already removed legacy uploads from Web-GPT project UI.  
- HomeGateway WIP files changed after checkpoint `45518bb`.  
- Triumph/ORCA workspace deltas excluded from baseline — current task state per workspace unverified.

---

*End of report — no commit, no push.*

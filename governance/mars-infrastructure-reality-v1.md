# MARS — Infrastructure Reality v1

**Status:** **documented** — operator-confirmed physical workspace layout (2026-06-02).  
**Pass:** MARS Infrastructure Reality Synchronization Pass v1 (Lane B).  
**Is not:** deployment topology, cloud account map, NAS/sync product choice, or proof that bulk folders exist on disk.

---

## Canonical statement

| Layer | Path | Role |
|-------|------|------|
| **Workspace root (git repository)** | `C:\AI MARS` | Single MARS working copy: governance, registry, projects, workspaces, docs, minimal R1. All agent filesystem work for MARS stays here unless a task explicitly charters otherwise. |
| **Storage layer (bulk, out-of-git)** | `C:\AI MARS STORAGE` | Supporting bulk-data root on the operator machine. Large binaries, promoted baselines, site archives, snapshots, temp extracts. **Not** a second git repository, **not** a second MARS instance, **not** a parallel workspace root. |
| **Localhost runtime (execution, out-of-git)** | `D:\MARS-Localhost` | Shared Windows local web runtime: Laragon, CMS sites, databases, uploads, caches, logs. **Not** MARS brain, **not** Git authority. Governed from [projects/mars-localhost-infrastructure/](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md). |
| **Operational relationship** | — | Metadata, passports, policies, manifests, and reports remain in `C:\AI MARS`. Bulk artefacts referenced by path + checksum live under `C:\AI MARS STORAGE\<system>\` per system registry (e.g. OCPilot [external-storage-registry.md](../projects/ocpilot/external-storage-registry.md)). Live local runtime files live under `D:\MARS-Localhost\`. |

**Repo folder `storage/`** (at `C:\AI MARS\storage\`) is the **documentation** Storage Layer in MARS architecture (contracts v0). It is **not** the physical path `C:\AI MARS STORAGE`. See [../storage/README.md](../storage/README.md).

---

## Infrastructure reality matrix (pass v1 audit)

| Pattern / location | Classification | Notes |
|--------------------|----------------|-------|
| `C:\AI MARS` | **canonical** | Repo root; `.cursorrules`, `AGENTS.md`, bootstrap packs, survivability, pilot paths. |
| `C:/AI MARS/...` | **canonical** | Forward-slash variant (e.g. n8n workflow `jsCode` paths) — same root. |
| `C:\AI MARS STORAGE` | **canonical** | Operator bulk root; family note [mars-storage-family-note.md](../projects/ocpilot/mars-storage-family-note.md). |
| `C:\AI MARS STORAGE\ocpilot\...` | **canonical** | OCPilot consumer layout (Run 3.7+). |
| `C:\AI MARS\projects\ocpilot\baselines\...\files\` | **example** (migration source) | Grandfathered repo-local trees; target external path documented in [baseline-storage-migration-plan.md](../projects/ocpilot/baseline-storage-migration-plan.md) — **not** obsolete wording. |
| `C:\AI MARS\workspaces\`, `\local\`, `\backups\` | **canonical** (repo-relative) | Workspaces and WPilot local-only policy paths under workspace root. |
| `D:\MARS-Localhost` | **canonical** (localhost runtime) | Operator-approved shared local execution root (MLI-00, 2026-06-22); brain docs in `projects/mars-localhost-infrastructure/`; **not** git, **not** governance SoT. |
| `D:\AI MARS`, `D:/AI MARS` | **none in repo** | No matches at pass v1; if seen in external chats, treat as **historical/obsolete** unless operator re-confirms. |
| `D:\MARS-WP` | **obsolete / none** | No repo matches; superseded by `D:\MARS-Localhost\sites\wordpress\` model if ever proposed. |
| `storage/` (in-repo docs folder) | **canonical** (doc layer name) | Architecture contracts only — disambiguate from `C:\AI MARS STORAGE`. |
| Drill/log paths with `c:\AI MARS\...` | **historical** | Case variant in [d01-observability-results.md](../projects/mars-survivability/tools/observability/reports/d01-observability-results.md) — preserved as run evidence. |

---

## Bootstrap and onboarding alignment

| Surface | Workspace root | Storage layer |
|---------|----------------|---------------|
| [.cursorrules](../.cursorrules) | `C:\AI MARS` | — |
| [AGENTS.md](../AGENTS.md) | `C:\AI MARS` | Pointer: this doc |
| [README.md](../README.md) | `C:\AI MARS` | Pointer: this doc |
| [web-gpt-sources/mars-v2/06_MARS_v2_BOOTSTRAP_AND_MIGRATION.md](../web-gpt-sources/mars-v2/06_MARS_v2_BOOTSTRAP_AND_MIGRATION.md) | `C:\AI MARS` | Per-system registry when bulk needed |
| [web-gpt-sources/chat-migration/](../web-gpt-sources/chat-migration/) | `C:\AI MARS` | — |
| [projects/mars-survivability/protocols/safe-execution-layer-v1.md](../projects/mars-survivability/protocols/safe-execution-layer-v1.md) | `C:\AI MARS` | External bulk via task/passport |
| [projects/ocpilot/external-storage-registry.md](../projects/ocpilot/external-storage-registry.md) | Metadata in repo | `C:\AI MARS STORAGE\ocpilot\` |

---

## Normative rules (v1)

1. **One workspace root** — `C:\AI MARS` is the only MARS git working copy for documentation and agent scope unless the operator charters an explicit exception in the task.
2. **Storage is support only** — Do not describe `C:\AI MARS STORAGE` as a second MARS repo, runtime instance, or governance root.
3. **Localhost executes on D:** — `D:\MARS-Localhost` is shared local **execution** only; governance and Git remain on `C:\AI MARS`. Do not relocate MARS brain to D:.
4. **Preserve history** — Migration plans, drill logs, and archived reports may show repo-local baseline paths or old drive letters; mark **historical** in new docs, do not rewrite evidence.
5. **SAFE UNKNOWN** — Existence of on-disk folders under `C:\AI MARS STORAGE`, sync/NAS layout, and per-machine mirrors are operator infrastructure unless verified in session.

---

## Related documents

| Topic | Path |
|-------|------|
| OCPilot bulk registry | [projects/ocpilot/external-storage-registry.md](../projects/ocpilot/external-storage-registry.md) |
| MARS storage family | [projects/ocpilot/mars-storage-family-note.md](../projects/ocpilot/mars-storage-family-note.md) |
| EAR placement (repo vs external artefacts) | [projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md](../projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md) |
| MARS Localhost Infrastructure | [projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| Pass v1 report | [logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md](../logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md) |

---

*Synchronized: 2026-06-02 — Infrastructure Reality Synchronization Pass v1.*

# MARS — Infrastructure Reality v1

**Status:** **documented** — operator-confirmed physical workspace layout.
**Pass:** MARS Infrastructure Reality Synchronization Pass v1 (Lane B); **Phoenix canonical cutover** 2026-06-25 — see [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md).
**Is not:** deployment topology, cloud account map, NAS/sync product choice, or proof that bulk folders exist on disk.

---

## Canonical statement (post–Phoenix cutover)

| Layer | Path | Role |
|-------|------|------|
| **Workspace root (git repository)** | `C:\MARS Phenix\AI MARS` | Single MARS working copy: governance, registry, projects, workspaces, docs, minimal R1. All agent filesystem work for MARS stays here unless a task explicitly charters otherwise. |
| **Storage layer (bulk, out-of-git)** | `C:\MARS Phenix\AI MARS STORAGE` | Supporting bulk-data root on the operator machine. Large binaries, promoted baselines, site archives, snapshots, temp extracts. **Not** a second git repository, **not** a second MARS instance, **not** a parallel workspace root. |
| **Localhost runtime (execution, out-of-git)** | `E:\MARS-Localhost` | Shared Windows local web runtime: Laragon at `E:\MARS-Localhost\laragon`, MLI tools under `tools\`, CMS sites under `sites\`, databases, logs. **Not** MARS brain, **not** Git authority. Governed from [projects/mars-localhost-infrastructure/](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md). |
| **Canonical development branch** | `mars/canonical-post-recovery` | Active Git development line after Phoenix recovery; see [mars-canonical-branch-cutover-v1.md](mars-canonical-branch-cutover-v1.md). |
| **Immutable recovery anchor** | `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` | Fixed recovery branch — no further commits; do not merge into. |
| **Operational relationship** | — | Metadata, passports, policies, manifests, and reports remain in `C:\MARS Phenix\AI MARS`. Bulk artefacts referenced by path + checksum live under `C:\MARS Phenix\AI MARS STORAGE\<system>\` per system registry (e.g. OCPilot [external-storage-registry.md](../projects/ocpilot/external-storage-registry.md)). Live local runtime files live under `E:\MARS-Localhost\`. |

**Repo folder `storage/`** (at `C:\MARS Phenix\AI MARS\storage\`) is the **documentation** Storage Layer in MARS architecture (contracts v0). It is **not** the physical path `C:\MARS Phenix\AI MARS STORAGE`. See [../storage/README.md](../storage/README.md).

---

## Legacy and evidence trees (read-only hold)

| Tree | Path | Status |
|------|------|--------|
| **Legacy current MARS** | `C:\AI MARS` | `LEGACY_READ_ONLY_HOLD_SOURCE` — pre-cutover forward checkout; archive copy under `_legacy-hold` |
| **Legacy bulk storage** | `C:\AI MARS STORAGE` | `LEGACY_READ_ONLY_HOLD_SOURCE` — archive copy under `_legacy-hold` |
| **Immutable pre-incident backup** | `C:\this is backUP AI MARS 23.06.2026` | `PERMANENT_IMMUTABLE_BACKUP` — **not** archive candidate; do not delete |
| **Legacy archive hold** | `C:\MARS Phenix\_legacy-hold\` | `VERIFIED_ARCHIVE_EVIDENCE` — same-disk only; not canonical |
| **Historical runtime letter** | `D:\MARS-Localhost` | Preserved in incident reports and MLI-03R.* evidence; active operator runtime confirmed on **E:** after Windows reinstall (2026-06-25 reconciliation) |

---

## Infrastructure reality matrix (pass v1 audit + Phoenix cutover)

| Pattern / location | Classification | Notes |
|--------------------|----------------|-------|
| `C:\MARS Phenix\AI MARS` | **canonical** | Repo root; `.cursorrules`, `AGENTS.md`, bootstrap packs, survivability, pilot paths. |
| `C:/MARS Phenix/AI MARS/...` | **canonical** | Forward-slash variant (e.g. n8n workflow `jsCode` paths) — same root. |
| `C:\MARS Phenix\AI MARS STORAGE` | **canonical** | Operator bulk root; family note [mars-storage-family-note.md](../projects/ocpilot/mars-storage-family-note.md). |
| `C:\MARS Phenix\AI MARS STORAGE\ocpilot\...` | **canonical** | OCPilot consumer layout (Run 3.7+). |
| `C:\MARS Phenix\AI MARS\projects\ocpilot\baselines\...\files\` | **example** (migration source) | Grandfathered repo-local trees; target external path documented in [baseline-storage-migration-plan.md](../projects/ocpilot/baseline-storage-migration-plan.md) — **not** obsolete wording. |
| `C:\MARS Phenix\AI MARS\workspaces\`, `\local\`, `\backups\` | **canonical** (repo-relative) | Workspaces and WPilot local-only policy paths under workspace root. |
| `E:\MARS-Localhost` | **canonical** (localhost runtime) | Operator-confirmed shared local execution root after drive-letter reconciliation (2026-06-25); brain docs in `projects/mars-localhost-infrastructure/`; **not** git, **not** governance SoT. |
| `D:\MARS-Localhost` | **historical** (runtime) | Pre-reinstall / MLI-03R.* incident evidence; **do not** global-replace in historical reports. |
| `C:\AI MARS`, `C:\AI MARS STORAGE` | **legacy (source)** | Pre-cutover paths — retained in place; **not** active operational authority |
| `C:\MARS Phenix\_legacy-hold\` | **archive evidence** | Verified 2026-06-25 file copies; same-disk; not canonical |
| `D:\AI MARS`, `D:/AI MARS` | **none in repo** | No matches at pass v1; if seen in external chats, treat as **historical/obsolete** unless operator re-confirms. |
| `D:\MARS-WP` | **obsolete / none** | No repo matches; superseded by `E:\MARS-Localhost\sites\wordpress\` model if ever proposed. |
| `storage/` (in-repo docs folder) | **canonical** (doc layer name) | Architecture contracts only — disambiguate from `C:\MARS Phenix\AI MARS STORAGE`. |
| Drill/log paths with `c:\AI MARS\...` | **historical** | Case variant in [d01-observability-results.md](../projects/mars-survivability/tools/observability/reports/d01-observability-results.md) — preserved as run evidence. |

---

## Bootstrap and onboarding alignment

| Surface | Workspace root | Storage layer |
|---------|----------------|---------------|
| [.cursorrules](../.cursorrules) | `C:\MARS Phenix\AI MARS` | — |
| [AGENTS.md](../AGENTS.md) | `C:\MARS Phenix\AI MARS` | Pointer: this doc |
| [README.md](../README.md) | `C:\MARS Phenix\AI MARS` | Pointer: this doc |
| [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) | `C:\MARS Phenix\AI MARS` | Legacy hold documented |
| [mars-canonical-branch-cutover-v1.md](mars-canonical-branch-cutover-v1.md) | `mars/canonical-post-recovery` | Canonical development branch |
| [web-gpt-sources/mars-v2/06_MARS_v2_BOOTSTRAP_AND_MIGRATION.md](../web-gpt-sources/mars-v2/06_MARS_v2_BOOTSTRAP_AND_MIGRATION.md) | Historical `C:\AI MARS` in pack — **legacy imported** | Per-system registry when bulk needed |
| [web-gpt-sources/chat-migration/](../web-gpt-sources/chat-migration/) | Historical `C:\AI MARS` in pack — **legacy imported** | — |
| [projects/mars-survivability/protocols/safe-execution-layer-v1.md](../projects/mars-survivability/protocols/safe-execution-layer-v1.md) | `C:\MARS Phenix\AI MARS` | External bulk via task/passport |
| [projects/ocpilot/external-storage-registry.md](../projects/ocpilot/external-storage-registry.md) | Metadata in repo | `C:\MARS Phenix\AI MARS STORAGE\ocpilot\` |

---

## Normative rules (v1 + Phoenix cutover)

1. **One workspace root** — `C:\MARS Phenix\AI MARS` is the only MARS git working copy for documentation and agent scope unless the operator charters an explicit exception in the task.
2. **Storage is support only** — Do not describe `C:\MARS Phenix\AI MARS STORAGE` as a second MARS repo, runtime instance, or governance root.
3. **Localhost executes on E:** — `E:\MARS-Localhost` is shared local **execution** only; governance and Git remain on `C:\MARS Phenix\AI MARS`. Do not relocate MARS brain to E:.
4. **Legacy hold** — `C:\AI MARS` and `C:\AI MARS STORAGE` remain on disk under `LEGACY_READ_ONLY_HOLD` until operator-approved archival; do not delete on cutover or by automation. See [mars-legacy-tree-retention-decision-v1.md](mars-legacy-tree-retention-decision-v1.md).
5. **Preserve history** — Migration plans, drill logs, incident reports, and archived reports may show `C:\AI MARS`, `C:\AI MARS STORAGE`, or `D:\MARS-Localhost`; mark **historical** in new docs, do not rewrite evidence.
6. **SAFE UNKNOWN** — Existence of on-disk folders under storage roots, sync/NAS layout, and per-machine mirrors are operator infrastructure unless verified in session.

---

## Related documents

| Topic | Path |
|-------|------|
| Phoenix cutover receipt | [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) |
| Disaster recovery closure | [mars-disaster-recovery-2026-06-24-closure-v1.md](mars-disaster-recovery-2026-06-24-closure-v1.md) |
| Normal operations checklist | [mars-normal-operations-resumption-checklist-v1.md](mars-normal-operations-resumption-checklist-v1.md) |
| Legacy tree retention | [mars-legacy-tree-retention-decision-v1.md](mars-legacy-tree-retention-decision-v1.md) |
| OCPilot bulk registry | [projects/ocpilot/external-storage-registry.md](../projects/ocpilot/external-storage-registry.md) |
| MARS storage family | [projects/ocpilot/mars-storage-family-note.md](../projects/ocpilot/mars-storage-family-note.md) |
| EAR placement (repo vs external artefacts) | [projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md](../projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md) |
| MARS Localhost Infrastructure | [projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| Pass v1 report | [logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md](../logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md) |

---

*Synchronized: 2026-06-02 — Infrastructure Reality Synchronization Pass v1; Phoenix canonical paths: 2026-06-25; disaster recovery closed: 2026-06-25.*

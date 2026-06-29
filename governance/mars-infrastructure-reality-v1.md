# MARS — Infrastructure Reality v1

**Status:** **documented** — operator-confirmed physical workspace layout.
**Pass:** MARS Infrastructure Reality Synchronization Pass v1 (Lane B); **Phoenix canonical cutover** 2026-06-25 — see [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md); **X-drive authority** 2026-06-29 — see [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md).
**Is not:** deployment topology, cloud account map, NAS/sync product choice, automated volume enforcement, or proof that bulk folders exist on disk.

---

## Volume identity (current)

| Property | Required value |
|----------|----------------|
| Drive letter | `X:` |
| Volume label | **AI WS** |
| Filesystem | NTFS (expected) |

**State:** All MARS-controlled physical roots are consolidated on the **AI WS** volume (`X:`).

**Preflight:** before filesystem mutation tasks, confirm drive `X:` and label `AI WS` when volume identity can be checked. Mismatch → **STOP**.

---

## Canonical statement (current operational authority)

| Layer | Path | Role |
|-------|------|------|
| **Active Brain (git repository)** | `X:\AI MARS\` | Single MARS working copy: governance, registry, projects, workspaces, docs, minimal R1. All agent filesystem work for MARS stays here unless a task explicitly charters otherwise. |
| **Storage layer (bulk, out-of-git)** | `X:\AI MARS STORAGE\` | Supporting bulk-data root. Large binaries, promoted baselines, site archives, snapshots, temp extracts, Knowledge Center, Cold Brain archives. **Not** a second git repository, **not** a second MARS instance, **not** a parallel workspace root. |
| **Localhost runtime (execution, out-of-git)** | `X:\MARS-Localhost\` | Shared Windows local web runtime: Laragon, MLI tools under `tools\`, CMS sites under `sites\`, databases, logs. **Not** MARS brain, **not** Git authority. Governed from [projects/mars-localhost-infrastructure/](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md). |
| **Canonical development branch** | `mars/canonical-post-recovery` | Active Git development line after Phoenix recovery; see [mars-canonical-branch-cutover-v1.md](mars-canonical-branch-cutover-v1.md). Branch authority is **separate** from filesystem authority. |
| **Immutable recovery anchor** | `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` | Fixed recovery branch — no further commits; do not merge into. |
| **Operational relationship** | — | Metadata, passports, policies, manifests, and reports remain in `X:\AI MARS\`. Bulk artefacts referenced by path + checksum live under `X:\AI MARS STORAGE\<system>\` per system registry (e.g. OCPilot [external-storage-registry.md](../projects/ocpilot/external-storage-registry.md)). Live local runtime files live under `X:\MARS-Localhost\`. |

**Repo folder `storage/`** (at `X:\AI MARS\storage\`) is the **documentation** Storage Layer in MARS architecture (contracts v0). It is **not** the physical path `X:\AI MARS STORAGE\`. See [../storage/README.md](../storage/README.md).

---

## Brain layers (organizational — not autonomous services)

These are **operator organizational layers**, not autonomous AI memory services or separate MARS instances. On conflict, **Git Active Brain** remains source of truth.

| Layer | Current path | Role |
|-------|--------------|------|
| **Active Brain** | `X:\AI MARS\` | Git workspace — governance, projects, workspaces, docs |
| **Visual Brain source** | `X:\AI MARS\docs\visualization\obsidian-canvas\` | Obsidian canvas exports for spatial navigation (documentation mirror) |
| **Knowledge Center** | `X:\AI MARS STORAGE\MARS KNOWLEDGE CENTER\` | Operator Obsidian vault and knowledge bulk — **out-of-Git** |
| **Cold Brain** | `X:\AI MARS STORAGE\ARCHIVE\` | Retired bulk, archives after operator triage — **out-of-Git** |

Knowledge Center and Cold Brain remain **out-of-Git**. Programme-specific deferred path families are recorded in [mars-x-drive-deferred-path-register-v1.md](mars-x-drive-deferred-path-register-v1.md).

---

## Deprecated operational roots (write denied)

The following paths are **DEPRECATED AS CURRENT OPERATIONAL PATH — HISTORICAL USE MAY REMAIN — WRITE DENIED** for MARS-controlled operations:

| Path | Classification |
|------|----------------|
| `C:\AI MARS\` | Deprecated operational root |
| `C:\MARS Phenix\AI MARS\` | Deprecated operational root (Phoenix-era) |
| `C:\AI MARS STORAGE\` | Deprecated operational root |
| `C:\MARS Phenix\AI MARS STORAGE\` | Deprecated operational root (Phoenix-era) |
| `D:\MARS-Localhost\` | Deprecated operational root (historical runtime letter) |
| `E:\MARS-Localhost\` | Deprecated operational root (pre-X migration) |

**Authority:** [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md). Historical incident, recovery, backup, and release evidence **retains original paths** — do not rewrite.

---

## Legacy and evidence trees (read-only hold — historical)

| Tree | Path | Status |
|------|------|--------|
| **Legacy current MARS** | `C:\AI MARS` | `LEGACY_READ_ONLY_HOLD_SOURCE` — pre-cutover forward checkout; archive copy under `_legacy-hold` |
| **Legacy bulk storage** | `C:\AI MARS STORAGE` | `LEGACY_READ_ONLY_HOLD_SOURCE` — archive copy under `_legacy-hold` |
| **Phoenix-era brain** | `C:\MARS Phenix\AI MARS` | `DEPRECATED_OPERATIONAL_ROOT` — superseded by `X:\AI MARS\` for current work |
| **Phoenix-era bulk** | `C:\MARS Phenix\AI MARS STORAGE` | `DEPRECATED_OPERATIONAL_ROOT` — superseded by `X:\AI MARS STORAGE\` |
| **Immutable pre-incident backup** | `C:\this is backUP AI MARS 23.06.2026` | `PERMANENT_IMMUTABLE_BACKUP` — **not** archive candidate; do not delete |
| **Legacy archive hold** | `C:\MARS Phenix\_legacy-hold\` | `VERIFIED_ARCHIVE_EVIDENCE` — same-disk only; not canonical |
| **Historical runtime (D:)** | `D:\MARS-Localhost` | Preserved in incident reports and MLI-03R.* evidence |
| **Historical runtime (E:)** | `E:\MARS-Localhost` | Pre-X migration operator runtime; preserved in evidence |

---

## Infrastructure reality matrix (current + historical classification)

| Pattern / location | Classification | Notes |
|--------------------|----------------|-------|
| `X:\AI MARS` | **canonical** (current) | Repo root; `.cursorrules`, `AGENTS.md`, bootstrap packs, survivability, pilot paths. |
| `X:/AI MARS/...` | **canonical** (current) | Forward-slash variant — same root. |
| `X:\AI MARS STORAGE` | **canonical** (current) | Operator bulk root. |
| `X:\AI MARS STORAGE\ocpilot\...` | **canonical** (current) | OCPilot consumer layout target (programme reconciliation X6+). |
| `X:\MARS-Localhost` | **canonical** (current localhost runtime) | Operator local execution root after X-drive migration (2026-06-29). |
| `X:\AI MARS\workspaces\`, `\local\`, `\backups\` | **canonical** (repo-relative) | Workspaces and WPilot local-only policy paths under workspace root. |
| `X:\AI MARS\storage\` | **canonical** (doc layer name) | Architecture contracts only — disambiguate from `X:\AI MARS STORAGE\`. |
| `C:\MARS Phenix\AI MARS` | **historical / deprecated** | Phoenix-era repo root — **not** current operational target |
| `C:\MARS Phenix\AI MARS STORAGE` | **historical / deprecated** | Phoenix-era bulk — **not** current operational target |
| `E:\MARS-Localhost` | **historical / deprecated** | Pre-X migration runtime — preserved in evidence |
| `D:\MARS-Localhost` | **historical** (runtime) | Pre-reinstall / MLI-03R.* incident evidence |
| `C:\AI MARS`, `C:\AI MARS STORAGE` | **legacy (source)** | Pre-Phoenix paths — retained in place; **not** active operational authority |
| `C:\MARS Phenix\_legacy-hold\` | **archive evidence** | Verified 2026-06-25 file copies; same-disk; not canonical |
| Programme docs with old paths | **historical / deferred** | Classified in [mars-x-drive-deferred-path-register-v1.md](mars-x-drive-deferred-path-register-v1.md) — not active authority |

---

## Bootstrap and onboarding alignment

| Surface | Workspace root | Storage layer |
|---------|----------------|---------------|
| [.cursorrules](../.cursorrules) | `X:\AI MARS` | — |
| [AGENTS.md](../AGENTS.md) | `X:\AI MARS` | Pointer: this doc + [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md) |
| [README.md](../README.md) | `X:\AI MARS` | Pointer: this doc |
| [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md) | `X:\AI MARS` | `X:\AI MARS STORAGE`, `X:\MARS-Localhost` |
| [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) | Historical `C:\MARS Phenix\AI MARS` | Legacy hold documented — **historical** |
| [web-gpt-sources/MARS-X-DRIVE-CURRENT-PATH-ADDENDUM.md](../web-gpt-sources/MARS-X-DRIVE-CURRENT-PATH-ADDENDUM.md) | `X:\AI MARS` | Current path addendum — supersedes **physical paths only** in chat packs |
| [web-gpt-sources/mars-v2-stable-baseline-2026-06-sync/](../web-gpt-sources/mars-v2-stable-baseline-2026-06-sync/) | Historical `C:\AI MARS` in pack — **legacy imported** | Do not rewrite in place |
| [projects/mars-survivability/protocols/safe-execution-layer-v1.md](../projects/mars-survivability/protocols/safe-execution-layer-v1.md) | `X:\AI MARS` (boundary updated X1) | External bulk via task/passport |

---

## Normative rules (current)

1. **One workspace root** — `X:\AI MARS\` is the only MARS git working copy for documentation and agent scope unless the operator charters an explicit exception in the task.
2. **Storage is support only** — Do not describe `X:\AI MARS STORAGE\` as a second MARS repo, runtime instance, or governance root.
3. **Localhost executes on X:** — `X:\MARS-Localhost\` is shared local **execution** only; governance and Git remain on `X:\AI MARS\`. Do not relocate MARS brain to Localhost.
4. **Volume discipline** — MARS-controlled writes are limited to approved roots on volume **AI WS** (`X:`) per [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md).
5. **Legacy hold** — Deprecated C/D/E roots may remain on disk for historical evidence; do not delete by automation. Do not use as active Cursor workspace or write targets.
6. **Preserve history** — Migration plans, drill logs, incident reports, and archived reports may show Phoenix or C/D/E paths; mark **historical** in new docs, do not rewrite evidence.
7. **SAFE UNKNOWN** — Existence of on-disk folders under storage roots, sync/NAS layout, per-machine mirrors, and live MySQL datadir location are operator infrastructure unless verified in session.

---

## X-drive migration state (central infrastructure)

| Wave | State |
|------|-------|
| **X0** — Root authority | **COMPLETE** |
| **X1** — Filesystem boundary | **COMPLETE** |
| **X2** — Core infrastructure reality and brain layers | **COMPLETE** (this doc alignment) |
| **X3** — Central registry/topology/README alignment | **COMPLETE** |
| **X4** — Website Factory, FOUNDRY, FP-0002 | **COMPLETE** |
| **X5** — MARS Localhost Infrastructure | **COMPLETE** |
| **X6** — CMS pilot programmes | **COMPLETE** |
| **X7** — Remaining programmes | **COMPLETE** |
| **X8** — Web-GPT sync pack | **COMPLETE** |
| **X9** — Final active-path audit and closure | **COMPLETE** ([mars-x-drive-migration-closure-v1.md](mars-x-drive-migration-closure-v1.md)) |

This is **infrastructure alignment**, not a new MARS version or architecture redesign.

---

## Related documents

| Topic | Path |
|-------|------|
| X-drive root authority | [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md) |
| Phoenix cutover receipt | [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) |
| Disaster recovery closure | [mars-disaster-recovery-2026-06-24-closure-v1.md](mars-disaster-recovery-2026-06-24-closure-v1.md) |
| Normal operations checklist | [mars-normal-operations-resumption-checklist-v1.md](mars-normal-operations-resumption-checklist-v1.md) |
| Legacy tree retention | [mars-legacy-tree-retention-decision-v1.md](mars-legacy-tree-retention-decision-v1.md) |
| Web-GPT current path addendum | [web-gpt-sources/MARS-X-DRIVE-CURRENT-PATH-ADDENDUM.md](../web-gpt-sources/MARS-X-DRIVE-CURRENT-PATH-ADDENDUM.md) |
| MARS Localhost Infrastructure | [projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| Pass v1 report | [logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md](../logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md) |
| X2–X3 alignment report | [reports/mars-x-drive-migration-x2-x3-core-alignment-v1.md](../reports/mars-x-drive-migration-x2-x3-core-alignment-v1.md) |

---

*Synchronized: 2026-06-02 — Infrastructure Reality Synchronization Pass v1; Phoenix canonical paths: 2026-06-25; X-drive authority and central alignment: 2026-06-29 (waves X2–X3).*

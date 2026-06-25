# MARS — Legacy tree retention decision v1

**Status:** **documented** — operator-authoritative retention and archive-readiness policy; **verified same-disk archive snapshots** recorded 2026-06-25.
**Is not:** deletion authority, unique-content export execution, or runtime migration.

**Audit receipt:** `C:\MARS Phenix\_reconstruction-control\reports\REPORT-LEGACY-STORAGE-UNIQUE-CONTENT-AUDIT.md`  
**Checkpoint:** `C:\MARS Phenix\_reconstruction-control\checkpoints\LEGACY-STORAGE-AUDIT-COMPLETE.md`

---

## Canonical authority (unchanged)

| Layer | Path | Status |
|-------|------|--------|
| **Git repository** | `C:\MARS Phenix\AI MARS` | `ACTIVE_CANONICAL_WORKING_TREE` |
| **Development branch** | `mars/canonical-post-recovery` @ `9f040e40` | Active |
| **Immutable recovery anchor** | `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` | Fixed — no further commits |
| **Bulk storage** | `C:\MARS Phenix\AI MARS STORAGE` | `ACTIVE_CANONICAL_STORAGE` |

---

## Legacy and evidence trees (final hold)

| Tree | Path | Status | Archive readiness |
|------|------|--------|-------------------|
| **Legacy forward repository** | `C:\AI MARS` | `LEGACY_READ_ONLY_HOLD_SOURCE` | archived — see below |
| **Legacy bulk storage** | `C:\AI MARS STORAGE` | `LEGACY_READ_ONLY_HOLD_SOURCE` | archived — see below |
| **Pre-incident backup** | `C:\this is backUP AI MARS 23.06.2026` | `PERMANENT_IMMUTABLE_BACKUP` | `NOT_ARCHIVE_CANDIDATE` |

### Verified archive snapshots (2026-06-25)

Operator-approved same-disk copies — **recovery evidence only**; **not** canonical; **not** deletion authority.

| Source | Archive destination | Role |
|--------|---------------------|------|
| `C:\AI MARS` | `C:\MARS Phenix\_legacy-hold\AI MARS-forward-source-2026-06-25` | `VERIFIED_ARCHIVED_LEGACY_FORWARD_SOURCE` |
| `C:\AI MARS STORAGE` | `C:\MARS Phenix\_legacy-hold\AI MARS STORAGE-forward-source-2026-06-25` | `VERIFIED_ARCHIVED_LEGACY_STORAGE_SNAPSHOT` |

Control root: `C:\MARS Phenix\_legacy-hold\README.md`
Checkpoint: `C:\MARS Phenix\_reconstruction-control\checkpoints\LEGACY-ARCHIVE-SNAPSHOT-COMPLETE.md`

**Redundancy:** `SAME-DISK_ARCHIVE_ONLY` — `OFF-DISK_REDUNDANCY_PENDING`. Sources remain in place.

---

## Legacy STORAGE audit conclusion (2026-06-25)

Structural comparison of `C:\AI MARS STORAGE` vs `C:\MARS Phenix\AI MARS STORAGE`:

| Metric | Value |
|--------|------:|
| Legacy files | 11 372 |
| Canonical files | 16 830 |
| Same relative path (both trees) | **1** (V7 release ZIP — identical SHA) |
| Legacy-only paths | 11 371 |
| Canonical-only paths | 16 829 |
| Same-path size conflicts | 0 |
| True unique content (archive blockers) | **0** |
| `SAFE_UNKNOWN` blocking archive | **0** |

**Legacy STORAGE composition:**

1. **`_mars-recovery-clone/`** (11 370 files) — recovery git clone snapshot (2026-06-24). Canonical authority is Phoenix Git (`recovery/mars-phenix-2026-06-25` + `mars/canonical-post-recovery`). Classified as `LEGACY_ONLY_RECOVERY_EVIDENCE` / forensic retain; **not** unreplicated unique bulk.
2. **`assessment-cache-recovery-20260624.json`** — post-incident assessment cache (`LEGACY_ONLY_CACHE`); non-authoritative.
3. **`website-factory/.../FP-0002-V7-...-SOURCE.zip`** — identical in both trees (SHA `5F009AE3…`).

Critical recovery assets (FIG, PNG, V7 ZIP) are present and hash-verified in canonical Phoenix STORAGE and/or working tree. Absence of a third legacy STORAGE FIG copy is **not** content loss.

---

## Policy rules

1. **No automatic archive** — further moves or compression require a separate operator charter. **2026-06-25:** operator-approved same-disk archive snapshots completed; sources retained.
2. **No deletion authority** — agents and automation **must not** delete or purge legacy trees, original backup, or canonical STORAGE.
3. **Explicit operator approval** — any future archive operation requires operator confirmation and a manifest-driven copy-before-move plan (see `legacy-storage-future-export-plan.csv` — empty blockers at audit time).
4. **Recovery branch immutable** — `recovery/mars-phenix-2026-06-25` remains a fixed anchor; do not merge or amend.
5. **Canonical branch active** — routine development on `mars/canonical-post-recovery` only.
6. **Offline redundancy** — Phoenix STORAGE is local-only on `C:`; see [REPORT-RECOVERY-OFFLINE-REDUNDANCY-PLAN.md](../../_reconstruction-control/reports/REPORT-RECOVERY-OFFLINE-REDUNDANCY-PLAN.md).

---

## Related documents

| Topic | Path |
|-------|------|
| Infrastructure reality | [mars-infrastructure-reality-v1.md](mars-infrastructure-reality-v1.md) |
| Phoenix cutover receipt | [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) |
| Canonical branch cutover | [mars-canonical-branch-cutover-v1.md](mars-canonical-branch-cutover-v1.md) |
| Control manifests | `C:\MARS Phenix\_reconstruction-control\manifests\` |

---

*Established: 2026-06-25 — legacy STORAGE unique-content audit and tree hold finalization.*

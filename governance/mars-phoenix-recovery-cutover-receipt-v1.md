# MARS Phoenix — Recovery and canonical cutover receipt v1

**Status:** **documented** — operator-authoritative cutover record after 2026-06-24 incident reconstruction.
**Is not:** branch integration decision, legacy archival execution, or runtime migration proof.

---

## Incident and recovery anchor

| Field | Value |
|-------|-------|
| **Incident date** | 2026-06-24 |
| **Recovery branch** | `recovery/mars-phenix-2026-06-25` |
| **Recovery reconstruction commit** | `eb2ca92224353efdb3157c6c5c9bdf210930afaf` |
| **Parent commit** | `84b9a8c77dd9472bea6b23e6ec327ba3081c3615` |
| **Remote** | `origin` → `https://github.com/MultyMartis/MARS.git` |
| **Reconstruction status** | **validated** (Phoenix tree; pre-cutover validation receipts under `C:\MARS Phenix\_reconstruction-control\`) |

---

## Canonical working layout (post-cutover)

| Layer | Path | Role |
|-------|------|------|
| **Canonical git repository** | `C:\MARS Phenix\AI MARS` | MARS brain — governance, projects, workspaces, docs |
| **Canonical bulk storage** | `C:\MARS Phenix\AI MARS STORAGE` | Out-of-git bulk — baselines, archives, large assets |
| **Localhost runtime (execution)** | `E:\MARS-Localhost` | Shared Windows local web runtime — **not** Git authority |

**Mandatory formulation (MLI):**

```text
C:\MARS Phenix\AI MARS governs.
E:\MARS-Localhost executes.
```

---

## Legacy and evidence trees (read-only hold)

| Tree | Path | Status |
|------|------|--------|
| **Legacy current MARS** | `C:\AI MARS` | `LEGACY_READ_ONLY_RECOVERY_SOURCE` — **not** canonical working copy; **no** deletion on this cutover |
| **Immutable pre-incident backup** | `C:\this is backUP AI MARS 23.06.2026` | `IMMUTABLE_PRE_INCIDENT_BACKUP` — forensic evidence only |
| **Reconstruction control** | `C:\MARS Phenix\_reconstruction-control` | Out-of-repo manifests, checkpoints, reports |

Historical documentation may still cite `C:\AI MARS` or `D:\MARS-Localhost` where those paths describe **past** operator state. Do **not** mass-rewrite incident, drill, or receipt evidence.

---

## Path reconciliation status

| Track | Status |
|-------|--------|
| **Repository / storage operational paths** | **completed** in post-cutover commit (`recovery: establish Phoenix canonical paths`) |
| **Runtime drive-letter reconciliation** | **completed** (2026-06-25 pass 2) — active MLI registries, standards, manifests, and operational authority docs use `E:\MARS-Localhost`; historical `D:\MARS-Localhost` preserved in MLI-03R.* reports and governance historical rows |
| **Branch integration** | **decision documented** — see [mars-phoenix-branch-integration-decision-v1.md](mars-phoenix-branch-integration-decision-v1.md); merge **not executed**; recovery branch remains canonical working line until permanent branch charter |

---

## Outstanding (explicit non-goals of this receipt)

- Merge recovery branch into `mars/post-cycle8-live-tests` or `main`
- Delete, rename, or archive `C:\AI MARS`
- Modify contents of legacy trees or original backup
- Start Laragon/MySQL/CMS runtime services
- Claim full Windows reboot / MLI cold-start validation complete

---

## Related authority

| Topic | Path |
|-------|------|
| Infrastructure reality (canonical paths) | [mars-infrastructure-reality-v1.md](mars-infrastructure-reality-v1.md) |
| Operational survivability | [operational-survivability.md](operational-survivability.md) |
| MLI operational index | [../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md](../projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| Post-cutover control reports | `C:\MARS Phenix\_reconstruction-control\reports\` (out-of-repo) |

---

*Established: 2026-06-25 — MARS Phoenix canonical cutover + controlled path reconciliation.*

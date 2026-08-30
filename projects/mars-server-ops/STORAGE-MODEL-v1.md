# MARS Server Ops — Storage Model v1

**Status:** **proposed** logical layout — **directories not created in Phase 1A**  
**Not:** second Git repository, Knowledge Center, or automated sync product

---

## 1. Purpose

Define where **out-of-Git** Server Ops artifacts live on the canonical bulk root, aligned with [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md) and OCPilot Storage patterns.

---

## 2. Canonical roots (reminder)

| Role | Path |
|------|------|
| **Active Brain** | `X:\AI MARS` — Git-safe documentation |
| **Bulk Storage** | `X:\AI MARS STORAGE` — large/sensitive artifacts |
| **Local runtime secrets** | `X:\AI MARS\local\` — gitignored |
| **Localhost runtime** | `X:\MARS-Localhost` — MLI only — **not** Server Ops default |

**Volume label:** AI WS (`X:`)

Storage is a **supporting layer** — not a parallel workspace root or second MARS repository.

**Knowledge Center** is **not** the programme source of truth for Server Ops inventories or passports.

---

## 3. Programme Storage root (proposed)

```text
X:\AI MARS STORAGE\mars-server-ops\
```

**Phase 1A:** path documented only — **no folders created**.

Naming aligns with programme slug; adjust only via explicit governance charter if global Storage taxonomy changes.

---

## 4. Logical structure (proposed)

| Folder | Purpose | Typical content |
|--------|---------|-----------------|
| `incoming\` | Staging uploads from operator | Raw exports pending sanitization |
| `inventories\` | Sanitized inventory exports | CSV/JSON snapshots for operator review |
| `configs\` | Redacted or full configs | **Full secrets stay here or local — never Git** |
| `backups\` | Backup artifacts | DB dumps, volume archives, manifest sidecars |
| `baselines\` | Known-good snapshots | Pre-change checkpoints |
| `logs\` | Exported logs (bounded) | Sanitized log bundles |
| `evidence\` | REPORT attachments | Screenshots, command output (redacted) |
| `restore-tests\` | Restore drill evidence | Proof of restore strategy |
| `temp\` | Short-lived working files | Delete per operator policy |
| `archive\` | Superseded material | Retired backups/configs |

Subpaths may include `<inventory_ref>/` or `<passport_id>/` when populated.

**OCPilot parallel:** [projects/ocpilot/external-storage-registry.md](../ocpilot/external-storage-registry.md) uses `X:\AI MARS STORAGE\ocpilot\` — Server Ops uses its own subtree to avoid mixing CMS acquisition bulk with VPS ops bulk.

---

## 5. Five-way separation

| Class | Location | Git? |
|-------|----------|------|
| **1. Active Brain / Git-safe docs** | `X:\AI MARS\projects\mars-server-ops\` | Yes |
| **2. Local-only secrets** | `X:\AI MARS\local\infrastructure\...` | **Never** |
| **3. Raw/sensitive Storage** | `X:\AI MARS STORAGE\mars-server-ops\...` | **Never** |
| **4. Backup/archive** | Storage `backups\`, `archive\`, `baselines\` | **Never** |
| **5. Incoming/temp** | Storage `incoming\`, `temp\` | **Never** — promote or purge |

---

## 6. Reference pattern in Git

Git documents **pointers** only:

```markdown
backup_manifest: X:\AI MARS STORAGE\mars-server-ops\backups\SRV-OPS-001\2026-08-25-manifest.md
```

Or relative narrative in REPORT — full paths preferred for operator clarity on Windows.

---

## 7. Agent boundaries

| Allowed | Forbidden |
|---------|-----------|
| Document proposed paths | Create Storage trees without charter |
| Read sanitized evidence when operator attaches | Bulk copy from production without charter |
| Reference manifests in REPORT | `robocopy /MIR` or purge without destructive charter |

---

## 8. Related documents

- [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md)  
- [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md)  
- [EAR Storage Model](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) — conceptual parallel  
- [governance/mars-x-drive-root-authority-v1.md](../../governance/mars-x-drive-root-authority-v1.md)  

---

*Storage Model v1 · proposed layout · Phase 1A · no directories created.*

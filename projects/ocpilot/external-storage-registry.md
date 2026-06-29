# OCPilot — External Storage Registry

**Run:** 3.7 — External Storage Architecture  
**Status:** canonical registry — **no** baseline migration in this run.

---

## Approved storage roots

| Scope | Path | Migration evidence (pre-X-drive) |
|-------|------|----------------------------------|
| **MARS bulk root** | `X:\AI MARS STORAGE` | `C:\MARS Phenix\AI MARS STORAGE` |
| **OCPilot bulk root** | `X:\AI MARS STORAGE\ocpilot\` | `C:\MARS Phenix\AI MARS STORAGE\ocpilot\` |

External storage is **not** a git repository by default. The MARS repo at `X:\AI MARS` holds metadata; this registry describes where bulk lives.

**On-disk READMEs:** each external folder has an operator-facing README under `X:\AI MARS STORAGE\`.

**Physical verification (2026-06-29, read-only):** `X:\AI MARS STORAGE\ocpilot\` present with `baselines\`, `incoming\`, `project-sites\`, `backups\`, `temp\` — **EXTERNAL_PRESENT**.

---

## OCPilot subfolder contract

| Subfolder | Full path |
|-----------|-----------|
| `baselines\` | `X:\AI MARS STORAGE\ocpilot\baselines\` |
| `incoming\` | `X:\AI MARS STORAGE\ocpilot\incoming\` |
| `project-sites\` | `X:\AI MARS STORAGE\ocpilot\project-sites\` |
| `backups\` | `X:\AI MARS STORAGE\ocpilot\backups\` |
| `temp\` | `X:\AI MARS STORAGE\ocpilot\temp\` |

---

## `baselines\`

**Purpose:** Canonical external storage for verified baseline ZIP archives and (after migration) promoted baseline `files/` trees.

| Aspect | Policy |
|--------|--------|
| **What can be stored** | Canonical OpenCart/ocStore ZIP per baseline; promoted sanitized vendor trees; optional checksum sidecars; per-baseline folders (`ocstore-3038-rs2/`, etc.) |
| **What must not be stored** | Unverified quarantine ZIPs; live production site dumps; credentials; unrelated system bulk |
| **Large files** | **Yes** — primary bulk zone |
| **Secrets** | **No** — forbidden |
| **Git-tracked** | **No** |

**OCPilot reference:** passports record `external_zip_path` and SHA256; future promoted path under this folder. Repo metadata: `projects/ocpilot/baselines/<id>/passports/`, `manifest/`.

---

## `incoming\`

**Purpose:** External dropzone for new baseline candidate ZIPs before verification.

| Aspect | Policy |
|--------|--------|
| **What can be stored** | New baseline ZIPs awaiting intake; working copies during acquisition |
| **What must not be stored** | Verified canonical ZIPs (belong in `baselines\`); promoted trees; project site archives |
| **Large files** | **Yes** |
| **Secrets** | **No** |
| **Git-tracked** | **No** |

**OCPilot reference:** mirrors repo quarantine at `projects/ocpilot/incoming/baselines/` — operator may use repo-local, external, or both during transition; both are gitignored under Option D.

---

## `project-sites\`

**Purpose:** Bulk storage for project site file archives and snapshots (Run 4+).

| Aspect | Policy |
|--------|--------|
| **What can be stored** | Read-only site snapshots; exported theme/catalog trees; site archive ZIPs; external DB dumps if operator policy allows |
| **What must not be stored** | Unreviewed PII-heavy dumps; baseline vendor ZIPs; credentials |
| **Large files** | **Yes** |
| **Secrets** | **No** — sanitize before storage |
| **Git-tracked** | **No** — site passports and audit reports in repo only |

**OCPilot reference:** `projects/ocpilot/sites/<slug>/` for metadata; bulk here.

---

## `backups\`

**Purpose:** Operator backup copies of OCPilot bulk artifacts.

| Aspect | Policy |
|--------|--------|
| **What can be stored** | Dated copies of ZIPs or promoted trees before migration; pre-change snapshots |
| **What must not be stored** | Sole retention of canonical ZIP; unlabeled dumps; secrets |
| **Large files** | **Yes** |
| **Secrets** | **No** |
| **Git-tracked** | **No** |

---

## `temp\`

**Purpose:** Temporary extractions and scratch work — discard when intake or comparison completes.

| Aspect | Policy |
|--------|--------|
| **What can be stored** | Short-lived extract trees; comparison scratch; manifest generation working copies |
| **What must not be stored** | Canonical ZIP; long-term promoted trees; only copy of audit-relevant material |
| **Large files** | **Yes** — during active work only |
| **Secrets** | **No** |
| **Git-tracked** | **No** |

---

## Repo vs external split (Run 3.7)

| In MARS git (`projects/ocpilot/`) | In external storage |
|-----------------------------------|---------------------|
| Passports, manifests, database metadata | Canonical baseline ZIPs |
| Comparison notes, readiness reports | Promoted baseline trees (target) |
| Policies, templates, OPERATIONAL-INDEX | Project site archives (Run 4+) |
| Intake reports, storage docs | File snapshots, DB snapshots |
| README / structure placeholders | Temporary extracts, backup copies |

**Grandfathered (Run 3.7):** Run 3.5 promoted `files/` trees and incoming ZIPs remain under repo paths until migration per [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md).

---

## How OCPilot references external storage

1. **Passports** — record approved external path and SHA256 for canonical ZIP (and promoted path when migrated).
2. **Manifests** — path counts and structure evidence; not a duplicate of every external file.
3. **This registry** — folder contract and allow/deny rules.
4. **Recommended model** — [recommended-storage-model.md](recommended-storage-model.md) Option D.
5. **External READMEs** — operator orientation at `X:\AI MARS STORAGE\ocpilot\`.

No automated path resolver or sync engine is claimed in Run 3.7.

---

## Related documents

| Doc | Role |
|-----|------|
| [recommended-storage-model.md](recommended-storage-model.md) | Option D canonical model |
| [git-storage-policy.md](git-storage-policy.md) | Git allow/deny |
| [baselines/storage-policy.md](baselines/storage-policy.md) | ZIP / extract / metadata classes |
| [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md) | Future repo → external move |
| [mars-storage-family-note.md](mars-storage-family-note.md) | MARS-wide bulk root family |

---

## SAFE UNKNOWN

- Whether operator will mirror external paths on a second machine — not defined.
- Automated integrity checks on external tree vs passport — not implemented.

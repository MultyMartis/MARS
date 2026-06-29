# OCPilot — Git Storage Policy

**Run:** 3.6 — Baseline Storage Review (updated Run 3.7)  
**Status:** policy document only — **no** `.gitignore` modifications in Run 3.6 or 3.7.

**Canonical model:** [recommended-storage-model.md](recommended-storage-model.md) — Option D (external baseline storage + metadata in repo).

**Approved external root (Run 3.7):** `X:\AI MARS STORAGE` — OCPilot bulk under `X:\AI MARS STORAGE\ocpilot\`. See [external-storage-registry.md](external-storage-registry.md).

---

## Policy statement

**Git tracks operational truth. Git does not track vendor bulk.**

OCPilot content in git should answer: *who is this baseline, what version, what paths matter, what changed vs upstream, is it READY, where is the canonical ZIP stored externally?*

Git should **not** answer: *store every OpenCart PHP file for every version forever.*

---

## Current git evidence (2026-05-30)

| Observation | Implication |
|-------------|-------------|
| `git ls-files -- projects/ocpilot` → **0** | No OCPilot content in git index yet |
| ~7735 untracked entries under `projects/ocpilot/` | First commit is a **policy choice**, not a rollback |
| ~7608 untracked files in promoted `files/` trees | Bulk can still be excluded from first commit |

Run 3.6 establishes policy **before** baseline bulk enters git history.

---

## Allowed in git

| Category | Examples | Rationale |
|----------|----------|-----------|
| **Passports** | `baselines/*/passports/*-passport-v*.md` | Baseline identity, source, readiness, external storage pointer |
| **Manifests** | `baselines/*/manifest/baseline-manifest-v*.md` | Path inventories, checksum labels, structure evidence |
| **Database metadata** | `baselines/*/database/database-metadata-v*.md` | Schema summary — not live dumps |
| **Comparison notes** | `comparison-notes/*.md`, `baselines/*/comparison-notes/*.md` | Audit deltas, structured reviews |
| **Readiness reports** | `run-*-readiness-recheck.md`, checklists applied | Operational gate evidence |
| **Intake reports** | From [templates/intake-report-template.md](templates/intake-report-template.md) | Acquisition evidence |
| **Storage and policy docs** | `storage-*.md`, `recommended-storage-model.md`, `git-storage-policy.md`, `baselines/storage-policy.md`, `external-storage-registry.md`, `baseline-storage-migration-plan.md`, `mars-storage-family-note.md` | Canonical policy |
| **Workflow and architecture** | `OPERATIONAL-INDEX.md`, `intake-workflow.md`, `architecture.md`, etc. | Human-operated procedures |
| **Templates** | `templates/*.md` | Standard forms |
| **Knowledge principles** | `knowledge/knowledge-storage-principles.md`, topic README stubs | Reference layer discipline |
| **Baseline README / placeholders** | `baselines/*/README.md`, `.gitkeep` in empty subfolders | Structure without bulk |
| **Site metadata (future Run 4+)** | `sites/<slug>/passports/`, audit reports — not full site file trees | Project site operational truth |

**Size expectation:** documentation-scale — on the order of **hundreds of KB to low MB** for OCPilot metadata, not hundreds of MB.

---

## Not allowed in git (recommended exclusion)

| Category | Path pattern (illustrative) | Rationale |
|----------|------------------------------|-----------|
| **Promoted vendor trees** | `baselines/*/files/**` | ~3800 files / ~48 MB per baseline; comparison cache only |
| **Canonical ZIP archives** | `incoming/baselines/*.zip` | Binary bulk; canonical copy lives externally |
| **Temporary extractions** | Scratch or quarantine extract paths | Working material per [baselines/storage-policy.md](baselines/storage-policy.md) |
| **Install SQL bulk** | `baselines/*/files/**/install/*.sql`, large schema dumps | Vendor install artifact inside promoted tree — excluded with `files/` |
| **Vendor packages (Composer/npm inside baseline)** | `baselines/*/files/**/vendor/**`, `**/node_modules/**` | Third-party dependency bulk |
| **Project site file snapshots (future)** | Full exported site trees under `sites/` | TBD in Run 4; default **exclude** pending site storage policy |
| **Extension reference package bulk (future)** | Large extension trees | External storage + manifest in repo |
| **Comparison pack archives (future)** | ZIP/tar of multi-baseline diff bundles | External storage + index in repo |
| **Secrets and live config** | `config.php` with real credentials, tokens, dumps with PII | Forbidden per [baseline-storage-model.md](baseline-storage-model.md) — never commit |

---

## Category-specific recommendations

### Promoted baseline trees (`baselines/*/files/`)

| Aspect | Recommendation |
|--------|----------------|
| **Git** | **Exclude** |
| **Disk** | Keep locally for active READY baselines |
| **Canonical reset** | Re-promote from external ZIP |
| **Current Run 3.5 trees** | Remain on disk under repo path (grandfathered local cache); do not commit |
| **Future promoted trees** | Prefer `X:\AI MARS STORAGE\ocpilot\baselines\<id>\files\` — gitignored via repo path or absent from repo |

**Why exclude:** 98% of OCPilot file count; poor git object model; duplicates ZIP content in another form.

### ZIP archives (`incoming/baselines/`)

| Aspect | Recommendation |
|--------|----------------|
| **Git** | **Exclude** |
| **Canonical location** | External operator storage (path in passport) |
| **Working copy** | May remain in `incoming/baselines/` locally for intake workflow |
| **Integrity** | SHA256 in manifest and passport |

**Why exclude:** Binary blobs; ~16 MB each; multiply with every baseline version.

### Install SQL

| Aspect | Recommendation |
|--------|----------------|
| **Inside promoted `files/`** | Excluded with `files/` gitignore pattern |
| **Metadata in `database/`** | **Include** — table lists, prefix notes, human summaries |
| **Full sanitized schema export (optional future)** | Case-by-case; prefer metadata over multi-MB SQL in git |

**Why:** Schema **descriptions** support audit; full install SQL is vendor bulk already present in ZIP and promoted tree.

### Vendor packages (scssphp, twig, etc. inside baseline)

| Aspect | Recommendation |
|--------|----------------|
| **Git** | **Exclude** — part of `files/` tree |
| **Audit** | Referenced via manifest path counts, not individual file git history |

---

## First OCPilot commit guidance (policy only — not executed in Run 3.6)

When operator authorizes first OCPilot git commit:

1. Stage metadata paths only (passports, manifests, policies, OPERATIONAL-INDEX, etc.).
2. **Do not stage** `baselines/*/files/` or `incoming/baselines/*.zip`.
3. Add `.gitignore` patterns in a **separate human-chartered change** (out of Run 3.6 scope).
4. Record external ZIP location in passports before relying on git-only clone.

Suggested ignore patterns (documentation — **not applied** in Run 3.6):

```
projects/ocpilot/baselines/*/files/
projects/ocpilot/incoming/baselines/*.zip
```

---

## Alignment with MARS discipline

| MARS principle | OCPilot git policy |
|----------------|-------------------|
| Status honesty | Metadata in git proves baseline **identity**; external ZIP proves baseline **content** |
| Repo survivability | Avoid vendor bulk dominating clone and index |
| Human-operated gates | Commit decision remains operator HITL — no automation |
| SAFE UNKNOWN | If external path missing, passport must say so — do not pretend baseline is clone-complete |

---

## Related documents

| Doc | Role |
|-----|------|
| [recommended-storage-model.md](recommended-storage-model.md) | Selected storage model |
| [storage-audit-run-3.6.md](storage-audit-run-3.6.md) | Size evidence |
| [baseline-storage-model.md](baseline-storage-model.md) | Forbidden content |
| [baselines/storage-policy.md](baselines/storage-policy.md) | ZIP / extract / metadata classes |
| [external-storage-registry.md](external-storage-registry.md) | External folder contract (Run 3.7) |

---

## Repo vs external (Run 3.7 summary)

| In git | Outside git (external or grandfathered local) |
|--------|-----------------------------------------------|
| Passports, manifests, database metadata, comparison notes, reports, policies | Baseline ZIPs, promoted trees, site archives, snapshots, temp extracts, backups |

External storage is **not** git by default. Grandfathered Run 3.5 bulk remains under `projects/ocpilot/` until migration per [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md).

---

## SAFE UNKNOWN

- Exact `.gitignore` patch timing — requires separate operator commit; not done in Run 3.6 or 3.7.
- Git LFS for ZIP — **not recommended** as default; treated as bulk storage in git remote either way.
- Whether `incoming/baselines/README.md` alone stays tracked while ZIPs ignored — yes, README is metadata.

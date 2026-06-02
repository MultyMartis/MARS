# OCPilot — Baseline Storage Policy

**Purpose:** define how baseline source archives, temporary extractions, and permanent metadata relate — and why OCPilot controls repository growth.

**Status:** documented policy; updated Run 3.7 — external root `C:\AI MARS STORAGE\ocpilot\` approved.

**Parent:** [README.md](README.md) · **Related:** [baseline-storage-model.md](../baseline-storage-model.md), [archive-intake-rules.md](../archive-intake-rules.md), [external-storage-registry.md](../external-storage-registry.md)

---

## Three storage classes

| Class | Role | Lifetime | Canonical? |
|-------|------|----------|------------|
| **ZIP archive** | Original operator-supplied baseline package | Retained per operator policy; may live in `incoming/baselines/` during quarantine or external to repo | **Yes — canonical source** |
| **Extracted copy** | Temporary working tree used for inspection, manifest generation, or sanitization review | **Temporary** — discard after work completes unless operator explicitly retains | No |
| **Permanent metadata** | Passport, manifest, comparison notes, version notes | Stored under `baselines/<version-folder>/` after human-approved intake | Yes — operational truth for comparison |

---

## Canonical source: ZIP archive

The **ZIP archive** is the canonical baseline source.

| Rule | Meaning |
|------|---------|
| Archive is source of truth | If extracted copy and metadata disagree, re-inspect archive |
| Do not assume root layout | OpenCart files may be nested inside a package folder — see [archive-intake-rules.md](../archive-intake-rules.md) |
| Prefer archive over re-download | Once intake-approved, archive identity (filename, size, structure) is recorded in passport and intake report |
| Repo growth control | Large binaries enter repo only when operator policy allows; metadata-first approach reduces duplicate bulk |

**Example archives (Run 3 targets):**

| Archive | Expected package root inside ZIP |
|---------|----------------------------------|
| `opencart-3.0.3.8-rs.zip` | `upload-3038-rs2/` |
| `opencart-3.0.3.9-rs.zip` | `upload-3039-rs1/` |

These are **known examples**, not a guarantee that all future archives follow the same naming pattern.

---

## Temporary source: extracted copy

Extracted copies exist only to support human-operated work:

- archive structure inspection
- package root / OpenCart root detection
- manifest or directory map generation
- sanitization review before placement in `baselines/<version-folder>/files/`

| Rule | Meaning |
|------|---------|
| **Temporary only** | Extraction is working material, not a second baseline |
| **Do not keep duplicates** | Do not maintain multiple full extracted copies of the same archive in repo |
| **Discard after use** | When passport, manifest, and intake report are complete, remove temporary extraction unless operator explicitly retains for external workflow |
| **Never replace ZIP** | Deleting archive because extraction exists is forbidden without operator decision |

Extracted content promoted to `baselines/<version-folder>/files/` is **sanitized reference material**, not a raw duplicate of the full archive tree.

**External promoted trees (Run 3.7+):** target location `C:\AI MARS STORAGE\ocpilot\baselines\<version-folder>\files\`. Run 3.5 trees remain under repo path temporarily — see [baseline-storage-migration-plan.md](../baseline-storage-migration-plan.md).

---

## Permanent metadata

After successful intake (Run 3+), permanent artifacts live under the versioned baseline folder:

| Artifact | Location | Purpose |
|----------|----------|---------|
| **Passport** | `passports/` | Identity, source, version, trust, readiness flags — [versioned-baseline-passport-template.md](../templates/versioned-baseline-passport-template.md) |
| **Manifest** | `manifest/` | Path lists, directory maps, checksum labels |
| **Comparison notes** | `comparison-notes/` | Known ocStore vs upstream deltas, rs build notes |
| **Version notes** | `notes/` | Source URL, exclusions, operator commentary, intake report reference |

Metadata is **small, durable, and comparison-useful**. It survives without keeping endless extracted copies in git.

---

## Repository growth control

| Principle | Application |
|-----------|-------------|
| **One canonical archive** | Avoid storing the same baseline as ZIP + full extract + full `files/` tree without operator justification |
| **Metadata over bulk** | Prefer manifest and passport over committing redundant full trees |
| **Sanitized `files/` only** | `baselines/<version-folder>/files/` holds sanitized vendor reference — not live configs, cache, or customer data |
| **No silent accumulation** | Temporary extractions in incoming or scratch paths must not persist run-to-run without review |
| **Human approval** | Promotion from incoming to `baselines/` requires operator gate — see [intake-workflow.md](../intake-workflow.md) |

---

## Why OCPilot prefers metadata over endless extracted copies

| Reason | Explanation |
|--------|---------------|
| **Repo size** | Full OpenCart/ocStore trees are large; multiple copies per version multiply git and clone cost |
| **Drift risk** | Two extracted copies of the same archive can diverge after ad-hoc edits; ZIP + metadata keeps a single inspectable source |
| **Comparison purpose** | Audits need **classified reference** (manifest, passport, sanitized tree) — not every intermediate extraction state |
| **Security** | Raw extracts may contain default configs or paths that should be stripped before permanent storage |
| **Operational clarity** | Passport + manifest answer *«what version is this and what paths matter?»* without requiring operators to diff duplicate folders |
| **Reproducibility** | Canonical ZIP can be re-extracted for verification; metadata records how that extraction was interpreted (package root, OpenCart root) |

OCPilot does **not** claim automated deduplication or storage enforcement — this policy guides **human-operated** intake and placement.

---

## Workflow summary

```
Operator ZIP  →  incoming/baselines/     (canonical source during quarantine)
       ↓
Temporary extract  →  inspect structure   (working copy; discard when done)
       ↓
Intake report + draft passport
       ↓
Operator approval
       ↓
Sanitized files/ + manifest/ + passports/ + comparison-notes/   (permanent metadata + reference tree)
```

No automatic promotion. No automatic extraction into `baselines/`.

---

## Related documents

| Doc | Role |
|-----|------|
| [archive-intake-rules.md](../archive-intake-rules.md) | Archive Root, Package Root, OpenCart Root |
| [baseline-acquisition-precheck.md](../baseline-acquisition-precheck.md) | Pre-intake checklist |
| [baseline-storage-model.md](../baseline-storage-model.md) | Subfolder contract and forbidden content |
| [incoming/baselines/README.md](../incoming/baselines/README.md) | Dropzone rules |
| [run-3-preparation.md](../run-3-preparation.md) | First acquisition run |
| [external-storage-registry.md](../external-storage-registry.md) | External folder contract |
| [baseline-storage-migration-plan.md](../baseline-storage-migration-plan.md) | Future migration from repo-local bulk |

---

## SAFE UNKNOWN

- Exact date of migration for Run 3.5 grandfathered repo-local `files/` — separate chartered run.
- Exact retention period for temporary extractions — not automated; operator decides per run.
- Automated manifest generation from ZIP without extraction — **not** claimed in Run 2.7.

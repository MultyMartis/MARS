# OCPilot — Baseline Promotion Strategy

**Purpose:** define how verified acquisition archives become **Reference Working Baselines** under `baselines/<version-folder>/files/` without replacing the canonical ZIP source.

**Run:** OCPilot Run 3.5 — Baseline Promotion  
**Status:** documented strategy; human-operated promotion only — **no** automation product claimed.

**Related:** [baselines/storage-policy.md](baselines/storage-policy.md), [archive-intake-rules.md](archive-intake-rules.md), [baseline-storage-model.md](baseline-storage-model.md), [intake-workflow.md](intake-workflow.md)

---

## Promotion chain

```
Acquisition ZIP
      ↓
Verified Archive          (Run 3: integrity, structure, version detection)
      ↓
Promoted Baseline         (Run 3.5: sanitized file tree in baselines/.../files/)
      ↓
Site Comparison           (Run 5+: read-only audit vs reference tree)
```

| Stage | Location | Role |
|-------|----------|------|
| **Acquisition ZIP** | `incoming/baselines/` | Operator-supplied artifact; immutable canonical source |
| **Verified Archive** | Same ZIP + manifest/passport metadata | Evidence that archive is readable, structured, and version-identified |
| **Promoted Baseline** | `baselines/<folder>/files/` | OpenCart-root-aligned reference tree for diff and audit |
| **Site Comparison** | Project site snapshots vs baseline | Classification per [baseline-comparison-methodology.md](baseline-comparison-methodology.md) |

---

## Why promoted baseline exists

| Need | How promoted baseline helps |
|------|----------------------------|
| **File-level comparison** | Auditors diff project sites against a stable local tree without re-extracting ZIP each run |
| **Repeatable scope** | Same paths, same version folder — comparison notes and manifests attach to one baseline identity |
| **Sanitization boundary** | Promotion is the gate where forbidden content is reviewed and excluded or documented before permanent reference use |
| **Operational speed** | Metadata alone (Run 3) proves acquisition; promoted tree (Run 3.5) enables Layers 1–4 comparison work |

Promoted baseline is **Reference Working Baseline** — not a deployment target, not a live store, not a substitute for production backups.

---

## Why ZIP remains canonical source

| Principle | Application |
|-----------|-------------|
| **Single authoritative artifact** | If promoted tree and manifest disagree, re-inspect ZIP |
| **Reproducibility** | Promotion can be repeated from ZIP with documented prefix strip (`upload-3038-rs2/` → `files/`) |
| **Integrity anchor** | SHA256 and entry counts recorded in Run 3 manifest refer to ZIP, not extracted copy |
| **No silent drift** | Edits to `files/` without ZIP update must be documented; ZIP is the reset point |
| **Storage policy** | See [baselines/storage-policy.md](baselines/storage-policy.md) — ZIP class remains **canonical** |

**Forbidden:** treating promoted `files/` as the only source; deleting or modifying incoming ZIP because extraction succeeded.

---

## Promotion procedure (Run 3.5 applied)

1. Confirm Run 3 manifest + passport exist for target baseline.
2. Run [baseline-sanitization-review.md](baseline-sanitization-review.md) against archive contents (before or during extract).
3. Extract **OpenCart Root** from Package Root — strip wrapper folder only:
   - `upload-3038-rs2/*` → `baselines/ocstore-3038-rs2/files/*`
   - `upload-3039-rs1/*` → `baselines/ocstore-3039-rs1/files/*`
4. **Do not** nest package folder inside `files/` (wrong: `files/upload-3038-rs2/admin`; correct: `files/admin`).
5. Populate `database/database-metadata-v1.md` from install artifacts — **metadata only**, no full dump promotion to `database/`.
6. Re-run [baseline-readiness-checklist.md](baseline-readiness-checklist.md).
7. Update passport readiness flags to match physical folder state.

---

## When baseline may be re-promoted

| Trigger | Action |
|---------|--------|
| **New canonical ZIP** | Operator replaces archive in `incoming/baselines/`; regenerate manifest, re-promote, new passport revision |
| **Sanitization policy change** | Re-extract from same ZIP with updated exclusion rules; document in sanitization review |
| **Promotion defect** | Wrong nesting, truncated extract, or corrupt tree — discard `files/`, re-promote from ZIP |
| **Manifest/ZIP mismatch** | Re-verify ZIP; if ZIP unchanged, re-promote; if ZIP changed, treat as new acquisition |
| **Operator explicit request** | Human charter to refresh reference tree without new acquisition |

Re-promotion **always** starts from canonical ZIP unless operator documents an exception.

---

## Run 3.5 promoted baselines

| Baseline folder | Canonical ZIP | Package prefix stripped | Files promoted |
|-----------------|---------------|-------------------------|----------------|
| `baselines/ocstore-3038-rs2/` | `opencart-3.0.3.8-rs.zip` | `upload-3038-rs2/` | 4055 |
| `baselines/ocstore-3039-rs1/` | `opencart-3.0.3.9-rs.zip` | `upload-3039-rs1/` | 3553 |

---

## SAFE UNKNOWN

- Operator retention policy for ZIP outside repo — not decided in Run 3.5.
- Whether future baselines use different wrapper folder names — detection rules in [archive-intake-rules.md](archive-intake-rules.md) apply per archive.
- Automated promotion pipeline — **not** claimed; human-operated Run 3.5 only.

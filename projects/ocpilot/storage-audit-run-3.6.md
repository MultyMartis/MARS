# OCPilot Run 3.6 — Baseline Storage Audit

**Date:** 2026-05-30  
**Run:** 3.6 — Baseline Storage Review  
**Method:** filesystem measurement on `projects/ocpilot/` (human-operated; no automation product claimed)

---

## Measurement scope

| Scope | Path pattern | Notes |
|-------|--------------|-------|
| Promoted vendor trees | `baselines/*/files/` | Sanitized OpenCart-root-aligned reference trees |
| Canonical ZIP archives | `incoming/baselines/*.zip` | Operator-supplied acquisition source |
| Baseline metadata | passports, manifests, database metadata, README, `.gitkeep` | Excludes `files/` bulk |
| Placeholder baselines | `baselines/opencart-*`, `ocstore-230`, `ocstore-3037`, `clean-opencart` | Skeleton only — no promoted bulk |

---

## Current state (measured 2026-05-30)

### Promoted baseline trees (READY)

| Baseline | Promoted files | Promoted size | Canonical ZIP | ZIP size |
|----------|----------------|---------------|---------------|----------|
| `ocstore-3038-rs2` | 4055 | 46.6 MB | `opencart-3.0.3.8-rs.zip` | 16.18 MB |
| `ocstore-3039-rs1` | 3553 | 48.9 MB | `opencart-3.0.3.9-rs.zip` | 16.29 MB |
| **Total (2 READY)** | **7608** | **95.5 MB** | **2 archives** | **32.5 MB** |

**Per-baseline averages (from 2 READY baselines):**

| Metric | Approximate value |
|--------|-------------------|
| Files per promoted baseline | ~3800 (range 3553–4055) |
| Promoted tree size | ~48 MB |
| Canonical ZIP size | ~16 MB |

### Baseline folder inventory

| Folder | Total files (incl. metadata) | Total size | Status |
|--------|-------------------------------|------------|--------|
| `ocstore-3038-rs2` | 4064 | 46.6 MB | READY — promoted |
| `ocstore-3039-rs1` | 3562 | 48.9 MB | READY — promoted |
| `opencart-230` | 7 | <0.1 MB | placeholder |
| `opencart-3037` | 7 | <0.1 MB | placeholder |
| `opencart-4x` | 7 | <0.1 MB | placeholder |
| `ocstore-230` | 7 | <0.1 MB | placeholder |
| `ocstore-3037` | 7 | <0.1 MB | placeholder |
| `clean-opencart` | 4 | <0.1 MB | legacy placeholder |

**Baseline folders:** 8 versioned + 1 legacy = **9 baseline roots**; **2** contain promoted vendor bulk.

### OCPilot totals

| Category | Files | Size |
|----------|-------|------|
| All OCPilot content | 7737 | 128.2 MB |
| Promoted vendor (`files/`) | 7608 | 95.5 MB |
| Metadata + docs (excl. `files/`) | 129 | ~32.7 MB* |
| Documentation-only (excl. ZIP) | 127 | ~0.2 MB |

\*The ~32.7 MB metadata bucket is dominated by the two canonical ZIP archives in `incoming/baselines/` (~32.5 MB). Human-authored OCPilot documentation is **small** (~0.2 MB).

### Git tracking state (evidence)

| Observation | Value |
|-------------|-------|
| `git ls-files -- projects/ocpilot` | **0** tracked files |
| `git status --short -uall -- projects/ocpilot` | **7735** untracked entries |

**Interpretation:** The entire OCPilot tree — including promoted baselines, ZIP archives, and metadata — is currently **untracked**. No baseline bulk has entered git history yet. This is a decision point, not a rollback requirement.

---

## Growth trajectory models

Assumptions (reasonable approximations — **not** fake precision):

- ~3800 promoted files and ~48 MB promoted tree per ocStore 3.x baseline
- ~16 MB canonical ZIP per baseline
- Placeholder/metadata overhead ~10 files and <0.1 MB per unfilled baseline folder
- Future OpenCart 4.x baselines may be larger — model uses same order of magnitude until measured
- Extension reference packages and comparison packs add variable bulk — not modeled numerically here (SAFE UNKNOWN per pack)

### Scenario table

| Scenario | READY baselines | Promoted files (est.) | Promoted size (est.) | ZIP size (est.) | OCPilot bulk total (est.) |
|----------|-----------------|----------------------|----------------------|-----------------|---------------------------|
| **Current** | 2 | 7608 | 95 MB | 33 MB | **~128 MB** |
| **2 baselines** | 2 | ~7600 | ~95 MB | ~33 MB | ~128 MB |
| **10 baselines** | 10 | ~38000 | ~480 MB | ~160 MB | **~640 MB** |
| **25 baselines** | 25 | ~95000 | ~1.2 GB | ~400 MB | **~1.6 GB** |
| **50 baselines** | 50 | ~190000 | ~2.4 GB | ~800 MB | **~3.2 GB** |

### Git impact if bulk were tracked (illustrative)

| Scenario | Untracked file entries (order of magnitude) | Risk |
|----------|---------------------------------------------|------|
| Current (2 READY) | ~7700 | Manageable locally; poor fit for git object model |
| 10 baselines | ~38000+ | Clone and diff noise; IDE indexing load |
| 25 baselines | ~95000+ | MARS repo dominated by vendor PHP/JS/CSS |
| 50 baselines | ~190000+ | Unsustainable as default MARS git content |

These estimates **exclude** project site snapshots, extension packs, and comparison pack archives — each would add separate bulk classes.

---

## Repository expansion risks

| Risk | Severity at 2 baselines | Severity at 25+ baselines | Notes |
|------|-------------------------|---------------------------|-------|
| **Git clone/fetch size** | Low (untracked today) | **High** if bulk committed | Vendor trees are many small files — poor git compression ratio |
| **Working tree indexing** | Moderate | **High** | IDEs and scanners traverse thousands of vendor files |
| **Duplicate storage** | Present | **Severe** | ZIP + promoted tree ≈ 3× logical baseline (archive + extract + metadata paths) |
| **Drift between ZIP and `files/`** | Low if re-promotion discipline holds | Moderate | Edits to promoted tree without ZIP update break comparison truth |
| **Operator sync burden** | Low | **High** if git-tracked | Every clone carries full vendor history |
| **MARS cross-project pollution** | Low today | **High** | OCPilot bulk would dwarf most documentation-only project folders |
| **Security surface** | Reviewed at Run 3.5 | Scales with count | More vendor trees = more paths to accidentally commit secrets into |

---

## Audit conclusions (Run 3.6)

1. **Two READY baselines are viable locally** (~128 MB OCPilot total) but **not** a pattern to scale into git by default.
2. **Promoted trees deliver comparison value** (Run 3.5 evidence) but **multiply storage** relative to canonical ZIP alone.
3. **Metadata is cheap; bulk is expensive** — 129 non-`files/` files vs 7608 promoted vendor files.
4. **Git decision is still open** — zero OCPilot files are tracked; policy can be set before first commit.
5. **Future baselines, 4.x, extension packs, and comparison packs** will accelerate growth unless storage class rules are enforced now.

---

## Related documents

| Doc | Role |
|-----|------|
| [storage-strategy-options.md](storage-strategy-options.md) | Option A–D evaluation |
| [recommended-storage-model.md](recommended-storage-model.md) | Selected canonical model |
| [git-storage-policy.md](git-storage-policy.md) | Git allow/deny list |
| [baselines/storage-policy.md](baselines/storage-policy.md) | Run 2.7 three-class policy (pre-promotion) |
| [baseline-promotion-strategy.md](baseline-promotion-strategy.md) | Run 3.5 promotion chain |

---

## SAFE UNKNOWN

- Exact size of future OpenCart 4.x baselines — not measured until acquisition.
- Extension reference package and comparison pack size distributions — depend on operator scope.
- Whether MARS-wide `.gitignore` patterns will be updated — out of scope for Run 3.6 (policy only).

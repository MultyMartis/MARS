# OCPilot — Baseline Storage Strategy Options

**Purpose:** evaluate long-term storage models for OCPilot baselines, extension reference material, and comparison packs.

**Run:** 3.6 — Baseline Storage Review  
**Status:** documented evaluation only — **no** implementation, **no** `.gitignore` changes in this run.

**Evidence base:** [storage-audit-run-3.6.md](storage-audit-run-3.6.md)

---

## Shared assumptions

| Assumption | Value |
|------------|-------|
| Canonical source | ZIP archive (per [baselines/storage-policy.md](baselines/storage-policy.md)) |
| Current READY baselines | 2 — `ocstore-3038-rs2`, `ocstore-3039-rs1` |
| Promoted tree value | Enables file-level diff without re-extract (Run 3.5) |
| MARS repo role | Documentation and operational metadata — not a vendor CDN |
| Git state today | Entire `projects/ocpilot/` untracked (0 files in git index) |

---

## Option A — ZIP + Promoted Trees + Git tracked

**Model:** Canonical ZIP, promoted `files/` trees, and all metadata committed to git.

### Pros

| Pro | Explanation |
|-----|-------------|
| **Full reproducibility on clone** | Any git clone contains complete comparison reference |
| **Audit trail in VCS** | Baseline bulk versioned alongside passports and manifests |
| **Simplest mental model** | «Everything is in the repo» |
| **No external dependency** | Comparison works offline immediately after clone |

### Cons

| Con | Explanation |
|-----|-------------|
| **Unsustainable at scale** | ~190k files / ~3 GB at 50 baselines (audit estimate) |
| **Poor git fit** | Thousands of small vendor files — slow status, diff, clone |
| **MARS size control failure** | OCPilot dominates repository; conflicts with survivability discipline |
| **Duplicate logical storage** | ZIP + full tree in same repo ≈ redundant bulk in history |
| **IDE and scanner load** | Every tool indexes full vendor trees |

### Operational impact

| Area | Impact |
|------|--------|
| Operator intake | Drop ZIP → promote → commit everything |
| Comparison (Run 5+) | Immediate — trees present after clone |
| New machine setup | Heavy clone; no separate baseline sync |
| Retention | Hard to prune — git history retains bulk |

### Recommended use

**Not recommended** as OCPilot default beyond a **small, explicitly chartered** set (e.g. 1–2 priority baselines) if human policy overrides size concerns. **Not** suitable for 10+ baselines, extension packs, or comparison pack archives.

---

## Option B — ZIP + Promoted Trees + Git ignored

**Model:** ZIP and promoted trees exist on disk under OCPilot paths but are **excluded from git**; metadata committed.

### Pros

| Pro | Explanation |
|-----|-------------|
| **Lean git history** | Passports, manifests, comparison notes versioned; bulk local only |
| **Preserves comparison workflow** | Active baselines keep local `files/` for diff tools |
| **Low migration cost from today** | Current untracked bulk maps naturally to gitignore pattern |
| **Grandfather friendly** | Run 3.5 promoted trees stay on disk unchanged |

### Cons

| Con | Explanation |
|-----|-------------|
| **Clone ≠ comparison-ready** | Fresh clone lacks baselines until operator restores bulk |
| **Machine-specific state** | Different operators may have different local baseline sets |
| **ZIP still on disk in repo path** | Local working tree still ~128 MB+ and growing |
| **Sync undefined** | Without external storage contract, baselines live only on one machine |
| **Partial solution** | Ignores git but not local MARS folder growth |

### Operational impact

| Area | Impact |
|------|--------|
| Operator intake | Promote locally; commit metadata only |
| Comparison (Run 5+) | Works on machine with promoted trees |
| New machine setup | Manual copy or re-promote from ZIP |
| Retention | Delete local `files/` without git history concern |

### Recommended use

**Acceptable short-term operator cache** for **active** baselines on a primary workstation. **Insufficient alone** as long-term canonical model — needs external ZIP storage and documented restore procedure (see Option D).

---

## Option C — ZIP + Metadata only + Temporary promotion

**Model:** Git and permanent storage hold metadata only; promoted `files/` exist briefly during intake or comparison, then removed.

### Pros

| Pro | Explanation |
|-----|-------------|
| **Strongest repo size control** | No permanent vendor bulk under `baselines/` |
| **Aligns with Run 2.7 policy** | [baselines/storage-policy.md](baselines/storage-policy.md) — «metadata over bulk» |
| **Single canonical artifact** | ZIP only; no drift from permanent extracted copy |
| **Scales to many baselines** | Metadata footprint grows slowly |

### Cons

| Con | Explanation |
|-----|-------------|
| **Comparison friction** | Re-extract before each file-level audit session |
| **Contradicts Run 3.5 outcome** | Demotes promoted trees that are already READY |
| **Operator time cost** | Repeated extract + sanitization checks |
| **Tooling assumptions** | Diff workflows expect stable local paths |
| **Incomplete for Run 5** | Read-only site audit against baseline slows down |

### Operational impact

| Area | Impact |
|------|--------|
| Operator intake | Extract → manifest → discard extract; keep ZIP + metadata |
| Comparison (Run 5+) | Promote temporarily to scratch path; delete after audit |
| New machine setup | Lightweight clone; extract on demand |
| Retention | No permanent `files/` — lowest local disk use |

### Recommended use

**Good default for inactive or archival baselines** and **good git policy** for bulk. **Poor sole model** for active comparison-heavy work unless operator accepts re-promotion cost every session.

---

## Option D — External baseline storage + Metadata in repo

**Model:** Canonical ZIP and optionally promoted trees live **outside** git-tracked MARS tree (operator NAS, external drive, object storage path documented in passport). Repo holds metadata, storage pointers, comparison notes, and policy.

### Pros

| Pro | Explanation |
|-----|-------------|
| **Best MARS size control** | Repo stays documentation-scale |
| **Scales to many baselines** | External store holds bulk; metadata scales linearly and slowly |
| **Clear separation of concerns** | Repo = operational truth; external = vendor artifacts |
| **Flexible retention** | Retire baselines externally without git rewrite |
| **Supports extension packs** | Large reference packages stay out of MARS |
| **Audit usefulness preserved** | Passport + manifest + comparison notes remain in repo |

### Cons

| Con | Explanation |
|-----|-------------|
| **External dependency** | Comparison requires baseline availability step |
| **Pointer discipline** | Passports must record external location, checksum, and revision |
| **Multi-operator sync** | Team needs shared external storage or restore playbook |
| **Not «clone and go»** | Onboarding includes baseline restore |
| **Policy enforcement human-only** | No automated storage product claimed |

### Operational impact

| Area | Impact |
|------|--------|
| Operator intake | Archive ZIP externally; record path + SHA256 in passport; optional local promote |
| Comparison (Run 5+) | Restore ZIP or promoted tree to local path; diff against project site |
| New machine setup | Clone repo (light) + restore active baselines from external store |
| Retention | External lifecycle managed by operator; repo metadata updated on retirement |

### Recommended use

**Preferred long-term canonical model** for OCPilot. Combines with **local promoted cache** (Option B pattern) for active baselines without committing bulk to git.

---

## Option comparison summary

| Criterion | A (git all) | B (ignore bulk) | C (temp only) | D (external) |
|-----------|-------------|-----------------|---------------|--------------|
| MARS size control | Poor | Moderate | Excellent | **Excellent** |
| Comparison speed | Excellent | Good | Poor | Good (with local cache) |
| Clone simplicity | Excellent | Poor | Excellent | Moderate |
| Scales to 25+ baselines | No | Partial | Yes | **Yes** |
| Aligns Run 2.7 metadata-first | No | Partial | **Yes** | **Yes** |
| Honors Run 3.5 promoted trees | Yes | Yes | Conflicts | Yes (local cache) |
| Operator workflow simplicity | Simple | Moderate | Tedious | Moderate |

---

## Decision input

See [recommended-storage-model.md](recommended-storage-model.md) for the **single selected model** and operational rules.

---

## SAFE UNKNOWN

- Exact external storage path convention — operator-defined; passport must record instance.
- Git LFS as variant of Option A — not evaluated; treated as still git-tracked bulk with different transport.
- Automated baseline restore — **not** claimed in Run 3.6.

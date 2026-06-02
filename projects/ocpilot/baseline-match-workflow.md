# OCPilot — Baseline Match Workflow

**Run:** 4 — First Project Site Intake  
**Purpose:** how OCPilot selects `ocstore-3038-rs2` or `ocstore-3039-rs1` (or rejects match) before read-only audit.  
**No assumptions** — every step requires evidence or **SAFE UNKNOWN**.

---

## Ready baselines (priority)

| Baseline folder | Version signal | Readiness |
|-----------------|----------------|-----------|
| `baselines/ocstore-3038-rs2/` | ocStore **3.0.3.8** (rs.2) | **READY** — [run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md) |
| `baselines/ocstore-3039-rs1/` | ocStore **3.0.3.9** (rs.1) | **READY** — [run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md) |

Other versioned baselines under [baselines/](baselines/README.md) exist as placeholders or older reference — **not** default for current operator targets.

---

## Workflow

```
Detect version
      ↓
Validate evidence
      ↓
Match baseline
      ↓
Record decision
      ↓
Proceed to audit (Run 5+)
```

---

## Step 1 — Detect version

Collect **independent** signals (any one insufficient alone):

| Source | What to extract |
|--------|-----------------|
| `index.php` / `admin/index.php` | `VERSION` constant |
| Operator brief | Stated ocStore/OpenCart line and rs build |
| Admin footer / about | Platform string (ocStore vs OpenCart) |
| Archive root (if materials received) | Package layout per [archive-intake-rules.md](archive-intake-rules.md) |

**Output:** proposed `Platform` + `Version` + rs build (if ocStore).

If signals conflict → **SAFE UNKNOWN**; do not match baseline yet.

---

## Step 2 — Validate evidence

| Check | Pass criterion |
|-------|----------------|
| Platform identified | `OpenCart` or `ocStore` with cited source |
| Version line identified | e.g. `3.0.3.8` or `3.0.3.9` with file or operator citation |
| rs build (ocStore) | rs.2 / rs.1 confirmed or **SAFE UNKNOWN** |
| Wrong family | OpenCart-only site must **not** use ocStore baseline without explicit charter |
| Baseline readiness | Target baseline passes [baseline-readiness-checklist.md](baseline-readiness-checklist.md) |

**Stop conditions:**

- Version unknown → record SAFE UNKNOWN; baseline match deferred.
- Version known but no READY baseline folder → request acquisition (Run 3 path) or charter; **no** silent substitute.
- Evidence suggests version **between** 3038 and 3039 without pin → SAFE UNKNOWN; operator must confirm.

---

## Step 3 — Match baseline

**Decision table (current operator targets):**

| Detected version | rs build | Matched baseline |
|------------------|----------|------------------|
| ocStore 3.0.3.8 | rs.2 (or consistent with 3038-rs2 package) | `baselines/ocstore-3038-rs2/` |
| ocStore 3.0.3.9 | rs.1 (or consistent with 3039-rs1 package) | `baselines/ocstore-3039-rs1/` |
| ocStore 3.0.3.8 | rs build SAFE UNKNOWN | **SAFE UNKNOWN** — do not assume 3038-rs2 |
| ocStore 3.0.3.9 | rs build SAFE UNKNOWN | **SAFE UNKNOWN** — do not assume 3039-rs1 |
| Any other line | — | **No match** — use correct baseline folder or acquire |

**Cross-version rule:** A site on 3.0.3.9 must **not** be compared against `ocstore-3038-rs2`. Cross-version notes ([comparison-notes/3038-vs-3039-structured-review-v1.md](comparison-notes/3038-vs-3039-structured-review-v1.md)) are for baseline understanding only.

---

## Step 4 — Record decision

Record in:

1. `sites/<slug>/site-passport.md` — field **Baseline Match**
2. [project-site-registry.md](project-site-registry.md) — **Baseline** column
3. `sites/<slug>/opencart-analysis/` — short evidence note (when folder populated)
4. `sites/<slug>/safe-unknown/` — if match blocked

**Decision record minimum:**

| Field | Example |
|-------|---------|
| Matched baseline | `baselines/ocstore-3038-rs2/` or `SAFE UNKNOWN` |
| Evidence sources | `index.php VERSION`, operator brief date |
| Reviewer | human operator / OCPilot assist |
| Run reference | e.g. Run 4 intake / Run 5 pre-audit |

---

## Step 5 — Proceed to audit

Baseline match is **necessary** but not **sufficient** for Run 5.

Before **First Read-Only Site Audit** (Run 5):

- Complete [intake-readiness-review.md](intake-readiness-review.md)
- Confirm materials and storage exist
- Confirm no forbidden-path operations (FTP write, admin change, etc.) in scope

Comparison method: [baseline-comparison-methodology.md](baseline-comparison-methodology.md).

---

## SAFE UNKNOWN triggers

- VERSION constant not accessible (no files yet)
- Operator brief missing or ambiguous
- ocStore vs OpenCart unclear
- rs build not confirmed for 3038/3039 line
- Site files suggest customized core without version pin

---

## Related documents

- [project-sites-workflow.md](project-sites-workflow.md) — Baseline Selection section
- [baseline-readiness-checklist.md](baseline-readiness-checklist.md)
- [comparison-notes/3038-vs-3039-structured-review-v1.md](comparison-notes/3038-vs-3039-structured-review-v1.md)

# Run 3 — Initial Baseline Comparison Notes

**Purpose:** initial cross-baseline comparison after first archive intake (OCPilot Run 3).  
**Date:** 2026-05-30  
**Scope:** `opencart-3.0.3.8-rs.zip` → `ocstore-3038-rs2` vs `opencart-3.0.3.9-rs.zip` → `ocstore-3039-rs1`  
**Method:** ZIP listing + selective file extract for version constants only; **no** full diff executed.

---

## Detected platform

| Baseline | Archive | Detected platform | Evidence |
|----------|---------|-------------------|----------|
| `ocstore-3038-rs2` | `opencart-3.0.3.8-rs.zip` | **ocStore** | `upload-3038-rs2/` folder; `ru-ru/` pack (348 paths); `tweak.ocmod.xml`, `tweak-54fz.ocmod.xml`; operator Run 3 brief |
| `ocstore-3039-rs1` | `opencart-3.0.3.9-rs.zip` | **ocStore** | `upload-3039-rs1/` folder; same ocStore signals as 3038-rs2 |

Neither archive is treated as vanilla upstream OpenCart — both are classified as **ocStore** distributions.

---

## Detected version

| Baseline | VERSION constant (verified) | rs build label | Archive filename |
|----------|----------------------------|----------------|------------------|
| `ocstore-3038-rs2` | `3.0.3.8` (`index.php`, `admin/index.php`) | rs.2 (from `upload-3038-rs2/`) | `opencart-3.0.3.8-rs.zip` |
| `ocstore-3039-rs1` | `3.0.3.9` (`index.php`, `admin/index.php`) | rs.1 (from `upload-3039-rs1/`) | `opencart-3.0.3.9-rs.zip` |

rs build numbers are inferred from package folder names — **not** independently verified against ocstore.com release metadata.

---

## Structural similarities

Both archives share:

- Single top-level Package Root matching OpenCart Root (no extra nesting).
- Pre-install vendor layout: `install/` present; root `config.php` absent; `config-dist.php` present (0 bytes).
- Core directory set: `admin/`, `catalog/`, `image/`, `system/`.
- ocStore OCMOD pair: `system/tweak.ocmod.xml`, `system/tweak-54fz.ocmod.xml`.
- Russian locale pack: 348 `ru-ru/` paths each.
- Nested `deleted-files.zip` inside package root.
- Placeholder cache/session stubs only (no live cache/session payload detected).
- `install/opencart.sql` present (similar size ~193 KB).

---

## Known differences (listing-level, not full diff)

| Area | ocstore-3038-rs2 | ocstore-3039-rs1 | Notes |
|------|------------------|------------------|-------|
| Package folder | `upload-3038-rs2/` | `upload-3039-rs1/` | rs suffix differs |
| VERSION | 3.0.3.8 | 3.0.3.9 | Verified in PHP |
| ZIP total entries | 4744 | 4190 | Archive-level |
| Files under Package Root | ~4055 | ~3553 | Listing count |
| `admin/` files | 1300 | 1313 | +13 in 3039 |
| `catalog/` files | 615 | 616 | +1 in 3039 |
| `system/` files | 1912 | 1391 | **−521 in 3039** — significant; root cause **SAFE UNKNOWN** without file-level diff |
| `install/` files | 112 | 117 | +5 in 3039 |
| `image/` files | 110 | 110 | same count |
| `deleted-files.zip` size | 1 190 104 B | 1 084 625 B | differs |
| `install/opencart.sql` size | 192 868 B | 193 177 B | minor delta |
| `wechat` path matches | 29 | 105 | vendor tree difference noted in listing |

No file-by-file diff was performed in Run 3 — counts and notable paths only.

---

## ocStore vs upstream OpenCart

**SAFE UNKNOWN** for both baselines.

Repo lacks pinned upstream OpenCart 3.0.3.8 / 3.0.3.9 clean baselines for subtraction. Future work: acquire upstream OpenCart baselines or vendor release notes before claiming ocStore-specific core deltas.

---

## Future comparison considerations

1. **Operator approval gate** — promote sanitized trees to `files/` before Layer 1+ file comparison ([baseline-comparison-methodology.md](../baseline-comparison-methodology.md)).
2. **Resolve 0-byte `config-dist.php`** — confirm vendor intent before sanitization template selection.
3. **Investigate `system/` file-count delta** — 3038-rs2 vs 3039-rs1 (−521 files) may reflect vendor pruning, dependency changes, or packaging differences; requires structured diff.
4. **Parse `install/opencart.sql` metadata** — optional schema metadata for DB layer (human-reviewed; no auto-import).
5. **Inspect nested `deleted-files.zip`** — may document removed upstream files per ocStore build.
6. **Document ocStore-known deltas** — move verified findings into each baseline's `comparison-notes/` when upstream reference exists.
7. **Site audit baseline selection** — match project site VERSION + rs build to correct priority baseline (`3038-rs2` vs `3039-rs1`); wrong version invalidates audit.
8. **Source verification** — operator may supply official ocStore download URL and vendor checksum in Run 4+.

---

## SAFE UNKNOWN

- Exact file-level diff between 3038-rs2 and 3039-rs1.
- Exact ocStore-vs-upstream OpenCart deltas per version.
- Semantic meaning of rs.1 vs rs.2 beyond folder naming.
- Whether archive filename prefix `opencart-` reflects historical naming only or mixed lineage.

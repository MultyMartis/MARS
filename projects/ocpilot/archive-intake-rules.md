# OCPilot — Archive Intake Rules

**Purpose:** define how OCPilot interprets baseline ZIP archives — distinguishing **Archive Root**, **Package Root**, and **OpenCart Root** — and how to detect each without assuming OpenCart files sit at ZIP root.

**Status:** documented rules only; **no** archive import or extraction in Run 2.7.

**Related:** [baselines/storage-policy.md](baselines/storage-policy.md), [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md), [intake-workflow.md](intake-workflow.md)

---

## Three distinct concepts

These terms are **not interchangeable**.

| Term | Definition | Example |
|------|------------|---------|
| **Archive Root** | Top-level entries inside the ZIP file (files and directories as listed by archive inspection) | `upload-3038-rs2/` as sole top-level directory |
| **Package Root** | The directory (or path) that represents the vendor distribution bundle — may wrap the OpenCart tree | `upload-3038-rs2/` |
| **OpenCart Root** | The directory containing OpenCart/ocStore core layout: `admin/`, `catalog/`, `system/`, `image/`, `config.php`, `index.php`, etc. | Often **same as Package Root** for ocStore upload bundles; may differ in other archive formats |

**Critical rule:** OCPilot **must not** assume OpenCart files exist at Archive Root. Always walk: ZIP → Archive Root → Package Root detection → OpenCart Root detection.

---

## Workflow

```
ZIP archive
    ↓
Archive Root          (list top-level entries in ZIP)
    ↓
Package Root Detection   (identify vendor bundle folder)
    ↓
OpenCart Root Detection  (locate core OpenCart/ocStore file tree)
    ↓
Version identification + intake report
```

Each step must complete successfully or stop with **SAFE UNKNOWN** and request operator clarification — see [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md).

---

## Step 1 — Archive Root

**Archive Root** = the immediate children of the ZIP container.

| Inspection action | Notes |
|-------------------|-------|
| List top-level entries | Files and directories only; do not execute contents |
| Count top-level directories | Single-directory archives are common for ocStore upload bundles |
| Note stray top-level files | README, license, install docs at Archive Root may indicate multi-root layout |
| Record in intake report | Archive Root listing is mandatory evidence |

**Do not** treat Archive Root as OpenCart Root without detection rules below.

---

## Step 2 — Package Root detection

**Package Root** = the folder that contains (or wraps) the distributable OpenCart/ocStore upload tree.

### Detection rules

| Rule | Action |
|------|--------|
| **Single top-level directory** | If archive contains **exactly one** top-level directory → **inspect that directory first** as primary Package Root candidate |
| **Multiple top-level entries** | Inspect each directory candidate; look for OpenCart markers; **SAFE UNKNOWN** if ambiguous |
| **Flat archive (no wrapper folder)** | If `admin/`, `catalog/`, etc. appear directly at Archive Root → Archive Root **may** equal Package Root **and** OpenCart Root — verify with OpenCart Root rules |
| **Nested wrappers** | If single top-level dir contains another single dir before OpenCart markers → inner directory may be Package Root; document path chain |

### Real examples (operator baseline archives — Run 3)

These are **valid Package Root candidates** documented from operator-provided archive structure:

| Archive | Archive Root (top level) | Package Root candidate |
|---------|--------------------------|------------------------|
| `opencart-3.0.3.8-rs.zip` | `upload-3038-rs2/` | `upload-3038-rs2/` |
| `opencart-3.0.3.9-rs.zip` | `upload-3039-rs1/` | `upload-3039-rs1/` |

Expected contents under each Package Root:

```
upload-3038-rs2/          upload-3039-rs1/
  admin/                    admin/
  catalog/                  catalog/
  image/                    image/
  system/                   system/
  config.php                config.php
  index.php                 index.php
  ...                       ...
```

**Warning:** Future archives may use different folder names (`upload/`, versioned paths, multilingual docs siblings, etc.). Detection rules apply; **folder names are not proof** of version or authenticity.

---

## Step 3 — OpenCart Root detection

**OpenCart Root** = directory where OpenCart/ocStore core install layout is rooted.

### Detection rules

Inspect candidate directory (usually Package Root after single-top-level-dir rule):

| Marker | Required for OpenCart Root? |
|--------|----------------------------|
| `admin/` | Expected |
| `catalog/` | Expected |
| `system/` | Expected |
| `image/` | Expected |
| `config.php` | Expected (may contain placeholders — treat as credential risk) |
| `index.php` | Expected |

**Rule:** If `admin/`, `catalog/`, `system/`, `image/`, `config.php`, and `index.php` are detected together in the same directory → treat that directory as **OpenCart Root**.

| Outcome | Action |
|---------|--------|
| All markers present | Record OpenCart Root path relative to Archive Root; proceed to version identification |
| Partial markers | **SAFE UNKNOWN** — may be incomplete archive, wrong folder, or non-standard layout; stop and ask operator |
| Markers in nested subfolder | OpenCart Root = nested path; Package Root may be outer wrapper — document both |
| Multiple directories each with partial markers | **SAFE UNKNOWN** — do not guess; request operator clarification |

### OpenCart Root ≠ Archive Root (common case)

For operator Run 3 archives:

```
Archive Root:     upload-3038-rs2/
OpenCart Root:    upload-3038-rs2/     (same path — no extra nesting)

NOT:

Archive Root:     admin/, catalog/, ...   ← wrong assumption for these ZIPs
```

For other archive formats, OpenCart Root may be `upload/admin/...` or deeper — **always inspect**, never assume.

---

## Mapping to baseline destinations

After OpenCart Root and version are identified:

| Detected target | Recommended baseline folder |
|-----------------|----------------------------|
| ocStore 3.0.3.8 (rs.2) | `baselines/ocstore-3038-rs2/` |
| ocStore 3.0.3.9 (rs.1) | `baselines/ocstore-3039-rs1/` |
| Other version/platform | Match to existing version folder or **reject** per [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) |

Filename alone (e.g. `opencart-3.0.3.8-rs.zip`) is **declared identity**, not verified version — confirm via file tree metadata and operator brief.

---

## Forbidden assumptions

| Forbidden assumption | Correct stance |
|---------------------|----------------|
| OpenCart files at ZIP root | Inspect Archive Root first |
| Filename equals version | Verify via tree + passport |
| Single top-level folder is always OpenCart Root | It is a **candidate** — confirm markers |
| All ocStore archives use `upload-XXXX-rsN/` naming | Documented examples only; future archives may differ |
| Package Root equals OpenCart Root always | Often true for upload bundles; verify each time |

---

## Intake integration

These rules apply during:

1. [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md) — before full intake
2. [intake-workflow.md](intake-workflow.md) — steps 2–5 (source, version, readiness pre-check, destination)
3. [templates/intake-report-template.md](templates/intake-report-template.md) — record Archive Root, Package Root, OpenCart Root paths

OCPilot **must inspect archive structure first** before any extraction, rename, or move — see [incoming/baselines/README.md](incoming/baselines/README.md).

---

## Related documents

| Doc | Role |
|-----|------|
| [baselines/storage-policy.md](baselines/storage-policy.md) | ZIP canonical; extract temporary |
| [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md) | Stop/go checklist |
| [run-3-preparation.md](run-3-preparation.md) | Run 3 operator and agent tasks |
| [quarantine-policy.md](quarantine-policy.md) | Stop conditions |

---

## SAFE UNKNOWN

- Exact internal paths for archives not yet placed in `incoming/baselines/` — verified only during Run 3 inspection.
- Whether future official OpenCart releases will match ocStore upload-folder convention — **not** assumed.
- Automated detection tooling — **not** claimed; human-operated inspection with agent assistance only.

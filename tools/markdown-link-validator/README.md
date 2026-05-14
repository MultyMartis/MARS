# PILOT 03 — Markdown link validator (local helper)

**Status:** experimental pilot under `tools/`. **Not** link integrity enforcement, **not** governance enforcement, **not** CI truth, **not** orchestration, **not** runtime monitoring.

**Purpose:** Read-only, explicit-invocation hints to help humans spot likely broken **relative** local markdown targets, optional **heuristic** `#anchor` checks, and a few **low-severity** fragment oddities.

**Governance alignment (minimal):**

- [operational-tooling-overview.md](../../governance/operational-tooling-overview.md) — S5 tooling boundaries and human-operated helpers  
- [helper-stabilization-rules.md](../helper-stabilization-rules.md) — narrow scope, anti–pseudo-runtime drift  
- [operational-experiments-overview.md](../../governance/operational-experiments-overview.md) — S7 experiment framing  
- [reality-audit-framework.md](../../governance/reality-audit-framework.md) — evidence / honesty posture for operational claims  

---

## Behavior (what it does)

- Recursively finds markdown files under `--root` (default: current working directory).  
- Parses **inline** links/images `(...)` and **reference-style** link targets on `]:` lines (simple pattern).  
- Skips obvious non-local targets (`http(s):`, `mailto:`, `data:`, `//…`, Windows `C:\…`-style).  
- Resolves relative file paths from the **source** markdown file’s directory; optional **extension inference** for extensionless paths (see `validator-config.json`).  
- If the path resolves to an **existing directory** (e.g. trailing `/` folder links), it is **not** reported as a missing file (directory targets are skipped; this is not an endorsement of folder links as stable APIs).
- Prints each hint: file path (relative to root), line, raw link, issue type, severity (from config).  
- Ends with a short summary.  
- **Stdout only** for normal report; **stderr** only for fatal usage errors (bad root).  
- **No** file writes, **no** auto-fix, **no** cache, **no** watchers, **no** background work, **no** sync.

---

## What it does **not** do (non-goals)

- Prove global link integrity or replace human review.  
- Understand HTML `<a href>`, autolinks, footnotes, or every markdown dialect edge case.  
- Match GitHub/CommonMark anchor algorithms exactly (unicode, duplicate headings, HTML `id=`).  
- Validate URLs, query strings, or workspace-external trees unless the resolved path exists as a file.  
- Rewrite, normalize, or “repair” links.

---

## False positives and SAFE UNKNOWN

- Anchor checks use **heading-derived slugs only** (heuristic). Custom HTML anchors, repeated headings, and renderer-specific slug rules → **false positives and misses**.  
- Reference-definition parsing is **intentionally minimal**; unusual whitespace or titles can be missed or misparsed.  
- **SAFE UNKNOWN:** absence of reported issues does **not** prove all links are valid; presence of an issue is a **triage hint**, not a verdict.

---

## Configuration

See [validator-config.json](validator-config.json): excluded directory names, markdown extensions, optional `.md` inference flag, severity labels, pilot status note.

---

## Usage

From repository root (examples use PowerShell paths as needed):

```bash
node tools/markdown-link-validator/markdown-link-validator.js --help
```

Dry-run (no link checks; shows scan posture):

```bash
node tools/markdown-link-validator/markdown-link-validator.js --root governance --dry-run
```

Default scan (missing local targets only; anchors off):

```bash
node tools/markdown-link-validator/markdown-link-validator.js --root governance
```

Include heuristic anchor hints (noisier):

```bash
node tools/markdown-link-validator/markdown-link-validator.js --root governance --check-anchors
```

---

## Issue types (overview)

| type | intent |
|------|--------|
| `missing_target_file` | Relative path does not resolve to an existing file (with configured inference rules). |
| `missing_target_file_inferred_md` | Same, after extension inference was applicable (still a missing target). |
| `missing_same_file_anchor` | `#fragment` in same file; slug not found among extracted headings (`--check-anchors`). |
| `missing_cross_file_anchor` | `path.md#fragment` resolved, but slug not found in target (`--check-anchors`). |
| `suspicious_fragment` | Low-severity fragment oddities (e.g. unusual characters with anchors on, or doubled spaces in fragment-only links). |

---

## Risks

- Misinterpreted output could drive unnecessary edits — treat as **hints** only.  
- Large trees produce large stdout; this is **manual** triage, not streaming telemetry.

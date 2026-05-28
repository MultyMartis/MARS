# ORCA DOCX Export Pilot v1

## Status

**Pilot — human-triggered local helper.** First operational bridge from ORCA semantic content packs to operator-grade DOCX for Website Factory handoff.

## What this is

| Property | Value |
|----------|--------|
| Trigger | Human operator runs `npm run export` or `node scripts/export-content-pack-docx.js` |
| Runtime | None — single Node.js process, exits when done |
| Approvals | **Not** granted by export; gates are **snapshotted** only |
| Semantic lock | **MODE 1** — export preserves locked copy; Factory may not rewrite |

## What this is NOT

- Not a daemon, queue, scheduler, or orchestration layer
- Not autonomous post-approval export
- Not a replacement for Commander XLSX exporter (`ppc/.../exporter-cli/`)
- Not governance or validation enforcement

## Pipeline

```
ORCA content pack (.md)
    → docx-pilot (this folder)
    → operator DOCX review
    → Website Factory implementation (presentation only)
    → operator launch / ads approval (separate gates)
```

## Relationship to Website Factory

DOCX is the **human-readable sign-off artifact**. Website Factory implements **presentation** (layout, partials, anchors, form wiring) against the same semantic pack. Under **MODE 1 semantic lock**, approved headlines, specs, CTAs, and denial lists must not be paraphrased by Factory tooling.

## Relationship to semantic lock (MODE 1)

When `semantic_lock: active` and `content_mode: MODE_1` in pack frontmatter:

- Export includes lock markers per section
- SAFE UNKNOWN blocks are never stripped or auto-resolved
- Factory implementation notes are emitted as a dedicated section

## Quick start

```bash
cd projects/orca/content-packs/exporters/docx-pilot
npm install
npm run export:pilot
```

Output: `output/triumph-manipulyator-5-tonn-pack-v1.docx`

## Documents

| File | Purpose |
|------|---------|
| [DOCX-PILOT-ARCHITECTURE-v1.md](DOCX-PILOT-ARCHITECTURE-v1.md) | Component layout |
| [EXPORT-RUNBOOK-v1.md](EXPORT-RUNBOOK-v1.md) | Install, run, verify |
| [STYLE-GUIDE-v1.md](STYLE-GUIDE-v1.md) | Visual / Word conventions |
| [SAFE-UNKNOWN-RULES-v1.md](SAFE-UNKNOWN-RULES-v1.md) | UNKNOWN handling |
| [validation/export-checklist-v1.md](validation/export-checklist-v1.md) | Post-export QA |

## Boundary

Local helper tooling under `projects/orca/` only. Does not modify `governance/`, `mars-runtime/`, or existing PPC exporter CLI.

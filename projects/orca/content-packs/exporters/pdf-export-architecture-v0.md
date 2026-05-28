# PDF Export Architecture v0

## Status

**FUTURE LAYER** — not implemented in v0.

## Role

PDF is the planned **client-ready** presentation layer for strategy/content delivery, generated **only** from:

1. Approved DOCX revision (`approved_for_client_export`), or
2. Locked Markdown with explicit client export gate

## Principles

| Rule | Rationale |
|------|-----------|
| No PDF from `draft` packs | Prevents accidental client send |
| No direct PDF from live HTML | HTML is Factory output — pack is semantic SoT |
| Redaction pass required | Strip internal factory notes and operator comments |
| Preserve semantic lock markers | Client sees same claims as DOCX |

## Proposed pipeline (future)

```
approved pack → DOCX (signed) → PDF render → redaction checklist → client-ready
```

## Formatting

- Inherit DOCX heading hierarchy
- CTA blocks as bordered boxes
- Metadata on cover page (pack_id, version, date) — no internal repo paths unless operator opts in

## Gate

Requires `approved_for_client_export` on pack envelope.

Maps to global ORCA `approved_for_client_pdf` where PDF is audit/strategy delivery — document mapping in approval file.

## SAFE UNKNOWN

- PDF tooling choice (LibreOffice headless, commercial API, etc.) — **not selected in v0**
- Digital signature requirements — operator charter

## Boundary

Future architecture stub only.

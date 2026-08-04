# LEAD QUALITY MODEL v1 — Phase 3E.1

**Harness:** H22–H24, H26

## Status values

| Status | Meaning |
|--------|---------|
| `sufficient` / `ok` | enough to contact + service-aware facts OK |
| `needs_clarification` / `needs_data` | contact OK but missing service facts |
| `bad` | damaged / missing primary contact |

## Rules

- Explicit no-site + WebsiteDevelopment can still be **sufficient** (do not force site URL).
- Damaged phone/email placeholders → insufficient / bad.
- Probable test names flagged separately (`is_probable_test`) without destroying the name value.
- Missing-information lists are **service-aware** (e.g. business type / functionality for site build).

Interim Sheets packing may append quality notes into `quality_comment` until additive columns land (see STORAGE-MIGRATION-v1).

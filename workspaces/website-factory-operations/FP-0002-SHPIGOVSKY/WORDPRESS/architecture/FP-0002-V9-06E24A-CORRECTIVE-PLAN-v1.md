# FP-0002 V9-06E24A Corrective Plan

**Wave:** V9-06E24A  
**Method:** **A — make optional**

## Decision

Keep `programme_items` in admin and on frontend. Harden optional semantics so title-only or empty rows never block service save.

## Components

| Component | Decision | Reason |
|---|---|---|
| `field_fp02_programme_items_service` | `required=0` + optional instructions | Programme block is optional; static fallback exists |
| Subfields `title`, `text` | explicit `required=0` + instructions | Partial rows (title without text) are valid editorial state |
| `RepeaterValidation::validate_optional_programme_items` | ACF filter returns true | Defensive guard against spurious repeater validation |
| ACF JSON + DB | Resync from PHP source authority | Remove DB/JSON drift vs plugin registration |

## Not in scope

- Remove/deactivate field (Method B) — rejected; field is USED_FRONTEND
- Service content migration
- Hero CTA architecture changes
- Global `Герои` settings

Evidence: `validation/v9-06e24a-service-structured-sections-required-field-polish/corrective-plan.json`

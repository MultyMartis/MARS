# FP-0002 V9-06E24A Correction Result

**Wave:** V9-06E24A  
**Method:** A

## Changes

| Item | Before | After |
|---|---|---|
| `programme_items` required | 0 | 0 (explicit + instructions) |
| Subfield `title` required | 0 | 0 (explicit + instructions) |
| Subfield `text` required | 0 | 0 (explicit + instructions) |
| Validation filter | absent | `validate_optional_programme_items` |
| ACF JSON | generic repeater instructions | optional programme instructions synced from PHP |

## Source files

- `plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `plugins/shpigovsky-core/src/Fields/RepeaterValidation.php`
- `acf-json/group_fp02_service_structured_sections.json`

## Service content

No postmeta content writes. Existing programme rows on services 73/74 unchanged.

Evidence: `validation/v9-06e24a-service-structured-sections-required-field-polish/correction-result.json`

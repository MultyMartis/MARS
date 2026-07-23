# Importer category resolution precedence

1. **GUID mapping table** — if source_group_id mapped → use category_id.
2. **Full source path match** — normalize 1C path names ↔ OC path names under tech tree; if unique match → use and optionally backfill GUID map.
3. **Create under resolved parent** — if parent resolved and leaf missing → auto-create (see design) → map.
4. **Collision guard** — block leaf-name match into legacy when source parent/path differs (esp. 154/159/165).
5. **Leaf-name-only** — **not** auto-assign; emit CATEGORY_MAPPING_REVIEW_REQUIRED (low confidence).

## Explicit bans

- Ban: mb_strtolower(name) → category_id global index as sole matcher.
- Ban: attaching tech-source leaf to legacy 154/159/165 by name.

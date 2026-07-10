# FP-0002 V9-06E29B-FIX2C Implementation Result

Split legacy `group_fp02_page_institutional` into:

- `group_fp02_page_ocentre_hub` — page #11 location rule
- `group_fp02_page_institutional_child` — pages #12–#16 + institutional template

Removed invalid field conditional logic (`param: page`).

Deleted 9 duplicate institutional DB groups; imported 2 canonical groups.

Source files: `FieldGroups.php`, hub/child ACF JSON.

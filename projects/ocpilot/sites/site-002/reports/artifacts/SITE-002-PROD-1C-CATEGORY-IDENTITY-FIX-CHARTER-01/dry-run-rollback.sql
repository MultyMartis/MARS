-- DRY RUN ONLY — DO NOT APPLY
-- Rollback mapping persistence (does not restore product relations; keep reparent rollback separate)

DROP TABLE IF EXISTS oc_mars_1c_category_map;

-- If importer code deployed: restore previous import_1C.php from backup artifact.
-- Product relations rollback: use SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01 rollback.sql only if needed.

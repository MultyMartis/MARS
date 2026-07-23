-- DRY RUN ONLY — DO NOT APPLY
-- SITE-002-PROD-CATALOG-STRUCTURE-FORENSIC-01
-- Proposed visibility cleanup candidates (HITL required)

-- Empty tech elektro hub (category_id=375): optional disable AFTER confirming
-- whether 1C child Хлеборезки should be created under it instead.
-- UPDATE oc_category SET status=0, date_modified=NOW() WHERE category_id=375;
-- ROLLBACK: UPDATE oc_category SET status=1 WHERE category_id=375;

-- DO NOT disable 153/159 while products remain.

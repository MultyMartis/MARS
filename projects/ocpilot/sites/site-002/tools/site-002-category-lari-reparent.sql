-- SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01
-- Sanitized apply plan (no credentials). Prefix: oc_
-- Applied on production 2026-07-09 after dry-run gates.

START TRANSACTION;

UPDATE oc_category SET parent_id = 358, date_modified = NOW() WHERE category_id = 88;

DELETE FROM oc_category_path WHERE category_id IN (88, 140, 141);

INSERT INTO oc_category_path (category_id, path_id, level) VALUES
(88, 79, 0), (88, 358, 1), (88, 88, 2),
(140, 79, 0), (140, 358, 1), (140, 88, 2), (140, 140, 3),
(141, 79, 0), (141, 358, 1), (141, 88, 2), (141, 141, 3);

COMMIT;

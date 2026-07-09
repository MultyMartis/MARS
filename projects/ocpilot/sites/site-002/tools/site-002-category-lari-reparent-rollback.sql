-- ROLLBACK SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01
-- Restore pre-reparent parent_id and category_path for IDs 88, 140, 141.

START TRANSACTION;

UPDATE oc_category SET parent_id = 79, date_modified = NOW() WHERE category_id = 88;

DELETE FROM oc_category_path WHERE category_id IN (88, 140, 141);

INSERT INTO oc_category_path (category_id, path_id, level) VALUES
(88, 79, 0), (88, 88, 1),
(140, 79, 0), (140, 88, 1), (140, 140, 2),
(141, 79, 0), (141, 88, 1), (141, 141, 2);

COMMIT;

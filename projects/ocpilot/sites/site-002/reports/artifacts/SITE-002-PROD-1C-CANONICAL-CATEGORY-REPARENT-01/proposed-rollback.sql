-- DRY RUN ONLY — DO NOT APPLY MANUALLY WITHOUT THIS OPERATION GATES
-- SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01 / OCPilot 4.290
-- generated 2026-07-23T11:42:12Z
-- Exact product_id/category_id only. No category delete/disable.

START TRANSACTION;
INSERT IGNORE INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4707, 154, 1);
DELETE FROM oc_product_to_category WHERE product_id=4707 AND category_id=373;
UPDATE oc_product_to_category SET main_category=0 WHERE product_id=4707;
UPDATE oc_product_to_category SET main_category=1 WHERE product_id=4707 AND category_id=154;
INSERT IGNORE INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4708, 154, 1);
DELETE FROM oc_product_to_category WHERE product_id=4708 AND category_id=373;
UPDATE oc_product_to_category SET main_category=0 WHERE product_id=4708;
UPDATE oc_product_to_category SET main_category=1 WHERE product_id=4708 AND category_id=154;
INSERT IGNORE INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4710, 159, 1);
DELETE FROM oc_product_to_category WHERE product_id=4710 AND category_id=373;
UPDATE oc_product_to_category SET main_category=0 WHERE product_id=4710;
UPDATE oc_product_to_category SET main_category=1 WHERE product_id=4710 AND category_id=159;
INSERT IGNORE INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712, 165, 1);
DELETE FROM oc_product_to_category WHERE product_id=4712 AND category_id=375;
UPDATE oc_product_to_category SET main_category=0 WHERE product_id=4712;
UPDATE oc_product_to_category SET main_category=1 WHERE product_id=4712 AND category_id=165;
-- COMMIT;
ROLLBACK;

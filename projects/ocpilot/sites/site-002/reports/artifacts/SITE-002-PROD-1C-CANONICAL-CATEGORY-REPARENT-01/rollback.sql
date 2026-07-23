-- SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01 ROLLBACK
-- 2026-07-23T11:43:55Z
START TRANSACTION;
DELETE FROM oc_product_to_category WHERE product_id IN (4707,4708,4710,4712);
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4707, 154, 1);
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4708, 154, 1);
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4710, 159, 1);
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712, 165, 1);
COMMIT;

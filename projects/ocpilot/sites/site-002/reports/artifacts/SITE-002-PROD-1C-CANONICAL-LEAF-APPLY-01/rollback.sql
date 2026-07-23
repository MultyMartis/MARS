-- ROLLBACK SQL — SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01
-- Concrete IDs after apply: {'myasorubki': 378, 'pily': 379, 'hleborezki': 380}
-- Generated: 2026-07-23T15:54:54Z
START TRANSACTION;

DELETE FROM oc_product_to_category WHERE product_id=4707 AND category_id=378;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4707, 373, 1);
DELETE FROM oc_product_to_category WHERE product_id=4708 AND category_id=378;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4708, 373, 1);
DELETE FROM oc_seo_url WHERE query='category_id=378' AND keyword='myasorubki-tehnologicheskoe';
DELETE FROM oc_category_path WHERE category_id=378;
DELETE FROM oc_category_to_store WHERE category_id=378;
DELETE FROM oc_category_description WHERE category_id=378;
DELETE FROM oc_category WHERE category_id=378;

DELETE FROM oc_product_to_category WHERE product_id=4710 AND category_id=379;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4710, 373, 1);
DELETE FROM oc_seo_url WHERE query='category_id=379' AND keyword='pily-dlya-myasa-tehnologicheskoe';
DELETE FROM oc_category_path WHERE category_id=379;
DELETE FROM oc_category_to_store WHERE category_id=379;
DELETE FROM oc_category_description WHERE category_id=379;
DELETE FROM oc_category WHERE category_id=379;

DELETE FROM oc_product_to_category WHERE product_id=4712 AND category_id=380;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712, 375, 1);
DELETE FROM oc_seo_url WHERE query='category_id=380' AND keyword='hleborezki-tehnologicheskoe';
DELETE FROM oc_category_path WHERE category_id=380;
DELETE FROM oc_category_to_store WHERE category_id=380;
DELETE FROM oc_category_description WHERE category_id=380;
DELETE FROM oc_category WHERE category_id=380;

COMMIT;

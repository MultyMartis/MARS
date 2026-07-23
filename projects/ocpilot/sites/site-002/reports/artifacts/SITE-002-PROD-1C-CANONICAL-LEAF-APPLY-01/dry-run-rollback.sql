-- DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION
-- SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01 / Run 4.295

-- ROLLBACK SQL — SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01
-- Generated: 2026-07-23T15:54:44Z
START TRANSACTION;

DELETE FROM oc_product_to_category WHERE product_id=4707 AND category_id=@NEW_MYASORUBKI_ID;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4707, 373, 1);
DELETE FROM oc_product_to_category WHERE product_id=4708 AND category_id=@NEW_MYASORUBKI_ID;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4708, 373, 1);
-- remove leaf Мясорубки (@NEW_MYASORUBKI_ID)
DELETE FROM oc_seo_url WHERE query=CONCAT('category_id=',@NEW_MYASORUBKI_ID) AND keyword='myasorubki-tehnologicheskoe';
DELETE FROM oc_category_path WHERE category_id=@NEW_MYASORUBKI_ID;
DELETE FROM oc_category_to_store WHERE category_id=@NEW_MYASORUBKI_ID;
DELETE FROM oc_category_description WHERE category_id=@NEW_MYASORUBKI_ID;
DELETE FROM oc_category WHERE category_id=@NEW_MYASORUBKI_ID;

DELETE FROM oc_product_to_category WHERE product_id=4710 AND category_id=@NEW_PILY_ID;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4710, 373, 1);
-- remove leaf Пилы для мяса (@NEW_PILY_ID)
DELETE FROM oc_seo_url WHERE query=CONCAT('category_id=',@NEW_PILY_ID) AND keyword='pily-dlya-myasa-tehnologicheskoe';
DELETE FROM oc_category_path WHERE category_id=@NEW_PILY_ID;
DELETE FROM oc_category_to_store WHERE category_id=@NEW_PILY_ID;
DELETE FROM oc_category_description WHERE category_id=@NEW_PILY_ID;
DELETE FROM oc_category WHERE category_id=@NEW_PILY_ID;

DELETE FROM oc_product_to_category WHERE product_id=4712 AND category_id=@NEW_HLEBOREZKI_ID;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712, 375, 1);
-- remove leaf Хлеборезки (@NEW_HLEBOREZKI_ID)
DELETE FROM oc_seo_url WHERE query=CONCAT('category_id=',@NEW_HLEBOREZKI_ID) AND keyword='hleborezki-tehnologicheskoe';
DELETE FROM oc_category_path WHERE category_id=@NEW_HLEBOREZKI_ID;
DELETE FROM oc_category_to_store WHERE category_id=@NEW_HLEBOREZKI_ID;
DELETE FROM oc_category_description WHERE category_id=@NEW_HLEBOREZKI_ID;
DELETE FROM oc_category WHERE category_id=@NEW_HLEBOREZKI_ID;

COMMIT;

-- DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION
-- SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01 / Run 4.295

-- APPLY SQL — SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01
-- Generated: 2026-07-23T15:54:44Z
-- Exact 3 category creates + category_to_store + path + seo + 4 product moves
START TRANSACTION;

-- LEAF: Мясорубки under 373
INSERT INTO oc_category SET parent_id=373, top=0, `column`=1, sort_order=10, status=1, date_added=NOW(), date_modified=NOW(), image='';
SET @NEW_MYASORUBKI_ID = LAST_INSERT_ID();
INSERT INTO oc_category_description SET category_id=@NEW_MYASORUBKI_ID, language_id=1, name='Мясорубки', description='', meta_title='Мясорубки', meta_description='Мясорубки ЗПМ для предприятий пищевого производства. Актуальные модели в каталоге.', meta_keyword='';
INSERT INTO oc_category_to_store SET category_id=@NEW_MYASORUBKI_ID, store_id=0;
INSERT INTO oc_category_path (category_id, path_id, level) VALUES (@NEW_MYASORUBKI_ID, 362, 0), (@NEW_MYASORUBKI_ID, 373, 1), (@NEW_MYASORUBKI_ID, @NEW_MYASORUBKI_ID, 2);
INSERT INTO oc_seo_url SET store_id=0, language_id=1, query=CONCAT('category_id=',@NEW_MYASORUBKI_ID), keyword='myasorubki-tehnologicheskoe';

DELETE FROM oc_product_to_category WHERE product_id=4707 AND category_id=373;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4707, @NEW_MYASORUBKI_ID, 1);
DELETE FROM oc_product_to_category WHERE product_id=4708 AND category_id=373;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4708, @NEW_MYASORUBKI_ID, 1);

-- LEAF: Пилы для мяса under 373
INSERT INTO oc_category SET parent_id=373, top=0, `column`=1, sort_order=20, status=1, date_added=NOW(), date_modified=NOW(), image='';
SET @NEW_PILY_ID = LAST_INSERT_ID();
INSERT INTO oc_category_description SET category_id=@NEW_PILY_ID, language_id=1, name='Пилы для мяса', description='', meta_title='Пилы для мяса', meta_description='Пилы для мяса ЗПМ для разделки мяса и костей. Актуальные модели в каталоге.', meta_keyword='';
INSERT INTO oc_category_to_store SET category_id=@NEW_PILY_ID, store_id=0;
INSERT INTO oc_category_path (category_id, path_id, level) VALUES (@NEW_PILY_ID, 362, 0), (@NEW_PILY_ID, 373, 1), (@NEW_PILY_ID, @NEW_PILY_ID, 2);
INSERT INTO oc_seo_url SET store_id=0, language_id=1, query=CONCAT('category_id=',@NEW_PILY_ID), keyword='pily-dlya-myasa-tehnologicheskoe';

DELETE FROM oc_product_to_category WHERE product_id=4710 AND category_id=373;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4710, @NEW_PILY_ID, 1);

-- LEAF: Хлеборезки under 375
INSERT INTO oc_category SET parent_id=375, top=0, `column`=1, sort_order=10, status=1, date_added=NOW(), date_modified=NOW(), image='';
SET @NEW_HLEBOREZKI_ID = LAST_INSERT_ID();
INSERT INTO oc_category_description SET category_id=@NEW_HLEBOREZKI_ID, language_id=1, name='Хлеборезки', description='', meta_title='Хлеборезки', meta_description='Хлеборезки ЗПМ для предприятий общественного питания и пищевого производства. Актуальные модели в каталоге.', meta_keyword='';
INSERT INTO oc_category_to_store SET category_id=@NEW_HLEBOREZKI_ID, store_id=0;
INSERT INTO oc_category_path (category_id, path_id, level) VALUES (@NEW_HLEBOREZKI_ID, 362, 0), (@NEW_HLEBOREZKI_ID, 375, 1), (@NEW_HLEBOREZKI_ID, @NEW_HLEBOREZKI_ID, 2);
INSERT INTO oc_seo_url SET store_id=0, language_id=1, query=CONCAT('category_id=',@NEW_HLEBOREZKI_ID), keyword='hleborezki-tehnologicheskoe';

DELETE FROM oc_product_to_category WHERE product_id=4712 AND category_id=375;
INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712, @NEW_HLEBOREZKI_ID, 1);

SELECT @NEW_MYASORUBKI_ID AS myasorubki_id, @NEW_PILY_ID AS pily_id, @NEW_HLEBOREZKI_ID AS hleborezki_id;
COMMIT;

-- DRY RUN ONLY — DO NOT APPLY

-- SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01
-- Templates only. Replace @NEW_* after inserts. language_id=1 store_id=0.

-- EXAMPLE: Мясорубки under 373
-- INSERT INTO oc_category SET parent_id=373, top=0, column=1, sort_order=10, status=1, date_added=NOW(), date_modified=NOW(), image='';
-- SET @NEW_MYASORUBKI_ID = LAST_INSERT_ID();
-- INSERT INTO oc_category_description SET category_id=@NEW_MYASORUBKI_ID, language_id=1, name='Мясорубки', description='', meta_title='Мясорубки | Технологическое оборудование | ООО «ЗПМ»', meta_description='Мясорубки технологического раздела ЗПМ для пищевых производств. Подберите модели в каталоге.', meta_keyword='';
-- INSERT INTO oc_category_to_store SET category_id=@NEW_MYASORUBKI_ID, store_id=0;
-- INSERT INTO oc_category_path (category_id, path_id, level) VALUES
--   (@NEW_MYASORUBKI_ID, 362, 0),
--   (@NEW_MYASORUBKI_ID, 373, 1),
--   (@NEW_MYASORUBKI_ID, @NEW_MYASORUBKI_ID, 2);
-- INSERT INTO oc_seo_url SET store_id=0, language_id=1, query=CONCAT('category_id=',@NEW_MYASORUBKI_ID), keyword='myasorubki-tehnologicheskoe';

-- EXAMPLE: Пилы для мяса under 373 (sort_order=20, keyword=pily-dlya-myasa-tehnologicheskoe)
-- EXAMPLE: Хлеборезки under 375 (parent_id=375, sort_order=10, keyword=hleborezki-tehnologicheskoe; path 362>375>self)

-- VERIFY before apply:
-- SELECT keyword FROM oc_seo_url WHERE keyword IN ('myasorubki-tehnologicheskoe','pily-dlya-myasa-tehnologicheskoe','hleborezki-tehnologicheskoe');

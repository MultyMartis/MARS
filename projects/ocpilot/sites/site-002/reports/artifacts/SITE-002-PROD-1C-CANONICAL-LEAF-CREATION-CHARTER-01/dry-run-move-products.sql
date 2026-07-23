-- DRY RUN ONLY — DO NOT APPLY

-- Move hub → leaf (after @NEW_* ids known)

-- 4707,4708 → @NEW_MYASORUBKI_ID
-- DELETE FROM oc_product_to_category WHERE product_id IN (4707,4708) AND category_id=373;
-- INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES
--   (4707, @NEW_MYASORUBKI_ID, 1),
--   (4708, @NEW_MYASORUBKI_ID, 1);

-- 4710 → @NEW_PILY_ID
-- DELETE FROM oc_product_to_category WHERE product_id=4710 AND category_id=373;
-- INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4710, @NEW_PILY_ID, 1);

-- 4712 → @NEW_HLEBOREZKI_ID
-- DELETE FROM oc_product_to_category WHERE product_id=4712 AND category_id=375;
-- INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712, @NEW_HLEBOREZKI_ID, 1);

-- 4709 KEEP on 376 — no change

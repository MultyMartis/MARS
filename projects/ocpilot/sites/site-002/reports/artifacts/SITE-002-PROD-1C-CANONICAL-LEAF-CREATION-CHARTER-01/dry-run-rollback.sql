-- DRY RUN ONLY — DO NOT APPLY

-- Rollback product relations to pre-move hub state
-- DELETE FROM oc_product_to_category WHERE product_id IN (4707,4708,4710) AND category_id IN (@NEW_MYASORUBKI_ID,@NEW_PILY_ID);
-- INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES
--   (4707,373,1),(4708,373,1),(4710,373,1);
-- DELETE FROM oc_product_to_category WHERE product_id=4712 AND category_id=@NEW_HLEBOREZKI_ID;
-- INSERT INTO oc_product_to_category (product_id, category_id, main_category) VALUES (4712,375,1);

-- Optional: disable/delete newly created categories ONLY if operator charter allows
-- (prefer status=0 over hard delete; hard delete needs path/seo/description cleanup)

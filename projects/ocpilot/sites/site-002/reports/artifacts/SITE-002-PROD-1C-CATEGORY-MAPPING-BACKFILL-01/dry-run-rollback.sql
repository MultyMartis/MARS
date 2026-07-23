-- OPERATION SITE-002-PROD-1C-CATEGORY-MAPPING-BACKFILL-01 ROLLBACK
-- DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION
START TRANSACTION;
DELETE FROM `oc_mars_1c_category_map` WHERE `source_group_id` IN ('e0fd5c42-a3b8-11ea-8152-a85e4515c4f4', '2adc2489-7c1a-11f1-aecc-581122cf362c', 'bac3dc26-7c19-11f1-aecc-581122cf362c', 'e0b6bb6d-7c1a-11f1-aecc-581122cf362c', '7e43262d-7c1a-11f1-aecc-581122cf362c', '95003163-7c1a-11f1-aecc-581122cf362c', '41a86281-7c1b-11f1-aecc-581122cf362c');
-- Drop table only if this operation created it and no other rows remain
SET @remain := (SELECT COUNT(*) FROM `oc_mars_1c_category_map`);
-- Manual gate: if @remain=0 then DROP TABLE `oc_mars_1c_category_map`;
COMMIT;

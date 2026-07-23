-- DRY RUN ONLY — DO NOT APPLY
-- SITE-002-PROD-CATALOG-STRUCTURE-FORENSIC-01
-- Review queries / proposed relation changes (HITL + preferably importer GUID fix first)

-- Current state
-- SELECT * FROM oc_product_to_category WHERE product_id=4710;
-- Expect: category_id=159

-- Proposed AFTER creating correct leaf under 373 (example new_id = <NEW_PILY_ID>):
-- START TRANSACTION;
-- INSERT INTO oc_product_to_category (product_id, category_id) VALUES (4710, <NEW_PILY_ID>);
-- DELETE FROM oc_product_to_category WHERE product_id=4710 AND category_id=159;
-- -- rebuild oc_category_path / seo caches via approved OCPilot charter only
-- ROLLBACK; -- default in dry-run mindset
-- COMMIT; -- ONLY with HITL approval in a future mutation charter

-- Parallel review candidates (same name-collision pattern):
-- SELECT ptc.*, pd.name FROM oc_product_to_category ptc
-- JOIN oc_product_description pd ON pd.product_id=ptc.product_id AND pd.language_id=1
-- WHERE ptc.category_id IN (154,165);

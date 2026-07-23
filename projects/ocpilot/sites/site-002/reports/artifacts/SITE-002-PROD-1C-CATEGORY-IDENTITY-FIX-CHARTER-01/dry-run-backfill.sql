-- DRY RUN ONLY — DO NOT APPLY
-- Backfill seeds for affected groups (hubs currently holding products after Run 4.290)
-- Leaf GUIDs for Мясорубки/Пилы/Хлеборезки may map to hubs until canonical leaves exist,
-- OR to newly created leaves in a follow-on wave.

INSERT INTO oc_mars_1c_category_map
  (source_group_id, category_id, source_full_path, source_name, source_parent_id, status, last_seen_at, created_at, updated_at)
VALUES
  ('e0fd5c42-a3b8-11ea-8152-a85e4515c4f4', 362, 'ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ', 'ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ', NULL, 'active', NULL, NOW(), NOW()),
  ('2adc2489-7c1a-11f1-aecc-581122cf362c', 373, 'ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Мясоперерабатывающее', 'Мясоперерабатывающее', 'e0fd5c42-a3b8-11ea-8152-a85e4515c4f4', 'active', NULL, NOW(), NOW()),
  ('bac3dc26-7c19-11f1-aecc-581122cf362c', 375, 'ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Электромеханическое', 'Электромеханическое', 'e0fd5c42-a3b8-11ea-8152-a85e4515c4f4', 'active', NULL, NOW(), NOW()),
  ('e0b6bb6d-7c1a-11f1-aecc-581122cf362c', 376, 'ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Мясоперерабатывающее > Слайсеры для мяса', 'Слайсеры для мяса', '2adc2489-7c1a-11f1-aecc-581122cf362c', 'active', NULL, NOW(), NOW()),
  -- interim: leaf GUIDs → current hubs until leaves created
  ('7e43262d-7c1a-11f1-aecc-581122cf362c', 373, '... > Мясоперерабатывающее > Мясорубки', 'Мясорубки', '2adc2489-7c1a-11f1-aecc-581122cf362c', 'active', NULL, NOW(), NOW()),
  ('95003163-7c1a-11f1-aecc-581122cf362c', 373, '... > Мясоперерабатывающее > Пилы для мяса', 'Пилы для мяса', '2adc2489-7c1a-11f1-aecc-581122cf362c', 'active', NULL, NOW(), NOW()),
  ('41a86281-7c1b-11f1-aecc-581122cf362c', 375, '... > Электромеханическое > Хлеборезки', 'Хлеборезки', 'bac3dc26-7c19-11f1-aecc-581122cf362c', 'active', NULL, NOW(), NOW());

-- Collision guard note (importer code): never resolve leaf-name-only to category_id IN (154,159,165)
-- when source parent path is under tech GUID e0fd5c42-...

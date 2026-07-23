-- DRY RUN ONLY — DO NOT APPLY
-- SITE-002-PROD-1C-CATEGORY-IDENTITY-FIX-CHARTER-01
-- Proposed mapping table (example name; final name HITL-approved)

CREATE TABLE IF NOT EXISTS oc_mars_1c_category_map (
  map_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  source_group_id VARCHAR(64) NOT NULL,
  category_id INT NOT NULL,
  source_full_path VARCHAR(512) NOT NULL DEFAULT '',
  source_name VARCHAR(255) NOT NULL DEFAULT '',
  source_parent_id VARCHAR(64) NULL DEFAULT NULL,
  status ENUM('active','blocked_legacy','deprecated') NOT NULL DEFAULT 'active',
  last_seen_at DATETIME NULL DEFAULT NULL,
  created_at DATETIME NOT NULL,
  updated_at DATETIME NOT NULL,
  PRIMARY KEY (map_id),
  UNIQUE KEY uq_source_group_id (source_group_id),
  KEY idx_category_id (category_id),
  KEY idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

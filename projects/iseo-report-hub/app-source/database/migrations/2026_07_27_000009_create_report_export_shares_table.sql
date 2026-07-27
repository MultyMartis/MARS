-- I-SEO Report Hub — DB-10 report export shares
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No share rows. No tokens. No public route.
-- Does not mutate report_exports or other business tables.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `report_export_shares` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `report_export_id` BIGINT UNSIGNED NOT NULL,
  `token_hash` CHAR(64) NOT NULL,
  `token_label` VARCHAR(150) NULL,
  `status` VARCHAR(30) NOT NULL DEFAULT 'active',
  `expires_at` DATETIME NOT NULL,
  `revoked_at` DATETIME NULL,
  `revoked_by` BIGINT UNSIGNED NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_accessed_at` DATETIME NULL,
  `access_count` INT UNSIGNED NOT NULL DEFAULT 0,
  `max_access_count` INT UNSIGNED NULL,
  `last_access_ip_hash` CHAR(64) NULL,
  `last_user_agent_hash` CHAR(64) NULL,
  `metadata_json` JSON NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_report_export_shares_token_hash` (`token_hash`),
  KEY `idx_report_export_shares_export_status` (`report_export_id`, `status`),
  KEY `idx_report_export_shares_expires_status` (`expires_at`, `status`),
  KEY `idx_report_export_shares_created_by` (`created_by`),
  KEY `idx_report_export_shares_revoked_by` (`revoked_by`),
  CONSTRAINT `fk_report_export_shares_export`
    FOREIGN KEY (`report_export_id`) REFERENCES `report_exports` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_report_export_shares_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_report_export_shares_revoked_by`
    FOREIGN KEY (`revoked_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_report_export_shares_status`
    CHECK (`status` IN (
      'active',
      'revoked',
      'expired'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

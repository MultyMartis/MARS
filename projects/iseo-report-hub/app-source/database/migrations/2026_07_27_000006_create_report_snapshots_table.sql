-- I-SEO Report Hub — DB-07 report snapshots
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No snapshot rows. No real client data.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `report_snapshots` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `monthly_report_content_id` BIGINT UNSIGNED NOT NULL,
  `reporting_period_id` BIGINT UNSIGNED NOT NULL,
  `snapshot_key` VARCHAR(96) NOT NULL,
  `version` INT UNSIGNED NOT NULL DEFAULT 1,
  `status` VARCHAR(32) NOT NULL DEFAULT 'active',
  `title` VARCHAR(255) NOT NULL,
  `render_mode` VARCHAR(32) NOT NULL,
  `payload_json` JSON NOT NULL,
  `rendered_text` MEDIUMTEXT NULL,
  `rendered_html` MEDIUMTEXT NULL,
  `checksum_sha256` CHAR(64) NOT NULL,
  `source_block_ids` JSON NULL,
  `source_weekly_checkpoint_ids` JSON NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `archived_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_report_snapshots_monthly_version` (`monthly_report_content_id`, `version`),
  UNIQUE KEY `uq_report_snapshots_snapshot_key` (`snapshot_key`),
  KEY `idx_report_snapshots_monthly_status` (`monthly_report_content_id`, `status`),
  KEY `idx_report_snapshots_period_status` (`reporting_period_id`, `status`),
  CONSTRAINT `fk_report_snapshots_monthly`
    FOREIGN KEY (`monthly_report_content_id`) REFERENCES `monthly_report_contents` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_report_snapshots_period`
    FOREIGN KEY (`reporting_period_id`) REFERENCES `reporting_periods` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_report_snapshots_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_report_snapshots_status`
    CHECK (`status` IN (
      'active',
      'superseded',
      'archived'
    )),
  CONSTRAINT `chk_report_snapshots_version`
    CHECK (`version` >= 1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

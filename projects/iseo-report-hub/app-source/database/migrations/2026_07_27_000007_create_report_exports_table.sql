-- I-SEO Report Hub — DB-08 report exports
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No export rows. No real client data.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `report_exports` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `report_snapshot_id` BIGINT UNSIGNED NOT NULL,
  `monthly_report_content_id` BIGINT UNSIGNED NOT NULL,
  `export_key` VARCHAR(128) NOT NULL,
  `format` VARCHAR(32) NOT NULL,
  `status` VARCHAR(32) NOT NULL DEFAULT 'ready',
  `storage_disk` VARCHAR(32) NOT NULL DEFAULT 'local',
  `storage_path` VARCHAR(1024) NOT NULL,
  `filename` VARCHAR(255) NOT NULL,
  `mime_type` VARCHAR(128) NOT NULL,
  `file_size_bytes` BIGINT UNSIGNED NULL,
  `checksum_sha256` CHAR(64) NULL,
  `source_snapshot_checksum_sha256` CHAR(64) NOT NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `archived_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_report_exports_export_key` (`export_key`),
  KEY `idx_report_exports_snapshot_format_status` (`report_snapshot_id`, `format`, `status`),
  KEY `idx_report_exports_monthly_format_status` (`monthly_report_content_id`, `format`, `status`),
  CONSTRAINT `fk_report_exports_snapshot`
    FOREIGN KEY (`report_snapshot_id`) REFERENCES `report_snapshots` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_report_exports_monthly`
    FOREIGN KEY (`monthly_report_content_id`) REFERENCES `monthly_report_contents` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_report_exports_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_report_exports_format`
    CHECK (`format` IN (
      'html',
      'pdf'
    )),
  CONSTRAINT `chk_report_exports_status`
    CHECK (`status` IN (
      'ready',
      'failed',
      'archived'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

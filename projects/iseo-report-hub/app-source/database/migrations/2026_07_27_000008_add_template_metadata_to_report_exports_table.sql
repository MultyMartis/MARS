-- I-SEO Report Hub — DB-09 report export template/render metadata
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- Nullable columns only. No seed rows. No NOT NULL. No template registry table.
-- Controlled backfill for existing styled export rows is a separate gated step after apply.

SET NAMES utf8mb4;

ALTER TABLE `report_exports`
  ADD COLUMN `template_id` VARCHAR(100) NULL AFTER `source_snapshot_checksum_sha256`,
  ADD COLUMN `template_version` VARCHAR(50) NULL AFTER `template_id`,
  ADD COLUMN `render_target` VARCHAR(50) NULL AFTER `template_version`,
  ADD COLUMN `render_engine` VARCHAR(100) NULL AFTER `render_target`,
  ADD COLUMN `render_options_json` JSON NULL AFTER `render_engine`,
  ADD COLUMN `source_html_export_id` BIGINT UNSIGNED NULL AFTER `render_options_json`,
  ADD COLUMN `metadata_json` JSON NULL AFTER `source_html_export_id`,
  ADD KEY `idx_report_exports_template` (`template_id`, `template_version`),
  ADD KEY `idx_report_exports_source_html` (`source_html_export_id`),
  ADD CONSTRAINT `fk_report_exports_source_html_export`
    FOREIGN KEY (`source_html_export_id`) REFERENCES `report_exports` (`id`) ON DELETE SET NULL;

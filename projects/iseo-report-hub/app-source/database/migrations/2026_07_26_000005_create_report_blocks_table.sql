-- I-SEO Report Hub — DB-06 report blocks
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No real client data.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `report_blocks` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `monthly_report_content_id` BIGINT UNSIGNED NOT NULL,
  `block_key` VARCHAR(64) NOT NULL,
  `block_type` VARCHAR(64) NOT NULL,
  `sort_order` INT UNSIGNED NOT NULL DEFAULT 0,
  `status` VARCHAR(32) NOT NULL DEFAULT 'draft',
  `title` VARCHAR(255) NOT NULL,
  `body` MEDIUMTEXT NULL,
  `summary` TEXT NULL,
  `data_json` JSON NULL,
  `source_weekly_checkpoint_ids` JSON NULL,
  `source_metric_refs` JSON NULL,
  `owner_user_id` BIGINT UNSIGNED NULL,
  `reviewer_user_id` BIGINT UNSIGNED NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `updated_by` BIGINT UNSIGNED NULL,
  `reviewed_at` DATETIME NULL,
  `approved_at` DATETIME NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_report_blocks_parent_key` (`monthly_report_content_id`, `block_key`),
  KEY `idx_report_blocks_parent_sort` (`monthly_report_content_id`, `sort_order`),
  KEY `idx_report_blocks_parent_type` (`monthly_report_content_id`, `block_type`),
  KEY `idx_report_blocks_status` (`status`),
  KEY `idx_report_blocks_owner_user_id` (`owner_user_id`),
  KEY `idx_report_blocks_reviewer_user_id` (`reviewer_user_id`),
  KEY `idx_report_blocks_created_by` (`created_by`),
  KEY `idx_report_blocks_updated_by` (`updated_by`),
  CONSTRAINT `fk_report_blocks_monthly_report_content_id`
    FOREIGN KEY (`monthly_report_content_id`) REFERENCES `monthly_report_contents` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_report_blocks_owner_user_id`
    FOREIGN KEY (`owner_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_report_blocks_reviewer_user_id`
    FOREIGN KEY (`reviewer_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_report_blocks_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_report_blocks_updated_by`
    FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_report_blocks_status`
    CHECK (`status` IN (
      'draft',
      'in_progress',
      'ready_for_review',
      'reviewed',
      'approved',
      'archived'
    )),
  CONSTRAINT `chk_report_blocks_block_type`
    CHECK (`block_type` IN (
      'executive_summary',
      'work_completed',
      'results_summary',
      'key_findings',
      'risks_and_blockers',
      'next_month_plan',
      'client_notes',
      'internal_notes',
      'custom_text',
      'metric_snapshot',
      'weekly_summary'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

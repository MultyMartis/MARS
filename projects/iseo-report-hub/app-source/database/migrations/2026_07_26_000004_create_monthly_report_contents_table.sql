-- I-SEO Report Hub — DB-05 monthly report contents
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No real client data.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `monthly_report_contents` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `reporting_period_id` BIGINT UNSIGNED NOT NULL,
  `status` VARCHAR(32) NOT NULL DEFAULT 'draft',
  `title` VARCHAR(255) NOT NULL,
  `executive_summary` TEXT NULL,
  `work_completed` TEXT NULL,
  `results_summary` TEXT NULL,
  `key_findings` TEXT NULL,
  `risks_and_blockers` TEXT NULL,
  `next_month_plan` TEXT NULL,
  `client_notes` TEXT NULL,
  `internal_notes` TEXT NULL,
  `source_weekly_checkpoint_ids` JSON NULL,
  `owner_user_id` BIGINT UNSIGNED NULL,
  `reviewer_user_id` BIGINT UNSIGNED NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `updated_by` BIGINT UNSIGNED NULL,
  `reviewed_at` DATETIME NULL,
  `finalized_at` DATETIME NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_monthly_report_contents_period` (`reporting_period_id`),
  KEY `idx_monthly_report_contents_status` (`status`),
  KEY `idx_monthly_report_contents_owner_user_id` (`owner_user_id`),
  KEY `idx_monthly_report_contents_reviewer_user_id` (`reviewer_user_id`),
  KEY `idx_monthly_report_contents_created_by` (`created_by`),
  KEY `idx_monthly_report_contents_updated_by` (`updated_by`),
  CONSTRAINT `fk_monthly_report_contents_reporting_period_id`
    FOREIGN KEY (`reporting_period_id`) REFERENCES `reporting_periods` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_monthly_report_contents_owner_user_id`
    FOREIGN KEY (`owner_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_monthly_report_contents_reviewer_user_id`
    FOREIGN KEY (`reviewer_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_monthly_report_contents_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_monthly_report_contents_updated_by`
    FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_monthly_report_contents_status`
    CHECK (`status` IN (
      'draft',
      'in_progress',
      'ready_for_review',
      'reviewed',
      'finalized',
      'archived'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

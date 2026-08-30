-- I-SEO Report Hub — DB-03 reporting periods
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No real client data.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `reporting_periods` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `project_id` BIGINT UNSIGNED NOT NULL,
  `period_key` CHAR(7) NOT NULL,
  `period_start` DATE NOT NULL,
  `period_end` DATE NOT NULL,
  `status` VARCHAR(32) NOT NULL DEFAULT 'draft',
  `title` VARCHAR(255) NULL,
  `summary` TEXT NULL,
  `owner_user_id` BIGINT UNSIGNED NULL,
  `reviewer_user_id` BIGINT UNSIGNED NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `updated_by` BIGINT UNSIGNED NULL,
  `finalized_at` DATETIME NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_reporting_periods_project_period` (`project_id`, `period_key`),
  KEY `idx_reporting_periods_project_id` (`project_id`),
  KEY `idx_reporting_periods_period_key` (`period_key`),
  KEY `idx_reporting_periods_status` (`status`),
  KEY `idx_reporting_periods_owner_user_id` (`owner_user_id`),
  KEY `idx_reporting_periods_reviewer_user_id` (`reviewer_user_id`),
  KEY `idx_reporting_periods_finalized_at` (`finalized_at`),
  KEY `idx_reporting_periods_created_at` (`created_at`),
  CONSTRAINT `fk_reporting_periods_project_id`
    FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_reporting_periods_owner_user_id`
    FOREIGN KEY (`owner_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_reporting_periods_reviewer_user_id`
    FOREIGN KEY (`reviewer_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_reporting_periods_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_reporting_periods_updated_by`
    FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_reporting_periods_dates`
    CHECK (`period_start` <= `period_end`),
  CONSTRAINT `chk_reporting_periods_status`
    CHECK (`status` IN (
      'draft',
      'active',
      'weekly_review',
      'monthly_review',
      'finalized',
      'archived'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

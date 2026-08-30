-- I-SEO Report Hub — DB-04 weekly checkpoints
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- No seed data. No real client data.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `weekly_checkpoints` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `reporting_period_id` BIGINT UNSIGNED NOT NULL,
  `week_index` TINYINT UNSIGNED NOT NULL,
  `checkpoint_key` VARCHAR(32) NOT NULL,
  `checkpoint_start` DATE NOT NULL,
  `checkpoint_end` DATE NOT NULL,
  `status` VARCHAR(32) NOT NULL DEFAULT 'draft',
  `title` VARCHAR(255) NOT NULL,
  `summary` TEXT NULL,
  `work_done` TEXT NULL,
  `findings` TEXT NULL,
  `next_steps` TEXT NULL,
  `risks` TEXT NULL,
  `owner_user_id` BIGINT UNSIGNED NULL,
  `reviewer_user_id` BIGINT UNSIGNED NULL,
  `created_by` BIGINT UNSIGNED NULL,
  `updated_by` BIGINT UNSIGNED NULL,
  `reviewed_at` DATETIME NULL,
  `completed_at` DATETIME NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_weekly_checkpoints_period_week` (`reporting_period_id`, `week_index`),
  UNIQUE KEY `uniq_weekly_checkpoints_period_key` (`reporting_period_id`, `checkpoint_key`),
  KEY `idx_weekly_checkpoints_reporting_period_id` (`reporting_period_id`),
  KEY `idx_weekly_checkpoints_status` (`status`),
  KEY `idx_weekly_checkpoints_owner_user_id` (`owner_user_id`),
  KEY `idx_weekly_checkpoints_reviewer_user_id` (`reviewer_user_id`),
  KEY `idx_weekly_checkpoints_created_by` (`created_by`),
  KEY `idx_weekly_checkpoints_updated_by` (`updated_by`),
  CONSTRAINT `fk_weekly_checkpoints_reporting_period_id`
    FOREIGN KEY (`reporting_period_id`) REFERENCES `reporting_periods` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_weekly_checkpoints_owner_user_id`
    FOREIGN KEY (`owner_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_weekly_checkpoints_reviewer_user_id`
    FOREIGN KEY (`reviewer_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_weekly_checkpoints_created_by`
    FOREIGN KEY (`created_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_weekly_checkpoints_updated_by`
    FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_weekly_checkpoints_week_index`
    CHECK (`week_index` >= 1 AND `week_index` <= 6),
  CONSTRAINT `chk_weekly_checkpoints_dates`
    CHECK (`checkpoint_start` <= `checkpoint_end`),
  CONSTRAINT `chk_weekly_checkpoints_status`
    CHECK (`status` IN (
      'draft',
      'in_progress',
      'ready_for_review',
      'reviewed',
      'completed',
      'skipped',
      'archived'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

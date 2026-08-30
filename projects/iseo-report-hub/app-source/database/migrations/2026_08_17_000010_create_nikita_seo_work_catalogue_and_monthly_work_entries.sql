-- I-SEO Report Hub — DB-11 Nikita SEO work catalogue and monthly work entries
-- Local target only: iseo_report_hub_dev
-- Ledger row for this file is inserted by tools/db-migrate.php after successful apply.
-- Additive only: new tables. No ALTER/DROP of existing MVP tables.
-- No seed data in this migration (see tools/seed-nikita-catalogue.php).
-- No real client credentials. No share/export/PDF mutation.

SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `seo_work_categories` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `slug` VARCHAR(96) NOT NULL,
  `name` VARCHAR(160) NOT NULL,
  `description` TEXT NULL,
  `sort_order` INT NOT NULL DEFAULT 100,
  `is_active` TINYINT(1) NOT NULL DEFAULT 1,
  `source` VARCHAR(96) NOT NULL DEFAULT 'nikita',
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_seo_work_categories_slug` (`slug`),
  KEY `idx_seo_work_categories_is_active` (`is_active`),
  KEY `idx_seo_work_categories_sort_order` (`sort_order`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `seo_work_items` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category_id` BIGINT UNSIGNED NOT NULL,
  `slug` VARCHAR(160) NOT NULL,
  `name` VARCHAR(220) NOT NULL,
  `description` TEXT NULL,
  `site_type` VARCHAR(32) NOT NULL DEFAULT 'both',
  `cadence` VARCHAR(32) NOT NULL DEFAULT 'monthly',
  `visibility` VARCHAR(32) NOT NULL DEFAULT 'client_safe',
  `fill_mode` VARCHAR(32) NOT NULL DEFAULT 'manual',
  `evidence_required` TINYINT(1) NOT NULL DEFAULT 0,
  `sort_order` INT NOT NULL DEFAULT 100,
  `is_active` TINYINT(1) NOT NULL DEFAULT 1,
  `source` VARCHAR(96) NOT NULL DEFAULT 'nikita',
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_seo_work_items_slug` (`slug`),
  KEY `idx_seo_work_items_category_id` (`category_id`),
  KEY `idx_seo_work_items_site_type` (`site_type`),
  KEY `idx_seo_work_items_cadence` (`cadence`),
  KEY `idx_seo_work_items_visibility` (`visibility`),
  KEY `idx_seo_work_items_is_active` (`is_active`),
  KEY `idx_seo_work_items_sort_order` (`sort_order`),
  CONSTRAINT `fk_seo_work_items_category_id`
    FOREIGN KEY (`category_id`) REFERENCES `seo_work_categories` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `chk_seo_work_items_site_type`
    CHECK (`site_type` IN ('both', 'service', 'ecommerce')),
  CONSTRAINT `chk_seo_work_items_cadence`
    CHECK (`cadence` IN ('one_time', 'weekly', 'monthly', 'recurring', 'as_needed')),
  CONSTRAINT `chk_seo_work_items_visibility`
    CHECK (`visibility` IN ('internal', 'client_safe', 'client_facing')),
  CONSTRAINT `chk_seo_work_items_fill_mode`
    CHECK (`fill_mode` IN ('manual', 'ai_assisted', 'computed'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `monthly_report_work_entries` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `monthly_report_id` BIGINT UNSIGNED NOT NULL,
  `work_item_id` BIGINT UNSIGNED NULL,
  `category_id` BIGINT UNSIGNED NULL,
  `title` VARCHAR(240) NOT NULL,
  `description` TEXT NULL,
  `status` VARCHAR(32) NOT NULL DEFAULT 'planned',
  `period_role` VARCHAR(32) NOT NULL DEFAULT 'done',
  `client_visibility` VARCHAR(32) NOT NULL DEFAULT 'client_safe',
  `client_summary` TEXT NULL,
  `internal_note` TEXT NULL,
  `evidence_note` TEXT NULL,
  `sort_order` INT NOT NULL DEFAULT 100,
  `created_by_user_id` BIGINT UNSIGNED NULL,
  `updated_by_user_id` BIGINT UNSIGNED NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_monthly_report_work_entries_monthly_report_id` (`monthly_report_id`),
  KEY `idx_monthly_report_work_entries_work_item_id` (`work_item_id`),
  KEY `idx_monthly_report_work_entries_category_id` (`category_id`),
  KEY `idx_monthly_report_work_entries_status` (`status`),
  KEY `idx_monthly_report_work_entries_period_role` (`period_role`),
  KEY `idx_monthly_report_work_entries_client_visibility` (`client_visibility`),
  KEY `idx_monthly_report_work_entries_sort_order` (`sort_order`),
  KEY `idx_monthly_report_work_entries_created_by_user_id` (`created_by_user_id`),
  KEY `idx_monthly_report_work_entries_updated_by_user_id` (`updated_by_user_id`),
  KEY `idx_monthly_report_work_entries_report_title` (`monthly_report_id`, `title`),
  CONSTRAINT `fk_monthly_report_work_entries_monthly_report_id`
    FOREIGN KEY (`monthly_report_id`) REFERENCES `monthly_report_contents` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_monthly_report_work_entries_work_item_id`
    FOREIGN KEY (`work_item_id`) REFERENCES `seo_work_items` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_monthly_report_work_entries_category_id`
    FOREIGN KEY (`category_id`) REFERENCES `seo_work_categories` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_monthly_report_work_entries_created_by_user_id`
    FOREIGN KEY (`created_by_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_monthly_report_work_entries_updated_by_user_id`
    FOREIGN KEY (`updated_by_user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  CONSTRAINT `chk_monthly_report_work_entries_status`
    CHECK (`status` IN (
      'planned',
      'in_progress',
      'done',
      'blocked',
      'cancelled',
      'deferred'
    )),
  CONSTRAINT `chk_monthly_report_work_entries_period_role`
    CHECK (`period_role` IN (
      'done',
      'planned_next',
      'risk',
      'note'
    )),
  CONSTRAINT `chk_monthly_report_work_entries_client_visibility`
    CHECK (`client_visibility` IN (
      'internal',
      'client_safe',
      'client_facing'
    ))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

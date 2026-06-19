<?php
/**
 * Plugin-owned database schema installation and upgrades.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Schema {
	const OPTION_SCHEMA_VALID = 'wpilot_schema_valid';

	/**
	 * Install or upgrade plugin-owned tables.
	 *
	 * @return bool True when schema is ready.
	 */
	public static function install_or_upgrade() {
		global $wpdb;

		require_once ABSPATH . 'wp-admin/includes/upgrade.php';

		$charset_collate = $wpdb->get_charset_collate();
		$backups_table   = self::backups_table();
		$audit_table     = self::audit_table();

		$backups_sql = "CREATE TABLE {$backups_table} (
			id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
			operation_id varchar(64) NOT NULL,
			changeset_ref varchar(64) DEFAULT '',
			target_type varchar(32) NOT NULL,
			target_id bigint(20) unsigned NOT NULL,
			post_type varchar(32) NOT NULL,
			post_status varchar(32) NOT NULL,
			content_before longtext NOT NULL,
			content_checksum varchar(96) NOT NULL,
			created_by_user_id bigint(20) unsigned DEFAULT NULL,
			created_at datetime NOT NULL,
			source varchar(32) NOT NULL DEFAULT 'plugin',
			rollback_used_at datetime DEFAULT NULL,
			PRIMARY KEY  (id),
			KEY operation_id (operation_id),
			KEY target_lookup (target_type,target_id),
			KEY created_at (created_at),
			KEY rollback_used_at (rollback_used_at)
		) {$charset_collate};";

		$audit_sql = "CREATE TABLE {$audit_table} (
			id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
			operation_id varchar(64) NOT NULL,
			event_type varchar(64) NOT NULL,
			route varchar(128) DEFAULT '',
			actor_type varchar(32) NOT NULL,
			actor_user_id bigint(20) unsigned DEFAULT NULL,
			target_type varchar(32) DEFAULT NULL,
			target_id bigint(20) unsigned DEFAULT NULL,
			outcome varchar(32) NOT NULL,
			reason_code varchar(64) DEFAULT '',
			backup_id bigint(20) unsigned DEFAULT NULL,
			before_checksum varchar(96) DEFAULT '',
			after_checksum varchar(96) DEFAULT '',
			metadata_json text DEFAULT NULL,
			created_at datetime NOT NULL,
			PRIMARY KEY  (id),
			KEY operation_id (operation_id),
			KEY event_type (event_type),
			KEY outcome (outcome),
			KEY target_lookup (target_type,target_id),
			KEY backup_id (backup_id),
			KEY created_at (created_at)
		) {$charset_collate};";

		dbDelta( $backups_sql );
		dbDelta( $audit_sql );

		$ready = self::tables_exist();

		if ( $ready ) {
			$options                    = WPilot_Settings::get_options();
			$options['schema_version']  = WPILOT_SCHEMA_VERSION;
			$options['last_safety_error'] = '';
			WPilot_Settings::update_options( $options );
			update_option( self::OPTION_SCHEMA_VALID, '1', false );
		} else {
			$options = WPilot_Settings::get_options();
			$options['last_safety_error'] = 'INVALID_CONFIG';
			WPilot_Settings::update_options( $options );
			update_option( self::OPTION_SCHEMA_VALID, '0', false );
		}

		return $ready;
	}

	/**
	 * Whether plugin-owned tables are present.
	 *
	 * @return bool
	 */
	public static function tables_exist() {
		global $wpdb;

		$backups_table = self::backups_table();
		$audit_table   = self::audit_table();
		$backups_found = $wpdb->get_var( $wpdb->prepare( 'SHOW TABLES LIKE %s', $backups_table ) );
		$audit_found   = $wpdb->get_var( $wpdb->prepare( 'SHOW TABLES LIKE %s', $audit_table ) );

		return $backups_table === $backups_found && $audit_table === $audit_found;
	}

	/**
	 * Whether schema is valid for operational write/recovery routes.
	 *
	 * @return bool
	 */
	public static function is_valid() {
		$options = WPilot_Settings::get_options();

		if ( empty( $options['schema_version'] ) || version_compare( $options['schema_version'], WPILOT_SCHEMA_VERSION, '<' ) ) {
			return false;
		}

		return self::tables_exist() && '1' === (string) get_option( self::OPTION_SCHEMA_VALID, '0' );
	}

	/**
	 * Ensure schema matches the current plugin version.
	 *
	 * @return void
	 */
	public static function maybe_upgrade() {
		$options = WPilot_Settings::get_options();

		if ( empty( $options['schema_version'] ) || version_compare( $options['schema_version'], WPILOT_SCHEMA_VERSION, '<' ) || ! self::tables_exist() ) {
			self::install_or_upgrade();
		}
	}

	/**
	 * Backups table name with prefix.
	 *
	 * @return string
	 */
	public static function backups_table() {
		global $wpdb;

		return $wpdb->prefix . 'wpilot_backups';
	}

	/**
	 * Audit log table name with prefix.
	 *
	 * @return string
	 */
	public static function audit_table() {
		global $wpdb;

		return $wpdb->prefix . 'wpilot_audit_log';
	}
}

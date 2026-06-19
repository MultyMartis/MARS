<?php
/**
 * Page content backup service for WPilot recovery path.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Backup_Service {
	/**
	 * Reader for live page content.
	 *
	 * @var WPilot_Site_Reader
	 */
	private $reader;

	public function __construct( WPilot_Site_Reader $reader = null ) {
		$this->reader = $reader instanceof WPilot_Site_Reader ? $reader : new WPilot_Site_Reader();
	}

	/**
	 * Create a plugin-owned backup for one page post_content field.
	 *
	 * @param int    $page_id Page ID.
	 * @param string $operation_id Operation ID for this run.
	 * @param array  $context Optional metadata: approval_ref, changeset_ref, reason, route.
	 * @return array|WP_Error
	 */
	public function create_backup( $page_id, $operation_id, array $context = array() ) {
		global $wpdb;

		$page_id = absint( $page_id );

		if ( ! WPilot_Schema::is_valid() ) {
			return new WP_Error( 'INVALID_CONFIG', 'Plugin storage schema is not ready.' );
		}

		$post = get_post( $page_id );

		if ( ! $post instanceof WP_Post || 'page' !== $post->post_type ) {
			return new WP_Error( 'TARGET_NOT_FOUND', 'Target page was not found.' );
		}

		$content  = $this->read_post_content( $post );
		$checksum = WPilot_Checksum::hash( $content );

		if ( '' === $checksum ) {
			return new WP_Error( 'CHECKSUM_FAILED', 'Backup checksum could not be generated.' );
		}

		$table = WPilot_Schema::backups_table();
		$now   = current_time( 'mysql', true );
		$row   = array(
			'operation_id'       => sanitize_text_field( $operation_id ),
			'changeset_ref'      => sanitize_text_field( (string) ( $context['changeset_ref'] ?? '' ) ),
			'target_type'        => 'page',
			'target_id'          => $page_id,
			'post_type'          => 'page',
			'post_status'        => sanitize_key( (string) $post->post_status ),
			'content_before'     => $content,
			'content_checksum'   => $checksum,
			'created_by_user_id' => get_current_user_id() > 0 ? get_current_user_id() : null,
			'created_at'         => $now,
			'source'             => 'plugin',
			'rollback_used_at'   => null,
		);

		$formats = array( '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s' );
		$inserted = $wpdb->insert( $table, $row, $formats );

		if ( false === $inserted ) {
			return new WP_Error( 'BACKUP_STORAGE_UNAVAILABLE', 'Backup could not be stored.' );
		}

		$backup_id = (int) $wpdb->insert_id;
		$stored    = $this->get_backup( $backup_id );

		if ( is_wp_error( $stored ) ) {
			return $stored;
		}

		if ( ! WPilot_Checksum::verify( $stored['content_before'], $stored['content_checksum'] ) ) {
			return new WP_Error( 'CHECKSUM_FAILED', 'Stored backup failed checksum verification.' );
		}

		return array(
			'backup_id'        => $backup_id,
			'operation_id'     => $operation_id,
			'target_type'      => 'page',
			'target_id'        => $page_id,
			'content_checksum' => $checksum,
			'post_type'        => 'page',
			'post_status'      => $stored['post_status'],
			'created_at'       => $stored['created_at'],
		);
	}

	/**
	 * Fetch one backup row by ID.
	 *
	 * @param int $backup_id Backup ID.
	 * @return array|WP_Error
	 */
	public function get_backup( $backup_id ) {
		global $wpdb;

		$backup_id = absint( $backup_id );

		if ( $backup_id <= 0 || ! WPilot_Schema::is_valid() ) {
			return new WP_Error( 'BACKUP_NOT_FOUND', 'Backup was not found.' );
		}

		$table = WPilot_Schema::backups_table();
		$row   = $wpdb->get_row(
			$wpdb->prepare(
				"SELECT * FROM {$table} WHERE id = %d LIMIT 1",
				$backup_id
			),
			ARRAY_A
		);

		if ( empty( $row ) || ! is_array( $row ) ) {
			return new WP_Error( 'BACKUP_NOT_FOUND', 'Backup was not found.' );
		}

		return $this->format_backup_row( $row );
	}

	/**
	 * List backups for one target ordered by newest first.
	 *
	 * @param string $target_type Target type.
	 * @param int    $target_id Target ID.
	 * @param int    $limit Max rows.
	 * @return array
	 */
	public function list_backups_for_target( $target_type, $target_id, $limit = 10 ) {
		global $wpdb;

		$target_type = sanitize_key( (string) $target_type );
		$target_id   = absint( $target_id );
		$limit       = max( 1, min( 50, absint( $limit ) ) );

		if ( ! WPilot_Schema::is_valid() ) {
			return array();
		}

		$table = WPilot_Schema::backups_table();
		$rows  = $wpdb->get_results(
			$wpdb->prepare(
				"SELECT * FROM {$table} WHERE target_type = %s AND target_id = %d ORDER BY created_at DESC, id DESC LIMIT %d",
				$target_type,
				$target_id,
				$limit
			),
			ARRAY_A
		);

		if ( empty( $rows ) || ! is_array( $rows ) ) {
			return array();
		}

		$items = array();

		foreach ( $rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}

			$formatted = $this->format_backup_row( $row );
			unset( $formatted['content_before'] );
			$items[] = $formatted;
		}

		return $items;
	}

	/**
	 * Mark a backup as used by rollback.
	 *
	 * @param int    $backup_id Backup ID.
	 * @param string $rollback_operation_id Rollback operation ID.
	 * @return bool|WP_Error
	 */
	public function mark_backup_used( $backup_id, $rollback_operation_id = '' ) {
		global $wpdb;

		$backup_id = absint( $backup_id );

		if ( $backup_id <= 0 || ! WPilot_Schema::is_valid() ) {
			return new WP_Error( 'BACKUP_NOT_FOUND', 'Backup was not found.' );
		}

		$table = WPilot_Schema::backups_table();
		$now   = current_time( 'mysql', true );
		$updated = $wpdb->update(
			$table,
			array( 'rollback_used_at' => $now ),
			array( 'id' => $backup_id ),
			array( '%s' ),
			array( '%d' )
		);

		if ( false === $updated ) {
			return new WP_Error( 'BACKUP_STORAGE_UNAVAILABLE', 'Backup usage marker could not be stored.' );
		}

		return true;
	}

	/**
	 * Read normalized post_content from a page post.
	 *
	 * @param WP_Post $post Page post.
	 * @return string
	 */
	private function read_post_content( WP_Post $post ) {
		$content = isset( $post->post_content ) && is_string( $post->post_content ) ? $post->post_content : '';

		return WPilot_Checksum::normalize_content( $content );
	}

	/**
	 * Normalize a backup DB row for service consumers.
	 *
	 * @param array $row Raw DB row.
	 * @return array
	 */
	private function format_backup_row( array $row ) {
		return array(
			'backup_id'          => (int) $row['id'],
			'operation_id'       => (string) $row['operation_id'],
			'changeset_ref'      => (string) $row['changeset_ref'],
			'target_type'        => (string) $row['target_type'],
			'target_id'          => (int) $row['target_id'],
			'post_type'          => (string) $row['post_type'],
			'post_status'        => (string) $row['post_status'],
			'content_before'     => (string) $row['content_before'],
			'content_checksum'   => (string) $row['content_checksum'],
			'created_by_user_id' => isset( $row['created_by_user_id'] ) ? (int) $row['created_by_user_id'] : 0,
			'created_at'         => (string) $row['created_at'],
			'source'             => (string) $row['source'],
			'rollback_used_at'   => ! empty( $row['rollback_used_at'] ) ? (string) $row['rollback_used_at'] : null,
		);
	}
}

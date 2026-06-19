<?php
/**
 * Audit trail persistence for WPilot operational events.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Audit_Service {
	/**
	 * Insert one sanitized audit event.
	 *
	 * @param array $args Event fields.
	 * @return int|false Insert ID or false on failure.
	 */
	public static function log_event( array $args ) {
		global $wpdb;

		if ( ! WPilot_Schema::is_valid() ) {
			return false;
		}

		$table = WPilot_Schema::audit_table();
		$now   = current_time( 'mysql', true );

		$metadata = isset( $args['metadata'] ) && is_array( $args['metadata'] ) ? $args['metadata'] : array();
		$metadata = self::sanitize_metadata( $metadata );

		$row = array(
			'operation_id'    => sanitize_text_field( (string) ( $args['operation_id'] ?? '' ) ),
			'event_type'      => sanitize_key( (string) ( $args['event_type'] ?? 'unknown' ) ),
			'route'           => sanitize_text_field( (string) ( $args['route'] ?? '' ) ),
			'actor_type'      => sanitize_key( (string) ( $args['actor_type'] ?? 'token' ) ),
			'outcome'         => sanitize_key( (string) ( $args['outcome'] ?? 'accepted' ) ),
			'reason_code'     => sanitize_text_field( (string) ( $args['reason_code'] ?? '' ) ),
			'before_checksum' => sanitize_text_field( (string) ( $args['before_checksum'] ?? '' ) ),
			'after_checksum'  => sanitize_text_field( (string) ( $args['after_checksum'] ?? '' ) ),
			'metadata_json'   => wp_json_encode( $metadata ),
			'created_at'      => $now,
		);
		$formats = array( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' );

		if ( isset( $args['actor_user_id'] ) && absint( $args['actor_user_id'] ) > 0 ) {
			$row['actor_user_id'] = absint( $args['actor_user_id'] );
			$formats[]            = '%d';
		}

		if ( isset( $args['target_type'] ) && '' !== (string) $args['target_type'] ) {
			$row['target_type'] = sanitize_key( (string) $args['target_type'] );
			$formats[]          = '%s';
		}

		if ( isset( $args['target_id'] ) && absint( $args['target_id'] ) > 0 ) {
			$row['target_id'] = absint( $args['target_id'] );
			$formats[]        = '%d';
		}

		if ( isset( $args['backup_id'] ) && absint( $args['backup_id'] ) > 0 ) {
			$row['backup_id'] = absint( $args['backup_id'] );
			$formats[]        = '%d';
		}

		$inserted = $wpdb->insert( $table, $row, $formats );

		if ( false === $inserted ) {
			return false;
		}

		return (int) $wpdb->insert_id;
	}

	/**
	 * Remove sensitive or oversized metadata keys.
	 *
	 * @param array $metadata Raw metadata.
	 * @return array
	 */
	private static function sanitize_metadata( array $metadata ) {
		$allowed = array(
			'approval_ref',
			'changeset_ref',
			'reason',
			'match_count',
			'operation_type',
			'replacements_count',
			'validation_result',
			'rollback_operation_id',
			'validation_status',
		);

		$clean = array();

		foreach ( $allowed as $key ) {
			if ( ! array_key_exists( $key, $metadata ) ) {
				continue;
			}

			$value = $metadata[ $key ];

			if ( is_scalar( $value ) ) {
				$clean[ $key ] = sanitize_text_field( (string) $value );
			}
		}

		return $clean;
	}
}

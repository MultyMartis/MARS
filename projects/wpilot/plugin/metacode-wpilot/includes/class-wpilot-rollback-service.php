<?php
/**
 * Page content rollback service for WPilot recovery path.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Rollback_Service {
	/**
	 * Backup service dependency.
	 *
	 * @var WPilot_Backup_Service
	 */
	private $backups;

	public function __construct( WPilot_Backup_Service $backups = null ) {
		$this->backups = $backups instanceof WPilot_Backup_Service ? $backups : new WPilot_Backup_Service();
	}

	/**
	 * Validate rollback preconditions without mutating WordPress content.
	 *
	 * @param int         $page_id Page ID.
	 * @param int         $backup_id Backup ID.
	 * @param string|null $expected_current_checksum Optional live checksum guard.
	 * @return array|WP_Error
	 */
	public function validate_rollback( $page_id, $backup_id, $expected_current_checksum = null ) {
		$page_id   = absint( $page_id );
		$backup_id = absint( $backup_id );

		$backup = $this->backups->get_backup( $backup_id );

		if ( is_wp_error( $backup ) ) {
			return $backup;
		}

		if ( 'plugin' !== $backup['source'] ) {
			return new WP_Error( 'BACKUP_NOT_FOUND', 'Backup source is not plugin-owned.' );
		}

		if ( 'page' !== $backup['target_type'] || (int) $backup['target_id'] !== $page_id ) {
			return new WP_Error( 'BACKUP_TARGET_MISMATCH', 'Backup does not belong to the requested page.' );
		}

		if ( ! empty( $backup['rollback_used_at'] ) ) {
			return new WP_Error( 'BACKUP_ALREADY_USED', 'Backup has already been used for rollback.' );
		}

		if ( ! WPilot_Checksum::verify( $backup['content_before'], $backup['content_checksum'] ) ) {
			return new WP_Error( 'CHECKSUM_MISMATCH', 'Backup content failed integrity verification.' );
		}

		$post = get_post( $page_id );

		if ( ! $post instanceof WP_Post || 'page' !== $post->post_type ) {
			return new WP_Error( 'TARGET_NOT_FOUND', 'Target page was not found.' );
		}

		$current_content  = $this->read_post_content( $post );
		$current_checksum = WPilot_Checksum::hash( $current_content );

		if ( is_string( $expected_current_checksum ) && '' !== $expected_current_checksum ) {
			if ( ! WPilot_Checksum::verify( $current_content, $expected_current_checksum ) ) {
				return new WP_Error(
					'CHECKSUM_MISMATCH',
					'Current page checksum does not match expected_current_checksum.'
				);
			}
		}

		return array(
			'valid'              => true,
			'target_id'          => $page_id,
			'backup_id'          => $backup_id,
			'backup_checksum'    => $backup['content_checksum'],
			'current_checksum'   => $current_checksum,
			'content_will_match' => WPilot_Checksum::verify( $backup['content_before'], $backup['content_checksum'] ),
		);
	}

	/**
	 * Restore post_content from a plugin-owned backup.
	 *
	 * @param int    $page_id Page ID.
	 * @param int    $backup_id Backup ID.
	 * @param string $operation_id Rollback operation ID.
	 * @param array  $context Optional metadata: approval_ref, expected_current_checksum, route.
	 * @return array|WP_Error
	 */
	public function rollback_backup( $page_id, $backup_id, $operation_id, array $context = array() ) {
		$page_id   = absint( $page_id );
		$backup_id = absint( $backup_id );
		$expected  = isset( $context['expected_current_checksum'] ) ? (string) $context['expected_current_checksum'] : null;

		$validation = $this->validate_rollback( $page_id, $backup_id, $expected );

		if ( is_wp_error( $validation ) ) {
			return $validation;
		}

		$backup = $this->backups->get_backup( $backup_id );

		if ( is_wp_error( $backup ) ) {
			return $backup;
		}

		$content_to_restore = WPilot_Checksum::normalize_content( $backup['content_before'] );

		$updated = wp_update_post(
			array(
				'ID'           => $page_id,
				'post_content' => wp_slash( $content_to_restore ),
			),
			true
		);

		if ( is_wp_error( $updated ) ) {
			return new WP_Error( 'ROLLBACK_WRITE_FAILED', 'Rollback write failed through WordPress APIs.' );
		}

		$post_after = get_post( $page_id );

		if ( ! $post_after instanceof WP_Post ) {
			return new WP_Error( 'ROLLBACK_WRITE_FAILED', 'Rollback target could not be read after write.' );
		}

		$restored_content  = $this->read_post_content( $post_after );
		$restored_checksum = WPilot_Checksum::hash( $restored_content );

		if ( ! WPilot_Checksum::verify( $restored_content, $backup['content_checksum'] ) ) {
			return new WP_Error(
				'ROLLBACK_VERIFICATION_FAILED',
				'Post-rollback checksum does not match backup checksum.',
				array(
					'mutation_performed' => true,
					'restored_checksum'  => $restored_checksum,
					'backup_checksum'    => $backup['content_checksum'],
				)
			);
		}

		$marked = $this->backups->mark_backup_used( $backup_id, $operation_id );

		if ( is_wp_error( $marked ) ) {
			return new WP_Error(
				'ROLLBACK_VERIFICATION_FAILED',
				'Rollback content restored but backup marker could not be stored.',
				array(
					'mutation_performed' => true,
					'restored_checksum'  => $restored_checksum,
				)
			);
		}

		return array(
			'operation_id'       => $operation_id,
			'target_id'          => $page_id,
			'backup_id'          => $backup_id,
			'restored_checksum'  => $restored_checksum,
			'before_checksum'    => $validation['current_checksum'],
			'mutation_performed' => true,
			'verification_status'=> 'matched',
		);
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
}

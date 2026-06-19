<?php

/**

 * Scoped exact replace service for WPilot page post_content writes.

 *

 * @package MetaCode_WPilot

 */



if ( ! defined( 'ABSPATH' ) ) {

	exit;

}



class WPilot_Scoped_Replace_Service {

	const OPERATION_TYPE = 'apply_content_change';



	/**

	 * Backup service.

	 *

	 * @var WPilot_Backup_Service

	 */

	private $backups;



	/**

	 * Dry-run validator.

	 *

	 * @var WPilot_Dry_Run

	 */

	private $dry_run;



	public function __construct( WPilot_Backup_Service $backups = null, WPilot_Dry_Run $dry_run = null ) {

		$this->backups = $backups instanceof WPilot_Backup_Service ? $backups : new WPilot_Backup_Service();

		$this->dry_run = $dry_run instanceof WPilot_Dry_Run ? $dry_run : new WPilot_Dry_Run();

	}



	/**

	 * Execute one scoped exact replace on page post_content.

	 *

	 * @param int    $page_id Page ID.

	 * @param string $operation_id Operation ID for this run.

	 * @param string $search Exact source text.

	 * @param string $replace Replacement text.

	 * @param array  $context Optional metadata: approval_ref, changeset_ref, route.

	 * @return array|WP_Error

	 */

	public function execute( $page_id, $operation_id, $search, $replace, array $context = array() ) {

		$page_id = absint( $page_id );

		$search  = is_string( $search ) ? $search : '';

		$replace = is_string( $replace ) ? $replace : '';



		if ( $search === $replace ) {

			return new WP_Error( 'INVALID_REQUEST', 'search and replace must differ.' );

		}



		$validation = $this->dry_run->validate_exact_replacement( $page_id, $search, $replace );



		if ( is_wp_error( $validation ) ) {

			return $validation;

		}



		$checksum_before = (string) $validation['content_checksum_before'];



		$backup = $this->backups->create_backup(

			$page_id,

			$operation_id,

			array(

				'approval_ref'  => (string) ( $context['approval_ref'] ?? '' ),

				'changeset_ref' => (string) ( $context['changeset_ref'] ?? '' ),

				'reason'        => 'pre_scoped_replace',

				'route'         => (string) ( $context['route'] ?? '' ),

			)

		);



		if ( is_wp_error( $backup ) ) {

			return $backup;

		}



		$backup_id = (int) $backup['backup_id'];



		if ( ! WPilot_Checksum::verify( $this->read_post_content_by_id( $page_id ), $backup['content_checksum'] ) ) {

			return new WP_Error( 'CHECKSUM_MISMATCH', 'Backup verification failed before scoped replace.' );

		}



		$post = get_post( $page_id );



		if ( ! $post instanceof WP_Post || 'page' !== $post->post_type ) {

			return new WP_Error( 'TARGET_NOT_FOUND', 'Target page was not found.' );

		}



		$content            = $this->read_post_content( $post );

		$replacements_count = 0;

		$new_content        = str_replace( $search, $replace, $content, $replacements_count );



		$updated = wp_update_post(

			array(

				'ID'           => $page_id,

				'post_content' => wp_slash( $new_content ),

			),

			true

		);



		if ( is_wp_error( $updated ) ) {

			return new WP_Error(

				'WRITE_FAILED',

				'Scoped replace write failed through WordPress APIs.',

				array(

					'mutation_performed' => false,

					'backup_id'          => $backup_id,

				)

			);

		}



		$post_after = get_post( $page_id );



		if ( ! $post_after instanceof WP_Post ) {

			return new WP_Error(

				'POST_WRITE_VALIDATION_FAILED',

				'Scoped replace target could not be read after write.',

				array(

					'mutation_performed' => true,

					'backup_id'          => $backup_id,

				)

			);

		}



		$content_after  = $this->read_post_content( $post_after );

		$checksum_after = WPilot_Checksum::hash( $content_after );

		$confirmed      = (
			false !== strpos( $content_after, $replace )
			&& substr_count( $content_after, $search ) === substr_count( $replace, $search )
		);



		$validation_passed = (

			1 === $replacements_count

			&& $checksum_before !== $checksum_after

			&& $confirmed

			&& $backup_id > 0

		);



		if ( ! $validation_passed ) {

			return new WP_Error(

				'POST_WRITE_VALIDATION_FAILED',

				'Scoped replace post-write validation failed.',

				array(

					'mutation_performed'  => true,

					'backup_id'           => $backup_id,

					'checksum_before'     => $checksum_before,

					'checksum_after'      => $checksum_after,

					'replacements_count'  => $replacements_count,

					'validation_result'   => 'failed',

					'replacement_confirmed' => $confirmed,

				)

			);

		}



		return array(

			'operation_type'     => self::OPERATION_TYPE,

			'target_id'          => $page_id,

			'backup_id'          => $backup_id,

			'checksum_before'    => $checksum_before,

			'checksum_after'     => $checksum_after,

			'replacements_count' => $replacements_count,

			'validation_result'  => 'passed',

			'mutation_performed' => true,

			'backup_checksum'    => $backup['content_checksum'],

		);

	}



	/**

	 * Read normalized post_content for one page ID.

	 *

	 * @param int $page_id Page ID.

	 * @return string

	 */

	private function read_post_content_by_id( $page_id ) {

		$post = get_post( absint( $page_id ) );



		if ( ! $post instanceof WP_Post ) {

			return '';

		}



		return $this->read_post_content( $post );

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



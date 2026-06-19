<?php
/**
 * REST route registration and read-only handlers for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_REST_Controller {
	/**
	 * Read-only site reader.
	 *
	 * @var WPilot_Site_Reader
	 */
	private $reader;

	/**
	 * Dry-run scoped replacement analyzer.
	 *
	 * @var WPilot_Dry_Run
	 */
	private $dry_run;

	/**
	 * Backup service.
	 *
	 * @var WPilot_Backup_Service
	 */
	private $backup_service;

	/**
	 * Rollback service.
	 *
	 * @var WPilot_Rollback_Service
	 */
	private $rollback_service;

	/**
	 * Scoped replace service.
	 *
	 * @var WPilot_Scoped_Replace_Service
	 */
	private $scoped_replace_service;

	public function __construct() {
		$this->reader                 = new WPilot_Site_Reader();
		$this->dry_run                = new WPilot_Dry_Run();
		$this->backup_service         = new WPilot_Backup_Service( $this->reader );
		$this->rollback_service       = new WPilot_Rollback_Service( $this->backup_service );
		$this->scoped_replace_service = new WPilot_Scoped_Replace_Service( $this->backup_service, $this->dry_run );
	}

	/**
	 * Register explicit read-only route allowlist.
	 *
	 * @return void
	 */
	public function register_routes() {
		register_rest_route(
			WPilot_Constants::REST_NAMESPACE,
			'/ping',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'ping' ),
				'permission_callback' => '__return_true',
			)
		);

		$this->register_read_route( '/site-info', 'site_info' );
		$this->register_read_route( '/themes', 'themes' );
		$this->register_read_route( '/plugins', 'plugins' );
		$this->register_read_route( '/pages', 'pages' );
		$this->register_read_route(
			'/pages/(?P<id>[\d]+)',
			'page',
			array(
				'id' => array(
					'required'          => true,
					'validate_callback' => array( $this, 'validate_page_id' ),
					'sanitize_callback' => array( $this, 'sanitize_page_id' ),
				),
			)
		);
		$this->register_read_route(
			'/pages/(?P<id>[\d]+)/structure',
			'page_structure',
			array(
				'id' => array(
					'required'          => true,
					'validate_callback' => array( $this, 'validate_page_id' ),
					'sanitize_callback' => array( $this, 'sanitize_page_id' ),
				),
			)
		);
		$this->register_dry_run_route(
			'/pages/(?P<id>[\d]+)/replace-text/dry-run',
			'page_replace_text_dry_run',
			array(
				'id' => array(
					'required'          => true,
					'validate_callback' => array( $this, 'validate_page_id' ),
					'sanitize_callback' => array( $this, 'sanitize_page_id' ),
				),
			)
		);
		$this->register_write_route(
			'/pages/(?P<id>[\d]+)/backups',
			'page_create_backup',
			array(
				'id' => array(
					'required'          => true,
					'validate_callback' => array( $this, 'validate_page_id' ),
					'sanitize_callback' => array( $this, 'sanitize_page_id' ),
				),
			)
		);
		$this->register_write_route(
			'/pages/(?P<id>[\d]+)/rollback',
			'page_rollback',
			array(
				'id' => array(
					'required'          => true,
					'validate_callback' => array( $this, 'validate_page_id' ),
					'sanitize_callback' => array( $this, 'sanitize_page_id' ),
				),
			)
		);
		$this->register_write_route(
			'/pages/(?P<id>[\d]+)/scoped-replace',
			'page_scoped_replace',
			array(
				'id' => array(
					'required'          => true,
					'validate_callback' => array( $this, 'validate_page_id' ),
					'sanitize_callback' => array( $this, 'sanitize_page_id' ),
				),
			)
		);
		$this->register_read_route( '/indexing-state', 'indexing_state' );
	}

	/**
	 * Public ping does not expose secrets or token details.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function ping( WP_REST_Request $request ) {
		$options = WPilot_Settings::get_options();

		return WPilot_Response::success(
			array(
				'plugin'         => WPilot_Constants::PLUGIN_SLUG,
				'status'         => 'installed',
				'bridge_enabled' => (bool) $options['bridge_enabled'],
				'write_enabled'  => (bool) $options['write_enabled'],
				'state'          => WPilot_Settings::get_state(),
			),
			WPilot_Request_Context::response_meta( $request, 'ping', 'not-required' )
		);
	}

	/**
	 * Read site information.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function site_info( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		return WPilot_Response::success( $this->reader->get_site_info(), $this->meta( $request, 'site-info' ) );
	}

	/**
	 * Read active theme.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function themes( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		return WPilot_Response::success( $this->reader->get_themes(), $this->meta( $request, 'themes' ) );
	}

	/**
	 * Read active plugins.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function plugins( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		return WPilot_Response::success( $this->reader->get_plugins(), $this->meta( $request, 'plugins' ) );
	}

	/**
	 * Read page summaries.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function pages( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		return WPilot_Response::success( $this->reader->get_pages(), $this->meta( $request, 'pages' ) );
	}

	/**
	 * Read one page.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function page( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		try {
			$page = $this->reader->get_page( $this->page_id_from_request( $request ) );
		} catch ( Throwable $exception ) {
			return $this->endpoint_failure( $request, 'page', 'PAGE_READ_FAILED', 'Page read failed safely.', $exception );
		}

		if ( $page instanceof WP_REST_Response ) {
			return $page;
		}

		return WPilot_Response::success( $page, $this->meta( $request, 'page' ) );
	}

	/**
	 * Read basic page structure signals.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function page_structure( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		try {
			$structure = $this->reader->get_page_structure( $this->page_id_from_request( $request ) );
		} catch ( Throwable $exception ) {
			return $this->endpoint_failure( $request, 'page-structure', 'PAGE_STRUCTURE_READ_FAILED', 'Page structure read failed safely.', $exception );
		}

		if ( $structure instanceof WP_REST_Response ) {
			return $structure;
		}

		return WPilot_Response::success( $structure, $this->meta( $request, 'page-structure' ) );
	}

	/**
	 * Read indexing state signals.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function indexing_state( WP_REST_Request $request ) {
		$guard = $this->guard_read( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		return WPilot_Response::success( $this->reader->get_indexing_state(), $this->meta( $request, 'indexing-state' ) );
	}

	/**
	 * Analyze a scoped exact text replacement without mutating content.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function page_replace_text_dry_run( WP_REST_Request $request ) {
		$guard = WPilot_Auth::require_dry_run_access( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		try {
			$result = $this->dry_run->analyze( $this->page_id_from_request( $request ), $request, $this->meta( $request, 'page-replace-text-dry-run' ) );
		} catch ( Throwable $exception ) {
			return $this->endpoint_failure( $request, 'page-replace-text-dry-run', 'SAFE_UNKNOWN', 'Dry-run analysis failed safely.', $exception );
		}

		if ( $result instanceof WP_REST_Response ) {
			return $result;
		}

		return WPilot_Response::success( $result, $this->meta( $request, 'page-replace-text-dry-run' ) );
	}

	/**
	 * Create a plugin-owned backup for page post_content.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function page_create_backup( WP_REST_Request $request ) {
		$operation_id = WPilot_Operation_Id::generate();
		$endpoint     = 'page-backups';
		$meta         = $this->meta( $request, $endpoint );
		$page_id      = $this->page_id_from_request( $request );

		$guard = WPilot_Auth::require_backup_access( $request );
		if ( true !== $guard ) {
			return $this->attach_operation_id( $guard, $operation_id );
		}

		$params = $request->get_json_params();
		$params = is_array( $params ) ? $params : array();

		$approval_ref  = isset( $params['approval_ref'] ) ? sanitize_text_field( (string) $params['approval_ref'] ) : '';
		$changeset_ref = isset( $params['changeset_ref'] ) ? sanitize_text_field( (string) $params['changeset_ref'] ) : '';
		$reason        = isset( $params['reason'] ) ? sanitize_text_field( (string) $params['reason'] ) : 'pre_recovery';

		WPilot_Audit_Service::log_event(
			array(
				'operation_id' => $operation_id,
				'event_type'   => 'backup_requested',
				'route'        => '/pages/' . $page_id . '/backups',
				'actor_type'   => 'token',
				'target_type'  => 'page',
				'target_id'    => $page_id,
				'outcome'      => 'accepted',
				'metadata'     => array(
					'approval_ref'  => $approval_ref,
					'changeset_ref' => $changeset_ref,
					'reason'        => $reason,
				),
			)
		);

		try {
			$result = $this->backup_service->create_backup(
				$page_id,
				$operation_id,
				array(
					'approval_ref'  => $approval_ref,
					'changeset_ref' => $changeset_ref,
					'reason'        => $reason,
					'route'         => '/pages/' . $page_id . '/backups',
				)
			);
		} catch ( Throwable $exception ) {
			return $this->operation_failure(
				$request,
				$endpoint,
				$operation_id,
				'BACKUP_STORAGE_UNAVAILABLE',
				'Backup creation failed safely.',
				$exception,
				'backup'
			);
		}

		if ( is_wp_error( $result ) ) {
			return $this->service_error_response( $result, $meta, $operation_id, $endpoint, 'backup', $page_id );
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id'    => $operation_id,
				'event_type'      => 'backup_created',
				'route'           => '/pages/' . $page_id . '/backups',
				'actor_type'      => 'token',
				'target_type'     => 'page',
				'target_id'       => $page_id,
				'outcome'         => 'succeeded',
				'backup_id'       => $result['backup_id'],
				'before_checksum' => $result['content_checksum'],
				'metadata'        => array(
					'approval_ref'  => $approval_ref,
					'changeset_ref' => $changeset_ref,
					'reason'        => $reason,
				),
			)
		);

		return WPilot_Response::success(
			array(
				'backup_id'        => $result['backup_id'],
				'target_id'        => $result['target_id'],
				'content_checksum' => $result['content_checksum'],
				'operation_id'     => $operation_id,
			),
			$meta,
			200,
			$operation_id
		);
	}

	/**
	 * Restore page post_content from a plugin-owned backup.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function page_rollback( WP_REST_Request $request ) {
		$operation_id = WPilot_Operation_Id::generate();
		$endpoint     = 'page-rollback';
		$meta         = $this->meta( $request, $endpoint );
		$page_id      = $this->page_id_from_request( $request );

		$guard = WPilot_Auth::require_rollback_access( $request );
		if ( true !== $guard ) {
			return $this->attach_operation_id( $guard, $operation_id );
		}

		$params = $request->get_json_params();
		$params = is_array( $params ) ? $params : array();

		$backup_id                 = isset( $params['backup_id'] ) ? absint( $params['backup_id'] ) : 0;
		$approval_ref              = isset( $params['approval_ref'] ) ? sanitize_text_field( (string) $params['approval_ref'] ) : '';
		$expected_current_checksum = isset( $params['expected_current_checksum'] ) ? sanitize_text_field( (string) $params['expected_current_checksum'] ) : '';

		if ( $backup_id <= 0 ) {
			return WPilot_Response::error(
				'INVALID_REQUEST',
				'backup_id is required.',
				$meta,
				400,
				array(
					'stage'              => 'request',
					'mutation_performed' => false,
					'rollback_available' => true,
				),
				$operation_id
			);
		}

		if ( '' === $approval_ref ) {
			return WPilot_Response::error(
				'APPROVAL_REQUIRED',
				'approval_ref is required for rollback.',
				$meta,
				403,
				array(
					'stage'              => 'approval',
					'mutation_performed' => false,
					'rollback_available' => true,
				),
				$operation_id
			);
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id' => $operation_id,
				'event_type'   => 'rollback_requested',
				'route'        => '/pages/' . $page_id . '/rollback',
				'actor_type'   => 'token',
				'target_type'  => 'page',
				'target_id'    => $page_id,
				'outcome'      => 'accepted',
				'backup_id'    => $backup_id,
				'metadata'     => array(
					'approval_ref' => $approval_ref,
				),
			)
		);

		try {
			$result = $this->rollback_service->rollback_backup(
				$page_id,
				$backup_id,
				$operation_id,
				array(
					'approval_ref'              => $approval_ref,
					'expected_current_checksum' => $expected_current_checksum,
					'route'                     => '/pages/' . $page_id . '/rollback',
				)
			);
		} catch ( Throwable $exception ) {
			return $this->operation_failure(
				$request,
				$endpoint,
				$operation_id,
				'ROLLBACK_WRITE_FAILED',
				'Rollback failed safely.',
				$exception,
				'rollback',
				$backup_id
			);
		}

		if ( is_wp_error( $result ) ) {
			return $this->service_error_response( $result, $meta, $operation_id, $endpoint, 'rollback', $page_id, $backup_id );
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id'    => $operation_id,
				'event_type'      => 'rollback_verified',
				'route'           => '/pages/' . $page_id . '/rollback',
				'actor_type'      => 'token',
				'target_type'     => 'page',
				'target_id'       => $page_id,
				'outcome'         => 'rolled_back',
				'backup_id'       => $backup_id,
				'before_checksum' => $result['before_checksum'],
				'after_checksum'  => $result['restored_checksum'],
				'metadata'        => array(
					'approval_ref'          => $approval_ref,
					'rollback_operation_id' => $operation_id,
					'validation_status'     => $result['verification_status'],
				),
			)
		);

		return WPilot_Response::success(
			array(
				'target_id'          => $result['target_id'],
				'backup_id'          => $result['backup_id'],
				'restored_checksum'  => $result['restored_checksum'],
				'mutation_performed' => true,
				'operation_id'       => $operation_id,
			),
			$meta,
			200,
			$operation_id
		);
	}

	/**
	 * Execute one scoped exact replace on page post_content.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return WP_REST_Response
	 */
	public function page_scoped_replace( WP_REST_Request $request ) {
		$operation_id = WPilot_Operation_Id::generate();
		$endpoint     = 'page-scoped-replace';
		$meta         = $this->meta( $request, $endpoint );
		$page_id      = $this->page_id_from_request( $request );

		$guard = WPilot_Auth::require_scoped_replace_access( $request );
		if ( true !== $guard ) {
			return $this->attach_operation_id( $guard, $operation_id );
		}

		$params = $request->get_json_params();
		$params = is_array( $params ) ? $params : array();

		$search        = isset( $params['search'] ) ? (string) $params['search'] : '';
		$replace       = isset( $params['replace'] ) ? (string) $params['replace'] : '';
		$approval_ref  = isset( $params['approval_ref'] ) ? sanitize_text_field( (string) $params['approval_ref'] ) : '';
		$changeset_ref = isset( $params['changeset_ref'] ) ? sanitize_text_field( (string) $params['changeset_ref'] ) : '';

		if ( '' === $approval_ref ) {
			return WPilot_Response::error(
				'APPROVAL_REQUIRED',
				'approval_ref is required for scoped replace.',
				$meta,
				403,
				array(
					'stage'              => 'approval',
					'mutation_performed' => false,
					'rollback_available' => true,
				),
				$operation_id
			);
		}

		if ( '' === $search ) {
			return WPilot_Response::error(
				'INVALID_REQUEST',
				'search is required and must be a non-empty string.',
				$meta,
				400,
				array(
					'stage'              => 'request',
					'mutation_performed' => false,
					'rollback_available' => true,
				),
				$operation_id
			);
		}

		if ( ! array_key_exists( 'replace', $params ) || ! is_string( $params['replace'] ) ) {
			return WPilot_Response::error(
				'INVALID_REQUEST',
				'replace is required and must be a string.',
				$meta,
				400,
				array(
					'stage'              => 'request',
					'mutation_performed' => false,
					'rollback_available' => true,
				),
				$operation_id
			);
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id' => $operation_id,
				'event_type'   => 'scoped_replace_requested',
				'route'        => '/pages/' . $page_id . '/scoped-replace',
				'actor_type'   => 'token',
				'target_type'  => 'page',
				'target_id'    => $page_id,
				'outcome'      => 'accepted',
				'metadata'     => array(
					'approval_ref'   => $approval_ref,
					'changeset_ref'  => $changeset_ref,
					'operation_type' => WPilot_Scoped_Replace_Service::OPERATION_TYPE,
				),
			)
		);

		try {
			$result = $this->scoped_replace_service->execute(
				$page_id,
				$operation_id,
				$search,
				$replace,
				array(
					'approval_ref'  => $approval_ref,
					'changeset_ref' => $changeset_ref,
					'route'         => '/pages/' . $page_id . '/scoped-replace',
				)
			);
		} catch ( Throwable $exception ) {
			return $this->operation_failure(
				$request,
				$endpoint,
				$operation_id,
				'WRITE_FAILED',
				'Scoped replace failed safely.',
				$exception,
				'scoped_replace'
			);
		}

		if ( is_wp_error( $result ) ) {
			return $this->scoped_replace_error_response( $result, $meta, $operation_id, $page_id );
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id'    => $operation_id,
				'event_type'      => 'backup_created',
				'route'           => '/pages/' . $page_id . '/scoped-replace',
				'actor_type'      => 'token',
				'target_type'     => 'page',
				'target_id'       => $page_id,
				'outcome'         => 'succeeded',
				'backup_id'       => $result['backup_id'],
				'before_checksum' => $result['checksum_before'],
				'metadata'        => array(
					'approval_ref'   => $approval_ref,
					'changeset_ref'  => $changeset_ref,
					'operation_type' => WPilot_Scoped_Replace_Service::OPERATION_TYPE,
					'reason'         => 'pre_scoped_replace',
				),
			)
		);

		WPilot_Audit_Service::log_event(
			array(
				'operation_id'    => $operation_id,
				'event_type'      => 'scoped_replace_verified',
				'route'           => '/pages/' . $page_id . '/scoped-replace',
				'actor_type'      => 'token',
				'target_type'     => 'page',
				'target_id'       => $page_id,
				'outcome'         => 'succeeded',
				'backup_id'       => $result['backup_id'],
				'before_checksum' => $result['checksum_before'],
				'after_checksum'  => $result['checksum_after'],
				'metadata'        => array(
					'approval_ref'        => $approval_ref,
					'changeset_ref'       => $changeset_ref,
					'operation_type'      => WPilot_Scoped_Replace_Service::OPERATION_TYPE,
					'replacements_count'  => (string) $result['replacements_count'],
					'validation_result'   => $result['validation_result'],
					'validation_status'   => $result['validation_result'],
				),
			)
		);

		return WPilot_Response::success(
			array(
				'operation_type'     => WPilot_Scoped_Replace_Service::OPERATION_TYPE,
				'target_id'          => $result['target_id'],
				'backup_id'          => $result['backup_id'],
				'checksum_before'    => $result['checksum_before'],
				'checksum_after'     => $result['checksum_after'],
				'replacements_count' => $result['replacements_count'],
				'validation_result'  => $result['validation_result'],
				'mutation_performed' => true,
				'operation_id'       => $operation_id,
			),
			$meta,
			200,
			$operation_id
		);
	}

	/**
	 * Register one authenticated read-only route.
	 *
	 * @param string $route Route path.
	 * @param string $method Handler method.
	 * @param array  $args Route args.
	 * @return void
	 */
	private function register_read_route( $route, $method, array $args = array() ) {
		register_rest_route(
			WPilot_Constants::REST_NAMESPACE,
			$route,
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, $method ),
				'permission_callback' => array( $this, 'read_permission_callback' ),
				'args'                => $args,
			)
		);
	}

	/**
	 * Register one authenticated dry-run route.
	 *
	 * @param string $route Route path.
	 * @param string $method Handler method.
	 * @param array  $args Route args.
	 * @return void
	 */
	private function register_dry_run_route( $route, $method, array $args = array() ) {
		register_rest_route(
			WPilot_Constants::REST_NAMESPACE,
			$route,
			array(
				'methods'             => WP_REST_Server::CREATABLE,
				'callback'            => array( $this, $method ),
				'permission_callback' => array( $this, 'read_permission_callback' ),
				'args'                => $args,
			)
		);
	}

	/**
	 * Register one authenticated write/recovery route.
	 *
	 * @param string $route Route path.
	 * @param string $method Handler method.
	 * @param array  $args Route args.
	 * @return void
	 */
	private function register_write_route( $route, $method, array $args = array() ) {
		register_rest_route(
			WPilot_Constants::REST_NAMESPACE,
			$route,
			array(
				'methods'             => WP_REST_Server::CREATABLE,
				'callback'            => array( $this, $method ),
				'permission_callback' => array( $this, 'read_permission_callback' ),
				'args'                => $args,
			)
		);
	}

	/**
	 * Route-level callback is intentionally side-effect free; handlers return envelopes.
	 *
	 * @return bool
	 */
	public function read_permission_callback() {
		return true;
	}

	/**
	 * Validate page ID route params without using PHP internal functions directly.
	 *
	 * WordPress passes multiple arguments to REST validation callbacks.
	 *
	 * @param mixed $value Route value.
	 * @return bool
	 */
	public function validate_page_id( $value ) {
		return is_numeric( $value ) && absint( $value ) > 0;
	}

	/**
	 * Sanitize page ID route params without using PHP internal functions directly.
	 *
	 * @param mixed $value Route value.
	 * @return int
	 */
	public function sanitize_page_id( $value ) {
		return absint( $value );
	}

	/**
	 * Shared read-only auth/state guard.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return true|WP_REST_Response
	 */
	private function guard_read( WP_REST_Request $request ) {
		return WPilot_Auth::require_read_access( $request );
	}

	/**
	 * Build response metadata for successful authenticated reads.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @param string          $endpoint_name Endpoint name.
	 * @return array
	 */
	private function meta( WP_REST_Request $request, $endpoint_name ) {
		return WPilot_Request_Context::response_meta( $request, $endpoint_name, 'authorized' );
	}

	/**
	 * Extract a sanitized page ID from the request.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return int
	 */
	private function page_id_from_request( WP_REST_Request $request ) {
		return absint( $request->get_param( 'id' ) );
	}

	/**
	 * Return a safe envelope for page endpoint failures.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @param string          $endpoint_name Endpoint name.
	 * @param string          $code Stable error code.
	 * @param string          $message Public operator-readable message.
	 * @param Throwable       $exception Captured exception.
	 * @return WP_REST_Response
	 */
	private function endpoint_failure( WP_REST_Request $request, $endpoint_name, $code, $message, Throwable $exception ) {
		$this->log_endpoint_failure( $endpoint_name, $request, $exception );

		return WPilot_Response::error( $code, $message, $this->meta( $request, $endpoint_name ), 500 );
	}

	/**
	 * Minimal DEV-safe logging for WP_DEBUG environments.
	 *
	 * Logs endpoint, sanitized page ID, exception class, and bounded message only.
	 *
	 * @param string          $endpoint_name Endpoint name.
	 * @param WP_REST_Request $request REST request.
	 * @param Throwable       $exception Captured exception.
	 * @return void
	 */
	private function log_endpoint_failure( $endpoint_name, WP_REST_Request $request, Throwable $exception ) {
		if ( ! defined( 'WP_DEBUG' ) || ! WP_DEBUG ) {
			return;
		}

		$page_id = $this->page_id_from_request( $request );
		$message = substr( sanitize_text_field( $exception->getMessage() ), 0, 240 );

		error_log(
			sprintf(
				'WPilot endpoint failure: endpoint=%s page_id=%d exception=%s message=%s',
				sanitize_key( $endpoint_name ),
				$page_id,
				get_class( $exception ),
				$message
			)
		);
	}

	/**
	 * Attach operation_id to an existing response envelope.
	 *
	 * @param WP_REST_Response $response REST response.
	 * @param string           $operation_id Operation ID.
	 * @return WP_REST_Response
	 */
	private function attach_operation_id( WP_REST_Response $response, $operation_id ) {
		$data = $response->get_data();

		if ( is_array( $data ) ) {
			$data['operation_id'] = $operation_id;
			$response->set_data( $data );
		}

		return $response;
	}

	/**
	 * Map a WP_Error from services into the REST envelope.
	 *
	 * @param WP_Error $error Service error.
	 * @param array    $meta Response metadata.
	 * @param string   $operation_id Operation ID.
	 * @param string   $endpoint Endpoint name.
	 * @param string   $stage Failure stage.
	 * @param int      $page_id Page ID.
	 * @param int      $backup_id Optional backup ID.
	 * @return WP_REST_Response
	 */
	private function service_error_response( WP_Error $error, array $meta, $operation_id, $endpoint, $stage, $page_id, $backup_id = 0 ) {
		$code    = $error->get_error_code();
		$message = $error->get_error_message();
		$data    = $error->get_error_data();
		$details = array(
			'stage'              => $stage,
			'mutation_performed' => is_array( $data ) && ! empty( $data['mutation_performed'] ),
			'rollback_available' => 'ROLLBACK_WRITE_FAILED' !== $code && 'ROLLBACK_VERIFICATION_FAILED' !== $code,
		);

		if ( is_array( $data ) ) {
			if ( isset( $data['restored_checksum'] ) ) {
				$details['restored_checksum'] = (string) $data['restored_checksum'];
			}
			if ( isset( $data['backup_checksum'] ) ) {
				$details['backup_checksum'] = (string) $data['backup_checksum'];
			}
		}

		$status = 400;
		if ( in_array( $code, array( 'TARGET_NOT_FOUND', 'BACKUP_NOT_FOUND' ), true ) ) {
			$status = 404;
		} elseif ( in_array( $code, array( 'CHECKSUM_MISMATCH', 'BACKUP_ALREADY_USED', 'BACKUP_TARGET_MISMATCH', 'APPROVAL_REQUIRED' ), true ) ) {
			$status = 409;
		} elseif ( in_array( $code, array( 'BACKUP_STORAGE_UNAVAILABLE', 'INVALID_CONFIG', 'AUDIT_UNAVAILABLE' ), true ) ) {
			$status = 503;
		} elseif ( in_array( $code, array( 'ROLLBACK_WRITE_FAILED', 'ROLLBACK_VERIFICATION_FAILED' ), true ) ) {
			$status = 500;
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id' => $operation_id,
				'event_type'   => 'rollback' === $stage ? 'rollback_refused' : 'backup_refused',
				'route'        => '/pages/' . absint( $page_id ) . ( 'rollback' === $stage ? '/rollback' : '/backups' ),
				'actor_type'   => 'token',
				'target_type'  => 'page',
				'target_id'    => $page_id,
				'outcome'      => 'rejected',
				'reason_code'  => $code,
				'backup_id'    => $backup_id > 0 ? $backup_id : null,
			)
		);

		return WPilot_Response::error( $code, $message, $meta, $status, $details, $operation_id );
	}

	/**
	 * Map scoped-replace service errors into the REST envelope.
	 *
	 * @param WP_Error $error Service error.
	 * @param array    $meta Response metadata.
	 * @param string   $operation_id Operation ID.
	 * @param int      $page_id Page ID.
	 * @return WP_REST_Response
	 */
	private function scoped_replace_error_response( WP_Error $error, array $meta, $operation_id, $page_id ) {
		$code    = $error->get_error_code();
		$message = $error->get_error_message();
		$data    = $error->get_error_data();
		$data    = is_array( $data ) ? $data : array();

		$mutation_performed = ! empty( $data['mutation_performed'] );
		$backup_id          = isset( $data['backup_id'] ) ? absint( $data['backup_id'] ) : 0;

		$details = array(
			'stage'              => 'scoped_replace',
			'mutation_performed' => $mutation_performed,
			'rollback_available' => $backup_id > 0 || ! $mutation_performed,
		);

		foreach ( array( 'checksum_before', 'checksum_after', 'replacements_count', 'validation_result', 'replacement_confirmed' ) as $key ) {
			if ( array_key_exists( $key, $data ) ) {
				$details[ $key ] = $data[ $key ];
			}
		}

		$status = 400;
		if ( in_array( $code, array( 'TARGET_NOT_FOUND', 'ZERO_MATCHES' ), true ) ) {
			$status = 404;
		} elseif ( in_array( $code, array( 'MULTIPLE_MATCHES', 'CHECKSUM_MISMATCH', 'APPROVAL_REQUIRED' ), true ) ) {
			$status = 409;
		} elseif ( in_array( $code, array( 'BACKUP_STORAGE_UNAVAILABLE', 'INVALID_CONFIG', 'AUDIT_UNAVAILABLE' ), true ) ) {
			$status = 503;
		} elseif ( in_array( $code, array( 'WRITE_FAILED', 'POST_WRITE_VALIDATION_FAILED' ), true ) ) {
			$status = 500;
		} elseif ( in_array( $code, array( 'UNSAFE_WPBAKERY_ZONE', 'UNSAFE_CONTENT_TYPE', 'SAFE_UNKNOWN' ), true ) ) {
			$status = 422;
		}

		WPilot_Audit_Service::log_event(
			array(
				'operation_id'    => $operation_id,
				'event_type'      => $mutation_performed ? 'scoped_replace_failed' : 'scoped_replace_refused',
				'route'           => '/pages/' . absint( $page_id ) . '/scoped-replace',
				'actor_type'      => 'token',
				'target_type'     => 'page',
				'target_id'       => $page_id,
				'outcome'         => $mutation_performed ? 'failed' : 'rejected',
				'reason_code'     => $code,
				'backup_id'       => $backup_id > 0 ? $backup_id : null,
				'before_checksum' => isset( $data['checksum_before'] ) ? (string) $data['checksum_before'] : '',
				'after_checksum'  => isset( $data['checksum_after'] ) ? (string) $data['checksum_after'] : '',
				'metadata'        => array(
					'operation_type'     => WPilot_Scoped_Replace_Service::OPERATION_TYPE,
					'validation_result'  => isset( $data['validation_result'] ) ? (string) $data['validation_result'] : 'failed',
					'replacements_count' => isset( $data['replacements_count'] ) ? (string) $data['replacements_count'] : '',
				),
			)
		);

		return WPilot_Response::error( $code, $message, $meta, $status, $details, $operation_id );
	}

	/**
	 * Return a safe envelope for operational endpoint failures.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @param string          $endpoint_name Endpoint name.
	 * @param string          $operation_id Operation ID.
	 * @param string          $code Stable error code.
	 * @param string          $message Public operator-readable message.
	 * @param Throwable       $exception Captured exception.
	 * @param string          $stage Failure stage.
	 * @param int             $backup_id Optional backup ID.
	 * @return WP_REST_Response
	 */
	private function operation_failure( WP_REST_Request $request, $endpoint_name, $operation_id, $code, $message, Throwable $exception, $stage, $backup_id = 0 ) {
		$this->log_endpoint_failure( $endpoint_name, $request, $exception );

		WPilot_Audit_Service::log_event(
			array(
				'operation_id' => $operation_id,
				'event_type'   => 'rollback' === $stage ? 'rollback_failed' : ( 'scoped_replace' === $stage ? 'scoped_replace_failed' : 'backup_failed' ),
				'route'        => (string) $request->get_route(),
				'actor_type'   => 'token',
				'target_type'  => 'page',
				'target_id'    => $this->page_id_from_request( $request ),
				'outcome'      => 'failed',
				'reason_code'  => $code,
				'backup_id'    => $backup_id > 0 ? $backup_id : null,
			)
		);

		return WPilot_Response::error(
			$code,
			$message,
			$this->meta( $request, $endpoint_name ),
			500,
			array(
				'stage'              => $stage,
				'mutation_performed' => false,
				'rollback_available' => 'rollback' !== $stage,
			),
			$operation_id
		);
	}
}

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

	public function __construct() {
		$this->reader  = new WPilot_Site_Reader();
		$this->dry_run = new WPilot_Dry_Run();
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
}

<?php

/**

 * Admin UI data model for WPilot status and informational panels.

 *

 * Display-only layer. Does not alter runtime behavior.

 *

 * @package MetaCode_WPilot

 */



if ( ! defined( 'ABSPATH' ) ) {

	exit;

}



class WPilot_Admin_UI_Model {

	/**

	 * Runtime status fields for the dashboard panel.

	 *

	 * @return array<string, string>

	 */

	public static function runtime_status_dashboard() {

		return array(

			'version'           => WPilot_Constants::VERSION,

			'release_label'     => WPilot_Constants::RELEASE_LABEL,

			'schema_version'    => WPilot_Constants::SCHEMA_VERSION,

			'status'            => WPilot_Constants::RUNTIME_STATUS,

			'environment'       => WPilot_Constants::ENVIRONMENT,

			'runtime_maturity'  => WPilot_Constants::RUNTIME_MATURITY,

		);

	}



	/**

	 * Compact overview payload for the operator dashboard.

	 *

	 * @param array $options Plugin options snapshot.

	 * @return array<string, mixed>

	 */

	public static function overview_dashboard( array $options ) {

		$runtime   = self::runtime_status_dashboard();

		$connection = WPilot_Connection_Tracker::get_snapshot();

		$milestone = self::milestone_001();

		$surface   = self::runtime_surface();



		return array(

			'runtime'    => $runtime,

			'connection' => array(

				'label'               => __( 'Last MARS Connection', 'metacode-wpilot' ),

				'status'              => $connection['status'],

				'success_at'          => $connection['success_at'],

				'authorized_at'       => $connection['authorized_at'],

				'authorized_endpoint' => $connection['authorized_endpoint'],

				'failure_at'          => $connection['failure_at'],

				'failure_reason'      => $connection['failure_reason'],

			),

			'safety'     => array(

				'bridge'         => self::bridge_enabled_label( $options['bridge_enabled'] ),

				'write_readiness'=> self::write_enabled_label( $options['write_enabled'] ),

				'dev_confirmed'  => self::dev_confirmed_label( $options['dev_confirmed'] ),

			),

			'summary'    => array(

				'proven_operations_count' => count( self::proven_operations() ),

				'endpoints_count'         => (int) $surface['read_endpoints'] + (int) $surface['write_endpoints'],

				'last_milestone'          => $milestone['id'] . ' — ' . $milestone['status'],

			),

		);

	}



	/**

	 * Human-readable connection status label.

	 *

	 * @param string $status Connection status code.

	 * @return string

	 */

	public static function connection_status_label( $status ) {

		switch ( $status ) {

			case WPilot_Connection_Tracker::STATUS_SUCCESS:

				return __( 'success', 'metacode-wpilot' );

			case WPilot_Connection_Tracker::STATUS_FAILED:

				return __( 'failed', 'metacode-wpilot' );

			default:

				return __( 'never', 'metacode-wpilot' );

		}

	}



	/**

	 * Human-readable UTC timestamp or dash placeholder.

	 *

	 * @param string $timestamp UTC MySQL timestamp.

	 * @return string

	 */

	public static function format_utc_timestamp( $timestamp ) {

		return '' !== $timestamp ? $timestamp . ' UTC' : '—';

	}



	/**

	 * Proven operations register (state freeze source of truth).

	 *

	 * @return array<int, string>

	 */

	public static function proven_operations() {

		return array(

			__( 'Inspect', 'metacode-wpilot' ),

			__( 'Backup', 'metacode-wpilot' ),

			__( 'Apply Content Change', 'metacode-wpilot' ),

			__( 'Validate', 'metacode-wpilot' ),

			__( 'Rollback', 'metacode-wpilot' ),

			__( 'Audit Trail', 'metacode-wpilot' ),

			__( 'Checksum Validation', 'metacode-wpilot' ),

		);

	}



	/**

	 * REST surface counts aligned with registered routes inventory.

	 *

	 * @return array<string, int|string>

	 */

	public static function runtime_surface() {

		return array(

			'read_endpoints'  => WPilot_Constants::READ_ENDPOINT_COUNT,

			'write_endpoints' => WPilot_Constants::WRITE_ENDPOINT_COUNT,

			'namespace'       => WPilot_Constants::REST_NAMESPACE,

		);

	}



	/**

	 * Safety features displayed in the admin panel.

	 *

	 * @return array<int, string>

	 */

	public static function safety_features() {

		return array(

			__( 'Backup Before Apply', 'metacode-wpilot' ),

			__( 'Checksum Validation', 'metacode-wpilot' ),

			__( 'Audit Trail', 'metacode-wpilot' ),

			__( 'Rollback Available', 'metacode-wpilot' ),

			__( 'Human Approval Required', 'metacode-wpilot' ),

		);

	}



	/**

	 * Milestone 001 record (evidence register).

	 *

	 * @return array<string, string>

	 */

	public static function milestone_001() {

		return array(

			'id'     => WPilot_Constants::MILESTONE_001_ID,

			'title'  => __( 'First Proven Runtime Write Path', 'metacode-wpilot' ),

			'date'   => WPilot_Constants::MILESTONE_001_DATE,

			'status' => WPilot_Constants::MILESTONE_001_STATUS,

		);

	}



	/**

	 * REST endpoint inventory for admin documentation.

	 *

	 * @param string $rest_base REST base path including /wp-json/ prefix.

	 * @return array<string, array<int, string>>

	 */

	public static function endpoint_inventory( $rest_base ) {

		return array(

			'read' => array(

				'GET ' . $rest_base . '/ping',

				'GET ' . $rest_base . '/site-info',

				'GET ' . $rest_base . '/themes',

				'GET ' . $rest_base . '/plugins',

				'GET ' . $rest_base . '/pages',

				'GET ' . $rest_base . '/pages/{id}',

				'GET ' . $rest_base . '/pages/{id}/structure',

				'GET ' . $rest_base . '/indexing-state',

			),

			'analysis' => array(

				'POST ' . $rest_base . '/pages/{id}/replace-text/dry-run',

			),

			'write' => array(

				'POST ' . $rest_base . '/pages/{id}/backups',

				'POST ' . $rest_base . '/pages/{id}/rollback',

				'POST ' . $rest_base . '/pages/{id}/scoped-replace',

			),

		);

	}



	/**

	 * Human-readable write readiness label.

	 *

	 * @param bool $write_enabled Whether write readiness is enabled.

	 * @return string

	 */

	public static function write_enabled_label( $write_enabled ) {

		if ( $write_enabled ) {

			return __( 'enabled (dry-run analysis and proven write endpoints)', 'metacode-wpilot' );

		}



		return __( 'disabled', 'metacode-wpilot' );

	}



	/**

	 * Human-readable bridge enabled label.

	 *

	 * @param bool $bridge_enabled Whether the bridge is enabled.

	 * @return string

	 */

	public static function bridge_enabled_label( $bridge_enabled ) {

		return $bridge_enabled

			? __( 'enabled', 'metacode-wpilot' )

			: __( 'disabled', 'metacode-wpilot' );

	}



	/**

	 * Human-readable DEV confirmation label.

	 *

	 * @param bool $dev_confirmed Whether DEV/test use is confirmed.

	 * @return string

	 */

	public static function dev_confirmed_label( $dev_confirmed ) {

		return $dev_confirmed

			? __( 'confirmed', 'metacode-wpilot' )

			: __( 'not confirmed', 'metacode-wpilot' );

	}



	/**

	 * Human-readable emergency disable label.

	 *

	 * @param bool $emergency_disabled Whether emergency disable is active.

	 * @return string

	 */

	public static function emergency_disabled_label( $emergency_disabled ) {

		return $emergency_disabled

			? __( 'yes — all data endpoints refuse until cleared', 'metacode-wpilot' )

			: __( 'no', 'metacode-wpilot' );

	}



	/**

	 * Human-readable token status label.

	 *

	 * @param array $options Plugin options snapshot.

	 * @return string

	 */

	public static function token_status_label( array $options ) {

		return empty( $options['token_hash'] )

			? __( 'not generated', 'metacode-wpilot' )

			: __( 'generated', 'metacode-wpilot' );

	}

}



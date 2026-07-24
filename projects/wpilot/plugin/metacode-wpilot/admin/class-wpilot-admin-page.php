<?php

/**

 * WPilot admin dashboard with tabbed operator UX.

 *

 * @package MetaCode_WPilot

 */



if ( ! defined( 'ABSPATH' ) ) {

	exit;

}



class WPilot_Admin_Page {

	const PAGE_SLUG = WPilot_Constants::PLUGIN_SLUG;

	const NONCE_ACTION = 'wpilot_admin_action';

	const NONCE_NAME = 'wpilot_nonce';



	/**

	 * Token shown only for the request that generated it.

	 *

	 * @var string

	 */

	private $generated_token = '';



	/**

	 * Admin notice messages.

	 *

	 * @var array

	 */

	private $messages = array();



	/**

	 * Register top-level admin menu and legacy Settings alias.

	 *

	 * @return void

	 */

	public function register_menu() {

		add_menu_page(

			__( 'MetaCODE WPilot', 'metacode-wpilot' ),

			__( 'MetaCODE WPilot', 'metacode-wpilot' ),

			WPilot_Constants::CAPABILITY_MANAGE_OPTIONS,

			self::PAGE_SLUG,

			array( $this, 'render' ),

			'dashicons-shield-alt',

			81

		);



		add_submenu_page(

			self::PAGE_SLUG,

			__( 'Overview', 'metacode-wpilot' ),

			__( 'Overview', 'metacode-wpilot' ),

			WPilot_Constants::CAPABILITY_MANAGE_OPTIONS,

			self::PAGE_SLUG,

			array( $this, 'render' )

		);



		add_options_page(

			__( 'MetaCODE WPilot', 'metacode-wpilot' ),

			__( 'MetaCODE WPilot', 'metacode-wpilot' ),

			WPilot_Constants::CAPABILITY_MANAGE_OPTIONS,

			self::PAGE_SLUG,

			array( $this, 'render' )

		);

	}



	/**

	 * Tab definitions for the operator dashboard.

	 *

	 * @return array<string, string>

	 */

	private function get_tabs() {

		return array(

			'overview'     => __( 'Overview', 'metacode-wpilot' ),

			'runtime'      => __( 'Runtime', 'metacode-wpilot' ),

			'connection'   => __( 'Connection', 'metacode-wpilot' ),

			'endpoints'    => __( 'Endpoints', 'metacode-wpilot' ),

			'safety'       => __( 'Safety', 'metacode-wpilot' ),

			'diagnostics'  => __( 'Diagnostics', 'metacode-wpilot' ),

		);

	}



	/**

	 * Resolve active tab from request.

	 *

	 * @return string

	 */

	private function get_current_tab() {

		$tabs = $this->get_tabs();

		$tab  = isset( $_GET['tab'] ) ? sanitize_key( wp_unslash( $_GET['tab'] ) ) : 'overview';



		return array_key_exists( $tab, $tabs ) ? $tab : 'overview';

	}



	/**

	 * Build admin page URL for a tab.

	 *

	 * @param string $tab Tab slug.

	 * @return string

	 */

	private function tab_url( $tab ) {

		return add_query_arg(

			array(

				'page' => self::PAGE_SLUG,

				'tab'  => $tab,

			),

			admin_url( 'admin.php' )

		);

	}



	/**

	 * Render settings page and process admin actions.

	 *

	 * @return void

	 */

	public function render() {

		if ( ! current_user_can( WPilot_Constants::CAPABILITY_MANAGE_OPTIONS ) ) {

			wp_die( esc_html__( 'Permission denied.', 'metacode-wpilot' ) );

		}



		$this->handle_post();



		$options            = WPilot_Settings::get_options();

		$state              = WPilot_Settings::get_state();

		$rest_base          = '/wp-json/' . WPilot_Constants::REST_NAMESPACE;

		$current_tab        = $this->get_current_tab();

		$tabs               = $this->get_tabs();

		$overview           = WPilot_Admin_UI_Model::overview_dashboard( $options );

		$runtime_status     = WPilot_Admin_UI_Model::runtime_status_dashboard();

		$runtime_surface    = WPilot_Admin_UI_Model::runtime_surface();

		$connection         = WPilot_Connection_Tracker::get_snapshot();

		$milestone          = WPilot_Admin_UI_Model::milestone_001();

		$endpoint_inventory = WPilot_Admin_UI_Model::endpoint_inventory( $rest_base );

		?>

		<div class="wrap">

			<h1><?php echo esc_html__( 'MetaCODE WPilot', 'metacode-wpilot' ); ?></h1>



			<div class="notice notice-warning inline">

				<p><strong><?php echo esc_html__( 'DEV/test only. Do not enable this bridge on production.', 'metacode-wpilot' ); ?></strong></p>

			</div>



			<?php foreach ( $this->messages as $message ) : ?>

				<div class="notice notice-info is-dismissible">

					<p><?php echo esc_html( $message ); ?></p>

				</div>

			<?php endforeach; ?>



			<?php if ( '' !== $this->generated_token ) : ?>

				<div class="notice notice-success">

					<p><strong><?php echo esc_html__( 'Generated token. Copy it now; it will not be shown again.', 'metacode-wpilot' ); ?></strong></p>

					<p><?php echo esc_html__( 'Generating or rotating a token invalidates the previous operational credential. Store the plaintext only in approved local operator secret storage.', 'metacode-wpilot' ); ?></p>

					<p><code><?php echo esc_html( $this->generated_token ); ?></code></p>

				</div>

			<?php endif; ?>



			<nav class="nav-tab-wrapper wp-clearfix" aria-label="<?php echo esc_attr__( 'WPilot sections', 'metacode-wpilot' ); ?>">

				<?php foreach ( $tabs as $tab_slug => $tab_label ) : ?>

					<a href="<?php echo esc_url( $this->tab_url( $tab_slug ) ); ?>" class="nav-tab <?php echo $current_tab === $tab_slug ? 'nav-tab-active' : ''; ?>">

						<?php echo esc_html( $tab_label ); ?>

					</a>

				<?php endforeach; ?>

			</nav>



			<div class="wpilot-admin-tab-panel" style="margin-top: 16px;">

				<?php

				switch ( $current_tab ) {

					case 'runtime':

						$this->render_runtime_tab( $runtime_status, $runtime_surface );

						break;

					case 'connection':

						$this->render_connection_tab( $connection, $options );

						break;

					case 'endpoints':

						$this->render_endpoints_tab( $endpoint_inventory );

						break;

					case 'safety':

						$this->render_safety_tab( $options );

						break;

					case 'diagnostics':

						$this->render_diagnostics_tab( $state, $options, $milestone );

						break;

					default:

						$this->render_overview_tab( $overview );

						break;

				}

				?>

			</div>

		</div>

		<?php

	}



	/**

	 * Render compact operator overview.

	 *

	 * @param array<string, mixed> $overview Overview payload.

	 * @return void

	 */

	private function render_overview_tab( array $overview ) {

		?>

		<?php $this->render_compact_section( __( 'Runtime', 'metacode-wpilot' ), array(

			__( 'Status', 'metacode-wpilot' )           => $overview['runtime']['status'],

			__( 'Version', 'metacode-wpilot' )          => $overview['runtime']['version'],

			__( 'Schema', 'metacode-wpilot' )           => $overview['runtime']['schema_version'],

			__( 'Environment', 'metacode-wpilot' )      => $overview['runtime']['environment'],

			__( 'Runtime Maturity', 'metacode-wpilot' ) => $overview['runtime']['runtime_maturity'],

		) ); ?>



		<?php $this->render_compact_section( __( 'Connection', 'metacode-wpilot' ), array(

			__( 'Last successful connection', 'metacode-wpilot' ) => WPilot_Admin_UI_Model::format_utc_timestamp( $overview['connection']['authorized_at'] ),

			__( 'Last endpoint', 'metacode-wpilot' )                => '' !== $overview['connection']['authorized_endpoint'] ? $overview['connection']['authorized_endpoint'] : '—',

			__( 'Last failure', 'metacode-wpilot' )                   => WPilot_Admin_UI_Model::format_utc_timestamp( $overview['connection']['failure_at'] ),

			__( 'Failure reason', 'metacode-wpilot' )                 => '' !== $overview['connection']['failure_reason'] ? $overview['connection']['failure_reason'] : '—',

		) ); ?>



		<?php $this->render_compact_section( __( 'Safety', 'metacode-wpilot' ), array(

			__( 'Bridge', 'metacode-wpilot' )            => $overview['safety']['bridge'],

			__( 'Write Readiness', 'metacode-wpilot' )   => $overview['safety']['write_readiness'],

			__( 'DEV Confirmation', 'metacode-wpilot' )  => $overview['safety']['dev_confirmed'],

		) ); ?>



		<?php $this->render_compact_section( __( 'Summary', 'metacode-wpilot' ), array(

			__( 'Proven Operations Count', 'metacode-wpilot' ) => (string) $overview['summary']['proven_operations_count'],

			__( 'Endpoints Count', 'metacode-wpilot' )           => (string) $overview['summary']['endpoints_count'],

			__( 'Last Milestone', 'metacode-wpilot' )            => $overview['summary']['last_milestone'],

		) ); ?>

		<?php

	}



	/**

	 * Render runtime details tab.

	 *

	 * @param array<string, string>     $runtime_status Runtime fields.

	 * @param array<string, int|string> $runtime_surface Endpoint counts.

	 * @return void

	 */

	private function render_runtime_tab( array $runtime_status, array $runtime_surface ) {

		$this->render_compact_section( __( 'Runtime Status', 'metacode-wpilot' ), array(

			__( 'Status', 'metacode-wpilot' )           => $runtime_status['status'],

			__( 'Version', 'metacode-wpilot' )          => $runtime_status['version'],

			__( 'Schema Version', 'metacode-wpilot' )   => $runtime_status['schema_version'],

			__( 'Environment', 'metacode-wpilot' )      => $runtime_status['environment'],

			__( 'Runtime Maturity', 'metacode-wpilot' ) => $runtime_status['runtime_maturity'],

		) );



		$this->render_compact_section( __( 'Runtime Surface', 'metacode-wpilot' ), array(

			__( 'Read Endpoints', 'metacode-wpilot' )  => (string) $runtime_surface['read_endpoints'],

			__( 'Write Endpoints', 'metacode-wpilot' ) => (string) $runtime_surface['write_endpoints'],

			__( 'Namespace', 'metacode-wpilot' )       => (string) $runtime_surface['namespace'],

		) );



		$this->render_checklist_panel( __( 'Proven Operations', 'metacode-wpilot' ), WPilot_Admin_UI_Model::proven_operations() );

	}



	/**

	 * Render connection diagnostics tab.

	 *

	 * @param array<string, string> $connection Connection snapshot.

	 * @param array                 $options Plugin options.

	 * @return void

	 */

	private function render_connection_tab( array $connection, array $options ) {

		$rows = array(

			__( 'Last successful connection', 'metacode-wpilot' ) => WPilot_Admin_UI_Model::format_utc_timestamp( $connection['authorized_at'] ),

			__( 'Last endpoint', 'metacode-wpilot' )                => '' !== $connection['authorized_endpoint'] ? $connection['authorized_endpoint'] : '—',

			__( 'Last failure', 'metacode-wpilot' )                   => WPilot_Admin_UI_Model::format_utc_timestamp( $connection['failure_at'] ),

			__( 'Failure reason', 'metacode-wpilot' )                 => '' !== $connection['failure_reason'] ? $connection['failure_reason'] : '—',

		);



		$rows[ __( 'Token status', 'metacode-wpilot' ) ] = WPilot_Admin_UI_Model::token_status_label( $options );



		if ( ! empty( $options['last_token_used_at'] ) ) {

			$rows[ __( 'Last token use (UTC)', 'metacode-wpilot' ) ] = WPilot_Admin_UI_Model::format_utc_timestamp( $options['last_token_used_at'] );

		}



		$this->render_compact_section( __( 'MARS Connection Diagnostics', 'metacode-wpilot' ), $rows );



		?>

		<p class="description"><?php echo esc_html__( 'Connection diagnostics store safe metadata only. Tokens, headers, payloads, and secrets are never persisted.', 'metacode-wpilot' ); ?></p>

		<p class="description"><?php echo esc_html__( 'Auth header for MARS operators:', 'metacode-wpilot' ); ?> <code><?php echo esc_html( WPilot_Constants::TOKEN_HEADER_NAME ); ?></code></p>

		<?php

	}



	/**

	 * Render REST endpoints tab.

	 *

	 * @param array<string, array<int, string>> $endpoint_inventory Endpoint groups.

	 * @return void

	 */

	private function render_endpoints_tab( array $endpoint_inventory ) {

		$this->render_endpoint_inventory( $endpoint_inventory );

	}



	/**

	 * Render safety controls tab.

	 *

	 * @param array $options Plugin options.

	 * @return void

	 */

	private function render_safety_tab( array $options ) {

		$this->render_checklist_panel( __( 'Safety Features', 'metacode-wpilot' ), WPilot_Admin_UI_Model::safety_features() );



		$this->render_compact_section( __( 'Current Safety State', 'metacode-wpilot' ), array(

			__( 'Bridge enabled', 'metacode-wpilot' )       => WPilot_Admin_UI_Model::bridge_enabled_label( $options['bridge_enabled'] ),

			__( 'DEV/test confirmed', 'metacode-wpilot' )   => WPilot_Admin_UI_Model::dev_confirmed_label( $options['dev_confirmed'] ),

			__( 'Write enabled', 'metacode-wpilot' )        => WPilot_Admin_UI_Model::write_enabled_label( $options['write_enabled'] ),

			__( 'Emergency disabled', 'metacode-wpilot' )   => WPilot_Admin_UI_Model::emergency_disabled_label( $options['emergency_disabled'] ),

		) );



		?>

		<p><strong><?php echo esc_html__( 'Production prohibition:', 'metacode-wpilot' ); ?></strong> <?php echo esc_html__( 'If this WordPress site is production or production-like, leave the bridge and writes disabled until a separate operational charter authorizes them. Token generation alone does not enable the bridge or writes.', 'metacode-wpilot' ); ?></p>



		<h2><?php echo esc_html__( 'Bridge Control', 'metacode-wpilot' ); ?></h2>

		<form method="post">

			<?php wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME ); ?>

			<input type="hidden" name="wpilot_action" value="save_bridge">

			<p>

				<label>

					<input type="checkbox" name="dev_confirmed" value="1" <?php checked( $options['dev_confirmed'] ); ?>>

					<?php echo esc_html__( 'I confirm this is a DEV/test WordPress site, not production.', 'metacode-wpilot' ); ?>

				</label>

			</p>

			<p>

				<label>

					<input type="checkbox" name="bridge_enabled" value="1" <?php checked( $options['bridge_enabled'] ); ?>>

					<?php echo esc_html__( 'Enable authenticated REST bridge.', 'metacode-wpilot' ); ?>

				</label>

			</p>

			<p>

				<label>

					<input type="checkbox" name="write_enabled" value="1" <?php checked( $options['write_enabled'] ); ?>>

					<?php echo esc_html__( 'Enable write readiness for dry-run analysis and proven content mutation endpoints.', 'metacode-wpilot' ); ?>

				</label>

			</p>

			<?php submit_button( __( 'Save Bridge State', 'metacode-wpilot' ) ); ?>

		</form>



		<h2><?php echo esc_html__( 'Token Control', 'metacode-wpilot' ); ?></h2>

		<p><?php echo esc_html__( 'Token generation requires an authorized administrator and a valid security nonce. It does not require DEV/test confirmation, bridge enablement, or write readiness. Generating a token does not enable the bridge or writes. Rotating a token replaces the previous credential; plaintext is shown once.', 'metacode-wpilot' ); ?></p>

		<form method="post" style="display:inline-block; margin-right: 8px;">

			<?php wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME ); ?>

			<input type="hidden" name="wpilot_action" value="generate_token">

			<?php submit_button( __( 'Generate / Rotate Token', 'metacode-wpilot' ), 'secondary', 'submit', false ); ?>

		</form>

		<form method="post" style="display:inline-block;">

			<?php wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME ); ?>

			<input type="hidden" name="wpilot_action" value="revoke_token">

			<?php submit_button( __( 'Revoke Token', 'metacode-wpilot' ), 'secondary', 'submit', false ); ?>

		</form>



		<h2><?php echo esc_html__( 'Emergency Control', 'metacode-wpilot' ); ?></h2>

		<p><?php echo esc_html__( 'Emergency disable immediately turns the bridge off. Clearing emergency state does not re-enable the bridge.', 'metacode-wpilot' ); ?></p>

		<form method="post" style="display:inline-block; margin-right: 8px;">

			<?php wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME ); ?>

			<input type="hidden" name="wpilot_action" value="emergency_disable">

			<?php submit_button( __( 'Emergency Disable', 'metacode-wpilot' ), 'delete', 'submit', false ); ?>

		</form>

		<form method="post" style="display:inline-block;">

			<?php wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME ); ?>

			<input type="hidden" name="wpilot_action" value="clear_emergency">

			<?php submit_button( __( 'Clear Emergency Disable', 'metacode-wpilot' ), 'secondary', 'submit', false ); ?>

		</form>

		<?php

	}



	/**

	 * Render diagnostics tab.

	 *

	 * @param string              $state Plugin state code.

	 * @param array               $options Plugin options.

	 * @param array<string,string> $milestone Milestone record.

	 * @return void

	 */

	private function render_diagnostics_tab( $state, array $options, array $milestone ) {

		$this->render_milestone_panel( $milestone );



		$this->render_compact_section( __( 'Current State', 'metacode-wpilot' ), array(

			__( 'Plugin state', 'metacode-wpilot' )     => $state,

			__( 'REST namespace', 'metacode-wpilot' )   => WPilot_Constants::REST_NAMESPACE,

			__( 'Schema valid option', 'metacode-wpilot' ) => WPilot_Schema::is_valid() ? __( 'yes', 'metacode-wpilot' ) : __( 'no', 'metacode-wpilot' ),

			__( 'Token created at UTC', 'metacode-wpilot' ) => WPilot_Admin_UI_Model::format_utc_timestamp( $options['token_created_at'] ?? '' ),

			__( 'Token revoked at UTC', 'metacode-wpilot' )   => WPilot_Admin_UI_Model::format_utc_timestamp( $options['token_revoked_at'] ?? '' ),

		) );



		?>

		<p class="description"><?php echo esc_html__( 'WPilot v0.3.0 provides a proven DEV runtime with authenticated inspection, pre-apply analysis, scoped content mutation, backup, validation, rollback, and audit trail. Browser automation, background jobs, and autonomous behavior are not part of this plugin.', 'metacode-wpilot' ); ?></p>

		<?php

	}



	/**

	 * Render a compact key-value section.

	 *

	 * @param string               $title Section title.

	 * @param array<string,string> $rows Label/value pairs.

	 * @return void

	 */

	private function render_compact_section( $title, array $rows ) {

		?>

		<h2><?php echo esc_html( $title ); ?></h2>

		<table class="widefat striped" style="max-width: 760px;">

			<tbody>

				<?php foreach ( $rows as $label => $value ) : ?>

					<tr>

						<th scope="row" style="width: 42%;"><?php echo esc_html( $label ); ?></th>

						<td><code><?php echo esc_html( $value ); ?></code></td>

					</tr>

				<?php endforeach; ?>

			</tbody>

		</table>

		<?php

	}



	/**

	 * Render a checklist-style informational panel.

	 *

	 * @param string             $title Panel title.

	 * @param array<int, string> $items Checklist items.

	 * @return void

	 */

	private function render_checklist_panel( $title, array $items ) {

		?>

		<h2><?php echo esc_html( $title ); ?></h2>

		<ul class="ul-disc" style="max-width: 760px;">

			<?php foreach ( $items as $item ) : ?>

				<li><?php echo esc_html( '✓ ' . $item ); ?></li>

			<?php endforeach; ?>

		</ul>

		<?php

	}



	/**

	 * Render milestone 001 panel.

	 *

	 * @param array<string, string> $milestone Milestone record.

	 * @return void

	 */

	private function render_milestone_panel( array $milestone ) {

		$this->render_compact_section( __( 'Milestone 001', 'metacode-wpilot' ), array(

			__( 'Title', 'metacode-wpilot' )       => $milestone['title'],

			__( 'Date', 'metacode-wpilot' )        => $milestone['date'],

			__( 'Status', 'metacode-wpilot' )      => $milestone['status'],

			__( 'Milestone ID', 'metacode-wpilot' ) => $milestone['id'],

		) );

	}



	/**

	 * Render grouped REST endpoint inventory.

	 *

	 * @param array<string, array<int, string>> $endpoint_inventory Endpoint groups.

	 * @return void

	 */

	private function render_endpoint_inventory( array $endpoint_inventory ) {

		?>

		<p><?php echo esc_html__( 'Except for ping, endpoints require the documented token header and may expose site metadata, plugin/theme names, page lists, and raw page content for the requested DEV page.', 'metacode-wpilot' ); ?></p>

		<p><strong><?php echo esc_html__( 'Raw-content notice:', 'metacode-wpilot' ); ?></strong> <?php echo esc_html__( 'The page detail endpoint returns raw post content for inspection. Use only on approved DEV content and avoid business-sensitive pages.', 'metacode-wpilot' ); ?></p>



		<h2><?php echo esc_html__( 'Read Endpoints', 'metacode-wpilot' ); ?></h2>

		<ul>

			<?php foreach ( $endpoint_inventory['read'] as $route ) : ?>

				<li><code><?php echo esc_html( $route ); ?></code></li>

			<?php endforeach; ?>

		</ul>



		<h2><?php echo esc_html__( 'Analysis Endpoint', 'metacode-wpilot' ); ?></h2>

		<p><?php echo esc_html__( 'Pre-apply dry-run analyzes one exact scoped replacement without mutating content. Proven write endpoints create backups, audit records, and support rollback.', 'metacode-wpilot' ); ?></p>

		<ul>

			<?php foreach ( $endpoint_inventory['analysis'] as $route ) : ?>

				<li><code><?php echo esc_html( $route ); ?></code></li>

			<?php endforeach; ?>

		</ul>



		<h2><?php echo esc_html__( 'Proven Write Endpoints', 'metacode-wpilot' ); ?></h2>

		<ul>

			<?php foreach ( $endpoint_inventory['write'] as $route ) : ?>

				<li><code><?php echo esc_html( $route ); ?></code></li>

			<?php endforeach; ?>

		</ul>

		<?php

	}



	/**

	 * Handle nonce-protected admin actions.

	 *

	 * @return void

	 */

	private function handle_post() {

		$request_method = isset( $_SERVER['REQUEST_METHOD'] ) ? sanitize_text_field( wp_unslash( $_SERVER['REQUEST_METHOD'] ) ) : '';



		if ( 'POST' !== $request_method || empty( $_POST['wpilot_action'] ) ) {

			return;

		}



		check_admin_referer( self::NONCE_ACTION, self::NONCE_NAME );



		$action  = sanitize_text_field( wp_unslash( $_POST['wpilot_action'] ) );

		$options = WPilot_Settings::get_options();



		switch ( $action ) {

			case 'save_bridge':

				$dev_confirmed             = ! empty( $_POST['dev_confirmed'] );

				$bridge_enabled            = ! empty( $_POST['bridge_enabled'] );

				$write_enabled             = ! empty( $_POST['write_enabled'] );

				$options['dev_confirmed']  = $dev_confirmed;

				$options['bridge_enabled'] = $dev_confirmed && $bridge_enabled;

				$options['write_enabled']  = $dev_confirmed && $bridge_enabled && $write_enabled;



				WPilot_Settings::update_options( $options, true );

				$this->messages[] = __( 'Bridge settings saved.', 'metacode-wpilot' );

				break;



			case 'generate_token':

				if ( ! WPilot_Environment::can_manage_token( $options ) ) {

					$this->messages[] = __( 'Token generation requires an authorized administrator and must not run while emergency disable is active.', 'metacode-wpilot' );

					break;

				}



				$this->generated_token = WPilot_Settings::generate_token();

				$this->messages[]      = __( 'Token generated. Plaintext is shown once below.', 'metacode-wpilot' );

				break;



			case 'revoke_token':

				WPilot_Settings::revoke_token();

				$this->messages[] = __( 'Token revoked.', 'metacode-wpilot' );

				break;



			case 'emergency_disable':

				$options['emergency_disabled'] = true;

				$options['bridge_enabled']     = false;

				$options['write_enabled']      = false;

				WPilot_Settings::update_options( $options );

				$this->messages[] = __( 'Emergency disable is active.', 'metacode-wpilot' );

				break;



			case 'clear_emergency':

				$options['emergency_disabled'] = false;

				$options['bridge_enabled']     = false;

				$options['write_enabled']      = false;

				WPilot_Settings::update_options( $options );

				$this->messages[] = __( 'Emergency disable cleared. Bridge remains disabled.', 'metacode-wpilot' );

				break;

		}

	}

}



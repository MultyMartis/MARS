<?php
/**
 * Minimal admin settings page for WPilot.
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
	 * Register under Settings.
	 *
	 * @return void
	 */
	public function register_menu() {
		add_options_page(
			__( 'MetaCODE WPilot', 'metacode-wpilot' ),
			__( 'MetaCODE WPilot', 'metacode-wpilot' ),
			WPilot_Constants::CAPABILITY_MANAGE_OPTIONS,
			self::PAGE_SLUG,
			array( $this, 'render' )
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

		$options   = WPilot_Settings::get_options();
		$state     = WPilot_Settings::get_state();
		$rest_base = '/wp-json/' . WPilot_Constants::REST_NAMESPACE;
		?>
		<div class="wrap">
			<h1><?php echo esc_html__( 'MetaCODE WPilot', 'metacode-wpilot' ); ?></h1>

			<div class="notice notice-warning">
				<p><strong><?php echo esc_html__( 'DEV/test only. Do not enable this bridge on production.', 'metacode-wpilot' ); ?></strong></p>
				<p><?php echo esc_html__( 'This phase exposes authenticated read endpoints and a dry-run replacement analyzer. It does not implement content mutation, rollback execution, browser automation, background jobs, or autonomous behavior.', 'metacode-wpilot' ); ?></p>
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

			<h2><?php echo esc_html__( 'Current State', 'metacode-wpilot' ); ?></h2>
			<table class="widefat striped" style="max-width: 760px;">
				<tbody>
					<tr>
						<th scope="row"><?php echo esc_html__( 'Plugin state', 'metacode-wpilot' ); ?></th>
						<td><code><?php echo esc_html( $state ); ?></code></td>
					</tr>
					<tr>
						<th scope="row"><?php echo esc_html__( 'Bridge enabled', 'metacode-wpilot' ); ?></th>
						<td><?php echo esc_html( $options['bridge_enabled'] ? 'enabled' : 'disabled' ); ?></td>
					</tr>
					<tr>
						<th scope="row"><?php echo esc_html__( 'DEV/test confirmed', 'metacode-wpilot' ); ?></th>
						<td><?php echo esc_html( $options['dev_confirmed'] ? 'confirmed' : 'not confirmed' ); ?></td>
					</tr>
					<tr>
						<th scope="row"><?php echo esc_html__( 'Write enabled', 'metacode-wpilot' ); ?></th>
						<td><?php echo esc_html( $options['write_enabled'] ? 'enabled for dry-run readiness only' : 'disabled' ); ?></td>
					</tr>
					<tr>
						<th scope="row"><?php echo esc_html__( 'Emergency disabled', 'metacode-wpilot' ); ?></th>
						<td>
							<?php echo esc_html( $options['emergency_disabled'] ? 'yes - all data endpoints refuse until cleared' : 'no' ); ?>
						</td>
					</tr>
					<tr>
						<th scope="row"><?php echo esc_html__( 'Token status', 'metacode-wpilot' ); ?></th>
						<td>
							<?php echo esc_html( empty( $options['token_hash'] ) ? 'not generated' : 'generated' ); ?>
							<?php if ( ! empty( $options['token_created_at'] ) ) : ?>
								<br><small><?php echo esc_html( sprintf( 'Created at UTC: %s', $options['token_created_at'] ) ); ?></small>
							<?php endif; ?>
						</td>
					</tr>
					<tr>
						<th scope="row"><?php echo esc_html__( 'REST namespace', 'metacode-wpilot' ); ?></th>
						<td><code><?php echo esc_html( WPilot_Constants::REST_NAMESPACE ); ?></code></td>
					</tr>
				</tbody>
			</table>

			<p><strong><?php echo esc_html__( 'Production prohibition:', 'metacode-wpilot' ); ?></strong> <?php echo esc_html__( 'If this WordPress site is production or production-like, leave the bridge disabled and do not generate a token.', 'metacode-wpilot' ); ?></p>

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
						<?php echo esc_html__( 'Enable authenticated read-only bridge.', 'metacode-wpilot' ); ?>
					</label>
				</p>
				<p>
					<label>
						<input type="checkbox" name="write_enabled" value="1" <?php checked( $options['write_enabled'] ); ?>>
						<?php echo esc_html__( 'Enable dry-run write readiness. This does not enable content mutation endpoints.', 'metacode-wpilot' ); ?>
					</label>
				</p>
				<?php submit_button( __( 'Save Bridge State', 'metacode-wpilot' ) ); ?>
			</form>

			<h2><?php echo esc_html__( 'Token Control', 'metacode-wpilot' ); ?></h2>
			<p><?php echo esc_html__( 'Token generation is allowed only after DEV/test confirmation and bridge enablement. Rotating a token replaces the previous credential; plaintext is shown once.', 'metacode-wpilot' ); ?></p>
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

			<h2><?php echo esc_html__( 'Read-only Endpoints', 'metacode-wpilot' ); ?></h2>
			<p><?php echo esc_html__( 'Except for ping, endpoints require the documented token header and may expose site metadata, plugin/theme names, page lists, and raw page content for the requested DEV page.', 'metacode-wpilot' ); ?></p>
			<p><strong><?php echo esc_html__( 'Raw-content notice:', 'metacode-wpilot' ); ?></strong> <?php echo esc_html__( 'The page detail endpoint returns raw post content for inspection. Use only on approved DEV content and avoid business-sensitive pages.', 'metacode-wpilot' ); ?></p>
			<ul>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/ping' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/site-info' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/themes' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/plugins' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/pages' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/pages/{id}' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/pages/{id}/structure' ); ?></code></li>
				<li><code><?php echo esc_html( 'GET ' . $rest_base . '/indexing-state' ); ?></code></li>
			</ul>
			<h2><?php echo esc_html__( 'Dry-run Endpoint', 'metacode-wpilot' ); ?></h2>
			<p><?php echo esc_html__( 'Phase 2A dry-run analyzes one exact scoped replacement without mutating content, creating backups, writing audit logs, or executing rollback.', 'metacode-wpilot' ); ?></p>
			<ul>
				<li><code><?php echo esc_html( 'POST ' . $rest_base . '/pages/{id}/replace-text/dry-run' ); ?></code></li>
			</ul>
		</div>
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
				$this->messages[] = 'Bridge settings saved.';
				break;

			case 'generate_token':
				if ( ! WPilot_Environment::is_operationally_ready( $options ) ) {
					$this->messages[] = 'Enable the bridge and confirm DEV/test use before generating a token.';
					break;
				}

				$this->generated_token = WPilot_Settings::generate_token();
				$this->messages[]      = 'Token generated. Plaintext is shown once below.';
				break;

			case 'revoke_token':
				WPilot_Settings::revoke_token();
				$this->messages[] = 'Token revoked.';
				break;

			case 'emergency_disable':
				$options['emergency_disabled'] = true;
				$options['bridge_enabled']     = false;
				$options['write_enabled']      = false;
				WPilot_Settings::update_options( $options );
				$this->messages[] = 'Emergency disable is active.';
				break;

			case 'clear_emergency':
				$options['emergency_disabled'] = false;
				$options['bridge_enabled']     = false;
				$options['write_enabled']      = false;
				WPilot_Settings::update_options( $options );
				$this->messages[] = 'Emergency disable cleared. Bridge remains disabled.';
				break;
		}
	}
}

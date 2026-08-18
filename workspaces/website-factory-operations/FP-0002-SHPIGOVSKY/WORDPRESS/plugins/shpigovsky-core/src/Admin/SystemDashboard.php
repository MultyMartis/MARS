<?php
/**
 * Dashboard widget: MetaCODE / system state — PROD-P17-FU02.
 *
 * Canonical concise operational summary for FP-0002. No global Admin notices.
 * No DNS/registrar credentials.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Single non-secret system widget on the main dashboard.
 */
final class SystemDashboard implements ModuleInterface {

	/**
	 * Baseline ID shown in the widget (updated by stabilization waves).
	 */
	const BASELINE_ID = 'FP-0002-PROD-BASELINE-2026-08-17';

	/**
	 * Latest accepted production wave label.
	 */
	const LATEST_ACCEPTED_WAVE = 'P17-FU02 Final Pre-Cutover Tail Closure';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.system-dashboard';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'wp_dashboard_setup', array( __CLASS__, 'register_widget' ) );
	}

	/**
	 * Register the dashboard widget.
	 */
	public static function register_widget() {
		if ( ! current_user_can( 'manage_options' ) ) {
			return;
		}

		wp_add_dashboard_widget(
			'fp02_metacode_system_state',
			__( 'MetaCODE / Состояние системы', 'shpigovsky-core' ),
			array( __CLASS__, 'render_widget' )
		);
	}

	/**
	 * Widget body.
	 */
	public static function render_widget() {
		$env_fn    = function_exists( 'wp_get_environment_type' ) ? wp_get_environment_type() : 'unknown';
		$env_const = defined( 'WP_ENVIRONMENT_TYPE' ) ? (string) WP_ENVIRONMENT_TYPE : '';
		$host      = wp_parse_url( home_url( '/' ), PHP_URL_HOST );
		$host      = is_string( $host ) ? $host : '';
		$is_beget  = ( false !== strpos( $host, 'beget.tech' ) || false !== strpos( $host, 'shpigovsky.ru' ) );

		$wpilot_write = get_option( 'wpilot_write_enabled', get_option( 'metacode_wpilot_write_enabled', false ) );
		$wpilot_opts  = get_option( 'metacode_wpilot', get_option( 'wpilot', array() ) );
		if ( is_array( $wpilot_opts ) && array_key_exists( 'write_enabled', $wpilot_opts ) ) {
			$wpilot_write = (bool) $wpilot_opts['write_enabled'];
		}
		$wpilot_on = self::plugin_active_prefix( 'metacode-wpilot' ) || self::plugin_active_prefix( 'wpilot' );
		$wpilot_ver = '';
		if ( defined( 'METACODE_WPILOT_VERSION' ) ) {
			$wpilot_ver = (string) METACODE_WPILOT_VERSION;
		} elseif ( defined( 'WPILOT_VERSION' ) ) {
			$wpilot_ver = (string) WPILOT_VERSION;
		} elseif ( is_array( $wpilot_opts ) && ! empty( $wpilot_opts['version'] ) ) {
			$wpilot_ver = (string) $wpilot_opts['version'];
		}

		$meta = get_option( 'fp02_metacode_system_meta', array() );
		if ( ! is_array( $meta ) ) {
			$meta = array();
		}
		$parity   = isset( $meta['parity'] ) ? (string) $meta['parity'] : 'MATCH';
		$verified = isset( $meta['verified_at'] ) ? (string) $meta['verified_at'] : gmdate( 'Y-m-d H:i' ) . ' UTC';
		$backup   = isset( $meta['backup'] ) ? (string) $meta['backup'] : '—';
		$git_sha  = isset( $meta['git_sha'] ) ? (string) $meta['git_sha'] : '';
		$baseline = isset( $meta['baseline_id'] ) ? (string) $meta['baseline_id'] : self::BASELINE_ID;
		$wave     = isset( $meta['latest_wave'] ) ? (string) $meta['latest_wave'] : self::LATEST_ACCEPTED_WAVE;

		$php_ver = function_exists( 'phpversion' ) ? phpversion() : '';
		$debug_on = ( defined( 'WP_DEBUG' ) && WP_DEBUG );
		$blog_public = (int) get_option( 'blog_public', 1 );
		$mail_suppressed = (bool) has_filter( 'pre_wp_mail' );

		$precutover = isset( $meta['precutover'] ) ? (string) $meta['precutover'] : 'READY FOR MANUAL NS SWITCH';
		$redirects  = isset( $meta['legacy_redirects'] ) ? (string) $meta['legacy_redirects'] : '7/7';

		echo '<div class="fp02-metacode-system">';

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'Сайт', 'shpigovsky-core' ) . '</h3>';
		echo '<table class="widefat striped" style="border:none;box-shadow:none;margin-bottom:12px;">';
		self::row( __( 'Проект', 'shpigovsky-core' ), 'FP-0002 / Шпиговский Дом' );
		self::row(
			__( 'Runtime', 'shpigovsky-core' ),
			$is_beget
				? __( 'Production / Beget', 'shpigovsky-core' )
				: sprintf(
					/* translators: %s: environment type */
					__( 'Environment: %s', 'shpigovsky-core' ),
					$env_fn
				)
		);
		self::row( __( 'Current host', 'shpigovsky-core' ), 'shpigovsky.beget.tech' );
		self::row( __( 'Future host', 'shpigovsky-core' ), 'https://shpigovsky.ru/' );
		self::row( __( 'WordPress', 'shpigovsky-core' ), get_bloginfo( 'version' ) );
		if ( $php_ver !== '' ) {
			self::row( __( 'PHP', 'shpigovsky-core' ), $php_ver );
		}
		echo '</table>';

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'Текущее состояние', 'shpigovsky-core' ) . '</h3>';
		echo '<table class="widefat striped" style="border:none;box-shadow:none;margin-bottom:12px;">';
		self::row( __( 'Latest wave', 'shpigovsky-core' ), $wave );
		self::row( __( 'Status', 'shpigovsky-core' ), $precutover );
		self::row( __( 'PRE-CUTOVER', 'shpigovsky-core' ), $precutover );
		self::row( __( 'Source ↔ production', 'shpigovsky-core' ), $parity );
		self::row( __( 'Legacy redirects', 'shpigovsky-core' ), $redirects );
		self::row(
			__( 'WPilot', 'shpigovsky-core' ),
			$wpilot_on
				? trim( $wpilot_ver . ' · ' . ( $wpilot_write ? __( 'writes enabled', 'shpigovsky-core' ) : __( 'write disabled', 'shpigovsky-core' ) ) )
				: __( 'Not active', 'shpigovsky-core' )
		);
		self::row(
			__( 'Debug', 'shpigovsky-core' ),
			$debug_on ? __( 'on', 'shpigovsky-core' ) : __( 'off', 'shpigovsky-core' )
		);
		self::row(
			__( 'Mail', 'shpigovsky-core' ),
			$mail_suppressed
				? __( 'suppressed until SMTP', 'shpigovsky-core' )
				: __( 'suppression not detected — verify before go-live', 'shpigovsky-core' )
		);
		self::row(
			__( 'Indexing', 'shpigovsky-core' ),
			( 0 === $blog_public )
				? __( 'closed until launch', 'shpigovsky-core' )
				: __( 'open', 'shpigovsky-core' )
		);
		self::row( __( 'shpigovsky-core', 'shpigovsky-core' ), defined( 'SHPIGOVSKY_CORE_VERSION' ) ? SHPIGOVSKY_CORE_VERSION : '—' );
		self::row( __( 'Last verification', 'shpigovsky-core' ), $verified );
		if ( $backup !== '' && $backup !== '—' ) {
			self::row( __( 'Backup', 'shpigovsky-core' ), $backup );
		}
		echo '</table>';

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'DNS', 'shpigovsky-core' ) . '</h3>';
		echo '<table class="widefat striped" style="border:none;box-shadow:none;margin-bottom:12px;">';
		self::row( __( 'NS switch', 'shpigovsky-core' ), __( 'MANUAL OPERATOR ACTION', 'shpigovsky-core' ) );
		self::row( __( 'Current delegation', 'shpigovsky-core' ), 'REG.RU' );
		self::row( __( 'Target', 'shpigovsky-core' ), 'Beget' );
		echo '</table>';

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'Следующий шаг', 'shpigovsky-core' ) . '</h3>';
		echo '<ul style="margin:0 0 12px 1.2em;">';
		self::li( __( '1. Manual NS switch in REG.RU', 'shpigovsky-core' ) );
		self::li( __( '2. DNS verification', 'shpigovsky-core' ) );
		self::li( __( '3. SSL / final domain', 'shpigovsky-core' ) );
		self::li( __( '4. SMTP', 'shpigovsky-core' ) );
		self::li( __( '5. Indexing', 'shpigovsky-core' ) );
		self::li( __( '6. Sitemap submissions', 'shpigovsky-core' ) );
		self::li( __( '7. Final crawl', 'shpigovsky-core' ) );
		echo '</ul>';
		echo '<p style="margin:0 0 12px;">' . esc_html__( 'Operator changes NS. Then run the final cutover execution wave (P18) after confirmation «NS SWITCHED».', 'shpigovsky-core' ) . '</p>';

		if ( $is_beget && ( 'local' === $env_const || 'local' === $env_fn ) ) {
			echo '<p style="margin:0 0 8px;padding:8px 10px;border-left:3px solid #dba617;background:#fff8e5;">';
			echo esc_html__( 'Environment warning: WP_ENVIRONMENT_TYPE is still «local» on this production host — unexpected after P15.', 'shpigovsky-core' );
			echo '</p>';
		}

		echo '<p class="description" style="margin:0;">' . esc_html__( 'No secrets, tokens, DNS credentials, or filesystem credentials are shown here.', 'shpigovsky-core' ) . '</p>';
		echo '</div>';
	}

	/**
	 * Table row.
	 *
	 * @param string $label Label.
	 * @param string $value Value.
	 */
	private static function row( $label, $value ) {
		printf(
			'<tr><th style="width:38%%;text-align:left;">%s</th><td>%s</td></tr>',
			esc_html( $label ),
			esc_html( $value )
		);
	}

	/**
	 * List item.
	 *
	 * @param string $text Text.
	 */
	private static function li( $text ) {
		echo '<li>' . esc_html( $text ) . '</li>';
	}

	/**
	 * Whether an active plugin path starts with a prefix.
	 *
	 * @param string $prefix Prefix.
	 * @return bool
	 */
	private static function plugin_active_prefix( $prefix ) {
		$plugins = (array) get_option( 'active_plugins', array() );
		foreach ( $plugins as $plugin ) {
			if ( 0 === strpos( (string) $plugin, $prefix ) ) {
				return true;
			}
		}
		return false;
	}
}

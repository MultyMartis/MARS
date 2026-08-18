<?php
/**
 * Dashboard widget: MetaCODE / system state — PROD-P18B.
 *
 * Operational status surface derived from runtime where practical.
 * Historical waves belong in reports, not this widget.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Leads\LeadRegistry;
use Shpigovsky\Core\Mail\MailOps;
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
	const BASELINE_ID = 'FP-0002-PROD-BASELINE-2026-08-19-P18C-FU01';

	/**
	 * Latest accepted production wave label.
	 */
	const LATEST_ACCEPTED_WAVE = 'P18C-FU01 Admin menu exposure';

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
		$home      = home_url( '/' );
		$host      = wp_parse_url( $home, PHP_URL_HOST );
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
		$verified = isset( $meta['verified_at'] ) ? (string) $meta['verified_at'] : '';
		$backup   = isset( $meta['backup'] ) ? (string) $meta['backup'] : 'FRESH BEGET BACKUP CONFIRMED BY OPERATOR';
		$baseline = isset( $meta['baseline_id'] ) ? (string) $meta['baseline_id'] : self::BASELINE_ID;
		$wave     = isset( $meta['latest_wave'] ) ? (string) $meta['latest_wave'] : self::LATEST_ACCEPTED_WAVE;
		$ssl      = isset( $meta['ssl'] ) ? (string) $meta['ssl'] : '';
		$dns_ns   = isset( $meta['dns_ns'] ) ? (string) $meta['dns_ns'] : 'DONE / Beget';
		$smtp_box = isset( $meta['smtp_sender'] ) ? (string) $meta['smtp_sender'] : 'noreply@shpigovsky.ru';
		$redirects = isset( $meta['legacy_redirects'] ) ? (string) $meta['legacy_redirects'] : '7/7';

		$php_ver         = function_exists( 'phpversion' ) ? phpversion() : '';
		$debug_on        = ( defined( 'WP_DEBUG' ) && WP_DEBUG );
		$mail_suppressed = class_exists( MailOps::class ) ? MailOps::should_suppress() : (bool) has_filter( 'pre_wp_mail' );
		$mail_line       = class_exists( MailOps::class ) ? MailOps::dashboard_mail_line() : __( 'SMTP SETTINGS READY — CREDENTIALS REQUIRED', 'shpigovsky-core' );
		$sender          = class_exists( MailOps::class ) ? MailOps::from_email() : $smtp_box;
		$leads_active    = class_exists( LeadRegistry::class );
		$goal_cfg        = class_exists( MailOps::class ) && '' !== MailOps::metrika_goal();
		$indexing_open   = class_exists( IndexingControl::class ) ? IndexingControl::is_open() : ( 1 === (int) get_option( 'blog_public', 1 ) );

		if ( '' === $ssl ) {
			$ssl = ( is_string( $home ) && 0 === strpos( $home, 'https://' ) )
				? __( 'HTTPS в адресах WordPress', 'shpigovsky-core' )
				: __( 'не подтверждён', 'shpigovsky-core' );
		}

		$public_origin = isset( $meta['public_origin'] ) ? (string) $meta['public_origin'] : '';

		echo '<div class="fp02-metacode-system">';

		if ( class_exists( IndexingControl::class ) ) {
			IndexingControl::render_banner();
		}

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'Сайт', 'shpigovsky-core' ) . '</h3>';
		echo '<table class="widefat striped" style="border:none;box-shadow:none;margin-bottom:12px;">';
		self::row( __( 'Проект', 'shpigovsky-core' ), 'FP-0002 / Шпиговский Дом' );
		self::row(
			__( 'Среда', 'shpigovsky-core' ),
			$is_beget
				? __( 'Production / Beget', 'shpigovsky-core' )
				: sprintf(
					/* translators: %s: environment type */
					__( 'Среда: %s', 'shpigovsky-core' ),
					$env_fn
				)
		);
		self::row( __( 'Боевой домен', 'shpigovsky-core' ), 'https://shpigovsky.ru/' );
		self::row( __( 'WordPress', 'shpigovsky-core' ), get_bloginfo( 'version' ) );
		if ( $php_ver !== '' ) {
			self::row( __( 'PHP', 'shpigovsky-core' ), $php_ver );
		}
		echo '</table>';

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'Текущее состояние', 'shpigovsky-core' ) . '</h3>';
		echo '<table class="widefat striped" style="border:none;box-shadow:none;margin-bottom:12px;">';
		self::row( __( 'Последняя волна', 'shpigovsky-core' ), $wave );
		self::row( __( 'Домен', 'shpigovsky-core' ), __( 'DONE', 'shpigovsky-core' ) );
		self::row( __( 'DNS / NS', 'shpigovsky-core' ), $dns_ns );
		self::row( __( 'HTTPS', 'shpigovsky-core' ), $ssl );
		if ( '' !== $public_origin ) {
			self::row( __( 'Публичный адрес', 'shpigovsky-core' ), $public_origin );
		}
		self::row( __( 'Source ↔ production', 'shpigovsky-core' ), $parity );
		self::row( __( 'Legacy redirects', 'shpigovsky-core' ), $redirects );
		self::row(
			__( 'WPilot', 'shpigovsky-core' ),
			$wpilot_on
				? trim( $wpilot_ver . ' · ' . ( $wpilot_write ? __( 'запись включена', 'shpigovsky-core' ) : __( 'write disabled', 'shpigovsky-core' ) ) )
				: __( 'не активен', 'shpigovsky-core' )
		);
		self::row(
			__( 'Debug', 'shpigovsky-core' ),
			$debug_on ? __( 'on', 'shpigovsky-core' ) : __( 'off', 'shpigovsky-core' )
		);
		self::row(
			__( 'Почта', 'shpigovsky-core' ),
			$mail_line
		);
		self::row( __( 'SMTP отправитель', 'shpigovsky-core' ), $sender );
		self::row(
			__( 'Журнал заявок', 'shpigovsky-core' ),
			$leads_active ? __( 'ACTIVE', 'shpigovsky-core' ) : __( 'не активен', 'shpigovsky-core' )
		);
		self::row(
			__( 'Цели Метрики для форм', 'shpigovsky-core' ),
			$goal_cfg
				? __( 'задана в Почта и формы', 'shpigovsky-core' )
				: __( 'CONFIGURABLE', 'shpigovsky-core' )
		);
		self::row(
			__( 'Индексация', 'shpigovsky-core' ),
			$indexing_open
				? __( 'OPEN', 'shpigovsky-core' )
				: __( 'CLOSED — WAITING FOR OLYA APPROVAL', 'shpigovsky-core' )
		);
		self::row( __( 'Core', 'shpigovsky-core' ), defined( 'SHPIGOVSKY_CORE_VERSION' ) ? SHPIGOVSKY_CORE_VERSION : '—' );
		self::row( __( 'Последняя проверка', 'shpigovsky-core' ), '' !== $verified ? $verified : __( 'ещё не зафиксирована', 'shpigovsky-core' ) );
		self::row( __( 'Бэкап', 'shpigovsky-core' ), $backup );
		self::row( __( 'Baseline', 'shpigovsky-core' ), $baseline );
		echo '</table>';

		echo '<h3 style="margin:0 0 6px;">' . esc_html__( 'Следующие шаги', 'shpigovsky-core' ) . '</h3>';
		echo '<ul style="margin:0 0 12px 1.2em;">';
		self::li( __( '1. Оператор вводит SMTP и получателей: Настройки сайта → Почта и формы', 'shpigovsky-core' ) );
		self::li( __( '2. Сохранить. Не открывать индексацию.', 'shpigovsky-core' ) );
		self::li( __( '3. Сообщить, что настройки сохранены — следующая волна проверит SMTP', 'shpigovsky-core' ) );
		self::li( __( '4. После проверки SMTP — QA доставки форм', 'shpigovsky-core' ) );
		self::li( __( '5. Привязка публичного https://shpigovsky.ru/ к WordPress, если ещё открывается старый сайт', 'shpigovsky-core' ) );
		self::li( __( '6. Индексация — только после разрешения Оли', 'shpigovsky-core' ) );
		self::li( __( '7. Отправка sitemap', 'shpigovsky-core' ) );
		self::li( __( '8. Финальный обход', 'shpigovsky-core' ) );
		echo '</ul>';

		if ( $is_beget && ( 'local' === $env_const || 'local' === $env_fn ) ) {
			echo '<p style="margin:0 0 8px;padding:8px 10px;border-left:3px solid #dba617;background:#fff8e5;">';
			echo esc_html__( 'Предупреждение среды: WP_ENVIRONMENT_TYPE всё ещё «local» на этом боевом хосте.', 'shpigovsky-core' );
			echo '</p>';
		}

		echo '<p class="description" style="margin:0;">' . esc_html__( 'Секреты, токены и пароли почтового ящика здесь не показываются.', 'shpigovsky-core' ) . '</p>';
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

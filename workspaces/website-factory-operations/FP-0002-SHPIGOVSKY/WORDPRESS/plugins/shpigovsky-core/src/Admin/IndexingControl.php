<?php
/**
 * Canonical site indexability owner + Dashboard control — PROD-P18B / P18G guard.
 *
 * SET SITE INDEXABILITY = OPEN / CLOSED.
 * Non-human OPEN→CLOSED is blocked by default (PROD-P18G).
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
 * One semantic indexing operation for blog_public, robots.txt, and site-level meta robots.
 *
 * Ownership split (PROD-MAINT Olya robots):
 * - Humans own global OPEN/CLOSED indexability.
 * - Olya/SEO owns the OPEN-state robots crawl policy (canonical file in plugin assets).
 * - CLOSED may write a temporary global Disallow; OPEN must restore the SEO policy intact.
 */
final class IndexingControl implements ModuleInterface {

	const ACTION                = 'fp02_set_indexability';
	const NONCE                 = 'fp02_set_indexability';
	const CAPABILITY            = 'manage_options';
	const CONFIRM_FIELD         = 'fp02_confirm';
	const CLOSE_ACK_FIELD       = 'fp02_close_ack';
	const STATE_FIELD           = 'fp02_indexability';
	const NOTICE_QUERY          = 'fp02_indexing';
	const ROBOTS_RELATIVE       = 'robots.txt';
	const SEO_POLICY_RELATIVE   = 'assets/robots-seo-policy.txt';
	const SEO_BACKUP_RELATIVE   = 'robots.txt.fp02-seo-open.bak';
	const TECHNICAL_CLOSE_CONST = 'FP02_INDEXING_TECHNICAL_CLOSE_AUTHORIZED';

	/**
	 * In-request flag: authorized mutation is in progress.
	 *
	 * @var bool
	 */
	private static $authorized_mutation = false;

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.indexing-control';
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
		add_action( 'admin_post_' . self::ACTION, array( __CLASS__, 'handle_admin_post' ) );
		add_action( 'admin_notices', array( __CLASS__, 'render_admin_notice' ) );
		add_filter( 'pre_update_option_blog_public', array( __CLASS__, 'guard_blog_public_update' ), 10, 2 );
	}

	/**
	 * Whether authorized indexing mutation is executing.
	 *
	 * @return bool
	 */
	public static function is_authorized_mutation_in_progress() {
		return self::$authorized_mutation;
	}

	/**
	 * Whether WordPress currently allows search-engine indexing (blog_public only).
	 *
	 * @return bool
	 */
	public static function is_open() {
		return 1 === (int) get_option( 'blog_public', 1 );
	}

	/**
	 * Guard direct blog_public writes (WP-CLI, rogue update_option).
	 *
	 * @param mixed $value New value.
	 * @param mixed $old Old value.
	 * @return mixed
	 */
	public static function guard_blog_public_update( $value, $old ) {
		$closing = ( '0' === (string) $value || 0 === $value );
		if ( ! $closing ) {
			return $value;
		}
		if ( self::$authorized_mutation ) {
			return $value;
		}

		$source = self::detect_unauthorized_source();
		$qa_ctx = array(
			'source'  => $source,
			'qa_test' => true,
			'test_id' => 'blog_public_filter',
		);
		if ( class_exists( IndexingQaContext::class ) && IndexingQaContext::is_authorized( $qa_ctx ) ) {
			IndexingQaContext::record_guard_blocked_pass( $qa_ctx, array( 'blocked' => true ) );
		} elseif ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event(
				'indexing_close_blocked',
				'setting',
				'Заблокирована попытка blog_public=0 без явной human authorization',
				0,
				$source
			);
		}

		return $old;
	}

	/**
	 * Best-effort source for unauthorized close attempts.
	 *
	 * @return string
	 */
	private static function detect_unauthorized_source() {
		if ( defined( 'WP_CLI' ) && WP_CLI ) {
			return 'wp_cli';
		}
		if ( defined( 'DOING_CRON' ) && DOING_CRON ) {
			return 'cron';
		}
		if ( is_admin() && is_user_logged_in() ) {
			return 'admin_unauthorized';
		}
		return 'system';
	}

	/**
	 * Canonical mutation API with human-authorization guard.
	 *
	 * @param bool                 $open Target state.
	 * @param array<string, mixed> $context actor/source/explicit_human_authorization/reason/charter_id.
	 * @return array<string, mixed>
	 */
	public static function request_state( $open, array $context = array() ) {
		$open = (bool) $open;

		if ( ! $open && empty( $context['explicit_human_authorization'] ) ) {
			$allowed_technical = ! empty( $context['technical_close_authorized'] )
				|| ( defined( self::TECHNICAL_CLOSE_CONST ) && constant( self::TECHNICAL_CLOSE_CONST ) );

			if ( ! $allowed_technical ) {
				$source = isset( $context['source'] ) ? sanitize_key( (string) $context['source'] ) : 'unknown';
				$result = array(
					'ok'      => false,
					'blocked' => true,
					'open'    => self::is_open(),
					'error'   => 'close_requires_human_authorization',
				);
				self::log_blocked_close_attempt( $context, $source, $result );
				return $result;
			}

			if ( class_exists( ActivityLog::class ) ) {
				ActivityLog::log_system_event(
					'indexing_closed',
					'setting',
					'Техническое закрытие по явной charter authorization',
					0,
					isset( $context['source'] ) ? (string) $context['source'] : 'technical_charter'
				);
			}
			if ( class_exists( IndexingAlerts::class ) ) {
				if ( ! IndexingAlerts::should_suppress_for_qa_context( $context ) ) {
					IndexingAlerts::send_critical_blocked_alert(
						array(
							'previous_effective' => IndexingState::STATE_OPEN,
							'source'             => isset( $context['source'] ) ? (string) $context['source'] : 'technical_charter',
							'actor'              => isset( $context['actor'] ) ? (string) $context['actor'] : 'technical charter',
						)
					);
				}
			}
		}

		self::$authorized_mutation = true;
		try {
			return self::apply_state( $open, $context );
		} finally {
			self::$authorized_mutation = false;
		}
	}

	/**
	 * Log or record a blocked unauthorized close attempt.
	 *
	 * @param array<string, mixed> $context Context.
	 * @param string               $source Source key.
	 * @param array<string, mixed> $result Guard result.
	 */
	private static function log_blocked_close_attempt( array $context, $source, array $result ) {
		if ( class_exists( IndexingQaContext::class ) && IndexingQaContext::is_authorized( $context ) ) {
			IndexingQaContext::record_guard_blocked_pass( $context, $result );
			return;
		}

		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event(
				'indexing_close_blocked',
				'setting',
				'OPEN→CLOSED отклонено: нет explicit_human_authorization',
				0,
				$source
			);
		}
	}

	/**
	 * Back-compat wrapper — requires explicit_human_authorization for close.
	 *
	 * @param bool $open True = OPEN, false = CLOSED.
	 * @return array<string, mixed>
	 */
	public static function set_site_indexability( $open ) {
		return self::request_state(
			(bool) $open,
			array(
				'source'                        => 'legacy_set_site_indexability',
				'explicit_human_authorization'  => (bool) $open,
			)
		);
	}

	/**
	 * Apply state after authorization checks.
	 *
	 * @param bool                 $open Open indexing.
	 * @param array<string, mixed> $context Context.
	 * @return array<string, mixed>
	 */
	private static function apply_state( $open, array $context ) {
		$previous_snap = class_exists( IndexingState::class ) ? IndexingState::snapshot() : array();
		$prev_effective = isset( $previous_snap['effective'] ) ? (string) $previous_snap['effective'] : '';

		update_option( 'blog_public', $open ? '1' : '0' );

		$robots_ok = self::sync_robots_file( $open );
		$state     = self::read_state();

		$source = isset( $context['source'] ) ? sanitize_key( (string) $context['source'] ) : 'admin_ui';
		$user_id = isset( $context['user_id'] ) ? (int) $context['user_id'] : get_current_user_id();

		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event(
				$open ? 'indexing_opened' : 'indexing_closed',
				'setting',
				$open ? 'Индексация: открыта' : 'Индексация: закрыта',
				0,
				$source,
				$user_id
			);
		}

		if ( class_exists( IndexingState::class ) ) {
			IndexingState::record_human_decision(
				$open ? IndexingState::STATE_OPEN : IndexingState::STATE_CLOSED,
				array_merge(
					$context,
					array(
						'user_id' => $user_id,
						'source'  => $source,
					)
				)
			);
		}

		$meta = get_option( 'fp02_metacode_system_meta', array() );
		if ( ! is_array( $meta ) ) {
			$meta = array();
		}
		$meta['verified_at'] = gmdate( 'Y-m-d H:i:s' ) . ' UTC';
		$meta['indexing']    = $open ? 'OPEN — HUMAN-APPROVED' : 'CLOSED — HUMAN';
		update_option( 'fp02_metacode_system_meta', $meta, false );

		$new_snap = class_exists( IndexingState::class ) ? IndexingState::snapshot() : array();

		// Alert on OPEN→CLOSED or inconsistency after close.
		if ( class_exists( IndexingAlerts::class ) && ! $open ) {
			if ( IndexingState::STATE_OPEN === $prev_effective || IndexingState::STATE_INCONSISTENT === $new_snap['effective'] ) {
				if ( ! IndexingAlerts::should_suppress_for_qa_context( $context ) ) {
					IndexingAlerts::send_critical_blocked_alert(
						array(
							'previous_effective' => $prev_effective,
							'source'             => $source,
							'actor'              => self::actor_label_from_context( $context ),
							'fingerprint'        => $new_snap['fingerprint'] ?? '',
						)
					);
				}
			}
		}

		if ( class_exists( IndexingWatchdog::class ) && class_exists( IndexingState::class ) && IndexingState::STATE_OPEN === $new_snap['effective'] ) {
			update_option(
				IndexingWatchdog::BASELINE_OPT,
				array(
					'effective'   => $new_snap['effective'],
					'fingerprint' => $new_snap['fingerprint'],
					'set_at'      => current_time( 'mysql' ),
				),
				false
			);
		}

		$ok = ( (int) $state['blog_public'] === ( $open ? 1 : 0 ) ) && (bool) $robots_ok && ( (bool) $state['robots_disallow_all'] === ! $open );

		return array(
			'ok'                  => $ok,
			'open'                => $open,
			'blog_public'         => (int) $state['blog_public'],
			'robots_ok'           => (bool) $robots_ok,
			'robots_disallow_all' => (bool) $state['robots_disallow_all'],
			'robots_sitemap_host' => $state['robots_sitemap_host'],
			'effective'           => $new_snap['effective'] ?? '',
		);
	}

	/**
	 * @param array<string, mixed> $context Context.
	 * @return string
	 */
	private static function actor_label_from_context( array $context ) {
		if ( ! empty( $context['actor'] ) ) {
			return (string) $context['actor'];
		}
		$user_id = isset( $context['user_id'] ) ? (int) $context['user_id'] : get_current_user_id();
		if ( $user_id > 0 ) {
			return ActivityLog::user_label( $user_id );
		}
		return __( 'System', 'shpigovsky-core' );
	}

	/**
	 * Current semantic state.
	 *
	 * @return array<string, mixed>
	 */
	public static function read_state() {
		$blog_public = (int) get_option( 'blog_public', 1 );
		$robots_path = self::robots_path();
		$body        = '';
		$exists      = is_file( $robots_path );
		if ( $exists ) {
			$raw = file_get_contents( $robots_path );
			$body = is_string( $raw ) ? $raw : '';
		}
		$disallow_all = (bool) preg_match( '/^\s*Disallow:\s*\/\s*$/mi', $body );
		if ( ! $exists ) {
			$disallow_all = ( 0 === $blog_public );
		}
		$sitemap_host = '';
		if ( preg_match( '/Sitemap:\s*(\S+)/i', $body, $m ) ) {
			$sitemap_host = (string) wp_parse_url( $m[1], PHP_URL_HOST );
		}

		return array(
			'blog_public'         => $blog_public,
			'open'                => ( 1 === $blog_public ),
			'robots_file_exists'  => $exists,
			'robots_disallow_all' => $disallow_all,
			'robots_sitemap_host' => $sitemap_host,
		);
	}

	/**
	 * Canonical robots.txt body for the semantic state.
	 *
	 * OPEN → Olya/SEO policy (never a generic MARS open template).
	 * CLOSED → temporary global crawl closure.
	 *
	 * @param bool $open Open indexing.
	 * @return string
	 */
	public static function robots_body( $open ) {
		$sitemap = home_url( '/wp-sitemap.xml' );
		if ( $open ) {
			return self::seo_policy_body( $sitemap );
		}
		return "User-agent: *\nDisallow: /\n\nSitemap: {$sitemap}\n";
	}

	/**
	 * Absolute path to the canonical OPEN-state SEO robots policy (plugin-owned).
	 *
	 * @return string
	 */
	public static function seo_policy_path() {
		return trailingslashit( SHPIGOVSKY_CORE_DIR ) . self::SEO_POLICY_RELATIVE;
	}

	/**
	 * Absolute path for emergency SEO-policy backup beside docroot robots.txt.
	 *
	 * @return string
	 */
	public static function seo_backup_path() {
		return trailingslashit( ABSPATH ) . self::SEO_BACKUP_RELATIVE;
	}

	/**
	 * OPEN-state SEO robots policy body with current Sitemap host.
	 *
	 * @param string|null $sitemap Absolute sitemap URL.
	 * @return string
	 */
	public static function seo_policy_body( $sitemap = null ) {
		$sitemap = is_string( $sitemap ) && '' !== $sitemap ? $sitemap : home_url( '/wp-sitemap.xml' );
		$path    = self::seo_policy_path();
		$raw     = is_readable( $path ) ? file_get_contents( $path ) : false;

		if ( ! is_string( $raw ) || '' === trim( $raw ) ) {
			// Last-resort recoverable OPEN body — still not the historical generic MARS template.
			$raw = "User-agent: *\nAllow: /\n\nSitemap: {$sitemap}\n";
		}

		$raw = str_replace( "\r\n", "\n", $raw );
		$raw = preg_replace( "/^\xEF\xBB\xBF/", '', $raw );
		if ( preg_match( '/^Sitemap:\s*\S+/mi', $raw ) ) {
			$raw = preg_replace( '/^Sitemap:\s*\S+/mi', 'Sitemap: ' . $sitemap, $raw, 1 );
		} else {
			$raw = rtrim( $raw ) . "\n\nSitemap: {$sitemap}\n";
		}
		$raw = rtrim( $raw ) . "\n";

		return $raw;
	}

	/**
	 * Absolute robots.txt path.
	 *
	 * @return string
	 */
	public static function robots_path() {
		return trailingslashit( ABSPATH ) . self::ROBOTS_RELATIVE;
	}

	/**
	 * Whether robots body is the temporary global-close template.
	 *
	 * @param string $body Robots body.
	 * @return bool
	 */
	public static function is_global_close_body( $body ) {
		return (bool) preg_match( '/^\s*Disallow:\s*\/\s*$/mi', (string) $body );
	}

	/**
	 * Keep physical robots.txt aligned with indexability state.
	 *
	 * Always writes a physical file so WordPress virtual robots cannot shadow SEO policy.
	 *
	 * @param bool $open Open indexing.
	 * @return bool
	 */
	private static function sync_robots_file( $open ) {
		$path = self::robots_path();
		$bak  = self::seo_backup_path();

		if ( ! $open && is_file( $path ) ) {
			$current = file_get_contents( $path );
			if ( is_string( $current ) && '' !== trim( $current ) && ! self::is_global_close_body( $current ) ) {
				// Preserve live SEO policy before temporary close overwrite.
				file_put_contents( $bak, str_replace( "\r\n", "\n", $current ) );
			}
		}

		$body = self::robots_body( $open );
		if ( $open ) {
			// Prefer canonical plugin SEO policy; backup is emergency only if canonical unreadable.
			$canonical = self::seo_policy_body( home_url( '/wp-sitemap.xml' ) );
			if ( is_readable( self::seo_policy_path() ) ) {
				$body = $canonical;
			} elseif ( is_file( $bak ) ) {
				$backup = file_get_contents( $bak );
				if ( is_string( $backup ) && '' !== trim( $backup ) && ! self::is_global_close_body( $backup ) ) {
					$body = self::normalize_robots( $backup ) . "\n";
					if ( ! preg_match( '/^Sitemap:\s*\S+/mi', $body ) ) {
						$body = rtrim( $body ) . "\n\nSitemap: " . home_url( '/wp-sitemap.xml' ) . "\n";
					}
				}
			}
		}

		$written = file_put_contents( $path, $body );
		if ( false === $written ) {
			return false;
		}

		$read = file_get_contents( $path );
		return is_string( $read ) && ( self::normalize_robots( $read ) === self::normalize_robots( $body ) );
	}

	/**
	 * @param string $text Text.
	 * @return string
	 */
	private static function normalize_robots( $text ) {
		$text = str_replace( "\r\n", "\n", (string) $text );
		return trim( $text );
	}

	/**
	 * POST mutation: capability, nonce, confirm, then SET SITE INDEXABILITY.
	 */
	public static function handle_admin_post() {
		if ( ! is_user_logged_in() ) {
			wp_die( esc_html__( 'Требуется авторизация.', 'shpigovsky-core' ), 403 );
		}

		if ( ! current_user_can( self::CAPABILITY ) ) {
			wp_die( esc_html__( 'Недостаточно прав для изменения индексации.', 'shpigovsky-core' ), 403 );
		}

		if ( 'POST' !== strtoupper( (string) ( $_SERVER['REQUEST_METHOD'] ?? '' ) ) ) {
			wp_die( esc_html__( 'Изменение индексации допускается только методом POST.', 'shpigovsky-core' ), 405 );
		}

		check_admin_referer( self::NONCE );

		$confirm = isset( $_POST[ self::CONFIRM_FIELD ] ) ? sanitize_text_field( wp_unslash( $_POST[ self::CONFIRM_FIELD ] ) ) : '';
		if ( '1' !== $confirm ) {
			wp_safe_redirect( self::redirect_url( 'missing_confirm' ) );
			exit;
		}

		$wanted = isset( $_POST[ self::STATE_FIELD ] ) ? sanitize_key( wp_unslash( $_POST[ self::STATE_FIELD ] ) ) : '';
		if ( ! in_array( $wanted, array( 'open', 'closed' ), true ) ) {
			wp_safe_redirect( self::redirect_url( 'bad_state' ) );
			exit;
		}

		if ( 'closed' === $wanted ) {
			$close_ack = isset( $_POST[ self::CLOSE_ACK_FIELD ] ) ? sanitize_text_field( wp_unslash( $_POST[ self::CLOSE_ACK_FIELD ] ) ) : '';
			if ( '1' !== $close_ack ) {
				wp_safe_redirect( self::redirect_url( 'missing_close_ack' ) );
				exit;
			}
		}

		$user = wp_get_current_user();
		$result = self::request_state(
			'open' === $wanted,
			array(
				'source'                       => 'admin_ui',
				'explicit_human_authorization' => true,
				'user_id'                      => (int) $user->ID,
				'actor_login'                  => $user->user_login,
				'actor_display'                => $user->display_name ? $user->display_name : $user->user_login,
				'actor'                        => ActivityLog::user_label( (int) $user->ID ),
			)
		);

		if ( ! empty( $result['blocked'] ) ) {
			wp_safe_redirect( self::redirect_url( 'close_blocked' ) );
			exit;
		}

		$code = ! empty( $result['ok'] ) ? ( 'open' === $wanted ? 'opened' : 'closed' ) : 'failed';

		wp_safe_redirect( self::redirect_url( $code ) );
		exit;
	}

	/**
	 * @param string $code Notice code.
	 * @return string
	 */
	private static function redirect_url( $code ) {
		return add_query_arg(
			array(
				self::NOTICE_QUERY => sanitize_key( $code ),
			),
			admin_url( 'index.php' )
		);
	}

	/**
	 * Result notice after POST.
	 */
	public static function render_admin_notice() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			return;
		}
		if ( ! isset( $_GET[ self::NOTICE_QUERY ] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
			return;
		}

		$code = sanitize_key( wp_unslash( $_GET[ self::NOTICE_QUERY ] ) ); // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$map  = array(
			'opened'           => array( 'success', __( 'Индексация сайта разрешена. Поисковые системы могут начать обход. Отправка sitemap не выполнялась.', 'shpigovsky-core' ) ),
			'closed'           => array( 'warning', __( 'Индексация сайта закрыта. Поисковые системы снова получают запрет на обход.', 'shpigovsky-core' ) ),
			'failed'           => array( 'error', __( 'Не удалось полностью применить состояние индексации. Проверьте blog_public и robots.txt.', 'shpigovsky-core' ) ),
			'missing_confirm'  => array( 'error', __( 'Изменение индексации отменено: нет подтверждения.', 'shpigovsky-core' ) ),
			'missing_close_ack'=> array( 'error', __( 'Закрытие индексации отменено: не отмечено осознанное подтверждение.', 'shpigovsky-core' ) ),
			'close_blocked'    => array( 'error', __( 'Закрытие индексации заблокировано политикой безопасности.', 'shpigovsky-core' ) ),
			'bad_state'        => array( 'error', __( 'Некорректное значение индексации.', 'shpigovsky-core' ) ),
		);

		if ( ! isset( $map[ $code ] ) ) {
			return;
		}

		printf(
			'<div class="notice notice-%1$s is-dismissible"><p>%2$s</p></div>',
			esc_attr( $map[ $code ][0] ),
			esc_html( $map[ $code ][1] )
		);
	}

	/**
	 * Prominent Dashboard banner + confirmed POST control.
	 */
	public static function render_banner() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			return;
		}

		$snap     = class_exists( IndexingState::class ) ? IndexingState::snapshot() : array();
		$effective = isset( $snap['effective'] ) ? (string) $snap['effective'] : ( self::is_open() ? IndexingState::STATE_OPEN : IndexingState::STATE_CLOSED );
		$open     = ( IndexingState::STATE_OPEN === $effective );
		$inconsistent = ( IndexingState::STATE_INCONSISTENT === $effective );

		if ( $inconsistent || ( ! $open && IndexingState::STATE_CLOSED !== $effective ) ) {
			echo '<div class="fp02-indexing-banner is-inconsistent">';
			echo '<p class="fp02-indexing-banner__title is-warning">' . esc_html__( '⚠️ Индексация сайта: требует проверки', 'shpigovsky-core' ) . '</p>';
			echo '<p class="fp02-indexing-banner__meta">' . esc_html__( 'Сигналы индексации расходятся. Свяжитесь с техподдержкой MetaCODE.', 'shpigovsky-core' ) . '</p>';
			if ( ! empty( $snap ) ) {
				echo '<ul class="fp02-indexing-banner__debug">';
				printf( '<li>blog_public=%d</li>', (int) $snap['blog_public'] );
				printf(
					'<li>robots: %s (%s)</li>',
					esc_html( ! empty( $snap['robots']['global_disallow'] ) ? 'Disallow: /' : 'OK' ),
					esc_html( (string) ( $snap['robots']['owner'] ?? '' ) )
				);
				printf(
					'<li>meta: %s</li>',
					esc_html( ! empty( $snap['meta']['global_noindex'] ) ? 'global noindex' : 'OK' )
				);
				echo '</ul>';
			}
		} elseif ( $open ) {
			echo '<div class="fp02-indexing-banner is-open">';
			echo '<p class="fp02-indexing-banner__title">' . esc_html__( 'Индексация сайта: открыта', 'shpigovsky-core' ) . '</p>';
			if ( ! empty( $snap['human_actor'] ) ) {
				printf(
					'<p class="fp02-indexing-banner__meta">%s</p>',
					esc_html(
						sprintf(
							/* translators: 1: actor, 2: datetime */
							__( 'Последнее решение: %1$s · %2$s', 'shpigovsky-core' ),
							(string) $snap['human_actor'],
							(string) $snap['human_recorded_at']
						)
					)
				);
			}
		} else {
			echo '<div class="fp02-indexing-banner is-closed">';
			echo '<p class="fp02-indexing-banner__title">' . esc_html__( 'Индексация сайта: закрыта', 'shpigovsky-core' ) . '</p>';
			echo '<p class="fp02-indexing-banner__meta">' . esc_html__( 'Поисковые системы не должны обходить и индексировать сайт.', 'shpigovsky-core' ) . '</p>';
			if ( ! empty( $snap['human_actor'] ) ) {
				printf(
					'<p class="fp02-indexing-banner__meta">%s</p>',
					esc_html(
						sprintf(
							/* translators: 1: actor, 2: datetime */
							__( 'Последнее решение: %1$s · %2$s', 'shpigovsky-core' ),
							(string) $snap['human_actor'],
							(string) $snap['human_recorded_at']
						)
					)
				);
			}
		}

		$action  = $open ? 'closed' : 'open';
		$button  = $open
			? __( 'Закрыть индексацию', 'shpigovsky-core' )
			: __( 'Открыть индексацию', 'shpigovsky-core' );
		$btn_cls = $open ? 'button' : 'button button-primary';

		if ( $open ) {
			$confirm_msg = __( 'Вы уверены, что хотите закрыть сайт от индексации поисковыми системами?', 'shpigovsky-core' );
		} else {
			$confirm_msg = __( 'Вы уверены, что хотите разрешить поисковым системам индексировать сайт?', 'shpigovsky-core' );
		}

		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" data-fp02-confirm="' . esc_attr( $confirm_msg ) . '" onsubmit="return window.confirm(this.getAttribute(\'data-fp02-confirm\'));">';
		echo '<input type="hidden" name="action" value="' . esc_attr( self::ACTION ) . '" />';
		echo '<input type="hidden" name="' . esc_attr( self::STATE_FIELD ) . '" value="' . esc_attr( $action ) . '" />';
		echo '<input type="hidden" name="' . esc_attr( self::CONFIRM_FIELD ) . '" value="1" />';

		if ( $open ) {
			echo '<div class="fp02-indexing-banner__warn">';
			echo '<p class="fp02-indexing-banner__warn-title">' . esc_html__( 'Внимание', 'shpigovsky-core' ) . '</p>';
			echo '<p>' . esc_html__( 'Закрытие индексации может привести к исключению страниц сайта из поисковой выдачи. Используйте это действие только осознанно.', 'shpigovsky-core' ) . '</p>';
			echo '<label><input type="checkbox" name="' . esc_attr( self::CLOSE_ACK_FIELD ) . '" value="1" required /> ';
			echo esc_html__( 'Я понимаю последствия и хочу закрыть индексацию', 'shpigovsky-core' ) . '</label>';
			echo '</div>';
		}

		wp_nonce_field( self::NONCE );
		printf(
			'<button type="submit" class="%1$s">%2$s</button>',
			esc_attr( $btn_cls ),
			esc_html( $button )
		);
		echo '</form>';
		echo '</div>';
	}
}

<?php
/**
 * Canonical site indexability owner + Dashboard control — PROD-P18B.
 *
 * SET SITE INDEXABILITY = OPEN / CLOSED.
 * Never opened automatically. Mutation is POST + capability + nonce + confirm.
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
 */
final class IndexingControl implements ModuleInterface {

	const ACTION          = 'fp02_set_indexability';
	const NONCE           = 'fp02_set_indexability';
	const CAPABILITY      = 'manage_options';
	const CONFIRM_FIELD   = 'fp02_confirm';
	const STATE_FIELD     = 'fp02_indexability';
	const NOTICE_QUERY    = 'fp02_indexing';
	const ROBOTS_RELATIVE = 'robots.txt';

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
	}

	/**
	 * Whether WordPress currently allows search-engine indexing.
	 *
	 * @return bool
	 */
	public static function is_open() {
		return 1 === (int) get_option( 'blog_public', 1 );
	}

	/**
	 * SET SITE INDEXABILITY = OPEN / CLOSED.
	 *
	 * Owners kept consistent:
	 * - option blog_public (drives WP meta robots via core wp_robots_noindex)
	 * - physical ABSPATH/robots.txt when present (otherwise WP virtual robots_txt)
	 *
	 * Does not submit sitemaps. Does not change Search Console / Yandex.
	 * Search-result pages remain noindex via theme wp_robots (intentional).
	 *
	 * @param bool $open True = OPEN, false = CLOSED.
	 * @return array{ok:bool,open:bool,blog_public:int,robots_ok:bool,robots_disallow_all:bool,error?:string}
	 */
	public static function set_site_indexability( $open ) {
		$open = (bool) $open;
		update_option( 'blog_public', $open ? '1' : '0' );

		$robots_ok = self::sync_robots_file( $open );
		$state     = self::read_state();

		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event(
				$open ? 'indexing_opened' : 'indexing_closed',
				'setting',
				$open ? 'Индексация: открыта' : 'Индексация: закрыта',
				0
			);
		}

		$meta = get_option( 'fp02_metacode_system_meta', array() );
		if ( ! is_array( $meta ) ) {
			$meta = array();
		}
		$meta['verified_at'] = gmdate( 'Y-m-d H:i' ) . ' UTC';
		$meta['indexing']    = $open ? 'OPEN' : 'CLOSED — WAITING FOR OLYA APPROVAL';
		update_option( 'fp02_metacode_system_meta', $meta, false );

		$ok = ( (int) $state['blog_public'] === ( $open ? 1 : 0 ) ) && (bool) $robots_ok && ( (bool) $state['robots_disallow_all'] === ! $open );

		return array(
			'ok'                   => $ok,
			'open'                 => $open,
			'blog_public'          => (int) $state['blog_public'],
			'robots_ok'            => (bool) $robots_ok,
			'robots_disallow_all'  => (bool) $state['robots_disallow_all'],
			'robots_sitemap_host'  => $state['robots_sitemap_host'],
		);
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
	 * @param bool $open Open indexing.
	 * @return string
	 */
	public static function robots_body( $open ) {
		$sitemap = home_url( '/wp-sitemap.xml' );
		if ( $open ) {
			return "User-agent: *\nDisallow: /wp-admin/\nAllow: /wp-admin/admin-ajax.php\n\nSitemap: {$sitemap}\n";
		}
		return "User-agent: *\nDisallow: /\n\nSitemap: {$sitemap}\n";
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
	 * Keep physical robots.txt aligned when it exists. Do not create a new file
	 * if WordPress virtual robots.txt is already the owner.
	 *
	 * @param bool $open Open indexing.
	 * @return bool
	 */
	private static function sync_robots_file( $open ) {
		$path = self::robots_path();
		$body = self::robots_body( $open );

		if ( ! is_file( $path ) ) {
			return true;
		}

		$written = file_put_contents( $path, $body );
		if ( false === $written ) {
			return false;
		}

		$read = file_get_contents( $path );
		return is_string( $read ) && ( self::normalize_robots( $read ) === self::normalize_robots( $body ) );
	}

	/**
	 * Normalize robots comparison.
	 *
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

		$result = self::set_site_indexability( 'open' === $wanted );
		$code   = $result['ok'] ? ( 'open' === $wanted ? 'opened' : 'closed' ) : 'failed';

		wp_safe_redirect( self::redirect_url( $code ) );
		exit;
	}

	/**
	 * Dashboard redirect with notice.
	 *
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
			'opened'          => array( 'success', __( 'Индексация сайта разрешена. Поисковые системы могут начать обход. Отправка sitemap не выполнялась.', 'shpigovsky-core' ) ),
			'closed'          => array( 'warning', __( 'Индексация сайта закрыта. Поисковые системы снова получают запрет на обход.', 'shpigovsky-core' ) ),
			'failed'          => array( 'error', __( 'Не удалось полностью применить состояние индексации. Проверьте blog_public и robots.txt.', 'shpigovsky-core' ) ),
			'missing_confirm' => array( 'error', __( 'Изменение индексации отменено: нет подтверждения.', 'shpigovsky-core' ) ),
			'bad_state'       => array( 'error', __( 'Некорректное значение индексации.', 'shpigovsky-core' ) ),
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

		$open    = self::is_open();
		$action  = $open ? 'closed' : 'open';
		$confirm = $open
			? __( 'Вы уверены, что хотите закрыть сайт от индексации поисковыми системами?', 'shpigovsky-core' )
			: __( 'Вы уверены, что хотите разрешить поисковым системам индексировать сайт? После открытия поисковые системы смогут начать обход и добавление страниц в поиск.', 'shpigovsky-core' );
		$button  = $open
			? __( 'Закрыть индексацию', 'shpigovsky-core' )
			: __( 'Открыть индексацию', 'shpigovsky-core' );
		$btn_cls = $open ? 'button' : 'button button-primary';

		$border = $open ? '#00a32a' : '#dba617';
		$bg     = $open ? '#edfaef' : '#fff8e5';

		echo '<div class="fp02-indexing-banner" style="margin:0 0 14px;padding:12px 14px;border-left:4px solid ' . esc_attr( $border ) . ';background:' . esc_attr( $bg ) . ';">';

		if ( $open ) {
			echo '<p style="margin:0 0 8px;font-weight:600;">' . esc_html__( 'Индексация сайта разрешена.', 'shpigovsky-core' ) . '</p>';
		} else {
			echo '<p style="margin:0 0 6px;font-weight:600;">' . esc_html__( 'Сайт закрыт от индексации поисковыми системами.', 'shpigovsky-core' ) . '</p>';
			echo '<p style="margin:0 0 8px;">' . esc_html__( 'Сайт работает, но обход и добавление страниц в поиск намеренно запрещены. Открывать индексацию может Оля или оператор по явной команде.', 'shpigovsky-core' ) . '</p>';
		}

		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" data-fp02-confirm="' . esc_attr( $confirm ) . '" onsubmit="return window.confirm(this.getAttribute(\'data-fp02-confirm\'));">';
		echo '<input type="hidden" name="action" value="' . esc_attr( self::ACTION ) . '" />';
		echo '<input type="hidden" name="' . esc_attr( self::STATE_FIELD ) . '" value="' . esc_attr( $action ) . '" />';
		echo '<input type="hidden" name="' . esc_attr( self::CONFIRM_FIELD ) . '" value="1" />';
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

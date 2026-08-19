<?php
/**
 * Cookie consent / privacy controls owner — PROD-P18E-A through P18E-F.
 *
 * Implemented here:
 * - browser consent record contract
 * - public banner + settings UI
 * - consent-gated Yandex Metrika bootstrap
 * - canonical frontend API for consent-aware modules
 * - policy page selection / status surface
 *
 * Deferred:
 * - server-side visitor consent evidence storage
 * - legal approval of final policy wording
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Privacy;

use Shpigovsky\Core\Admin\ActivityLog;
use Shpigovsky\Core\Admin\OptionsPage;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Single owner of the cookie consent foundation.
 */
final class PrivacyConsent implements ModuleInterface {

	public const MENU_SLUG    = 'fp02-site-settings-cookie-privacy';
	public const CAPABILITY   = 'manage_options';
	public const SAVE_ACTION  = 'fp02_save_cookie_privacy';
	public const SAVE_NONCE   = 'fp02_save_cookie_privacy';
	public const NOTICE_QUERY = 'fp02_cookie_privacy';

	public const OPTION_SETTINGS = 'fp02_cookie_privacy_settings';
	public const COOKIE_NAME     = 'fp02_cookie_consent';

	public const CATEGORY_NECESSARY = 'necessary';
	public const CATEGORY_ANALYTICS = 'analytics';

	public const STATE_UNDECIDED         = 'UNDECIDED';
	public const STATE_NECESSARY_ONLY    = 'NECESSARY_ONLY';
	public const STATE_ANALYTICS_ALLOWED = 'ANALYTICS_ALLOWED';

	public const DEFAULT_CONSENT_VERSION = 1;
	public const DEFAULT_LIFETIME_DAYS   = 365; // Product default, not a legal rule.
	public const MIN_LIFETIME_DAYS       = 30;
	public const MAX_LIFETIME_DAYS       = 730;

	public const EVENT_COOKIE_SETTINGS_UPDATED = 'cookie_privacy_settings_updated';
	public const EVENT_CONSENT_VERSION_CHANGED = 'cookie_consent_version_changed';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'privacy.consent';
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
		add_action( 'admin_menu', array( __CLASS__, 'register_menu' ), 100 );
		add_action( 'admin_post_' . self::SAVE_ACTION, array( __CLASS__, 'handle_save' ) );
		add_action( 'admin_notices', array( __CLASS__, 'render_notice' ) );
		add_action( 'wp_enqueue_scripts', array( __CLASS__, 'enqueue_frontend_assets' ), 40 );
		add_action( 'wp_footer', array( __CLASS__, 'render_frontend_markup' ), 5 );
	}

	/**
	 * Register submenu under the visible Site Settings parent.
	 *
	 * @return void
	 */
	public static function register_menu() {
		add_submenu_page(
			OptionsPage::visible_menu_slug(),
			__( 'Cookie и конфиденциальность', 'shpigovsky-core' ),
			__( 'Cookie и конфиденциальность', 'shpigovsky-core' ),
			self::CAPABILITY,
			self::MENU_SLUG,
			array( __CLASS__, 'render_page' ),
			4
		);
	}

	/**
	 * Render the foundation settings page.
	 *
	 * @return void
	 */
	public static function render_page() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			wp_die( esc_html__( 'Недостаточно прав.', 'shpigovsky-core' ) );
		}

		$settings      = self::get_settings();
		$policy_page   = self::get_policy_page();
		$policy_status = self::policy_status_label( $policy_page );
		$counter       = self::metrika_counter_id();

		echo '<div class="wrap fp02-cookie-privacy">';
		echo '<h1>' . esc_html__( 'Cookie и конфиденциальность', 'shpigovsky-core' ) . '</h1>';
		echo '<p>' . esc_html__( 'Единый owner cookie-согласия: настройки, browser record, публичный notice и consent-gated аналитика.', 'shpigovsky-core' ) . '</p>';

		echo '<div class="notice notice-info" style="padding:12px;">';
		echo '<p><strong>' . esc_html__( 'Техническая основа:', 'shpigovsky-core' ) . '</strong> <code>ACTIVE</code></p>';
		echo '<p><strong>' . esc_html__( 'Публичное уведомление:', 'shpigovsky-core' ) . '</strong> <code>ACTIVE</code></p>';
		echo '<p><strong>' . esc_html__( 'Consent-gating Метрики:', 'shpigovsky-core' ) . '</strong> <code>CONSENT-GATED</code></p>';
		echo '<p><strong>' . esc_html__( 'Form goals:', 'shpigovsky-core' ) . '</strong> <code>CONSENT-GATED</code></p>';
		echo '<p><strong>' . esc_html__( 'Повторное открытие настроек:', 'shpigovsky-core' ) . '</strong> <code>ACTIVE</code></p>';
		echo '</div>';

		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" autocomplete="off">';
		echo '<input type="hidden" name="action" value="' . esc_attr( self::SAVE_ACTION ) . '" />';
		wp_nonce_field( self::SAVE_NONCE );

		echo '<h2>' . esc_html__( 'Баннер', 'shpigovsky-core' ) . '</h2>';
		echo '<table class="form-table" role="presentation">';
		self::row_checkbox(
			'system_enabled',
			__( 'Система cookie-согласия', 'shpigovsky-core' ),
			(bool) $settings['system_enabled'],
			__( 'Если отключить эту UI-систему, публичный banner/settings не рендерятся, но аналитика всё равно не должна включаться автоматически.', 'shpigovsky-core' )
		);
		self::row_text(
			'banner_title',
			__( 'Заголовок', 'shpigovsky-core' ),
			(string) $settings['banner_title'],
			__( 'Мы используем файлы cookie', 'shpigovsky-core' ),
			120
		);
		self::row_textarea(
			'banner_description',
			__( 'Короткий текст', 'shpigovsky-core' ),
			(string) $settings['banner_description'],
			4,
			600
		);
		self::row_page_select(
			'policy_page_id',
			__( 'Страница политики cookie', 'shpigovsky-core' ),
			(int) $settings['policy_page_id'],
			__( 'Выберите текущую страницу политики cookie. Содержимое страницы этой волной не переписывается.', 'shpigovsky-core' )
		);
		self::row_number(
			'consent_version',
			__( 'Версия согласия', 'shpigovsky-core' ),
			(int) $settings['consent_version'],
			1,
			50,
			__( 'Только целое число. Рост версии нужен для будущего повторного запроса после материальных изменений privacy-модели.', 'shpigovsky-core' )
		);
		self::row_number(
			'consent_lifetime_days',
			__( 'Срок хранения выбора', 'shpigovsky-core' ),
			(int) $settings['consent_lifetime_days'],
			self::MIN_LIFETIME_DAYS,
			self::MAX_LIFETIME_DAYS,
			__( 'Технический product default, не юридическое требование. Значение можно изменить позже после решения legal/operator.', 'shpigovsky-core' )
		);
		self::row_text( 'label_accept', __( 'Кнопка «Принять»', 'shpigovsky-core' ), (string) $settings['label_accept'], __( 'Принять', 'shpigovsky-core' ), 60 );
		self::row_text( 'label_necessary_only', __( 'Кнопка «Только необходимые»', 'shpigovsky-core' ), (string) $settings['label_necessary_only'], __( 'Только необходимые', 'shpigovsky-core' ), 80 );
		self::row_text( 'label_customize', __( 'Кнопка «Настроить»', 'shpigovsky-core' ), (string) $settings['label_customize'], __( 'Настроить', 'shpigovsky-core' ), 60 );
		self::row_text( 'label_save', __( 'Кнопка «Сохранить выбор»', 'shpigovsky-core' ), (string) $settings['label_save'], __( 'Сохранить выбор', 'shpigovsky-core' ), 80 );
		echo '</table>';

		echo '<h2>' . esc_html__( 'Категории', 'shpigovsky-core' ) . '</h2>';
		echo '<table class="form-table" role="presentation">';
		self::row_html(
			__( 'Необходимые', 'shpigovsky-core' ),
			'<strong>' . esc_html__( 'Всегда включены', 'shpigovsky-core' ) . '</strong><p class="description">' . esc_html__( 'Не редактируется и не может быть выключено. Necessary всегда остаётся true.', 'shpigovsky-core' ) . '</p>'
		);
		self::row_checkbox(
			'analytics_category_enabled',
			__( 'Аналитика доступна для выбора', 'shpigovsky-core' ),
			(bool) $settings['analytics_category_enabled'],
			__( 'Категория остаётся отдельной от Necessary. Фактическая загрузка Метрики происходит только после разрешения аналитики.', 'shpigovsky-core' )
		);
		self::row_textarea(
			'analytics_description',
			__( 'Описание категории «Аналитика»', 'shpigovsky-core' ),
			(string) $settings['analytics_description'],
			4,
			600
		);
		echo '</table>';

		echo '<h2>' . esc_html__( 'Интеграции', 'shpigovsky-core' ) . '</h2>';
		echo '<table class="form-table" role="presentation">';
		self::row_html(
			__( 'Яндекс Метрика', 'shpigovsky-core' ),
			'<code>analytics</code><p class="description">'
			. esc_html__( 'Классификация техническая и не редактируется обычным редактором.', 'shpigovsky-core' )
			. '</p>'
		);
		self::row_html(
			__( 'Счётчик Метрики', 'shpigovsky-core' ),
			'' !== $counter
				? '<code>' . esc_html( $counter ) . '</code> — ' . esc_html__( 'источник истины: Настройки сайта → SEO и интеграции', 'shpigovsky-core' )
				: esc_html__( 'Не задан. Источник истины остаётся в SEO и интеграциях, дублировать ID здесь нельзя.', 'shpigovsky-core' )
		);
		echo '</table>';

		echo '<h2>' . esc_html__( 'Состояние', 'shpigovsky-core' ) . '</h2>';
		echo '<table class="form-table" role="presentation">';
		self::row_html( __( 'Техническая основа', 'shpigovsky-core' ), '<code>ACTIVE</code>' );
		self::row_html( __( 'Публичное уведомление', 'shpigovsky-core' ), '<code>ACTIVE</code>' );
		self::row_html( __( 'Consent-gating Метрики', 'shpigovsky-core' ), '<code>CONSENT-GATED</code>' );
		self::row_html( __( 'Form goals', 'shpigovsky-core' ), '<code>CONSENT-GATED</code>' );
		self::row_html( __( 'Повторное открытие настроек', 'shpigovsky-core' ), '<code>ACTIVE</code>' );
		self::row_html( __( 'Политика Cookie', 'shpigovsky-core' ), '<code>' . esc_html( $policy_status ) . '</code>' );
		self::row_html( __( 'Legal review', 'shpigovsky-core' ), 'CURRENT' === $policy_status ? '<code>PENDING FINAL LEGAL REVIEW</code>' : '<code>REQUIRED BEFORE LEGAL COMPLETE</code>' );
		self::row_html( __( 'Хранилище доказательств согласия', 'shpigovsky-core' ), '<code>' . esc_html__( 'BROWSER STATE FOUNDATION ONLY / SERVER EVIDENCE DEFERRED', 'shpigovsky-core' ) . '</code>' );
		self::row_html( __( 'Ключ browser record', 'shpigovsky-core' ), '<code>' . esc_html( self::COOKIE_NAME ) . '</code>' );
		self::row_html( __( 'Категории v1', 'shpigovsky-core' ), '<code>necessary</code> + <code>analytics</code>' );
		echo '</table>';

		submit_button( __( 'Сохранить настройки', 'shpigovsky-core' ) );
		echo '</form>';
		echo '</div>';
	}

	/**
	 * Save settings from POST.
	 *
	 * @return void
	 */
	public static function handle_save() {
		self::require_post_cap();
		check_admin_referer( self::SAVE_NONCE );

		$old      = self::get_settings();
		$new      = self::sanitize_settings( wp_unslash( $_POST ) );
		$changed  = self::diff_settings( $old, $new );
		$changed_summary = self::format_changed_summary( $changed );

		update_option( self::OPTION_SETTINGS, $new, false );

		if ( ! empty( $changed ) && class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event(
				self::EVENT_COOKIE_SETTINGS_UPDATED,
				'setting',
				sprintf(
					/* translators: %s: changed fields summary */
					__( 'Cookie / privacy settings updated: %s', 'shpigovsky-core' ),
					$changed_summary
				),
				0
			);

			if ( isset( $changed['consent_version'] ) ) {
				ActivityLog::log_system_event(
					self::EVENT_CONSENT_VERSION_CHANGED,
					'setting',
					sprintf(
						/* translators: %s: new version */
						__( 'Cookie consent version changed to %s', 'shpigovsky-core' ),
						(string) $new['consent_version']
					),
					0
				);
			}
		}

		wp_safe_redirect(
			add_query_arg(
				self::NOTICE_QUERY,
				'saved',
				admin_url( 'admin.php?page=' . self::MENU_SLUG )
			)
		);
		exit;
	}

	/**
	 * Render admin notice on the settings page.
	 *
	 * @return void
	 */
	public static function render_notice() {
		if ( ! current_user_can( self::CAPABILITY ) ) {
			return;
		}

		$page = isset( $_GET['page'] ) ? sanitize_key( wp_unslash( $_GET['page'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$code = isset( $_GET[ self::NOTICE_QUERY ] ) ? sanitize_key( wp_unslash( $_GET[ self::NOTICE_QUERY ] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended

		if ( self::MENU_SLUG !== $page || 'saved' !== $code ) {
			return;
		}

		echo '<div class="notice notice-success is-dismissible"><p>'
			. esc_html__( 'Настройки Cookie и конфиденциальности сохранены. Публичный banner/settings, consent-gated Метрика и reopen path активны; финальная legal формулировка policy остаётся отдельным review-этапом.', 'shpigovsky-core' )
			. '</p></div>';
	}

	/**
	 * Current settings merged with defaults.
	 *
	 * @return array<string, mixed>
	 */
	public static function get_settings() {
		$stored = get_option( self::OPTION_SETTINGS, array() );
		if ( ! is_array( $stored ) ) {
			$stored = array();
		}

		return wp_parse_args( $stored, self::default_settings() );
	}

	/**
	 * Default settings.
	 *
	 * @return array<string, mixed>
	 */
	public static function default_settings() {
		return array(
			'system_enabled'             => true,
			'banner_title'               => __( 'Мы используем файлы cookie', 'shpigovsky-core' ),
			'banner_description'         => __( 'Мы используем необходимые cookie для работы сайта и, с вашего разрешения, аналитические технологии для понимания того, как используется сайт.', 'shpigovsky-core' ),
			'policy_page_id'             => self::default_policy_page_id(),
			'consent_version'            => self::DEFAULT_CONSENT_VERSION,
			'consent_lifetime_days'      => self::DEFAULT_LIFETIME_DAYS,
			'analytics_category_enabled' => true,
			'analytics_description'      => __( 'Аналитические технологии помогают понять, как используется сайт. Сейчас эта категория относится к Яндекс Метрике.', 'shpigovsky-core' ),
			'label_accept'               => __( 'Принять', 'shpigovsky-core' ),
			'label_necessary_only'       => __( 'Только необходимые', 'shpigovsky-core' ),
			'label_customize'            => __( 'Настроить', 'shpigovsky-core' ),
			'label_save'                 => __( 'Сохранить выбор', 'shpigovsky-core' ),
		);
	}

	/**
	 * Category registry.
	 *
	 * @return array<string, array<string, mixed>>
	 */
	public static function categories() {
		return array(
			self::CATEGORY_NECESSARY => array(
				'label'       => __( 'Необходимые', 'shpigovsky-core' ),
				'always_true' => true,
			),
			self::CATEGORY_ANALYTICS => array(
				'label'       => __( 'Аналитика', 'shpigovsky-core' ),
				'always_true' => false,
			),
		);
	}

	/**
	 * Technical integration registry.
	 *
	 * @return array<string, string>
	 */
	public static function integration_registry() {
		return array(
			'yandex_metrika' => self::CATEGORY_ANALYTICS,
		);
	}

	/**
	 * Current consent version.
	 *
	 * @return int
	 */
	public static function current_version() {
		$settings = self::get_settings();
		return max( 1, (int) $settings['consent_version'] );
	}

	/**
	 * Product-configured browser lifetime in days.
	 *
	 * @return int
	 */
	public static function lifetime_days() {
		$settings = self::get_settings();
		$days     = (int) $settings['consent_lifetime_days'];
		return max( self::MIN_LIFETIME_DAYS, min( self::MAX_LIFETIME_DAYS, $days ) );
	}

	/**
	 * Cookie write attributes for the future frontend owner.
	 *
	 * HttpOnly stays false because the future JS UI must read and update consent.
	 *
	 * @return array<string, mixed>
	 */
	public static function cookie_attributes() {
		return array(
			'path'     => '/',
			'secure'   => function_exists( 'is_ssl' ) ? is_ssl() : true,
			'httponly' => false,
			'samesite' => 'Lax',
			'max_age'  => DAY_IN_SECONDS * self::lifetime_days(),
		);
	}

	/**
	 * Build a canonical browser record from a machine state.
	 *
	 * @param string      $state      Machine state.
	 * @param string|null $decided_at ISO-8601 UTC timestamp.
	 * @param int|null    $version    Consent version.
	 * @return array<string, mixed>|null
	 */
	public static function build_record_for_state( $state, $decided_at = null, $version = null ) {
		$state = is_string( $state ) ? strtoupper( trim( $state ) ) : '';

		if ( null === $version ) {
			$version = self::current_version();
		}

		if ( null === $decided_at ) {
			$decided_at = gmdate( 'c' );
		}

		if ( self::STATE_NECESSARY_ONLY === $state ) {
			return array(
				'version'    => (int) $version,
				'necessary'  => true,
				'analytics'  => false,
				'decided_at' => (string) $decided_at,
			);
		}

		if ( self::STATE_ANALYTICS_ALLOWED === $state ) {
			return array(
				'version'    => (int) $version,
				'necessary'  => true,
				'analytics'  => true,
				'decided_at' => (string) $decided_at,
			);
		}

		return null;
	}

	/**
	 * Encode a record for the future browser cookie.
	 *
	 * @param array<string, mixed> $record Consent record.
	 * @return string
	 */
	public static function encode_record( array $record ) {
		$json = function_exists( 'wp_json_encode' )
			? wp_json_encode( $record, JSON_UNESCAPED_SLASHES )
			: json_encode( $record, JSON_UNESCAPED_SLASHES );

		return is_string( $json ) ? $json : '';
	}

	/**
	 * Parse a raw browser record. Unknown or tampered data becomes undecided.
	 *
	 * @param string $raw Raw browser value.
	 * @return array{state:string,record:array<string,mixed>|null,is_valid:bool,requires_redecision:bool}
	 */
	public static function parse_browser_record( $raw ) {
		$fallback = array(
			'state'              => self::STATE_UNDECIDED,
			'record'             => null,
			'is_valid'           => false,
			'requires_redecision' => false,
		);

		if ( ! is_string( $raw ) || '' === trim( $raw ) ) {
			return $fallback;
		}

		$decoded = json_decode( $raw, true );
		if ( ! is_array( $decoded ) ) {
			return $fallback;
		}

		$allowed_keys = array( 'version', 'necessary', 'analytics', 'decided_at' );
		$keys         = array_keys( $decoded );
		sort( $allowed_keys );
		sort( $keys );

		if ( $keys !== $allowed_keys ) {
			return $fallback;
		}

		$version = isset( $decoded['version'] ) ? (int) $decoded['version'] : 0;
		if ( $version < 1 || $version > 50 ) {
			return $fallback;
		}

		if ( ! array_key_exists( 'necessary', $decoded ) || true !== $decoded['necessary'] ) {
			return $fallback;
		}

		if ( ! array_key_exists( 'analytics', $decoded ) || ! is_bool( $decoded['analytics'] ) ) {
			return $fallback;
		}

		$decided_at = isset( $decoded['decided_at'] ) ? (string) $decoded['decided_at'] : '';
		$timestamp  = strtotime( $decided_at );
		$min_ts     = strtotime( '2020-01-01T00:00:00+00:00' );
		$max_ts     = time() + DAY_IN_SECONDS;
		if ( false === $timestamp || $timestamp < $min_ts || $timestamp > $max_ts ) {
			return $fallback;
		}

		$state = ( true === $decoded['analytics'] ) ? self::STATE_ANALYTICS_ALLOWED : self::STATE_NECESSARY_ONLY;

		return array(
			'state'              => $state,
			'record'             => array(
				'version'    => $version,
				'necessary'  => true,
				'analytics'  => (bool) $decoded['analytics'],
				'decided_at' => gmdate( 'c', $timestamp ),
			),
			'is_valid'           => true,
			'requires_redecision' => ( $version !== self::current_version() ),
		);
	}

	/**
	 * Whether the current/future consent state allows a category.
	 *
	 * @param string                               $category Category name.
	 * @param string|array<string, mixed>|null     $record   Optional raw or parsed record.
	 * @return bool
	 */
	public static function is_allowed( $category, $record = null ) {
		$category = sanitize_key( (string) $category );

		if ( self::CATEGORY_NECESSARY === $category ) {
			return true;
		}

		if ( self::CATEGORY_ANALYTICS !== $category ) {
			return false;
		}

		if ( is_string( $record ) ) {
			$parsed = self::parse_browser_record( $record );
		} elseif ( is_array( $record ) && isset( $record['state'] ) ) {
			$parsed = $record;
		} else {
			return false;
		}

		if ( ! empty( $parsed['requires_redecision'] ) ) {
			return false;
		}

		return isset( $parsed['state'] ) && self::STATE_ANALYTICS_ALLOWED === $parsed['state'];
	}

	/**
	 * Save settings sanitization.
	 *
	 * @param array<string, mixed> $input Raw POST.
	 * @return array<string, mixed>
	 */
	private static function sanitize_settings( array $input ) {
		$out = self::default_settings();

		$out['system_enabled']             = ! empty( $input['system_enabled'] );
		$out['banner_title']               = self::sanitize_text( $input['banner_title'] ?? '', 120, $out['banner_title'] );
		$out['banner_description']         = self::sanitize_textarea( $input['banner_description'] ?? '', 600, $out['banner_description'] );
		$out['policy_page_id']             = self::sanitize_page_id( $input['policy_page_id'] ?? 0 );
		$out['consent_version']            = self::sanitize_int( $input['consent_version'] ?? self::DEFAULT_CONSENT_VERSION, 1, 50, self::DEFAULT_CONSENT_VERSION );
		$out['consent_lifetime_days']      = self::sanitize_int( $input['consent_lifetime_days'] ?? self::DEFAULT_LIFETIME_DAYS, self::MIN_LIFETIME_DAYS, self::MAX_LIFETIME_DAYS, self::DEFAULT_LIFETIME_DAYS );
		$out['analytics_category_enabled'] = ! empty( $input['analytics_category_enabled'] );
		$out['analytics_description']      = self::sanitize_textarea( $input['analytics_description'] ?? '', 600, $out['analytics_description'] );
		$out['label_accept']               = self::sanitize_text( $input['label_accept'] ?? '', 60, $out['label_accept'] );
		$out['label_necessary_only']       = self::sanitize_text( $input['label_necessary_only'] ?? '', 80, $out['label_necessary_only'] );
		$out['label_customize']            = self::sanitize_text( $input['label_customize'] ?? '', 60, $out['label_customize'] );
		$out['label_save']                 = self::sanitize_text( $input['label_save'] ?? '', 80, $out['label_save'] );

		return $out;
	}

	/**
	 * Diff old and new settings.
	 *
	 * @param array<string, mixed> $old Old.
	 * @param array<string, mixed> $new New.
	 * @return array<string, array{old:mixed,new:mixed}>
	 */
	private static function diff_settings( array $old, array $new ) {
		$changed = array();
		foreach ( $new as $key => $value ) {
			$old_value = $old[ $key ] ?? null;
			if ( $old_value !== $value ) {
				$changed[ $key ] = array(
					'old' => $old_value,
					'new' => $value,
				);
			}
		}
		return $changed;
	}

	/**
	 * Human-safe change summary for Activity Log.
	 *
	 * @param array<string, array{old:mixed,new:mixed}> $changed Changed.
	 * @return string
	 */
	private static function format_changed_summary( array $changed ) {
		if ( empty( $changed ) ) {
			return 'no effective changes';
		}

		$labels = array(
			'system_enabled'             => 'enabled',
			'banner_title'               => 'title',
			'banner_description'         => 'description',
			'policy_page_id'             => 'policy_page',
			'consent_version'            => 'version',
			'consent_lifetime_days'      => 'lifetime_days',
			'analytics_category_enabled' => 'analytics_enabled',
			'analytics_description'      => 'analytics_description',
			'label_accept'               => 'label_accept',
			'label_necessary_only'       => 'label_necessary_only',
			'label_customize'            => 'label_customize',
			'label_save'                 => 'label_save',
		);

		$out = array();
		foreach ( array_keys( $changed ) as $key ) {
			$out[] = $labels[ $key ] ?? $key;
		}

		return implode( ', ', $out );
	}

	/**
	 * Selected policy page or current fallback page.
	 *
	 * @return \WP_Post|null
	 */
	public static function get_policy_page() {
		$settings = self::get_settings();
		$page_id  = (int) $settings['policy_page_id'];
		if ( $page_id > 0 ) {
			$page = get_post( $page_id );
			if ( $page instanceof \WP_Post && 'page' === $page->post_type ) {
				return $page;
			}
		}

		$fallback = get_page_by_path( 'cookie-files-policy', OBJECT, 'page' );
		return ( $fallback instanceof \WP_Post ) ? $fallback : null;
	}

	/**
	 * Human-readable policy status.
	 *
	 * @param \WP_Post|null $page Policy page.
	 * @return string
	 */
	public static function policy_status_label( $page ) {
		if ( ! $page instanceof \WP_Post ) {
			return 'NOT CONFIGURED';
		}

		$content = (string) $page->post_content;
		$lower   = function_exists( 'mb_strtolower' ) ? mb_strtolower( $content, 'UTF-8' ) : strtolower( $content );

		$needs_review = false !== strpos( $lower, 'демо' )
			|| false !== strpos( $lower, 'placeholder' )
			|| false !== strpos( $lower, 'баннер' )
			|| false !== strpos( $lower, 'панел');

		return $needs_review ? 'CURRENT / NEEDS LEGAL REVIEW' : 'CURRENT';
	}

	/**
	 * Current Metrika counter id from the existing SEO owner.
	 *
	 * @return string
	 */
	public static function metrika_counter_id() {
		if ( function_exists( 'shpigovsky_seo_get_option' ) ) {
			$value = (string) shpigovsky_seo_get_option( 'yandex_metrica_counter_id', '' );
			return preg_replace( '/\D+/', '', $value );
		}

		return preg_replace( '/\D+/', '', (string) get_option( 'options_yandex_metrica_counter_id', '' ) );
	}

	/**
	 * Whether the public runtime is enabled.
	 *
	 * @return bool
	 */
	public static function frontend_runtime_enabled() {
		$settings = self::get_settings();
		return ! is_admin() && ! wp_doing_ajax() && ! empty( $settings['system_enabled'] );
	}

	/**
	 * Register and localize public assets.
	 *
	 * @return void
	 */
	public static function enqueue_frontend_assets() {
		if ( ! self::frontend_runtime_enabled() ) {
			return;
		}

		$style_deps = array();
		if ( wp_style_is( 'shpigovsky-v9', 'registered' ) || wp_style_is( 'shpigovsky-v9', 'enqueued' ) ) {
			$style_deps[] = 'shpigovsky-v9';
		}

		$script_deps = array();
		if ( wp_script_is( 'shpigovsky-v9-shell', 'registered' ) || wp_script_is( 'shpigovsky-v9-shell', 'enqueued' ) ) {
			$script_deps[] = 'shpigovsky-v9-shell';
		}

		wp_enqueue_style(
			'fp02-privacy-consent',
			SHPIGOVSKY_CORE_URI . 'assets/css/privacy-consent.css',
			$style_deps,
			self::asset_version( 'assets/css/privacy-consent.css' )
		);

		wp_enqueue_script(
			'fp02-privacy-consent',
			SHPIGOVSKY_CORE_URI . 'assets/js/privacy-consent.js',
			$script_deps,
			self::asset_version( 'assets/js/privacy-consent.js' ),
			true
		);

		wp_localize_script(
			'fp02-privacy-consent',
			'fp02PrivacyConsent',
			self::public_runtime_config()
		);
	}

	/**
	 * Render the shared banner/settings markup.
	 *
	 * Same HTML can be cached for all visitors; browser state is resolved client-side.
	 *
	 * @return void
	 */
	public static function render_frontend_markup() {
		if ( ! self::frontend_runtime_enabled() ) {
			return;
		}

		$settings   = self::get_settings();
		$policy     = self::get_policy_page();
		$policy_url = $policy instanceof \WP_Post ? get_permalink( $policy ) : '';
		?>
		<div
			class="fp02-cookie-consent"
			data-fp02-cookie-consent
			hidden
			aria-hidden="true"
		>
			<div class="fp02-cookie-consent__card" role="region" aria-labelledby="fp02-cookie-consent-title">
				<div class="fp02-cookie-consent__notice" data-fp02-consent-notice>
					<h2 class="fp02-cookie-consent__title" id="fp02-cookie-consent-title"><?php echo esc_html( (string) $settings['banner_title'] ); ?></h2>
					<p class="fp02-cookie-consent__text"><?php echo esc_html( (string) $settings['banner_description'] ); ?></p>
					<?php if ( is_string( $policy_url ) && '' !== $policy_url ) : ?>
						<p class="fp02-cookie-consent__policy">
							<a href="<?php echo esc_url( $policy_url ); ?>"><?php esc_html_e( 'Подробнее в политике cookie', 'shpigovsky-core' ); ?></a>
						</p>
					<?php endif; ?>
					<div class="fp02-cookie-consent__actions">
						<button type="button" class="btn btn_dark btn--primary fp02-cookie-consent__action" data-fp02-consent-accept><?php echo esc_html( (string) $settings['label_accept'] ); ?></button>
						<button type="button" class="btn fp02-cookie-consent__action fp02-cookie-consent__action--secondary" data-fp02-consent-necessary><?php echo esc_html( (string) $settings['label_necessary_only'] ); ?></button>
						<button type="button" class="fp02-cookie-consent__link-button" data-fp02-consent-customize aria-expanded="false" aria-controls="fp02-cookie-consent-settings"><?php echo esc_html( (string) $settings['label_customize'] ); ?></button>
					</div>
				</div>

				<section
					class="fp02-cookie-consent__settings"
					id="fp02-cookie-consent-settings"
					data-fp02-consent-settings
					hidden
					aria-labelledby="fp02-cookie-consent-settings-title"
				>
					<div class="fp02-cookie-consent__settings-head">
						<h3 class="fp02-cookie-consent__settings-title" id="fp02-cookie-consent-settings-title"><?php esc_html_e( 'Настройки cookie', 'shpigovsky-core' ); ?></h3>
						<button type="button" class="fp02-cookie-consent__close" data-fp02-consent-close-settings aria-label="<?php esc_attr_e( 'Закрыть настройки cookie', 'shpigovsky-core' ); ?>">
							<span aria-hidden="true">×</span>
						</button>
					</div>

					<div class="fp02-cookie-consent__group">
						<div class="fp02-cookie-consent__group-copy">
							<h4 class="fp02-cookie-consent__group-title"><?php esc_html_e( 'Необходимые', 'shpigovsky-core' ); ?></h4>
							<p class="fp02-cookie-consent__group-text"><?php esc_html_e( 'Всегда включены', 'shpigovsky-core' ); ?></p>
						</div>
						<span class="fp02-cookie-consent__badge"><?php esc_html_e( 'Всегда включены', 'shpigovsky-core' ); ?></span>
					</div>

					<div class="fp02-cookie-consent__group">
						<div class="fp02-cookie-consent__group-copy">
							<h4 class="fp02-cookie-consent__group-title"><?php esc_html_e( 'Аналитика', 'shpigovsky-core' ); ?></h4>
							<p class="fp02-cookie-consent__group-text"><?php echo esc_html( (string) $settings['analytics_description'] ); ?></p>
							<p class="fp02-cookie-consent__provider"><?php esc_html_e( 'Провайдер: Яндекс Метрика', 'shpigovsky-core' ); ?></p>
						</div>
						<label class="fp02-cookie-consent__toggle">
							<input type="checkbox" class="fp02-cookie-consent__toggle-input" data-fp02-consent-analytics />
							<span class="fp02-cookie-consent__toggle-ui" aria-hidden="true"></span>
							<span class="screen-reader-text"><?php esc_html_e( 'Разрешить аналитические cookie', 'shpigovsky-core' ); ?></span>
						</label>
					</div>

					<div class="fp02-cookie-consent__actions fp02-cookie-consent__actions--settings">
						<button type="button" class="btn btn_dark btn--primary fp02-cookie-consent__action" data-fp02-consent-save><?php echo esc_html( (string) $settings['label_save'] ); ?></button>
					</div>
				</section>
			</div>
		</div>
		<?php
	}

	/**
	 * Public-safe runtime config for the browser owner.
	 *
	 * @return array<string, mixed>
	 */
	public static function public_runtime_config() {
		$settings   = self::get_settings();
		$policy     = self::get_policy_page();
		$policy_url = $policy instanceof \WP_Post ? get_permalink( $policy ) : '';
		$attrs      = self::cookie_attributes();

		return array(
			'cookieName'                => self::COOKIE_NAME,
			'currentVersion'            => self::current_version(),
			'systemEnabled'             => ! empty( $settings['system_enabled'] ),
			'analyticsCategoryEnabled'  => ! empty( $settings['analytics_category_enabled'] ),
			'metrikaCounterId'          => self::metrika_counter_id(),
			'policyUrl'                 => is_string( $policy_url ) ? $policy_url : '',
			'cookie'                    => array(
				'path'    => (string) ( $attrs['path'] ?? '/' ),
				'maxAge'  => (int) ( $attrs['max_age'] ?? DAY_IN_SECONDS * self::lifetime_days() ),
				'secure'  => ! empty( $attrs['secure'] ),
				'sameSite'=> (string) ( $attrs['samesite'] ?? 'Lax' ),
			),
			'states'                    => array(
				'undecided'        => self::STATE_UNDECIDED,
				'necessaryOnly'    => self::STATE_NECESSARY_ONLY,
				'analyticsAllowed' => self::STATE_ANALYTICS_ALLOWED,
			),
			'events'                    => array(
				'updated'          => 'fp02:privacy-consent-updated',
				'openSettings'     => 'fp02:privacy-consent-open',
				'analyticsGranted' => 'analytics_granted',
				'analyticsRevoked' => 'analytics_revoked',
			),
		);
	}

	/**
	 * Default policy page if present.
	 *
	 * @return int
	 */
	private static function default_policy_page_id() {
		$page = get_page_by_path( 'cookie-files-policy', OBJECT, 'page' );
		return ( $page instanceof \WP_Post ) ? (int) $page->ID : 0;
	}

	/**
	 * Version string for plugin assets.
	 *
	 * @param string $relative_path Relative path from plugin root.
	 * @return string
	 */
	private static function asset_version( $relative_path ) {
		$path = SHPIGOVSKY_CORE_DIR . ltrim( $relative_path, '/\\' );
		if ( is_readable( $path ) ) {
			return (string) filemtime( $path );
		}

		return defined( 'SHPIGOVSKY_CORE_VERSION' ) ? SHPIGOVSKY_CORE_VERSION : '1';
	}

	/**
	 * Safe page selector.
	 *
	 * @param mixed $value Raw value.
	 * @return int
	 */
	private static function sanitize_page_id( $value ) {
		$page_id = absint( $value );
		if ( $page_id <= 0 ) {
			return 0;
		}

		$page = get_post( $page_id );
		if ( ! $page instanceof \WP_Post || 'page' !== $page->post_type ) {
			return 0;
		}

		return (int) $page->ID;
	}

	/**
	 * Safe bounded integer.
	 *
	 * @param mixed $value Raw.
	 * @param int   $min   Min.
	 * @param int   $max   Max.
	 * @param int   $fallback Fallback.
	 * @return int
	 */
	private static function sanitize_int( $value, $min, $max, $fallback ) {
		$int = is_numeric( $value ) ? (int) $value : (int) $fallback;
		return max( (int) $min, min( (int) $max, $int ) );
	}

	/**
	 * Safe text.
	 *
	 * @param mixed  $value Raw.
	 * @param int    $max Max chars.
	 * @param string $fallback Fallback.
	 * @return string
	 */
	private static function sanitize_text( $value, $max, $fallback = '' ) {
		if ( ! is_string( $value ) && ! is_numeric( $value ) ) {
			return (string) $fallback;
		}

		$text = sanitize_text_field( wp_unslash( (string) $value ) );
		$text = trim( $text );

		if ( '' === $text ) {
			return (string) $fallback;
		}

		if ( function_exists( 'mb_substr' ) ) {
			return mb_substr( $text, 0, (int) $max, 'UTF-8' );
		}

		return substr( $text, 0, (int) $max );
	}

	/**
	 * Safe textarea.
	 *
	 * @param mixed  $value Raw.
	 * @param int    $max Max chars.
	 * @param string $fallback Fallback.
	 * @return string
	 */
	private static function sanitize_textarea( $value, $max, $fallback = '' ) {
		if ( ! is_string( $value ) && ! is_numeric( $value ) ) {
			return (string) $fallback;
		}

		$text = sanitize_textarea_field( wp_unslash( (string) $value ) );
		$text = trim( $text );

		if ( '' === $text ) {
			return (string) $fallback;
		}

		if ( function_exists( 'mb_substr' ) ) {
			return mb_substr( $text, 0, (int) $max, 'UTF-8' );
		}

		return substr( $text, 0, (int) $max );
	}

	/**
	 * Gate POST handlers.
	 *
	 * @return void
	 */
	private static function require_post_cap() {
		if ( ! is_user_logged_in() || ! current_user_can( self::CAPABILITY ) ) {
			wp_die( esc_html__( 'Недостаточно прав.', 'shpigovsky-core' ), 403 );
		}

		if ( 'POST' !== strtoupper( (string) ( $_SERVER['REQUEST_METHOD'] ?? '' ) ) ) {
			wp_die( esc_html__( 'Только POST.', 'shpigovsky-core' ), 405 );
		}
	}

	/**
	 * Render checkbox row.
	 *
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param bool   $checked Checked.
	 * @param string $help Help.
	 * @return void
	 */
	private static function row_checkbox( $name, $label, $checked, $help ) {
		echo '<tr><th>' . esc_html( $label ) . '</th><td>';
		printf(
			'<label><input type="checkbox" name="%1$s" value="1"%2$s /> %3$s</label>',
			esc_attr( $name ),
			checked( $checked, true, false ),
			esc_html( $label )
		);
		if ( '' !== $help ) {
			echo '<p class="description">' . esc_html( $help ) . '</p>';
		}
		echo '</td></tr>';
	}

	/**
	 * Render text row.
	 *
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param string $value Value.
	 * @param string $placeholder Placeholder.
	 * @param int    $maxlength Max length.
	 * @return void
	 */
	private static function row_text( $name, $label, $value, $placeholder, $maxlength ) {
		echo '<tr><th><label for="' . esc_attr( $name ) . '">' . esc_html( $label ) . '</label></th><td>';
		printf(
			'<input type="text" class="regular-text" id="%1$s" name="%1$s" value="%2$s" placeholder="%3$s" maxlength="%4$d" />',
			esc_attr( $name ),
			esc_attr( $value ),
			esc_attr( $placeholder ),
			(int) $maxlength
		);
		echo '</td></tr>';
	}

	/**
	 * Render textarea row.
	 *
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param string $value Value.
	 * @param int    $rows Rows.
	 * @param int    $maxlength Max chars.
	 * @return void
	 */
	private static function row_textarea( $name, $label, $value, $rows, $maxlength ) {
		echo '<tr><th><label for="' . esc_attr( $name ) . '">' . esc_html( $label ) . '</label></th><td>';
		printf(
			'<textarea class="large-text" id="%1$s" name="%1$s" rows="%2$d" maxlength="%3$d">%4$s</textarea>',
			esc_attr( $name ),
			(int) $rows,
			(int) $maxlength,
			esc_textarea( $value )
		);
		echo '</td></tr>';
	}

	/**
	 * Render number row.
	 *
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param int    $value Value.
	 * @param int    $min Min.
	 * @param int    $max Max.
	 * @param string $help Help.
	 * @return void
	 */
	private static function row_number( $name, $label, $value, $min, $max, $help ) {
		echo '<tr><th><label for="' . esc_attr( $name ) . '">' . esc_html( $label ) . '</label></th><td>';
		printf(
			'<input type="number" id="%1$s" name="%1$s" value="%2$d" min="%3$d" max="%4$d" step="1" />',
			esc_attr( $name ),
			(int) $value,
			(int) $min,
			(int) $max
		);
		if ( '' !== $help ) {
			echo '<p class="description">' . esc_html( $help ) . '</p>';
		}
		echo '</td></tr>';
	}

	/**
	 * Render page selector row.
	 *
	 * @param string $name Name.
	 * @param string $label Label.
	 * @param int    $selected Selected page ID.
	 * @param string $help Help.
	 * @return void
	 */
	private static function row_page_select( $name, $label, $selected, $help ) {
		echo '<tr><th><label for="' . esc_attr( $name ) . '">' . esc_html( $label ) . '</label></th><td>';
		wp_dropdown_pages(
			array(
				'name'             => $name,
				'id'               => $name,
				'selected'         => (int) $selected,
				'show_option_none' => __( '— Не выбрано —', 'shpigovsky-core' ),
				'option_none_value'=> '0',
			)
		);
		if ( '' !== $help ) {
			echo '<p class="description">' . esc_html( $help ) . '</p>';
		}
		echo '</td></tr>';
	}

	/**
	 * Render HTML row.
	 *
	 * @param string $label Label.
	 * @param string $html HTML.
	 * @return void
	 */
	private static function row_html( $label, $html ) {
		echo '<tr><th>' . esc_html( $label ) . '</th><td>' . $html . '</td></tr>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
	}
}

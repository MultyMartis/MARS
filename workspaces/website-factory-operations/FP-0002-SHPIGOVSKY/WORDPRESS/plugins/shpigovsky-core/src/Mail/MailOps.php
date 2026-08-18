<?php
/**
 * SMTP / form delivery configuration owner — PROD-P18C.
 *
 * Option names are allowlisted and must not contain smtp/password fragments
 * (see SiteSettings::prevent_secret_like_options). Nested keys may be technical.
 * The mailbox secret is never returned to Admin, REST, Dashboard, or logs.
 *
 * WordPress DB storage is not a dedicated secret manager.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Mail;

use Shpigovsky\Core\Admin\ActivityLog;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Canonical mail operations settings + readiness state.
 */
final class MailOps implements ModuleInterface {

	public const OPTION_CONFIG = 'fp02_mail_ops';
	public const OPTION_AUTH   = 'fp02_mailbox_auth';

	public const STATE_NOT_CONFIGURED          = 'not_configured';
	public const STATE_CONFIGURED_NOT_VERIFIED = 'configured_not_verified';
	public const STATE_VERIFIED_READY          = 'verified_ready';
	public const STATE_VERIFIED_ACTIVE         = 'verified_active';
	public const STATE_ERROR                   = 'error';

	public const ENCRYPTION_NONE = 'none';
	public const ENCRYPTION_SSL  = 'ssl';
	public const ENCRYPTION_TLS  = 'tls';

	public const DEFAULT_FROM_EMAIL = 'noreply@shpigovsky.ru';
	public const DEFAULT_FROM_NAME  = 'Шпиговский Дом';
	public const FORM_KEY           = 'consultation';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'mail.ops';
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
		add_filter( 'wp_mail_from', array( __CLASS__, 'filter_from_email' ), 20 );
		add_filter( 'wp_mail_from_name', array( __CLASS__, 'filter_from_name' ), 20 );
	}

	/**
	 * Option names allowed through the secret-like name guard.
	 *
	 * @return array<int, string>
	 */
	public static function allowlisted_option_names() {
		return array( self::OPTION_CONFIG, self::OPTION_AUTH );
	}

	/**
	 * Default non-secret config.
	 *
	 * @return array<string, mixed>
	 */
	public static function default_config() {
		return array(
			'smtp_enabled'             => 0,
			'smtp_host'                => '',
			'smtp_port'                => 0,
			'smtp_encryption'          => self::ENCRYPTION_NONE,
			'smtp_auth'                => 1,
			'smtp_username'            => '',
			'smtp_from_email'          => self::DEFAULT_FROM_EMAIL,
			'smtp_from_name'           => '',
			'recipients'               => array(),
			'reply_to_mode'            => 'visitor_if_valid',
			'form_metrika_goal'        => '',
			'lead_logging'             => 1,
			'lead_retention_days'      => 0,
			'verified'                 => 0,
			'verified_at'              => '',
			'last_test_status'         => '',
			'last_test_error_category' => '',
			'delivery_active'          => 0,
		);
	}

	/**
	 * Read config without secrets.
	 *
	 * @return array<string, mixed>
	 */
	public static function get_config() {
		$stored = get_option( self::OPTION_CONFIG, array() );
		if ( ! is_array( $stored ) ) {
			$stored = array();
		}
		$cfg = array_merge( self::default_config(), $stored );
		$cfg['smtp_enabled']        = (int) $cfg['smtp_enabled'] ? 1 : 0;
		$cfg['smtp_auth']           = (int) $cfg['smtp_auth'] ? 1 : 0;
		$cfg['smtp_port']           = (int) $cfg['smtp_port'];
		$cfg['verified']            = (int) $cfg['verified'] ? 1 : 0;
		$cfg['delivery_active']     = (int) $cfg['delivery_active'] ? 1 : 0;
		$cfg['lead_logging']        = 1;
		$cfg['lead_retention_days'] = max( 0, (int) $cfg['lead_retention_days'] );
		$cfg['smtp_encryption']     = self::sanitize_encryption( (string) $cfg['smtp_encryption'] );
		$cfg['recipients']          = self::normalize_recipients( $cfg['recipients'] );
		$cfg['smtp_from_email']     = self::sanitize_email_or_default( (string) $cfg['smtp_from_email'] );
		$cfg['smtp_from_name']      = is_string( $cfg['smtp_from_name'] ) ? $cfg['smtp_from_name'] : '';
		$cfg['smtp_host']           = is_string( $cfg['smtp_host'] ) ? $cfg['smtp_host'] : '';
		$cfg['smtp_username']       = is_string( $cfg['smtp_username'] ) ? $cfg['smtp_username'] : '';
		$cfg['form_metrika_goal']   = is_string( $cfg['form_metrika_goal'] ) ? $cfg['form_metrika_goal'] : '';
		unset( $cfg['smtp_password'], $cfg['password'], $cfg['secret'] );
		return $cfg;
	}

	/**
	 * Whether a mailbox secret is stored.
	 *
	 * @return bool
	 */
	public static function password_is_configured() {
		$auth = get_option( self::OPTION_AUTH, array() );
		if ( ! is_array( $auth ) ) {
			return false;
		}
		return ! empty( $auth['configured'] ) && isset( $auth['secret'] ) && is_string( $auth['secret'] ) && '' !== $auth['secret'];
	}

	/**
	 * Mailbox secret for transport only. Never pass to HTML, logs, or REST.
	 *
	 * @return string
	 */
	public static function get_password_for_transport() {
		$auth = get_option( self::OPTION_AUTH, array() );
		if ( ! is_array( $auth ) || empty( $auth['secret'] ) || ! is_string( $auth['secret'] ) ) {
			return '';
		}
		return $auth['secret'];
	}

	/**
	 * Human-readable sender name.
	 *
	 * @return string
	 */
	public static function from_name() {
		$cfg = self::get_config();
		if ( '' !== trim( (string) $cfg['smtp_from_name'] ) ) {
			return trim( (string) $cfg['smtp_from_name'] );
		}
		$org = '';
		if ( function_exists( 'get_field' ) ) {
			$raw = get_field( 'organisation_name', 'option' );
			if ( is_string( $raw ) ) {
				$org = trim( $raw );
			}
		}
		if ( '' !== $org ) {
			return $org;
		}
		$blog = trim( (string) get_option( 'blogname', '' ) );
		return '' !== $blog ? $blog : self::DEFAULT_FROM_NAME;
	}

	/**
	 * Technical From address.
	 *
	 * @return string
	 */
	public static function from_email() {
		$cfg = self::get_config();
		return self::sanitize_email_or_default( (string) $cfg['smtp_from_email'] );
	}

	/**
	 * Valid recipient emails in list order (main first).
	 *
	 * @return array<int, string>
	 */
	public static function recipient_emails() {
		$emails = array();
		foreach ( self::get_config()['recipients'] as $row ) {
			if ( ! empty( $row['email'] ) && is_email( $row['email'] ) ) {
				$emails[] = $row['email'];
			}
		}
		return array_values( array_unique( $emails ) );
	}

	/**
	 * Configuration completeness (not the same as verified).
	 *
	 * @return bool
	 */
	public static function is_complete() {
		$cfg = self::get_config();
		if ( '' === trim( (string) $cfg['smtp_host'] ) ) {
			return false;
		}
		$port = (int) $cfg['smtp_port'];
		if ( $port < 1 || $port > 65535 ) {
			return false;
		}
		if ( ! is_email( self::from_email() ) ) {
			return false;
		}
		if ( empty( self::recipient_emails() ) ) {
			return false;
		}
		if ( $cfg['smtp_auth'] ) {
			if ( '' === trim( (string) $cfg['smtp_username'] ) ) {
				return false;
			}
			if ( ! self::password_is_configured() ) {
				return false;
			}
		}
		return true;
	}

	/**
	 * Computed operator-facing state.
	 *
	 * @return string
	 */
	public static function state() {
		$cfg = self::get_config();
		if ( 'fail' === (string) $cfg['last_test_status'] && self::is_complete() ) {
			return self::STATE_ERROR;
		}
		if ( ! self::is_complete() ) {
			return self::STATE_NOT_CONFIGURED;
		}
		if ( $cfg['verified'] && $cfg['delivery_active'] ) {
			return self::STATE_VERIFIED_ACTIVE;
		}
		if ( $cfg['verified'] ) {
			return self::STATE_VERIFIED_READY;
		}
		return self::STATE_CONFIGURED_NOT_VERIFIED;
	}

	/**
	 * Russian label for computed state.
	 *
	 * @param string $state State key.
	 * @return string
	 */
	public static function state_label( $state = '' ) {
		$state = '' === $state ? self::state() : (string) $state;
		$map   = array(
			self::STATE_NOT_CONFIGURED          => __( 'NOT CONFIGURED', 'shpigovsky-core' ),
			self::STATE_CONFIGURED_NOT_VERIFIED => __( 'CONFIGURED / NOT VERIFIED', 'shpigovsky-core' ),
			self::STATE_VERIFIED_READY          => __( 'VERIFIED / NOT ACTIVE', 'shpigovsky-core' ),
			self::STATE_VERIFIED_ACTIVE         => __( 'VERIFIED / ACTIVE', 'shpigovsky-core' ),
			self::STATE_ERROR                   => __( 'ERROR', 'shpigovsky-core' ),
		);
		return isset( $map[ $state ] ) ? $map[ $state ] : $state;
	}

	/**
	 * Dashboard mail line for this wave / later waves.
	 *
	 * @return string
	 */
	public static function dashboard_mail_line() {
		$state = self::state();
		if ( self::STATE_NOT_CONFIGURED === $state ) {
			return __( 'SMTP SETTINGS READY — CREDENTIALS REQUIRED', 'shpigovsky-core' );
		}
		if ( self::STATE_CONFIGURED_NOT_VERIFIED === $state ) {
			return __( 'SMTP CONFIGURED / NOT VERIFIED — подавление включено', 'shpigovsky-core' );
		}
		if ( self::STATE_VERIFIED_READY === $state ) {
			return __( 'SMTP VERIFIED — отправка ещё не активирована', 'shpigovsky-core' );
		}
		if ( self::STATE_VERIFIED_ACTIVE === $state ) {
			return __( 'SMTP VERIFIED / ACTIVE', 'shpigovsky-core' );
		}
		return __( 'SMTP ERROR — подавление включено', 'shpigovsky-core' );
	}

	/**
	 * Whether MU / plugin should short-circuit wp_mail.
	 *
	 * @return bool
	 */
	public static function should_suppress() {
		if ( defined( 'FP02_MAIL_ALLOW_ONCE' ) && FP02_MAIL_ALLOW_ONCE ) {
			return false;
		}
		return 1 !== (int) self::get_config()['delivery_active'];
	}

	/**
	 * Whether a form should attempt outbound mail.
	 *
	 * @return bool
	 */
	public static function should_attempt_mail() {
		return ! self::should_suppress() && self::is_complete() && self::STATE_VERIFIED_ACTIVE === self::state();
	}

	/**
	 * Yandex Metrika counter from SEO settings (one owner).
	 *
	 * @return string
	 */
	public static function metrika_counter_id() {
		if ( ! function_exists( 'get_field' ) ) {
			return '';
		}
		$raw = get_field( 'yandex_metrica_counter_id', 'option' );
		if ( ! is_string( $raw ) && ! is_numeric( $raw ) ) {
			return '';
		}
		$id = preg_replace( '/\D+/', '', (string) $raw );
		return is_string( $id ) ? $id : '';
	}

	/**
	 * Safe Metrika goal identifier for the consultation form.
	 *
	 * @return string
	 */
	public static function metrika_goal() {
		$goal = (string) self::get_config()['form_metrika_goal'];
		$goal = preg_replace( '/[^A-Za-z0-9_\-.]/', '', $goal );
		return is_string( $goal ) ? $goal : '';
	}

	/**
	 * Save posted Admin fields. Blank password keeps the existing secret.
	 *
	 * @param array<string, mixed> $posted Posted data.
	 * @return array{ok:bool,errors:array<string,string>}
	 */
	public static function save_from_post( array $posted ) {
		$cfg      = self::get_config();
		$errors   = array();
		$enabled  = ! empty( $posted['smtp_enabled'] ) ? 1 : 0;
		$host     = self::sanitize_host( isset( $posted['smtp_host'] ) ? (string) $posted['smtp_host'] : '' );
		$port     = isset( $posted['smtp_port'] ) ? (int) $posted['smtp_port'] : 0;
		$enc      = self::sanitize_encryption( isset( $posted['smtp_encryption'] ) ? (string) $posted['smtp_encryption'] : self::ENCRYPTION_NONE );
		$auth     = ! empty( $posted['smtp_auth'] ) ? 1 : 0;
		$username = isset( $posted['smtp_username'] ) ? sanitize_text_field( (string) $posted['smtp_username'] ) : '';
		$from     = isset( $posted['smtp_from_email'] ) ? sanitize_email( (string) $posted['smtp_from_email'] ) : '';
		$name     = isset( $posted['smtp_from_name'] ) ? sanitize_text_field( (string) $posted['smtp_from_name'] ) : '';
		$goal     = isset( $posted['form_metrika_goal'] ) ? (string) $posted['form_metrika_goal'] : '';
		$goal     = preg_replace( '/[^A-Za-z0-9_\-.]/', '', $goal );
		$retain   = isset( $posted['lead_retention_days'] ) ? max( 0, (int) $posted['lead_retention_days'] ) : 0;
		$new_pass = isset( $posted['smtp_password'] ) ? (string) $posted['smtp_password'] : '';
		$clear    = ! empty( $posted['smtp_password_clear'] );

		$recipients = array();
		$raw_rows   = isset( $posted['recipients'] ) && is_array( $posted['recipients'] ) ? $posted['recipients'] : array();
		foreach ( $raw_rows as $row ) {
			if ( ! is_array( $row ) ) {
				continue;
			}
			$email = isset( $row['email'] ) ? sanitize_email( (string) $row['email'] ) : '';
			$label = isset( $row['label'] ) ? sanitize_text_field( (string) $row['label'] ) : '';
			if ( '' === $email && '' === $label ) {
				continue;
			}
			if ( '' !== $email && ! is_email( $email ) ) {
				$errors['recipients'] = __( 'Проверьте адреса получателей.', 'shpigovsky-core' );
				continue;
			}
			if ( is_email( $email ) ) {
				$recipients[] = array(
					'email' => $email,
					'label' => $label,
				);
			}
		}

		if ( $enabled || '' !== $host ) {
			if ( '' === $host ) {
				$errors['smtp_host'] = __( 'Укажите SMTP-сервер.', 'shpigovsky-core' );
			}
			if ( $port < 1 || $port > 65535 ) {
				$errors['smtp_port'] = __( 'Укажите корректный порт (1–65535).', 'shpigovsky-core' );
			}
			if ( $auth && '' === $username ) {
				$errors['smtp_username'] = __( 'Укажите имя пользователя SMTP.', 'shpigovsky-core' );
			}
			if ( $auth && ! self::password_is_configured() && '' === $new_pass && ! $clear ) {
				$errors['smtp_password'] = __( 'Укажите пароль почтового ящика.', 'shpigovsky-core' );
			}
		}

		if ( '' === $from || ! is_email( $from ) ) {
			$errors['smtp_from_email'] = __( 'Укажите корректный email отправителя.', 'shpigovsky-core' );
		}

		if ( ! empty( $errors ) ) {
			return array(
				'ok'     => false,
				'errors' => $errors,
			);
		}

		$was_complete = self::is_complete();

		$cfg['smtp_enabled']        = $enabled;
		$cfg['smtp_host']           = $host;
		$cfg['smtp_port']           = $port;
		$cfg['smtp_encryption']     = $enc;
		$cfg['smtp_auth']           = $auth;
		$cfg['smtp_username']       = $username;
		$cfg['smtp_from_email']     = $from;
		$cfg['smtp_from_name']      = $name;
		$cfg['recipients']          = $recipients;
		$cfg['form_metrika_goal']   = is_string( $goal ) ? $goal : '';
		$cfg['lead_retention_days'] = $retain;
		$cfg['lead_logging']        = 1;

		if ( $clear ) {
			self::store_password( '' );
			$cfg['verified']                 = 0;
			$cfg['verified_at']              = '';
			$cfg['last_test_status']         = '';
			$cfg['last_test_error_category'] = '';
			$cfg['delivery_active']          = 0;
		} elseif ( '' !== $new_pass ) {
			self::store_password( $new_pass );
			$cfg['verified']                 = 0;
			$cfg['verified_at']              = '';
			$cfg['last_test_status']         = '';
			$cfg['last_test_error_category'] = '';
			$cfg['delivery_active']          = 0;
		}

		$now_complete = self::compute_complete( $cfg, self::password_is_configured() );
		if ( $was_complete && ! $now_complete ) {
			$cfg['verified']                 = 0;
			$cfg['delivery_active']          = 0;
			$cfg['last_test_status']         = '';
			$cfg['last_test_error_category'] = '';
		}

		update_option( self::OPTION_CONFIG, $cfg, false );

		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event(
				'smtp_config_updated',
				'setting',
				'Почта и формы: настройки сохранены',
				0
			);
		}

		return array(
			'ok'     => true,
			'errors' => array(),
		);
	}

	/**
	 * Record a sanitized SMTP test result. Does not activate delivery.
	 *
	 * @param bool   $ok Success.
	 * @param string $category Sanitized error category.
	 */
	public static function record_test_result( $ok, $category = '' ) {
		$cfg = self::get_config();
		if ( $ok ) {
			$cfg['verified']                 = 1;
			$cfg['verified_at']              = gmdate( 'Y-m-d H:i:s' ) . ' UTC';
			$cfg['last_test_status']         = 'ok';
			$cfg['last_test_error_category'] = '';
		} else {
			$cfg['verified']                 = 0;
			$cfg['delivery_active']          = 0;
			$cfg['last_test_status']         = 'fail';
			$cfg['last_test_error_category'] = self::sanitize_error_category( $category );
		}
		update_option( self::OPTION_CONFIG, $cfg, false );
	}

	/**
	 * Activate production outbound mail. Requires verified complete config.
	 *
	 * @return bool
	 */
	public static function activate_delivery() {
		if ( ! self::is_complete() || 1 !== (int) self::get_config()['verified'] ) {
			return false;
		}
		$cfg                     = self::get_config();
		$cfg['delivery_active']  = 1;
		$cfg['last_test_status'] = 'ok';
		update_option( self::OPTION_CONFIG, $cfg, false );
		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event( 'smtp_activated', 'setting', 'Почта: исходящая отправка активирована', 0 );
		}
		return true;
	}

	/**
	 * Deactivate outbound mail. Suppression returns.
	 *
	 * @return void
	 */
	public static function deactivate_delivery() {
		$cfg                    = self::get_config();
		$cfg['delivery_active'] = 0;
		update_option( self::OPTION_CONFIG, $cfg, false );
		if ( class_exists( ActivityLog::class ) ) {
			ActivityLog::log_system_event( 'smtp_deactivated', 'setting', 'Почта: исходящая отправка выключена', 0 );
		}
	}

	/**
	 * wp_mail_from filter.
	 *
	 * @param string $email Email.
	 * @return string
	 */
	public static function filter_from_email( $email ) {
		$from = self::from_email();
		return is_email( $from ) ? $from : $email;
	}

	/**
	 * wp_mail_from_name filter.
	 *
	 * @param string $name Name.
	 * @return string
	 */
	public static function filter_from_name( $name ) {
		$custom = self::from_name();
		return '' !== $custom ? $custom : $name;
	}

	/**
	 * Sanitize PHPMailer / wp_mail failure into a category. Never include secrets.
	 *
	 * @param string $raw Raw error.
	 * @return string
	 */
	public static function sanitize_error_category( $raw ) {
		$raw = strtolower( wp_strip_all_tags( (string) $raw ) );
		$raw = preg_replace( '/[^\x20-\x7E]/', '', $raw );
		if ( false !== strpos( $raw, 'auth' ) || false !== strpos( $raw, '535' ) || false !== strpos( $raw, 'password' ) ) {
			return 'auth_failed';
		}
		if ( false !== strpos( $raw, 'connect' ) || false !== strpos( $raw, 'timed out' ) || false !== strpos( $raw, 'timeout' ) ) {
			return 'connection_failed';
		}
		if ( false !== strpos( $raw, 'certificate' ) || false !== strpos( $raw, 'ssl' ) || false !== strpos( $raw, 'tls' ) ) {
			return 'tls_failed';
		}
		if ( false !== strpos( $raw, 'recipient' ) || false !== strpos( $raw, 'rcpt' ) ) {
			return 'recipient_rejected';
		}
		if ( defined( 'FP02_MAIL_ALLOW_ONCE' ) && false !== strpos( $raw, 'suppress' ) ) {
			return 'suppressed';
		}
		return 'send_failed';
	}

	/**
	 * @param string $host Host.
	 * @return string
	 */
	private static function sanitize_host( $host ) {
		$host = strtolower( trim( sanitize_text_field( $host ) ) );
		$host = preg_replace( '/^ssl:\/\//', '', $host );
		$host = preg_replace( '/[^a-z0-9.\-]/', '', $host );
		return is_string( $host ) ? $host : '';
	}

	/**
	 * @param string $enc Encryption.
	 * @return string
	 */
	public static function sanitize_encryption( $enc ) {
		$enc = strtolower( sanitize_key( $enc ) );
		if ( in_array( $enc, array( self::ENCRYPTION_NONE, self::ENCRYPTION_SSL, self::ENCRYPTION_TLS ), true ) ) {
			return $enc;
		}
		return self::ENCRYPTION_NONE;
	}

	/**
	 * @param mixed $rows Recipients.
	 * @return array<int, array{email:string,label:string}>
	 */
	private static function normalize_recipients( $rows ) {
		$out = array();
		if ( ! is_array( $rows ) ) {
			return $out;
		}
		foreach ( $rows as $row ) {
			if ( is_string( $row ) && is_email( $row ) ) {
				$out[] = array(
					'email' => $row,
					'label' => '',
				);
				continue;
			}
			if ( ! is_array( $row ) ) {
				continue;
			}
			$email = isset( $row['email'] ) ? sanitize_email( (string) $row['email'] ) : '';
			$label = isset( $row['label'] ) ? sanitize_text_field( (string) $row['label'] ) : '';
			if ( is_email( $email ) ) {
				$out[] = array(
					'email' => $email,
					'label' => $label,
				);
			}
		}
		return $out;
	}

	/**
	 * @param string $email Email.
	 * @return string
	 */
	private static function sanitize_email_or_default( $email ) {
		$email = sanitize_email( $email );
		return is_email( $email ) ? $email : self::DEFAULT_FROM_EMAIL;
	}

	/**
	 * @param array<string, mixed> $cfg Config.
	 * @param bool                 $has_password Password present.
	 * @return bool
	 */
	private static function compute_complete( array $cfg, $has_password ) {
		if ( '' === trim( (string) $cfg['smtp_host'] ) ) {
			return false;
		}
		$port = (int) $cfg['smtp_port'];
		if ( $port < 1 || $port > 65535 ) {
			return false;
		}
		if ( ! is_email( (string) $cfg['smtp_from_email'] ) ) {
			return false;
		}
		$emails = array();
		foreach ( self::normalize_recipients( $cfg['recipients'] ) as $row ) {
			$emails[] = $row['email'];
		}
		if ( empty( $emails ) ) {
			return false;
		}
		if ( ! empty( $cfg['smtp_auth'] ) ) {
			if ( '' === trim( (string) $cfg['smtp_username'] ) ) {
				return false;
			}
			if ( ! $has_password ) {
				return false;
			}
		}
		return true;
	}

	/**
	 * @param string $secret Secret or empty to clear.
	 */
	private static function store_password( $secret ) {
		if ( '' === $secret ) {
			update_option(
				self::OPTION_AUTH,
				array(
					'configured' => 0,
					'secret'     => '',
				),
				false
			);
			return;
		}
		update_option(
			self::OPTION_AUTH,
			array(
				'configured' => 1,
				'secret'     => $secret,
			),
			false
		);
	}
}

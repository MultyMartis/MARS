<?php
/**
 * Lead form AJAX handler — persist first, then optional wp_mail.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Forms;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Leads\LeadRegistry;
use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Unified lead / consultation form submission handler (wp_ajax).
 *
 * Validate → persist lead → attempt mail → update status → JSON.
 * Frontend success means the lead was stored, not that email was delivered.
 */
final class ConsultationHandler implements ModuleInterface {

	/**
	 * AJAX action name (also FormData action field).
	 */
	public const AJAX_ACTION = 'fp02_lead_submit';

	/**
	 * Nonce action.
	 */
	public const NONCE_ACTION = 'fp02_lead_submit';

	/**
	 * Historical pre-SMTP recipient constant. Recipients now come from Admin
	 * «Почта и формы». Do not send to this address.
	 */
	public const FUTURE_RECIPIENT = '';

	/**
	 * Minimum seconds between form render and submit.
	 */
	public const MIN_FILL_SECONDS = 3;

	/**
	 * Maximum form session age (seconds).
	 */
	public const MAX_FILL_SECONDS = 86400;

	/**
	 * Per-IP rate limit window (seconds).
	 */
	public const RATE_LIMIT_WINDOW = 3600;

	/**
	 * Max accepted submissions per IP per window.
	 */
	public const RATE_LIMIT_MAX = 8;

	/**
	 * Duplicate request token TTL (seconds).
	 */
	public const DUPLICATE_TOKEN_TTL = 600;

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'forms.consultation';
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
		add_action( 'wp_ajax_' . self::AJAX_ACTION, array( __CLASS__, 'handle_ajax' ) );
		add_action( 'wp_ajax_nopriv_' . self::AJAX_ACTION, array( __CLASS__, 'handle_ajax' ) );
		add_action( 'wp_enqueue_scripts', array( __CLASS__, 'localize_lead_form_script' ), 30 );

		// Legacy admin-post boundary retained as safe no-op redirect.
		add_action( 'admin_post_nopriv_shpigovsky_consultation', array( __CLASS__, 'handle_legacy_post' ) );
		add_action( 'admin_post_shpigovsky_consultation', array( __CLASS__, 'handle_legacy_post' ) );
	}

	/**
	 * Localize endpoint / nonce / messages onto theme shell script.
	 */
	public static function localize_lead_form_script() {
		if ( ! wp_script_is( 'shpigovsky-v9-shell', 'enqueued' ) && ! wp_script_is( 'shpigovsky-v9-shell', 'registered' ) ) {
			return;
		}

		wp_localize_script(
			'shpigovsky-v9-shell',
			'fp02LeadForm',
			array(
				'endpoint'               => admin_url( 'admin-ajax.php' ),
				'action'                 => self::AJAX_ACTION,
				'nonce'                  => wp_create_nonce( self::NONCE_ACTION ),
				'nonceField'             => 'fp02_lead_nonce',
				'phoneMask'              => '+7 999 999 - 99 - 99',
				'recaptchaAction'        => 'form_lead',
				'siteConfigEndpoint'     => '',
				'backendBlockedMessage'  => self::message( 'backend_blocked' ),
				'validationErrorMessage' => self::message( 'validation' ),
				'recaptchaSecurityMessage' => self::message( 'recaptcha' ),
				'successMessage'         => self::message( 'local_success' ),
				'rateLimitedMessage'     => self::message( 'rate_limited' ),
				'duplicateMessage'       => self::message( 'duplicate' ),
				'formKey'                => LeadRegistry::FORM_KEY,
				'metrikaCounter'         => MailOps::metrika_counter_id(),
				'metrikaGoal'            => MailOps::metrika_goal(),
				'messages'               => array(
					'local_success'  => self::message( 'local_success' ),
					'validation'     => self::message( 'validation' ),
					'rate_limited'   => self::message( 'rate_limited' ),
					'duplicate'      => self::message( 'duplicate' ),
					'honeypot'       => self::message( 'honeypot' ),
					'too_fast'       => self::message( 'too_fast' ),
					'stale'          => self::message( 'stale' ),
					'server_error'   => self::message( 'server_error' ),
					'backend_blocked'=> self::message( 'backend_blocked' ),
				),
			)
		);
	}

	/**
	 * AJAX entry point.
	 */
	public static function handle_ajax() {
		nocache_headers();

		if ( 'POST' !== strtoupper( (string) ( $_SERVER['REQUEST_METHOD'] ?? '' ) ) ) {
			self::json_response( false, self::message( 'method' ), 405 );
		}

		$nonce = isset( $_POST['fp02_lead_nonce'] )
			? sanitize_text_field( wp_unslash( $_POST['fp02_lead_nonce'] ) )
			: ( isset( $_POST['_wpnonce'] ) ? sanitize_text_field( wp_unslash( $_POST['_wpnonce'] ) ) : '' );

		if ( ! $nonce || ! wp_verify_nonce( $nonce, self::NONCE_ACTION ) ) {
			self::json_response( false, self::message( 'nonce' ), 403 );
		}

		$honeypot = isset( $_POST['company_url'] ) ? trim( (string) wp_unslash( $_POST['company_url'] ) ) : '';
		if ( '' !== $honeypot ) {
			// Silent accept for bots — do not reveal honeypot logic.
			self::json_response( true, self::message( 'local_success' ), 200, array( 'mode' => 'pre_smtp', 'spam' => true ) );
		}

		$timing = self::check_fill_timing( $_POST );
		if ( ! $timing['ok'] ) {
			self::json_response( false, $timing['message'], 422 );
		}

		$ip = self::client_ip();
		if ( ! self::check_rate_limit( $ip ) ) {
			self::json_response( false, self::message( 'rate_limited' ), 429 );
		}

		$request_token = isset( $_POST['request_token'] )
			? sanitize_text_field( wp_unslash( $_POST['request_token'] ) )
			: '';

		if ( '' === $request_token || strlen( $request_token ) < 16 || strlen( $request_token ) > 128 ) {
			self::json_response( false, self::message( 'validation' ), 422 );
		}

		if ( ! self::claim_request_token( $request_token ) ) {
			self::json_response( false, self::message( 'duplicate' ), 409 );
		}

		$payload = self::sanitize_payload( $_POST );
		$errors  = self::validate_payload( $payload );

		if ( ! empty( $errors ) ) {
			self::json_response(
				false,
				self::message( 'validation' ),
				422,
				array(
					'fields' => $errors,
				)
			);
		}

		$lead_id = self::persist_lead( $payload );
		if ( $lead_id <= 0 ) {
			self::json_response( false, self::message( 'server_error' ), 500 );
		}

		$mail = self::attempt_outbound_mail( $payload, $lead_id );
		self::bump_rate_limit( $ip );

		self::json_response(
			true,
			self::message( 'local_success' ),
			200,
			array(
				'accepted'        => true,
				'mail_attempted'  => (bool) $mail['attempted'],
				'mail_accepted'   => (bool) $mail['accepted'],
				'mail_status'     => $mail['status'],
				'form_key'        => LeadRegistry::FORM_KEY,
				'metrika_goal'    => MailOps::metrika_goal(),
				'metrika_counter' => MailOps::metrika_counter_id(),
				'metrika_event'   => 'form_submission_accepted',
			)
		);
	}

	/**
	 * Legacy admin-post handler — no processing.
	 */
	public static function handle_legacy_post() {
		wp_safe_redirect( wp_get_referer() ? wp_get_referer() : home_url( '/' ) );
		exit;
	}

	/**
	 * Russian operator-facing messages.
	 *
	 * @param string $key Message key.
	 * @return string
	 */
	public static function message( $key ) {
		$messages = array(
			'local_success'   => 'Заявка принята. Мы свяжемся с вами по указанному телефону.',
			'validation'      => 'Проверьте поля формы и попробуйте снова.',
			'rate_limited'    => 'Слишком много заявок с вашего адреса. Подождите немного или позвоните нам: 8 (925) 183-64-64.',
			'duplicate'       => 'Эта заявка уже была отправлена. Обновите страницу, если нужно отправить новую.',
			'honeypot'        => 'Заявка отклонена.',
			'too_fast'        => 'Форма отправлена слишком быстро. Попробуйте ещё раз.',
			'stale'           => 'Сессия формы устарела. Обновите страницу и отправьте снова.',
			'nonce'           => 'Сессия безопасности устарела. Обновите страницу и попробуйте снова.',
			'method'          => 'Метод не поддерживается.',
			'server_error'    => 'Не удалось принять заявку. Позвоните нам: 8 (925) 183-64-64.',
			'backend_blocked' => 'Отправка заявки пока недоступна. Позвоните нам по телефону 8 (925) 183-64-64.',
			'recaptcha'       => 'Проверка безопасности не пройдена. Обновите страницу и попробуйте снова.',
		);

		return isset( $messages[ $key ] ) ? $messages[ $key ] : $messages['server_error'];
	}

	/**
	 * @param array<string,mixed> $input Raw POST.
	 * @return array{ok:bool,message:string}
	 */
	private static function check_fill_timing( array $input ) {
		$started_raw   = isset( $input['form_started_at'] ) ? (string) wp_unslash( $input['form_started_at'] ) : '';
		$submitted_raw = isset( $input['timestamp'] ) ? (string) wp_unslash( $input['timestamp'] ) : '';

		$started_at   = self::parse_time( $started_raw );
		$submitted_at = self::parse_time( $submitted_raw );

		if ( null === $started_at || null === $submitted_at ) {
			return array(
				'ok'      => false,
				'message' => self::message( 'validation' ),
			);
		}

		$delta = $submitted_at - $started_at;

		if ( $delta < self::MIN_FILL_SECONDS ) {
			return array(
				'ok'      => false,
				'message' => self::message( 'too_fast' ),
			);
		}

		if ( $delta > self::MAX_FILL_SECONDS ) {
			return array(
				'ok'      => false,
				'message' => self::message( 'stale' ),
			);
		}

		return array(
			'ok'      => true,
			'message' => '',
		);
	}

	/**
	 * @param string $value Time string or unix epoch.
	 * @return int|null
	 */
	private static function parse_time( $value ) {
		$value = trim( (string) $value );
		if ( '' === $value ) {
			return null;
		}

		if ( preg_match( '/^\d{10,13}$/', $value ) ) {
			$ts = (int) $value;
			if ( $ts > 20000000000 ) {
				$ts = (int) floor( $ts / 1000 );
			}
			return $ts > 0 ? $ts : null;
		}

		$parsed = strtotime( $value );
		return false === $parsed ? null : $parsed;
	}

	/**
	 * @param array<string,mixed> $input Raw POST.
	 * @return array<string,string>
	 */
	private static function sanitize_payload( array $input ) {
		$name    = self::sanitize_text( isset( $input['name'] ) ? $input['name'] : '', 120 );
		$phone   = self::sanitize_text( isset( $input['phone'] ) ? $input['phone'] : '', 40 );
		$email   = self::sanitize_text( isset( $input['email'] ) ? $input['email'] : '', 120 );
		$message_raw = isset( $input['message'] ) ? $input['message'] : '';
		$message     = is_string( $message_raw ) || is_numeric( $message_raw )
			? sanitize_textarea_field( wp_unslash( (string) $message_raw ) )
			: '';
		if ( function_exists( 'mb_substr' ) ) {
			$message = mb_substr( $message, 0, 4000, 'UTF-8' );
		} else {
			$message = substr( $message, 0, 4000 );
		}

		$consent_raw = isset( $input['consent'] ) ? $input['consent'] : '';
		$consent     = in_array( (string) $consent_raw, array( '1', 'on', 'true', 'yes' ), true ) || true === $consent_raw;

		return array(
			'name'         => $name,
			'phone'        => $phone,
			'email'        => $email,
			'message'      => $message,
			'consent'      => $consent ? '1' : '',
			'form_context' => self::sanitize_text( isset( $input['form_context'] ) ? $input['form_context'] : '', 64 ),
			'lead_source'  => self::sanitize_text( isset( $input['lead_source'] ) ? $input['lead_source'] : '', 120 ),
			'page_url'     => self::sanitize_text( isset( $input['page_url'] ) ? $input['page_url'] : '', 500 ),
			'page_title'   => self::sanitize_text( isset( $input['page_title'] ) ? $input['page_title'] : '', 200 ),
			'utm_source'   => self::sanitize_text( isset( $input['utm_source'] ) ? $input['utm_source'] : '', 120 ),
			'utm_medium'   => self::sanitize_text( isset( $input['utm_medium'] ) ? $input['utm_medium'] : '', 120 ),
			'utm_campaign' => self::sanitize_text( isset( $input['utm_campaign'] ) ? $input['utm_campaign'] : '', 120 ),
			'utm_content'  => self::sanitize_text( isset( $input['utm_content'] ) ? $input['utm_content'] : '', 120 ),
			'utm_term'     => self::sanitize_text( isset( $input['utm_term'] ) ? $input['utm_term'] : '', 120 ),
			'referrer'     => self::sanitize_text( isset( $input['referrer'] ) ? $input['referrer'] : '', 255 ),
			'is_qa'        => ! empty( $input['fp02_qa'] ),
		);
	}

	/**
	 * @param array<string,string> $payload Sanitized payload.
	 * @return array<string,string>
	 */
	private static function validate_payload( array $payload ) {
		$errors = array();

		if ( '' === $payload['name'] || mb_strlen( $payload['name'] ) < 2 ) {
			$errors['name'] = 'Укажите ваше имя';
		}

		$digits = preg_replace( '/\D+/', '', $payload['phone'] );
		$digits = is_string( $digits ) ? $digits : '';
		$phone_ok = strlen( $digits ) >= 10;
		if ( 0 === strpos( $digits, '7' ) || 0 === strpos( $digits, '8' ) ) {
			$phone_ok = strlen( $digits ) >= 11;
		}
		if ( ! $phone_ok ) {
			$errors['phone'] = 'Укажите корректный номер телефона';
		}

		if ( '' !== $payload['email'] && ! is_email( $payload['email'] ) ) {
			$errors['email'] = 'Укажите корректный email или оставьте поле пустым';
		}

		if ( '' === $payload['message'] || mb_strlen( $payload['message'] ) < 3 ) {
			$errors['message'] = 'Опишите ситуацию';
		}

		if ( '1' !== $payload['consent'] ) {
			$errors['consent'] = 'Подтвердите согласие на обработку данных';
		}

		return $errors;
	}

	/**
	 * @param mixed $value Raw value.
	 * @param int   $max Max length.
	 * @return string
	 */
	private static function sanitize_text( $value, $max ) {
		if ( ! is_string( $value ) && ! is_numeric( $value ) ) {
			return '';
		}

		$value = sanitize_text_field( wp_unslash( (string) $value ) );
		$value = preg_replace( '/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $value );
		$value = is_string( $value ) ? trim( $value ) : '';

		if ( function_exists( 'mb_substr' ) ) {
			return mb_substr( $value, 0, $max, 'UTF-8' );
		}

		return substr( $value, 0, $max );
	}

	/**
	 * @param string $ip Client IP.
	 * @return bool
	 */
	private static function check_rate_limit( $ip ) {
		$key   = 'fp02_lead_rl_' . md5( $ip );
		$count = (int) get_transient( $key );
		return $count < self::RATE_LIMIT_MAX;
	}

	/**
	 * @param string $ip Client IP.
	 */
	private static function bump_rate_limit( $ip ) {
		$key   = 'fp02_lead_rl_' . md5( $ip );
		$count = (int) get_transient( $key );
		set_transient( $key, $count + 1, self::RATE_LIMIT_WINDOW );
	}

	/**
	 * Claim one-time request token via transient.
	 *
	 * @param string $token Token.
	 * @return bool True if newly claimed.
	 */
	private static function claim_request_token( $token ) {
		$key = 'fp02_lead_tok_' . hash( 'sha256', $token );
		if ( false !== get_transient( $key ) ) {
			return false;
		}
		set_transient( $key, 1, self::DUPLICATE_TOKEN_TTL );
		return true;
	}

	/**
	 * @return string
	 */
	private static function client_ip() {
		$candidates = array(
			isset( $_SERVER['HTTP_CF_CONNECTING_IP'] ) ? $_SERVER['HTTP_CF_CONNECTING_IP'] : null,
			isset( $_SERVER['HTTP_X_FORWARDED_FOR'] ) ? $_SERVER['HTTP_X_FORWARDED_FOR'] : null,
			isset( $_SERVER['REMOTE_ADDR'] ) ? $_SERVER['REMOTE_ADDR'] : null,
		);

		foreach ( $candidates as $candidate ) {
			if ( ! is_string( $candidate ) || '' === $candidate ) {
				continue;
			}
			$parts = explode( ',', $candidate );
			$ip    = trim( $parts[0] );
			if ( filter_var( $ip, FILTER_VALIDATE_IP ) ) {
				return $ip;
			}
		}

		return '0.0.0.0';
	}

	/**
	 * Write redacted local receipt under uploads (not in git).
	 *
	 * @param array<string,mixed> $receipt Receipt payload.
	 */
	private static function write_local_receipt( array $receipt ) {
		$uploads = wp_upload_dir();
		if ( ! empty( $uploads['error'] ) || empty( $uploads['basedir'] ) ) {
			error_log( '[fp02-lead-local] accepted mode=local mail=disabled (uploads unavailable)' ); // phpcs:ignore WordPress.PHP.DevelopmentFunctions.error_log_error_log
			return;
		}

		$dir = trailingslashit( $uploads['basedir'] ) . 'fp02-leads-local';
		if ( ! is_dir( $dir ) ) {
			wp_mkdir_p( $dir );
		}

		$htaccess = $dir . '/.htaccess';
		if ( ! file_exists( $htaccess ) ) {
			file_put_contents( $htaccess, "Require all denied\nDeny from all\n" );
		}

		$index = $dir . '/index.php';
		if ( ! file_exists( $index ) ) {
			file_put_contents( $index, "<?php\n// Silence is golden.\n" );
		}

		$file = $dir . '/receipt-' . gmdate( 'Ymd-His' ) . '-' . wp_generate_password( 6, false, false ) . '.json';
		file_put_contents( $file, wp_json_encode( $receipt, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );

		error_log( // phpcs:ignore WordPress.PHP.DevelopmentFunctions.error_log_error_log
			sprintf(
				'[fp02-lead-local] accepted context=%s source=%s mail=disabled',
				$receipt['form_context'],
				$receipt['lead_source']
			)
		);
	}

	/**
	 * @param string $name Name.
	 * @return string
	 */
	private static function redact_name( $name ) {
		$len = function_exists( 'mb_strlen' ) ? mb_strlen( $name, 'UTF-8' ) : strlen( $name );
		if ( $len <= 1 ) {
			return '*';
		}
		$first = function_exists( 'mb_substr' ) ? mb_substr( $name, 0, 1, 'UTF-8' ) : substr( $name, 0, 1 );
		return $first . str_repeat( '*', min( 8, $len - 1 ) );
	}

	/**
	 * @param string $phone Phone.
	 * @return string
	 */
	private static function redact_phone( $phone ) {
		$digits = preg_replace( '/\D+/', '', $phone );
		$digits = is_string( $digits ) ? $digits : '';
		if ( strlen( $digits ) < 4 ) {
			return '****';
		}
		return str_repeat( '*', max( 0, strlen( $digits ) - 4 ) ) . substr( $digits, -4 );
	}

	/**
	 * @param string $email Email.
	 * @return string
	 */
	private static function redact_email( $email ) {
		$parts = explode( '@', $email, 2 );
		if ( 2 !== count( $parts ) ) {
			return '***';
		}
		$local = $parts[0];
		$first = function_exists( 'mb_substr' ) ? mb_substr( $local, 0, 1, 'UTF-8' ) : substr( $local, 0, 1 );
		return $first . '***@' . $parts[1];
	}

	/**
	 * Persist lead before mail.
	 *
	 * @param array<string, string> $payload Payload.
	 * @return int
	 */
	private static function persist_lead( array $payload ) {
		$source = self::source_from_url( $payload['page_url'] );
		$ua     = isset( $_SERVER['HTTP_USER_AGENT'] ) ? (string) $_SERVER['HTTP_USER_AGENT'] : '';

		return LeadRegistry::insert(
			array(
				'form_key'        => LeadRegistry::FORM_KEY,
				'form_context'    => $payload['form_context'],
				'source_url'      => $payload['page_url'],
				'source_path'     => $source['path'],
				'source_post_id'  => $source['post_id'],
				'visitor_name'    => $payload['name'],
				'phone'           => $payload['phone'],
				'email'           => $payload['email'],
				'message'         => $payload['message'],
				'delivery_status' => LeadRegistry::STATUS_RECEIVED,
				'metrika_goal'    => MailOps::metrika_goal(),
				'utm_source'      => $payload['utm_source'],
				'utm_medium'      => $payload['utm_medium'],
				'utm_campaign'    => $payload['utm_campaign'],
				'utm_content'     => $payload['utm_content'],
				'utm_term'        => $payload['utm_term'],
				'referrer'        => $payload['referrer'],
				'ua_class'        => LeadRegistry::ua_class_from( $ua ),
				'is_qa'           => ! empty( $payload['is_qa'] ),
			)
		);
	}

	/**
	 * Attempt wp_mail after persist. Never throws to the visitor.
	 *
	 * @param array<string, string> $payload Payload.
	 * @param int                   $lead_id Lead ID.
	 * @return array{attempted:bool,accepted:bool,status:string}
	 */
	private static function attempt_outbound_mail( array $payload, $lead_id ) {
		if ( MailOps::should_suppress() ) {
			$status = MailOps::is_complete()
				? LeadRegistry::STATUS_SMTP_PENDING
				: LeadRegistry::STATUS_MAIL_SUPPRESSED;
			LeadRegistry::update_delivery(
				$lead_id,
				array(
					'delivery_status' => $status,
					'smtp_status'     => 'suppressed',
					'attempt_count'   => 0,
				)
			);
			return array(
				'attempted' => false,
				'accepted'  => false,
				'status'    => $status,
			);
		}

		if ( ! MailOps::should_attempt_mail() ) {
			LeadRegistry::update_delivery(
				$lead_id,
				array(
					'delivery_status' => LeadRegistry::STATUS_SMTP_PENDING,
					'smtp_status'     => 'pending',
					'attempt_count'   => 0,
				)
			);
			return array(
				'attempted' => false,
				'accepted'  => false,
				'status'    => LeadRegistry::STATUS_SMTP_PENDING,
			);
		}

		$to = MailOps::recipient_emails();
		if ( empty( $to ) ) {
			LeadRegistry::update_delivery(
				$lead_id,
				array(
					'delivery_status' => LeadRegistry::STATUS_MAIL_ERROR,
					'smtp_status'     => 'no_recipient',
					'error_code'      => 'no_recipient',
					'attempt_count'   => 1,
				)
			);
			return array(
				'attempted' => true,
				'accepted'  => false,
				'status'    => LeadRegistry::STATUS_MAIL_ERROR,
			);
		}

		$subject = sprintf(
			'[%s] %s',
			MailOps::from_name(),
			__( 'Заявка с сайта', 'shpigovsky-core' )
		);
		$body    = self::build_mail_body( $payload );
		$headers = array(
			'Content-Type: text/plain; charset=UTF-8',
			'From: ' . MailOps::from_name() . ' <' . MailOps::from_email() . '>',
		);
		if ( '' !== $payload['email'] && is_email( $payload['email'] ) ) {
			$headers[] = 'Reply-To: ' . $payload['email'];
		}

		$sent = wp_mail( $to, $subject, $body, $headers );
		if ( $sent ) {
			LeadRegistry::update_delivery(
				$lead_id,
				array(
					'delivery_status' => LeadRegistry::STATUS_MAIL_ACCEPTED,
					'smtp_status'     => 'accepted',
					'attempt_count'   => 1,
				)
			);
			return array(
				'attempted' => true,
				'accepted'  => true,
				'status'    => LeadRegistry::STATUS_MAIL_ACCEPTED,
			);
		}

		global $phpmailer;
		$raw = ( is_object( $phpmailer ) && ! empty( $phpmailer->ErrorInfo ) ) ? (string) $phpmailer->ErrorInfo : 'send_failed';
		$cat = MailOps::sanitize_error_category( $raw );
		LeadRegistry::update_delivery(
			$lead_id,
			array(
				'delivery_status' => LeadRegistry::STATUS_MAIL_ERROR,
				'smtp_status'     => 'error',
				'error_code'      => $cat,
				'attempt_count'   => 1,
			)
		);
		return array(
			'attempted' => true,
			'accepted'  => false,
			'status'    => LeadRegistry::STATUS_MAIL_ERROR,
		);
	}

	/**
	 * @param array<string, string> $payload Payload.
	 * @return string
	 */
	private static function build_mail_body( array $payload ) {
		$lines = array(
			'Форма: consultation',
			'Имя: ' . $payload['name'],
			'Телефон: ' . $payload['phone'],
			'Email: ' . ( $payload['email'] !== '' ? $payload['email'] : '—' ),
			'Страница: ' . $payload['page_url'],
			'Сообщение:',
			$payload['message'],
		);
		return implode( "\n", $lines );
	}

	/**
	 * @param string $url Page URL.
	 * @return array{path:string,post_id:int}
	 */
	private static function source_from_url( $url ) {
		$path = '';
		$parsed = wp_parse_url( $url );
		if ( is_array( $parsed ) && ! empty( $parsed['path'] ) ) {
			$path = (string) $parsed['path'];
		}
		$post_id = 0;
		$url_id  = $url ? url_to_postid( $url ) : 0;
		if ( $url_id > 0 ) {
			$post_id = (int) $url_id;
		}
		return array(
			'path'    => $path,
			'post_id' => $post_id,
		);
	}

	/**
	 * @param bool               $ok Success.
	 * @param string             $message User message.
	 * @param int                $status HTTP status.
	 * @param array<string,mixed> $extra Extra fields.
	 */
	private static function json_response( $ok, $message, $status = 200, array $extra = array() ) {
		status_header( $status );
		wp_send_json(
			array_merge(
				array(
					'ok'      => (bool) $ok,
					'success' => (bool) $ok,
					'message' => $message,
				),
				$extra
			),
			$status
		);
	}
}

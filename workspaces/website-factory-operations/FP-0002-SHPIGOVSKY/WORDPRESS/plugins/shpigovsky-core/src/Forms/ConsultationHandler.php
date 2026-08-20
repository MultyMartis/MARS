<?php
/**
 * Lead form AJAX handler — anti-spam first, persist, then optional wp_mail.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Forms;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Leads\LeadRegistry;
use Shpigovsky\Core\Mail\FormLeadMailPresenter;
use Shpigovsky\Core\Mail\MailOps;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Unified lead / consultation form submission handler (wp_ajax).
 *
 * Validate → anti-spam → persist lead → attempt mail → JSON.
 * Frontend success means the lead was stored, not that email was delivered.
 * Spam is rejected before real lead persistence.
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
	 * Localize endpoint / nonce / signed token / messages onto theme shell script.
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
				'formSessionField'       => AntiSpam::TOKEN_FIELD,
				'formSession'            => AntiSpam::issue_token( LeadRegistry::FORM_KEY, '' ),
				'phoneMask'              => '+7 999 999 - 99 - 99',
				'siteConfigEndpoint'     => '',
				'backendBlockedMessage'  => self::message( 'backend_blocked' ),
				'validationErrorMessage' => self::message( 'validation' ),
				'successMessage'         => self::message( 'local_success' ),
				'rateLimitedMessage'     => AntiSpam::visitor_message( AntiSpam::REASON_RATE ),
				'duplicateMessage'       => self::message( 'duplicate' ),
				'formKey'                => LeadRegistry::FORM_KEY,
				'metrikaCounter'         => MailOps::metrika_counter_id(),
				'metrikaGoal'            => MailOps::metrika_goal(),
				'messages'               => array(
					'local_success'   => self::message( 'local_success' ),
					'validation'      => self::message( 'validation' ),
					'rate_limited'    => AntiSpam::visitor_message( AntiSpam::REASON_RATE ),
					'duplicate'       => self::message( 'duplicate' ),
					'stale'           => AntiSpam::visitor_message( AntiSpam::REASON_TOKEN_EXP ),
					'server_error'    => self::message( 'server_error' ),
					'backend_blocked' => self::message( 'backend_blocked' ),
					'antispam'        => AntiSpam::visitor_message( AntiSpam::REASON_TOKEN_BAD ),
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

		// Anti-spam layers (honeypot / signed timing / rate) before persistence.
		$spam_early = AntiSpam::evaluate( $_POST, array() );
		if ( ! $spam_early['ok'] ) {
			self::json_response( false, $spam_early['message'], 422 );
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

		$spam_payload = AntiSpam::evaluate( $_POST, $payload );
		if ( ! $spam_payload['ok'] ) {
			self::json_response( false, $spam_payload['message'], 422 );
		}

		$lead_id = self::persist_lead( $payload );
		if ( $lead_id <= 0 ) {
			self::json_response( false, self::message( 'server_error' ), 500 );
		}

		AntiSpam::bump_attempt();

		$mail = self::attempt_outbound_mail( $payload, $lead_id );

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
			'duplicate'       => 'Эта заявка уже была отправлена. Обновите страницу, если нужно отправить новую.',
			'nonce'           => 'Сессия безопасности устарела. Обновите страницу и попробуйте снова.',
			'method'          => 'Метод не поддерживается.',
			'server_error'    => 'Не удалось принять заявку. Позвоните нам: 8 (925) 183-64-64.',
			'backend_blocked' => 'Отправка заявки пока недоступна. Позвоните нам по телефону 8 (925) 183-64-64.',
		);

		return isset( $messages[ $key ] ) ? $messages[ $key ] : $messages['server_error'];
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

		// One lead already persisted. One wp_mail() with the full recipient array.
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

		$mail_pack = FormLeadMailPresenter::build( LeadRegistry::FORM_KEY, $payload );
		$subject   = $mail_pack['subject'];
		$body      = $mail_pack['html'];
		$headers   = $mail_pack['headers'];

		$alt_body_setter = static function ( $phpmailer ) use ( $mail_pack ) {
			if ( is_object( $phpmailer ) && method_exists( $phpmailer, 'isHTML' ) ) {
				$phpmailer->isHTML( true );
			}
			if ( is_object( $phpmailer ) && property_exists( $phpmailer, 'AltBody' ) ) {
				$phpmailer->AltBody = $mail_pack['plain'];
			}
		};
		add_action( 'phpmailer_init', $alt_body_setter, 20, 1 );

		$sent = wp_mail( $to, $subject, $body, $headers );

		remove_action( 'phpmailer_init', $alt_body_setter, 20 );
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

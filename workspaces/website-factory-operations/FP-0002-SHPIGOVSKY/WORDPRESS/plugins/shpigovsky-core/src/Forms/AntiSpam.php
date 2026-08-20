<?php
/**
 * First-party layered form anti-spam — server authoritative.
 *
 * Layers: honeypot, signed timing token, replay (caller), rate limit, heuristics.
 * No external CAPTCHA providers.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Forms;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Native anti-spam evaluation for public lead forms.
 */
final class AntiSpam {

	public const HONEYPOT_FIELD = 'company_url';
	public const TOKEN_FIELD    = 'fp02_fs';

	public const REASON_HONEYPOT   = 'HONEYPOT_FILLED';
	public const REASON_TOO_FAST   = 'TIMING_TOO_FAST';
	public const REASON_TOKEN_BAD  = 'TOKEN_INVALID';
	public const REASON_TOKEN_EXP  = 'TOKEN_EXPIRED';
	public const REASON_RATE       = 'RATE_LIMIT';
	public const REASON_PAYLOAD    = 'PAYLOAD_STRONG_SPAM_SIGNAL';
	public const REASON_PASS       = 'PASS';

	/** Minimum human interaction (seconds). */
	public const MIN_ELAPSED = 2;

	/** Maximum signed token age (seconds) — 2 hours. */
	public const MAX_AGE = 7200;

	/** Short rate window. */
	public const RATE_SHORT_WINDOW = 60;
	public const RATE_SHORT_MAX    = 6;

	/** Medium rate window. */
	public const RATE_MED_WINDOW = 1200;
	public const RATE_MED_MAX    = 20;

	/** Counter option (no PII). */
	public const COUNTERS_OPTION = 'fp02_antispam_counters_v1';

	/**
	 * Issue a server-signed form-start token.
	 *
	 * @param string $form_type Machine form key.
	 * @param string $form_context Optional context (final|modal|…).
	 * @return string
	 */
	public static function issue_token( $form_type = 'consultation', $form_context = '' ) {
		$payload = array(
			'iat' => time(),
			'ft'  => sanitize_key( (string) $form_type ),
			'fc'  => sanitize_key( (string) $form_context ),
			'n'   => wp_generate_password( 12, false, false ),
		);
		$body = self::b64url( wp_json_encode( $payload ) );
		$sig  = self::b64url( hash_hmac( 'sha256', $body, self::signing_key(), true ) );
		return $body . '.' . $sig;
	}

	/**
	 * Evaluate anti-spam layers (except request_token idempotency — owned by handler).
	 *
	 * @param array<string,mixed> $input Raw POST.
	 * @param array<string,string> $payload Sanitized business fields (may be empty before sanitize).
	 * @return array{ok:bool,reason:string,message:string}
	 */
	public static function evaluate( array $input, array $payload = array() ) {
		// When payload is provided, run heuristics only (early layers already passed).
		if ( ! empty( $payload ) ) {
			$heur = self::payload_heuristics( $payload );
			if ( ! $heur['ok'] ) {
				self::record_reject( self::REASON_PAYLOAD, $input );
				return self::reject( self::REASON_PAYLOAD );
			}
			return array(
				'ok'      => true,
				'reason'  => self::REASON_PASS,
				'message' => '',
			);
		}

		$honey = isset( $input[ self::HONEYPOT_FIELD ] )
			? trim( (string) wp_unslash( $input[ self::HONEYPOT_FIELD ] ) )
			: '';
		if ( '' !== $honey ) {
			self::record_reject( self::REASON_HONEYPOT, $input );
			return self::reject( self::REASON_HONEYPOT );
		}

		$timing = self::verify_signed_timing( $input );
		if ( ! $timing['ok'] ) {
			self::record_reject( $timing['reason'], $input );
			return self::reject( $timing['reason'] );
		}

		$rate = self::check_rate_limit();
		if ( ! $rate['ok'] ) {
			self::record_reject( self::REASON_RATE, $input );
			return self::reject( self::REASON_RATE );
		}

		return array(
			'ok'      => true,
			'reason'  => self::REASON_PASS,
			'message' => '',
		);
	}

	/**
	 * Bump rate counters after an attempt (accepted or rejected spam/abuse).
	 * Validation/nonce failures should not always bump — caller decides.
	 */
	public static function bump_attempt() {
		$fp = self::source_fingerprint();
		self::bump_bucket( 's_' . $fp, self::RATE_SHORT_WINDOW );
		self::bump_bucket( 'm_' . $fp, self::RATE_MED_WINDOW );
	}

	/**
	 * Clear transient rate buckets for the current request source (QA / ops only).
	 */
	public static function clear_rate_state_for_current_source() {
		$fp = self::source_fingerprint();
		delete_transient( 'fp02_as_s_' . $fp );
		delete_transient( 'fp02_as_m_' . $fp );
	}

	/**
	 * Human-readable admin status block data.
	 *
	 * @return array{active:bool,layers:array<int,string>,rejected_24h:int,rejected_7d:int}
	 */
	public static function admin_status() {
		$counters = self::read_counters();
		$now      = time();
		$d24      = 0;
		$d7       = 0;
		foreach ( $counters['days'] as $day => $row ) {
			$ts = strtotime( $day . ' UTC' );
			if ( false === $ts ) {
				continue;
			}
			$total = (int) ( $row['total'] ?? 0 );
			if ( ( $now - $ts ) <= 86400 ) {
				$d24 += $total;
			}
			if ( ( $now - $ts ) <= 604800 ) {
				$d7 += $total;
			}
		}

		return array(
			'active'       => true,
			'layers'       => array(
				'скрытая проверка формы',
				'защита от слишком быстрых отправок',
				'ограничение частоты',
				'защита от повторов',
			),
			'rejected_24h' => $d24,
			'rejected_7d'  => $d7,
		);
	}

	/**
	 * Neutral visitor message (no reason leakage).
	 *
	 * @param string $reason Internal reason.
	 * @return string
	 */
	public static function visitor_message( $reason ) {
		if ( self::REASON_RATE === $reason ) {
			return 'Не удалось подтвердить отправку. Попробуйте ещё раз через несколько секунд.';
		}
		if ( self::REASON_TOKEN_EXP === $reason || self::REASON_TOO_FAST === $reason ) {
			return 'Не удалось отправить форму. Обновите страницу и попробуйте ещё раз.';
		}
		return 'Не удалось отправить форму. Обновите страницу и попробуйте ещё раз.';
	}

	/**
	 * @param array<string,mixed> $input Raw POST.
	 * @return array{ok:bool,reason:string}
	 */
	private static function verify_signed_timing( array $input ) {
		$token = isset( $input[ self::TOKEN_FIELD ] )
			? sanitize_text_field( wp_unslash( (string) $input[ self::TOKEN_FIELD ] ) )
			: '';

		if ( '' === $token || false === strpos( $token, '.' ) ) {
			return array( 'ok' => false, 'reason' => self::REASON_TOKEN_BAD );
		}

		$parts = explode( '.', $token, 2 );
		if ( 2 !== count( $parts ) || '' === $parts[0] || '' === $parts[1] ) {
			return array( 'ok' => false, 'reason' => self::REASON_TOKEN_BAD );
		}

		list( $body, $sig ) = $parts;
		$expected = self::b64url( hash_hmac( 'sha256', $body, self::signing_key(), true ) );
		if ( ! hash_equals( $expected, $sig ) ) {
			return array( 'ok' => false, 'reason' => self::REASON_TOKEN_BAD );
		}

		$json = self::b64url_decode( $body );
		$data = is_string( $json ) ? json_decode( $json, true ) : null;
		if ( ! is_array( $data ) || empty( $data['iat'] ) ) {
			return array( 'ok' => false, 'reason' => self::REASON_TOKEN_BAD );
		}

		$iat = (int) $data['iat'];
		$now = time();
		$age = $now - $iat;

		if ( $age < 0 || $age > self::MAX_AGE ) {
			return array( 'ok' => false, 'reason' => self::REASON_TOKEN_EXP );
		}

		$form_type = isset( $data['ft'] ) ? sanitize_key( (string) $data['ft'] ) : '';
		if ( 'consultation' !== $form_type && '' !== $form_type ) {
			// Only consultation exists today; reject unexpected types.
			return array( 'ok' => false, 'reason' => self::REASON_TOKEN_BAD );
		}

		if ( $age < self::MIN_ELAPSED ) {
			return array( 'ok' => false, 'reason' => self::REASON_TOO_FAST );
		}

		return array( 'ok' => true, 'reason' => self::REASON_PASS );
	}

	/**
	 * @return array{ok:bool}
	 */
	private static function check_rate_limit() {
		$fp = self::source_fingerprint();
		$s  = (int) get_transient( 'fp02_as_s_' . $fp );
		$m  = (int) get_transient( 'fp02_as_m_' . $fp );
		if ( $s >= self::RATE_SHORT_MAX || $m >= self::RATE_MED_MAX ) {
			return array( 'ok' => false );
		}
		return array( 'ok' => true );
	}

	/**
	 * Conservative payload heuristics — strong signals only.
	 *
	 * @param array<string,string> $payload Sanitized fields.
	 * @return array{ok:bool,score:int}
	 */
	private static function payload_heuristics( array $payload ) {
		$score   = 0;
		$message = isset( $payload['message'] ) ? (string) $payload['message'] : '';
		$name    = isset( $payload['name'] ) ? (string) $payload['name'] : '';

		$len = function_exists( 'mb_strlen' ) ? mb_strlen( $message, 'UTF-8' ) : strlen( $message );
		if ( $len > 3500 ) {
			$score += 5;
		}

		$url_count = preg_match_all( '#https?://#iu', $message );
		$url_count = is_int( $url_count ) ? $url_count : 0;
		if ( $url_count >= 4 ) {
			$score += 5;
		} elseif ( $url_count >= 3 ) {
			$score += 3;
		}

		if ( preg_match( '/(<script|javascript:|onerror\s*=|<\s*iframe)/iu', $message ) ) {
			$score += 5;
		}

		if ( preg_match( '/(.)\1{20,}/u', $message ) ) {
			$score += 3;
		}

		$newlines = substr_count( $message, "\n" );
		if ( $len < 80 && $newlines >= 12 && $url_count >= 2 ) {
			$score += 3;
		}

		// Same URL repeated many times.
		if ( $url_count >= 2 && preg_match( '#(https?://[^\s]+).*?\1#isu', $message ) ) {
			$score += 2;
		}

		// Name looking like a URL dump.
		if ( preg_match( '#https?://#iu', $name ) ) {
			$score += 4;
		}

		// Threshold: prefer OBSERVE for weak; REJECT only strong.
		if ( $score >= 5 ) {
			return array( 'ok' => false, 'score' => $score );
		}

		return array( 'ok' => true, 'score' => $score );
	}

	/**
	 * @param string $reason Reason.
	 * @return array{ok:bool,reason:string,message:string}
	 */
	private static function reject( $reason ) {
		return array(
			'ok'      => false,
			'reason'  => $reason,
			'message' => self::visitor_message( $reason ),
		);
	}

	/**
	 * @param string               $reason Reason.
	 * @param array<string,mixed>  $input Input (unused beyond form type).
	 */
	private static function record_reject( $reason, array $input ) {
		self::bump_attempt();

		$form_type = 'consultation';
		$day       = gmdate( 'Y-m-d' );
		$counters  = self::read_counters();
		if ( ! isset( $counters['days'][ $day ] ) || ! is_array( $counters['days'][ $day ] ) ) {
			$counters['days'][ $day ] = array( 'total' => 0, 'by_reason' => array() );
		}
		$counters['days'][ $day ]['total'] = (int) $counters['days'][ $day ]['total'] + 1;
		$prev = (int) ( $counters['days'][ $day ]['by_reason'][ $reason ] ?? 0 );
		$counters['days'][ $day ]['by_reason'][ $reason ] = $prev + 1;

		// Keep ~14 days.
		foreach ( array_keys( $counters['days'] ) as $d ) {
			$ts = strtotime( $d . ' UTC' );
			if ( false !== $ts && ( time() - $ts ) > 14 * DAY_IN_SECONDS ) {
				unset( $counters['days'][ $d ] );
			}
		}
		update_option( self::COUNTERS_OPTION, $counters, false );

		if ( class_exists( '\\Shpigovsky\\Core\\Admin\\ActivityLog' ) ) {
			$label = sanitize_key( $reason ) . ' · ' . sanitize_key( $form_type );
			\Shpigovsky\Core\Admin\ActivityLog::log_system_event(
				'form_spam_rejected',
				'form',
				$label,
				0,
				'antispam',
				0
			);
		}

		error_log( // phpcs:ignore WordPress.PHP.DevelopmentFunctions.error_log_error_log
			sprintf( '[fp02-antispam] reject reason=%s form=%s', sanitize_key( $reason ), $form_type )
		);
	}

	/**
	 * @return array{days:array<string,array{total:int,by_reason:array<string,int>}>}
	 */
	private static function read_counters() {
		$raw = get_option( self::COUNTERS_OPTION, array() );
		if ( ! is_array( $raw ) || ! isset( $raw['days'] ) || ! is_array( $raw['days'] ) ) {
			return array( 'days' => array() );
		}
		return array( 'days' => $raw['days'] );
	}

	/**
	 * Transient source fingerprint — salted hash, short TTL only.
	 *
	 * @return string
	 */
	private static function source_fingerprint() {
		$ip = self::client_ip_raw();
		return substr( hash_hmac( 'sha256', $ip, self::signing_key() ), 0, 32 );
	}

	/**
	 * @return string
	 */
	private static function client_ip_raw() {
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
	 * @param string $suffix Bucket suffix already including fingerprint.
	 * @param int    $ttl TTL.
	 */
	private static function bump_bucket( $suffix, $ttl ) {
		$key   = 'fp02_as_' . $suffix;
		$count = (int) get_transient( $key );
		set_transient( $key, $count + 1, $ttl );
	}

	/**
	 * @return string
	 */
	private static function signing_key() {
		if ( defined( 'AUTH_KEY' ) && is_string( AUTH_KEY ) && '' !== AUTH_KEY ) {
			return AUTH_KEY . '|fp02-form-antispam-v1';
		}
		return wp_salt( 'auth' ) . '|fp02-form-antispam-v1';
	}

	/**
	 * @param string $bin Binary or string.
	 * @return string
	 */
	private static function b64url( $bin ) {
		return rtrim( strtr( base64_encode( $bin ), '+/', '-_' ), '=' );
	}

	/**
	 * @param string $data Encoded.
	 * @return string|false
	 */
	private static function b64url_decode( $data ) {
		$remainder = strlen( $data ) % 4;
		if ( $remainder ) {
			$data .= str_repeat( '=', 4 - $remainder );
		}
		return base64_decode( strtr( $data, '-_', '+/' ), true );
	}
}

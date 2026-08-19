<?php
/**
 * Critical administrator alerts for indexing state changes — PROD-P18G.
 *
 * Recipients: WordPress administrators only — never form lead recipients.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Email alerts with deduplication for indexing safety events.
 */
final class IndexingAlerts {

	const DEDUPE_OPTION = 'fp02_indexing_alert_dedupe';

	/**
	 * Resolve administrator email recipients.
	 *
	 * @return array<int, string>
	 */
	public static function admin_recipient_emails() {
		$emails = array();

		$admin_email = sanitize_email( (string) get_option( 'admin_email' ) );
		if ( is_email( $admin_email ) ) {
			$emails[] = $admin_email;
		}

		$admins = get_users(
			array(
				'role'   => 'administrator',
				'fields' => array( 'user_email' ),
			)
		);

		foreach ( $admins as $admin ) {
			$addr = sanitize_email( (string) $admin->user_email );
			if ( is_email( $addr ) ) {
				$emails[] = $addr;
			}
		}

		$unique = array();
		foreach ( $emails as $email ) {
			$key = strtolower( $email );
			if ( ! isset( $unique[ $key ] ) ) {
				$unique[ $key ] = $email;
			}
		}

		return array_values( $unique );
	}

	/**
	 * Send critical closed/blocked alert.
	 *
	 * @param array<string, mixed> $context Event context.
	 * @return array{sent:bool,recipients:int,error?:string,deduped?:bool}
	 */
	public static function send_critical_blocked_alert( array $context ) {
		$snap = IndexingState::snapshot();
		$fp   = isset( $context['fingerprint'] ) ? (string) $context['fingerprint'] : $snap['fingerprint'];

		if ( self::is_deduped( 'blocked', $fp ) ) {
			return array(
				'sent'        => false,
				'recipients'  => 0,
				'deduped'     => true,
			);
		}

		$host = wp_parse_url( home_url( '/' ), PHP_URL_HOST );
		$host = is_string( $host ) ? $host : 'site';

		$subject = sprintf(
			/* translators: %s: site host */
			__( '⚠️ ВНИМАНИЕ: обнаружена блокировка индексации %s', 'shpigovsky-core' ),
			$host
		);

		if ( IndexingState::STATE_CLOSED === $snap['effective'] && IndexingState::STATE_OPEN === strtoupper( (string) ( $context['previous_effective'] ?? '' ) ) ) {
			$subject = sprintf(
				/* translators: %s: site host */
				__( '⚠️ ВНИМАНИЕ: %s закрыт от индексации', 'shpigovsky-core' ),
				$host
			);
		}

		$body = self::build_blocked_body( $context, $snap );
		$result = self::dispatch( $subject, $body, 'critical_blocked' );

		if ( $result['sent'] ) {
			self::mark_deduped( 'blocked', $fp );
			self::log_alert_event( 'indexing_alert_sent', $subject, $context );
		} else {
			self::log_alert_event( 'indexing_alert_error', $subject, array_merge( $context, array( 'error' => $result['error'] ?? 'unknown' ) ) );
		}

		return $result;
	}

	/**
	 * Send recovery alert when OPEN is restored.
	 *
	 * @param array<string, mixed> $context Event context.
	 * @return array{sent:bool,recipients:int,error?:string,deduped?:bool}
	 */
	public static function send_recovery_alert( array $context ) {
		$snap = IndexingState::snapshot();
		$fp   = 'recovery:' . $snap['fingerprint'];

		if ( self::is_deduped( 'recovery', $fp ) ) {
			return array(
				'sent'       => false,
				'recipients' => 0,
				'deduped'    => true,
			);
		}

		$host = wp_parse_url( home_url( '/' ), PHP_URL_HOST );
		$host = is_string( $host ) ? $host : 'site';

		$subject = sprintf(
			/* translators: %s: site host */
			__( '✅ Индексация %s восстановлена', 'shpigovsky-core' ),
			$host
		);

		$lines   = array();
		$lines[] = sprintf( __( 'Сайт: %s', 'shpigovsky-core' ), home_url( '/' ) );
		$lines[] = sprintf( __( 'Время обнаружения: %s', 'shpigovsky-core' ), current_time( 'mysql' ) );
		if ( ! empty( $context['prior_issue'] ) ) {
			$lines[] = sprintf( __( 'Предыдущая проблема: %s', 'shpigovsky-core' ), (string) $context['prior_issue'] );
		}
		$lines[] = sprintf( 'blog_public=%d', (int) $snap['blog_public'] );
		$lines[] = sprintf(
			__( 'robots: %s', 'shpigovsky-core' ),
			! empty( $snap['robots']['global_disallow'] ) ? 'Disallow: /' : __( 'без глобального Disallow', 'shpigovsky-core' )
		);
		$lines[] = sprintf(
			__( 'meta robots: %s', 'shpigovsky-core' ),
			! empty( $snap['meta']['global_noindex'] ) ? 'noindex (глобально)' : __( 'без глобального noindex', 'shpigovsky-core' )
		);
		$lines[] = '';
		$lines[] = __( 'Панель управления:', 'shpigovsky-core' ) . ' ' . admin_url( 'index.php' );

		$result = self::dispatch( $subject, implode( "\n", $lines ), 'recovery' );

		if ( $result['sent'] ) {
			self::mark_deduped( 'recovery', $fp );
			self::log_alert_event( 'indexing_recovered', $subject, $context );
		}

		return $result;
	}

	/**
	 * Synthetic test alert — does not mutate indexing.
	 *
	 * @return array{sent:bool,recipients:int,error?:string}
	 */
	public static function send_test_alert() {
		$host = wp_parse_url( home_url( '/' ), PHP_URL_HOST );
		$host = is_string( $host ) ? $host : 'site';

		$subject = 'TEST — INDEXING SAFETY ALERT — ' . $host;
		$body    = __( 'Тестовое письмо системы безопасности индексации. Состояние индексации не изменялось.', 'shpigovsky-core' ) . "\n\n"
			. __( 'Если вы получили это письмо, канал оповещения администраторов работает.', 'shpigovsky-core' ) . "\n"
			. current_time( 'mysql' );

		return self::dispatch( $subject, $body, 'test' );
	}

	/**
	 * @param string $kind Alert kind.
	 * @param string $fingerprint Fingerprint.
	 * @return bool
	 */
	private static function is_deduped( $kind, $fingerprint ) {
		$raw = get_option( self::DEDUPE_OPTION, array() );
		if ( ! is_array( $raw ) ) {
			return false;
		}
		$key = sanitize_key( $kind ) . ':' . sanitize_text_field( $fingerprint );
		if ( empty( $raw[ $key ]['at'] ) ) {
			return false;
		}
		$at = strtotime( (string) $raw[ $key ]['at'] );
		if ( ! $at ) {
			return false;
		}
		// 6h cool-down for same fingerprint.
		return ( time() - $at ) < ( 6 * HOUR_IN_SECONDS );
	}

	/**
	 * @param string $kind Alert kind.
	 * @param string $fingerprint Fingerprint.
	 */
	private static function mark_deduped( $kind, $fingerprint ) {
		$raw = get_option( self::DEDUPE_OPTION, array() );
		if ( ! is_array( $raw ) ) {
			$raw = array();
		}
		$key = sanitize_key( $kind ) . ':' . sanitize_text_field( $fingerprint );
		$raw[ $key ] = array(
			'at' => current_time( 'mysql' ),
		);
		// Bound size.
		if ( count( $raw ) > 40 ) {
			$raw = array_slice( $raw, -30, null, true );
		}
		update_option( self::DEDUPE_OPTION, $raw, false );
	}

	/**
	 * Clear dedupe when effective state meaningfully changes (called by watchdog on recovery).
	 */
	public static function clear_blocked_dedupe() {
		$raw = get_option( self::DEDUPE_OPTION, array() );
		if ( ! is_array( $raw ) ) {
			return;
		}
		foreach ( array_keys( $raw ) as $key ) {
			if ( 0 === strpos( (string) $key, 'blocked:' ) ) {
				unset( $raw[ $key ] );
			}
		}
		update_option( self::DEDUPE_OPTION, $raw, false );
	}

	/**
	 * @param array<string, mixed> $context Context.
	 * @param array<string, mixed> $snap Snapshot.
	 * @return string
	 */
	private static function build_blocked_body( array $context, array $snap ) {
		$lines   = array();
		$lines[] = sprintf( __( 'Сайт: %s', 'shpigovsky-core' ), home_url( '/' ) );
		$lines[] = sprintf( __( 'Время события: %s', 'shpigovsky-core' ), current_time( 'mysql' ) );
		if ( ! empty( $context['previous_effective'] ) ) {
			$lines[] = sprintf( __( 'Предыдущее состояние: %s', 'shpigovsky-core' ), (string) $context['previous_effective'] );
		}
		$lines[] = sprintf( __( 'Текущее состояние: %s', 'shpigovsky-core' ), (string) $snap['effective'] );
		if ( ! empty( $context['actor'] ) ) {
			$lines[] = sprintf( __( 'Инициатор: %s', 'shpigovsky-core' ), (string) $context['actor'] );
		}
		if ( ! empty( $context['source'] ) ) {
			$lines[] = sprintf( __( 'Источник: %s', 'shpigovsky-core' ), (string) $context['source'] );
		}
		$lines[] = sprintf( 'blog_public=%d', (int) $snap['blog_public'] );
		$lines[] = sprintf(
			__( 'robots: %s (владелец: %s)', 'shpigovsky-core' ),
			! empty( $snap['robots']['global_disallow'] ) ? 'Disallow: /' : __( 'без глобального Disallow', 'shpigovsky-core' ),
			(string) ( $snap['robots']['owner'] ?? 'unknown' )
		);
		$lines[] = sprintf(
			__( 'meta robots: %s', 'shpigovsky-core' ),
			! empty( $snap['meta']['global_noindex'] ) ? 'noindex (глобально)' : __( 'без глобального noindex', 'shpigovsky-core' )
		);
		$lines[] = '';
		$lines[] = __( 'Внимание: видимость сайта в поиске может быть ограничена.', 'shpigovsky-core' );
		$lines[] = '';
		$lines[] = __( 'Панель управления:', 'shpigovsky-core' ) . ' ' . admin_url( 'index.php' );
		$lines[] = __( 'Управление индексацией — виджет MetaCODE на главной странице админки.', 'shpigovsky-core' );

		return implode( "\n", $lines );
	}

	/**
	 * @param string $subject Subject.
	 * @param string $body Body.
	 * @param string $kind Kind for From name suffix.
	 * @return array{sent:bool,recipients:int,error?:string}
	 */
	private static function dispatch( $subject, $body, $kind ) {
		$recipients = self::admin_recipient_emails();
		if ( empty( $recipients ) ) {
			return array(
				'sent'       => false,
				'recipients' => 0,
				'error'      => 'no_admin_recipients',
			);
		}

		$headers = array( 'Content-Type: text/plain; charset=UTF-8' );
		$sent_any = false;
		$last_err = '';

		foreach ( $recipients as $to ) {
			$ok = wp_mail( $to, $subject, $body, $headers );
			if ( $ok ) {
				$sent_any = true;
			} else {
				$last_err = 'wp_mail_failed';
			}
		}

		return array(
			'sent'       => $sent_any,
			'recipients' => count( $recipients ),
			'error'      => $sent_any ? '' : $last_err,
		);
	}

	/**
	 * @param string               $action Action key.
	 * @param string               $subject Subject summary.
	 * @param array<string, mixed> $context Context.
	 */
	private static function log_alert_event( $action, $subject, array $context ) {
		if ( ! class_exists( ActivityLog::class ) ) {
			return;
		}
		$source = isset( $context['source'] ) ? (string) $context['source'] : 'indexing_alerts';
		ActivityLog::log_system_event(
			$action,
			'setting',
			mb_substr( $subject . ' · ' . $source, 0, 255 ),
			0,
			$source
		);
	}
}

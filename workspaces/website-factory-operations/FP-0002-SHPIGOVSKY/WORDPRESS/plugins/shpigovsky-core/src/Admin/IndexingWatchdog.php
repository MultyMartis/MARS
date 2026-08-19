<?php
/**
 * Hourly indexing watchdog — alert only, never auto-mutate — PROD-P18G.
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
 * Scheduled effective-state verification with administrator alerts.
 */
final class IndexingWatchdog implements ModuleInterface {

	const CRON_HOOK     = 'fp02_indexing_watchdog_check';
	const LAST_OPTION   = 'fp02_indexing_watchdog_last';
	const BASELINE_OPT  = 'fp02_indexing_watchdog_baseline';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.indexing-watchdog';
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
		add_action( self::CRON_HOOK, array( __CLASS__, 'run_check' ) );
		add_action( 'init', array( __CLASS__, 'ensure_schedule' ) );
	}

	/**
	 * Schedule hourly if missing.
	 */
	public static function ensure_schedule() {
		if ( wp_next_scheduled( self::CRON_HOOK ) ) {
			return;
		}
		wp_schedule_event( time() + 300, 'hourly', self::CRON_HOOK );
	}

	/**
	 * Watchdog entry point.
	 */
	public static function run_check() {
		$previous = get_option( self::LAST_OPTION, array() );
		if ( ! is_array( $previous ) ) {
			$previous = array();
		}

		$snap = IndexingState::snapshot();

		update_option(
			self::LAST_OPTION,
			array(
				'checked_at'  => current_time( 'mysql' ),
				'effective'   => $snap['effective'],
				'fingerprint' => $snap['fingerprint'],
				'blog_public' => $snap['blog_public'],
			),
			false
		);

		$baseline = get_option( self::BASELINE_OPT, array() );
		if ( ! is_array( $baseline ) || empty( $baseline['effective'] ) ) {
			update_option(
				self::BASELINE_OPT,
				array(
					'effective'   => $snap['effective'],
					'fingerprint' => $snap['fingerprint'],
					'set_at'      => current_time( 'mysql' ),
				),
				false
			);
			return;
		}

		$prev_effective = isset( $previous['effective'] ) ? (string) $previous['effective'] : (string) $baseline['effective'];

		// OPEN → CLOSED transition.
		if ( IndexingState::STATE_OPEN === $prev_effective && IndexingState::STATE_OPEN !== $snap['effective'] ) {
			if ( class_exists( ActivityLog::class ) ) {
				ActivityLog::log_system_event(
					'indexing_inconsistency_detected',
					'setting',
					sprintf(
						'Watchdog: %s → %s · blog_public=%d',
						$prev_effective,
						$snap['effective'],
						(int) $snap['blog_public']
					),
					0,
					'watchdog'
				);
			}
			if ( class_exists( IndexingAlerts::class ) ) {
				IndexingAlerts::send_critical_blocked_alert(
					array(
						'previous_effective' => $prev_effective,
						'source'             => 'watchdog',
						'actor'              => __( 'Плановая проверка (watchdog)', 'shpigovsky-core' ),
						'fingerprint'        => $snap['fingerprint'],
					)
				);
			}
			return;
		}

		// Human OPEN but globally blocked.
		if ( IndexingState::is_human_open_but_blocked() ) {
			if ( class_exists( ActivityLog::class ) ) {
				ActivityLog::log_system_event(
					'indexing_inconsistency_detected',
					'setting',
					'Watchdog: human OPEN но effective ' . $snap['effective'],
					0,
					'watchdog'
				);
			}
			if ( class_exists( IndexingAlerts::class ) ) {
				IndexingAlerts::send_critical_blocked_alert(
					array(
						'previous_effective' => IndexingState::STATE_OPEN,
						'source'             => 'watchdog_human_open_blocked',
						'actor'              => __( 'Плановая проверка (watchdog)', 'shpigovsky-core' ),
						'fingerprint'        => 'human_open:' . $snap['fingerprint'],
					)
				);
			}
			return;
		}

		// Recovery: was blocked/inconsistent, now OPEN.
		if ( IndexingState::STATE_OPEN === $snap['effective']
			&& in_array( $prev_effective, array( IndexingState::STATE_CLOSED, IndexingState::STATE_INCONSISTENT ), true ) ) {
			if ( class_exists( IndexingAlerts::class ) ) {
				IndexingAlerts::clear_blocked_dedupe();
				IndexingAlerts::send_recovery_alert(
					array(
						'prior_issue' => $prev_effective,
						'source'      => 'watchdog',
					)
				);
			}
			if ( class_exists( ActivityLog::class ) ) {
				ActivityLog::log_system_event(
					'indexing_recovered',
					'setting',
					'Watchdog: индексация восстановлена до OPEN',
					0,
					'watchdog'
				);
			}
		}

		// Refresh baseline when stable OPEN.
		if ( IndexingState::STATE_OPEN === $snap['effective'] ) {
			update_option(
				self::BASELINE_OPT,
				array(
					'effective'   => $snap['effective'],
					'fingerprint' => $snap['fingerprint'],
					'set_at'      => current_time( 'mysql' ),
				),
				false
			);
		}
	}

	/**
	 * Dashboard line for watchdog status.
	 *
	 * @return string
	 */
	public static function dashboard_line() {
		$last = get_option( self::LAST_OPTION, array() );
		if ( ! is_array( $last ) || empty( $last['checked_at'] ) ) {
			return __( 'ACTIVE — ожидает первой проверки', 'shpigovsky-core' );
		}
		return sprintf(
			/* translators: 1: datetime, 2: effective state */
			__( 'ACTIVE · последняя проверка %1$s · %2$s', 'shpigovsky-core' ),
			(string) $last['checked_at'],
			isset( $last['effective'] ) ? (string) $last['effective'] : '?'
		);
	}
}

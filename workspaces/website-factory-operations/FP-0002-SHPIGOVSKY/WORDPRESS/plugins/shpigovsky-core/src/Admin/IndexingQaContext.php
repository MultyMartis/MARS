<?php
/**
 * Explicit synthetic QA context for indexing guard validation — PROD-P18J.
 *
 * QA mode requires a server-side constant; public requests cannot spoof it.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Bounded QA evidence + authorization gate for non-production incident noise.
 */
final class IndexingQaContext {

	const QA_MODE_CONST   = 'FP02_INDEXING_QA_MODE_AUTHORIZED';
	const EVIDENCE_OPTION = 'fp02_indexing_qa_evidence';
	const EVIDENCE_MAX    = 100;

	/**
	 * Whether the current request is an authorized synthetic QA run.
	 *
	 * @param array<string, mixed> $context Mutation / guard context.
	 * @return bool
	 */
	public static function is_authorized( array $context ) {
		if ( ! defined( self::QA_MODE_CONST ) || ! constant( self::QA_MODE_CONST ) ) {
			return false;
		}

		if ( empty( $context['qa_test'] ) && empty( $context['test_id'] ) ) {
			return false;
		}

		return true;
	}

	/**
	 * Normalize test id from context.
	 *
	 * @param array<string, mixed> $context Context.
	 * @return string
	 */
	public static function test_id_from_context( array $context ) {
		if ( ! empty( $context['test_id'] ) ) {
			return sanitize_key( (string) $context['test_id'] );
		}
		if ( ! empty( $context['source'] ) ) {
			return sanitize_key( (string) $context['source'] );
		}
		return 'indexing_guard';
	}

	/**
	 * Record a synthetic guard-block PASS into bounded QA evidence (not production incident stream).
	 *
	 * @param array<string, mixed> $context Context.
	 * @param array<string, mixed> $result Guard result.
	 */
	public static function record_guard_blocked_pass( array $context, array $result ) {
		$test_id = self::test_id_from_context( $context );
		$entry   = array(
			'at'       => current_time( 'mysql' ),
			'at_gmt'   => gmdate( 'Y-m-d H:i:s' ) . ' UTC',
			'test_id'  => $test_id,
			'kind'     => 'guard_blocked_close',
			'result'   => 'PASS',
			'blocked'  => ! empty( $result['blocked'] ),
			'blog_public_before' => (int) get_option( 'blog_public', 1 ),
			'blog_public_after'  => (int) get_option( 'blog_public', 1 ),
			'effective' => class_exists( IndexingState::class )
				? (string) ( IndexingState::snapshot()['effective'] ?? '' )
				: '',
		);

		$raw = get_option( self::EVIDENCE_OPTION, array() );
		if ( ! is_array( $raw ) ) {
			$raw = array();
		}
		$raw[] = $entry;
		if ( count( $raw ) > self::EVIDENCE_MAX ) {
			$raw = array_slice( $raw, -self::EVIDENCE_MAX );
		}
		update_option( self::EVIDENCE_OPTION, $raw, false );
	}

	/**
	 * Whether an Activity Log row represents historical synthetic QA (presentation only).
	 *
	 * @param object $row DB row.
	 * @return bool
	 */
	public static function is_historical_qa_activity_row( $row ) {
		if ( ! is_object( $row ) ) {
			return false;
		}
		$action = isset( $row->action ) ? (string) $row->action : '';
		$title  = isset( $row->object_title ) ? (string) $row->object_title : '';

		if ( 'indexing_qa_pass' === $action ) {
			return true;
		}

		if ( 'indexing_close_blocked' !== $action ) {
			return false;
		}

		return self::title_indicates_qa( $title );
	}

	/**
	 * @param string $title Object title from Activity Log.
	 * @return bool
	 */
	public static function title_indicates_qa( $title ) {
		$hay = strtolower( (string) $title );
		$needles = array(
			'p18g_qa_guard_test',
			'p18j_qa_guard_test',
			'qa_test',
			'· qa ·',
			'qa: ',
		);
		foreach ( $needles as $needle ) {
			if ( false !== strpos( $hay, $needle ) ) {
				return true;
			}
		}
		return false;
	}

	/**
	 * Whether critical alerting may be suppressed for this QA context.
	 *
	 * Suppression applies only while effective production state remains OPEN/consistent.
	 *
	 * @param array<string, mixed> $context Context.
	 * @return bool
	 */
	public static function may_suppress_critical_alert( array $context ) {
		if ( ! self::is_authorized( $context ) ) {
			return false;
		}
		if ( ! class_exists( IndexingState::class ) ) {
			return 1 === (int) get_option( 'blog_public', 1 );
		}
		$snap = IndexingState::snapshot();
		return IndexingState::STATE_OPEN === ( $snap['effective'] ?? '' );
	}

	/**
	 * @return array<int, array<string, mixed>>
	 */
	public static function get_evidence_tail( $limit = 20 ) {
		$raw = get_option( self::EVIDENCE_OPTION, array() );
		if ( ! is_array( $raw ) ) {
			return array();
		}
		$limit = max( 1, (int) $limit );
		return array_slice( $raw, -$limit );
	}
}

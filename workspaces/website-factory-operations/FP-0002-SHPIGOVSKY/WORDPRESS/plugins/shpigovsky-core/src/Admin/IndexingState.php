<?php
/**
 * Canonical indexability state from multiple runtime surfaces — PROD-P18G.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Computes OPEN / CLOSED / INCONSISTENT from blog_public, robots, and global meta signals.
 */
final class IndexingState {

	public const STATE_OPEN         = 'OPEN';
	public const STATE_CLOSED       = 'CLOSED';
	public const STATE_INCONSISTENT = 'INCONSISTENT';

	/**
	 * Option key for last explicit human indexing decision (audit metadata only).
	 */
	public const HUMAN_AUTHORITY_OPTION = 'fp02_indexing_human_authority';

	/**
	 * Read stored human authority metadata.
	 *
	 * @return array<string, mixed>
	 */
	public static function get_human_authority() {
		$raw = get_option( self::HUMAN_AUTHORITY_OPTION, array() );
		return is_array( $raw ) ? $raw : array();
	}

	/**
	 * Persist human authority metadata.
	 *
	 * @param string $decision OPEN|CLOSED.
	 * @param array<string, mixed> $context Actor/source context.
	 */
	public static function record_human_decision( $decision, array $context ) {
		$decision = strtoupper( sanitize_key( (string) $decision ) );
		if ( ! in_array( $decision, array( self::STATE_OPEN, self::STATE_CLOSED ), true ) ) {
			return;
		}

		$user_id = isset( $context['user_id'] ) ? (int) $context['user_id'] : get_current_user_id();
		$login   = isset( $context['actor_login'] ) ? sanitize_user( (string) $context['actor_login'] ) : '';
		$display = isset( $context['actor_display'] ) ? sanitize_text_field( (string) $context['actor_display'] ) : '';
		if ( $user_id > 0 && ( '' === $login || '' === $display ) ) {
			$user = get_userdata( $user_id );
			if ( $user ) {
				if ( '' === $login ) {
					$login = $user->user_login;
				}
				if ( '' === $display ) {
					$display = $user->display_name ? $user->display_name : $user->user_login;
				}
			}
		}

		$payload = array(
			'decision'      => $decision,
			'user_id'       => $user_id,
			'actor_login'   => $login,
			'actor_display' => $display,
			'source'        => isset( $context['source'] ) ? sanitize_key( (string) $context['source'] ) : 'unknown',
			'recorded_at'   => current_time( 'mysql' ),
			'recorded_at_gmt' => gmdate( 'Y-m-d H:i:s' ) . ' UTC',
		);

		update_option( self::HUMAN_AUTHORITY_OPTION, $payload, false );
	}

	/**
	 * Effective indexability snapshot.
	 *
	 * @return array<string, mixed>
	 */
	public static function snapshot() {
		$blog_public = (int) get_option( 'blog_public', 1 );
		$robots      = self::robots_signals();
		$meta        = self::global_meta_signals();

		$blog_open     = ( 1 === $blog_public );
		$robots_open   = ! $robots['global_disallow'];
		$meta_open     = ! $meta['global_noindex'];
		$signals_open  = $blog_open && $robots_open && $meta_open;
		$signals_closed = ( ! $blog_open ) && $robots['global_disallow'] && $meta['global_noindex'];

		if ( $signals_open ) {
			$effective = self::STATE_OPEN;
		} elseif ( $signals_closed ) {
			$effective = self::STATE_CLOSED;
		} else {
			$effective = self::STATE_INCONSISTENT;
		}

		$human = self::get_human_authority();

		return array(
			'effective'          => $effective,
			'blog_public'        => $blog_public,
			'blog_open'          => $blog_open,
			'robots'             => $robots,
			'meta'               => $meta,
			'signals_open'       => $signals_open,
			'signals_closed'     => $signals_closed,
			'human_decision'     => isset( $human['decision'] ) ? (string) $human['decision'] : '',
			'human_actor'        => self::human_actor_label( $human ),
			'human_recorded_at'  => isset( $human['recorded_at'] ) ? (string) $human['recorded_at'] : '',
			'human_source'       => isset( $human['source'] ) ? (string) $human['source'] : '',
			'fingerprint'        => self::fingerprint( $effective, $blog_public, $robots, $meta, $human ),
		);
	}

	/**
	 * Robots-related signals (prefer local file; no frontend HTTP).
	 *
	 * @return array<string, mixed>
	 */
	public static function robots_signals() {
		$path   = IndexingControl::robots_path();
		$exists = is_file( $path );
		$body   = '';
		if ( $exists ) {
			$raw = file_get_contents( $path );
			$body = is_string( $raw ) ? $raw : '';
		}

		$global_disallow = (bool) preg_match( '/^\s*Disallow:\s*\/\s*$/mi', $body );
		if ( ! $exists ) {
			$global_disallow = ( 0 === (int) get_option( 'blog_public', 1 ) );
		}

		$owner = $exists ? 'physical_file' : 'wordpress_virtual';

		return array(
			'file_exists'      => $exists,
			'owner'            => $owner,
			'global_disallow'  => $global_disallow,
			'body_head'        => mb_substr( trim( (string) $body ), 0, 160 ),
		);
	}

	/**
	 * Global meta / X-Robots signals derived locally.
	 *
	 * @return array<string, mixed>
	 */
	public static function global_meta_signals() {
		$blog_public = (int) get_option( 'blog_public', 1 );
		// Core wp_robots_noindex adds sitewide noindex when blog_public=0.
		$global_noindex = ( 0 === $blog_public );

		return array(
			'global_noindex' => $global_noindex,
			'source'         => 'blog_public_core_robots',
		);
	}

	/**
	 * Whether human decision OPEN conflicts with effective global block.
	 *
	 * @return bool
	 */
	public static function is_human_open_but_blocked() {
		$human = self::get_human_authority();
		if ( empty( $human['decision'] ) || self::STATE_OPEN !== strtoupper( (string) $human['decision'] ) ) {
			return false;
		}
		$snap = self::snapshot();
		return self::STATE_OPEN !== $snap['effective'];
	}

	/**
	 * Stable alert fingerprint.
	 *
	 * @param string               $effective Effective state.
	 * @param int                  $blog_public blog_public.
	 * @param array<string, mixed> $robots Robots signals.
	 * @param array<string, mixed> $meta Meta signals.
	 * @param array<string, mixed> $human Human authority.
	 * @return string
	 */
	public static function fingerprint( $effective, $blog_public, array $robots, array $meta, array $human ) {
		$parts = array(
			(string) $effective,
			(string) $blog_public,
			! empty( $robots['global_disallow'] ) ? '1' : '0',
			! empty( $meta['global_noindex'] ) ? '1' : '0',
			isset( $human['decision'] ) ? (string) $human['decision'] : '',
		);
		return hash( 'sha256', implode( '|', $parts ) );
	}

	/**
	 * Human actor label for dashboard.
	 *
	 * @param array<string, mixed> $human Human authority option.
	 * @return string
	 */
	public static function human_actor_label( array $human ) {
		if ( empty( $human['decision'] ) ) {
			return '';
		}
		$display = isset( $human['actor_display'] ) ? (string) $human['actor_display'] : '';
		$login   = isset( $human['actor_login'] ) ? (string) $human['actor_login'] : '';
		if ( '' !== $display && '' !== $login ) {
			return $display . ' (' . $login . ')';
		}
		if ( '' !== $display ) {
			return $display;
		}
		if ( '' !== $login ) {
			return $login;
		}
		return '';
	}
}

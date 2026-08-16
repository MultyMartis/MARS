<?php
/**
 * Native permalink persistence + readable uniqueness for public custom entities.
 *
 * PROD-P13-FU01: no custom permalink UI. Canonical owner is wp_posts.post_name.
 * Native WordPress permalink row owns editing. This module only:
 * - preserves a submitted native slug;
 * - regenerates from title when the native slug is intentionally cleared;
 * - applies readable -copy-NN uniqueness (including drafts).
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\ContentTypes\Specialist;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Data-layer slug uniqueness for public CPTs. No Admin permalink UI.
 */
final class PermalinkSlugUX implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.permalink-slug-ux';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * Post types that need public permalink editing (native WP UI).
	 *
	 * @return array<int, string>
	 */
	public static function public_slug_post_types() {
		return array( Service::POST_TYPE, Specialist::POST_TYPE );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_filter( 'wp_unique_post_slug', array( __CLASS__, 'filter_unique_slug' ), 10, 6 );
		add_filter( 'wp_insert_post_data', array( __CLASS__, 'filter_insert_post_data' ), 99, 2 );
	}

	/**
	 * Honor native slug submission on the same write that stores the post.
	 *
	 * Does not invent a second URL field. Does not regenerate existing slugs
	 * unless the native slug was submitted empty.
	 *
	 * @param array<string, mixed> $data    Sanitized post data.
	 * @param array<string, mixed> $postarr Raw post array.
	 * @return array<string, mixed>
	 */
	public static function filter_insert_post_data( $data, $postarr ) {
		$post_type = isset( $data['post_type'] ) ? (string) $data['post_type'] : '';
		if ( ! in_array( $post_type, self::public_slug_post_types(), true ) ) {
			return $data;
		}

		if ( ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) || wp_is_post_revision( isset( $postarr['ID'] ) ? (int) $postarr['ID'] : 0 ) ) {
			return $data;
		}

		$post_id = isset( $postarr['ID'] ) ? (int) $postarr['ID'] : 0;
		$parent  = isset( $data['post_parent'] ) ? (int) $data['post_parent'] : 0;
		$title   = isset( $data['post_title'] ) ? (string) $data['post_title'] : '';

		$existing = '';
		if ( $post_id > 0 ) {
			$existing = (string) get_post_field( 'post_name', $post_id );
		}

		$native_posted = self::read_native_posted_slug();
		if ( null === $native_posted ) {
			// Programmatic / non-form save: uniqueness only, never regenerate from title.
			$current = isset( $data['post_name'] ) ? sanitize_title( (string) $data['post_name'] ) : '';
			if ( '' === $current ) {
				$current = sanitize_title( $existing );
			}
			if ( '' === $current ) {
				return $data;
			}
			$data['post_name'] = self::make_unique_slug( $current, $post_id, $post_type, $parent );
			return $data;
		}

		if ( '' === $native_posted ) {
			// Operator cleared the native slug → regenerate from current title.
			if ( '' === $title ) {
				return $data;
			}
			$native_posted = sanitize_title( $title );
			if ( '' === $native_posted ) {
				return $data;
			}
		}

		$data['post_name'] = self::make_unique_slug( $native_posted, $post_id, $post_type, $parent );
		return $data;
	}

	/**
	 * Native WordPress slug field from the editor form, or null if not submitted.
	 *
	 * @return string|null Sanitized slug, empty string if cleared, null if absent.
	 */
	private static function read_native_posted_slug() {
		if ( ! isset( $_POST['post_name'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Missing
			return null;
		}

		$raw = trim( (string) wp_unslash( $_POST['post_name'] ) ); // phpcs:ignore WordPress.Security.NonceVerification.Missing, WordPress.Security.ValidatedSanitizedInput.InputNotSanitized
		if ( '' === $raw ) {
			return '';
		}

		return sanitize_title( $raw );
	}

	/**
	 * Unique slug with readable -copy-01 suffix, including drafts.
	 *
	 * Core wp_unique_post_slug returns early for draft/pending, so uniqueness
	 * for those statuses is applied here.
	 *
	 * @param string $slug        Desired slug.
	 * @param int    $post_id     Post ID.
	 * @param string $post_type   Type.
	 * @param int    $post_parent Parent.
	 * @return string
	 */
	public static function make_unique_slug( $slug, $post_id, $post_type, $post_parent ) {
		$slug = sanitize_title( (string) $slug );
		if ( '' === $slug ) {
			return $slug;
		}

		if ( self::is_slug_available( $slug, $post_id, $post_type, $post_parent ) ) {
			return $slug;
		}

		$base = preg_replace( '/-copy-\d+$/', '', $slug );
		if ( ! is_string( $base ) || '' === $base ) {
			$base = $slug;
		}

		for ( $i = 1; $i <= 99; $i++ ) {
			$candidate = $base . '-copy-' . sprintf( '%02d', $i );
			if ( self::is_slug_available( $candidate, $post_id, $post_type, $post_parent ) ) {
				return $candidate;
			}
		}

		return $slug . '-' . (string) time();
	}

	/**
	 * Prefer readable -copy-01 uniqueness for FP-0002 public CPTs.
	 *
	 * @param string $slug          Unique slug candidate from core.
	 * @param int    $post_id       Post ID.
	 * @param string $post_status   Status.
	 * @param string $post_type     Type.
	 * @param int    $post_parent   Parent.
	 * @param string $original_slug Original desired slug.
	 * @return string
	 */
	public static function filter_unique_slug( $slug, $post_id, $post_status, $post_type, $post_parent, $original_slug ) {
		if ( ! in_array( $post_type, self::public_slug_post_types(), true ) ) {
			return $slug;
		}

		$desired = sanitize_title( (string) $original_slug );
		if ( '' === $desired ) {
			$desired = sanitize_title( (string) $slug );
		}
		if ( '' === $desired ) {
			return $slug;
		}

		return self::make_unique_slug( $desired, $post_id, $post_type, $post_parent );
	}

	/**
	 * Whether a slug is free for the post type/parent scope.
	 *
	 * @param string $slug        Slug.
	 * @param int    $post_id     Post ID.
	 * @param string $post_type   Type.
	 * @param int    $post_parent Parent.
	 * @return bool
	 */
	private static function is_slug_available( $slug, $post_id, $post_type, $post_parent ) {
		global $wpdb;

		$slug = (string) $slug;
		if ( '' === $slug ) {
			return false;
		}

		$sql = $wpdb->prepare(
			"SELECT ID FROM {$wpdb->posts} WHERE post_name = %s AND post_type = %s AND ID != %d AND post_parent = %d LIMIT 1",
			$slug,
			$post_type,
			(int) $post_id,
			(int) $post_parent
		);

		$found = $wpdb->get_var( $sql ); // phpcs:ignore WordPress.DB.PreparedSQL.NotPrepared

		return empty( $found );
	}
}

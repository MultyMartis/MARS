<?php
/**
 * Legal document boolean helpers (PROD-P18A).
 *
 * Explicit false/0 is a stored value. Defaults apply only when the meta key is unset.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether a stored ACF/WordPress true_false flag is ON.
 *
 * Does not use `?:` / empty() coalescing: string "0" and boolean false stay OFF.
 *
 * @param mixed $raw Raw post meta / ACF value.
 * @return bool
 */
function shpigovsky_legal_flag_raw_is_on( $raw ) {
	if ( true === $raw || 1 === $raw || '1' === $raw ) {
		return true;
	}

	if ( false === $raw || 0 === $raw || '0' === $raw || '' === $raw || null === $raw ) {
		return false;
	}

	if ( is_string( $raw ) ) {
		$normalized = strtolower( trim( $raw ) );
		if ( in_array( $normalized, array( 'true', 'on', 'yes' ), true ) ) {
			return true;
		}
		if ( in_array( $normalized, array( 'false', 'off', 'no' ), true ) ) {
			return false;
		}
	}

	return false;
}

/**
 * Read an explicit legal boolean from post meta.
 *
 * Three-state:
 * - unset / missing key → $default_if_unset (migration fallback only)
 * - stored false / 0    → false
 * - stored true / 1     → true
 *
 * @param int    $post_id          Post ID (published, revision, or autosave).
 * @param string $meta_key         Meta key (machine name).
 * @param bool   $default_if_unset Default used only when the key does not exist.
 * @return bool
 */
function shpigovsky_legal_get_explicit_bool( $post_id, $meta_key, $default_if_unset ) {
	$post_id  = (int) $post_id;
	$meta_key = (string) $meta_key;

	if ( $post_id <= 0 || '' === $meta_key ) {
		return (bool) $default_if_unset;
	}

	if ( ! metadata_exists( 'post', $post_id, $meta_key ) ) {
		$post = get_post( $post_id );
		if ( $post && ( wp_is_post_revision( $post_id ) || wp_is_post_autosave( $post_id ) ) ) {
			$parent = (int) $post->post_parent;
			if ( $parent > 0 && $parent !== $post_id ) {
				return shpigovsky_legal_get_explicit_bool( $parent, $meta_key, $default_if_unset );
			}
		}

		return (bool) $default_if_unset;
	}

	$raw = get_post_meta( $post_id, $meta_key, true );

	return shpigovsky_legal_flag_raw_is_on( $raw );
}

/**
 * Demo marker ON → render DEMO warning. OFF → do not render.
 *
 * Uninitialized posts keep the historical ACF default (true) until an editor saves the field.
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_legal_demo_marker_enabled( $post_id = 0 ) {
	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		$post_id = (int) get_the_ID();
	}

	return shpigovsky_legal_get_explicit_bool( $post_id, 'legal_demo_marker', true );
}

/**
 * Production blocker flag. Independent of demo marker and legal_status.
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_legal_production_blocker_enabled( $post_id = 0 ) {
	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		$post_id = (int) get_the_ID();
	}

	return shpigovsky_legal_get_explicit_bool( $post_id, 'legal_production_blocker', true );
}

/**
 * Legal status slug. Independent of demo marker.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_legal_status( $post_id = 0 ) {
	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		$post_id = (int) get_the_ID();
	}

	if ( $post_id <= 0 ) {
		return '';
	}

	$raw = get_post_meta( $post_id, 'legal_status', true );

	return is_string( $raw ) ? $raw : '';
}

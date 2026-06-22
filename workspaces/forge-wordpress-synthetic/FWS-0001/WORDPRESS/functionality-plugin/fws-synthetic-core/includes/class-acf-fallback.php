<?php
/**
 * ACF Free fallback — read ACF fields or post meta when ACF is inactive.
 *
 * Global options (phone, email, address, CTA) are managed via theme Settings API
 * (see theme inc/options.php and acf-json/group_fws_options.json).
 *
 * @package FWS_Synthetic_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Unified field getter with ACF / post meta fallback.
 */
class FWS_Synthetic_ACF_Fallback {

	/**
	 * Hook registration.
	 */
	public static function init() {
		// Public API for theme template-tags.php.
	}

	/**
	 * Get field value from ACF or post meta.
	 *
	 * @param string    $key     Field name.
	 * @param int|false $post_id Post ID or false for current.
	 * @return string
	 */
	public static function get_field( $key, $post_id = false ) {
		if ( false === $post_id ) {
			$post_id = get_the_ID();
		}

		if ( function_exists( 'get_field' ) && $post_id ) {
			$acf_value = get_field( $key, $post_id );
			if ( null !== $acf_value && false !== $acf_value && '' !== $acf_value ) {
				return is_string( $acf_value ) ? $acf_value : (string) $acf_value;
			}
		}

		if ( $post_id ) {
			$meta = get_post_meta( $post_id, $key, true );
			if ( '' !== $meta && null !== $meta ) {
				return (string) $meta;
			}
		}

		return '';
	}

	/**
	 * Update field via ACF or post meta.
	 *
	 * @param string $key     Field name.
	 * @param string $value   Value.
	 * @param int    $post_id Post ID.
	 * @return bool
	 */
	public static function update_field( $key, $value, $post_id ) {
		if ( function_exists( 'update_field' ) ) {
			return (bool) update_field( $key, $value, $post_id );
		}

		return (bool) update_post_meta( $post_id, $key, sanitize_textarea_field( $value ) );
	}
}

/**
 * Theme-facing helper.
 *
 * @param string    $key     Field name.
 * @param int|false $post_id Post ID.
 * @return string
 */
function fws_synthetic_get_field( $key, $post_id = false ) {
	return FWS_Synthetic_ACF_Fallback::get_field( $key, $post_id );
}

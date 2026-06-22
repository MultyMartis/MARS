<?php
/**
 * Template helpers for options, fields, and escaping.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Get a global theme option from Settings API storage.
 *
 * @param string $key     Option key.
 * @param string $default Default value.
 * @return string
 */
function fws_get_option( $key, $default = '' ) {
	$options = get_option( 'fws_synthetic_options', array() );

	if ( ! is_array( $options ) || ! isset( $options[ $key ] ) ) {
		return $default;
	}

	return (string) $options[ $key ];
}

/**
 * Get a field value via plugin fallback or post meta.
 *
 * @param string    $key     Field/meta key.
 * @param int|false $post_id Post ID.
 * @param string    $default Default value.
 * @return string
 */
function fws_get_field( $key, $post_id = false, $default = '' ) {
	if ( function_exists( 'fws_synthetic_get_field' ) ) {
		$value = fws_synthetic_get_field( $key, $post_id );
		if ( '' !== $value && null !== $value ) {
			return (string) $value;
		}
	}

	if ( false === $post_id ) {
		$post_id = get_the_ID();
	}

	if ( $post_id ) {
		$meta = get_post_meta( $post_id, $key, true );
		if ( '' !== $meta && null !== $meta ) {
			return (string) $meta;
		}
	}

	return $default;
}

/**
 * Echo escaped HTML text.
 *
 * @param string $text Text to output.
 */
function fws_esc_html_e( $text ) {
	echo esc_html( $text );
}

/**
 * Return services archive URL.
 *
 * @return string
 */
function fws_get_services_url() {
	$link = get_post_type_archive_link( 'service' );
	return $link ? $link : home_url( '/services/' );
}

/**
 * Return contacts page URL.
 *
 * @return string
 */
function fws_get_contacts_url() {
	$contacts = get_pages(
		array(
			'meta_key'   => '_wp_page_template',
			'meta_value' => 'page-contacts.php',
			'number'     => 1,
		)
	);

	if ( ! empty( $contacts ) ) {
		return get_permalink( $contacts[0]->ID );
	}

	return home_url( '/contacts/' );
}

/**
 * Build tel: href from phone string.
 *
 * @param string $phone Phone number.
 * @return string
 */
function fws_phone_href( $phone ) {
	$digits = preg_replace( '/[^0-9+]/', '', $phone );
	return 'tel:' . $digits;
}

/**
 * Get service card excerpt text.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function fws_get_service_excerpt( $post_id ) {
	$short = fws_get_field( 'short_description', $post_id );
	if ( '' !== $short ) {
		return $short;
	}

	$service_post = get_post( $post_id );
	if ( $service_post && ! empty( $service_post->post_excerpt ) ) {
		return $service_post->post_excerpt;
	}

	return wp_trim_words( wp_strip_all_tags( get_post_field( 'post_content', $post_id ) ), 20 );
}

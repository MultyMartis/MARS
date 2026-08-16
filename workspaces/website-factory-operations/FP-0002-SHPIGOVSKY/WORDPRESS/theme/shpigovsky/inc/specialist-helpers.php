<?php
/**
 * Specialist profile helpers — PROD-P08 structured model / PROD-P11 CPT.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether the given/current object is a Specialist CPT singular (or legacy child page).
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_is_specialist_page( $post_id = 0 ) {
	$post_id = $post_id > 0 ? (int) $post_id : (int) get_the_ID();
	if ( $post_id <= 0 ) {
		return false;
	}

	if ( 'specialist' === get_post_type( $post_id ) ) {
		return true;
	}

	// Legacy safety during migration only: former child pages under hub.
	$parent_id          = (int) wp_get_post_parent_id( $post_id );
	$specialists_parent = function_exists( 'shpigovsky_get_specialists_parent_page_id' )
		? (int) shpigovsky_get_specialists_parent_page_id()
		: 0;
	return 'page' === get_post_type( $post_id )
		&& $specialists_parent > 0
		&& $parent_id === $specialists_parent;
}

/**
 * Whether the current front request is a Specialist singular.
 *
 * @return bool
 */
function shpigovsky_is_specialist_singular() {
	return is_singular( 'specialist' )
		|| ( is_page() && shpigovsky_is_specialist_page() );
}

/**
 * Normalize ACF text/wysiwyg value to trimmed string.
 *
 * @param mixed $value Raw value.
 * @return string
 */
function shpigovsky_specialist_field_string( $value ) {
	if ( is_string( $value ) ) {
		return trim( $value );
	}
	return '';
}

/**
 * Load structured specialist profile payload.
 *
 * @param int $page_id Post ID.
 * @return array<string,mixed>
 */
function shpigovsky_get_specialist_profile( $page_id ) {
	$page_id = (int) $page_id;
	$empty   = array(
		'name'            => '',
		'role'            => '',
		'experience'      => '',
		'specialty'       => '',
		'education'       => '',
		'specialization'  => '',
		'principles'      => '',
		'additional'      => '',
		'certificates'    => array(),
		'portrait_url'    => '',
		'portrait_width'  => 640,
		'portrait_height' => 640,
		'portrait_alt'    => '',
		'has_structured'  => false,
	);

	if ( $page_id <= 0 ) {
		return $empty;
	}

	$name = get_the_title( $page_id );
	$role = '';
	$experience = '';
	$specialty = '';
	$education = '';
	$specialization = '';
	$principles = '';
	$additional = '';
	$certificates = array();

	if ( function_exists( 'get_field' ) ) {
		$role           = shpigovsky_specialist_field_string( get_field( 'specialist_role', $page_id ) );
		$experience     = shpigovsky_specialist_field_string( get_field( 'specialist_experience', $page_id ) );
		$specialty      = shpigovsky_specialist_field_string( get_field( 'specialist_specialty', $page_id ) );
		$education      = shpigovsky_specialist_field_string( get_field( 'specialist_education', $page_id ) );
		$specialization = shpigovsky_specialist_field_string( get_field( 'specialist_specialization', $page_id ) );
		$principles     = shpigovsky_specialist_field_string( get_field( 'specialist_principles', $page_id ) );
		$additional     = shpigovsky_specialist_field_string( get_field( 'specialist_additional', $page_id ) );
		$gallery        = get_field( 'specialist_certificates', $page_id );
		if ( is_array( $gallery ) ) {
			foreach ( $gallery as $img ) {
				if ( ! is_array( $img ) || empty( $img['ID'] ) && empty( $img['url'] ) ) {
					continue;
				}
				$certificates[] = $img;
			}
		}
	}

	if ( '' === $role ) {
		$role_meta = trim( (string) get_post_meta( $page_id, '_shpigovsky_specialist_role', true ) );
		if ( '' !== $role_meta ) {
			$role = $role_meta;
		} else {
			$excerpt = trim( (string) get_post_field( 'post_excerpt', $page_id ) );
			if ( '' !== $excerpt ) {
				$role = wp_strip_all_tags( $excerpt );
			}
		}
	}

	$portrait_url    = '';
	$portrait_width  = 640;
	$portrait_height = 640;
	$portrait_alt    = $name;
	$thumb_id        = (int) get_post_thumbnail_id( $page_id );
	if ( $thumb_id > 0 ) {
		$src = wp_get_attachment_image_src( $thumb_id, 'large' );
		if ( is_array( $src ) && ! empty( $src[0] ) ) {
			$portrait_url    = (string) $src[0];
			$portrait_width  = ! empty( $src[1] ) ? (int) $src[1] : $portrait_width;
			$portrait_height = ! empty( $src[2] ) ? (int) $src[2] : $portrait_height;
		}
		$alt = trim( (string) get_post_meta( $thumb_id, '_wp_attachment_image_alt', true ) );
		if ( '' !== $alt ) {
			$portrait_alt = $alt;
		}
	}
	if ( '' === $portrait_url && function_exists( 'shpigovsky_get_specialist_placeholder_image' ) ) {
		$placeholder     = shpigovsky_get_specialist_placeholder_image();
		$portrait_url    = (string) $placeholder['url'];
		$portrait_width  = (int) $placeholder['width'];
		$portrait_height = (int) $placeholder['height'];
	}

	$has_structured = (
		'' !== $role
		|| '' !== $experience
		|| '' !== $specialty
		|| '' !== $education
		|| '' !== $specialization
		|| '' !== $principles
		|| '' !== $additional
		|| ! empty( $certificates )
	);

	return array(
		'name'            => $name,
		'role'            => $role,
		'experience'      => $experience,
		'specialty'       => $specialty,
		'education'       => $education,
		'specialization'  => $specialization,
		'principles'      => $principles,
		'additional'      => $additional,
		'certificates'    => $certificates,
		'portrait_url'    => $portrait_url,
		'portrait_width'  => $portrait_width,
		'portrait_height' => $portrait_height,
		'portrait_alt'    => $portrait_alt,
		'has_structured'  => $has_structured,
	);
}

/**
 * Enqueue Fancybox on specialist pages that have a certificate gallery.
 */
function shpigovsky_maybe_enqueue_specialist_fancybox() {
	if ( ! shpigovsky_is_specialist_singular() ) {
		return;
	}
	$profile = shpigovsky_get_specialist_profile( (int) get_the_ID() );
	if ( empty( $profile['certificates'] ) ) {
		return;
	}
	if ( function_exists( 'shpigovsky_enqueue_fancybox_vendor' ) ) {
		shpigovsky_enqueue_fancybox_vendor();
	}
}
add_action( 'wp_enqueue_scripts', 'shpigovsky_maybe_enqueue_specialist_fancybox', 40 );

/**
 * Enqueue specialist profile CSS.
 */
function shpigovsky_enqueue_specialist_profile_assets() {
	if ( ! shpigovsky_is_specialist_singular() ) {
		return;
	}
	$path = SHPIGOVSKY_THEME_DIR . '/assets/css/fp02-specialist-profile.css';
	if ( ! is_readable( $path ) ) {
		return;
	}
	$deps = array();
	if ( wp_style_is( 'shpigovsky-v9', 'enqueued' ) || wp_style_is( 'shpigovsky-v9', 'registered' ) ) {
		$deps[] = 'shpigovsky-v9';
	}
	wp_enqueue_style(
		'shpigovsky-fp02-specialist-profile',
		SHPIGOVSKY_THEME_URI . '/assets/css/fp02-specialist-profile.css',
		$deps,
		shpigovsky_asset_version( 'css/fp02-specialist-profile.css' )
	);
}
add_action( 'wp_enqueue_scripts', 'shpigovsky_enqueue_specialist_profile_assets', 35 );

/**
 * PROD-P11: never render Specialist CPT via leftover page template meta.
 *
 * WordPress may prefer `_wp_page_template` over `single-specialist.php` for CPT singles.
 *
 * @param string $template Resolved template path.
 * @return string
 */
function shpigovsky_force_specialist_single_template( $template ) {
	if ( ! is_singular( 'specialist' ) ) {
		return $template;
	}

	$custom = locate_template( array( 'single-specialist.php' ) );
	return $custom ? $custom : $template;
}
add_filter( 'single_template', 'shpigovsky_force_specialist_single_template', 99 );
add_filter( 'template_include', 'shpigovsky_force_specialist_single_template', 99 );

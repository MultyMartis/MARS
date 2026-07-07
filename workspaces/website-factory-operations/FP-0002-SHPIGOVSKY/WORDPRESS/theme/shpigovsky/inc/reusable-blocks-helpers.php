<?php
/**
 * Reusable blocks helpers — V9-06E18 Batch 1.
 *
 * Read-only option resolution with layered fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ACF options context for final form block admin.
 */
function shpigovsky_get_final_form_block_context() {
	return 'fp02-block-final-form';
}

/**
 * ACF options context for specialists block admin.
 */
function shpigovsky_get_specialists_block_context() {
	return 'fp02-block-specialists';
}

/**
 * ACF options context for global CTA band defaults admin.
 */
function shpigovsky_get_cta_bands_block_context() {
	return 'fp02-block-cta-bands';
}

/**
 * Read a scalar block option field.
 *
 * @param string $field_name Field name.
 * @param string $context    ACF options context slug.
 * @return string
 */
function shpigovsky_get_block_option_scalar( $field_name, $context ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$value = get_field( $field_name, $context );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Resolve final form heading with block → home → static fallback chain.
 *
 * @param string $static_fallback Static fallback when all sources empty.
 * @return string
 */
function shpigovsky_get_final_form_heading( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'final_form_heading', shpigovsky_get_final_form_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Остались вопросы?', 'shpigovsky' );
	}

	return shpigovsky_home_text_or_fallback( 'home_cta_title', $static_fallback );
}

/**
 * Resolve final form lead text.
 *
 * @param string $static_fallback Static fallback when all sources empty.
 * @return string
 */
function shpigovsky_get_final_form_lead( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'final_form_lead', shpigovsky_get_final_form_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь', 'shpigovsky' );
	}

	return shpigovsky_home_text_or_fallback( 'home_cta_text', $static_fallback );
}

/**
 * Resolve final form submit button label.
 *
 * @param string $static_fallback Static fallback when all sources empty.
 * @return string
 */
function shpigovsky_get_final_form_submit_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'final_form_submit_label', shpigovsky_get_final_form_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Записаться на консультацию', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_button_label', $static_fallback );
}

/**
 * Resolve a final form field label with block option then static i18n fallback.
 *
 * @param string $field_name      Block option field name.
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_final_form_field_label( $field_name, $static_fallback ) {
	$block = shpigovsky_get_block_option_scalar( $field_name, shpigovsky_get_final_form_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve specialists section heading.
 *
 * @param string $static_fallback Static fallback heading.
 * @return string
 */
function shpigovsky_get_specialists_section_heading( $static_fallback = 'Специалисты центра' ) {
	$block = shpigovsky_get_block_option_scalar( 'specialists_section_heading', shpigovsky_get_specialists_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	return shpigovsky_home_text_or_fallback( 'home_specialists_heading', $static_fallback );
}

/**
 * Resolve specialists all-link label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_specialists_all_link_label( $static_fallback = 'все специалисты' ) {
	$block = shpigovsky_get_block_option_scalar( 'specialists_all_link_label', shpigovsky_get_specialists_block_context() );

	return '' !== $block ? $block : $static_fallback;
}

/**
 * Resolve specialists all-link URL.
 *
 * @param string $static_fallback Static fallback URL.
 * @return string
 */
function shpigovsky_get_specialists_all_link_url( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'specialists_all_link_url', shpigovsky_get_specialists_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = home_url( '/o-centre/' );
	}

	return $static_fallback;
}

/**
 * Normalize one specialists repeater row into render-ready card data.
 *
 * @param array<string, mixed> $row          ACF repeater row.
 * @param array<string, mixed> $fallback_row Static fallback row matched by index.
 * @return array{image:string,width:int,height:int,name:string,role:string,link:string}|null
 */
function shpigovsky_normalize_specialist_card_row( $row, $fallback_row ) {
	if ( ! is_array( $row ) ) {
		return null;
	}

	$name = isset( $row['specialist_name'] ) ? trim( (string) $row['specialist_name'] ) : '';
	$role = isset( $row['specialist_role'] ) ? trim( (string) $row['specialist_role'] ) : '';
	$link = isset( $row['specialist_link'] ) ? trim( (string) $row['specialist_link'] ) : '';

	if ( '' === $name && '' === $role ) {
		return null;
	}

	if ( '' === $name && is_array( $fallback_row ) ) {
		$name = isset( $fallback_row['name'] ) ? (string) $fallback_row['name'] : '';
	}

	if ( '' === $role && is_array( $fallback_row ) ) {
		$role = isset( $fallback_row['role'] ) ? (string) $fallback_row['role'] : '';
	}

	$image_path = isset( $row['specialist_photo_asset'] ) ? trim( (string) $row['specialist_photo_asset'] ) : '';
	$width      = isset( $row['specialist_photo_width'] ) ? (int) $row['specialist_photo_width'] : 0;
	$height     = isset( $row['specialist_photo_height'] ) ? (int) $row['specialist_photo_height'] : 0;
	$media      = isset( $row['specialist_photo'] ) ? $row['specialist_photo'] : null;
	$media_url  = shpigovsky_acf_image_url( $media );

	if ( '' !== $media_url ) {
		$image_path = $media_url;
		if ( is_array( $media ) ) {
			if ( ! empty( $media['width'] ) ) {
				$width = (int) $media['width'];
			}
			if ( ! empty( $media['height'] ) ) {
				$height = (int) $media['height'];
			}
		}
	} elseif ( '' !== $image_path ) {
		if ( ! preg_match( '#^https?://#i', $image_path ) ) {
			$image_path = shpigovsky_asset_uri( $image_path );
		}
	} elseif ( is_array( $fallback_row ) && ! empty( $fallback_row['image'] ) ) {
		$image_path = shpigovsky_asset_uri( (string) $fallback_row['image'] );
	}

	if ( '' === $image_path ) {
		return null;
	}

	if ( $width <= 0 && is_array( $fallback_row ) ) {
		$width = isset( $fallback_row['width'] ) ? (int) $fallback_row['width'] : 615;
	}

	if ( $height <= 0 && is_array( $fallback_row ) ) {
		$height = isset( $fallback_row['height'] ) ? (int) $fallback_row['height'] : 605;
	}

	return array(
		'image'  => $image_path,
		'width'  => $width,
		'height' => $height,
		'name'   => $name,
		'role'   => $role,
		'link'   => $link,
	);
}

/**
 * Resolve specialists cards for all reusable specialists renderers.
 *
 * Fallback order: block repeater → V9 static fixture.
 *
 * @return array<int, array{image:string,width:int,height:int,name:string,role:string,link:string}>
 */
function shpigovsky_get_specialists_cards() {
	$fallback = shpigovsky_get_v9_specialists_cards();
	$rows     = array();

	if ( function_exists( 'get_field' ) ) {
		$candidate = get_field( 'specialists_items', shpigovsky_get_specialists_block_context() );

		if ( is_array( $candidate ) ) {
			$rows = $candidate;
		}
	}

	if ( empty( $rows ) ) {
		return $fallback;
	}

	$cards = array();

	foreach ( $rows as $index => $row ) {
		$fallback_row = isset( $fallback[ $index ] ) ? $fallback[ $index ] : ( ! empty( $fallback ) ? $fallback[0] : array() );
		$card         = shpigovsky_normalize_specialist_card_row( $row, $fallback_row );

		if ( null !== $card ) {
			$cards[] = $card;
		}
	}

	return ! empty( $cards ) ? $cards : $fallback;
}

/**
 * Resolve global program CTA band default title.
 *
 * @param string $static_fallback Static fallback title.
 * @return string
 */
function shpigovsky_get_cta_band_default_title( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_default_title', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	$global = shpigovsky_get_site_option( 'global_cta_title' );

	if ( '' !== $global ) {
		return $global;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Запишитесь на встречу', 'shpigovsky' );
	}

	return $static_fallback;
}

/**
 * Resolve global program CTA band default subtitle.
 *
 * @param string $static_fallback Static fallback subtitle.
 * @return string
 */
function shpigovsky_get_cta_band_default_subtitle( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_default_subtitle', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	$global = shpigovsky_get_site_option( 'global_cta_text' );

	if ( '' !== $global ) {
		return $global;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.', 'shpigovsky' );
	}

	return $static_fallback;
}

/**
 * Resolve global program CTA band phone hint.
 *
 * @param string $static_fallback Static fallback hint.
 * @return string
 */
function shpigovsky_get_cta_band_phone_hint( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_phone_hint', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Или позвоните нам', 'shpigovsky' );
	}

	return $static_fallback;
}

/**
 * Resolve global program CTA band default button label.
 *
 * @param string $static_fallback Static fallback label.
 * @return string
 */
function shpigovsky_get_cta_band_default_button_label( $static_fallback = '' ) {
	$block = shpigovsky_get_block_option_scalar( 'cta_band_default_button_label', shpigovsky_get_cta_bands_block_context() );

	if ( '' !== $block ) {
		return $block;
	}

	if ( '' === $static_fallback ) {
		$static_fallback = __( 'Записаться', 'shpigovsky' );
	}

	return shpigovsky_chrome_label_or_fallback( 'default_button_label', $static_fallback );
}

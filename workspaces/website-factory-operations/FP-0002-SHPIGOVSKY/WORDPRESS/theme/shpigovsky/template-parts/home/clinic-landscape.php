<?php
/**
 * Template part: home/clinic-landscape.php
 *
 * V9-06E40: ACF image with theme asset fallback.
 * V9-06E46-FIX04: on service section pages use section_clinic_landscape_image (not Home).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$args            = isset( $args ) && is_array( $args ) ? $args : array();
$modifier_class  = isset( $args['modifier_class'] ) ? trim( (string) $args['modifier_class'] ) : '';
$section_classes = 'clinic-landscape';

if ( '' !== $modifier_class ) {
	$section_classes .= ' ' . $modifier_class;
}

$asset_rel     = 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp';
$fallback_alt  = __( 'Здание и территория реабилитационного центра', 'shpigovsky' );
$fallback_w    = 1139;
$fallback_h    = 584;

if ( function_exists( 'shpigovsky_is_service_section_context' ) && shpigovsky_is_service_section_context() ) {
	$section_id = function_exists( 'shpigovsky_get_current_service_id' ) ? shpigovsky_get_current_service_id() : get_the_ID();
	$image      = function_exists( 'shpigovsky_section_image_or_asset' )
		? shpigovsky_section_image_or_asset( $section_id, 'section_clinic_landscape_image', $asset_rel, $fallback_alt, $fallback_w, $fallback_h )
		: array(
			'url'    => function_exists( 'shpigovsky_asset_uri' ) ? shpigovsky_asset_uri( $asset_rel ) : '',
			'alt'    => $fallback_alt,
			'width'  => $fallback_w,
			'height' => $fallback_h,
		);
} elseif ( function_exists( 'shpigovsky_is_service_general_context' ) && shpigovsky_is_service_general_context() ) {
	// V9-06E47: service_general pages use page-specific landscape image (not Home).
	$service_id = function_exists( 'shpigovsky_get_current_service_id' ) ? shpigovsky_get_current_service_id() : get_the_ID();
	$image      = function_exists( 'shpigovsky_general_image_or_asset' )
		? shpigovsky_general_image_or_asset( $service_id, 'service_general_clinic_landscape_image', $asset_rel, $fallback_alt, $fallback_w, $fallback_h )
		: array(
			'url'    => function_exists( 'shpigovsky_asset_uri' ) ? shpigovsky_asset_uri( $asset_rel ) : '',
			'alt'    => $fallback_alt,
			'width'  => $fallback_w,
			'height' => $fallback_h,
		);
} else {
	$image = shpigovsky_home_image_or_asset(
		'home_clinic_landscape_image',
		$asset_rel,
		$fallback_alt,
		$fallback_w,
		$fallback_h
	);
}

?>
<section data-reveal class="<?php echo esc_attr( $section_classes ); ?>" aria-label="<?php esc_attr_e( 'Территория клиники', 'shpigovsky' ); ?>">
	<div class="container">
		<div class="clinic-landscape__bleed">
			<img
				class="clinic-landscape__image"
				src="<?php echo esc_url( $image['url'] ); ?>"
				width="<?php echo esc_attr( (string) $image['width'] ); ?>"
				height="<?php echo esc_attr( (string) $image['height'] ); ?>"
				alt="<?php echo esc_attr( $image['alt'] ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>
	</div>
</section>

<?php
/**
 * Template part: service/corridor.php
 *
 * V9 service-leaf-corridor-v1 — ACF image SoT on service_general (V9-06E47).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );

if ( ! shpigovsky_is_service_general_variant( $variant ) && 'leaf' !== $variant ) {
	return;
}

$alt_fallback = __( 'Интерьер клиники — коридор с картинами', 'shpigovsky' );
$alt_field    = function_exists( 'shpigovsky_get_general_field' )
	? shpigovsky_get_general_field( $post_id, 'service_general_corridor_image_alt' )
	: '';
$alt          = '' !== $alt_field ? $alt_field : $alt_fallback;

if ( shpigovsky_is_service_general_variant( $variant ) && function_exists( 'shpigovsky_general_image_or_asset' ) ) {
	$image = shpigovsky_general_image_or_asset(
		$post_id,
		'service_general_corridor_image',
		'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp',
		$alt,
		2187,
		1231
	);
} else {
	$image = array(
		'url'    => shpigovsky_asset_uri( 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp' ),
		'alt'    => $alt,
		'width'  => 2187,
		'height' => 1231,
	);
}

if ( empty( $image['url'] ) ) {
	return;
}
?>
<section data-reveal class="service-leaf-corridor-v1" aria-label="<?php esc_attr_e( 'Интерьер клиники', 'shpigovsky' ); ?>">
	<div class="container service-leaf-corridor-v1__container">
		<div class="service-leaf-corridor-v1__bleed">
			<img
				class="service-leaf-corridor-v1__image"
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

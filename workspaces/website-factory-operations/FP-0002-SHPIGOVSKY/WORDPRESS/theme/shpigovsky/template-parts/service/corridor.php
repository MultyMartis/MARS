<?php
/**
 * Template part: service/corridor.php
 *
 * V9 service-leaf-corridor-v1 static visual block.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );

if ( 'alcohol-special' !== $variant && 'leaf' !== $variant ) {
	return;
}
?>
<section data-reveal class="service-leaf-corridor-v1" aria-label="<?php esc_attr_e( 'Интерьер клиники', 'shpigovsky' ); ?>">
	<div class="container service-leaf-corridor-v1__container">
		<div class="service-leaf-corridor-v1__bleed">
			<img
				class="service-leaf-corridor-v1__image"
				src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp' ) ); ?>"
				width="2187"
				height="1231"
				alt="<?php esc_attr_e( 'Интерьер клиники — коридор с картинами', 'shpigovsky' ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>
	</div>
</section>

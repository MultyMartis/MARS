<?php
/**
 * Template part: home/clinic-landscape.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
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

?>
<section data-reveal class="<?php echo esc_attr( $section_classes ); ?>" aria-label="<?php esc_attr_e( 'Территория клиники', 'shpigovsky' ); ?>">
	<div class="container">
		<div class="clinic-landscape__bleed">
			<img
				class="clinic-landscape__image"
				src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp' ) ); ?>"
				width="1139"
				height="584"
				alt="<?php esc_attr_e( 'Здание и территория реабилитационного центра', 'shpigovsky' ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>
	</div>
</section>

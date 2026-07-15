<?php
/**
 * Template part: service/bordered-info.php
 *
 * Service-general bordered info band — ACF repeater SoT (V9-06E47).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );

if ( ! shpigovsky_is_service_general_variant( $variant ) ) {
	return;
}

$subsections = function_exists( 'shpigovsky_get_general_bordered_info_items' )
	? shpigovsky_get_general_bordered_info_items( $post_id )
	: array();

if ( empty( $subsections ) ) {
	return;
}
?>
<section data-reveal class="service-leaf-bordered-info-v1" id="service-leaf-bordered-info" aria-labelledby="service-leaf-bordered-info-heading">
	<div class="container service-leaf-bordered-info-v1__container">
		<div class="service-leaf-bordered-info-v1__panel">
			<h2 class="visually-hidden" id="service-leaf-bordered-info-heading"><?php echo esc_html__( 'О природе зависимости', 'shpigovsky' ); ?></h2>
			<?php foreach ( $subsections as $subsection ) : ?>
				<div class="service-leaf-bordered-info-v1__subsection">
					<h3 class="service-leaf-bordered-info-v1__subsection-heading"><?php echo esc_html( $subsection['heading'] ); ?></h3>
					<p class="service-leaf-bordered-info-v1__text"><?php echo esc_html( $subsection['text'] ); ?></p>
				</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>

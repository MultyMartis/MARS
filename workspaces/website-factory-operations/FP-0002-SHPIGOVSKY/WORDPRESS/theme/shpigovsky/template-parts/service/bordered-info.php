<?php
/**
 * Template part: service/bordered-info.php
 *
 * Alcohol-special bordered info band — static V9 subsections.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );

if ( 'alcohol-special' !== $variant ) {
	return;
}

$subsections = shpigovsky_get_v9_alcohol_bordered_info_subsections();

if ( empty( $subsections ) ) {
	return;
}
?>
<section data-reveal class="service-leaf-bordered-info-v1" id="service-leaf-bordered-info" aria-labelledby="service-leaf-bordered-info-heading">
	<div class="container service-leaf-bordered-info-v1__container">
		<div class="service-leaf-bordered-info-v1__panel">
			<h2 class="visually-hidden" id="service-leaf-bordered-info-heading"><?php echo esc_html__( 'О природе алкогольной зависимости', 'shpigovsky' ); ?></h2>
			<?php foreach ( $subsections as $subsection ) : ?>
				<div class="service-leaf-bordered-info-v1__subsection">
					<h3 class="service-leaf-bordered-info-v1__subsection-heading"><?php echo esc_html( $subsection['heading'] ); ?></h3>
					<p class="service-leaf-bordered-info-v1__text"><?php echo esc_html( $subsection['text'] ); ?></p>
				</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>

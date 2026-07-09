<?php
/**
 * Template part: institutional/approach-band.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_is_about_hub_page() ) {
	return;
}

$page_id = (int) get_queried_object_id();
$context = shpigovsky_get_about_approach_context( $page_id );
?>
<section class="program-approach-band" id="our-approach" aria-labelledby="our-approach-heading">
	<div class="container program-approach-band__container">
		<div class="program-approach-band__head">
			<h2 class="program-approach-band__heading" id="our-approach-heading"><?php echo esc_html( $context['heading'] ); ?></h2>
			<a class="home-rehabilitation-program__all-link program-approach-band__all-link" href="<?php echo esc_url( $context['link_url'] ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html( $context['link_label'] ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>
		<p class="program-approach-band__highlight block-whith-red-line"><?php echo esc_html( $context['highlight'] ); ?></p>
		<p class="program-approach-band__intro"><?php echo esc_html( $context['intro'] ); ?></p>
	</div>
</section>

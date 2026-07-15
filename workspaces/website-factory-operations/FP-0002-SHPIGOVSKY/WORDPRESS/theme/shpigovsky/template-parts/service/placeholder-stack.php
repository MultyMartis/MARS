<?php
/**
 * Service placeholder / stub stack (V9-06E51).
 *
 * Temporary layout mode: H1 only inside main.
 * Header, navigation, and footer come from the normal theme shell.
 * ACF content is preserved in meta and is not rendered here.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = function_exists( 'shpigovsky_get_current_service_id' )
	? (int) shpigovsky_get_current_service_id()
	: (int) get_the_ID();

$h1 = '';
if ( function_exists( 'shpigovsky_get_service_hero_title' ) ) {
	$h1 = (string) shpigovsky_get_service_hero_title( $post_id );
}
if ( '' === trim( $h1 ) ) {
	$h1 = (string) get_the_title( $post_id );
}
if ( '' === trim( $h1 ) ) {
	$h1 = __( 'Услуга', 'shpigovsky' );
}
?>
<section class="service-placeholder-stack plain-page-content" data-content-status="service-placeholder" data-layout-mode="placeholder">
	<div class="container plain-page-content__container">
		<h1 class="plain-page-content__title"><?php echo esc_html( $h1 ); ?></h1>
	</div>
</section>

<?php
/**
 * Template part: service/bordered-info.php
 *
 * Alcohol-special bordered info band — uses intro_note when present.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$note    = shpigovsky_get_service_field( $post_id, 'intro_note' );

if ( '' === $note ) {
	return;
}
?>
<section data-reveal class="service-leaf-bordered-info-v1" id="service-leaf-bordered-info" aria-labelledby="service-leaf-bordered-info-heading">
	<div class="container service-leaf-bordered-info-v1__container">
		<h2 class="visually-hidden" id="service-leaf-bordered-info-heading"><?php echo esc_html__( 'Дополнительная информация', 'shpigovsky' ); ?></h2>
		<p class="service-leaf-bordered-info-v1__text"><?php echo wp_kses_post( $note ); ?></p>
	</div>
</section>

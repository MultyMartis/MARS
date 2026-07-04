<?php
/**
 * Template part: service/intro.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id  = shpigovsky_get_current_service_id();
$heading  = shpigovsky_get_service_hero_title( $post_id );
$intro    = shpigovsky_get_service_field( $post_id, 'intro_text' );
$highlight = shpigovsky_get_service_field( $post_id, 'intro_note' );

if ( '' === $intro && '' === $highlight ) {
	$content = get_post_field( 'post_content', $post_id );
	$intro   = is_string( $content ) ? trim( wp_strip_all_tags( $content ) ) : '';
}

if ( '' === $intro && '' === $highlight ) {
	return;
}
?>
<section data-reveal class="service-leaf-intro-v1" id="service-leaf-intro" aria-labelledby="service-leaf-intro-heading">
	<div class="container service-leaf-intro-v1__container">
		<?php if ( '' !== $heading ) : ?>
			<h2 class="service-leaf-intro-v1__heading" id="service-leaf-intro-heading"><?php echo esc_html( $heading ); ?></h2>
		<?php endif; ?>
		<?php if ( '' !== $highlight ) : ?>
			<p class="service-leaf-intro-v1__lead block-whith-red-line"><?php echo wp_kses_post( $highlight ); ?></p>
		<?php endif; ?>
		<?php if ( '' !== $intro && $intro !== $highlight ) : ?>
			<p class="service-leaf-intro-v1__body"><?php echo wp_kses_post( $intro ); ?></p>
		<?php endif; ?>
	</div>
</section>

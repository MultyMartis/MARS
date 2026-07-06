<?php
/**
 * Template part: components/service-card.php
 *
 * Expects query vars: service_card_title, service_card_url, service_card_text, service_card_variant.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$title   = get_query_var( 'service_card_title', '' );
$url     = get_query_var( 'service_card_url', '' );
$text    = get_query_var( 'service_card_text', '' );
$variant = get_query_var( 'service_card_variant', 'hub' );

$title = is_string( $title ) ? trim( $title ) : '';

if ( '' === $title ) {
	return;
}

$url  = is_string( $url ) ? trim( $url ) : '';
$text = is_string( $text ) ? trim( $text ) : '';

if ( 'v2' === $variant ) :
	?>
	<article class="services-category-section-v2__service">
		<div class="services-category-section-v2__service-head">
			<h3 class="services-category-section-v2__service-title">
				<span class="services-category-section-v2__service-name"><?php echo esc_html( $title ); ?></span>
				<span class="services-category-section-v2__service-leader" aria-hidden="true"></span>
			</h3>
			<?php if ( '' !== $url ) : ?>
				<a class="services-category-section-v2__service-link home-rehabilitation-program__all-link" href="<?php echo esc_url( $url ); ?>">
					<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'узнать больше', 'shpigovsky' ); ?></span>
					<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
				</a>
			<?php endif; ?>
		</div>
		<?php if ( '' !== $text ) : ?>
			<p class="services-category-section-v2__service-text"><?php echo wp_kses_post( $text ); ?></p>
		<?php endif; ?>
	</article>
	<?php
	return;
endif;
?>
<article class="services-category-hub__service">
	<h3 class="services-category-hub__service-title">
		<?php if ( '' !== $url ) : ?>
			<a class="services-category-hub__service-link" href="<?php echo esc_url( $url ); ?>">
				<span class="services-category-hub__service-name"><?php echo esc_html( $title ); ?></span>
				<span class="services-category-hub__service-leader" aria-hidden="true"></span>
				<span class="services-category-hub__service-icon" aria-hidden="true">
					<i class="fas fa-external-link-alt services-category-hub__service-icon-image" aria-hidden="true"></i>
				</span>
			</a>
		<?php else : ?>
			<span class="services-category-hub__service-name"><?php echo esc_html( $title ); ?></span>
		<?php endif; ?>
	</h3>
	<?php if ( '' !== $text ) : ?>
		<p class="services-category-hub__service-text"><?php echo wp_kses_post( $text ); ?></p>
	<?php endif; ?>
</article>

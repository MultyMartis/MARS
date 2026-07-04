<?php
/**
 * Template part: components/service-card.php
 *
 * Expects query vars: service_card_title, service_card_url, service_card_text.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$title = get_query_var( 'service_card_title', '' );
$url   = get_query_var( 'service_card_url', '' );
$text  = get_query_var( 'service_card_text', '' );

$title = is_string( $title ) ? trim( $title ) : '';

if ( '' === $title ) {
	return;
}

$url  = is_string( $url ) ? trim( $url ) : '';
$text = is_string( $text ) ? trim( $text ) : '';
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

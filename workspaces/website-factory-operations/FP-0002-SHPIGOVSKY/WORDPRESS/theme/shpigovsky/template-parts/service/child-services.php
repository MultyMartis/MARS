<?php
/**
 * Template part: service/child-services.php
 *
 * Tile grid of direct child services — shown before FAQ on service stack.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();

if ( $post_id <= 0 || ! shpigovsky_service_child_services_block_enabled( $post_id ) ) {
	return;
}

$children = shpigovsky_get_service_children( $post_id );

if ( empty( $children ) ) {
	return;
}

$heading    = shpigovsky_get_service_child_services_heading( $post_id );
$heading_id = 'service-child-services-heading';
?>
<section
	data-reveal
	class="service-child-services"
	id="service-child-services"
	aria-labelledby="<?php echo esc_attr( $heading_id ); ?>"
>
	<div class="container service-child-services__container">
		<h2 class="service-child-services__heading" id="<?php echo esc_attr( $heading_id ); ?>">
			<?php echo esc_html( $heading ); ?>
		</h2>

		<div class="service-child-services__grid">
			<?php foreach ( $children as $child ) : ?>
				<?php
				if ( ! $child instanceof WP_Post ) {
					continue;
				}

				$title = get_the_title( $child );
				$url   = get_permalink( $child );
				$text  = '';

				if ( function_exists( 'shpigovsky_get_service_mini_description' ) ) {
					$text = shpigovsky_get_service_mini_description( $child->ID );
				} else {
					$text = shpigovsky_get_service_field( $child->ID, 'service_short_description' );
					$text = is_string( $text ) ? trim( $text ) : '';
				}

				$image = shpigovsky_get_service_child_card_image_url( $child->ID );

				if ( '' === $title || ! is_string( $url ) || '' === $url ) {
					continue;
				}
				?>
				<article class="service-child-services__card">
					<a class="service-child-services__card-link" href="<?php echo esc_url( $url ); ?>">
						<?php if ( '' !== $image ) : ?>
							<span class="service-child-services__card-media" aria-hidden="true">
								<img
									class="service-child-services__card-image"
									src="<?php echo esc_url( $image ); ?>"
									alt=""
									loading="lazy"
									decoding="async"
								>
							</span>
						<?php endif; ?>
						<span class="service-child-services__card-body">
							<span class="service-child-services__card-title"><?php echo esc_html( $title ); ?></span>
							<?php if ( '' !== $text ) : ?>
								<span class="service-child-services__card-text"><?php echo esc_html( $text ); ?></span>
							<?php endif; ?>
						</span>
					</a>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>

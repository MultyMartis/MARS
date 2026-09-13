<?php
/**
 * Template part: service/child-services.php
 *
 * Adaptive tile grid of direct child services — shown before FAQ on service stack.
 * Featured card (optional): first child in canonical order with a valid service-owned image.
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

$cards = array();

foreach ( $children as $child ) {
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

	$cards[] = array(
		'title' => $title,
		'url'   => $url,
		'text'  => is_string( $text ) ? trim( $text ) : '',
		'image' => is_string( $image ) ? $image : '',
	);
}

if ( empty( $cards ) ) {
	return;
}

$featured_index = null;

foreach ( $cards as $index => $card ) {
	if ( '' !== $card['image'] ) {
		$featured_index = $index;
		break;
	}
}

$grid_classes = array( 'service-child-services__grid' );

if ( null !== $featured_index ) {
	$grid_classes[] = 'service-child-services__grid--has-featured';
}
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

		<div class="<?php echo esc_attr( implode( ' ', $grid_classes ) ); ?>">
			<?php foreach ( $cards as $index => $card ) : ?>
				<?php
				$is_featured = ( null !== $featured_index && $index === $featured_index );
				$has_image   = '' !== $card['image'];
				$has_text    = '' !== $card['text'];

				$card_classes = array( 'service-child-services__card' );

				if ( $is_featured ) {
					$card_classes[] = 'service-child-services__card--featured';
				}

				if ( $has_image ) {
					$card_classes[] = 'service-child-services__card--has-image';
				} else {
					$card_classes[] = 'service-child-services__card--no-image';
				}

				if ( $has_text ) {
					$card_classes[] = 'service-child-services__card--has-text';
				} else {
					$card_classes[] = 'service-child-services__card--compact';
				}
				?>
				<article class="<?php echo esc_attr( implode( ' ', $card_classes ) ); ?>">
					<a class="service-child-services__card-link" href="<?php echo esc_url( $card['url'] ); ?>">
						<?php if ( $has_image ) : ?>
							<span class="service-child-services__card-media" aria-hidden="true">
								<img
									class="service-child-services__card-image"
									src="<?php echo esc_url( $card['image'] ); ?>"
									alt=""
									loading="lazy"
									decoding="async"
								>
							</span>
						<?php endif; ?>
						<span class="service-child-services__card-body">
							<span class="service-child-services__card-title"><?php echo esc_html( $card['title'] ); ?></span>
							<?php if ( $has_text ) : ?>
								<span class="service-child-services__card-text"><?php echo esc_html( $card['text'] ); ?></span>
							<?php endif; ?>
						</span>
					</a>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>

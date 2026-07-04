<?php
/**
 * Template part: service/children.php
 *
 * Parent service child listing — CPT query with optional manual_related_services override.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$posts   = array();

if ( function_exists( 'get_field' ) ) {
	$manual = get_field( 'manual_related_services', $post_id );

	if ( is_array( $manual ) && ! empty( $manual ) ) {
		foreach ( $manual as $related ) {
			if ( $related instanceof WP_Post && 'service' === $related->post_type ) {
				$posts[] = $related;
			}
		}
	}
}

if ( empty( $posts ) ) {
	$posts = shpigovsky_get_service_children( $post_id );
}

if ( empty( $posts ) ) {
	return;
}

$heading = shpigovsky_get_service_hero_title( $post_id );
$lead    = shpigovsky_get_service_field( $post_id, 'intro_text' );

if ( '' === $lead ) {
	$lead = shpigovsky_get_service_field( $post_id, 'hero_lead' );
}

$section_id = 'service-subdivision-dependencies';
$heading_id = 'service-subdivision-dependencies-heading';
?>
<section
	data-reveal
	class="services-category-section-v2 services-category-section-v2--subdivision-dependencies service-subdivision-dependencies-v1"
	id="<?php echo esc_attr( $section_id ); ?>"
	aria-labelledby="<?php echo esc_attr( $heading_id ); ?>"
>
	<div class="container services-category-section-v2__container">
		<h2 class="services-category-section-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
			<?php echo esc_html( $heading ); ?>
		</h2>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-category-section-v2__lead"><?php echo wp_kses_post( $lead ); ?></p>
		<?php endif; ?>

		<div class="services-category-section-v2__services">
			<?php foreach ( $posts as $child ) : ?>
				<?php
				if ( ! $child instanceof WP_Post ) {
					continue;
				}

				$title = get_the_title( $child );
				$url   = get_permalink( $child );

				if ( '' === $title ) {
					continue;
				}
				?>
				<article class="services-category-section-v2__service">
					<div class="services-category-section-v2__service-head">
						<h3 class="services-category-section-v2__service-title">
							<span class="services-category-section-v2__service-name"><?php echo esc_html( $title ); ?></span>
							<span class="services-category-section-v2__service-leader" aria-hidden="true"></span>
						</h3>
						<?php if ( is_string( $url ) && '' !== $url ) : ?>
							<a class="services-category-section-v2__service-link home-rehabilitation-program__all-link" href="<?php echo esc_url( $url ); ?>">
								<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'узнать больше', 'shpigovsky' ); ?></span>
								<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
							</a>
						<?php endif; ?>
					</div>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>

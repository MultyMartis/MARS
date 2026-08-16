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
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
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

$section_id = 'service-subdivision-dependencies';
$heading_id = 'service-subdivision-dependencies-heading';

if ( 'subdivision' === $variant ) {
	// V9-06E50: ACF chrome only — no hardcoded demo when empty. Children list remains automatic.
	$heading = shpigovsky_section_text( $post_id, 'section_dependencies_heading', '' );

	$lead = shpigovsky_get_section_field( $post_id, 'section_dependencies_lead' );

	if ( '' === $lead ) {
		$lead = shpigovsky_get_service_field( $post_id, 'intro_text' );
	}

	if ( '' === $lead ) {
		$lead = shpigovsky_get_service_field( $post_id, 'hero_lead' );
	}

	$footer_text = shpigovsky_section_text( $post_id, 'section_dependencies_footer', '' );
} else {
	$heading     = shpigovsky_get_service_hero_title( $post_id );
	$lead        = shpigovsky_get_service_field( $post_id, 'intro_text' );
	$footer_text = '';

	if ( '' === $lead ) {
		$lead = shpigovsky_get_service_field( $post_id, 'hero_lead' );
	}
}
?>
<section
	data-reveal
	class="services-category-section-v2 services-category-section-v2--subdivision-dependencies service-subdivision-dependencies-v1"
	id="<?php echo esc_attr( $section_id ); ?>"
	aria-labelledby="<?php echo esc_attr( $heading_id ); ?>"
>
	<div class="container services-category-section-v2__container">
		<?php if ( 'subdivision' === $variant ) : ?>
			<header class="services-category-section-v2__head">
				<div class="services-category-section-v2__head-main">
					<span class="services-category-section-v2__marker" aria-hidden="true">01</span>
					<div class="services-category-section-v2__head-copy">
						<h2 class="services-category-section-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
							<?php echo esc_html( $heading ); ?>
						</h2>
						<p class="services-category-section-v2__intro"></p>
					</div>
				</div>
			</header>
		<?php else : ?>
			<h2 class="services-category-section-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php echo esc_html( $heading ); ?>
			</h2>
		<?php endif; ?>

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
							<?php if ( is_string( $url ) && '' !== $url ) : ?>
								<a class="services-category-section-v2__service-name" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
							<?php else : ?>
								<span class="services-category-section-v2__service-name"><?php echo esc_html( $title ); ?></span>
							<?php endif; ?>
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

			<?php if ( 'subdivision' === $variant && '' !== $footer_text ) : ?>
				<p class="service-subdivision-dependencies-v1__footer-text"><?php echo esc_html( $footer_text ); ?></p>
			<?php endif; ?>
		</div>

		<div class="services-category-section-v2__actions">
			<button
				type="button"
				class="btn btn_dark btn--primary services-category-section-v2__cta"
				data-modal-open="consultation"
				data-modal-source="service-child-services"
				data-modal-title="<?php echo esc_attr__( 'Записаться на консультацию', 'shpigovsky' ); ?>"
				data-modal-submit-text="<?php echo esc_attr__( 'Записаться на консультацию', 'shpigovsky' ); ?>"
			>
				<?php echo esc_html__( 'Записаться на консультацию', 'shpigovsky' ); ?>
			</button>
		</div>
	</div>
</section>

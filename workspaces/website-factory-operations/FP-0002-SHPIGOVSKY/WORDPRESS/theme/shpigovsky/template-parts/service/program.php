<?php
/**
 * Template part: service/program.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id   = shpigovsky_get_current_service_id();
$variant   = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$section_id = 'subdivision' === $variant ? 'service-subdivision-program' : 'service-leaf-program';
$heading_id = $section_id . '-heading';
$items     = shpigovsky_get_service_repeater( $post_id, 'programme_items' );

if ( empty( $items ) ) {
	$items = shpigovsky_get_service_programme_fallback_items();
}

$program_url = home_url( '/o-centre/programma-lecheniya/' );
$lead        = shpigovsky_get_service_field( $post_id, 'hero_lead' );
?>
<section data-reveal class="services-program-v2 services-program-v2--play-link services-program-v2--intro-stacked" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container services-program-v2__container">
		<div class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="<?php echo esc_attr( $heading_id ); ?>">
				<?php echo esc_html__( 'Наша программа включает 4 направления', 'shpigovsky' ); ?>
			</h2>
			<a class="home-rehabilitation-program__all-link services-program-v2__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-program-v2__lead"><?php echo wp_kses_post( $lead ); ?></p>
		<?php endif; ?>

		<div class="services-program-v2__grid">
			<?php foreach ( $items as $item ) : ?>
				<?php
				$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

				if ( '' === $title && '' === $text ) {
					continue;
				}
				?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<?php if ( '' !== $title ) : ?>
							<h3 class="services-program-v2__item-title"><?php echo esc_html( $title ); ?></h3>
						<?php endif; ?>
						<?php if ( '' !== $text ) : ?>
							<p class="services-program-v2__item-text"><?php echo wp_kses_post( $text ); ?></p>
						<?php endif; ?>
					</div>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>

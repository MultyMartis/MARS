<?php
/**
 * Template part: service/approach.php
 *
 * Approach cards from programme_items when present.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id   = shpigovsky_get_current_service_id();
$programme = shpigovsky_get_service_repeater( $post_id, 'programme_items' );

if ( empty( $programme ) ) {
	return;
}

$heading     = sprintf(
	/* translators: %s: service title */
	__( 'Наш подход к лечению: %s', 'shpigovsky' ),
	shpigovsky_get_service_hero_title( $post_id )
);
$program_url = home_url( '/o-centre/programma-lecheniya/' );
?>
<section data-reveal class="service-leaf-approach-v1" id="service-leaf-approach" aria-labelledby="service-leaf-approach-heading">
	<div class="container service-leaf-approach-v1__container">
		<div class="service-leaf-approach-v1__head">
			<h2 class="service-leaf-approach-v1__heading" id="service-leaf-approach-heading"><?php echo esc_html( $heading ); ?></h2>
			<a class="home-rehabilitation-program__all-link service-leaf-approach-v1__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<ul class="home-feature-grid__card-grid service-leaf-approach-v1__approach-cards">
			<?php foreach ( $programme as $item ) : ?>
				<?php
				$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

				if ( '' === $title && '' === $text ) {
					continue;
				}
				?>
				<li class="home-feature-grid__card service-leaf-approach-v1__approach-card">
					<?php if ( '' !== $title ) : ?>
						<h3 class="home-feature-grid__card-title"><?php echo esc_html( $title ); ?></h3>
					<?php endif; ?>
					<?php if ( '' !== $text ) : ?>
						<p class="home-feature-grid__card-text"><?php echo wp_kses_post( $text ); ?></p>
					<?php endif; ?>
				</li>
			<?php endforeach; ?>
		</ul>
	</div>
</section>

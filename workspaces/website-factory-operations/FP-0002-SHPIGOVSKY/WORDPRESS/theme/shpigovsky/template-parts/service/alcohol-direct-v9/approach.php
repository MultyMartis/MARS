<?php
/**
 * Direct V9 port: service-leaf-approach-v1 (usluga-konechnaya-v1.html).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$v9          = shpigovsky_get_v9_alcohol_leaf_approach_copy();
$program_url = home_url( '/o-centre/programma-lecheniya/' );
$staff_image = shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-staff-group.webp' );
?>
<section data-reveal class="service-leaf-approach-v1" id="service-leaf-approach" aria-labelledby="service-leaf-approach-heading">
	<div class="container service-leaf-approach-v1__container">
		<div class="service-leaf-approach-v1__head">
			<h2 class="service-leaf-approach-v1__heading" id="service-leaf-approach-heading"><?php echo esc_html( $v9['heading'] ); ?></h2>
			<a class="home-rehabilitation-program__all-link service-leaf-approach-v1__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<p class="service-leaf-approach-v1__highlight block-whith-red-line"><?php echo esc_html( $v9['highlight'] ); ?></p>

		<p class="service-leaf-approach-v1__intro"><?php echo esc_html( $v9['intro'] ); ?></p>

		<div class="service-leaf-approach-v1__staff-bleed">
			<img
				class="service-leaf-approach-v1__staff-image"
				src="<?php echo esc_url( $staff_image ); ?>"
				width="1139"
				height="443"
				alt="<?php esc_attr_e( 'Команда специалистов реабилитационного центра', 'shpigovsky' ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>

		<ul class="home-feature-grid__card-grid service-leaf-approach-v1__approach-cards">
			<?php foreach ( $v9['cards'] as $card ) : ?>
				<li class="home-feature-grid__card service-leaf-approach-v1__approach-card">
					<h3 class="home-feature-grid__card-title"><?php echo esc_html( $card['title'] ); ?></h3>
					<p class="home-feature-grid__card-text"><?php echo esc_html( $card['text'] ); ?></p>
				</li>
			<?php endforeach; ?>
		</ul>
	</div>
</section>

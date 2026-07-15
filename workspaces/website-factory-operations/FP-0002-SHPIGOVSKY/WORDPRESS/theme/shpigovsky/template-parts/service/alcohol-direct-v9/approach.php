<?php
/**
 * Service-leaf approach — ACF SoT (V9-06E47); visual parity with usluga-konechnaya-v1.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$v9      = function_exists( 'shpigovsky_get_general_approach_copy' )
	? shpigovsky_get_general_approach_copy( $post_id )
	: null;

if ( ! is_array( $v9 ) || empty( $v9['cards'] ) ) {
	return;
}

$program_url = ! empty( $v9['more_url'] ) ? (string) $v9['more_url'] : home_url( '/o-centre/programma-lecheniya/' );
$more_label  = ! empty( $v9['more_label'] ) ? (string) $v9['more_label'] : __( 'подробнее', 'shpigovsky' );
$staff_alt   = shpigovsky_get_general_field( $post_id, 'service_general_team_image_alt' );
$staff_alt   = '' !== $staff_alt ? $staff_alt : __( 'Команда специалистов реабилитационного центра', 'shpigovsky' );
$staff       = function_exists( 'shpigovsky_general_image_or_asset' )
	? shpigovsky_general_image_or_asset(
		$post_id,
		'service_general_team_image',
		'img/content/pre-reviews/shpigovsky-staff-group.webp',
		$staff_alt,
		1139,
		443
	)
	: array(
		'url'    => shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-staff-group.webp' ),
		'alt'    => $staff_alt,
		'width'  => 1139,
		'height' => 443,
	);
?>
<section data-reveal class="service-leaf-approach-v1" id="service-leaf-approach" aria-labelledby="service-leaf-approach-heading">
	<div class="container service-leaf-approach-v1__container">
		<div class="service-leaf-approach-v1__head">
			<h2 class="service-leaf-approach-v1__heading" id="service-leaf-approach-heading"><?php echo esc_html( $v9['heading'] ); ?></h2>
			<a class="home-rehabilitation-program__all-link service-leaf-approach-v1__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html( $more_label ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<?php if ( ! empty( $v9['highlight'] ) ) : ?>
			<p class="service-leaf-approach-v1__highlight block-whith-red-line"><?php echo esc_html( $v9['highlight'] ); ?></p>
		<?php endif; ?>

		<?php if ( ! empty( $v9['intro'] ) ) : ?>
			<p class="service-leaf-approach-v1__intro"><?php echo esc_html( $v9['intro'] ); ?></p>
		<?php endif; ?>

		<?php if ( ! empty( $staff['url'] ) ) : ?>
			<div class="service-leaf-approach-v1__staff-bleed">
				<img
					class="service-leaf-approach-v1__staff-image"
					src="<?php echo esc_url( $staff['url'] ); ?>"
					width="<?php echo esc_attr( (string) $staff['width'] ); ?>"
					height="<?php echo esc_attr( (string) $staff['height'] ); ?>"
					alt="<?php echo esc_attr( $staff['alt'] ); ?>"
					loading="lazy"
					decoding="async"
				>
			</div>
		<?php endif; ?>

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

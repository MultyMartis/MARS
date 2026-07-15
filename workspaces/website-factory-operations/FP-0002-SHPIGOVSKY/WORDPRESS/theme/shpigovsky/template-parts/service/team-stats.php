<?php
/**
 * Template part: service/team-stats.php
 *
 * Service subdivision approach/team block — ACF SoT (V9-06E50).
 * Emergency theme-asset image reserve only when section image fields are empty.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();

$program_url = shpigovsky_get_section_field( $post_id, 'section_approach_more_url' );
if ( '' === $program_url ) {
	$program_url = home_url( '/o-centre/programma-lecheniya/' );
}

$heading   = shpigovsky_section_text( $post_id, 'section_approach_heading', '' );
$more      = shpigovsky_section_text( $post_id, 'section_approach_more_label', '' );
$highlight = shpigovsky_section_text( $post_id, 'section_approach_highlight', '' );
$intro     = shpigovsky_section_text( $post_id, 'section_approach_intro', '' );

$corridor_alt = shpigovsky_section_text( $post_id, 'section_corridor_image_alt', '' );
if ( '' === $corridor_alt ) {
	$corridor_alt = shpigovsky_section_text( $post_id, 'section_approach_corridor_alt', '' );
}
if ( '' === $corridor_alt ) {
	$corridor_alt = __( 'Интерьер клиники — коридор с картинами', 'shpigovsky' );
}
$corridor = function_exists( 'shpigovsky_section_image_or_asset_prefer' )
	? shpigovsky_section_image_or_asset_prefer(
		$post_id,
		array( 'section_corridor_image', 'section_approach_corridor_image' ),
		'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp',
		$corridor_alt,
		2187,
		1231
	)
	: shpigovsky_section_image_or_asset(
		$post_id,
		'section_corridor_image',
		'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp',
		$corridor_alt,
		2187,
		1231
	);

$staff_alt = shpigovsky_section_text( $post_id, 'section_team_image_alt', '' );
if ( '' === $staff_alt ) {
	$staff_alt = shpigovsky_section_text( $post_id, 'section_approach_staff_alt', '' );
}
if ( '' === $staff_alt ) {
	$staff_alt = __( 'Команда специалистов реабилитационного центра', 'shpigovsky' );
}
$staff = function_exists( 'shpigovsky_section_image_or_asset_prefer' )
	? shpigovsky_section_image_or_asset_prefer(
		$post_id,
		array( 'section_team_image', 'section_approach_staff_image' ),
		'img/content/pre-reviews/shpigovsky-staff-group.webp',
		$staff_alt,
		1139,
		443
	)
	: shpigovsky_section_image_or_asset(
		$post_id,
		'section_team_image',
		'img/content/pre-reviews/shpigovsky-staff-group.webp',
		$staff_alt,
		1139,
		443
	);

$cards = shpigovsky_section_normalize_title_text_rows( shpigovsky_get_section_field_raw( $post_id, 'section_approach_cards' ) );
?>
<section data-reveal class="service-subdivision-team-stats-v1" id="service-subdivision-approach" aria-labelledby="service-subdivision-approach-heading">
	<div class="container service-subdivision-team-stats-v1__container">
		<div class="service-subdivision-team-stats-v1__corridor-bleed">
			<img
				class="service-subdivision-team-stats-v1__corridor-image"
				src="<?php echo esc_url( $corridor['url'] ); ?>"
				width="<?php echo esc_attr( (string) $corridor['width'] ); ?>"
				height="<?php echo esc_attr( (string) $corridor['height'] ); ?>"
				alt="<?php echo esc_attr( $corridor['alt'] ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>

		<div class="service-subdivision-team-stats-v1__head">
			<?php if ( '' !== $heading ) : ?>
				<h2 class="service-subdivision-team-stats-v1__heading" id="service-subdivision-approach-heading"><?php echo esc_html( $heading ); ?></h2>
			<?php else : ?>
				<h2 class="service-subdivision-team-stats-v1__heading screen-reader-text" id="service-subdivision-approach-heading"><?php esc_html_e( 'Подход', 'shpigovsky' ); ?></h2>
			<?php endif; ?>
			<?php if ( '' !== $more ) : ?>
				<a class="home-rehabilitation-program__all-link service-subdivision-team-stats-v1__all-link" href="<?php echo esc_url( $program_url ); ?>">
					<span class="home-rehabilitation-program__all-text"><?php echo esc_html( $more ); ?></span>
					<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
				</a>
			<?php endif; ?>
		</div>

		<?php if ( '' !== $highlight ) : ?>
			<p class="service-subdivision-team-stats-v1__highlight block-whith-red-line">
				<?php echo esc_html( $highlight ); ?>
			</p>
		<?php endif; ?>

		<?php if ( '' !== $intro ) : ?>
			<p class="service-subdivision-team-stats-v1__intro">
				<?php echo esc_html( $intro ); ?>
			</p>
		<?php endif; ?>

		<div class="service-subdivision-team-stats-v1__staff-bleed">
			<img
				class="service-subdivision-team-stats-v1__staff-image"
				src="<?php echo esc_url( $staff['url'] ); ?>"
				width="<?php echo esc_attr( (string) $staff['width'] ); ?>"
				height="<?php echo esc_attr( (string) $staff['height'] ); ?>"
				alt="<?php echo esc_attr( $staff['alt'] ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>

		<?php if ( ! empty( $cards ) ) : ?>
			<ul class="home-feature-grid__card-grid service-subdivision-team-stats-v1__approach-cards">
				<?php foreach ( $cards as $card ) : ?>
					<li class="home-feature-grid__card service-subdivision-team-stats-v1__approach-card">
						<h3 class="home-feature-grid__card-title"><?php echo esc_html( $card['title'] ); ?></h3>
						<p class="home-feature-grid__card-text"><?php echo esc_html( $card['text'] ); ?></p>
					</li>
				<?php endforeach; ?>
			</ul>
		<?php endif; ?>
	</div>
</section>

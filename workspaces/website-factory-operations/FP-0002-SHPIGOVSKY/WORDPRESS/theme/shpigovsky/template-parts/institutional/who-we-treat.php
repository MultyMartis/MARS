<?php
/**
 * Template part: institutional/who-we-treat.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_is_about_hub_page() ) {
	return;
}

$page_id = (int) get_queried_object_id();
$context = shpigovsky_get_about_who_we_treat_context( $page_id );
$staff   = shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-staff-group.webp' );
?>
<section data-reveal class="services-category-section-v2 services-category-section-v2--addictions services-category-section-v2--o-centre-who-we-treat" id="who-we-treat" aria-labelledby="who-we-treat-heading">
	<div class="container services-category-section-v2__container">
		<header class="services-category-section-v2__head">
			<div class="services-category-section-v2__head-main">
				<div class="services-category-section-v2__head-copy">
					<h2 class="services-category-section-v2__heading" id="who-we-treat-heading"><?php echo esc_html( $context['heading'] ); ?></h2>
					<p class="services-category-section-v2__intro"><?php echo esc_html( $context['intro'] ); ?></p>
				</div>
			</div>
		</header>

		<p class="services-category-section-v2__lead"><?php echo esc_html( $context['lead'] ); ?></p>

		<div class="services-category-section-v2__body">
			<ul class="who-we-treat-visual__spectrum-list">
				<?php foreach ( $context['spectrum'] as $item ) : ?>
					<?php
					$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
					$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

					if ( '' === $title && '' === $text ) {
						continue;
					}
					?>
					<li class="who-we-treat-visual__spectrum-item">
						<?php if ( '' !== $title ) : ?>
							<strong class="who-we-treat-visual__spectrum-title"><?php echo esc_html( $title ); ?></strong>
						<?php endif; ?>
						<?php echo esc_html( $text ); ?>
					</li>
				<?php endforeach; ?>
			</ul>
			<p class="who-we-treat-visual__callout"><?php echo esc_html( $context['callout'] ); ?></p>
			<a class="home-rehabilitation-program__all-link who-we-treat-visual__more-link" href="<?php echo esc_url( home_url( '/uslugi/' ) ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php esc_html_e( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<div class="services-category-section-v2__gallery">
			<div class="who-we-treat-visual">
				<div class="who-we-treat-visual__staff-bleed">
					<img class="who-we-treat-visual__staff-image" src="<?php echo esc_url( $staff ); ?>" width="1139" height="443" alt="<?php esc_attr_e( 'Команда специалистов реабилитационного центра', 'shpigovsky' ); ?>" loading="lazy" decoding="async">
				</div>
				<ul class="home-feature-grid__card-grid who-we-treat-visual__cards">
					<?php foreach ( $context['cards'] as $card ) : ?>
						<?php
						$card_title = isset( $card['title'] ) ? trim( (string) $card['title'] ) : '';
						$card_text  = isset( $card['text'] ) ? trim( (string) $card['text'] ) : '';

						if ( '' === $card_title && '' === $card_text ) {
							continue;
						}
						?>
						<li class="home-feature-grid__card who-we-treat-visual__card">
							<h3 class="home-feature-grid__card-title"><?php echo esc_html( $card_title ); ?></h3>
							<p class="home-feature-grid__card-text"><?php echo esc_html( $card_text ); ?></p>
						</li>
					<?php endforeach; ?>
				</ul>
			</div>
		</div>
	</div>
</section>

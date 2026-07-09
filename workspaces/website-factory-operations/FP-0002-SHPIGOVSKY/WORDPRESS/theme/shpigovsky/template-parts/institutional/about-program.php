<?php
/**
 * Template part: institutional/about-program.php
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
$context = shpigovsky_get_about_program_context( $page_id );
?>
<section data-reveal class="services-program-v2 services-program-v2--play-link services-program-v2--intro-stacked services-program-v2--title-flush services-program-v2--item-body-spaced services-program-v2--item-image-stack-tall services-program-v2--media-frame-fixed services-program-v2--o-centre-program" id="our-program" aria-labelledby="our-program-heading">
	<div class="container services-program-v2__container">
		<header class="services-program-v2__head">
			<h2 class="services-program-v2__heading" id="our-program-heading"><?php echo esc_html( $context['heading'] ); ?></h2>
			<a class="home-rehabilitation-program__all-link services-program-v2__all-link" href="<?php echo esc_url( $context['link_url'] ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php esc_html_e( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</header>

		<?php if ( '' !== $context['lead'] ) : ?>
			<p class="services-program-v2__lead"><?php echo esc_html( $context['lead'] ); ?></p>
		<?php endif; ?>

		<?php if ( '' !== $context['intro'] ) : ?>
			<p class="services-program-v2__intro"><?php echo esc_html( $context['intro'] ); ?></p>
		<?php endif; ?>

		<?php if ( '' !== $context['intro2'] ) : ?>
			<p class="services-program-v2__intro services-program-v2__intro--secondary"><?php echo esc_html( $context['intro2'] ); ?></p>
		<?php endif; ?>

		<div class="services-program-v2__grid">
			<?php foreach ( $context['items'] as $item ) : ?>
				<article class="services-program-v2__item">
					<div class="services-program-v2__item-body">
						<h3 class="services-program-v2__item-title"><?php echo esc_html( $item['title'] ); ?></h3>
					</div>
					<div class="services-program-v2__item-media">
						<img
							class="services-program-v2__item-image"
							src="<?php echo esc_url( $item['image'] ); ?>"
							width="<?php echo (int) $item['width']; ?>"
							height="<?php echo (int) $item['height']; ?>"
							alt="<?php echo esc_attr( $item['alt'] ); ?>"
							loading="lazy"
							decoding="async"
						>
					</div>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>

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

		<?php
		// Nested inside #who-we-treat <section>: use visual band <div>, not nested <section>.
		$who_we_treat_cta                 = shpigovsky_get_about_guest_cta_band( 'o-centre-who-we-treat-cta' );
		$who_we_treat_cta['wrap_section'] = false;
		set_query_var( 'shpigovsky_program_cta_band', $who_we_treat_cta );
		get_template_part( 'template-parts/components/program-cta-band' );
		?>
	</div>
</section>
